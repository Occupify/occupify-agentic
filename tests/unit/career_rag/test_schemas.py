import pytest
from pydantic import ValidationError

from app.features.career_rag.schemas import (
    CareerRecommendation,
    Citation,
    GroundedCareerResponse,
)


def test_citation_schema_validation():
    cit = Citation(
        chunk_id="chunk-123",
        source_id="roadmap.sh",
        source_record_id="backend",
        title="Backend Developer - Python",
        source_url="https://roadmap.sh/backend",
        snippet="FastAPI and Python asynchronous programming",
    )
    assert cit.chunk_id == "chunk-123"
    assert cit.source_id == "roadmap.sh"
    assert cit.source_url == "https://roadmap.sh/backend"
    assert "FastAPI" in cit.snippet

    # Missing required field
    with pytest.raises(ValidationError):
        Citation(chunk_id="chunk-123", title="No source")


def test_career_recommendation_schema():
    cit = Citation(
        chunk_id="c-1",
        source_id="esco",
        source_record_id="occ-1",
        title="Software Engineer",
        snippet="Designs software systems",
    )
    rec = CareerRecommendation(
        claim="Software engineers require knowledge of algorithms",
        evidence_citations=[cit],
        confidence_level="high",
    )
    assert rec.confidence_level == "high"
    assert len(rec.evidence_citations) == 1
    assert rec.evidence_citations[0].chunk_id == "c-1"

    # Invalid confidence level
    with pytest.raises(ValidationError):
        CareerRecommendation(
            claim="Invalid",
            confidence_level="unsupported_level",  # type: ignore
        )


def test_grounded_career_response_schema():
    cit = Citation(
        chunk_id="c-1",
        source_id="onet",
        source_record_id="15-1252.00",
        title="Software Developers",
        snippet="Analyze users' needs and then design, test, and develop software",
    )
    rec = CareerRecommendation(
        claim="Develops software according to user requirements",
        evidence_citations=[cit],
        confidence_level="high",
    )
    resp = GroundedCareerResponse(
        answer="Overview of software developers",
        recommendations=[rec],
        citations=[cit],
        abstention=False,
        abstention_reason=None,
        conflicting_sources=[],
    )
    assert not resp.abstention
    assert resp.abstention_reason is None
    assert len(resp.recommendations) == 1
    assert len(resp.citations) == 1


def test_grounded_career_response_abstention():
    resp = GroundedCareerResponse(
        answer="I abstain due to lack of evidence",
        recommendations=[],
        citations=[],
        abstention=True,
        abstention_reason="No documents found above confidence threshold.",
        conflicting_sources=[],
    )
    assert resp.abstention
    assert resp.abstention_reason == "No documents found above confidence threshold."
    assert len(resp.citations) == 0
