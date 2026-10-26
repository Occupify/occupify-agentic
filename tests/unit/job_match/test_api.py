import asyncio
import io

import pytest
from httpx import AsyncClient
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import CurrentUser
from app.db.models import JobMatchRun
from app.features.job_match.ports import RunResult, RunState


def make_dummy_pdf() -> bytes:
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)
    styles = getSampleStyleSheet()
    doc.build([Paragraph("Nguyễn Văn Testcase\n# KỸ NĂNG\nJava, Spring Boot", styles["Normal"])])
    return buf.getvalue()


@pytest.fixture
def dummy_pdf() -> bytes:
    return make_dummy_pdf()


@pytest.mark.asyncio
async def test_post_valid_pdf_returns_202_and_queued_run(
    client: AsyncClient, dummy_pdf: bytes, monkeypatch
):
    async def fake_run(*args, **kwargs):
        return RunResult(status="succeeded", outcome="OK")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", fake_run)

    files = {"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    data = {"salaryType": "MONTHLY", "limit": 10}

    res = await client.post("/ai/job-matches", files=files, data=data)
    assert res.status_code == 202
    body = res.json()
    assert body["statusCode"] == 202
    assert body["data"]["status"] == "queued"
    assert "runId" in body["data"]


@pytest.mark.asyncio
async def test_post_invalid_pdf_400_no_run(client: AsyncClient, test_db: AsyncSession):
    files = {"file": ("invalid.txt", b"plain text not pdf", "text/plain")}
    res = await client.post("/ai/job-matches", files=files)
    assert res.status_code == 400
    body = res.json()
    assert body["error"]["code"] == "FILE_INVALID"

    # Verify no run created in DB
    runs = (await test_db.execute(select(JobMatchRun))).scalars().all()
    assert len(runs) == 0


@pytest.mark.asyncio
async def test_post_bad_criteria_422_no_run(
    client: AsyncClient, dummy_pdf: bytes, test_db: AsyncSession
):
    # min_budget > max_budget
    files = {"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    data = {"minBudget": 50000000, "maxBudget": 20000000}

    res = await client.post("/ai/job-matches", files=files, data=data)
    assert res.status_code == 422
    body = res.json()
    assert body["error"]["code"] == "VALIDATION_ERROR"

    runs = (await test_db.execute(select(JobMatchRun))).scalars().all()
    assert len(runs) == 0


@pytest.mark.asyncio
async def test_second_active_run_409_busy(client: AsyncClient, dummy_pdf: bytes, monkeypatch):
    run_started = asyncio.Event()
    finish_run = asyncio.Event()

    async def slow_pipeline_run(*args, **kwargs):
        run_started.set()
        await finish_run.wait()
        return RunResult(status="succeeded", outcome="OK")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", slow_pipeline_run)

    files1 = {"file": ("cv1.pdf", dummy_pdf, "application/pdf")}
    task1 = asyncio.create_task(client.post("/ai/job-matches", files=files1))
    await run_started.wait()

    # Second active run while first is running
    files2 = {"file": ("cv2.pdf", dummy_pdf, "application/pdf")}
    res2 = await client.post("/ai/job-matches", files=files2)
    assert res2.status_code == 409
    body2 = res2.json()
    assert body2["error"]["code"] == "JOB_MATCH_BUSY"
    assert body2["error"]["message"].startswith("Failed to")

    finish_run.set()
    res1 = await task1
    assert res1.status_code == 202


@pytest.mark.asyncio
async def test_concurrent_posts_create_one_run(client: AsyncClient, dummy_pdf: bytes, monkeypatch):
    async def slow_pipeline_run(*args, **kwargs):
        await asyncio.sleep(0.1)
        return RunResult(status="succeeded", outcome="OK")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", slow_pipeline_run)

    files = {"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    res1, res2 = await asyncio.gather(
        client.post("/ai/job-matches", files=files),
        client.post("/ai/job-matches", files=files),
        return_exceptions=True,
    )

    statuses = {res1.status_code, res2.status_code}
    assert statuses == {202, 409}


@pytest.mark.asyncio
async def test_get_run_owner_only_404_for_other_user(
    client: AsyncClient, test_db: AsyncSession, mock_user: CurrentUser
):
    # Insert finished run for mock_user
    run = JobMatchRun(
        id="run-u1",
        user_id=mock_user.user_id,
        status="succeeded",
        stage="done",
        outcome="OK",
    )
    test_db.add(run)
    await test_db.commit()

    # Owner can read
    res_owner = await client.get("/ai/job-matches/run-u1")
    assert res_owner.status_code == 200
    assert res_owner.json()["data"]["runId"] == "run-u1"

    # Other user gets 404 JOB_MATCH_NOT_FOUND
    other_headers = {"X-User-Id": "other-user-uuid-999"}
    res_other = await client.get("/ai/job-matches/run-u1", headers=other_headers)
    assert res_other.status_code == 404
    assert res_other.json()["error"]["code"] == "JOB_MATCH_NOT_FOUND"


@pytest.mark.asyncio
async def test_list_runs_only_own_paged(
    client: AsyncClient, test_db: AsyncSession, mock_user: CurrentUser
):
    # Insert 2 runs for mock_user and 1 for other
    r1 = JobMatchRun(id="run-1", user_id=mock_user.user_id, status="succeeded", stage="done")
    r2 = JobMatchRun(id="run-2", user_id=mock_user.user_id, status="succeeded", stage="done")
    r3 = JobMatchRun(id="run-3", user_id="other-user", status="succeeded", stage="done")
    test_db.add_all([r1, r2, r3])
    await test_db.commit()

    res = await client.get("/ai/job-matches?page=1&limit=10")
    assert res.status_code == 200
    body = res.json()["data"]
    run_ids = [item["runId"] for item in body["data"]]
    assert "run-1" in run_ids
    assert "run-2" in run_ids
    assert "run-3" not in run_ids


@pytest.mark.asyncio
async def test_pipeline_crash_marks_run_failed_and_releases_busy(
    client: AsyncClient, dummy_pdf: bytes, test_db: AsyncSession, monkeypatch
):
    async def crashing_run(*args, **kwargs):
        raise RuntimeError("Unexpected pipeline crash")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", crashing_run)

    files = {"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    res = await client.post("/ai/job-matches", files=files)
    assert res.status_code == 202
    run_id = res.json()["data"]["runId"]

    # Wait briefly for execute_run task to finish and catch-all to persist failed
    await asyncio.sleep(0.1)

    run_in_db = await test_db.get(JobMatchRun, run_id)
    assert run_in_db is not None
    assert run_in_db.status == "failed"
    assert run_in_db.error_code == "INTERNAL_ERROR"
    assert run_in_db.message.startswith("Failed to")

    # Releases busy: next POST gets 202
    async def ok_run(*args, **kwargs):
        return RunResult(status="succeeded", outcome="OK")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", ok_run)
    res2 = await client.post(
        "/ai/job-matches", files={"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    )
    assert res2.status_code == 202


@pytest.mark.asyncio
async def test_timeout_persists_partial_or_failed(
    client: AsyncClient, dummy_pdf: bytes, test_db: AsyncSession, monkeypatch
):
    monkeypatch.setenv("JOB_MATCH_RUN_TIMEOUT_S", "0.05")

    async def timing_out_run(state: RunState, *args, **kwargs):
        # Fill state with partial ranking
        state.stage = "ranking"
        state.ranking = [{"rank": 1, "project_id": "p01", "match_score": 85}]
        await asyncio.sleep(0.2)
        return RunResult(status="succeeded", outcome="OK")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", timing_out_run)

    res = await client.post(
        "/ai/job-matches", files={"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    )
    assert res.status_code == 202
    run_id = res.json()["data"]["runId"]

    await asyncio.sleep(0.15)
    run_in_db = await test_db.get(JobMatchRun, run_id)
    assert run_in_db is not None
    assert run_in_db.status in ("partial", "failed")
    if run_in_db.status == "failed":
        assert run_in_db.error_code == "RUN_TIMEOUT"


@pytest.mark.asyncio
async def test_raw_pdf_never_persisted(
    client: AsyncClient, dummy_pdf: bytes, test_db: AsyncSession, monkeypatch
):
    async def ok_run(*args, **kwargs):
        return RunResult(status="succeeded", outcome="OK")

    monkeypatch.setattr("app.features.job_match.service.pipeline.run", ok_run)

    res = await client.post(
        "/ai/job-matches", files={"file": ("cv.pdf", dummy_pdf, "application/pdf")}
    )
    run_id = res.json()["data"]["runId"]
    await asyncio.sleep(0.05)

    run_in_db = await test_db.get(JobMatchRun, run_id)
    assert run_in_db is not None
    # Ensure PDF bytes never appear in any DB column
    for col in run_in_db.__table__.columns:
        val = getattr(run_in_db, col.name)
        assert not isinstance(val, (bytes, bytearray))
        if isinstance(val, str):
            assert "PDF-" not in val
