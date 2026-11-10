"""Configuration module for Occupify Contribution Sync Engine.

Manages environment configuration, credentials, Git endpoints,
and database connections with resilient fallback and URL normalization.
"""

from __future__ import annotations

import os
from functools import lru_cache

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def normalize_sync_database_url(url: str) -> str:
    """Normalize database connection URL for synchronous SQLAlchemy engine.

    Converts:
      - postgresql+asyncpg:// -> postgresql://
      - postgres:// -> postgresql://
      - sqlite:///tmp/... -> sqlite:////tmp/... (ensuring directory exists)

    Args:
        url: Raw database URL string.

    Returns:
        Normalized database URL string.
    """
    if not url:
        return "postgresql://postgres:postgres@localhost:5432/occupify_agentic"

    stripped = url.strip()
    if stripped.startswith("postgresql+asyncpg://"):
        return "postgresql://" + stripped[len("postgresql+asyncpg://") :]
    if stripped.startswith("postgres://"):
        return "postgresql://" + stripped[len("postgres://") :]
    if stripped.startswith("sqlite:///"):
        path_str = stripped[len("sqlite:///") :]
        if path_str and path_str != ":memory:":
            from pathlib import Path

            if path_str.startswith("tmp/") and os.name != "nt":
                stripped = f"sqlite:////{path_str}"
                path_str = f"/{path_str}"
            p = Path(path_str)
            if p.parent and not p.parent.exists():
                p.parent.mkdir(parents=True, exist_ok=True)
    return stripped


class SyncConfig(BaseSettings):
    """Configuration settings for Occupify Contribution Sync Engine."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    SOURCE_REPO: str = Field(
        default="https://github.com/se373agenticengineering/nhom-01.git",
        description="Source Git repository clone URL",
    )
    TARGET_REPO: str = Field(
        default="https://github.com/Occupify/occupify-agentic.git",
        description="Target Git repository clone URL",
    )
    SOURCE_BRANCH: str = Field(
        default="main",
        description="Source branch to monitor for merged contributions",
    )
    TARGET_BRANCH: str = Field(
        default="main",
        description="Target branch to integrate contributions into",
    )
    GITHUB_TOKEN: str | None = Field(
        default=None,
        description="Default GitHub personal access token",
    )
    SOURCE_GITHUB_TOKEN: str | None = Field(
        default=None,
        description="GitHub token for source repo (defaults to GITHUB_TOKEN)",
    )
    TARGET_GITHUB_TOKEN: str | None = Field(
        default=None,
        description="GitHub token for target repo (defaults to GITHUB_TOKEN)",
    )
    DATABASE_URL: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/occupify_agentic",
        description="Database connection URL for sync state tracking",
    )
    FALL_BACK_DB_URL: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/occupify_agentic",
        description="Fallback database connection URL for sync state tracking",
    )
    DRY_RUN: bool = Field(
        default=False,
        description="Simulate synchronization without pushing branches or creating PRs",
    )
    LOCK_EXPIRY_SECONDS: int = Field(
        default=1800,
        description="Duration in seconds before an acquired distributed lock expires",
    )

    @model_validator(mode="before")
    @classmethod
    def apply_env_fallbacks(cls, data: dict) -> dict:
        """Resolve token fallbacks and database URL aliases from environment."""
        if not isinstance(data, dict):
            data = {}

        # Respect SYNC_DATABASE_URL if DATABASE_URL is not explicitly set in data
        if "DATABASE_URL" not in data or not data.get("DATABASE_URL"):
            sync_db_url = os.getenv("SYNC_DATABASE_URL")
            if sync_db_url:
                data["DATABASE_URL"] = sync_db_url

        # Check environment variables directly for tokens
        github_token = data.get("GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")
        if not data.get("SOURCE_GITHUB_TOKEN"):
            data["SOURCE_GITHUB_TOKEN"] = os.getenv("SOURCE_GITHUB_TOKEN") or github_token
        if not data.get("TARGET_GITHUB_TOKEN"):
            data["TARGET_GITHUB_TOKEN"] = os.getenv("TARGET_GITHUB_TOKEN") or github_token

        # Normalize DATABASE_URL for sync driver
        raw_db_url = (
            data.get("DATABASE_URL") or os.getenv("DATABASE_URL") or os.getenv("SYNC_DATABASE_URL")
        )
        if raw_db_url:
            data["DATABASE_URL"] = normalize_sync_database_url(raw_db_url)

        return data

    @property
    def sync_database_url(self) -> str:
        """Return normalized synchronous database connection URL."""
        return normalize_sync_database_url(self.DATABASE_URL)

    @property
    def sync_fallback_database_url(self) -> str:
        """Return normalized synchronous fallback database connection URL."""
        return normalize_sync_database_url(self.FALL_BACK_DB_URL)


@lru_cache(maxsize=1)
def get_settings() -> SyncConfig:
    """Return cached singleton instance of SyncConfig."""
    return SyncConfig()


# Module-level convenience exports
settings = get_settings()
SOURCE_REPO: str = settings.SOURCE_REPO
TARGET_REPO: str = settings.TARGET_REPO
SOURCE_BRANCH: str = settings.SOURCE_BRANCH
TARGET_BRANCH: str = settings.TARGET_BRANCH
GITHUB_TOKEN: str | None = settings.GITHUB_TOKEN
SOURCE_GITHUB_TOKEN: str | None = settings.SOURCE_GITHUB_TOKEN
TARGET_GITHUB_TOKEN: str | None = settings.TARGET_GITHUB_TOKEN
DATABASE_URL: str = settings.DATABASE_URL
DRY_RUN: bool = settings.DRY_RUN
LOCK_EXPIRY_SECONDS: int = settings.LOCK_EXPIRY_SECONDS
