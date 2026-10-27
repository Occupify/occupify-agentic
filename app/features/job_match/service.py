import asyncio
import hashlib
import logging
import os
import uuid
from decimal import Decimal

import anyio
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.errors import AppError
from app.core.logging import bind_context, log_step
from app.core.security import CurrentUser
from app.db.models import JobMatchResult, JobMatchRun, utc_now
from app.db.session import get_sessionmaker
from app.features.job_match import pipeline
from app.features.job_match.index.store import PgJobIndex
from app.features.job_match.ports import PipelineOptions, RunResult, RunState
from app.features.job_match.schemas import (
    ErrorCode,
    JobMatchWarning,
    MatchCriteria,
    RunOutcome,
    RunStatus,
    WarningCode,
)
from app.messaging.core_client import get_core_rpc
from app.ml import get_embedder

logger = logging.getLogger(__name__)

# Strong reference set for ongoing background tasks (INV-3)
_active_tasks: set[asyncio.Task] = set()


def _get_timeout_seconds() -> float:
    env_val = os.getenv("JOB_MATCH_RUN_TIMEOUT_S")
    if env_val:
        try:
            return float(env_val)
        except ValueError:
            pass
    return float(get_settings().JOB_MATCH_RUN_TIMEOUT_S)


async def execute_run(
    run_id: str,
    user: CurrentUser,
    pdf_bytes: bytes,
    criteria: MatchCriteria,
) -> None:
    """Executes the CV-Job matching pipeline with timeout, error handling, and DB persistence."""
    session_maker = get_sessionmaker()
    bind_context(run_id=run_id, user_id=user.user_id, use_case="job_match", redact_errors=True)
    state = RunState(run_id=run_id)

    # 1. Update status to running
    async with session_maker() as session:
        run = await session.get(JobMatchRun, run_id)
        if run:
            run.status = RunStatus.RUNNING.value
            run.stage = "s0_extract_text"
            await session.commit()

    timeout_s = _get_timeout_seconds()
    res: RunResult | None = None
    is_timeout = False

    try:
        async with session_maker() as search_session:
            try:
                embedder = get_embedder()
            except Exception:
                embedder = None
            store = PgJobIndex(session=search_session, embedder=embedder)
            core_rpc = get_core_rpc()

            async with asyncio.timeout(timeout_s):
                res = await pipeline.run(
                    state=state,
                    pdf_bytes=pdf_bytes,
                    user=user,
                    criteria=criteria,
                    lang=criteria.lang,
                    store=store,
                    core_rpc=core_rpc,
                    options=PipelineOptions(),
                )
    except TimeoutError:
        is_timeout = True
        logger.warning("Job match run %s timed out after %.2fs", run_id, timeout_s)
    except BaseException as exc:
        log_step(
            "job_match.error",
            run_id=run_id,
            error_type=type(exc).__name__,
        )
        logger.exception("Unexpected error in execute_run for %s: %s", run_id, type(exc).__name__)
        with anyio.CancelScope(shield=True):
            async with session_maker() as session:
                run = await session.get(JobMatchRun, run_id)
                if run:
                    run.status = RunStatus.FAILED.value
                    run.stage = "done"
                    run.error_code = ErrorCode.INTERNAL_ERROR.value
                    run.message = "Failed to process job match run."
                    run.finished_at = utc_now()
                    await session.commit()
        return

    # 2. Handle timeout outcome
    if is_timeout:
        if state.ranking:
            # Partial results available
            warn = JobMatchWarning(
                code=WarningCode.SEARCH_STOPPED_EARLY.value,
                message="Run deadline passed; partial ranking persisted.",
            )
            res = RunResult(
                status=RunStatus.PARTIAL,
                outcome=RunOutcome.OK,
                warnings=[warn],
                items=state.ranking,
                stop_reason="RUN_TIMEOUT",
            )
        else:
            with anyio.CancelScope(shield=True):
                async with session_maker() as session:
                    run = await session.get(JobMatchRun, run_id)
                    if run:
                        run.status = RunStatus.FAILED.value
                        run.stage = "done"
                        run.error_code = ErrorCode.RUN_TIMEOUT.value
                        run.message = "Failed to complete within timeout deadline."
                        run.finished_at = utc_now()
                        await session.commit()
            return

    # 3. Persist success or partial result
    if res is not None:
        with anyio.CancelScope(shield=True):
            async with session_maker() as session:
                run = await session.get(JobMatchRun, run_id)
                if run:
                    run.status = (
                        res.status.value if hasattr(res.status, "value") else str(res.status)
                    )
                    run.stage = "done"
                    run.outcome = (
                        res.outcome.value
                        if hasattr(res.outcome, "value")
                        else (str(res.outcome) if res.outcome else None)
                    )
                    run.stop_reason = res.stop_reason
                    run.error_code = (
                        res.error_code.value
                        if hasattr(res.error_code, "value")
                        else (str(res.error_code) if res.error_code else None)
                    )
                    run.message = res.message
                    run.warnings = [
                        w.model_dump() if hasattr(w, "model_dump") else w for w in res.warnings
                    ]
                    run.profile = res.profile
                    run.top_missing_skills = res.top_missing_skills
                    run.cv_sha256 = hashlib.sha256(pdf_bytes).hexdigest()
                    run.skill_versions = res.skill_versions
                    run.scoring_version = res.scoring_version
                    run.tokens_in = res.tokens_in
                    run.tokens_out = res.tokens_out
                    run.cost_usd = Decimal(str(res.cost_usd))
                    run.stages = [
                        s.model_dump() if hasattr(s, "model_dump") else s for s in state.stages
                    ]
                    run.finished_at = utc_now()

                    # Save items
                    if res.items:
                        for item in res.items:
                            # Handle both dataclass/Pydantic item and dict
                            rank = getattr(item, "rank", None) or (
                                item.get("rank") if isinstance(item, dict) else 1
                            )
                            proj_id = getattr(item, "project_id", None) or (
                                item.get("projectId") or item.get("project_id")
                                if isinstance(item, dict)
                                else ""
                            )
                            match_score = getattr(item, "match_score", None) or (
                                item.get("matchScore") or item.get("match_score")
                                if isinstance(item, dict)
                                else 0.0
                            )
                            verified = (
                                getattr(item, "verified", True)
                                if not isinstance(item, dict)
                                else item.get("verified", True)
                            )
                            jobs = (
                                getattr(item, "jobs", [])
                                if not isinstance(item, dict)
                                else item.get("jobs", [])
                            )
                            dumped_jobs = [
                                j.model_dump(by_alias=True) if hasattr(j, "model_dump") else j
                                for j in jobs
                            ]

                            result_row = JobMatchResult(
                                run_id=run_id,
                                rank=rank,
                                project_id=proj_id,
                                match_score=float(match_score),
                                verified=verified,
                                jobs=dumped_jobs,
                            )
                            session.add(result_row)

                    await session.commit()


async def start_job_match(
    user: CurrentUser,
    pdf_bytes: bytes,
    criteria: MatchCriteria,
    db: AsyncSession,
) -> JobMatchRun:
    """Validates user busy state, commits queued run, and spawns background task."""
    # Check if user already has an active run
    stmt = select(JobMatchRun).where(
        JobMatchRun.user_id == user.user_id,
        JobMatchRun.status.in_([RunStatus.QUEUED.value, RunStatus.RUNNING.value]),
    )
    existing = (await db.execute(stmt)).scalars().first()
    if existing:
        raise AppError(
            status_code=409,
            message="Failed to start job match: another job match run is already in progress.",
            error_code="JOB_MATCH_BUSY",
        )

    run_id = str(uuid.uuid4())
    run = JobMatchRun(
        id=run_id,
        user_id=user.user_id,
        status=RunStatus.QUEUED.value,
        stage="init",
        criteria=criteria.model_dump(by_alias=True) if criteria else None,
    )
    db.add(run)
    try:
        await db.commit()
        await db.refresh(run)
    except IntegrityError as exc:
        await db.rollback()
        raise AppError(
            status_code=409,
            message="Failed to start job match: another job match run is already in progress.",
            error_code="JOB_MATCH_BUSY",
        ) from exc

    log_step("job_match.accepted", run_id=run_id, user_id=user.user_id)

    task = asyncio.create_task(
        execute_run(
            run_id=run_id,
            user=user,
            pdf_bytes=pdf_bytes,
            criteria=criteria,
        )
    )
    _active_tasks.add(task)
    task.add_done_callback(_active_tasks.discard)

    return run
