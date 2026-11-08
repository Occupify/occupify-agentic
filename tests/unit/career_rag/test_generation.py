from unittest.mock import AsyncMock, MagicMock

import pytest

from app.features.career_rag.retrieval import RetrievalHit
from app.features.career_rag.service import CareerConsultantService
from app.ml.fakes import FakeEmbedder, FakeReranker


@pytest.mark.asyncio
async def test_generation_grounded_answer():
    """Verify that sufficient evidence results in non-abstention answer with valid citations."""
    mock_session = AsyncMock()
    service = CareerConsultantService(
        session=mock_session,
        embedder=FakeEmbedder(),
        reranker=FakeReranker(),
        confidence_threshold=0.35,
    )

    hit1 = RetrievalHit(
        chunk_id="chunk-backend-1",
        source_id="roadmap.sh",
        source_record_id="backend",
        source_url="https://roadmap.sh/backend",
        source_type="learning_roadmap",
        title="Backend Developer - Python",
        content="Learn Python, FastAPI, and relational databases for modern backend development.",
        score=0.85,
    )
    hit2 = RetrievalHit(
        chunk_id="chunk-esco-1",
        source_id="esco",
        source_record_id="2512.1",
        source_url="http://data.europa.eu/esco/occupation/2512.1",
        source_type="occupation_taxonomy",
        title="Software Developer",
        content="Software developers analyze user requirements and develop backend software architectures.",
        score=0.75,
    )

    # Mock hybrid search and reranker
    service.retriever.search_hybrid = AsyncMock(return_value=[hit1, hit2])
    service.reranker.rerank = MagicMock(
        return_value=[
            hit1.model_copy(update={"rerank_score": 0.88, "score": 0.88}),
            hit2.model_copy(update={"rerank_score": 0.72, "score": 0.72}),
        ]
    )

    response = await service.consult(query="Python backend development roadmap")

    assert response.abstention is False
    assert response.abstention_reason is None
    assert len(response.citations) == 2
    assert response.citations[0].chunk_id == "chunk-backend-1"
    assert response.citations[0].source_id == "roadmap.sh"
    assert response.citations[0].source_url == "https://roadmap.sh/backend"
    assert "FastAPI" in response.citations[0].snippet

    assert len(response.recommendations) >= 1
    assert "### Tư vấn lộ trình & tiêu chuẩn nghề nghiệp" in response.answer
    assert "#### 📚 Nguồn trích dẫn (Citations):" in response.answer
    assert "chunk-backend-1" in response.answer


@pytest.mark.asyncio
async def test_generation_abstention_on_empty_candidates():
    """Verify clean abstention when search returns empty results (Rule 5.49)."""
    mock_session = AsyncMock()
    service = CareerConsultantService(
        session=mock_session,
        embedder=FakeEmbedder(),
        reranker=FakeReranker(),
    )

    service.retriever.search_hybrid = AsyncMock(return_value=[])

    response = await service.consult(query="Intergalactic Warp Drive Pilot")

    assert response.abstention is True
    assert "No candidate knowledge chunks found" in (response.abstention_reason or "")
    assert len(response.citations) == 0
    assert len(response.recommendations) == 0
    assert "chưa có thông tin chính thức phù hợp" in response.answer


@pytest.mark.asyncio
async def test_generation_abstention_on_low_confidence():
    """Verify clean abstention when top candidate score is below threshold (Rule 5.49)."""
    mock_session = AsyncMock()
    service = CareerConsultantService(
        session=mock_session,
        embedder=FakeEmbedder(),
        reranker=FakeReranker(),
        confidence_threshold=0.50,
    )

    low_hit = RetrievalHit(
        chunk_id="chunk-unrelated",
        source_id="onet",
        source_record_id="99-9999",
        source_type="occupation_taxonomy",
        title="Unrelated Occupation",
        content="Completely unrelated content to astronomy warp drives.",
        score=0.20,
    )
    service.retriever.search_hybrid = AsyncMock(return_value=[low_hit])
    service.reranker.rerank = MagicMock(
        return_value=[low_hit.model_copy(update={"rerank_score": 0.22, "score": 0.22})]
    )

    response = await service.consult(query="Warp Drive navigation protocols")

    assert response.abstention is True
    assert "below confidence threshold" in (response.abstention_reason or "")
    assert len(response.citations) == 0
    assert "chưa đủ độ tin cậy" in response.answer


@pytest.mark.asyncio
async def test_generation_conflicting_sources_disclosure():
    """Verify disclosure when sources from different frameworks (ESCO & O*NET) are both present (Rule 5.48)."""
    mock_session = AsyncMock()
    service = CareerConsultantService(
        session=mock_session,
        embedder=FakeEmbedder(),
        reranker=FakeReranker(),
        confidence_threshold=0.30,
    )

    hit_esco = RetrievalHit(
        chunk_id="c-esco",
        source_id="esco",
        source_record_id="esco-1",
        source_type="occupation_taxonomy",
        title="Data Scientist (ESCO)",
        content="European framework data scientist specifications.",
        score=0.8,
    )
    hit_onet = RetrievalHit(
        chunk_id="c-onet",
        source_id="onet",
        source_record_id="onet-1",
        source_type="occupation_taxonomy",
        title="Data Scientists (O*NET)",
        content="US framework occupational abilities and knowledge for data scientists.",
        score=0.78,
    )

    service.retriever.search_hybrid = AsyncMock(return_value=[hit_esco, hit_onet])
    service.reranker.rerank = MagicMock(
        return_value=[
            hit_esco.model_copy(update={"rerank_score": 0.85, "score": 0.85}),
            hit_onet.model_copy(update={"rerank_score": 0.82, "score": 0.82}),
        ]
    )

    response = await service.consult(query="Data scientist competencies")

    assert response.abstention is False
    assert len(response.conflicting_sources) > 0
    assert "Lưu ý khác biệt nguồn chuẩn hóa" in response.answer
