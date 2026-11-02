import asyncio
import logging
import random
import time
from typing import Any

from sqlalchemy import and_, func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.logging import log_step, setup_logging
from app.db.models import IndexMetaModel, JobIndexRow, utc_now
from app.db.session import get_sessionmaker
from app.features.job_match.index.store import get_expected_index_source
from app.features.job_match.ports import IndexMeta, IndexRow
from app.features.job_match.sanitize import DOC_TEXT_VERSION, sanitize_project
from app.messaging.core_client import get_core_rpc
from app.ml import get_embedder

logger = logging.getLogger(__name__)


async def write_index(
    session: AsyncSession,
    rows: list[IndexRow],
    vectors: list[list[float]],
    meta: IndexMeta | None = None,
    embedder: Any = None,
) -> int:
    """Writes all rows and vectors into job_index within a single transaction.

    Enforces:
    - Non-empty index (refuse 0 jobs)
    - Re-creation of job_index table with embedding NOT NULL
    - SET LOCAL lock_timeout = '5s'
    - Writing index_meta
    - Pre-commit self-retrieval verification (dense rank 1 and lexical top 10 for sample rows)
    """
    if len(rows) == 0:
        raise ValueError("Refusing to write empty index (jobs_n == 0)")
    if len(rows) != len(vectors):
        raise ValueError("Mismatch between rows and vectors length")

    is_pg = session.bind and "postgresql" in str(session.bind.dialect.name)
    if is_pg:
        await session.execute(text("SET LOCAL lock_timeout = '5s'"))

    # Drop and recreate job_index
    def _recreate(sync_session):
        conn = sync_session.connection()
        JobIndexRow.__table__.drop(conn, checkfirst=True)
        JobIndexRow.__table__.create(conn)

    await session.run_sync(_recreate)

    # Insert rows
    for row, vec in zip(rows, vectors, strict=True):
        db_row = JobIndexRow(
            job_id=row.job_id,
            project_id=row.project_id,
            project_title=row.project_title,
            project_description=row.project_description,
            job_title=row.job_title,
            job_description=row.job_description,
            skills=row.skills,
            requirements=row.requirements,
            salary_type=row.salary_type or "MONTHLY",
            budget_min=row.budget_min,
            budget_max=row.budget_max,
            experience_level=row.experience_level or "ENTRY",
            period=row.period or "MONTHLY",
            hours_per_day=row.hours_per_day,
            project_status=row.project_status,
            job_status=row.job_status,
            doc_text=row.doc_text,
            embedding=vec,
        )
        if is_pg:
            db_row.search_tsv = func.to_tsvector("simple", func.unaccent(row.doc_text))
        session.add(db_row)

    # Write index_meta
    settings = get_settings()
    meta_source = meta.source if meta else get_expected_index_source()
    meta_model = meta.embed_model if meta else settings.EMBEDDER_MODEL
    meta_dim = meta.dim if meta else (len(vectors[0]) if vectors else settings.EMBEDDING_DIM)
    meta_doc_version = meta.doc_text_version if meta else DOC_TEXT_VERSION

    meta_res = await session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
    meta_row = meta_res.scalar_one_or_none()
    if meta_row is None:
        meta_row = IndexMetaModel(
            id=1,
            embed_model=meta_model,
            dim=meta_dim,
            source=meta_source,
            doc_text_version=meta_doc_version,
            built_at=utc_now(),
            jobs_n=len(rows),
        )
        session.add(meta_row)
    else:
        meta_row.embed_model = meta_model
        meta_row.dim = meta_dim
        meta_row.source = meta_source
        meta_row.doc_text_version = meta_doc_version
        meta_row.built_at = utc_now()
        meta_row.jobs_n = len(rows)

    await session.flush()

    # Pre-commit self-retrieval verification
    sample_size = min(30, len(rows))
    sample_indices = random.sample(range(len(rows)), sample_size)
    for idx in sample_indices:
        target_row = rows[idx]
        target_vec = vectors[idx]

        # 1. Dense self-retrieval check (rank 1 must be target_row.job_id)
        if embedder is not None:
            q_vec = embedder.embed([target_row.doc_text])[0]
        else:
            q_vec = target_vec

        if is_pg:
            dense_stmt = (
                select(
                    JobIndexRow.job_id, JobIndexRow.embedding.cosine_distance(q_vec).label("dist")
                )
                .order_by("dist")
                .limit(10)
            )
            dense_res = await session.execute(dense_stmt)
            top_rows = dense_res.all()
            if not top_rows:
                raise RuntimeError("Self-retrieval check failed: no rows returned")
            best_dist = top_rows[0][1]
            tied_jids = [r[0] for r in top_rows if abs((r[1] or 0.0) - (best_dist or 0.0)) < 1e-5]
            if target_row.job_id not in tied_jids:
                raise RuntimeError(
                    f"Self-retrieval check failed: expected {target_row.job_id} at rank 1, got {top_rows[0][0]}"
                )

        # 2. Lexical self-retrieval check (target_row must match and rank in top 10 or tie)
        if target_row.job_title and target_row.job_title.strip() and is_pg:
            ts_q = func.phraseto_tsquery("simple", func.unaccent(target_row.job_title))
            target_score_stmt = select(func.ts_rank_cd(JobIndexRow.search_tsv, ts_q)).where(
                and_(
                    JobIndexRow.job_id == target_row.job_id,
                    JobIndexRow.search_tsv.op("@@")(ts_q),
                )
            )
            target_score = (await session.execute(target_score_stmt)).scalar() or 0.0
            if target_score == 0.0:
                ts_q = func.plainto_tsquery("simple", func.unaccent(target_row.job_title))
                target_score_stmt = select(func.ts_rank_cd(JobIndexRow.search_tsv, ts_q)).where(
                    and_(
                        JobIndexRow.job_id == target_row.job_id,
                        JobIndexRow.search_tsv.op("@@")(ts_q),
                    )
                )
                target_score = (await session.execute(target_score_stmt)).scalar() or 0.0

            if target_score == 0.0:
                raise RuntimeError(
                    f"Self-retrieval check failed: lexical query on job title did not match {target_row.job_id}"
                )

            top_stmt = (
                select(func.ts_rank_cd(JobIndexRow.search_tsv, ts_q).label("score"))
                .where(JobIndexRow.search_tsv.op("@@")(ts_q))
                .order_by(text("score DESC"))
                .limit(10)
            )
            top_scores = [r[0] for r in (await session.execute(top_stmt)).all()]
            min_top10 = min(top_scores) if len(top_scores) >= 10 else 0.0
            if target_score < min_top10 - 1e-4:
                raise RuntimeError(
                    f"Self-retrieval check failed: lexical score {target_score} not in top 10 (min={min_top10}) for {target_row.job_id}"
                )

    return len(rows)


async def build(
    core_rpc: Any = None,
    embedder: Any = None,
    session: AsyncSession | None = None,
) -> int:
    """Reads projects from core, filters, embeds, and writes the index."""
    if core_rpc is None:
        core_rpc = get_core_rpc()
    if embedder is None:
        embedder = get_embedder()

    page = 0
    all_rows: list[IndexRow] = []
    while True:
        reply = await core_rpc.call("core.project.search", {"page": page, "size": 50})
        if not reply or not reply.get("ok"):
            if page == 0:
                raise RuntimeError("Failed to read from core_rpc: search returned non-ok")
            break
        projects = reply.get("data", {}).get("data", [])
        if not projects:
            break
        for p in projects:
            proj_status = p.get("status", "OPEN")
            if proj_status != "OPEN":
                continue
            sanitized_rows = sanitize_project(p)
            for r in sanitized_rows:
                if r.project_status == "OPEN" and r.job_status == "RECRUITING":
                    all_rows.append(r)
        paging = reply.get("data", {}).get("paging", {})
        total_pages = paging.get("totalPages", 1)
        if page >= total_pages - 1:
            break
        page += 1

    if not all_rows:
        raise RuntimeError("Refusing to write index: 0 recruiting jobs found in OPEN projects")

    # Embed doc texts in batches of 32
    texts = [r.doc_text for r in all_rows]
    vectors: list[list[float]] = []
    batch_size = 32
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i : i + batch_size]
        batch_vectors = embedder.embed(batch_texts)
        vectors.extend(batch_vectors)

    # Write index inside transaction
    if session is not None:
        jobs_n = await write_index(session, all_rows, vectors, embedder=embedder)
        await session.commit()
    else:
        session_maker = get_sessionmaker()
        async with session_maker() as sess:
            jobs_n = await write_index(sess, all_rows, vectors, embedder=embedder)
            await sess.commit()

    log_step("index.built", jobs_n=jobs_n)
    return jobs_n


async def main() -> None:
    setup_logging()
    t0 = time.perf_counter()
    logger.info("Starting job index migration...")
    jobs_n = await build()
    elapsed_ms = int((time.perf_counter() - t0) * 1000)
    logger.info("Migration complete: %d jobs migrated in %d ms", jobs_n, elapsed_ms)
    print(f"Index migration successful: {jobs_n} jobs in {elapsed_ms} ms")


if __name__ == "__main__":
    asyncio.run(main())
