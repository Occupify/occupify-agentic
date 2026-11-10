"""Workflow Engine for Occupify Contribution Sync Engine.

Orchestrates the 8-stage synchronization pipeline between Source Repository B
and Target Repository A (Occupify Agentic), adhering to principles of
api-and-interface-design and observability-and-instrumentation.
"""

from __future__ import annotations

import logging
import os
import re
from datetime import UTC, datetime
from typing import Any

from sync_engine import db
from sync_engine.config import SyncConfig, get_settings
from sync_engine.git_ops import GitOps
from sync_engine.github_client import GitHubClient
from sync_engine.models import Checkpoint, ContributionRecord, Contributor

logger = logging.getLogger(__name__)


def parse_repo_owner_name(repo_url: str) -> tuple[str, str]:
    """Extract (owner, repo_name) from Git remote URL or GitHub path.

    Supports HTTPS URLs, SSH URLs, and short 'owner/repo' strings.

    Args:
        repo_url: Git clone URL or repository identifier.

    Returns:
        Tuple of (owner, repo_name) with any trailing .git stripped.

    Raises:
        ValueError: If repository owner and name cannot be parsed.
    """
    clean = repo_url.strip()
    if clean.endswith(".git"):
        clean = clean[:-4]
    clean = clean.rstrip("/")

    if "github.com/" in clean:
        parts = clean.split("github.com/")[-1].split("/")
        if len(parts) >= 2:
            return parts[0], parts[1]
    elif "github.com:" in clean:
        parts = clean.split("github.com:")[-1].split("/")
        if len(parts) >= 2:
            return parts[0], parts[1]
    elif "/" in clean:
        parts = clean.split("/")
        if len(parts) >= 2:
            return parts[-2], parts[-1]

    raise ValueError(f"Cannot parse GitHub owner and repo name from URL: {repo_url}")


def _format_contributors_markdown(contributors: list[dict[str, Any]]) -> str:
    """Format contributor list as markdown list items."""
    if not contributors:
        return "- Unknown: 1 commit"
    lines: list[str] = []
    for c in contributors:
        name = c.get("name") or c.get("username") or "Contributor"
        commits_count = len(c.get("commits") or []) or 1
        commit_plural = "commit" if commits_count == 1 else "commits"
        lines.append(f"- {name}: {commits_count} {commit_plural}")
    return "\n".join(lines)


def _format_files_markdown(files: list[str]) -> str:
    """Format changed file paths as markdown list items."""
    if not files:
        return "- No files changed"
    return "\n".join(f"- {f}" for f in files)


class SyncEngine:
    """Coordinates the 8-stage Contribution Synchronization Engine.

    Manages repository checkouts, checkpoint tracking, PR discovery, metadata extraction,
    diff calculation, branch creation, PR opening, and persistent state updates.
    """

    def __init__(
        self,
        config: SyncConfig | None = None,
        github_client: GitHubClient | None = None,
        git_ops: GitOps | None = None,
        work_dir: str | None = None,
        source_dir: str | None = None,
        target_dir: str | None = None,
        runner_id: str | None = None,
    ) -> None:
        """Initialize the SyncEngine with configuration and operational clients.

        Args:
            config: Optional SyncConfig instance. Defaults to cached settings.
            github_client: Optional GitHubClient instance for source/target API queries.
            git_ops: Optional GitOps instance for local git subprocess management.
            work_dir: Optional root working directory for cloned repos (default: '.sync_repos').
            source_dir: Optional path for source repository checkout.
            target_dir: Optional path for target repository checkout.
            runner_id: Unique identifier for distributed lock ownership.
        """
        self.config = config or get_settings()

        # GitHub API clients
        if github_client is not None:
            self.github_client = github_client
            self.target_github_client = github_client
        else:
            self.github_client = GitHubClient(
                token=self.config.SOURCE_GITHUB_TOKEN or self.config.GITHUB_TOKEN
            )
            target_token = (
                self.config.TARGET_GITHUB_TOKEN
                or self.config.SOURCE_GITHUB_TOKEN
                or self.config.GITHUB_TOKEN
            )
            self.target_github_client = GitHubClient(token=target_token)

        self.git_ops = git_ops or GitOps()

        # Workspace directories
        self.work_dir = work_dir or os.getenv("SYNC_WORK_DIR", ".sync_repos")
        self.source_dir = (
            source_dir or self.config.SOURCE_DIR or os.path.join(self.work_dir, "source")
        )
        self.target_dir = target_dir or os.path.join(self.work_dir, "target")

        # Distributed lock tracking
        self.runner_id = (
            runner_id
            or os.getenv("BUILD_TAG")
            or os.getenv("SYNC_RUNNER_ID")
            or f"sync-runner-{os.getpid()}"
        )
        self.lock_name = "occupify_sync"
        self._lock_held = False

        # Ensure database is ready
        if db._engine is None:
            db.init_db(self.config.sync_database_url)

    # -------------------------------------------------------------------------
    # Stage 1: Checkout Source
    # -------------------------------------------------------------------------
    def stage1_checkout_source(self) -> str:
        """Stage 1: Checkout Source Repository.

        Clones or fetches the source repository, verifies clean working tree,
        and retrieves the latest HEAD commit SHA.

        Returns:
            Latest commit SHA of source repository branch.
        """
        if self.config.SOURCE_DIR and os.path.isdir(os.path.join(self.source_dir, ".git")):
            logger.info(
                "Stage 1 [Checkout Source]: Using existing source repository at %s",
                self.source_dir,
                extra={"stage": 1, "event": "checkout_source_start"},
            )
            head_sha = self.git_ops.get_head_sha(self.source_dir, branch=self.config.SOURCE_BRANCH)
            logger.info(
                "Stage 1 [Checkout Source]: Successfully verified source at SHA %s",
                head_sha,
                extra={"stage": 1, "event": "checkout_source_success", "head_sha": head_sha},
            )
            return head_sha

        repo_url = self.config.SOURCE_CLONE_URL or self.config.SOURCE_REPO
        logger.info(
            "Stage 1 [Checkout Source]: Fetching source repo %s (branch: %s)...",
            repo_url,
            self.config.SOURCE_BRANCH,
            extra={"stage": 1, "event": "checkout_source_start"},
        )
        self.git_ops.clone_or_fetch(
            repo_url=repo_url,
            target_dir=self.source_dir,
            branch=self.config.SOURCE_BRANCH,
            token=self.config.SOURCE_GITHUB_TOKEN or self.config.GITHUB_TOKEN,
        )

        clean = self.git_ops.ensure_clean_working_tree(self.source_dir)
        if not clean:
            raise RuntimeError(
                f"Source repository at {self.source_dir} is in a dirty, unrecoverable state."
            )

        head_sha = self.git_ops.get_head_sha(self.source_dir, branch=self.config.SOURCE_BRANCH)
        logger.info(
            "Stage 1 [Checkout Source]: Successfully checked out source at SHA %s",
            head_sha,
            extra={"stage": 1, "event": "checkout_source_success", "head_sha": head_sha},
        )
        return head_sha

    # -------------------------------------------------------------------------
    # Stage 2: Load Checkpoint
    # -------------------------------------------------------------------------
    def stage2_load_checkpoint(self, source_head_sha: str | None = None) -> Checkpoint:
        """Stage 2: Load Checkpoint & Reconcile Integrated State.

        Acquires distributed lock, loads existing checkpoint (or initializes baseline
        with current source HEAD SHA), and reconciles existing EXPORTED PRs in Target Repo A.

        Args:
            source_head_sha: Optional source HEAD SHA to initialize new checkpoint baseline.

        Returns:
            Current active Checkpoint model.

        Raises:
            RuntimeError: If distributed lock acquisition fails.
        """
        logger.info(
            "Stage 2 [Load Checkpoint]: Acquiring distributed lock '%s' for %s...",
            self.lock_name,
            self.runner_id,
            extra={"stage": 2, "event": "lock_acquire_attempt"},
        )
        acquired = db.acquire_lock(
            lock_name=self.lock_name,
            locked_by=self.runner_id,
            timeout_seconds=self.config.LOCK_EXPIRY_SECONDS,
        )
        if not acquired:
            logger.error("Stage 2: Could not acquire distributed sync lock '%s'.", self.lock_name)
            raise RuntimeError(
                f"Failed to acquire distributed lock '{self.lock_name}'. Another sync is active."
            )
        self._lock_held = True

        # Retrieve or initialize checkpoint
        checkpoint = db.get_or_create_checkpoint(
            source_repo=self.config.SOURCE_REPO,
            target_repo=self.config.TARGET_REPO,
            initial_sha=source_head_sha or "",
        )

        logger.info(
            "Stage 2 [Load Checkpoint]: Loaded checkpoint (baseline SHA: %s, last_exported: %s, last_integrated: %s)",
            checkpoint.initial_checkpoint_sha,
            checkpoint.last_exported_sha,
            checkpoint.last_integrated_sha,
            extra={
                "stage": 2,
                "event": "checkpoint_loaded",
                "initial_sha": checkpoint.initial_checkpoint_sha,
            },
        )

        # Reconcile existing EXPORTED PRs in Target Repo A
        self._reconcile_exported_prs()

        # Reload updated checkpoint after reconciliation
        checkpoint = db.get_or_create_checkpoint(
            source_repo=self.config.SOURCE_REPO,
            target_repo=self.config.TARGET_REPO,
        )
        return checkpoint

    def _reconcile_exported_prs(self) -> None:
        """Check status of exported PRs in target repo and update DB accordingly."""
        target_owner, target_repo_name = parse_repo_owner_name(self.config.TARGET_REPO)
        exported_records = db.list_contributions(status="EXPORTED")

        for record in exported_records:
            if not record.destination_pr_number:
                continue

            try:
                pr_data = self.target_github_client.get_pr_details(
                    owner=target_owner,
                    repo=target_repo_name,
                    pr_number=record.destination_pr_number,
                )
                is_merged = bool(pr_data.get("merged", False))
                pr_state = pr_data.get("state")

                if is_merged:
                    logger.info(
                        "Reconciliation: Target PR #%d merged. Updating %s to INTEGRATED.",
                        record.destination_pr_number,
                        record.sync_key,
                        extra={"event": "pr_integrated", "dest_pr": record.destination_pr_number},
                    )
                    db.update_contribution_status(
                        sync_key=record.sync_key,
                        status="INTEGRATED",
                        dest_pr_number=record.destination_pr_number,
                        dest_pr_url=record.destination_pr_url,
                    )
                    db.update_checkpoint(
                        source_repo=self.config.SOURCE_REPO,
                        target_repo=self.config.TARGET_REPO,
                        last_integrated_sha=record.merge_commit_sha,
                    )
                elif pr_state == "closed":
                    logger.info(
                        "Reconciliation: Target PR #%d closed without merge. Updating %s to REJECTED.",
                        record.destination_pr_number,
                        record.sync_key,
                        extra={"event": "pr_rejected", "dest_pr": record.destination_pr_number},
                    )
                    db.update_contribution_status(
                        sync_key=record.sync_key,
                        status="REJECTED",
                        dest_pr_number=record.destination_pr_number,
                        dest_pr_url=record.destination_pr_url,
                    )
                elif pr_state == "open":
                    # Active target PR is open. Reset any CONFLICT records so rolling sync can retry them cleanly.
                    conflict_records = db.list_contributions(status="CONFLICT")
                    for c_rec in conflict_records:
                        logger.info(
                            "Reconciliation: Active target PR #%d is open. Resetting %s from CONFLICT to PENDING for rolling sync.",
                            record.destination_pr_number,
                            c_rec.sync_key,
                            extra={
                                "event": "conflict_reset_for_rolling_sync",
                                "dest_pr": record.destination_pr_number,
                            },
                        )
                        db.update_contribution_status(
                            sync_key=c_rec.sync_key,
                            status="PENDING",
                            error_message=None,
                        )
            except Exception as exc:
                logger.warning(
                    "Reconciliation check failed for destination PR #%d: %s",
                    record.destination_pr_number,
                    exc,
                )

        # Check active open target PR directly via GitHub query and reset any conflicts
        active_rec, active_pr = self.get_active_open_target_pr()
        if active_pr and active_pr.get("state") == "open":
            conflict_records = db.list_contributions(status="CONFLICT")
            for c_rec in conflict_records:
                dest_pr_id = active_pr.get("number")
                logger.info(
                    "Reconciliation: Active target PR #%s is open on GitHub. Resetting %s from CONFLICT to PENDING for rolling sync.",
                    dest_pr_id,
                    c_rec.sync_key,
                    extra={
                        "event": "conflict_reset_for_rolling_sync",
                        "dest_pr": dest_pr_id,
                    },
                )
                db.update_contribution_status(
                    sync_key=c_rec.sync_key,
                    status="PENDING",
                    error_message=None,
                )

    def get_active_open_target_pr(
        self,
    ) -> tuple[ContributionRecord | None, dict[str, Any] | None]:
        """Find an active open sync PR on Target Repo A directly from GitHub and DB.

        Returns:
            Tuple of (ContributionRecord, pr_details_dict) if open target PR exists, else (None, None).
        """
        target_owner, target_repo_name = parse_repo_owner_name(self.config.TARGET_REPO)

        # 1. Primary: Direct query on GitHub for active open sync PRs
        try:
            open_prs = self.target_github_client.get_open_prs(
                owner=target_owner,
                repo=target_repo_name,
                base_branch=self.config.TARGET_BRANCH,
            )
            for pr in open_prs:
                head_ref = (pr.get("head") or {}).get("ref", "")
                if head_ref.startswith("sync/b/"):
                    dest_pr_num = pr["number"]
                    dest_pr_url = pr.get("html_url")

                    # Look up or create corresponding record
                    exported_records = db.list_contributions(status="EXPORTED")
                    matched_rec = next(
                        (
                            r
                            for r in exported_records
                            if r.destination_pr_number == dest_pr_num or r.sync_branch == head_ref
                        ),
                        None,
                    )
                    if matched_rec is None:
                        match = re.search(r"pr-(\d+)", head_ref)
                        src_num = int(match.group(1)) if match else 0
                        matched_rec = ContributionRecord(
                            sync_key=f"PR_{src_num}",
                            source_pr_number=src_num,
                            source_branch=head_ref,
                            target_branch=self.config.TARGET_BRANCH,
                            sync_branch=head_ref,
                            destination_pr_number=dest_pr_num,
                            destination_pr_url=dest_pr_url,
                            status="EXPORTED",
                            merged_at=datetime.now(UTC),
                        )
                    else:
                        matched_rec.destination_pr_number = dest_pr_num
                        matched_rec.destination_pr_url = dest_pr_url
                        matched_rec.sync_branch = head_ref
                        db.record_contribution(matched_rec)

                    return matched_rec, pr
        except Exception as exc:
            logger.debug("Direct GitHub query for open PRs failed: %s", exc)

        # 2. Secondary fallback: DB inspection
        exported_records = db.list_contributions(status="EXPORTED")
        for rec in exported_records:
            if not rec.destination_pr_number:
                continue
            try:
                pr_data = self.target_github_client.get_pr_details(
                    owner=target_owner,
                    repo=target_repo_name,
                    pr_number=rec.destination_pr_number,
                )
                if pr_data.get("state") == "open":
                    return rec, pr_data
            except Exception as exc:
                logger.debug(
                    "Failed querying destination PR #%s: %s",
                    rec.destination_pr_number,
                    exc,
                )

        return None, None

    # -------------------------------------------------------------------------
    # Stage 3: Find New Merged PRs
    # -------------------------------------------------------------------------
    def stage3_find_new_prs(self, checkpoint: Checkpoint | None = None) -> list[dict[str, Any]]:
        """Stage 3: Find New Merged Pull Requests.

        Queries GitHub API for closed PRs targeting source main merged after initial_checkpoint,
        filters out already processed PRs in DB, and sorts chronologically by merge date.

        Args:
            checkpoint: Active Checkpoint instance. If None, loaded from database.

        Returns:
            List of eligible merged pull request dictionaries ordered by merge date.
        """
        if checkpoint is None:
            checkpoint = db.get_or_create_checkpoint(
                source_repo=self.config.SOURCE_REPO,
                target_repo=self.config.TARGET_REPO,
            )

        source_owner, source_repo_name = parse_repo_owner_name(self.config.SOURCE_REPO)
        logger.info(
            "Stage 3 [Find New Merged PRs]: Querying closed PRs from %s/%s (branch: %s)...",
            source_owner,
            source_repo_name,
            self.config.SOURCE_BRANCH,
            extra={"stage": 3, "event": "find_prs_start"},
        )

        try:
            closed_prs = self.github_client.get_closed_prs(
                owner=source_owner,
                repo=source_repo_name,
                base_branch=self.config.SOURCE_BRANCH,
            )
        except Exception as exc:
            logger.warning(
                "Stage 3: GitHub API query for %s/%s failed (%s). Falling back to local git history inspection.",
                source_owner,
                source_repo_name,
                exc,
            )
            closed_prs = self.git_ops.find_merged_prs_from_history(
                repo_dir=self.source_dir,
                since_commit=checkpoint.initial_checkpoint_sha,
                branch=self.config.SOURCE_BRANCH,
            )

        eligible_prs: list[dict[str, Any]] = []
        init_ts = checkpoint.initial_checkpoint_timestamp
        if init_ts.tzinfo is None:
            init_ts = init_ts.replace(tzinfo=UTC)

        for pr in closed_prs:
            merged_at_str = pr.get("merged_at")
            if not merged_at_str:
                continue

            merged_at = datetime.fromisoformat(merged_at_str)
            if merged_at.tzinfo is None:
                merged_at = merged_at.replace(tzinfo=UTC)

            # Skip PRs merged before or at the initial activation checkpoint
            if merged_at <= init_ts:
                continue

            merge_sha = pr.get("merge_commit_sha") or ""
            if checkpoint.initial_checkpoint_sha and merge_sha == checkpoint.initial_checkpoint_sha:
                continue

            # Check if already processed in database
            pr_number = pr["number"]
            sync_key = f"PR_{pr_number}"
            existing = db.get_contribution(sync_key)
            if existing is not None and existing.status in (
                "EXPORTED",
                "INTEGRATED",
                "REJECTED",
                "CONFLICT",
            ):
                continue

            eligible_prs.append(pr)

        # Sort chronologically by merge date ascending
        eligible_prs.sort(key=lambda p: p.get("merged_at") or "")

        logger.info(
            "Stage 3 [Find New Merged PRs]: Found %d eligible merged PR(s) to synchronize.",
            len(eligible_prs),
            extra={"stage": 3, "event": "find_prs_complete", "count": len(eligible_prs)},
        )

        # Ensure pending records exist in DB for tracking
        for pr in eligible_prs:
            pr_num = pr["number"]
            sync_key = f"PR_{pr_num}"
            existing = db.get_contribution(sync_key)
            if existing is None:
                merged_at_dt = datetime.fromisoformat(pr["merged_at"])
                new_record = ContributionRecord(
                    sync_key=sync_key,
                    source_pr_number=pr_num,
                    source_branch=pr.get("head_branch")
                    or (pr.get("head") or {}).get("ref", "unknown"),
                    target_branch=self.config.TARGET_BRANCH,
                    merge_commit_sha=pr.get("merge_commit_sha") or "",
                    merged_at=merged_at_dt,
                    status="PENDING",
                )
                db.record_contribution(new_record)

        return eligible_prs

    # -------------------------------------------------------------------------
    # Stage 4: Extract Contributions
    # -------------------------------------------------------------------------
    def stage4_extract_contributions(
        self, pr_or_number: dict[str, Any] | int | ContributionRecord
    ) -> ContributionRecord:
        """Stage 4: Extract Contributions.

        Fetches PR commits, changed files, and contributors from GitHub API,
        or falls back to local git history between parents if API is unavailable.
        Builds a contributor manifest, and updates the database record.

        Args:
            pr_or_number: Pull request dict, PR number, or existing ContributionRecord.

        Returns:
            Updated ContributionRecord domain model with contributors and changed files.
        """
        source_owner, source_repo_name = parse_repo_owner_name(self.config.SOURCE_REPO)

        parent1_sha = None
        parent2_sha = None
        if isinstance(pr_or_number, dict):
            pr_number = pr_or_number["number"]
            parent1_sha = pr_or_number.get("parent1_sha")
            parent2_sha = pr_or_number.get("parent2_sha")
        elif isinstance(pr_or_number, ContributionRecord):
            pr_number = pr_or_number.source_pr_number
        else:
            pr_number = int(pr_or_number)

        sync_key = f"PR_{pr_number}"
        record = db.get_contribution(sync_key)
        if record is None:
            # Create stub if not present
            record = ContributionRecord(
                sync_key=sync_key,
                source_pr_number=pr_number,
                source_branch="unknown",
                target_branch=self.config.TARGET_BRANCH,
                merge_commit_sha="",
                merged_at=datetime.now(UTC),
                status="PENDING",
            )

        logger.info(
            "Stage 4 [Extract Contributions]: Extracting metadata for PR #%d...",
            pr_number,
            extra={"stage": 4, "event": "extract_contributions_start", "pr_number": pr_number},
        )

        commits: list[dict[str, Any]] = []
        changed_files: list[str] = []

        try:
            commits = self.github_client.get_pr_commits(source_owner, source_repo_name, pr_number)
            changed_files = self.github_client.get_pr_files(
                source_owner, source_repo_name, pr_number
            )
        except Exception as exc:
            logger.warning(
                "Stage 4: GitHub API extraction for PR #%d failed (%s). Extracting directly from local git history.",
                pr_number,
                exc,
            )
            # Resolve parents from merge commit sha if not passed
            if not parent1_sha and record.merge_commit_sha:
                from sync_engine.git_ops import _run_git

                parents_proc = _run_git(
                    ["git", "log", "-1", "--format=%P", record.merge_commit_sha],
                    cwd=self.source_dir,
                    check=False,
                )
                if parents_proc.returncode == 0 and len(parents_proc.stdout.strip().split()) >= 2:
                    p_list = parents_proc.stdout.strip().split()
                    parent1_sha, parent2_sha = p_list[0], p_list[1]

            if parent1_sha and parent2_sha:
                raw_commits = self.git_ops.get_pr_commits_from_history(
                    self.source_dir, parent1_sha, parent2_sha
                )
                commits = [
                    {
                        "sha": rc["sha"],
                        "author_login": rc["author"]["login"],
                        "author_name": rc["commit"]["author"]["name"],
                        "author_email": rc["commit"]["author"]["email"],
                        "commit_message": rc["commit"]["message"],
                        "author_date": rc["commit"]["author"]["date"],
                    }
                    for rc in raw_commits
                ]
                changed_files = self.git_ops.get_pr_files_from_history(
                    self.source_dir, parent1_sha, parent2_sha
                )

        # Aggregate contributors by login/name
        contributors_map: dict[str, Contributor] = {}
        for c in commits:
            login = c.get("author_login") or c.get("author_name") or "unknown"
            if login not in contributors_map:
                contributors_map[login] = Contributor(
                    username=login,
                    name=c.get("author_name"),
                    email=c.get("author_email"),
                    commits=[],
                )
            if c.get("sha"):
                contributors_map[login].commits.append(c["sha"])

        contributor_dicts = [contributor.to_dict() for contributor in contributors_map.values()]
        record.contributors = contributor_dicts
        record.changed_files = changed_files

        db.record_contribution(record)
        logger.info(
            "Stage 4 [Extract Contributions]: PR #%d metadata extracted (%d contributors, %d files).",
            pr_number,
            len(contributor_dicts),
            len(changed_files),
            extra={
                "stage": 4,
                "event": "extract_contributions_success",
                "pr_number": pr_number,
                "contributors": len(contributor_dicts),
                "files": len(changed_files),
            },
        )
        return record

    # -------------------------------------------------------------------------
    # Stage 5: Calculate Diff
    # -------------------------------------------------------------------------
    def stage5_calculate_diff(
        self,
        record: ContributionRecord,
        pr_data: dict[str, Any] | None = None,
    ) -> str:
        """Stage 5: Calculate Diff.

        Calculates the unified diff patch representing the exact code changes
        introduced by the pull request.

        Args:
            record: ContributionRecord being synchronized.
            pr_data: Optional GitHub PR dictionary containing base and head SHAs.

        Returns:
            Unified diff patch string.
        """
        logger.info(
            "Stage 5 [Calculate Diff]: Computing patch for PR #%d...",
            record.source_pr_number,
            extra={
                "stage": 5,
                "event": "calculate_diff_start",
                "pr_number": record.source_pr_number,
            },
        )

        base_sha = (pr_data.get("base") or {}).get("sha") if pr_data else None
        head_sha = (pr_data.get("head") or {}).get("sha") if pr_data else None
        patch = ""

        # Attempt PR base..head diff if both commits are locally available
        if base_sha and head_sha:
            try:
                patch = self.git_ops.calculate_patch(self.source_dir, base_sha, head_sha)
            except Exception as exc:
                logger.debug(
                    "Direct base..head patch calculation failed for %s..%s: %s",
                    base_sha,
                    head_sha,
                    exc,
                )

        # Fallback to merge commit parent diff
        if not patch and record.merge_commit_sha:
            try:
                patch = self.git_ops.calculate_patch(
                    self.source_dir,
                    f"{record.merge_commit_sha}^1",
                    record.merge_commit_sha,
                )
            except Exception as exc:
                logger.debug(
                    "Merge commit parent diff failed for %s: %s",
                    record.merge_commit_sha,
                    exc,
                )

        logger.info(
            "Stage 5 [Calculate Diff]: Patch computed for PR #%d (length: %d chars).",
            record.source_pr_number,
            len(patch),
            extra={
                "stage": 5,
                "event": "calculate_diff_success",
                "pr_number": record.source_pr_number,
                "patch_length": len(patch),
            },
        )
        return patch

    # -------------------------------------------------------------------------
    # Stage 6: Synchronize to Occupify Agentic (Target Repo)
    # -------------------------------------------------------------------------
    def stage6_sync_target(
        self,
        record: ContributionRecord,
        patch_text: str,
        pr_data: dict[str, Any] | None = None,
    ) -> tuple[bool, str | None]:
        """Stage 6: Synchronize to Target Repository.

        Fetches Target Repo A, creates a synchronization branch `sync/b/pr-{number}-{slug}`,
        and applies the patch/commits with author attribution and Co-authored-by trailers.
        On conflict, rolls back cleanly and records status CONFLICT in the database.

        Args:
            record: ContributionRecord being synchronized.
            patch_text: Patch diff string from Stage 5.
            pr_data: Optional PR metadata dictionary.

        Returns:
            Tuple of (success: bool, error_message: str | None).
        """
        logger.info(
            "Stage 6 [Synchronize to Target]: Syncing PR #%d to Target Repo %s...",
            record.source_pr_number,
            self.config.TARGET_REPO,
            extra={"stage": 6, "event": "sync_target_start", "pr_number": record.source_pr_number},
        )

        # Clone or fetch target repository
        self.git_ops.clone_or_fetch(
            repo_url=self.config.TARGET_REPO,
            target_dir=self.target_dir,
            branch=self.config.TARGET_BRANCH,
            token=self.config.TARGET_GITHUB_TOKEN or self.config.GITHUB_TOKEN,
        )
        self.git_ops.ensure_clean_working_tree(self.target_dir)

        # Check if an active open target PR already exists on Target Repo A
        active_rec, active_pr = self.get_active_open_target_pr()
        if active_rec and active_rec.sync_branch:
            branch_name = active_rec.sync_branch
            record.sync_branch = branch_name
            dest_pr_num = active_pr.get("number") if active_pr else active_rec.destination_pr_number
            logger.info(
                "Stage 6 [Synchronize to Target]: Active open target PR #%s detected on branch %s. Rolling changes into active branch...",
                dest_pr_num,
                branch_name,
                extra={
                    "stage": 6,
                    "event": "rolling_branch_reuse",
                    "branch": branch_name,
                    "dest_pr": dest_pr_num,
                },
            )
            # Ensure branch is fetched and checkout branch
            self.git_ops.fetch_branch(
                self.target_dir,
                branch_name,
                token=self.config.TARGET_GITHUB_TOKEN or self.config.GITHUB_TOKEN,
            )
            self.git_ops.create_branch(
                self.target_dir,
                branch_name,
                start_point=branch_name,
            )
        else:
            # Generate clean branch slug
            raw_slug = record.source_branch or "patch"
            clean_slug = re.sub(r"[^a-zA-Z0-9_-]", "-", raw_slug).strip("-")[:30] or "sync"
            branch_name = f"sync/b/pr-{record.source_pr_number}-{clean_slug}"
            record.sync_branch = branch_name

            # Create branch from target branch HEAD
            self.git_ops.create_branch(
                self.target_dir,
                branch_name,
                start_point=f"origin/{self.config.TARGET_BRANCH}",
            )

        # Resolve primary author attribution and co-authors
        author_name = "Occupify Contributor"
        author_email = "contributor@occupify.local"
        author_date = record.merged_at.isoformat()
        co_authors: list[tuple[str, str]] = []

        if record.contributors:
            first_c = record.contributors[0]
            author_name = first_c.get("name") or first_c.get("username") or author_name
            author_email = first_c.get("email") or author_email

            for other_c in record.contributors[1:]:
                c_name = other_c.get("name") or other_c.get("username")
                c_email = other_c.get("email")
                if c_name and c_email:
                    co_authors.append((c_name, c_email))

        pr_title = (pr_data or {}).get(
            "title"
        ) or f"Contribution from PR #{record.source_pr_number}"
        commit_message = f"Sync contribution from PR #{record.source_pr_number}: {pr_title}"

        # Apply patch and commit with author attribution
        success, error_msg = self.git_ops.apply_patch_or_commit(
            repo_dir=self.target_dir,
            patch_text=patch_text,
            author_name=author_name,
            author_email=author_email,
            author_date=author_date,
            commit_message=commit_message,
            co_authors=co_authors,
        )

        if not success:
            logger.warning(
                "Stage 6 [Synchronize to Target]: Conflict detected for PR #%d: %s",
                record.source_pr_number,
                error_msg,
                extra={"stage": 6, "event": "sync_conflict", "error": error_msg},
            )
            record.status = "CONFLICT"
            record.error_message = error_msg
            db.update_contribution_status(
                record.sync_key,
                status="CONFLICT",
                error_message=error_msg,
            )
            return False, error_msg

        db.record_contribution(record)
        logger.info(
            "Stage 6 [Synchronize to Target]: Applied changes to branch %s successfully.",
            branch_name,
            extra={"stage": 6, "event": "sync_target_success", "branch": branch_name},
        )
        return True, None

    # -------------------------------------------------------------------------
    # Stage 7: Create Pull Request
    # -------------------------------------------------------------------------
    def stage7_create_pr(
        self,
        record: ContributionRecord,
        pr_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Stage 7: Create Pull Request.

        Pushes the sync branch to Target Repo A and opens a Pull Request
        targeting A's main with formatted metadata and contributor attribution.
        In dry-run mode, logs the intended actions and returns simulated PR data.

        Args:
            record: ContributionRecord being synchronized.
            pr_data: Optional PR metadata dictionary.

        Returns:
            Dictionary containing created destination pull request data.
        """
        target_owner, target_repo_name = parse_repo_owner_name(self.config.TARGET_REPO)
        branch_name = record.sync_branch or f"sync/b/pr-{record.source_pr_number}-sync"
        pr_title = (pr_data or {}).get(
            "title"
        ) or f"[Sync] #{record.source_pr_number}: {record.source_branch}"
        if not pr_title.startswith("[Sync]"):
            pr_title = f"[Sync] #{record.source_pr_number}: {pr_title}"

        # Markdown description
        contributors_md = _format_contributors_markdown(record.contributors)
        files_md = _format_files_markdown(record.changed_files)
        body = f"""## Source Contribution

- Repository: {self.config.SOURCE_REPO}
- Original PR: #{record.source_pr_number}
- Source branch: {record.source_branch}
- Target branch: {record.target_branch}
- Merge commit: {record.merge_commit_sha}
- Sync Tracking ID: {record.sync_key}

## Contributors

{contributors_md}

## Changes

{files_md}

## Synchronization

- Managed by Occupify Contribution Sync Engine
- Synchronization branch: {branch_name}
"""

        # Check if an active open target PR already exists on Target Repo A
        active_rec, active_pr = self.get_active_open_target_pr()
        if active_rec and active_pr:
            dest_pr_number = int(active_pr["number"])
            dest_pr_url = active_pr.get("html_url") or (
                f"https://github.com/{target_owner}/{target_repo_name}/pull/{dest_pr_number}"
            )
            branch_name = active_rec.sync_branch or branch_name

            logger.info(
                "Stage 7 [Create PR]: Force-pushing rolling branch %s to Target Repo %s for active PR #%d...",
                branch_name,
                self.config.TARGET_REPO,
                dest_pr_number,
                extra={
                    "stage": 7,
                    "event": "rolling_pr_force_push",
                    "branch": branch_name,
                    "dest_pr": dest_pr_number,
                },
            )

            if not self.config.DRY_RUN:
                self.git_ops.push_branch(
                    repo_dir=self.target_dir,
                    branch_name=branch_name,
                    remote_url=self.config.TARGET_REPO,
                    token=self.config.TARGET_GITHUB_TOKEN or self.config.GITHUB_TOKEN,
                    force=True,
                )

                existing_body = active_pr.get("body") or ""
                new_entry = (
                    f"\n\n### Integrated PR #{record.source_pr_number}: {record.source_branch}\n"
                    f"- Merge commit: `{record.merge_commit_sha}`\n"
                    f"- Tracking ID: `{record.sync_key}`\n\n"
                    f"#### Contributors\n{contributors_md}\n\n"
                    f"#### Changed Files\n{files_md}"
                )
                updated_body = existing_body + new_entry

                try:
                    self.target_github_client.update_pull_request(
                        owner=target_owner,
                        repo=target_repo_name,
                        pr_number=dest_pr_number,
                        body=updated_body,
                    )
                    logger.info(
                        "Stage 7 [Create PR]: Successfully updated description for active destination PR #%d.",
                        dest_pr_number,
                    )
                except Exception as exc:
                    logger.warning(
                        "Stage 7 [Create PR]: Could not update description for destination PR #%d: %s",
                        dest_pr_number,
                        exc,
                    )

            record.destination_pr_number = dest_pr_number
            record.destination_pr_url = dest_pr_url
            db.record_contribution(record)
            return active_pr

        if self.config.DRY_RUN:
            simulated_pr_num = 9999 + record.source_pr_number
            simulated_url = (
                f"https://github.com/{target_owner}/{target_repo_name}/pull/{simulated_pr_num}"
            )
            logger.info(
                "[DRY-RUN] Would push branch %s and open PR in %s/%s (%s)",
                branch_name,
                target_owner,
                target_repo_name,
                pr_title,
                extra={"dry_run": True, "event": "dry_run_create_pr"},
            )
            return {
                "number": simulated_pr_num,
                "html_url": simulated_url,
                "title": pr_title,
                "head": {"ref": branch_name},
                "base": {"ref": self.config.TARGET_BRANCH},
            }

        # Push synchronization branch
        logger.info(
            "Stage 7 [Create PR]: Pushing branch %s to %s...",
            branch_name,
            self.config.TARGET_REPO,
            extra={"stage": 7, "event": "push_branch_start", "branch": branch_name},
        )
        self.git_ops.push_branch(
            repo_dir=self.target_dir,
            branch_name=branch_name,
            remote_url=self.config.TARGET_REPO,
            token=self.config.TARGET_GITHUB_TOKEN or self.config.GITHUB_TOKEN,
        )

        # Create destination pull request
        logger.info(
            "Stage 7 [Create PR]: Opening PR in %s/%s targeting %s...",
            target_owner,
            target_repo_name,
            self.config.TARGET_BRANCH,
            extra={"stage": 7, "event": "open_pr_start"},
        )
        created_pr = self.target_github_client.create_pull_request(
            owner=target_owner,
            repo=target_repo_name,
            title=pr_title,
            head_branch=branch_name,
            base_branch=self.config.TARGET_BRANCH,
            body=body,
        )

        logger.info(
            "Stage 7 [Create PR]: Created destination PR #%s (%s)",
            created_pr.get("number"),
            created_pr.get("html_url"),
            extra={
                "stage": 7,
                "event": "open_pr_success",
                "dest_pr_number": created_pr.get("number"),
                "dest_pr_url": created_pr.get("html_url"),
            },
        )
        return created_pr

    # -------------------------------------------------------------------------
    # Stage 8: Update Sync State
    # -------------------------------------------------------------------------
    def stage8_update_state(
        self,
        record: ContributionRecord,
        dest_pr_data: dict[str, Any] | None = None,
        release_lock: bool = True,
    ) -> None:
        """Stage 8: Update Sync State.

        Persists destination PR details and status EXPORTED in the database,
        advances checkpoint last_exported_sha, and optionally releases distributed lock.

        Args:
            record: ContributionRecord being synchronized.
            dest_pr_data: Created pull request data from Stage 7.
            release_lock: Whether to release distributed lock (default True).
        """
        dest_num = (dest_pr_data or {}).get("number") or record.destination_pr_number
        dest_url = (dest_pr_data or {}).get("html_url") or record.destination_pr_url

        record.destination_pr_number = dest_num
        record.destination_pr_url = dest_url
        record.status = "EXPORTED"

        if self.config.DRY_RUN:
            logger.info(
                "[DRY-RUN] Would update %s status to EXPORTED (dest PR: #%s) and advance checkpoint.",
                record.sync_key,
                dest_num,
                extra={"dry_run": True, "event": "dry_run_update_state"},
            )
        else:
            db.update_contribution_status(
                sync_key=record.sync_key,
                status="EXPORTED",
                dest_pr_number=dest_num,
                dest_pr_url=dest_url,
            )
            db.update_checkpoint(
                source_repo=self.config.SOURCE_REPO,
                target_repo=self.config.TARGET_REPO,
                last_exported_sha=record.merge_commit_sha,
            )
            logger.info(
                "Stage 8 [Update State]: Recorded %s as EXPORTED (dest PR #%s).",
                record.sync_key,
                dest_num,
                extra={"stage": 8, "event": "update_state_success", "dest_pr": dest_num},
            )

        if release_lock:
            self.release_distributed_lock()

    def release_distributed_lock(self, force: bool = False) -> None:
        """Release distributed lock if currently held by this runner or forced."""
        logger.info(
            "Releasing distributed sync lock '%s' for %s (force=%s)...",
            self.lock_name,
            self.runner_id,
            force,
            extra={"event": "lock_release"},
        )
        db.release_lock(lock_name=self.lock_name, locked_by=None if force else self.runner_id)
        self._lock_held = False

    # -------------------------------------------------------------------------
    # End-to-End Coordination
    # -------------------------------------------------------------------------
    def run_all(self) -> dict[str, Any]:
        """Execute all 8 stages end-to-end.

        Coordinates checkout, checkpoint loading, PR discovery, diff extraction,
        synchronization branch creation, PR opening, and persistent state updates.

        Returns:
            Dictionary summarizing synchronization results.
        """
        logger.info(
            "Starting Occupify Contribution Sync Pipeline (dry_run=%s)...",
            self.config.DRY_RUN,
            extra={"event": "pipeline_start", "dry_run": self.config.DRY_RUN},
        )
        synced_prs: list[dict[str, Any]] = []

        try:
            # Stage 1: Checkout Source
            head_sha = self.stage1_checkout_source()

            # Stage 2: Load Checkpoint
            checkpoint = self.stage2_load_checkpoint(source_head_sha=head_sha)

            # Stage 3: Find New Merged PRs
            eligible_prs = self.stage3_find_new_prs(checkpoint=checkpoint)
            if not eligible_prs:
                logger.info(
                    "Pipeline: No new merged PRs found since checkpoint. Synchronization complete."
                )
                return {
                    "status": "SUCCESS",
                    "message": "No new PRs to synchronize",
                    "synced_prs": [],
                }

            # Process eligible PRs sequentially
            for pr in eligible_prs:
                pr_num = pr["number"]
                logger.info("--- Processing source PR #%d ---", pr_num)

                # Stage 4: Extract Contributions
                record = self.stage4_extract_contributions(pr)

                # Stage 5: Calculate Diff
                patch = self.stage5_calculate_diff(record, pr_data=pr)

                # Stage 6: Synchronize to Occupify Agentic (Target Repo)
                success, error_msg = self.stage6_sync_target(record, patch, pr_data=pr)
                if not success:
                    logger.error(
                        "Conflict detected on PR #%d. Halting synchronization safely: %s",
                        pr_num,
                        error_msg,
                    )
                    return {
                        "status": "CONFLICT",
                        "pr_number": pr_num,
                        "error": error_msg,
                        "synced_prs": synced_prs,
                    }

                # Stage 7: Create Pull Request
                dest_pr = self.stage7_create_pr(record, pr_data=pr)

                # Stage 8: Update Sync State
                self.stage8_update_state(record, dest_pr_data=dest_pr, release_lock=False)

                synced_prs.append(
                    {
                        "source_pr": pr_num,
                        "destination_pr": dest_pr.get("number"),
                        "destination_url": dest_pr.get("html_url"),
                    }
                )

            return {
                "status": "SUCCESS",
                "message": f"Successfully synchronized {len(synced_prs)} PR(s)",
                "synced_prs": synced_prs,
            }

        finally:
            self.release_distributed_lock()
