"""Tests for GitHub REST API client."""

from __future__ import annotations

import httpx
import pytest
import respx
from sync_engine.github_client import (
    GitHubClient,
    GitHubRateLimitError,
    GitHubResourceNotFoundError,
)


@pytest.fixture
def client() -> GitHubClient:
    return GitHubClient(token="test-secret-token", max_retries=2, backoff_factor=0.01)


@respx.mock
def test_headers_and_auth(client: GitHubClient) -> None:
    route = respx.get("https://api.github.com/user").respond(200, json={"login": "testbot"})
    resp = client._request("GET", "/user")
    assert resp.status_code == 200
    assert route.called
    req = route.calls.last.request
    assert req.headers["authorization"] == "Bearer test-secret-token"
    assert req.headers["accept"] == "application/vnd.github+json"
    assert req.headers["x-github-api-version"] == "2022-11-28"


@respx.mock
def test_get_closed_prs(client: GitHubClient) -> None:
    mock_data = [
        {"number": 101, "title": "Feat A", "state": "closed", "merged_at": "2026-11-01T10:00:00Z"},
        {"number": 102, "title": "Fix B", "state": "closed", "merged_at": None},
    ]
    respx.get("https://api.github.com/repos/test-org/repo-b/pulls").respond(200, json=mock_data)

    prs = client.get_closed_prs("test-org", "repo-b", base_branch="main")
    assert len(prs) == 2
    assert prs[0]["number"] == 101
    assert prs[1]["title"] == "Fix B"


@respx.mock
def test_get_pr_details(client: GitHubClient) -> None:
    respx.get("https://api.github.com/repos/test-org/repo-b/pulls/42").respond(
        200,
        json={
            "number": 42,
            "title": "Add Agent Core",
            "merged": True,
            "merge_commit_sha": "abc1234",
        },
    )

    details = client.get_pr_details("test-org", "repo-b", 42)
    assert details["number"] == 42
    assert details["merge_commit_sha"] == "abc1234"
    assert details["merged"] is True


@respx.mock
def test_get_pr_commits(client: GitHubClient) -> None:
    mock_commits = [
        {
            "sha": "c1a2b3c4d5",
            "commit": {
                "message": "feat: initialize sync engine",
                "author": {
                    "name": "Jane Developer",
                    "email": "jane@example.com",
                    "date": "2026-11-02T12:00:00Z",
                },
                "committer": {
                    "name": "GitHub Web",
                    "email": "noreply@github.com",
                    "date": "2026-11-02T12:00:00Z",
                },
            },
            "author": {"login": "janedev"},
            "committer": {"login": "web-flow"},
        }
    ]
    respx.get("https://api.github.com/repos/test-org/repo-b/pulls/10/commits").respond(
        200, json=mock_commits
    )

    commits = client.get_pr_commits("test-org", "repo-b", 10)
    assert len(commits) == 1
    c = commits[0]
    assert c["sha"] == "c1a2b3c4d5"
    assert c["message"] == "feat: initialize sync engine"
    assert c["author_name"] == "Jane Developer"
    assert c["author_email"] == "jane@example.com"
    assert c["author_date"] == "2026-11-02T12:00:00Z"
    assert c["author_login"] == "janedev"
    assert c["committer_info"]["name"] == "GitHub Web"


@respx.mock
def test_get_pr_files(client: GitHubClient) -> None:
    mock_files = [
        {"filename": "app/main.py", "status": "modified"},
        {"filename": "sync-commit/sync_engine/git_ops.py", "status": "added"},
    ]
    respx.get("https://api.github.com/repos/test-org/repo-b/pulls/15/files").respond(
        200, json=mock_files
    )

    files = client.get_pr_files("test-org", "repo-b", 15)
    assert files == ["app/main.py", "sync-commit/sync_engine/git_ops.py"]


@respx.mock
def test_check_pr_merged_status_codes(client: GitHubClient) -> None:
    # Test merged = True (204 No Content)
    respx.get("https://api.github.com/repos/test-org/repo-b/pulls/20/merge").respond(204)
    assert client.check_pr_merged("test-org", "repo-b", 20) is True

    # Test merged = False (404 Not Found)
    respx.get("https://api.github.com/repos/test-org/repo-b/pulls/21/merge").respond(404)
    assert client.check_pr_merged("test-org", "repo-b", 21) is False


@respx.mock
def test_create_pull_request(client: GitHubClient) -> None:
    route = respx.post("https://api.github.com/repos/Occupify/occupify-agentic/pulls").respond(
        201,
        json={"number": 77, "html_url": "https://github.com/Occupify/occupify-agentic/pull/77"},
    )

    created = client.create_pull_request(
        owner="Occupify",
        repo="occupify-agentic",
        title="Sync: PR #25 from Source",
        head_branch="sync/b/pr-25",
        base_branch="main",
        body="Automated sync of contributions.",
    )
    assert created["number"] == 77
    assert route.called
    payload = route.calls.last.request.read().decode("utf-8")
    assert "sync/b/pr-25" in payload
    assert "Automated sync of contributions." in payload


@respx.mock
def test_retry_on_rate_limit_and_success(client: GitHubClient) -> None:
    route = respx.get("https://api.github.com/repos/test-org/repo/pulls/1")
    route.side_effect = [
        httpx.Response(429, headers={"Retry-After": "0"}),
        httpx.Response(200, json={"number": 1, "state": "open"}),
    ]

    res = client.get_pr_details("test-org", "repo", 1)
    assert res["number"] == 1
    assert route.call_count == 2


@respx.mock
def test_rate_limit_exhausted_raises_error() -> None:
    client = GitHubClient(token="token", max_retries=1, backoff_factor=0.01)
    respx.get("https://api.github.com/repos/test-org/repo/pulls/1").respond(429)

    with pytest.raises(GitHubRateLimitError):
        client.get_pr_details("test-org", "repo", 1)


@respx.mock
def test_404_raises_resource_not_found(client: GitHubClient) -> None:
    respx.get("https://api.github.com/repos/test-org/repo/pulls/999").respond(404, text="Not Found")

    with pytest.raises(GitHubResourceNotFoundError):
        client.get_pr_details("test-org", "repo", 999)
