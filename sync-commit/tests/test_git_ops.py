"""Tests for local Git operations and patch management."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest
from sync_engine.git_ops import (
    apply_patch_or_commit,
    calculate_patch,
    clone_or_fetch,
    create_branch,
    ensure_clean_working_tree,
    get_head_sha,
    is_ancestor,
    is_clean_working_tree,
)


@pytest.fixture
def git_repo(tmp_path: Path) -> Path:
    """Create a temporary git repository with initial commit."""
    repo_dir = tmp_path / "test_repo"
    repo_dir.mkdir()

    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = "Initial Author"
    env["GIT_AUTHOR_EMAIL"] = "initial@example.com"
    env["GIT_COMMITTER_NAME"] = "Initial Committer"
    env["GIT_COMMITTER_EMAIL"] = "committer@example.com"

    subprocess.run(["git", "init", "-b", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "config", "user.name", "Initial Author"], cwd=repo_dir, check=True)
    subprocess.run(["git", "config", "user.email", "initial@example.com"], cwd=repo_dir, check=True)

    test_file = repo_dir / "README.md"
    test_file.write_text("# Project Occupify\n")

    subprocess.run(["git", "add", "README.md"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo_dir, env=env, check=True)

    return repo_dir


def test_get_head_sha(git_repo: Path) -> None:
    sha = get_head_sha(str(git_repo), branch="main")
    assert isinstance(sha, str)
    assert len(sha) == 40


def test_create_branch_and_is_ancestor(git_repo: Path) -> None:
    initial_sha = get_head_sha(str(git_repo), branch="main")

    # Create new branch
    create_branch(str(git_repo), "feature-sync", start_point="main")

    # Make commit on feature-sync
    new_file = git_repo / "feature.py"
    new_file.write_text("print('hello world')\n")
    subprocess.run(["git", "add", "feature.py"], cwd=git_repo, check=True)
    subprocess.run(["git", "commit", "-m", "Add feature"], cwd=git_repo, check=True)

    feature_sha = get_head_sha(str(git_repo), branch="feature-sync")

    assert initial_sha != feature_sha
    # initial_sha should be ancestor of feature-sync
    assert is_ancestor(str(git_repo), ancestor_sha=initial_sha, descendant_sha=feature_sha) is True
    # feature_sha should NOT be ancestor of initial_sha
    assert is_ancestor(str(git_repo), ancestor_sha=feature_sha, descendant_sha=initial_sha) is False


def test_calculate_patch(git_repo: Path) -> None:
    initial_sha = get_head_sha(str(git_repo), branch="main")

    new_file = git_repo / "new_service.py"
    new_file.write_text("def service():\n    return 'OK'\n")
    subprocess.run(["git", "add", "new_service.py"], cwd=git_repo, check=True)
    subprocess.run(["git", "commit", "-m", "feat: new service"], cwd=git_repo, check=True)

    head_sha = get_head_sha(str(git_repo), branch="main")

    patch = calculate_patch(str(git_repo), base_sha=initial_sha, head_sha=head_sha)
    assert "diff --git" in patch
    assert "new_service.py" in patch
    assert "+def service():" in patch


def test_apply_patch_or_commit_preserves_attribution(git_repo: Path, tmp_path: Path) -> None:
    # 1. Create a change in git_repo
    initial_sha = get_head_sha(str(git_repo), branch="main")
    hello_file = git_repo / "hello.txt"
    hello_file.write_text("Hello Sync Engine\n")
    subprocess.run(["git", "add", "hello.txt"], cwd=git_repo, check=True)
    subprocess.run(["git", "commit", "-m", "Add hello"], cwd=git_repo, check=True)
    head_sha = get_head_sha(str(git_repo), branch="main")

    patch = calculate_patch(str(git_repo), initial_sha, head_sha)

    # 2. Clone repo to target destination
    target_repo = tmp_path / "dest_repo"
    clone_or_fetch(str(git_repo), str(target_repo), branch="main")

    # 3. Create sync branch
    create_branch(str(target_repo), "sync/test-pr", start_point="main")
    # Reset target branch to initial commit so the patch can apply
    subprocess.run(["git", "reset", "--hard", initial_sha], cwd=target_repo, check=True)

    # 4. Apply patch with author metadata and co-authors
    author_name = "Alice Contributor"
    author_email = "alice@contributor.org"
    author_date = "2026-11-05T09:30:00+07:00"
    commit_msg = "feat(hello): add greeting file"
    co_authors = [("Bob Reviewer", "bob@reviewer.org")]

    success, err = apply_patch_or_commit(
        repo_dir=str(target_repo),
        patch_text=patch,
        author_name=author_name,
        author_email=author_email,
        author_date=author_date,
        commit_message=commit_msg,
        co_authors=co_authors,
    )

    assert success is True
    assert err is None

    # Verify commit metadata
    log_author = subprocess.run(
        ["git", "log", "-1", "--format=%an <%ae>"],
        cwd=target_repo,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    assert log_author == f"{author_name} <{author_email}>"

    log_body = subprocess.run(
        ["git", "log", "-1", "--format=%B"],
        cwd=target_repo,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    assert "feat(hello): add greeting file" in log_body
    assert "Co-authored-by: Bob Reviewer <bob@reviewer.org>" in log_body


def test_apply_patch_conflict_handling(git_repo: Path, tmp_path: Path) -> None:
    # 1. Modify README in git_repo
    initial_sha = get_head_sha(str(git_repo), branch="main")
    readme = git_repo / "README.md"
    readme.write_text("# Project Occupify\nVersion 1.0\nLine from source.\n")
    subprocess.run(["git", "add", "README.md"], cwd=git_repo, check=True)
    subprocess.run(["git", "commit", "-m", "Update readme on source"], cwd=git_repo, check=True)
    head_sha = get_head_sha(str(git_repo), branch="main")

    patch = calculate_patch(str(git_repo), initial_sha, head_sha)

    # 2. Clone repo to destination
    target_repo = tmp_path / "dest_repo_conflict"
    clone_or_fetch(str(git_repo), str(target_repo), branch="main")
    subprocess.run(["git", "reset", "--hard", initial_sha], cwd=target_repo, check=True)

    # 3. Create incompatible change in destination README
    dest_readme = target_repo / "README.md"
    dest_readme.write_text("# Incompatible Occupify Header\nCompletely different content.\n")
    subprocess.run(["git", "add", "README.md"], cwd=target_repo, check=True)
    subprocess.run(["git", "commit", "-m", "Conflicting local commit"], cwd=target_repo, check=True)

    # 4. Attempt to apply patch
    success, err = apply_patch_or_commit(
        repo_dir=str(target_repo),
        patch_text=patch,
        author_name="Alice Contributor",
        author_email="alice@contributor.org",
        author_date="2026-11-05T09:30:00Z",
        commit_message="Update readme",
    )

    # Should detect conflict and abort cleanly
    assert success is False
    assert err is not None
    assert is_clean_working_tree(str(target_repo)) is True


def test_clean_working_tree_functions(git_repo: Path) -> None:
    # Initially clean
    assert is_clean_working_tree(str(git_repo)) is True
    assert ensure_clean_working_tree(str(git_repo)) is True

    # Make working tree dirty
    dirty_file = git_repo / "untracked.tmp"
    dirty_file.write_text("dirty content")

    assert is_clean_working_tree(str(git_repo)) is False

    # ensure_clean_working_tree should clean it up
    cleaned = ensure_clean_working_tree(str(git_repo))
    assert cleaned is True
    assert is_clean_working_tree(str(git_repo)) is True
    assert not dirty_file.exists()
