from typing import Any

from pydantic import BaseModel, Field
from sqlalchemy import String, and_, cast, func, or_, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import CareerKnowledgeChunk
from app.ml.embedder import Embedder
from app.ml.fakes import FakeEmbedder


class RetrievalHit(BaseModel):
    chunk_id: str
    source_id: str
    source_record_id: str
    source_url: str | None = None
    source_version: str = "v1"
    source_type: str
    title: str
    content: str
    chunk_metadata: dict[str, Any] = Field(default_factory=dict)

    # Retrieval scores & diagnostics
    score: float = 0.0
    vector_rank: int | None = None
    vector_score: float | None = None
    keyword_rank: int | None = None
    keyword_score: float | None = None
    rrf_score: float | None = None
    rerank_score: float | None = None


def rrf_combine(
    vector_hits: list[RetrievalHit],
    keyword_hits: list[RetrievalHit],
    k: int = 60,
    top_k: int = 20,
) -> list[RetrievalHit]:
    """Combines vector and keyword search results using Reciprocal Rank Fusion (RRF).
    Score(d) = sum(1.0 / (k + rank))
    Retains original vector and keyword rank/score diagnostics for auditability.
    """
    rrf_scores: dict[str, float] = {}
    combined_map: dict[str, RetrievalHit] = {}

    for rank, hit in enumerate(vector_hits, start=1):
        cid = hit.chunk_id
        rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (k + rank))
        if cid not in combined_map:
            combined_map[cid] = hit.model_copy(deep=True)
        combined_map[cid].vector_rank = rank
        combined_map[cid].vector_score = hit.score

    for rank, hit in enumerate(keyword_hits, start=1):
        cid = hit.chunk_id
        rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (k + rank))
        if cid not in combined_map:
            combined_map[cid] = hit.model_copy(deep=True)
        combined_map[cid].keyword_rank = rank
        combined_map[cid].keyword_score = hit.score

    sorted_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)

    results: list[RetrievalHit] = []
    for cid in sorted_ids[:top_k]:
        hit = combined_map[cid]
        hit.rrf_score = rrf_scores[cid]
        hit.score = rrf_scores[cid]
        results.append(hit)

    return results


class CareerKnowledgeRetriever:
    """Hybrid retrieval service across CareerKnowledgeChunk in PostgreSQL/pgvector.

    Supports:
    - Semantic vector cosine similarity search.
    - Keyword / full-text search with TSVector (with plain text/ILIKE fallback).
    - Metadata filters: source_id, source_type, domain, tags.
    - Reciprocal Rank Fusion (RRF).
    """

    def __init__(
        self,
        session: AsyncSession,
        embedder: Embedder | FakeEmbedder | None = None,
    ) -> None:
        self.session = session
        self._embedder = embedder

    def _get_embedder(self) -> Embedder | FakeEmbedder:
        if self._embedder is None:
            self._embedder = Embedder()
        return self._embedder

    def _build_filters(
        self,
        source_id: str | None = None,
        source_type: str | None = None,
        domain: str | None = None,
        tags: list[str] | None = None,
    ) -> list[Any]:
        filters: list[Any] = []
        if source_id:
            filters.append(CareerKnowledgeChunk.source_id == source_id)
        if source_type:
            filters.append(CareerKnowledgeChunk.source_type == source_type)
        if domain:
            filters.append(
                cast(CareerKnowledgeChunk.chunk_metadata["domain"], String).ilike(f"%{domain}%")
            )
        if tags:
            # Match if any tag is in tags metadata or content
            tag_conds = [
                cast(CareerKnowledgeChunk.chunk_metadata["tags"], String).ilike(f"%{t}%")
                for t in tags
            ]
            if tag_conds:
                filters.append(or_(*tag_conds))
        return filters

    async def search_vector(
        self,
        query: str,
        top_k: int = 20,
        filters: list[Any] | None = None,
        query_vector: list[float] | None = None,
    ) -> list[RetrievalHit]:
        """Performs cosine distance search on CareerKnowledgeChunk.embedding."""
        if query_vector is None:
            embedder = self._get_embedder()
            vecs = embedder.embed([query])
            if not vecs:
                return []
            query_vector = vecs[0]

        base_filters = list(filters or [])
        cosine_dist = CareerKnowledgeChunk.embedding.cosine_distance(query_vector)

        stmt = (
            select(
                CareerKnowledgeChunk,
                cosine_dist.label("dist"),
            )
            .where(and_(*base_filters))
            .order_by(cosine_dist)
            .limit(top_k)
        )

        res = await self.session.execute(stmt)
        hits: list[RetrievalHit] = []
        for rank, (chunk, dist) in enumerate(res.all(), start=1):
            score = max(0.0, 1.0 - float(dist)) if dist is not None else 0.0
            hits.append(
                RetrievalHit(
                    chunk_id=chunk.id,
                    source_id=chunk.source_id,
                    source_record_id=chunk.source_record_id,
                    source_url=chunk.source_url,
                    source_version=chunk.source_version,
                    source_type=chunk.source_type,
                    title=chunk.title,
                    content=chunk.content,
                    chunk_metadata=chunk.chunk_metadata or {},
                    score=score,
                    vector_rank=rank,
                    vector_score=score,
                )
            )
        return hits

    async def search_keyword(
        self,
        query: str,
        top_k: int = 20,
        filters: list[Any] | None = None,
    ) -> list[RetrievalHit]:
        """Performs TSVector full-text search with ILIKE fallback."""
        if not query or not query.strip():
            return []

        base_filters = list(filters or [])
        is_pg = self.session.bind and "postgresql" in str(
            getattr(self.session.bind.dialect, "name", "")
        )

        if is_pg:
            # Use websearch_to_tsquery or plainto_tsquery
            ts_query = func.websearch_to_tsquery("simple", func.unaccent(query))
            rank_expr = func.ts_rank_cd(CareerKnowledgeChunk.search_tsv, ts_query)
            stmt = (
                select(CareerKnowledgeChunk, rank_expr.label("score"))
                .where(and_(*base_filters, CareerKnowledgeChunk.search_tsv.op("@@")(ts_query)))
                .order_by(text("score DESC"))
                .limit(top_k)
            )
        else:
            # Fallback for SQLite / tests
            like_pat = f"%{query.strip()}%"
            score_expr = func.length(CareerKnowledgeChunk.content).label("score")
            stmt = (
                select(CareerKnowledgeChunk, score_expr)
                .where(
                    and_(
                        *base_filters,
                        or_(
                            CareerKnowledgeChunk.title.ilike(like_pat),
                            CareerKnowledgeChunk.content.ilike(like_pat),
                        ),
                    )
                )
                .limit(top_k)
            )

        res = await self.session.execute(stmt)
        hits: list[RetrievalHit] = []
        for rank, (chunk, score_val) in enumerate(res.all(), start=1):
            s = float(score_val) if score_val is not None else 1.0
            hits.append(
                RetrievalHit(
                    chunk_id=chunk.id,
                    source_id=chunk.source_id,
                    source_record_id=chunk.source_record_id,
                    source_url=chunk.source_url,
                    source_version=chunk.source_version,
                    source_type=chunk.source_type,
                    title=chunk.title,
                    content=chunk.content,
                    chunk_metadata=chunk.chunk_metadata or {},
                    score=s,
                    keyword_rank=rank,
                    keyword_score=s,
                )
            )
        return hits

    async def search_hybrid(
        self,
        query: str,
        top_k: int = 20,
        source_id: str | None = None,
        source_type: str | None = None,
        domain: str | None = None,
        tags: list[str] | None = None,
        rrf_k: int = 60,
    ) -> list[RetrievalHit]:
        """Executes vector + keyword search and combines them with RRF."""
        filters = self._build_filters(
            source_id=source_id,
            source_type=source_type,
            domain=domain,
            tags=tags,
        )

        vector_hits = await self.search_vector(query, top_k=top_k * 2, filters=filters)
        keyword_hits = await self.search_keyword(query, top_k=top_k * 2, filters=filters)

        return rrf_combine(vector_hits, keyword_hits, k=rrf_k, top_k=top_k)
