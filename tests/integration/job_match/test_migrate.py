from decimal import Decimal
from typing import Any

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import IndexMetaModel, JobIndexRow
from app.features.job_match.index import build, index_state, write_index
from app.features.job_match.ports import IndexRow
from app.main import create_app
from app.ml.fakes import FakeEmbedder


@pytest.fixture
def fake_embedder():
    return FakeEmbedder(dim=1024)


def make_test_row(
    job_id: str,
    project_id: str = "p-1",
    job_title: str = "Backend Developer",
    doc_text: str = "Python FastAPI",
) -> IndexRow:
    full_doc = f"{job_title} {doc_text}".strip()
    return IndexRow(
        job_id=job_id,
        project_id=project_id,
        project_title="Project 1",
        project_description="Desc 1",
        job_title=job_title,
        job_description="Job Desc",
        skills=["Python", "FastAPI"],
        requirements=["Requirement 1"],
        salary_type="MONTHLY",
        budget_min=Decimal("20000000"),
        budget_max=Decimal("30000000"),
        experience_level="ENTRY",
        period="MONTHLY",
        hours_per_day=8.0,
        project_status="OPEN",
        job_status="RECRUITING",
        doc_text=full_doc,
    )


class FailingCoreRpc:
    async def call(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        return {"ok": False, "error": "RPC_UNAVAILABLE"}


class EmptyCoreRpc:
    async def call(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        return {"ok": True, "data": {"data": [], "paging": {"totalPages": 0}}}


@pytest.mark.integration
@pytest.mark.asyncio
async def test_write_index_replaces_all_in_one_tx(pg_session: AsyncSession, fake_embedder):
    rows1 = [make_test_row(f"j-init-{i}", doc_text=f"Initial python job {i}") for i in range(5)]
    vecs1 = fake_embedder.embed([r.doc_text for r in rows1])
    n1 = await write_index(pg_session, rows1, vecs1, embedder=fake_embedder)
    assert n1 == 5

    res1 = await pg_session.execute(select(func.count(JobIndexRow.job_id)))
    assert res1.scalar() == 5

    # Replace with 3 completely new rows in one transaction
    rows2 = [make_test_row(f"j-next-{i}", doc_text=f"Next rust job {i}") for i in range(3)]
    vecs2 = fake_embedder.embed([r.doc_text for r in rows2])
    n2 = await write_index(pg_session, rows2, vecs2, embedder=fake_embedder)
    assert n2 == 3

    res2 = await pg_session.execute(select(func.count(JobIndexRow.job_id)))
    assert res2.scalar() == 3

    all_jids = (await pg_session.execute(select(JobIndexRow.job_id))).scalars().all()
    assert sorted(all_jids) == [f"j-next-{i}" for i in range(3)]


@pytest.mark.integration
@pytest.mark.asyncio
async def test_source_failure_writes_nothing(pg_session: AsyncSession, fake_embedder):
    with pytest.raises(RuntimeError, match="Failed to read from core_rpc"):
        await build(core_rpc=FailingCoreRpc(), embedder=fake_embedder, session=pg_session)

    res = await pg_session.execute(select(func.count(JobIndexRow.job_id)))
    assert res.scalar() == 0


@pytest.mark.integration
@pytest.mark.asyncio
async def test_empty_source_refused(pg_session: AsyncSession, fake_embedder):
    # build() on empty RPC raises RuntimeError
    with pytest.raises(RuntimeError, match="Refusing to write index"):
        await build(core_rpc=EmptyCoreRpc(), embedder=fake_embedder, session=pg_session)

    # Direct write_index with empty rows raises ValueError
    with pytest.raises(ValueError, match="Refusing to write empty index"):
        await write_index(pg_session, [], [], embedder=fake_embedder)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_self_retrieval_check_rolls_back_bad_vectors(pg_session: AsyncSession, fake_embedder):
    rows = [make_test_row(f"j-chk-{i}", doc_text=f"Unique specialized skill {i}") for i in range(5)]
    # Intentionally shuffle/corrupt vectors so dense self-retrieval does not match rank 1
    # We pass the vector of job 4 to job 0, etc.
    correct_vecs = fake_embedder.embed([r.doc_text for r in rows])
    bad_vecs = list(reversed(correct_vecs))

    with pytest.raises(RuntimeError, match="Self-retrieval check failed"):
        await write_index(pg_session, rows, bad_vecs, embedder=fake_embedder)

    await pg_session.rollback()
    res = await pg_session.execute(select(func.count(JobIndexRow.job_id)))
    assert res.scalar() == 0


@pytest.mark.integration
@pytest.mark.asyncio
async def test_meta_mismatch_is_not_usable(pg_session: AsyncSession, fake_embedder):
    rows = [make_test_row(f"j-meta-{i}", doc_text=f"Meta check job {i}") for i in range(3)]
    vecs = fake_embedder.embed([r.doc_text for r in rows])
    await write_index(pg_session, rows, vecs, embedder=fake_embedder)

    # Status is ok
    state = await index_state(session=pg_session)
    assert state == "ok"

    # Mutate source in metadata to simulate mismatch
    meta_row = (await pg_session.execute(select(IndexMetaModel).where(IndexMetaModel.id == 1))).scalar_one()
    meta_row.source = "mismatched:fake_source"
    await pg_session.commit()

    mismatch_state = await index_state(session=pg_session)
    assert mismatch_state == "mismatch"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_ready_200_when_index_missing():
    from app.messaging import broker as broker_mod
    broker_mod._broker_connected = True

    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/ready")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "UP"
        assert "index" in data["checks"]
        assert "models_loaded" in data["checks"]
        assert data["checks"]["index"] in ("ok", "missing", "mismatch")
