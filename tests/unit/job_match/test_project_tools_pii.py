import pytest
from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.features.projects.schemas import ProjectFilterParams, ProjectGetParams
from app.features.projects.tools import get_project_detail, search_filter_projects
from tests.unit.helpers import FakeRpc


@pytest.mark.asyncio
async def test_employer_stripped_recursively_mock_and_rabbit(mock_user):
    # Simulated core response with employer objects deeply nested
    raw_project = {
        "id": "a1000000-0000-0000-0000-000000000001",
        "title": "Project Title",
        "employer": {"id": "emp-1", "name": "Secret Corp", "email": "ceo@secret.com"},
        "jobs": [
            {
                "id": "job-1",
                "title": "Job Title",
                "employer": {"id": "emp-1", "name": "Secret Corp"},
            }
        ],
    }

    # 1. Test search with real nesting {data: {statusCode: 200, data: [raw_project]}}
    search_reply = {
        "ok": True,
        "data": {
            "statusCode": 200,
            "message": "OK",
            "data": [dict(raw_project)],
            "paging": {"page": 0, "limit": 20, "total": 1, "totalPages": 1},
        },
    }
    rpc_search = FakeRpc(search_reply)
    deps_search = AgentDeps(user=mock_user, rpc=rpc_search)
    ctx_search = RunContext(deps=deps_search, model=None, usage=None, prompt=None)

    search_result = await search_filter_projects(ctx_search, ProjectFilterParams())
    assert isinstance(search_result, dict)
    projects_list = search_result.get("data", [])
    assert len(projects_list) == 1
    p = projects_list[0]
    assert "employer" not in p
    assert "employer" not in p["jobs"][0]

    # 2. Test get with real nesting {data: {statusCode: 200, data: raw_project}}
    get_reply = {
        "ok": True,
        "data": {
            "statusCode": 200,
            "message": "OK",
            "data": dict(raw_project),
        },
    }
    rpc_get = FakeRpc(get_reply)
    deps_get = AgentDeps(user=mock_user, rpc=rpc_get)
    ctx_get = RunContext(deps=deps_get, model=None, usage=None, prompt=None)

    get_result = await get_project_detail(
        ctx_get,
        ProjectGetParams(project_id="a1000000-0000-0000-0000-000000000001"),
    )
    assert isinstance(get_result, dict)
    proj_data = get_result.get("data", {})
    assert "employer" not in proj_data
    assert "employer" not in proj_data["jobs"][0]
