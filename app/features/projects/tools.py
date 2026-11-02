import uuid
from typing import Any

from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.features.projects.schemas import ProjectFilterParams, ProjectGetParams
from app.messaging.core_client import get_core_rpc


def strip_employer_recursive(obj: Any) -> Any:
    """Recursively removes any 'employer' key from dicts and lists."""
    if isinstance(obj, dict):
        return {k: strip_employer_recursive(v) for k, v in obj.items() if k != "employer"}
    elif isinstance(obj, list):
        return [strip_employer_recursive(item) for item in obj]
    return obj


async def search_filter_projects(
    ctx: RunContext[AgentDeps],
    params: ProjectFilterParams,
) -> dict[str, Any] | str:
    """
    Search and filter projects on Occupify. Returns a paginated list of projects with their complete details and roles (jobs and skills).
    By default (without filters), returns the first page of projects (up to `size`, default 20) with their complete details and roles, along with paging metadata.
    Each item in the list has the same structure as `get_project_detail` (including jobs, required skills, and employer).
    """
    if (
        params.min_price is not None
        and params.max_price is not None
        and params.min_price > params.max_price
    ):
        return f"Validation error: min_price ({params.min_price}) cannot exceed max_price ({params.max_price})."

    payload = {
        "keyword": params.keyword,
        "skills": params.skills,
        "status": params.status.value if params.status else None,
        "employerId": params.employer_id,
        "period": params.period.value if params.period else None,
        "experienceLevel": params.experience_level.value if params.experience_level else None,
        "minPrice": params.min_price,
        "maxPrice": params.max_price,
        "page": params.page,
        "size": params.size,
        "sort": params.sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    rpc = getattr(ctx.deps, "rpc", None) or get_core_rpc()
    response = await rpc.call("core.project.search", payload)

    if not response.get("ok"):
        err = response.get("error", {})
        return f"Failed to search projects: {err.get('message', 'Service error')} (code: {err.get('code', 'RPC_ERROR')})"

    return strip_employer_recursive(response.get("data", {}))


async def get_project_detail(
    ctx: RunContext[AgentDeps],
    params: ProjectGetParams,
) -> dict[str, Any] | str:
    """
    Retrieve full details for a specific project by UUID, including jobs, required skills, and employer profile.
    """
    clean_id = (params.project_id or "").strip()
    if not clean_id:
        return "Validation error: project_id is required."

    try:
        uuid.UUID(clean_id)
    except ValueError:
        return f"Validation error: '{params.project_id}' is not a valid UUID format (expected standard UUID string e.g. '123e4567-e89b-12d3-a456-426614174000')."

    rpc = getattr(ctx.deps, "rpc", None) or get_core_rpc()
    response = await rpc.call("core.project.get", {"projectId": clean_id})

    if not response.get("ok"):
        err = response.get("error", {})
        return f"Could not retrieve project details for ID '{clean_id}': {err.get('message', 'Project not found')} (code: {err.get('code', 'RPC_ERROR')})"

    return strip_employer_recursive(response.get("data", {}))
