from decimal import Decimal

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.job_match.index.migrate import write_index
from app.features.job_match.index.store import PgJobIndex
from app.features.job_match.ports import IndexRow, MatchCriteria
from app.features.job_match.schemas import SalaryTypeFilter
from app.ml.fakes import FakeEmbedder


@pytest.fixture
def fake_embedder():
    return FakeEmbedder(dim=1024)


def make_test_row(
    job_id: str = "j-int-1",
    project_id: str = "p-int-1",
    job_title: str = "Java Backend Developer",
    doc_text: str = "Spring Boot PostgreSQL",
    salary_type: str = "MONTHLY",
    budget_min: float = 20000000,
    budget_max: float = 35000000,
    project_status: str = "OPEN",
    job_status: str = "RECRUITING",
) -> IndexRow:
    full_doc = f"{job_title} {doc_text}".strip()
    return IndexRow(
        job_id=job_id,
        project_id=project_id,
        project_title="HealthTech System",
        project_description="Medical booking platform",
        job_title=job_title,
        job_description="Backend development",
        skills=["Java", "Spring Boot", "PostgreSQL"],
        requirements=["2+ years experience"],
        salary_type=salary_type,
        budget_min=Decimal(str(budget_min)),
        budget_max=Decimal(str(budget_max)),
        experience_level="INTERMEDIATE",
        period="MONTHLY",
        hours_per_day=8.0,
        project_status=project_status,
        job_status=job_status,
        doc_text=full_doc,
    )


@pytest.mark.integration
@pytest.mark.asyncio
async def test_init_db_creates_extensions_tables_indexes(pg_session: AsyncSession):
    # Check vector and unaccent extensions
    ext_res = await pg_session.execute(
        text("SELECT extname FROM pg_extension WHERE extname IN ('vector', 'unaccent');")
    )
    ext_names = {r[0] for r in ext_res.fetchall()}
    assert "vector" in ext_names
    assert "unaccent" in ext_names

    # Check job_index table and indexes exist
    idx_res = await pg_session.execute(
        text("SELECT indexname FROM pg_indexes WHERE tablename = 'job_index';")
    )
    idx_names = {r[0] for r in idx_res.fetchall()}
    assert any("hnsw" in n.lower() or "vector" in n.lower() for n in idx_names)
    assert any("gin" in n.lower() or "tsv" in n.lower() for n in idx_names)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_hybrid_search_filters(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    r_hourly = make_test_row(
        job_id="j-h-1", salary_type="HOURLY", budget_min=300000, budget_max=500000, doc_text="Java Hourly Developer"
    )
    r_monthly = make_test_row(
        job_id="j-m-1", salary_type="MONTHLY", budget_min=25000000, budget_max=40000000, doc_text="Java Monthly Engineer"
    )
    rows = [r_hourly, r_monthly]
    vectors = fake_embedder.embed([r.doc_text for r in rows])
    await write_index(pg_session, rows, vectors, embedder=fake_embedder)

    criteria = MatchCriteria(salary_type=SalaryTypeFilter.HOURLY)
    _, hits = await store.hybrid_search(dense_queries=[], lexical="Java", criteria=criteria)
    hit_ids = [h.job_id for h in hits]
    assert "j-h-1" in hit_ids
    assert "j-m-1" not in hit_ids


@pytest.mark.integration
@pytest.mark.asyncio
async def test_filtered_dense_search_returns_full_top(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    rows = [make_test_row(job_id=f"j-dense-{i}", doc_text=f"Java developer specialized tier {i}") for i in range(10)]
    vectors = fake_embedder.embed([r.doc_text for r in rows])
    await write_index(pg_session, rows, vectors, embedder=fake_embedder)

    # Dense search with iterative_scan / ef_search=200 returns full requested top
    query_vec = fake_embedder.embed(["Java developer"])[0]
    dense_lists, _ = await store.hybrid_search(
        dense_queries=[query_vec],
        lexical="",
        criteria=MatchCriteria(),
        top=5,
    )
    assert len(dense_lists) == 1
    assert len(dense_lists[0]) == 5
