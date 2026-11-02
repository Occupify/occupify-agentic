import pytest

from app.features.job_match.freshness import check_projects_freshness


@pytest.mark.asyncio
async def test_closed_project_and_filled_job_dropped_and_refilled():
    # p1 is CLOSED, p2 has job j21 RECRUITING and j22 FILLED
    rpc_reply_p1 = {
        "ok": True,
        "data": {
            "statusCode": 200,
            "data": {
                "id": "p1",
                "status": "CLOSED",
                "jobs": [{"id": "j11", "status": "RECRUITING"}],
            },
        },
    }
    rpc_reply_p2 = {
        "ok": True,
        "data": {
            "statusCode": 200,
            "data": {
                "id": "p2",
                "status": "OPEN",
                "jobs": [
                    {"id": "j21", "status": "RECRUITING"},
                    {"id": "j22", "status": "FILLED"},
                ],
            },
        },
    }

    class FreshnessFakeRpc:
        async def call(self, routing_key: str, args: dict):
            pid = args.get("projectId")
            if pid == "p1":
                return rpc_reply_p1
            elif pid == "p2":
                return rpc_reply_p2
            return {"ok": False, "error": {"code": "PROJECT_NOT_FOUND"}}

    shortlisted = [
        {"project_id": "p1", "jobs": [{"job_id": "j11"}]},
        {"project_id": "p2", "jobs": [{"job_id": "j21"}, {"job_id": "j22"}]},
    ]

    verified_items, warnings, is_partial = await check_projects_freshness(
        shortlisted=shortlisted,
        rpc=FreshnessFakeRpc(),
    )

    # p1 must be dropped because project is CLOSED
    # In p2, j22 must be dropped because job is FILLED; j21 kept
    project_ids = [item["project_id"] for item in verified_items]
    assert "p1" not in project_ids
    assert "p2" in project_ids

    p2_jobs = next(item["jobs"] for item in verified_items if item["project_id"] == "p2")
    job_ids = [j["job_id"] for j in p2_jobs]
    assert "j21" in job_ids
    assert "j22" not in job_ids


@pytest.mark.asyncio
async def test_project_not_found_dropped_not_unverified():
    # When core returns PROJECT_NOT_FOUND, item must be dropped, not kept as unverified
    class NotFoundRpc:
        async def call(self, routing_key: str, args: dict):
            return {"ok": False, "error": {"code": "PROJECT_NOT_FOUND", "message": "Not found"}}

    shortlisted = [{"project_id": "p-missing", "jobs": [{"job_id": "j1"}]}]

    verified_items, warnings, is_partial = await check_projects_freshness(
        shortlisted=shortlisted,
        rpc=NotFoundRpc(),
    )

    assert len(verified_items) == 0
    assert "JOBS_UNVERIFIED" not in warnings


@pytest.mark.asyncio
async def test_core_timeout_keeps_items_unverified_partial():
    # When core RPC times out or errors, keep items with verified=False, warning JOBS_UNVERIFIED, partial=True
    class TimeoutRpc:
        async def call(self, routing_key: str, args: dict):
            return {"ok": False, "error": {"code": "RPC_TIMEOUT", "message": "Timeout"}}

    shortlisted = [{"project_id": "p-timeout", "jobs": [{"job_id": "j1"}]}]

    verified_items, warnings, is_partial = await check_projects_freshness(
        shortlisted=shortlisted,
        rpc=TimeoutRpc(),
    )

    assert len(verified_items) == 1
    assert verified_items[0]["verified"] is False
    assert "JOBS_UNVERIFIED" in warnings
    assert is_partial is True


@pytest.mark.asyncio
async def test_freshness_drops_closed_and_refills_from_candidates():
    class RefillRpc:
        async def call(self, routing_key: str, args: dict):
            pid = args.get("projectId")
            if pid == "p1":
                return {
                    "ok": True,
                    "data": {"status": "CLOSED", "jobs": [{"id": "j1", "status": "RECRUITING"}]},
                }
            elif pid in ("p2", "p3"):
                return {
                    "ok": True,
                    "data": {
                        "status": "OPEN",
                        "jobs": [{"id": f"{pid}-j1", "status": "RECRUITING"}],
                    },
                }
            return {"ok": False, "error": {"code": "PROJECT_NOT_FOUND"}}

    shortlisted = [
        {"project_id": "p1", "jobs": [{"job_id": "j1"}]},
        {"project_id": "p2", "jobs": [{"job_id": "p2-j1"}]},
    ]
    all_candidates = [
        {"project_id": "p1", "jobs": [{"job_id": "j1"}]},
        {"project_id": "p2", "jobs": [{"job_id": "p2-j1"}]},
        {"project_id": "p3", "jobs": [{"job_id": "p3-j1"}]},
    ]

    verified_items, warnings, is_partial = await check_projects_freshness(
        shortlisted=shortlisted,
        rpc=RefillRpc(),
        limit=2,
        all_candidates=all_candidates,
    )

    assert len(verified_items) == 2
    pids = [item["project_id"] for item in verified_items]
    assert pids == ["p2", "p3"]
