"""Command Line Interface for Occupify Contribution Sync Engine.

Provides CLI subcommands for database initialization, status inspection,
individual pipeline stages (1-8), and full end-to-end execution.
"""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import UTC, datetime
from typing import Any

from sync_engine import db
from sync_engine.config import SyncConfig, get_settings
from sync_engine.engine import SyncEngine
from sync_engine.models import ContributionRecord

logger = logging.getLogger("sync_engine.cli")


def _setup_logging(verbose: bool = False) -> None:
    """Configure unified logging format and level."""
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def _get_engine(args: argparse.Namespace) -> SyncEngine:
    """Construct SyncEngine configured with CLI argument overrides."""
    base_cfg = get_settings()
    overrides: dict[str, Any] = {}

    if getattr(args, "source_repo", None):
        overrides["SOURCE_REPO"] = args.source_repo
    if getattr(args, "target_repo", None):
        overrides["TARGET_REPO"] = args.target_repo
    if getattr(args, "db_url", None):
        overrides["DATABASE_URL"] = args.db_url
    if getattr(args, "dry_run", False):
        overrides["DRY_RUN"] = True

    cfg = SyncConfig(**{**base_cfg.model_dump(), **overrides})
    return SyncEngine(config=cfg)


def cmd_init_db(args: argparse.Namespace) -> int:
    """Initialize database tables."""
    engine = _get_engine(args)
    db.init_db(engine.config.sync_database_url)
    print("Database tables initialized successfully.")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    """Display current synchronization checkpoints, active locks, and recent contributions."""
    engine = _get_engine(args)
    db.init_db(engine.config.sync_database_url)

    print("=" * 60)
    print("Occupify Contribution Sync Engine - Status Report")
    print("=" * 60)

    # Checkpoint
    checkpoint = db.get_or_create_checkpoint(
        source_repo=engine.config.SOURCE_REPO,
        target_repo=engine.config.TARGET_REPO,
    )
    print("\n[Checkpoint]")
    print(f"  Source Repository  : {checkpoint.source_repo}")
    print(f"  Target Repository  : {checkpoint.target_repo}")
    print(f"  Initial Baseline   : {checkpoint.initial_checkpoint_sha or '(none)'}")
    print(f"  Baseline Timestamp : {checkpoint.initial_checkpoint_timestamp}")
    print(f"  Last Exported SHA  : {checkpoint.last_exported_sha or '(none)'}")
    print(f"  Last Integrated SHA: {checkpoint.last_integrated_sha or '(none)'}")

    # Active lock inspection
    print("\n[Active Sync Lock]")
    with db.get_session() as session:
        lock = session.query(db.SyncLockModel).filter_by(lock_name=engine.lock_name).first()
        now = datetime.now(UTC)
        if lock is not None:
            expires_at = lock.expires_at
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=UTC)
            if expires_at > now:
                print("  Status    : LOCKED")
                print(f"  Locked By : {lock.locked_by}")
                print(f"  Acquired  : {lock.acquired_at}")
                print(f"  Expires   : {lock.expires_at}")
            else:
                print(f"  Status    : EXPIRED (held by {lock.locked_by})")
        else:
            print("  Status    : UNLOCKED (no active lock)")

    # Recent contributions
    print("\n[Recent Contributions]")
    contributions = db.list_contributions()
    if not contributions:
        print("  No contributions tracked yet.")
    else:
        for c in contributions[-10:]:
            print(
                f"  - Key: {c.sync_key} | Source PR: #{c.source_pr_number} | "
                f"Status: {c.status} | Dest PR: {c.destination_pr_number or '-'} | "
                f"Merged: {c.merged_at.strftime('%Y-%m-%d %H:%M:%S') if c.merged_at else '-'}"
            )
            if c.error_message:
                print(f"    Error: {c.error_message}")

    print("=" * 60)
    return 0


def cmd_checkout_source(args: argparse.Namespace) -> int:
    """Execute Stage 1: Checkout Source."""
    engine = _get_engine(args)
    head_sha = engine.stage1_checkout_source()
    print(f"Stage 1 Complete: Source HEAD SHA is {head_sha}")
    return 0


def cmd_load_checkpoint(args: argparse.Namespace) -> int:
    """Execute Stage 2: Load Checkpoint."""
    engine = _get_engine(args)
    checkpoint = engine.stage2_load_checkpoint()
    print(
        f"Stage 2 Complete: Loaded checkpoint. Baseline: {checkpoint.initial_checkpoint_sha or '(none)'}"
    )
    return 0


def cmd_find_prs(args: argparse.Namespace) -> int:
    """Execute Stage 3: Find New Merged PRs."""
    engine = _get_engine(args)
    prs = engine.stage3_find_new_prs()
    print(f"Stage 3 Complete: Found {len(prs)} eligible merged PR(s).")
    for p in prs:
        print(f"  - PR #{p['number']}: {p.get('title')} (merged: {p.get('merged_at')})")
    return 0


def _get_target_contribution(args: argparse.Namespace) -> ContributionRecord | None:
    """Find specific contribution by --pr flag or first pending record in DB."""
    pr_num = getattr(args, "pr", None)
    if pr_num is not None:
        sync_key = f"PR_{pr_num}"
        record = db.get_contribution(sync_key)
        if record is None:
            raise ValueError(f"Contribution record with sync key '{sync_key}' not found.")
        return record

    pending = db.list_contributions(status="PENDING")
    if pending:
        return pending[0]
    return None


def cmd_extract_contributions(args: argparse.Namespace) -> int:
    """Execute Stage 4: Extract Contributions."""
    engine = _get_engine(args)
    record = _get_target_contribution(args)
    if record is None:
        print("Stage 4: No pending contribution found to extract.")
        return 0

    record = engine.stage4_extract_contributions(record)
    print(
        f"Stage 4 Complete: Extracted {len(record.contributors)} contributor(s), "
        f"{len(record.changed_files)} file(s) for PR #{record.source_pr_number}."
    )
    return 0


def cmd_calculate_diff(args: argparse.Namespace) -> int:
    """Execute Stage 5: Calculate Diff."""
    engine = _get_engine(args)
    record = _get_target_contribution(args)
    if record is None:
        print("Stage 5: No pending contribution found to calculate diff.")
        return 0

    patch = engine.stage5_calculate_diff(record)
    print(
        f"Stage 5 Complete: Computed diff for PR #{record.source_pr_number} ({len(patch)} characters)."
    )
    return 0


def cmd_sync_target(args: argparse.Namespace) -> int:
    """Execute Stage 6: Synchronize to Target Repo."""
    engine = _get_engine(args)
    record = _get_target_contribution(args)
    if record is None:
        print("Stage 6: No pending contribution found to synchronize.")
        return 0

    patch = engine.stage5_calculate_diff(record)
    success, error_msg = engine.stage6_sync_target(record, patch)
    if not success:
        print(f"Stage 6 Failed: Conflict detected: {error_msg}", file=sys.stderr)
        return 1

    print(
        f"Stage 6 Complete: Applied PR #{record.source_pr_number} to target branch '{record.sync_branch}'."
    )
    return 0


def cmd_create_pr(args: argparse.Namespace) -> int:
    """Execute Stage 7: Create Pull Request."""
    engine = _get_engine(args)
    record = _get_target_contribution(args)
    if record is None:
        print("Stage 7: No pending contribution found to open PR.")
        return 0

    dest_pr = engine.stage7_create_pr(record)
    print(
        f"Stage 7 Complete: Destination PR #{dest_pr.get('number')} created at {dest_pr.get('html_url')}."
    )
    return 0


def cmd_update_state(args: argparse.Namespace) -> int:
    """Execute Stage 8: Update Sync State."""
    engine = _get_engine(args)
    record = _get_target_contribution(args)
    if record is None:
        print("Stage 8: No pending contribution found to update state.")
        engine.release_distributed_lock()
        return 0

    engine.stage8_update_state(record, release_lock=True)
    print(f"Stage 8 Complete: Contribution {record.sync_key} recorded as EXPORTED. Lock released.")
    return 0


def cmd_run_all(args: argparse.Namespace) -> int:
    """Execute full pipeline end-to-end (Stages 1-8)."""
    engine = _get_engine(args)
    result = engine.run_all()
    print(f"Pipeline Result: {result.get('status')} - {result.get('message')}")
    if result.get("status") == "CONFLICT":
        print(
            f"Halting on conflict for PR #{result.get('pr_number')}: {result.get('error')}",
            file=sys.stderr,
        )
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Construct command-line argument parser."""
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--source-repo",
        type=str,
        default=argparse.SUPPRESS,
        help="Source Git repository clone URL",
    )
    parent_parser.add_argument(
        "--target-repo",
        type=str,
        default=argparse.SUPPRESS,
        help="Target Git repository clone URL",
    )
    parent_parser.add_argument(
        "--db-url",
        type=str,
        default=argparse.SUPPRESS,
        help="Database connection URL",
    )
    parent_parser.add_argument(
        "--dry-run",
        action="store_true",
        default=argparse.SUPPRESS,
        help="Simulate actions without pushing branches, opening PRs, or updating exported state",
    )
    parent_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=argparse.SUPPRESS,
        help="Enable detailed debug logging output",
    )

    parser = argparse.ArgumentParser(
        prog="sync_engine",
        description="Occupify Contribution Synchronization Engine CLI",
        parents=[parent_parser],
    )

    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # init-db
    subparsers.add_parser("init-db", parents=[parent_parser], help="Initialize database tables")

    # status
    subparsers.add_parser(
        "status",
        parents=[parent_parser],
        help="Display current checkpoints, active locks, and recent contributions",
    )

    # Stage 1: checkout-source
    subparsers.add_parser(
        "checkout-source",
        parents=[parent_parser],
        help="Stage 1: Checkout source repository",
    )

    # Stage 2: load-checkpoint
    subparsers.add_parser(
        "load-checkpoint",
        parents=[parent_parser],
        help="Stage 2: Acquire lock, load checkpoint, and reconcile integrated PRs",
    )

    # Stage 3: find-prs
    subparsers.add_parser(
        "find-prs",
        parents=[parent_parser],
        help="Stage 3: Query GitHub API for merged PRs targeting source main",
    )

    # Stage 4: extract-contributions
    p_extract = subparsers.add_parser(
        "extract-contributions",
        parents=[parent_parser],
        help="Stage 4: Retrieve PR commits, contributors, and changed files",
    )
    p_extract.add_argument("--pr", type=int, help="Optional specific source PR number")

    # Stage 5: calculate-diff
    p_diff = subparsers.add_parser(
        "calculate-diff",
        parents=[parent_parser],
        help="Stage 5: Calculate unified diff patch for PR",
    )
    p_diff.add_argument("--pr", type=int, help="Optional specific source PR number")

    # Stage 6: sync-target
    p_sync = subparsers.add_parser(
        "sync-target",
        parents=[parent_parser],
        help="Stage 6: Create sync branch and apply patch to target repo",
    )
    p_sync.add_argument("--pr", type=int, help="Optional specific source PR number")

    # Stage 7: create-pr
    p_pr = subparsers.add_parser(
        "create-pr",
        parents=[parent_parser],
        help="Stage 7: Push sync branch and open destination PR in target repo",
    )
    p_pr.add_argument("--pr", type=int, help="Optional specific source PR number")

    # Stage 8: update-state
    p_update = subparsers.add_parser(
        "update-state",
        parents=[parent_parser],
        help="Stage 8: Persist exported state, update checkpoint, and release lock",
    )
    p_update.add_argument("--pr", type=int, help="Optional specific source PR number")

    # run-all
    subparsers.add_parser(
        "run-all",
        parents=[parent_parser],
        help="Run full synchronization pipeline (Stages 1-8)",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    _setup_logging(verbose=getattr(args, "verbose", False))

    command_handlers = {
        "init-db": cmd_init_db,
        "status": cmd_status,
        "checkout-source": cmd_checkout_source,
        "load-checkpoint": cmd_load_checkpoint,
        "find-prs": cmd_find_prs,
        "extract-contributions": cmd_extract_contributions,
        "calculate-diff": cmd_calculate_diff,
        "sync-target": cmd_sync_target,
        "create-pr": cmd_create_pr,
        "update-state": cmd_update_state,
        "run-all": cmd_run_all,
    }

    handler = command_handlers.get(args.command)
    if not handler:
        parser.print_help()
        return 1

    try:
        return handler(args)
    except Exception as exc:
        verbose = getattr(args, "verbose", False)
        logger.error("Command '%s' failed: %s", args.command, exc, exc_info=verbose)
        return 1


if __name__ == "__main__":
    sys.exit(main())
