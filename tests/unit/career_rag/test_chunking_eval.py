from app.features.career_rag.schemas import CareerKnowledgeRecord, SourceMetadata
from evals.uc1.chunking_eval import (
    compare_chunking_strategies,
    compute_chunking_metrics,
    fixed_character_chunk,
    naive_paragraph_chunk,
)


def _make_sample_roadmap_record() -> CareerKnowledgeRecord:
    content = """# Backend Developer

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/backend

---

## 1. Beginner

### 1.1 Introduction
- **Go**: Go is a statically typed compiled language designed for concurrency with goroutines and channels.
- **Ruby**: Ruby is a dynamic object-oriented language prioritizing simplicity.

### 1.2 Pick a Language
- **Python**: Python is versatile with dynamic typing and standard library.
- **Java**: Java is enterprise-grade running on the JVM.

---

## 2. Intermediate

### 2.1 Databases
- **PostgreSQL**: Relational database supporting advanced indexing and ACID transactions.
"""
    sections = [
        {
            "title": "1. Beginner - 1.1 Introduction",
            "content": "- **Go**: Go is a statically typed compiled language designed for concurrency with goroutines and channels.\n- **Ruby**: Ruby is a dynamic object-oriented language prioritizing simplicity.",
        },
        {
            "title": "1. Beginner - 1.2 Pick a Language",
            "content": "- **Python**: Python is versatile with dynamic typing and standard library.\n- **Java**: Java is enterprise-grade running on the JVM.",
        },
        {
            "title": "2. Intermediate - 2.1 Databases",
            "content": "- **PostgreSQL**: Relational database supporting advanced indexing and ACID transactions.",
        },
    ]

    return CareerKnowledgeRecord(
        title="Backend Developer",
        content=content,
        sections=sections,
        source_meta=SourceMetadata(
            source_id="roadmap.sh",
            source_record_id="roadmap-backend",
            source_url="https://roadmap.sh/backend",
            source_type="learning_roadmap",
            domain="software_engineering",
        ),
    )


def test_fixed_character_chunk_produces_fragmentation():
    record = _make_sample_roadmap_record()
    chunks = fixed_character_chunk(record, chunk_size=200, overlap=30)
    metrics = compute_chunking_metrics(chunks, record_title=record.title)

    # Fixed character windows slice arbitrary offsets
    assert len(chunks) > 1
    assert metrics["boundary_fragmentation_rate"] > 0.0


def test_naive_paragraph_chunk_loses_parent_context():
    record = _make_sample_roadmap_record()
    chunks = naive_paragraph_chunk(record)
    metrics = compute_chunking_metrics(chunks, record_title=record.title)

    # Paragraphs like "- **Go**: Go is..." have no parent "Backend Developer" title
    assert metrics["orphan_chunk_rate"] > 0.0


def test_compare_chunking_strategies_proves_semantic_superiority():
    record = _make_sample_roadmap_record()
    comparison = compare_chunking_strategies([record])

    fixed_res = comparison["Fixed-Character (600 chars, 100 overlap)"]
    para_res = comparison["Naive Paragraph (Split on \\n\\n)"]
    semantic_res = comparison["Content-Aware Semantic (Occupify UC1)"]

    # Semantic chunker must achieve PASS and superior integrity
    assert semantic_res["adherence_verdict"] == "PASS (Appropriate)"
    assert semantic_res["orphan_chunk_rate"] == 0.0
    assert semantic_res["semantic_integrity_score"] > fixed_res["semantic_integrity_score"]
    assert semantic_res["semantic_integrity_score"] > para_res["semantic_integrity_score"]
