"""Database access layer for Occupify Contribution Sync Engine.

Provides resilient database connectivity using SQLAlchemy, distributed state locking,
checkpoint tracking, and contribution record auditing. Supports automatic fallback
to SQLite when PostgreSQL is unreachable during local testing.
"""

from __future__ import annotations

import logging
from collections.abc import Generator
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta

from sqlalchemy import (
    JSON,
    DateTime,
    Integer,
    String,
    Text,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    sessionmaker,
)

from sync_engine import config
from sync_engine.models import Checkpoint, ContributionRecord

logger = logging.getLogger(__name__)

# Global engine and sessionmaker singletons
_engine: Engine | None = None
_sessionmaker: sessionmaker[Session] | None = None


class Base(DeclarativeBase):
    """SQLAlchemy Declarative Base for sync engine tables."""

    pass


class SyncCheckpointModel(Base):
    """Tracks commit synchronization progress between source and target repositories."""

    __tablename__ = "sync_checkpoints"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    source_repo: Mapped[str] = mapped_column(String(255), nullable=False)
    target_repo: Mapped[str] = mapped_column(String(255), nullable=False)
    initial_checkpoint_sha: Mapped[str] = mapped_column(String(100), nullable=False)
    initial_checkpoint_timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    last_exported_sha: Mapped[str | None] = mapped_column(String(100), nullable=True)
    last_integrated_sha: Mapped[str | None] = mapped_column(String(100), nullable=True)

    __table_args__ = (
        UniqueConstraint("source_repo", "target_repo", name="uq_sync_checkpoints_repos"),
    )


class SyncContributionModel(Base):
    """Tracks synchronization state of individual source PRs and their destination PRs."""

    __tablename__ = "sync_contributions"

    sync_key: Mapped[str] = mapped_column(String(100), primary_key=True)
    source_pr_number: Mapped[int] = mapped_column(Integer, nullable=False)
    source_branch: Mapped[str] = mapped_column(String(100), nullable=False)
    target_branch: Mapped[str] = mapped_column(String(100), nullable=False)
    merge_commit_sha: Mapped[str] = mapped_column(String(100), nullable=False)
    merged_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="PENDING")
    sync_branch: Mapped[str | None] = mapped_column(String(150), nullable=True)
    destination_pr_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    destination_pr_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    contributors: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    changed_files: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    commit_mapping: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)


class SyncLockModel(Base):
    """Distributed lock record for preventing concurrent synchronization jobs."""

    __tablename__ = "sync_locks"

    lock_name: Mapped[str] = mapped_column(String(100), primary_key=True)
    locked_by: Mapped[str] = mapped_column(String(255), nullable=False)
    acquired_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


def _ensure_utc(dt: datetime | None) -> datetime | None:
    """Ensure datetime object is timezone-aware UTC."""
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def _row_to_checkpoint(row: SyncCheckpointModel) -> Checkpoint:
    """Convert ORM row to Checkpoint model."""
    return Checkpoint(
        id=row.id,
        source_repo=row.source_repo,
        target_repo=row.target_repo,
        initial_checkpoint_sha=row.initial_checkpoint_sha,
        initial_checkpoint_timestamp=_ensure_utc(row.initial_checkpoint_timestamp),
        last_exported_sha=row.last_exported_sha,
        last_integrated_sha=row.last_integrated_sha,
    )


def _row_to_contribution(row: SyncContributionModel) -> ContributionRecord:
    """Convert ORM row to ContributionRecord model."""
    return ContributionRecord(
        sync_key=row.sync_key,
        source_pr_number=row.source_pr_number,
        source_branch=row.source_branch,
        target_branch=row.target_branch,
        merge_commit_sha=row.merge_commit_sha,
        merged_at=_ensure_utc(row.merged_at) or datetime.now(UTC),
        status=row.status,
        sync_branch=row.sync_branch,
        destination_pr_number=row.destination_pr_number,
        destination_pr_url=row.destination_pr_url,
        contributors=list(row.contributors or []),
        changed_files=list(row.changed_files or []),
        commit_mapping=dict(row.commit_mapping or {}),
        error_message=row.error_message,
    )


def init_db(db_url: str | None = None) -> Engine:
    """Initialize database engine and create tables.

    Attempts connection to the specified database URL. If PostgreSQL is unreachable
    (e.g., during offline testing), safely falls back to SQLite.

    Args:
        db_url: Optional database connection string. Defaults to config.DATABASE_URL.

    Returns:
        SQLAlchemy Engine instance.
    """
    global _engine, _sessionmaker

    url = db_url or config.DATABASE_URL
    url = config.normalize_sync_database_url(url)

    # Attempt connecting to requested database
    try:
        engine = create_engine(url, pool_pre_ping=True)
        # Test connection readiness
        with engine.connect():
            pass
        logger.info("Connected to database at %s", url.split("@")[-1] if "@" in url else url)
    except (OperationalError, Exception) as exc:
        fallback_url = config.get_settings().sync_fallback_database_url
        if fallback_url and fallback_url != url:
            try:
                logger.warning(
                    "Could not connect to database at %s (%s). Attempting FALL_BACK_DB_URL at %s.",
                    url,
                    exc,
                    fallback_url.split("@")[-1] if "@" in fallback_url else fallback_url,
                )
                engine = create_engine(fallback_url, pool_pre_ping=True)
                with engine.connect():
                    pass
                logger.info(
                    "Connected to fallback database at %s",
                    fallback_url.split("@")[-1] if "@" in fallback_url else fallback_url,
                )
            except Exception as fb_exc:
                if not url.startswith("sqlite"):
                    logger.warning(
                        "Fallback database at %s also failed (%s). Falling back to SQLite for local execution.",
                        fallback_url,
                        fb_exc,
                    )
                    engine = create_engine("sqlite:///sync_engine.db")
                else:
                    raise fb_exc
        elif not url.startswith("sqlite"):
            logger.warning(
                "Could not connect to database at %s (%s). Falling back to SQLite for local execution.",
                url,
                exc,
            )
            fallback_url = "sqlite:///sync_engine.db"
            engine = create_engine(fallback_url)
        else:
            raise exc

    # Create tables
    Base.metadata.create_all(bind=engine)

    _engine = engine
    _sessionmaker = sessionmaker(bind=_engine, expire_on_commit=False)
    return _engine


@contextmanager
def get_session() -> Generator[Session]:
    """Provide a transactional SQLAlchemy session scope.

    Automatically initializes the database if not already done.
    """
    global _sessionmaker
    if _sessionmaker is None:
        init_db()

    assert _sessionmaker is not None
    session = _sessionmaker()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def acquire_lock(lock_name: str, locked_by: str, timeout_seconds: int = 1800) -> bool:
    """Attempt to acquire a distributed named lock.

    The lock is acquired if no active lock exists, or if the current lock has expired,
    or if it is already held by the same `locked_by` identifier (re-entrant renewal).

    Args:
        lock_name: Unique identifier for the lock (e.g. 'occupify_sync').
        locked_by: Identifier of the process or worker attempting acquisition.
        timeout_seconds: Duration before lock expiration. Defaults to 1800.

    Returns:
        True if the lock was successfully acquired or renewed; False otherwise.
    """
    now = datetime.now(UTC)
    expires_at = now + timedelta(seconds=timeout_seconds)

    with get_session() as session:
        lock = session.query(SyncLockModel).filter_by(lock_name=lock_name).first()
        if lock is None:
            new_lock = SyncLockModel(
                lock_name=lock_name,
                locked_by=locked_by,
                acquired_at=now,
                expires_at=expires_at,
            )
            session.add(new_lock)
            try:
                session.commit()
                return True
            except IntegrityError:
                session.rollback()
                # Re-query in case of concurrent insert
                lock = session.query(SyncLockModel).filter_by(lock_name=lock_name).first()
                if lock is None:
                    return False

        # Existing lock evaluation
        lock_expires_at = _ensure_utc(lock.expires_at)
        if lock_expires_at is None or lock_expires_at <= now or lock.locked_by == locked_by:
            lock.locked_by = locked_by
            lock.acquired_at = now
            lock.expires_at = expires_at
            session.commit()
            return True

        return False


def release_lock(lock_name: str, locked_by: str) -> bool:
    """Release an acquired distributed lock if owned by the caller.

    Args:
        lock_name: Unique identifier for the lock.
        locked_by: Identifier of the holder attempting release.

    Returns:
        True if the lock was found and released; False otherwise.
    """
    with get_session() as session:
        lock = session.query(SyncLockModel).filter_by(lock_name=lock_name).first()
        if lock is not None and lock.locked_by == locked_by:
            session.delete(lock)
            session.commit()
            return True
        return False


def get_or_create_checkpoint(
    source_repo: str,
    target_repo: str,
    initial_sha: str | None = None,
) -> Checkpoint:
    """Retrieve existing sync checkpoint or initialize a new one.

    Args:
        source_repo: Clone URL of the source repository.
        target_repo: Clone URL of the target repository.
        initial_sha: Initial commit SHA marker if creating a new checkpoint.

    Returns:
        Checkpoint domain model.
    """
    with get_session() as session:
        cp = (
            session.query(SyncCheckpointModel)
            .filter_by(source_repo=source_repo, target_repo=target_repo)
            .first()
        )
        if cp is not None:
            return _row_to_checkpoint(cp)

        now = datetime.now(UTC)
        new_cp = SyncCheckpointModel(
            source_repo=source_repo,
            target_repo=target_repo,
            initial_checkpoint_sha=initial_sha or "",
            initial_checkpoint_timestamp=now,
            last_exported_sha=None,
            last_integrated_sha=None,
        )
        session.add(new_cp)
        try:
            session.commit()
            session.refresh(new_cp)
            return _row_to_checkpoint(new_cp)
        except IntegrityError:
            session.rollback()
            cp = (
                session.query(SyncCheckpointModel)
                .filter_by(source_repo=source_repo, target_repo=target_repo)
                .first()
            )
            if cp is not None:
                return _row_to_checkpoint(cp)
            raise


def update_checkpoint(
    source_repo: str,
    target_repo: str,
    last_exported_sha: str | None = None,
    last_integrated_sha: str | None = None,
) -> Checkpoint:
    """Update exported and/or integrated commit SHAs for a checkpoint.

    Args:
        source_repo: Clone URL of the source repository.
        target_repo: Clone URL of the target repository.
        last_exported_sha: Latest commit SHA exported to synchronization branch.
        last_integrated_sha: Latest commit SHA integrated/merged into target repository.

    Returns:
        Updated Checkpoint domain model.
    """
    with get_session() as session:
        cp = (
            session.query(SyncCheckpointModel)
            .filter_by(source_repo=source_repo, target_repo=target_repo)
            .first()
        )
        if cp is None:
            now = datetime.now(UTC)
            cp = SyncCheckpointModel(
                source_repo=source_repo,
                target_repo=target_repo,
                initial_checkpoint_sha="",
                initial_checkpoint_timestamp=now,
                last_exported_sha=last_exported_sha,
                last_integrated_sha=last_integrated_sha,
            )
            session.add(cp)
        else:
            if last_exported_sha is not None:
                cp.last_exported_sha = last_exported_sha
            if last_integrated_sha is not None:
                cp.last_integrated_sha = last_integrated_sha

        session.commit()
        session.refresh(cp)
        return _row_to_checkpoint(cp)


def get_contribution(sync_key: str) -> ContributionRecord | None:
    """Retrieve a contribution record by its unique sync key.

    Args:
        sync_key: Unique identifier of the contribution (e.g., 'PR_12').

    Returns:
        ContributionRecord domain model if found; None otherwise.
    """
    with get_session() as session:
        row = session.query(SyncContributionModel).filter_by(sync_key=sync_key).first()
        if row is None:
            return None
        return _row_to_contribution(row)


def list_contributions(status: str | None = None) -> list[ContributionRecord]:
    """List contribution records, optionally filtered by status.

    Args:
        status: Optional status string (e.g. 'PENDING', 'EXPORTED', 'INTEGRATED', 'FAILED').

    Returns:
        List of ContributionRecord domain models ordered by merged_at ascending.
    """
    with get_session() as session:
        query = session.query(SyncContributionModel)
        if status is not None:
            query = query.filter_by(status=status)
        rows = query.order_by(SyncContributionModel.merged_at.asc()).all()
        return [_row_to_contribution(r) for r in rows]


def record_contribution(record: ContributionRecord) -> None:
    """Create or update a contribution record in the database.

    Args:
        record: ContributionRecord model to insert or update.
    """
    with get_session() as session:
        existing = session.query(SyncContributionModel).filter_by(sync_key=record.sync_key).first()
        if existing is None:
            new_row = SyncContributionModel(
                sync_key=record.sync_key,
                source_pr_number=record.source_pr_number,
                source_branch=record.source_branch,
                target_branch=record.target_branch,
                merge_commit_sha=record.merge_commit_sha,
                merged_at=_ensure_utc(record.merged_at) or datetime.now(UTC),
                status=record.status,
                sync_branch=record.sync_branch,
                destination_pr_number=record.destination_pr_number,
                destination_pr_url=record.destination_pr_url,
                contributors=record.contributors or [],
                changed_files=record.changed_files or [],
                commit_mapping=record.commit_mapping or {},
                error_message=record.error_message,
            )
            session.add(new_row)
        else:
            existing.source_pr_number = record.source_pr_number
            existing.source_branch = record.source_branch
            existing.target_branch = record.target_branch
            existing.merge_commit_sha = record.merge_commit_sha
            existing.merged_at = _ensure_utc(record.merged_at) or existing.merged_at
            existing.status = record.status
            existing.sync_branch = record.sync_branch
            existing.destination_pr_number = record.destination_pr_number
            existing.destination_pr_url = record.destination_pr_url
            existing.contributors = record.contributors or []
            existing.changed_files = record.changed_files or []
            existing.commit_mapping = record.commit_mapping or {}
            existing.error_message = record.error_message

        session.commit()


def update_contribution_status(
    sync_key: str,
    status: str,
    dest_pr_number: int | None = None,
    dest_pr_url: str | None = None,
    error_message: str | None = None,
) -> None:
    """Update status and destination PR information for an existing contribution.

    Args:
        sync_key: Unique identifier of the contribution.
        status: New status string (e.g., 'EXPORTED', 'INTEGRATED', 'FAILED').
        dest_pr_number: Optional destination pull request number.
        dest_pr_url: Optional destination pull request URL.
        error_message: Optional error message if synchronization failed.

    Raises:
        ValueError: If no contribution with sync_key is found.
    """
    with get_session() as session:
        existing = session.query(SyncContributionModel).filter_by(sync_key=sync_key).first()
        if existing is None:
            raise ValueError(f"Contribution record with sync_key '{sync_key}' not found.")

        existing.status = status
        if dest_pr_number is not None:
            existing.destination_pr_number = dest_pr_number
        if dest_pr_url is not None:
            existing.destination_pr_url = dest_pr_url
        if error_message is not None:
            existing.error_message = error_message

        session.commit()
