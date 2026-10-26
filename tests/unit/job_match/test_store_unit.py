from decimal import Decimal

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.job_match.index.store import PgJobIndex
from app.features.job_match.index.sync import sweep_job_index
from app.features.job_match.ports import IndexRow, MatchCriteria
from app.features.job_match.schemas import SalaryTypeFilter
from app.ml.fakes import FakeEmbedder


def make_test_row(
    job_id: str = "j-unit-1",
    project_id: str = "p-unit-1",
    job_title: str = "Python Backend Developer",
    doc_text: str = "Python FastAPI PostgreSQL",
    salary_type: str = "MONTHLY",
) -> IndexRow:
    return IndexRow(
        job_id=job_id,
        project_id=project_id,
        project_title="Cloud Platform",
        project_description="Enterprise cloud",
        job_title=job_title,
        job_description="Backend development",
        skills=["Python", "FastAPI"],
        requirements=["1+ years experience"],
        salary_type=salary_type,
        budget_min=Decimal("15000000"),
        budget_max=Decimal("25000000"),
        experience_level="ENTRY",
        period="MONTHLY",
        hours_per_day=8.0,
        project_status="OPEN",
        job_status="RECRUITING",
        doc_text=doc_text,
    )


@pytest.mark.asyncio
async def test_store_upsert_and_get_rows_sqlite(test_db: AsyncSession):
    store = PgJobIndex(session=test_db, embedder=FakeEmbedder(dim=1024))
    assert store.is_usable() is True

    row = make_test_row()
    stats = await store.upsert([row])
    assert stats.inserted == 1
    assert stats.reembed_queued == 1

    rows = await store.get_rows(["j-unit-1"])
    assert len(rows) == 1
    assert rows[0].job_id == "j-unit-1"
    assert rows[0].active is True

    # Sweep job index: seen_job_ids has j-unit-1 -> missed_sweeps remains 0
    await sweep_job_index(test_db, seen_job_ids=["j-unit-1"])
    rows_after = await store.get_rows(["j-unit-1"])
    assert rows_after[0].missed_sweeps == 0

    # Sweep with missing job -> missed_sweeps = 1
    await sweep_job_index(test_db, seen_job_ids=[])
    rows_after_miss1 = await store.get_rows(["j-unit-1"])
    assert rows_after_miss1[0].missed_sweeps == 1
    assert rows_after_miss1[0].active is True

    # Sweep with missing job again -> missed_sweeps = 2, active becomes False
    await sweep_job_index(test_db, seen_job_ids=[])
    rows_after_miss2 = await store.get_rows(["j-unit-1"])
    assert rows_after_miss2[0].missed_sweeps == 2
    assert rows_after_miss2[0].active is False


@pytest.mark.asyncio
async def test_store_mark_inactive_and_meta(test_db: AsyncSession):
    store = PgJobIndex(session=test_db, embedder=FakeEmbedder(dim=1024))
    row = make_test_row(job_id="j-inact-1")
    await store.upsert([row])

    await store.mark_inactive(["j-inact-1"])
    rows = await store.get_rows(["j-inact-1"])
    assert rows[0].active is False

    meta = await store.meta()
    assert meta.jobs_n >= 1


def test_filter_clauses():
    store = PgJobIndex(session=None)
    criteria = MatchCriteria(salary_type=SalaryTypeFilter.HOURLY, min_budget=100000)
    clauses = store._build_filter_clauses(criteria)
    assert len(clauses) >= 4
