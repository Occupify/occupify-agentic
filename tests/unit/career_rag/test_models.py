from app.db.models import CareerIngestionRun, CareerKnowledgeChunk


def test_career_knowledge_chunk_model():
    """Verify CareerKnowledgeChunk columns, constraints and table args."""
    assert CareerKnowledgeChunk.__tablename__ == "career_knowledge_chunks"

    # Check table columns exist
    columns = {c.name: c for c in CareerKnowledgeChunk.__table__.columns}
    expected_cols = [
        "id",
        "source_id",
        "source_record_id",
        "source_url",
        "source_version",
        "source_type",
        "title",
        "content",
        "chunk_metadata",
        "embedding",
        "search_tsv",
    ]
    for col in expected_cols:
        assert col in columns, f"Missing column {col} in CareerKnowledgeChunk"

    # Check unique constraint
    unique_constraints = [
        c
        for c in CareerKnowledgeChunk.__table__.constraints
        if getattr(c, "name", None) == "uq_career_chunk_source_record"
    ]
    assert len(unique_constraints) == 1
    uq = unique_constraints[0]
    assert {c.name for c in uq.columns} == {"source_id", "source_record_id", "title"}

    # Check indexes
    index_names = {idx.name for idx in CareerKnowledgeChunk.__table__.indexes}
    assert "ix_career_knowledge_chunks_embedding_hnsw" in index_names
    assert "ix_career_knowledge_chunks_search_tsv_gin" in index_names
    assert "ix_career_knowledge_chunks_source_filter" in index_names


def test_career_ingestion_run_model():
    """Verify CareerIngestionRun columns and defaults."""
    assert CareerIngestionRun.__tablename__ == "career_ingestion_runs"

    columns = {c.name: c for c in CareerIngestionRun.__table__.columns}
    expected_cols = [
        "id",
        "source_id",
        "source_version",
        "status",
        "chunks_count",
        "manifest_hash",
        "created_at",
        "finished_at",
    ]
    for col in expected_cols:
        assert col in columns, f"Missing column {col} in CareerIngestionRun"


def test_model_instantiation():
    """Verify models can be initialized with expected attributes."""
    chunk = CareerKnowledgeChunk(
        id="chunk-123",
        source_id="roadmap.sh",
        source_record_id="ai_engineer",
        source_url="https://roadmap.sh/ai-engineer",
        source_version="v1",
        source_type="learning_roadmap",
        title="AI Engineer Overview",
        content="AI engineers build intelligent systems.",
        chunk_metadata={"domain": "AI"},
        embedding=[0.01] * 1024,
    )
    assert chunk.id == "chunk-123"
    assert chunk.source_id == "roadmap.sh"
    assert len(chunk.embedding) == 1024

    run = CareerIngestionRun(
        id="run-456",
        source_id="esco",
        source_version="v1.1",
        status="completed",
        chunks_count=150,
        manifest_hash="abc123hash",
    )
    assert run.id == "run-456"
    assert run.chunks_count == 150
