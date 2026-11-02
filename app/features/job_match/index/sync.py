import asyncio
import logging
import time
from typing import Any

from sqlalchemy import func, select

from app.core.config import get_settings
from app.core.logging import log_step
from app.db.models import IndexMetaModel, JobIndexRow, utc_now
from app.db.session import get_sessionmaker
from app.features.job_match.index.store import (
    delete_job_by_id,
    delete_jobs_by_project,
    get_expected_index_source,
    upsert_jobs,
)
from app.features.job_match.ports import IndexRow
from app.features.job_match.sanitize import DOC_TEXT_VERSION, sanitize_project
from app.messaging.core_client import get_core_rpc
from app.ml import get_embedder

logger = logging.getLogger(__name__)


async def sync_single_project(
    project: dict[str, Any],
    embedder: Any = None,
) -> int:
    """
    Sanitizes, embeds, and atomically upserts/deletes a single project and its jobs in job_index.
    Called when a project.created or project.updated event arrives over RabbitMQ.
    """
    proj_id = str(project.get("id") or project.get("projectId") or "")
    if not proj_id:
        return 0

    proj_status = str(project.get("status") or "OPEN").upper()

    session_maker = get_sessionmaker()
    async with session_maker() as session:
        if proj_status != "OPEN":
            # Project is closed/archived; remove all associated jobs from active search index
            deleted = await delete_jobs_by_project(session, proj_id)
            log_step("job_sync.project_deactivated", project_id=proj_id, deleted=deleted)
            return 0

        # Sanitize project and jobs
        rows = sanitize_project(project)
        recruiting_rows = [r for r in rows if r.job_status == "RECRUITING"]
        closed_job_ids = [r.job_id for r in rows if r.job_status != "RECRUITING"]

        # Remove any jobs that are filled or closed
        for cjid in closed_job_ids:
            await delete_job_by_id(session, cjid)

        if not recruiting_rows:
            await delete_jobs_by_project(session, proj_id)
            return 0

        if embedder is None:
            embedder = get_embedder()

        texts = [r.doc_text for r in recruiting_rows]
        vectors = embedder.embed(texts)

        upserted = await upsert_jobs(session, recruiting_rows, vectors)
        log_step("job_sync.project_upserted", project_id=proj_id, jobs_n=upserted)
        return upserted


async def sync_all_jobs_in_background(
    batch_size: int = 32,
    core_rpc: Any = None,
    embedder: Any = None,
) -> int:
    """
    Background worker that queries core_rpc (paged), sanitizes projects,
    generates embeddings in batches of `batch_size`, and atomically upserts
    into PostgreSQL job_index without wiping the table or blocking API requests.
    """
    t0 = time.perf_counter()
    logger.info("Starting background batch sync of job index...")

    if core_rpc is None:
        core_rpc = get_core_rpc()
    if embedder is None:
        embedder = get_embedder()

    page = 0
    all_recruiting_rows: list[IndexRow] = []

    while True:
        try:
            reply = await core_rpc.call("core.project.search", {"page": page, "size": 50})
        except Exception as exc:
            logger.warning("Background sync RPC call failed on page %d: %s", page, exc)
            break

        if not reply or not reply.get("ok"):
            break

        projects = reply.get("data", {}).get("data", [])
        if not projects:
            break

        for p in projects:
            proj_status = str(p.get("status") or "OPEN").upper()
            if proj_status != "OPEN":
                continue
            sanitized_rows = sanitize_project(p)
            for r in sanitized_rows:
                if r.project_status == "OPEN" and r.job_status == "RECRUITING":
                    all_recruiting_rows.append(r)

        paging = reply.get("data", {}).get("paging", {})
        total_pages = paging.get("totalPages", 1)
        if page >= total_pages - 1:
            break
        page += 1

    if not all_recruiting_rows:
        logger.info("Background sync found 0 recruiting jobs to sync.")
        return 0

    session_maker = get_sessionmaker()

    # Batch embedding and upsert
    total_synced = 0
    for i in range(0, len(all_recruiting_rows), batch_size):
        batch = all_recruiting_rows[i : i + batch_size]
        texts = [r.doc_text for r in batch]
        vectors = embedder.embed(texts)

        async with session_maker() as session:
            await upsert_jobs(session, batch, vectors)
            total_synced += len(batch)

        await asyncio.sleep(0.01)

    # Update index_meta
    settings = get_settings()
    async with session_maker() as session:
        meta_res = await session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
        meta_row = meta_res.scalar_one_or_none()
        cnt_res = await session.execute(select(func.count(JobIndexRow.job_id)))
        current_jobs_count = cnt_res.scalar() or total_synced

        if meta_row is None:
            meta_row = IndexMetaModel(
                id=1,
                embed_model=settings.EMBEDDER_MODEL,
                dim=settings.EMBEDDING_DIM,
                source=get_expected_index_source(),
                doc_text_version=DOC_TEXT_VERSION,
                built_at=utc_now(),
                jobs_n=current_jobs_count,
            )
            session.add(meta_row)
        else:
            meta_row.embed_model = settings.EMBEDDER_MODEL
            meta_row.dim = settings.EMBEDDING_DIM
            meta_row.source = get_expected_index_source()
            meta_row.doc_text_version = DOC_TEXT_VERSION
            meta_row.built_at = utc_now()
            meta_row.jobs_n = current_jobs_count
        await session.commit()

    elapsed_ms = int((time.perf_counter() - t0) * 1000)
    logger.info("Background sync complete: %d jobs synced in %d ms", total_synced, elapsed_ms)
    log_step("index.sync_complete", jobs_n=total_synced, ms=elapsed_ms)
    return total_synced
