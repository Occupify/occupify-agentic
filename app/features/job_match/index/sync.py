import asyncio
import logging
from typing import Any

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.config import get_settings
from app.core.logging import log_step
from app.db.models import IndexMetaModel, JobIndexRow, utc_now
from app.features.job_match.index.store import (
    PgJobIndex,
    set_index_building,
    set_index_jobs_count,
)
from app.features.job_match.sanitize import sanitize_project
from app.ml import get_embedder

logger = logging.getLogger(__name__)

SWEEP_ADVISORY_LOCK_ID = 84729103


async def sweep_job_index(session: AsyncSession, seen_job_ids: list[str]) -> None:
    """Sweeps job index against newly seen job IDs from core.

    Increments missed_sweeps for jobs not present in seen_job_ids.
    Deactivates jobs (active = False) when missed_sweeps >= 2.
    Resets missed_sweeps to 0 for seen jobs.
    """
    seen_set = set(seen_job_ids)
    stmt = select(JobIndexRow).where(JobIndexRow.active.is_(True))
    result = await session.execute(stmt)
    rows = result.scalars().all()

    for row in rows:
        if row.job_id not in seen_set:
            row.missed_sweeps += 1
            if row.missed_sweeps >= 2:
                row.active = False
                logger.info(
                    "Deactivated job %s after %d missed sweeps", row.job_id, row.missed_sweeps
                )
        else:
            row.missed_sweeps = 0

    await session.commit()


async def build_job_index(
    session: AsyncSession,
    core_rpc: Any,
    embedder: Any = None,
) -> int:
    """Builds or rebuilds the job index by paging core.project.search,

    upserting rows, embedding backlog, updating metadata, and logging index.built.
    """
    settings = get_settings()
    set_index_building(True)
    try:
        store = PgJobIndex(session=session, embedder=embedder)

        # 1. Check existing meta for model mismatch
        meta = await store.meta()
        if (
            meta
            and meta.embed_model
            and (meta.embed_model != settings.EMBEDDING_MODEL or meta.dim != settings.EMBEDDING_DIM)
        ):
            log_step(
                "index.model_mismatch",
                old_model=meta.embed_model,
                new_model=settings.EMBEDDING_MODEL,
            )
            await store.handle_model_mismatch(
                new_model=settings.EMBEDDING_MODEL, new_dim=settings.EMBEDDING_DIM
            )

        # 2. Page all projects from core.project.search
        all_rows = []
        page = 0
        while True:
            reply = await core_rpc.call("core.project.search", {"page": page, "size": 50})
            if not reply or not reply.get("ok"):
                break
            projects = reply.get("data", {}).get("data", [])
            if not projects:
                break
            for p in projects:
                all_rows.extend(sanitize_project(p))
            paging = reply.get("data", {}).get("paging", {})
            total_pages = paging.get("totalPages", 1)
            if page >= total_pages - 1:
                break
            page += 1

        # 3. Upsert into database
        if all_rows:
            await store.upsert(all_rows)

        # 4. Embed backlog if embedder is available
        if store.embedder is not None:
            while True:
                embedded_n = await store.embed_backlog_batch(batch_size=64)
                if embedded_n == 0:
                    break

        # 5. Compute active jobs and update IndexMetaModel
        from sqlalchemy import and_, func

        jobs_res = await session.execute(
            select(func.count(JobIndexRow.job_id)).where(JobIndexRow.active.is_(True))
        )
        jobs_n = jobs_res.scalar() or len(all_rows)

        pending_res = await session.execute(
            select(func.count(JobIndexRow.job_id)).where(
                and_(JobIndexRow.active.is_(True), JobIndexRow.embedding.is_(None))
            )
        )
        embeddings_pending = pending_res.scalar() or 0
        set_index_jobs_count(jobs_n)

        meta_res = await session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
        meta_row = meta_res.scalar_one_or_none()
        if meta_row is None:
            meta_row = IndexMetaModel(
                id=1,
                embed_model=settings.EMBEDDING_MODEL,
                dim=settings.EMBEDDING_DIM,
                source="core_rpc",
                built_at=utc_now(),
                jobs_n=jobs_n,
            )
            session.add(meta_row)
        else:
            meta_row.embed_model = settings.EMBEDDING_MODEL
            meta_row.dim = settings.EMBEDDING_DIM
            meta_row.built_at = utc_now()
            meta_row.jobs_n = jobs_n

        await session.commit()
        log_step("index.built", jobs_n=jobs_n, embeddings_pending=embeddings_pending)
        return jobs_n
    finally:
        set_index_building(False)


async def start_embed_backlog_task(
    session_maker: async_sessionmaker[AsyncSession],
    interval_s: int = 10,
) -> None:
    """Background worker draining un-embedded rows."""
    while True:
        try:
            await asyncio.sleep(interval_s)
            async with session_maker() as session:
                try:
                    embedder = get_embedder()
                except Exception:
                    embedder = None
                if embedder:
                    store = PgJobIndex(session=session, embedder=embedder)
                    while True:
                        c = await store.embed_backlog_batch(batch_size=32)
                        if c == 0:
                            break
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.warning("Error during embed backlog worker: %s", e)


async def start_sweep_task(
    session_maker: async_sessionmaker[AsyncSession],
    core_rpc: Any,
    sweep_interval_s: int = 600,
) -> None:
    """Runs a periodic background sweep every sweep_interval_s seconds."""
    logger.info("Starting job index sweep task (interval %ds)", sweep_interval_s)

    while True:
        try:
            await asyncio.sleep(sweep_interval_s)
            async with session_maker() as session:
                is_pg = session.bind and "postgresql" in str(session.bind.dialect.name)
                got_lock = False
                if is_pg:
                    lock_res = await session.execute(
                        text(f"SELECT pg_try_advisory_lock({SWEEP_ADVISORY_LOCK_ID});")
                    )
                    got_lock = bool(lock_res.scalar())
                    if not got_lock:
                        continue

                try:
                    all_rows = []
                    seen_job_ids = []
                    page = 0
                    while True:
                        reply = await core_rpc.call(
                            "core.project.search", {"page": page, "size": 50}
                        )
                        if not reply or not reply.get("ok"):
                            break
                        projects = reply.get("data", {}).get("data", [])
                        if not projects:
                            break
                        for p in projects:
                            s_rows = sanitize_project(p)
                            all_rows.extend(s_rows)
                            for sr in s_rows:
                                seen_job_ids.append(sr.job_id)
                        paging = reply.get("data", {}).get("paging", {})
                        total_pages = paging.get("totalPages", 1)
                        if page >= total_pages - 1:
                            break
                        page += 1

                    try:
                        embedder = get_embedder()
                    except Exception:
                        embedder = None

                    store = PgJobIndex(session=session, embedder=embedder)
                    if all_rows:
                        await store.upsert(all_rows)

                    await sweep_job_index(session, seen_job_ids)

                    if store.embedder is not None:
                        while True:
                            c = await store.embed_backlog_batch(batch_size=16)
                            if c == 0:
                                break

                    meta = await store.meta()
                    log_step("index.refreshed", jobs_n=meta.jobs_n)
                finally:
                    if is_pg and got_lock:
                        await session.execute(
                            text(f"SELECT pg_advisory_unlock({SWEEP_ADVISORY_LOCK_ID});")
                        )
        except asyncio.CancelledError:
            logger.info("Job index sweep task cancelled")
            break
        except Exception as e:
            logger.warning("Error during job index sweep: %s", e)
