from app.features.career_rag.chunking import chunk_record, compute_chunk_id
from app.features.career_rag.schemas import CareerKnowledgeRecord, SourceMetadata


def test_chunk_roadmap_record():
    """Verify semantic chunking of a roadmap into sections with parent context."""
    source_meta = SourceMetadata(
        source_id="roadmap.sh",
        source_record_id="backend_developer",
        source_url="https://roadmap.sh/backend",
        source_type="learning_roadmap",
        domain="software_engineering",
        geography="Global",
        extra={"related_roles": ["DevOps Engineer", "Frontend Developer"]},
    )
    record = CareerKnowledgeRecord(
        source_meta=source_meta,
        title="Backend Developer",
        content="Overview content",
        summary="Backend Developer Roadmap",
        sections=[
            {"title": "Beginner - Fundamentals", "content": "Learn HTTP, REST APIs, Git"},
            {
                "title": "Intermediate - Databases",
                "content": "Learn PostgreSQL, Redis, Query Optimization",
            },
            {
                "title": "Advanced - System Design",
                "content": "Learn Microservices, Caching, Event Driven",
            },
        ],
    )

    chunks = chunk_record(record)
    assert len(chunks) == 3

    # Check first chunk
    c0 = chunks[0]
    assert c0.source_id == "roadmap.sh"
    assert c0.source_record_id == "backend_developer"
    assert c0.title == "Backend Developer - Beginner - Fundamentals"
    assert "Learn HTTP, REST APIs" in c0.content
    assert "# Backend Developer" in c0.content
    assert c0.chunk_metadata["domain"] == "software_engineering"
    assert c0.chunk_metadata["parent_title"] == "Backend Developer"
    assert "DevOps Engineer" in c0.chunk_metadata["tags"]

    # Check idempotency of chunk_id
    expected_id = compute_chunk_id(
        "roadmap.sh", "backend_developer", "Backend Developer - Beginner - Fundamentals"
    )
    assert c0.chunk_id == expected_id


def test_chunk_taxonomy_record_esco():
    """Verify semantic chunking of an ESCO record into overview and skill clusters."""
    source_meta = SourceMetadata(
        source_id="esco",
        source_record_id="http://data.europa.eu/esco/occupation/1234",
        source_type="occupation_taxonomy",
        domain="Information Technology",
        geography="EU",
    )
    record = CareerKnowledgeRecord(
        source_meta=source_meta,
        title="Software Developer",
        content="Designs and develops software systems and applications.",
        summary="Software Developer ESCO Profile",
        skills=["SQL", "Python", "Git"],
        competencies=["Analytical Thinking", "Problem Solving"],
        raw_attributes={"isco_group": "2512"},
    )

    chunks = chunk_record(record)
    assert len(chunks) == 2

    overview_chunk = chunks[0]
    assert overview_chunk.title == "Software Developer - Overview & Profile"
    assert "Software Developer" in overview_chunk.content
    assert overview_chunk.chunk_metadata["profile_type"] == "summary"
    assert overview_chunk.chunk_metadata["geography"] == "EU"

    skills_chunk = chunks[1]
    assert skills_chunk.title == "Software Developer - Core Skills & Competencies"
    assert "SQL" in skills_chunk.content
    assert "Problem Solving" in skills_chunk.content
    assert skills_chunk.chunk_metadata["profile_type"] == "skills_cluster"
    assert "SQL" in skills_chunk.chunk_metadata["tags"]


def test_chunk_record_no_sections():
    """Verify chunking when no sections or skills exist falls back to single semantic chunk."""
    source_meta = SourceMetadata(
        source_id="roadmap.sh",
        source_record_id="simple_doc",
        source_type="learning_roadmap",
    )
    record = CareerKnowledgeRecord(
        source_meta=source_meta,
        title="Simple Guide",
        content="Just a simple guide without sections.",
    )

    chunks = chunk_record(record)
    assert len(chunks) == 1
    assert chunks[0].title == "Simple Guide"
    assert chunks[0].content == "Just a simple guide without sections."
