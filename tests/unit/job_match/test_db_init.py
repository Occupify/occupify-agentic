import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.init import init_db
from app.db.models import JobMatchRun


@pytest.mark.asyncio
async def test_restart_marks_open_runs_failed(test_db: AsyncSession):
    # Insert two open runs: one queued, one running
    run_queued = JobMatchRun(
        id="run-queued-1",
        user_id="user-1",
        status="queued",
        stage="init",
    )
    run_running = JobMatchRun(
        id="run-running-2",
        user_id="user-2",
        status="running",
        stage="matching",
    )
    run_succeeded = JobMatchRun(
        id="run-done-3",
        user_id="user-3",
        status="succeeded",
        stage="done",
    )
    test_db.add_all([run_queued, run_running, run_succeeded])
    await test_db.commit()

    # Call init_db() which simulates service restart
    await init_db()

    # Query back
    test_db.expire_all()
    res = await test_db.execute(select(JobMatchRun).order_by(JobMatchRun.id))
    runs = {r.id: r for r in res.scalars().all()}

    assert runs["run-queued-1"].status == "failed"
    assert runs["run-queued-1"].error_code == "SERVICE_RESTARTED"
    assert runs["run-queued-1"].message.startswith("Failed to")

    assert runs["run-running-2"].status == "failed"
    assert runs["run-running-2"].error_code == "SERVICE_RESTARTED"
    assert runs["run-running-2"].message.startswith("Failed to")

    # Succeeded run must not be touched
    assert runs["run-done-3"].status == "succeeded"
