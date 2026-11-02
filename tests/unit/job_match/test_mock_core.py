import json
from pathlib import Path

import pytest

from app.messaging.mock_core import MockCoreRpc


@pytest.fixture
def mock_core():
    return MockCoreRpc()


@pytest.mark.asyncio
async def test_search_filters_like_project_specification(mock_core):
    # Default search: returns OPEN projects with RECRUITING jobs
    res = await mock_core.call("core.project.search", {"page": 0, "size": 50})
    assert res["ok"] is True
    projects = res["data"]["data"]
    for p in projects:
        assert p["status"] == "OPEN"
        recruiting_jobs = [j for j in p.get("jobs", []) if j.get("status") == "RECRUITING"]
        assert len(recruiting_jobs) > 0

    # Keyword search (accent & case-insensitive)
    kw_res = await mock_core.call(
        "core.project.search", {"keyword": "react", "page": 0, "size": 10}
    )
    assert kw_res["ok"] is True
    kw_projects = kw_res["data"]["data"]
    assert len(kw_projects) > 0
    for p in kw_projects:
        content = (p["title"] + " " + p["description"] + " " + str(p.get("jobs", []))).lower()
        assert "react" in content

    # Experience level filter
    exp_res = await mock_core.call(
        "core.project.search", {"experienceLevel": "EXPERT", "page": 0, "size": 10}
    )
    assert exp_res["ok"] is True
    for p in exp_res["data"]["data"]:
        assert p["experienceLevel"] == "EXPERT"

    # Period filter
    period_res = await mock_core.call(
        "core.project.search", {"period": "MONTHLY", "page": 0, "size": 10}
    )
    assert period_res["ok"] is True
    for p in period_res["data"]["data"]:
        assert p["period"] == "MONTHLY"

    # Skills filter
    skill_res = await mock_core.call(
        "core.project.search", {"skills": ["Spring Boot"], "page": 0, "size": 10}
    )
    assert skill_res["ok"] is True
    for p in skill_res["data"]["data"]:
        all_skills = [s.lower() for j in p.get("jobs", []) for s in j.get("skills", [])]
        assert "spring boot" in all_skills


@pytest.mark.asyncio
async def test_get_returns_any_status_and_not_found(mock_core):
    # Returns OPEN project
    open_res = await mock_core.call(
        "core.project.get", {"projectId": "a1000000-0000-0000-0000-000000000001"}
    )
    assert open_res["ok"] is True
    assert open_res["data"]["data"]["id"] == "a1000000-0000-0000-0000-000000000001"

    # Returns CLOSED project p14
    closed_res = await mock_core.call(
        "core.project.get", {"projectId": "a1000000-0000-0000-0000-000000000014"}
    )
    assert closed_res["ok"] is True
    assert closed_res["data"]["data"]["status"] == "CLOSED"

    # Not found
    nf_res = await mock_core.call(
        "core.project.get", {"projectId": "00000000-0000-0000-0000-000000000000"}
    )
    assert nf_res["ok"] is False
    assert nf_res["error"]["code"] == "PROJECT_NOT_FOUND"


@pytest.mark.asyncio
async def test_mock_returns_rpcclient_envelope(mock_core):
    res = await mock_core.call("core.project.search", {"page": 0, "size": 5})
    assert isinstance(res, dict)
    assert "ok" in res
    assert res["ok"] is True
    assert "data" in res
    data = res["data"]
    assert "statusCode" in data
    assert data["statusCode"] == 200
    assert "message" in data
    assert "data" in data
    assert "paging" in data


@pytest.mark.asyncio
async def test_get_overlay(monkeypatch):
    overlay_fixture = Path("tests/fixtures/job_match/get_overlay.json").resolve()
    monkeypatch.setenv("CORE_MOCK_GET_OVERLAY", str(overlay_fixture))

    rpc = MockCoreRpc()
    # p03 is a1000000-0000-0000-0000-000000000003
    p03_res = await rpc.call(
        "core.project.get", {"projectId": "a1000000-0000-0000-0000-000000000003"}
    )
    assert p03_res["ok"] is True
    proj = p03_res["data"]["data"]
    assert proj["status"] == "CLOSED"
    j0301 = next(j for j in proj["jobs"] if j["id"] == "b1000000-0000-0000-0000-000000000301")
    assert j0301["status"] == "FILLED"


def test_fixture_equals_app_mock_json():
    fixture_path = Path("tests/fixtures/job_match/core_projects.json")
    app_mock_path = Path("app/features/job_match/mock/core_projects.json")

    assert fixture_path.exists(), "tests/fixtures/job_match/core_projects.json missing"
    assert app_mock_path.exists(), "app/features/job_match/mock/core_projects.json missing"

    with open(fixture_path, encoding="utf-8") as f1, open(app_mock_path, encoding="utf-8") as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)

    assert d1 == d2, (
        "Fixture core_projects.json must match app/features/job_match/mock/core_projects.json"
    )
