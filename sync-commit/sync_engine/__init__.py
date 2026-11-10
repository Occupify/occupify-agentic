"""Occupify Contribution Synchronization Engine.

Provides metadata tracking, distributed state locking, checkpoint management,
GitHub API client, and Git operations for synchronizing contributions between
source and target repositories.
"""

from sync_engine import config, db, models
from sync_engine.models import Checkpoint, ContributionRecord, Contributor, SyncLock

# Optional imports from sibling modules that may be developed concurrently
try:
    from sync_engine.github_client import GitHubClient
except ImportError:
    GitHubClient = None  # type: ignore

try:
    from sync_engine.git_ops import GitOps
except ImportError:
    GitOps = None  # type: ignore

try:
    from sync_engine.engine import SyncEngine
except ImportError:
    SyncEngine = None  # type: ignore

__all__ = [
    "config",
    "models",
    "db",
    "Contributor",
    "ContributionRecord",
    "Checkpoint",
    "SyncLock",
    "GitHubClient",
    "GitOps",
    "SyncEngine",
]
