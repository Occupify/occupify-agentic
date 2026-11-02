import hashlib
import logging
from pathlib import Path
from typing import Any, Literal

from sqlalchemy import and_, delete, func, or_, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.db.models import IndexMetaModel, JobIndexRow
from app.db.session import get_sessionmaker
from app.features.job_match.ports import IndexHit, IndexMeta, IndexRow, MatchCriteria
from app.features.job_match.sanitize import DOC_TEXT_VERSION
from app.features.job_match.schemas import HoursPerDayFilter

logger = logging.getLogger(__name__)


def get_expected_index_source() -> str:
    """Computes expected source identifier based on CORE_RPC_MODE and mock file sha256."""
    settings = get_settings()
    if settings.CORE_RPC_MODE == "mock":
        p = Path(settings.CORE_MOCK_PATH)
        if p.exists():
            return "mock:" + hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        return "mock:unknown"
    return "rpc"


async def check_index_state_with_session(
    session: AsyncSession,
) -> Literal["ok", "missing", "mismatch"]:
    """Inspects index_meta in session and evaluates status against current settings."""
    settings = get_settings()
    try:
        res = await session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
        meta = res.scalar_one_or_none()
        if meta is None or meta.jobs_n == 0:
            return "missing"

        expected_source = get_expected_index_source()
        if (
            meta.embed_model != settings.EMBEDDER_MODEL
            or meta.dim != settings.EMBEDDING_DIM
            or getattr(meta, "doc_text_version", "") != DOC_TEXT_VERSION
            or meta.source != expected_source
        ):
            return "mismatch"

        return "ok"
    except Exception as exc:
        logger.warning("Error checking index state: %s", exc)
        return "missing"


async def index_state(session: AsyncSession | None = None) -> Literal["ok", "missing", "mismatch"]:
    """Asynchronously checks whether the job index is ok, missing, or mismatched."""
    if session is not None:
        return await check_index_state_with_session(session)

    session_maker = get_sessionmaker()
    async with session_maker() as sess:
        return await check_index_state_with_session(sess)


class PgJobIndex:
    """PostgreSQL-backed hybrid job search index using pgvector (HNSW) and full-text search (GIN)."""

    def __init__(
        self,
        session: AsyncSession,
        embedder: Any = None,
        is_empty: bool | None = None,
    ):
        self.session = session
        self.embedder = embedder
        self._is_empty = is_empty

    async def index_state(self) -> Literal["ok", "missing", "mismatch"]:
        return await check_index_state_with_session(self.session)

    def _build_filter_clauses(self, criteria: MatchCriteria) -> list[Any]:
        """Constructs SQLAlchemy WHERE clauses for MatchCriteria."""
        clauses = [
            JobIndexRow.project_status == "OPEN",
            JobIndexRow.job_status == "RECRUITING",
        ]

        if criteria.salary_type is not None:
            clauses.append(JobIndexRow.salary_type == criteria.salary_type.value)

        if criteria.experience_level is not None:
            clauses.append(JobIndexRow.experience_level == criteria.experience_level.value)

        if criteria.min_budget is not None:
            clauses.append(
                or_(
                    JobIndexRow.budget_max >= criteria.min_budget,
                    JobIndexRow.budget_min >= criteria.min_budget,
                )
            )

        if criteria.max_budget is not None:
            clauses.append(
                or_(
                    JobIndexRow.budget_min <= criteria.max_budget,
                    JobIndexRow.budget_max <= criteria.max_budget,
                )
            )

        if criteria.hours_per_day is not None:
            if criteria.hours_per_day == HoursPerDayFilter.UNDER_FOUR:
                clauses.append(
                    or_(
                        JobIndexRow.hours_per_day.is_(None),
                        JobIndexRow.hours_per_day < 4.0,
                    )
                )
            elif criteria.hours_per_day == HoursPerDayFilter.FOUR_TO_EIGHT:
                clauses.append(
                    or_(
                        JobIndexRow.hours_per_day.is_(None),
                        and_(JobIndexRow.hours_per_day >= 4.0, JobIndexRow.hours_per_day <= 8.0),
                    )
                )
            elif criteria.hours_per_day == HoursPerDayFilter.ABOVE_EIGHT:
                clauses.append(
                    or_(
                        JobIndexRow.hours_per_day.is_(None),
                        JobIndexRow.hours_per_day > 8.0,
                    )
                )

        return clauses

    async def hybrid_search(
        self,
        dense_queries: list[list[float]],
        lexical: str,
        criteria: MatchCriteria,
        top: int = 50,
    ) -> tuple[list[list[IndexHit]], list[IndexHit]]:
        """Executes dense vector searches and lexical fulltext search against the index."""
        try:
            await self.session.execute(text("SET LOCAL hnsw.ef_search = 200;"))
            await self.session.execute(text("SET LOCAL hnsw.iterative_scan = 'relaxed_order';"))
        except Exception:
            pass

        base_filters = self._build_filter_clauses(criteria)

        # 1. Dense vector searches
        dense_results: list[list[IndexHit]] = []
        for q_vec in dense_queries:
            distance_expr = JobIndexRow.embedding.cosine_distance(q_vec)
            stmt = (
                select(JobIndexRow.job_id, JobIndexRow.project_id, distance_expr.label("distance"))
                .where(and_(*base_filters, JobIndexRow.embedding.isnot(None)))
                .order_by("distance")
                .limit(top)
            )
            res = await self.session.execute(stmt)
            hits = []
            for rank, (jid, pid, dist) in enumerate(res.all(), 1):
                score = max(0.0, 1.0 - float(dist)) if dist is not None else 0.0
                hits.append(IndexHit(job_id=jid, project_id=pid, rank=rank, score=score))
            dense_results.append(hits)

        # 2. Lexical search
        lexical_hits: list[IndexHit] = []
        if lexical and lexical.strip():
            is_pg = self.session.bind and "postgresql" in str(self.session.bind.dialect.name)
            if is_pg:
                ts_query = func.websearch_to_tsquery("simple", func.unaccent(lexical))
                rank_expr = func.ts_rank_cd(JobIndexRow.search_tsv, ts_query)
                stmt = (
                    select(JobIndexRow.job_id, JobIndexRow.project_id, rank_expr.label("score"))
                    .where(and_(*base_filters, JobIndexRow.search_tsv.op("@@")(ts_query)))
                    .order_by(text("score DESC"))
                    .limit(top)
                )
            else:
                score_expr = func.length(JobIndexRow.doc_text).label("score")
                stmt = (
                    select(JobIndexRow.job_id, JobIndexRow.project_id, score_expr)
                    .where(and_(*base_filters, JobIndexRow.doc_text.ilike(f"%{lexical}%")))
                    .limit(top)
                )

            res = await self.session.execute(stmt)
            for rank, (jid, pid, score) in enumerate(res.all(), 1):
                lexical_hits.append(
                    IndexHit(
                        job_id=jid,
                        project_id=pid,
                        rank=rank,
                        score=float(score) if score is not None else 0.0,
                    )
                )

        return dense_results, lexical_hits

    async def get_rows(self, job_ids: list[str]) -> list[IndexRow]:
        """Retrieves IndexRow models by job_ids."""
        if not job_ids:
            return []
        stmt = select(JobIndexRow).where(JobIndexRow.job_id.in_(job_ids))
        res = await self.session.execute(stmt)
        db_rows = res.scalars().all()

        results: list[IndexRow] = []
        for r in db_rows:
            results.append(
                IndexRow(
                    job_id=r.job_id,
                    project_id=r.project_id,
                    project_title=r.project_title,
                    project_description=r.project_description,
                    job_title=r.job_title,
                    job_description=r.job_description,
                    skills=r.skills,
                    requirements=r.requirements,
                    salary_type=r.salary_type,
                    budget_min=r.budget_min,
                    budget_max=r.budget_max,
                    experience_level=r.experience_level,
                    period=r.period,
                    hours_per_day=r.hours_per_day,
                    project_status=r.project_status,
                    job_status=r.job_status,
                    doc_text=r.doc_text,
                )
            )
        return results

    async def meta(self) -> IndexMeta | None:
        """Returns current index metadata."""
        res = await self.session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
        meta_row = res.scalar_one_or_none()
        count_res = await self.session.execute(select(func.count(JobIndexRow.job_id)))
        jobs_n = count_res.scalar() or 0

        if meta_row is None:
            return None

        return IndexMeta(
            embed_model=meta_row.embed_model,
            dim=meta_row.dim,
            source=meta_row.source,
            doc_text_version=meta_row.doc_text_version,
            built_at=meta_row.built_at,
            jobs_n=jobs_n,
        )


async def upsert_jobs(
    session: AsyncSession,
    rows: list[IndexRow],
    vectors: list[list[float]],
) -> int:
    """Atomically upserts IndexRows and their vector embeddings into job_index."""
    if not rows:
        return 0
    if len(rows) != len(vectors):
        raise ValueError("Mismatch between rows and vectors length")

    is_pg = session.bind and "postgresql" in str(session.bind.dialect.name)

    if is_pg:
        from sqlalchemy.dialects.postgresql import insert as pg_insert

        for row, vec in zip(rows, vectors, strict=True):
            insert_stmt = pg_insert(JobIndexRow).values(
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
                search_tsv=func.to_tsvector("simple", func.unaccent(row.doc_text)),
            )
            upsert_stmt = insert_stmt.on_conflict_do_update(
                index_elements=[JobIndexRow.job_id],
                set_={
                    "project_id": insert_stmt.excluded.project_id,
                    "project_title": insert_stmt.excluded.project_title,
                    "project_description": insert_stmt.excluded.project_description,
                    "job_title": insert_stmt.excluded.job_title,
                    "job_description": insert_stmt.excluded.job_description,
                    "skills": insert_stmt.excluded.skills,
                    "requirements": insert_stmt.excluded.requirements,
                    "salary_type": insert_stmt.excluded.salary_type,
                    "budget_min": insert_stmt.excluded.budget_min,
                    "budget_max": insert_stmt.excluded.budget_max,
                    "experience_level": insert_stmt.excluded.experience_level,
                    "period": insert_stmt.excluded.period,
                    "hours_per_day": insert_stmt.excluded.hours_per_day,
                    "project_status": insert_stmt.excluded.project_status,
                    "job_status": insert_stmt.excluded.job_status,
                    "doc_text": insert_stmt.excluded.doc_text,
                    "embedding": insert_stmt.excluded.embedding,
                    "search_tsv": func.to_tsvector(
                        "simple", func.unaccent(insert_stmt.excluded.doc_text)
                    ),
                },
            )
            await session.execute(upsert_stmt)
    else:
        jids = [r.job_id for r in rows]
        await session.execute(delete(JobIndexRow).where(JobIndexRow.job_id.in_(jids)))
        for row, vec in zip(rows, vectors, strict=True):
            session.add(
                JobIndexRow(
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
            )

    await session.commit()
    return len(rows)


async def delete_jobs_by_project(session: AsyncSession, project_id: str) -> int:
    """Removes all jobs for a project from job_index."""
    stmt = delete(JobIndexRow).where(JobIndexRow.project_id == project_id)
    res = await session.execute(stmt)
    await session.commit()
    return getattr(res, "rowcount", 0) or 0


async def delete_job_by_id(session: AsyncSession, job_id: str) -> int:
    """Removes a single job from job_index."""
    stmt = delete(JobIndexRow).where(JobIndexRow.job_id == job_id)
    res = await session.execute(stmt)
    await session.commit()
    return getattr(res, "rowcount", 0) or 0
