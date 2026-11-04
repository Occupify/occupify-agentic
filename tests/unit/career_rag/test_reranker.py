from app.features.career_rag.rerank import CareerKnowledgeReranker
from app.features.career_rag.retrieval import RetrievalHit
from app.ml.fakes import FakeReranker


def test_reranker_scoring_and_diagnostics():
    """Verify reranking rescores candidates and retains original diagnostics."""
    fake_reranker = FakeReranker()
    service = CareerKnowledgeReranker(reranker=fake_reranker)

    candidates = [
        RetrievalHit(
            chunk_id="chunk-1",
            source_id="roadmap.sh",
            source_record_id="frontend",
            source_type="learning_roadmap",
            title="Frontend Developer - CSS Basics",
            content="Styling and layout using CSS Flexbox and Grid",
            score=0.03,
            vector_rank=1,
            vector_score=0.88,
            keyword_rank=5,
            keyword_score=1.2,
            rrf_score=0.03,
        ),
        RetrievalHit(
            chunk_id="chunk-2",
            source_id="roadmap.sh",
            source_record_id="backend",
            source_type="learning_roadmap",
            title="Backend Developer - Python APIs",
            content="Building scalable REST APIs with Python and FastAPI",
            score=0.02,
            vector_rank=4,
            vector_score=0.75,
            keyword_rank=2,
            keyword_score=2.1,
            rrf_score=0.02,
        ),
    ]

    query = "FastAPI Python backend API development"
    reranked = service.rerank(query, candidates, top_n=2)

    assert len(reranked) == 2
    # chunk-2 should score higher because it matches Python and FastAPI words
    top_hit = reranked[0]
    assert top_hit.chunk_id == "chunk-2"
    assert top_hit.rerank_score is not None
    assert top_hit.rerank_score > reranked[1].rerank_score
    # Verify diagnostics preserved
    assert top_hit.vector_rank == 4
    assert top_hit.keyword_rank == 2
    assert top_hit.rrf_score == 0.02


def test_reranker_empty_candidates():
    service = CareerKnowledgeReranker(reranker=FakeReranker())
    assert service.rerank("some query", []) == []
