from unittest.mock import AsyncMock

import pytest

from app.features.career_rag.retrieval import (
    CareerKnowledgeRetriever,
    RetrievalHit,
    rrf_combine,
)
from app.ml.fakes import FakeEmbedder


def test_rrf_combine_ranking_and_scores():
    """Verify RRF formula Score(d) = sum(1.0 / (k + rank)) and score ranking."""
    # Doc 1: vector rank 1, keyword rank 2
    # Doc 2: vector rank 2, keyword rank 1
    # Doc 3: vector rank 3, not in keyword
    hit1_vec = RetrievalHit(
        chunk_id="chunk-1",
        source_id="roadmap.sh",
        source_record_id="rec-1",
        source_type="learning_roadmap",
        title="Title 1",
        content="Content 1",
        score=0.9,
    )
    hit2_vec = RetrievalHit(
        chunk_id="chunk-2",
        source_id="esco",
        source_record_id="rec-2",
        source_type="occupation_taxonomy",
        title="Title 2",
        content="Content 2",
        score=0.8,
    )
    hit3_vec = RetrievalHit(
        chunk_id="chunk-3",
        source_id="onet",
        source_record_id="rec-3",
        source_type="occupation_taxonomy",
        title="Title 3",
        content="Content 3",
        score=0.7,
    )

    hit2_kw = RetrievalHit(
        chunk_id="chunk-2",
        source_id="esco",
        source_record_id="rec-2",
        source_type="occupation_taxonomy",
        title="Title 2",
        content="Content 2",
        score=5.0,
    )
    hit1_kw = RetrievalHit(
        chunk_id="chunk-1",
        source_id="roadmap.sh",
        source_record_id="rec-1",
        source_type="learning_roadmap",
        title="Title 1",
        content="Content 1",
        score=4.0,
    )

    fused = rrf_combine(
        vector_hits=[hit1_vec, hit2_vec, hit3_vec],
        keyword_hits=[hit2_kw, hit1_kw],
        k=60,
        top_k=3,
    )

    assert len(fused) == 3
    # Both chunk-1 and chunk-2 have ranks 1 and 2:
    # chunk-1: 1/(60+1) + 1/(60+2) = 1/61 + 1/62
    # chunk-2: 1/(60+2) + 1/(60+1) = 1/62 + 1/61 (identical score)
    expected_top_score = 1.0 / 61.0 + 1.0 / 62.0
    assert abs(fused[0].rrf_score - expected_top_score) < 1e-6
    assert abs(fused[1].rrf_score - expected_top_score) < 1e-6

    # chunk-3 only has vector rank 3: 1/(60+3) = 1/63
    assert fused[2].chunk_id == "chunk-3"
    assert abs(fused[2].rrf_score - 1.0 / 63.0) < 1e-6
    assert fused[2].vector_rank == 3
    assert fused[2].keyword_rank is None


@pytest.mark.asyncio
async def test_retriever_filter_construction():
    """Verify metadata filter building in CareerKnowledgeRetriever."""
    mock_session = AsyncMock()
    retriever = CareerKnowledgeRetriever(session=mock_session, embedder=FakeEmbedder())

    filters = retriever._build_filters(
        source_id="roadmap.sh",
        source_type="learning_roadmap",
        domain="software",
        tags=["python", "fastapi"],
    )
    assert len(filters) == 4


@pytest.mark.asyncio
async def test_retriever_search_hybrid_mock():
    """Verify search_hybrid orchestrates vector search, keyword search, and RRF fusion."""
    mock_session = AsyncMock()
    retriever = CareerKnowledgeRetriever(session=mock_session, embedder=FakeEmbedder())

    mock_vec_hit = RetrievalHit(
        chunk_id="c-vec",
        source_id="roadmap.sh",
        source_record_id="rec-1",
        source_type="learning_roadmap",
        title="Vector Hit",
        content="Vector content",
        score=0.95,
    )
    mock_kw_hit = RetrievalHit(
        chunk_id="c-kw",
        source_id="roadmap.sh",
        source_record_id="rec-2",
        source_type="learning_roadmap",
        title="Keyword Hit",
        content="Keyword content",
        score=3.5,
    )

    retriever.search_vector = AsyncMock(return_value=[mock_vec_hit])
    retriever.search_keyword = AsyncMock(return_value=[mock_kw_hit])

    results = await retriever.search_hybrid(query="developer", top_k=5)
    assert len(results) == 2
    assert {r.chunk_id for r in results} == {"c-vec", "c-kw"}
    assert retriever.search_vector.called
    assert retriever.search_keyword.called
