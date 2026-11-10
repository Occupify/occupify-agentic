"""Unit and integration tests for SyncEngine."""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from sync_engine import config, db
from sync_engine.engine import SyncEngine, parse_repo_owner_name
from sync_engine.models import ContributionRecord


@pytest.fixture(autouse=True)
def setup_isolated_db(tmp_path, monkeypatch):
    """Provide an isolated SQLite database for each test."""
    db_file = tmp_path / "engine_test.db"
    db_url = f"sqlite:///{db_file}"
    monkeypatch.setenv("DATABASE_URL", db_url)
    monkeypatch.setenv("SYNC_DATABASE_URL", db_url)
    config.get_settings.cache_clear()
    db.init_db(db_url)
    yield db_url
    db._engine = None
    db._sessionmaker = None


@pytest.fixture
def mock_git_ops():
    """Mock GitOps instance."""
    mock = MagicMock()
    mock.ensure_clean_working_tree.return_value = True
    mock.get_head_sha.return_value = "source_head_sha_12345"
    mock.calculate_patch.return_value = "diff --git a/test.py b/test.py\n+print('hello')\n"
    mock.apply_patch_or_commit.return_value = (True, None)
    return mock


@pytest.fixture
def mock_github_client():
    """Mock GitHubClient instance."""
    mock = MagicMock()
    mock.get_closed_prs.return_value = []
    mock.get_pr_details.return_value = {"merged": True, "state": "closed"}
    mock.get_pr_commits.return_value = [
        {
            "sha": "commit_111",
            "message": "Add payment gateway",
            "author_name": "Alice Smith",
            "author_email": "alice@example.com",
            "author_date": "2026-11-10T00:00:00Z",
            "author_login": "alicesmith",
        }
    ]
    mock.get_pr_files.return_value = ["src/Payment.java"]
    mock.create_pull_request.return_value = {
        "number": 101,
        "html_url": "https://github.com/Occupify/occupify-agentic/pull/101",
        "title": "[Sync] #25: Feature payment",
    }
    return mock


def test_parse_repo_owner_name():
    """Verify repository owner and repo extraction across URL formats."""
    # HTTPS
    assert parse_repo_owner_name("https://github.com/se373agenticengineering/nhom-01.git") == (
        "se373agenticengineering",
        "nhom-01",
    )
    assert parse_repo_owner_name("https://github.com/Occupify/occupify-agentic") == (
        "Occupify",
        "occupify-agentic",
    )
    # SSH
    assert parse_repo_owner_name("git@github.com:Occupify/occupify-agentic.git") == (
        "Occupify",
        "occupify-agentic",
    )
    # Short
    assert parse_repo_owner_name("Occupify/occupify-agentic") == ("Occupify", "occupify-agentic")

    # Invalid
    with pytest.raises(ValueError):
        parse_repo_owner_name("invalid_url_without_slashes")


def test_stage1_checkout_source(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 1: Checkout Source clones repo, verifies clean state, returns HEAD SHA."""
    cfg = config.SyncConfig(DRY_RUN=True)
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    head_sha = engine.stage1_checkout_source()
    assert head_sha == "source_head_sha_12345"
    mock_git_ops.clone_or_fetch.assert_called_once()
    mock_git_ops.ensure_clean_working_tree.assert_called_once()

    # Dirty working tree raises RuntimeError
    mock_git_ops.ensure_clean_working_tree.return_value = False
    with pytest.raises(RuntimeError, match="dirty"):
        engine.stage1_checkout_source()


def test_stage2_load_checkpoint_and_reconcile(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 2: Acquires lock, initializes baseline, and reconciles EXPORTED PRs."""
    cfg = config.SyncConfig()
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
        runner_id="test-runner-1",
    )

    # Seed an exported contribution to test reconciliation
    exported_record = ContributionRecord(
        sync_key="PR_10",
        source_pr_number=10,
        source_branch="feat/auth",
        target_branch="main",
        merge_commit_sha="auth_merge_sha",
        merged_at=datetime.now(UTC),
        status="EXPORTED",
        destination_pr_number=55,
        destination_pr_url="https://github.com/Occupify/occupify-agentic/pull/55",
    )
    db.record_contribution(exported_record)

    # Target PR is merged -> should become INTEGRATED
    mock_github_client.get_pr_details.return_value = {"merged": True, "state": "closed"}

    checkpoint = engine.stage2_load_checkpoint(source_head_sha="baseline_sha_000")
    assert checkpoint.initial_checkpoint_sha == "baseline_sha_000"
    assert checkpoint.last_integrated_sha == "auth_merge_sha"

    updated = db.get_contribution("PR_10")
    assert updated is not None
    assert updated.status == "INTEGRATED"

    # Test closed without merge -> REJECTED
    rejected_record = ContributionRecord(
        sync_key="PR_11",
        source_pr_number=11,
        source_branch="feat/rejected",
        target_branch="main",
        merge_commit_sha="rejected_sha",
        merged_at=datetime.now(UTC),
        status="EXPORTED",
        destination_pr_number=56,
        destination_pr_url="https://github.com/Occupify/occupify-agentic/pull/56",
    )
    db.record_contribution(rejected_record)
    mock_github_client.get_pr_details.return_value = {"merged": False, "state": "closed"}

    engine.stage2_load_checkpoint()
    updated_rej = db.get_contribution("PR_11")
    assert updated_rej is not None
    assert updated_rej.status == "REJECTED"

    engine.release_distributed_lock()


def test_stage2_lock_conflict_raises_error(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 2: Raises RuntimeError if lock is held by another process."""
    cfg = config.SyncConfig()
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
        runner_id="runner_b",
    )

    # Acquire lock with another runner
    db.acquire_lock("occupify_sync", locked_by="runner_a", timeout_seconds=1800)

    with pytest.raises(RuntimeError, match="Failed to acquire distributed lock"):
        engine.stage2_load_checkpoint()


def test_stage3_find_new_prs(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 3: Filters PRs merged after checkpoint and ignores already processed ones."""
    cfg = config.SyncConfig()
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    now = datetime.now(UTC)
    init_time = now - timedelta(hours=2)

    # Create baseline checkpoint
    cp = db.get_or_create_checkpoint(cfg.SOURCE_REPO, cfg.TARGET_REPO, initial_sha="baseline_sha")
    cp.initial_checkpoint_timestamp = init_time

    # Mock GitHub closed PRs
    mock_github_client.get_closed_prs.return_value = [
        # PR 1: merged before baseline -> should be ignored
        {
            "number": 1,
            "title": "Old PR",
            "merged_at": (init_time - timedelta(hours=1)).isoformat(),
            "merge_commit_sha": "old_sha",
            "head": {"ref": "old-branch"},
        },
        # PR 2: matches baseline SHA -> should be ignored
        {
            "number": 2,
            "title": "Baseline PR",
            "merged_at": (init_time + timedelta(minutes=10)).isoformat(),
            "merge_commit_sha": "baseline_sha",
            "head": {"ref": "base-branch"},
        },
        # PR 3: eligible new PR
        {
            "number": 3,
            "title": "New Feature 1",
            "merged_at": (init_time + timedelta(minutes=20)).isoformat(),
            "merge_commit_sha": "sha_pr_3",
            "head": {"ref": "feature/one"},
        },
        # PR 4: eligible new PR (later)
        {
            "number": 4,
            "title": "New Feature 2",
            "merged_at": (init_time + timedelta(minutes=30)).isoformat(),
            "merge_commit_sha": "sha_pr_4",
            "head": {"ref": "feature/two"},
        },
    ]

    eligible = engine.stage3_find_new_prs(checkpoint=cp)
    assert len(eligible) == 2
    assert [p["number"] for p in eligible] == [3, 4]

    # Verify pending records were created in DB
    rec3 = db.get_contribution("PR_3")
    assert rec3 is not None
    assert rec3.status == "PENDING"
    assert rec3.source_branch == "feature/one"


def test_stage4_extract_contributions(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 4: Extracts commits, contributors, changed files and updates DB."""
    cfg = config.SyncConfig()
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    mock_github_client.get_pr_commits.return_value = [
        {
            "sha": "commit_1",
            "author_login": "alice",
            "author_name": "Alice Developer",
            "author_email": "alice@company.com",
            "author_date": "2026-11-10T01:00:00Z",
        },
        {
            "sha": "commit_2",
            "author_login": "alice",
            "author_name": "Alice Developer",
            "author_email": "alice@company.com",
            "author_date": "2026-11-10T01:10:00Z",
        },
        {
            "sha": "commit_3",
            "author_login": "bob",
            "author_name": "Bob Pair",
            "author_email": "bob@company.com",
            "author_date": "2026-11-10T01:15:00Z",
        },
    ]
    mock_github_client.get_pr_files.return_value = ["README.md", "app/main.py"]

    record = engine.stage4_extract_contributions(42)
    assert record.source_pr_number == 42
    assert len(record.contributors) == 2
    assert len(record.changed_files) == 2

    # Verify persistence
    db_record = db.get_contribution("PR_42")
    assert db_record is not None
    assert len(db_record.contributors) == 2
    alice = next(c for c in db_record.contributors if c["username"] == "alice")
    assert len(alice["commits"]) == 2


def test_stage5_calculate_diff(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 5: Computes diff between base and head or merge commit parent."""
    cfg = config.SyncConfig()
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    record = ContributionRecord(
        sync_key="PR_5",
        source_pr_number=5,
        source_branch="feat/patch",
        target_branch="main",
        merge_commit_sha="merge_commit_sha_555",
        merged_at=datetime.now(UTC),
    )
    pr_data = {
        "base": {"sha": "base_sha_111"},
        "head": {"sha": "head_sha_222"},
    }

    patch_text = engine.stage5_calculate_diff(record, pr_data)
    assert "diff --git" in patch_text
    mock_git_ops.calculate_patch.assert_called_with(
        engine.source_dir, "base_sha_111", "head_sha_222"
    )


def test_stage6_sync_target_success_and_conflict(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 6: Applies patch to target repo and handles merge conflicts cleanly."""
    cfg = config.SyncConfig()
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    record = ContributionRecord(
        sync_key="PR_6",
        source_pr_number=6,
        source_branch="feature/payment-v2",
        target_branch="main",
        merge_commit_sha="merge_sha_6",
        merged_at=datetime.now(UTC),
        contributors=[
            {"username": "alice", "name": "Alice", "email": "alice@test.com"},
            {"username": "bob", "name": "Bob", "email": "bob@test.com"},
        ],
    )
    db.record_contribution(record)

    # Success case
    success, err = engine.stage6_sync_target(record, "patch content")
    assert success is True
    assert err is None
    assert record.sync_branch == "sync/b/pr-6-feature-payment-v2"
    mock_git_ops.apply_patch_or_commit.assert_called_once()

    # Conflict case
    mock_git_ops.apply_patch_or_commit.return_value = (
        False,
        "Patch conflict at line 42",
    )
    record_conflict = ContributionRecord(
        sync_key="PR_7",
        source_pr_number=7,
        source_branch="conflict-branch",
        target_branch="main",
        merge_commit_sha="merge_sha_7",
        merged_at=datetime.now(UTC),
    )
    db.record_contribution(record_conflict)

    success_c, err_c = engine.stage6_sync_target(record_conflict, "conflict patch")
    assert success_c is False
    assert "conflict" in err_c.lower()

    # Verify status in DB is CONFLICT
    updated = db.get_contribution("PR_7")
    assert updated is not None
    assert updated.status == "CONFLICT"
    assert updated.error_message == err_c


def test_stage7_create_pr(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 7: Handles PR creation in both dry-run and live modes."""
    # Live mode
    cfg_live = config.SyncConfig(DRY_RUN=False)
    engine_live = SyncEngine(
        config=cfg_live,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )
    record = ContributionRecord(
        sync_key="PR_8",
        source_pr_number=8,
        source_branch="feat/shipping",
        target_branch="main",
        merge_commit_sha="sha_8",
        merged_at=datetime.now(UTC),
        sync_branch="sync/b/pr-8-feat-shipping",
    )

    dest_pr = engine_live.stage7_create_pr(record)
    assert dest_pr["number"] == 101
    mock_git_ops.push_branch.assert_called_once()
    mock_github_client.create_pull_request.assert_called_once()

    # Dry run mode
    cfg_dry = config.SyncConfig(DRY_RUN=True)
    engine_dry = SyncEngine(
        config=cfg_dry,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )
    mock_git_ops.reset_mock()
    mock_github_client.reset_mock()

    dry_pr = engine_dry.stage7_create_pr(record)
    assert dry_pr["number"] == 9999 + 8
    # Push and create_pr must NOT be called in dry run
    mock_git_ops.push_branch.assert_not_called()
    mock_github_client.create_pull_request.assert_not_called()


def test_stage8_update_state(mock_git_ops, mock_github_client, tmp_path):
    """Test Stage 8: Updates DB to EXPORTED, advances checkpoint, and releases lock."""
    cfg = config.SyncConfig(DRY_RUN=False)
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
        runner_id="runner_stage8",
    )
    # Establish lock
    db.acquire_lock("occupify_sync", "runner_stage8")
    engine._lock_held = True

    record = ContributionRecord(
        sync_key="PR_9",
        source_pr_number=9,
        source_branch="feat/state",
        target_branch="main",
        merge_commit_sha="export_sha_999",
        merged_at=datetime.now(UTC),
    )
    db.record_contribution(record)

    dest_pr_data = {
        "number": 109,
        "html_url": "https://github.com/Occupify/occupify-agentic/pull/109",
    }
    engine.stage8_update_state(record, dest_pr_data=dest_pr_data, release_lock=True)

    # Check contribution updated
    updated_rec = db.get_contribution("PR_9")
    assert updated_rec is not None
    assert updated_rec.status == "EXPORTED"
    assert updated_rec.destination_pr_number == 109

    # Check checkpoint updated
    cp = db.get_or_create_checkpoint(cfg.SOURCE_REPO, cfg.TARGET_REPO)
    assert cp.last_exported_sha == "export_sha_999"

    # Lock must be released
    assert engine._lock_held is False


def test_run_all_end_to_end_success(mock_git_ops, mock_github_client, tmp_path):
    """Test run_all() coordinating all stages end-to-end with multiple PRs."""
    cfg = config.SyncConfig(DRY_RUN=False)
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    now = datetime.now(UTC)
    # Pre-seed baseline checkpoint from 1 hour ago
    with db.get_session() as session:
        cp_row = db.SyncCheckpointModel(
            source_repo=cfg.SOURCE_REPO,
            target_repo=cfg.TARGET_REPO,
            initial_checkpoint_sha="old_baseline",
            initial_checkpoint_timestamp=now - timedelta(hours=1),
        )
        session.add(cp_row)
        session.commit()

    mock_github_client.get_closed_prs.return_value = [
        {
            "number": 100,
            "title": "Feature Alpha",
            "merged_at": (now - timedelta(minutes=10)).isoformat(),
            "merge_commit_sha": "sha_alpha",
            "head": {"ref": "feature/alpha", "sha": "head_alpha"},
            "base": {"sha": "base_alpha"},
        }
    ]

    result = engine.run_all()
    assert result["status"] == "SUCCESS"
    assert len(result["synced_prs"]) == 1
    assert result["synced_prs"][0]["source_pr"] == 100

    # Ensure contribution was exported
    rec = db.get_contribution("PR_100")
    assert rec is not None
    assert rec.status == "EXPORTED"


def test_run_all_conflict_halts_safely(mock_git_ops, mock_github_client, tmp_path):
    """Test run_all() halts cleanly and records CONFLICT when patch conflict occurs."""
    cfg = config.SyncConfig(DRY_RUN=False)
    engine = SyncEngine(
        config=cfg,
        git_ops=mock_git_ops,
        github_client=mock_github_client,
        work_dir=str(tmp_path),
    )

    now = datetime.now(UTC)
    # Pre-seed baseline checkpoint from 1 hour ago
    with db.get_session() as session:
        cp_row = db.SyncCheckpointModel(
            source_repo=cfg.SOURCE_REPO,
            target_repo=cfg.TARGET_REPO,
            initial_checkpoint_sha="old_baseline",
            initial_checkpoint_timestamp=now - timedelta(hours=1),
        )
        session.add(cp_row)
        session.commit()

    mock_github_client.get_closed_prs.return_value = [
        {
            "number": 200,
            "title": "Conflict PR",
            "merged_at": (now - timedelta(minutes=5)).isoformat(),
            "merge_commit_sha": "sha_conflict",
            "head": {"ref": "feature/conflict", "sha": "head_c"},
            "base": {"sha": "base_c"},
        }
    ]
    # Simulate conflict in git_ops
    mock_git_ops.apply_patch_or_commit.return_value = (False, "Conflict in File.java")

    result = engine.run_all()
    assert result["status"] == "CONFLICT"
    assert result["pr_number"] == 200

    # Check DB status is CONFLICT
    rec = db.get_contribution("PR_200")
    assert rec is not None
    assert rec.status == "CONFLICT"
