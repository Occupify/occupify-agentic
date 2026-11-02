from datetime import UTC, datetime
from decimal import Decimal

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import IndexMetaModel, JobIndexRow
from app.features.job_match.index.store import PgJobIndex, get_expected_index_source, index_state
from app.features.job_match.ports import IndexRow, MatchCriteria
from app.features.job_match.sanitize import DOC_TEXT_VERSION
from app.features.job_match.schemas import SalaryTypeFilter


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
async def test_index_state_missing_when_no_meta(test_db: AsyncSession):
    state = await index_state(session=test_db)
    assert state == "missing"


@pytest.mark.asyncio
async def test_index_state_ok_when_meta_matches(test_db: AsyncSession):
    source = get_expected_index_source()
    meta = IndexMetaModel(
        id=1,
        embed_model="BAAI/bge-m3",
        dim=1024,
        source=source,
        doc_text_version=DOC_TEXT_VERSION,
        built_at=datetime.now(UTC),
        jobs_n=10,
    )
    test_db.add(meta)
    await test_db.commit()

    state = await index_state(session=test_db)
    assert state == "ok"


@pytest.mark.asyncio
async def test_index_state_mismatch_when_model_or_source_differs(test_db: AsyncSession):
    meta = IndexMetaModel(
        id=1,
        embed_model="old-model",
        dim=512,
        source="wrong_source",
        doc_text_version="v0",
        built_at=datetime.now(UTC),
        jobs_n=5,
    )
    test_db.add(meta)
    await test_db.commit()

    state = await index_state(session=test_db)
    assert state == "mismatch"


def test_filter_clauses():
    store = PgJobIndex(session=None)
    criteria = MatchCriteria(salary_type=SalaryTypeFilter.HOURLY, min_budget=100000)
    clauses = store._build_filter_clauses(criteria)
    assert len(clauses) >= 4


@pytest.mark.asyncio
async def test_get_rows(test_db: AsyncSession):
    store = PgJobIndex(session=test_db)
    db_row = JobIndexRow(
        job_id="j-unit-1",
        project_id="p-unit-1",
        project_title="Title",
        project_description="Desc",
        job_title="Job",
        job_description="Desc",
        skills=["Python"],
        requirements=["Req"],
        salary_type="MONTHLY",
        budget_min=Decimal("1000"),
        budget_max=Decimal("2000"),
        experience_level="ENTRY",
        period="MONTHLY",
        hours_per_day=8.0,
        project_status="OPEN",
        job_status="RECRUITING",
        doc_text="Python",
        embedding=[0.1] * 1024,
    )
    test_db.add(db_row)
    await test_db.commit()

    rows = await store.get_rows(["j-unit-1"])
    assert len(rows) == 1
    assert rows[0].job_id == "j-unit-1"
    assert rows[0].job_title == "Job"
