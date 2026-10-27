import hashlib
import logging
from datetime import datetime
from typing import Any

from sqlalchemy import and_, func, or_, select, text, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import IndexMetaModel, JobIndexRow, utc_now
from app.features.job_match.ports import (
    IndexHit,
    IndexMeta,
    IndexRow,
    MatchCriteria,
    UpsertStats,
)
from app.features.job_match.schemas import HoursPerDayFilter

logger = logging.getLogger(__name__)


_index_building: bool = False
_index_jobs_count: int = 0
_index_empty: bool = True


def set_index_building(val: bool) -> None:
    global _index_building
    _index_building = val


def set_index_jobs_count(count: int) -> None:
    global _index_jobs_count, _index_empty
    _index_jobs_count = count
    _index_empty = count == 0


def set_index_empty(val: bool) -> None:
    global _index_empty
    _index_empty = val


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

    def is_usable(self) -> bool:
        """Synchronous check if store has an active session, embedder, and is not rebuilding or empty."""
        if self.session is None:
            return False
        if self.embedder is None:
            return False
        if _index_building:
            return False
        if self._is_empty is True:
            return False
        if self._is_empty is None and _index_empty:
            return False
        return True

    async def upsert(self, rows: list[IndexRow]) -> UpsertStats:
        """Upserts a batch of IndexRows.

        Detects identical content_hash to avoid re-embedding on metadata-only updates.
        Computes search_tsv vector for lexical search immediately upon insert.
        """
        inserted = 0
        updated = 0
        reembed_queued = 0
        unchanged = 0

        job_ids = [r.job_id for r in rows]
        existing_stmt = select(JobIndexRow).where(JobIndexRow.job_id.in_(job_ids))
        res = await self.session.execute(existing_stmt)
        existing_map = {row.job_id: row for row in res.scalars().all()}

        is_pg = self.session.bind and "postgresql" in str(self.session.bind.dialect.name)

        for row in rows:
            content_hash = hashlib.sha256(row.doc_text.encode("utf-8")).hexdigest()
            existing = existing_map.get(row.job_id)

            if existing is None:
                # Insert new row
                new_db_row = JobIndexRow(
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
                    active=(row.project_status == "OPEN" and row.job_status == "RECRUITING"),
                    missed_sweeps=0,
                    content_hash=content_hash,
                    embedding=None,
                    embedding_model=None,
                )
                self.session.add(new_db_row)
                inserted += 1
                reembed_queued += 1

                if is_pg:
                    # Update search_tsv via SQL function
                    new_db_row.search_tsv = func.to_tsvector("simple", func.unaccent(row.doc_text))
            else:
                # Existing row
                content_changed = existing.content_hash != content_hash
                existing.project_title = row.project_title
                existing.project_description = row.project_description
                existing.job_title = row.job_title
                existing.job_description = row.job_description
                existing.skills = row.skills
                existing.requirements = row.requirements
                existing.salary_type = row.salary_type or existing.salary_type
                existing.budget_min = row.budget_min
                existing.budget_max = row.budget_max
                existing.experience_level = row.experience_level or existing.experience_level
                existing.period = row.period or existing.period
                existing.hours_per_day = row.hours_per_day
                existing.project_status = row.project_status
                existing.job_status = row.job_status
                existing.active = row.project_status == "OPEN" and row.job_status == "RECRUITING"
                existing.missed_sweeps = 0

                if content_changed:
                    existing.doc_text = row.doc_text
                    existing.content_hash = content_hash
                    existing.embedding = None
                    existing.embedding_model = None
                    if is_pg:
                        existing.search_tsv = func.to_tsvector(
                            "simple", func.unaccent(row.doc_text)
                        )
                    updated += 1
                    reembed_queued += 1
                else:
                    updated += 1

        await self.session.commit()
        if inserted > 0 or updated > 0:
            set_index_jobs_count(max(1, inserted + updated))
        return UpsertStats(
            inserted=inserted,
            updated=updated,
            reembed_queued=reembed_queued,
            unchanged=unchanged,
        )

    async def embed_backlog_batch(self, batch_size: int = 100) -> int:
        """Finds active rows without embeddings and computes them."""
        stmt = (
            select(JobIndexRow)
            .where(and_(JobIndexRow.active.is_(True), JobIndexRow.embedding.is_(None)))
            .limit(batch_size)
        )
        res = await self.session.execute(stmt)
        rows = res.scalars().all()

        if not rows or not self.embedder:
            return 0

        texts = [r.doc_text for r in rows]
        embeddings = self.embedder.embed(texts)
        for r, emb in zip(rows, embeddings, strict=False):
            r.embedding = emb

        await self.session.commit()
        return len(rows)

    def _build_filter_clauses(self, criteria: MatchCriteria) -> list[Any]:
        """Constructs SQLAlchemy WHERE clauses for MatchCriteria."""
        clauses = [
            JobIndexRow.active.is_(True),
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
        # Set HNSW index params if in PostgreSQL
        try:
            await self.session.execute(text("SET LOCAL hnsw.ef_search = 200;"))
            await self.session.execute(text("SET LOCAL hnsw.iterative_scan = 'relaxed_order';"))
        except Exception:
            pass

        base_filters = self._build_filter_clauses(criteria)

        # 1. Dense vector searches
        dense_results: list[list[IndexHit]] = []
        for q_vec in dense_queries:
            # Distance using cosine_distance <=>
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
            # In PG, use search_tsv @@ plainto_tsquery
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
                # Fallback for SQLite/test
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
                    active=r.active,
                    missed_sweeps=r.missed_sweeps,
                    content_hash=r.content_hash,
                    embedding=r.embedding,
                    embedding_model=r.embedding_model,
                    indexed_at=r.indexed_at,
                )
            )
        return results

    async def mark_inactive(self, job_ids: list[str]) -> None:
        """Marks given job_ids as inactive."""
        if not job_ids:
            return
        stmt = update(JobIndexRow).where(JobIndexRow.job_id.in_(job_ids)).values(active=False)
        await self.session.execute(stmt)
        await self.session.commit()

    async def handle_model_mismatch(self, new_model: str, new_dim: int) -> None:
        """Resets all embeddings when embedding model changes."""
        await self.session.execute(
            update(JobIndexRow).values(embedding=None, embedding_model=new_model)
        )

        res = await self.session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
        meta_row = res.scalar_one_or_none()
        if meta_row is None:
            meta_row = IndexMetaModel(
                id=1,
                embed_model=new_model,
                dim=new_dim,
                source="core_rpc",
                built_at=utc_now(),
                jobs_n=0,
            )
            self.session.add(meta_row)
        else:
            meta_row.embed_model = new_model
            meta_row.dim = new_dim
            meta_row.built_at = utc_now()

        await self.session.commit()

    async def meta(self) -> IndexMeta:
        """Returns current index metadata."""
        res = await self.session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))
        meta_row = res.scalar_one_or_none()
        count_res = await self.session.execute(select(func.count(JobIndexRow.job_id)))
        jobs_n = count_res.scalar() or 0

        if meta_row is None:
            return IndexMeta(
                embed_model="",
                dim=1024,
                source="core_rpc",
                built_at=datetime.now(),
                jobs_n=jobs_n,
            )

        return IndexMeta(
            embed_model=meta_row.embed_model,
            dim=meta_row.dim,
            source=meta_row.source,
            built_at=meta_row.built_at,
            jobs_n=jobs_n,
        )
