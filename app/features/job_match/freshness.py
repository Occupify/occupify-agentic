import logging
from typing import Any

logger = logging.getLogger(__name__)


async def check_projects_freshness(
    shortlisted: list[dict[str, Any]],
    rpc: Any,
    limit: int | None = None,
    all_candidates: list[dict[str, Any]] | None = None,
) -> tuple[list[dict[str, Any]], list[str], bool]:
    """S8 Freshness check against core.project.get concurrently.

    CLOSED, non-RECRUITING or PROJECT_NOT_FOUND -> drop and refill from next ranked candidates.
    RPC_TIMEOUT or other RPC failure -> keep items with verified=False,
    warning JOBS_UNVERIFIED, and is_partial=True.
    """
    if not shortlisted and not all_candidates:
        return [], [], False

    target_limit = limit if limit is not None else len(shortlisted)
    candidates = list(all_candidates) if all_candidates else list(shortlisted)
    warnings: list[str] = []
    is_partial: bool = False
    verified_items: list[dict[str, Any]] = []
    checked_pids: set[str] = set()

    for item in candidates:
        pid = item.get("project_id") or item.get("projectId") or item.get("id")
        if not pid or pid in checked_pids:
            continue
        checked_pids.add(pid)

        try:
            reply = await rpc.call("core.project.get", {"projectId": pid})
        except Exception as exc:
            logger.warning("RPC error fetching project %s: %s", pid, type(exc).__name__)
            reply = {"ok": False, "error": {"code": "RPC_ERROR", "message": str(exc)}}

        # Check if RPC succeeded
        if not reply.get("ok"):
            err = reply.get("error") or {}
            err_code = err.get("code")
            if err_code == "PROJECT_NOT_FOUND":
                # Dropped, do not mark as unverified, refill from next candidate
                continue
            else:
                # RPC failure / timeout -> keep item as unverified
                item_copy = dict(item)
                item_copy["verified"] = False
                verified_items.append(item_copy)
                if "JOBS_UNVERIFIED" not in warnings:
                    warnings.append("JOBS_UNVERIFIED")
                is_partial = True
                if len(verified_items) >= target_limit:
                    break
                continue

        # RPC succeeded -> inspect core project data
        data_wrapper = reply.get("data") or {}
        core_proj = data_wrapper
        if "data" in data_wrapper and isinstance(data_wrapper["data"], dict):
            core_proj = data_wrapper["data"]

        # Check project status: must be OPEN
        proj_status = core_proj.get("status")
        if proj_status != "OPEN":
            # Project is CLOSED / PAUSED / etc. -> drop and refill
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
            jid = j.get("job_id") or j.get("id") or j.get("jobId")
            status = core_job_status.get(jid)
            if status == "RECRUITING":
                active_jobs.append(j)

        if active_jobs:
            item_copy = dict(item)
            item_copy["jobs"] = active_jobs
            item_copy["verified"] = True
            verified_items.append(item_copy)
            if len(verified_items) >= target_limit:
                break

    return verified_items, warnings, is_partial
