from unittest.mock import AsyncMock, MagicMock

import pytest

from app.db.models import CareerIngestionRun
from app.features.career_rag.pipeline import IngestionPipeline
from app.features.career_rag.schemas import CareerKnowledgeRecord, SourceMetadata
from app.ml.fakes import FakeEmbedder


@pytest.mark.asyncio
async def test_pipeline_ingest_records_flow():
    """Verify ingestion flow processes records, generates embeddings, and saves chunks."""
    records = [
        CareerKnowledgeRecord(
            source_meta=SourceMetadata(
                source_id="roadmap.sh",
                source_record_id="ai_engineer",
                source_type="learning_roadmap",
                domain="AI",
            ),
            title="AI Engineer",
            content="Guide to becoming an AI Engineer",
            sections=[
                {"title": "Mathematics", "content": "Linear Algebra, Calculus, Statistics"},
                {"title": "Machine Learning", "content": "Scikit-Learn, PyTorch, Transformers"},
            ],
        )
    ]

    mock_session = AsyncMock()
    mock_session.add = MagicMock()
    mock_session.bind = None  # Non-PG mode (generic SQLite/fallback path)

    # In non-PG fallback, session.get returns None (no existing chunk)
    mock_session.get = AsyncMock(return_value=None)
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()

    # Mock get_last_completed_run returning None (first run)
    mock_scalar_res = MagicMock()
    mock_scalar_res.scalar_one_or_none.return_value = None
    mock_session.execute = AsyncMock(return_value=mock_scalar_res)

    pipeline = IngestionPipeline(
        session=mock_session,
        embedder=FakeEmbedder(),
        batch_size=10,
    )

    run = await pipeline.ingest_records(
        records=records,
        source_id="roadmap.sh",
        source_version="v1",
        manifest_hash="hash-123",
    )

    assert run.status == "completed"
    assert run.chunks_count == 2
    assert run.manifest_hash == "hash-123"
    assert mock_session.commit.called


@pytest.mark.asyncio
async def test_pipeline_idempotency_manifest_check():
    """Verify that if manifest_hash matches last completed run, ingestion is skipped."""
    mock_session = AsyncMock()

    existing_run = CareerIngestionRun(
        id="existing-run-id",
        source_id="roadmap.sh",
        source_version="v1",
        status="completed",
        chunks_count=10,
        manifest_hash="identical-hash",
    )

    mock_scalar_res = MagicMock()
    mock_scalar_res.scalar_one_or_none.return_value = existing_run
    mock_session.execute = AsyncMock(return_value=mock_scalar_res)

    pipeline = IngestionPipeline(session=mock_session, embedder=FakeEmbedder())

    # When manifest_hash == "identical-hash" and force=False
    run = await pipeline.ingest_records(
        records=[],
        source_id="roadmap.sh",
        source_version="v1",
        manifest_hash="identical-hash",
        force=False,
    )

    assert run.id == "existing-run-id"
    assert run.status == "completed"
    assert run.manifest_hash == "identical-hash"
