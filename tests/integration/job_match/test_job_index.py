from decimal import Decimal
import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.db.models import JobMatchRun
from app.features.job_match.index.store import PgJobIndex
from app.features.job_match.index.sync import sweep_job_index
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
    doc_text: str = "Java Spring Boot PostgreSQL",
    salary_type: str = "MONTHLY",
    budget_min: float = 20000000,
    budget_max: float = 35000000,
    project_status: str = "OPEN",
    job_status: str = "RECRUITING",
) -> IndexRow:
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
        doc_text=doc_text,
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
async def test_partial_unique_active_run(pg_session: AsyncSession):
    # Partial unique index allows at most one active run (status IN (queued, running)) per user_id
    r1 = JobMatchRun(id="run-act-1", user_id="user-unique", status="queued", stage="init")
    pg_session.add(r1)
    await pg_session.commit()

    # Second active run for same user must raise IntegrityError
    r2 = JobMatchRun(id="run-act-2", user_id="user-unique", status="running", stage="matching")
    pg_session.add(r2)
    with pytest.raises(IntegrityError):
        await pg_session.commit()

    await pg_session.rollback()

    # Completed runs do not violate the index
    r3 = JobMatchRun(id="run-done-1", user_id="user-unique", status="succeeded", stage="done")
    pg_session.add(r3)
    await pg_session.commit()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_new_project_findable_by_fulltext_before_embedding(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    row = make_test_row(job_id="j-ft-1", doc_text="Kubernetes cluster DevOps engineer")
    stats = await store.upsert([row])
    assert stats.inserted == 1

    # Before embedding has run (embedding is NULL), lexical search finds it immediately
    dense_lists, lex_hits = await store.hybrid_search(
        dense_queries=[],
        lexical="Kubernetes",
        criteria=MatchCriteria(),
    )
    assert len(lex_hits) >= 1
    assert any(h.job_id == "j-ft-1" for h in lex_hits)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_status_change_no_reembed(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    row = make_test_row(job_id="j-st-1", doc_text="Text content stays identical")
    await store.upsert([row])

    # Embed it
    await store.embed_backlog_batch(batch_size=10)

    # Now update only status
    row_updated = make_test_row(job_id="j-st-1", doc_text="Text content stays identical", job_status="FILLED")
    stats2 = await store.upsert([row_updated])
    assert stats2.updated == 1
    assert stats2.reembed_queued == 0  # No re-embed needed for metadata/status only change


@pytest.mark.integration
@pytest.mark.asyncio
async def test_deactivate_after_two_missed_sweeps(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    row = make_test_row(job_id="j-sw-1")
    await store.upsert([row])

    # Sweep 1: missing from sweep -> missed_sweeps becomes 1, active is still True
    await sweep_job_index(session=pg_session, seen_job_ids=[])
    db_row1 = await store.get_rows(["j-sw-1"])
    assert len(db_row1) == 1
    assert db_row1[0].active is True

    # Sweep 2: missing again -> missed_sweeps becomes 2 -> deactivated (active becomes False)
    await sweep_job_index(session=pg_session, seen_job_ids=[])
    db_row2 = await store.get_rows(["j-sw-1"])
    assert len(db_row2) == 1
    assert db_row2[0].active is False


@pytest.mark.integration
@pytest.mark.asyncio
async def test_hybrid_search_filters(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    r_hourly = make_test_row(job_id="j-h-1", salary_type="HOURLY", budget_min=300000, budget_max=500000)
    r_monthly = make_test_row(job_id="j-m-1", salary_type="MONTHLY", budget_min=25000000, budget_max=40000000)
    await store.upsert([r_hourly, r_monthly])

    criteria = MatchCriteria(salary_type=SalaryTypeFilter.HOURLY)
    _, hits = await store.hybrid_search(dense_queries=[], lexical="Java", criteria=criteria)
    hit_ids = [h.job_id for h in hits]
    assert "j-h-1" in hit_ids
    assert "j-m-1" not in hit_ids


@pytest.mark.integration
@pytest.mark.asyncio
async def test_filtered_dense_search_returns_full_top(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    # Insert rows and embed them
    rows = [make_test_row(job_id=f"j-dense-{i}") for i in range(10)]
    await store.upsert(rows)
    await store.embed_backlog_batch(batch_size=20)

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


@pytest.mark.integration
@pytest.mark.asyncio
async def test_model_mismatch_rebuilds_index(pg_session: AsyncSession, fake_embedder):
    store = PgJobIndex(session=pg_session, embedder=fake_embedder)
    await store.upsert([make_test_row(job_id="j-mismatch-1")])

    # Simulate model mismatch detected on startup
    await store.handle_model_mismatch(new_model="BAAI/bge-m3", new_dim=1024)
    meta = await store.meta()
    assert meta.embed_model == "BAAI/bge-m3"
    assert meta.dim == 1024
