"""Domain models for Occupify Contribution Sync Engine.

Provides dataclass representations of contributors, synchronized contribution records,
checkpoints, and distributed synchronization locks.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass
class Contributor:
    """Represents a code contributor extracted from source repository pull requests."""

    username: str
    github_id: int | None = None
    name: str | None = None
    email: str | None = None
    commits: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert model to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Contributor:
        """Create model instance from dictionary."""
        return cls(
            username=data.get("username", ""),
            github_id=data.get("github_id"),
            name=data.get("name"),
            email=data.get("email"),
            commits=list(data.get("commits") or []),
        )


@dataclass
class ContributionRecord:
    """Represents the complete synchronization state of a source pull request."""

    sync_key: str
    source_pr_number: int
    source_branch: str
    target_branch: str
    merge_commit_sha: str
    merged_at: datetime
    status: str = "PENDING"
    sync_branch: str | None = None
    destination_pr_number: int | None = None
    destination_pr_url: str | None = None
    contributors: list[dict[str, Any]] = field(default_factory=list)
    changed_files: list[str] = field(default_factory=list)
    commit_mapping: dict[str, Any] = field(default_factory=dict)
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert model to dictionary with ISO-formatted timestamps."""
        data = asdict(self)
        if isinstance(self.merged_at, datetime):
            data["merged_at"] = self.merged_at.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContributionRecord:
        """Create model instance from dictionary."""
        merged_at = data.get("merged_at")
        if isinstance(merged_at, str):
            merged_at = datetime.fromisoformat(merged_at)
        elif merged_at is None:
            merged_at = datetime.now(UTC)

        return cls(
            sync_key=data["sync_key"],
            source_pr_number=int(data["source_pr_number"]),
            source_branch=data.get("source_branch", "main"),
            target_branch=data.get("target_branch", "main"),
            merge_commit_sha=data.get("merge_commit_sha", ""),
            merged_at=merged_at,
            status=data.get("status", "PENDING"),
            sync_branch=data.get("sync_branch"),
            destination_pr_number=data.get("destination_pr_number"),
            destination_pr_url=data.get("destination_pr_url"),
            contributors=list(data.get("contributors") or []),
            changed_files=list(data.get("changed_files") or []),
            commit_mapping=dict(data.get("commit_mapping") or {}),
            error_message=data.get("error_message"),
        )


@dataclass
class Checkpoint:
    """Tracks synchronization progress markers between source and target repositories."""

    source_repo: str
    target_repo: str
    initial_checkpoint_sha: str
    initial_checkpoint_timestamp: datetime
    id: int | None = None
    last_exported_sha: str | None = None
    last_integrated_sha: str | None = None

    def __init__(
        self,
        id: int | None = None,
        source_repo: str = "",
        target_repo: str = "",
        initial_checkpoint_sha: str = "",
        initial_checkpoint_timestamp: datetime | None = None,
        last_exported_sha: str | None = None,
        last_integrated_sha: str | None = None,
    ) -> None:
        """Initialize Checkpoint supporting both positional and keyword argument orders."""
        self.id = id
        self.source_repo = source_repo
        self.target_repo = target_repo
        self.initial_checkpoint_sha = initial_checkpoint_sha
        self.initial_checkpoint_timestamp = initial_checkpoint_timestamp or datetime.now(UTC)
        self.last_exported_sha = last_exported_sha
        self.last_integrated_sha = last_integrated_sha

    def to_dict(self) -> dict[str, Any]:
        """Convert model to dictionary."""
        data = asdict(self)
        if isinstance(self.initial_checkpoint_timestamp, datetime):
            data["initial_checkpoint_timestamp"] = self.initial_checkpoint_timestamp.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Checkpoint:
        """Create model instance from dictionary."""
        init_ts = data.get("initial_checkpoint_timestamp")
        if isinstance(init_ts, str):
            init_ts = datetime.fromisoformat(init_ts)

        return cls(
            id=data.get("id"),
            source_repo=data.get("source_repo", ""),
            target_repo=data.get("target_repo", ""),
            initial_checkpoint_sha=data.get("initial_checkpoint_sha", ""),
            initial_checkpoint_timestamp=init_ts,
            last_exported_sha=data.get("last_exported_sha"),
            last_integrated_sha=data.get("last_integrated_sha"),
        )


@dataclass
class SyncLock:
    """Represents a distributed execution lock preventing concurrent sync pipeline runs."""

    lock_name: str
    locked_by: str
    acquired_at: datetime
    expires_at: datetime

    def to_dict(self) -> dict[str, Any]:
        """Convert model to dictionary."""
        return {
            "lock_name": self.lock_name,
            "locked_by": self.locked_by,
            "acquired_at": (
                self.acquired_at.isoformat()
                if isinstance(self.acquired_at, datetime)
                else self.acquired_at
            ),
            "expires_at": (
                self.expires_at.isoformat()
                if isinstance(self.expires_at, datetime)
                else self.expires_at
            ),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SyncLock:
        """Create model instance from dictionary."""
        acquired_at = data["acquired_at"]
        if isinstance(acquired_at, str):
            acquired_at = datetime.fromisoformat(acquired_at)

        expires_at = data["expires_at"]
        if isinstance(expires_at, str):
            expires_at = datetime.fromisoformat(expires_at)

        return cls(
            lock_name=data["lock_name"],
            locked_by=data["locked_by"],
            acquired_at=acquired_at,
            expires_at=expires_at,
        )
