import asyncio
import logging
from typing import Any

logger = logging.getLogger(__name__)


async def check_projects_freshness(
    shortlisted: list[dict[str, Any]],
    rpc: Any,
) -> tuple[list[dict[str, Any]], list[str], bool]:
    """S8 Freshness check against core.project.get concurrently.

    CLOSED, non-RECRUITING or PROJECT_NOT_FOUND -> drop.
    RPC_TIMEOUT or other RPC failure -> keep items with verified=False,
    warning JOBS_UNVERIFIED, and is_partial=True.
    """
    if not shortlisted:
        return [], [], False

    warnings: list[str] = []
    is_partial: bool = False

    async def _fetch_project(item: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
        project_id = item.get("project_id") or item.get("id")
        try:
            reply = await rpc.call("core.project.get", {"projectId": project_id})
            return item, reply
        except Exception as exc:
            logger.warning("RPC error fetching project %s: %s", project_id, type(exc).__name__)
            return item, {"ok": False, "error": {"code": "RPC_ERROR", "message": str(exc)}}

    tasks = [_fetch_project(item) for item in shortlisted]
    results = await asyncio.gather(*tasks)

    verified_items: list[dict[str, Any]] = []

    for item, reply in results:
        # Check if RPC succeeded
        if not reply.get("ok"):
            err = reply.get("error") or {}
            err_code = err.get("code")
            if err_code == "PROJECT_NOT_FOUND":
                # Dropped, do not mark as unverified
                continue
            else:
                # RPC failure / timeout -> keep item as unverified
                item_copy = dict(item)
                item_copy["verified"] = False
                verified_items.append(item_copy)
                if "JOBS_UNVERIFIED" not in warnings:
                    warnings.append("JOBS_UNVERIFIED")
                is_partial = True
                continue

        # RPC succeeded -> inspect core project data
        data_wrapper = reply.get("data") or {}
        # Core data might be nested inside standard Spring SingleResponse {"data": {"statusCode": 200, "data": {...}}}
        core_proj = data_wrapper
        if "data" in data_wrapper and isinstance(data_wrapper["data"], dict):
            core_proj = data_wrapper["data"]

        # Check project status: must be OPEN
        proj_status = core_proj.get("status")
        if proj_status != "OPEN":
            # Project is CLOSED / PAUSED / etc. -> drop
            continue

        # Filter jobs: must be RECRUITING
        core_jobs = core_proj.get("jobs") or []
        core_job_status = {}
        for cj in core_jobs:
            jid = cj.get("id") or cj.get("job_id")
            if jid:
                core_job_status[jid] = cj.get("status")

        active_jobs = []
        for j in item.get("jobs", []):
            jid = j.get("job_id") or j.get("id")
            status = core_job_status.get(jid)
            # If job exists in core and is RECRUITING, keep it
            if status == "RECRUITING":
                active_jobs.append(j)

        if active_jobs:
            item_copy = dict(item)
            item_copy["jobs"] = active_jobs
            item_copy["verified"] = True
            verified_items.append(item_copy)

    return verified_items, warnings, is_partial
