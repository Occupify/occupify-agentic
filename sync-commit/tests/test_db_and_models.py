"""Tests for sync_engine config, models, and db layer."""

from datetime import UTC, datetime, timedelta

import pytest
from sync_engine import config, db
from sync_engine.models import Checkpoint, ContributionRecord, Contributor, SyncLock


@pytest.fixture(autouse=True)
def setup_test_db(tmp_path):
    """Set up an isolated SQLite database for each test."""
    db_file = tmp_path / "test_sync.db"
    test_db_url = f"sqlite:///{db_file}"
    db.init_db(test_db_url)
    yield
    # Clean up global engine
    db._engine = None
    db._sessionmaker = None


def test_config_defaults_and_normalization():
    """Verify configuration defaults and database URL normalization."""
    # Test normalization function
    assert (
        config.normalize_sync_database_url("postgresql+asyncpg://user:pass@host:5432/db")
        == "postgresql://user:pass@host:5432/db"
    )
    assert (
        config.normalize_sync_database_url("postgres://user:pass@host:5432/db")
        == "postgresql://user:pass@host:5432/db"
    )
    assert config.normalize_sync_database_url("sqlite:///test.db") == "sqlite:///test.db"

    # Test config instance
    cfg = config.SyncConfig(
        GITHUB_TOKEN="ghp_test_token_123",
        DATABASE_URL="postgresql+asyncpg://localhost:5432/testdb",
    )
    assert cfg.SOURCE_REPO == "https://github.com/se373agenticengineering/nhom-01.git"
    assert cfg.TARGET_REPO == "https://github.com/Occupify/occupify-agentic.git"
    assert cfg.SOURCE_BRANCH == "main"
    assert cfg.TARGET_BRANCH == "main"
    assert cfg.SOURCE_GITHUB_TOKEN == "ghp_test_token_123"
    assert cfg.TARGET_GITHUB_TOKEN == "ghp_test_token_123"
    assert cfg.sync_database_url == "postgresql://localhost:5432/testdb"
    assert cfg.DRY_RUN is False
    assert cfg.LOCK_EXPIRY_SECONDS == 1800


def test_models_dataclasses():
    """Verify models instantiation, dict conversion, and roundtrips."""
    now = datetime.now(UTC)

    # Contributor
    contributor = Contributor(
        username="octocat",
        github_id=583231,
        name="The Octocat",
        email="octocat@github.com",
        commits=["sha1", "sha2"],
    )
    c_dict = contributor.to_dict()
    assert c_dict["username"] == "octocat"
    assert c_dict["commits"] == ["sha1", "sha2"]
    c_restored = Contributor.from_dict(c_dict)
    assert c_restored == contributor

    # Checkpoint
    checkpoint = Checkpoint(
        id=1,
        source_repo="https://github.com/source/repo.git",
        target_repo="https://github.com/target/repo.git",
        initial_checkpoint_sha="init_sha",
        initial_checkpoint_timestamp=now,
        last_exported_sha="exp_sha",
        last_integrated_sha="int_sha",
    )
    cp_dict = checkpoint.to_dict()
    assert cp_dict["initial_checkpoint_sha"] == "init_sha"
    cp_restored = Checkpoint.from_dict(cp_dict)
    assert cp_restored.source_repo == checkpoint.source_repo
    assert cp_restored.last_exported_sha == "exp_sha"

    # SyncLock
    expires = now + timedelta(seconds=1800)
    lock = SyncLock(
        lock_name="test_lock",
        locked_by="worker_1",
        acquired_at=now,
        expires_at=expires,
    )
    lock_dict = lock.to_dict()
    lock_restored = SyncLock.from_dict(lock_dict)
    assert lock_restored.lock_name == "test_lock"
    assert lock_restored.locked_by == "worker_1"

    # ContributionRecord
    record = ContributionRecord(
        sync_key="PR_42",
        source_pr_number=42,
        source_branch="feat/test",
        target_branch="main",
        merge_commit_sha="abcdef123456",
        merged_at=now,
        status="PENDING",
        contributors=[c_dict],
        changed_files=["app/main.py", "README.md"],
        commit_mapping={"sha1": "sha1_sync"},
    )
    rec_dict = record.to_dict()
    rec_restored = ContributionRecord.from_dict(rec_dict)
    assert rec_restored.sync_key == "PR_42"
    assert rec_restored.source_pr_number == 42
    assert len(rec_restored.changed_files) == 2


def test_distributed_lock_lifecycle():
    """Verify lock acquisition, exclusion, renewal, and release."""
    lock_name = "sync_job"
    worker_a = "worker_alpha"
    worker_b = "worker_beta"

    # 1. Worker A acquires lock
    assert db.acquire_lock(lock_name, worker_a, timeout_seconds=10) is True

    # 2. Worker B fails to acquire same active lock
    assert db.acquire_lock(lock_name, worker_b, timeout_seconds=10) is False

    # 3. Worker A can re-entrantly renew lock
    assert db.acquire_lock(lock_name, worker_a, timeout_seconds=20) is True

    # 4. Worker B cannot release Worker A's lock
    assert db.release_lock(lock_name, worker_b) is False

    # 5. Worker A releases lock
    assert db.release_lock(lock_name, worker_a) is True

    # 6. Now Worker B can acquire it
    assert db.acquire_lock(lock_name, worker_b, timeout_seconds=10) is True

    # 7. Releasing already released lock returns False
    assert db.release_lock(lock_name, worker_b) is True
    assert db.release_lock(lock_name, worker_b) is False


def test_lock_expiration():
    """Verify that an expired lock can be taken over by another worker."""
    lock_name = "expiring_lock"
    worker_a = "worker_a"
    worker_b = "worker_b"

    # Acquire lock with 0 timeout (already expired immediately)
    assert db.acquire_lock(lock_name, worker_a, timeout_seconds=0) is True

    # Worker B can acquire expired lock
    assert db.acquire_lock(lock_name, worker_b, timeout_seconds=60) is True

    # Worker A can no longer release it
    assert db.release_lock(lock_name, worker_a) is False
    assert db.release_lock(lock_name, worker_b) is True


def test_checkpoint_management():
    """Verify get_or_create_checkpoint and update_checkpoint operations."""
    source = "https://github.com/source/repo.git"
    target = "https://github.com/target/repo.git"

    # 1. Create new checkpoint
    cp = db.get_or_create_checkpoint(source, target, initial_sha="sha_001")
    assert cp.id is not None
    assert cp.source_repo == source
    assert cp.target_repo == target
    assert cp.initial_checkpoint_sha == "sha_001"
    assert cp.last_exported_sha is None
    assert cp.last_integrated_sha is None

    # 2. Getting existing checkpoint returns same record
    cp_again = db.get_or_create_checkpoint(source, target, initial_sha="ignored_sha")
    assert cp_again.id == cp.id
    assert cp_again.initial_checkpoint_sha == "sha_001"

    # 3. Update exported SHA
    cp_updated = db.update_checkpoint(source, target, last_exported_sha="sha_export_1")
    assert cp_updated.last_exported_sha == "sha_export_1"
    assert cp_updated.last_integrated_sha is None

    # 4. Update integrated SHA
    cp_updated2 = db.update_checkpoint(source, target, last_integrated_sha="sha_integ_1")
    assert cp_updated2.last_exported_sha == "sha_export_1"
    assert cp_updated2.last_integrated_sha == "sha_integ_1"


def test_contribution_lifecycle():
    """Verify recording, querying, listing, and updating contribution records."""
    now = datetime.now(UTC)
    rec1 = ContributionRecord(
        sync_key="PR_101",
        source_pr_number=101,
        source_branch="feature/auth",
        target_branch="main",
        merge_commit_sha="merge_101",
        merged_at=now,
        status="PENDING",
        contributors=[{"username": "dev1"}],
        changed_files=["app/auth.py"],
        commit_mapping={"c1": "c1_synced"},
    )
    rec2 = ContributionRecord(
        sync_key="PR_102",
        source_pr_number=102,
        source_branch="feature/payments",
        target_branch="main",
        merge_commit_sha="merge_102",
        merged_at=now + timedelta(minutes=5),
        status="PENDING",
        contributors=[{"username": "dev2"}],
        changed_files=["app/pay.py"],
        commit_mapping={},
    )

    # Record contributions
    db.record_contribution(rec1)
    db.record_contribution(rec2)

    # Retrieve by sync_key
    fetched1 = db.get_contribution("PR_101")
    assert fetched1 is not None
    assert fetched1.sync_key == "PR_101"
    assert fetched1.source_pr_number == 101
    assert fetched1.status == "PENDING"
    assert fetched1.contributors == [{"username": "dev1"}]
    assert fetched1.changed_files == ["app/auth.py"]

    # Non-existent key
    assert db.get_contribution("PR_999") is None

    # List contributions
    all_recs = db.list_contributions()
    assert len(all_recs) == 2

    # Update contribution status
    db.update_contribution_status(
        sync_key="PR_101",
        status="EXPORTED",
        dest_pr_number=501,
        dest_pr_url="https://github.com/Occupify/occupify-agentic/pull/501",
    )

    updated1 = db.get_contribution("PR_101")
    assert updated1.status == "EXPORTED"
    assert updated1.destination_pr_number == 501
    assert updated1.destination_pr_url == "https://github.com/Occupify/occupify-agentic/pull/501"

    # Filter list by status
    pending_recs = db.list_contributions(status="PENDING")
    assert len(pending_recs) == 1
    assert pending_recs[0].sync_key == "PR_102"

    exported_recs = db.list_contributions(status="EXPORTED")
    assert len(exported_recs) == 1
    assert exported_recs[0].sync_key == "PR_101"

    # Update non-existent record raises ValueError
    with pytest.raises(ValueError, match="not found"):
        db.update_contribution_status(sync_key="PR_NONEXISTENT", status="FAILED")
