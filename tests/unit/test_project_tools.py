import pytest
from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart, ToolReturnPart
from pydantic_ai.models.function import AgentInfo, FunctionModel

from app.agents.deps import AgentDeps
from app.features.chat.agent import chat_agent
from tests.unit.helpers import FakeRpc, scripted_model


@pytest.mark.asyncio
async def test_search_maps_args_to_rpc_payload(mock_user):
    rpc = FakeRpc({"ok": True, "data": {"content": [], "totalElements": 0}})
    deps = AgentDeps(user=mock_user, rpc=rpc)

    model = scripted_model(
        "search_filter_projects",
        {"status": "OPEN", "min_price": 10, "experience_level": "ENTRY"},
    )

    with chat_agent.override(model=model):
        result = await chat_agent.run("Find open entry-level projects", deps=deps)

    assert result.output == "done"
    assert len(rpc.calls) == 1
    routing_key, payload = rpc.calls[0]
    assert routing_key == "core.project.search"
    assert payload == {
        "status": "OPEN",
        "minPrice": 10.0,
        "experienceLevel": "ENTRY",
        "page": 0,
        "size": 20,
        "sort": "createdAt,desc",
    }


@pytest.mark.asyncio
async def test_search_defaults_send_empty_payload(mock_user):
    rpc = FakeRpc({"ok": True, "data": {"content": [], "totalElements": 0}})
    deps = AgentDeps(user=mock_user, rpc=rpc)

    model = scripted_model("search_filter_projects", {})

    with chat_agent.override(model=model):
        result = await chat_agent.run("Browse projects", deps=deps)

    assert result.output == "done"
    assert len(rpc.calls) == 1
    routing_key, payload = rpc.calls[0]
    assert routing_key == "core.project.search"
    assert payload == {
        "page": 0,
        "size": 20,
        "sort": "createdAt,desc",
    }


@pytest.mark.asyncio
async def test_search_min_gt_max_returns_message_without_rpc(mock_user):
    rpc = FakeRpc({"ok": True, "data": {}})
    deps = AgentDeps(user=mock_user, rpc=rpc)

    tool_return_captured = []

    def model_fn(messages, info: AgentInfo):
        last_msg = messages[-1]
        for part in getattr(last_msg, "parts", []):
            if isinstance(part, ToolReturnPart):
                tool_return_captured.append(part.content)
                return ModelResponse(parts=[TextPart("handled")])
        return ModelResponse(
            parts=[
                ToolCallPart(
                    "search_filter_projects",
                    {"min_price": 500, "max_price": 10},
                )
            ]
        )

    with chat_agent.override(model=FunctionModel(model_fn)):
        result = await chat_agent.run("Filter projects", deps=deps)

    assert result.output == "handled"
    assert len(rpc.calls) == 0
    assert len(tool_return_captured) == 1
    assert (
        "Validation error: min_price (500.0) cannot exceed max_price (10.0)."
        in tool_return_captured[0]
    )


@pytest.mark.asyncio
async def test_search_invalid_enum_triggers_retry(mock_user):
    rpc = FakeRpc({"ok": True, "data": {"content": []}})
    deps = AgentDeps(user=mock_user, rpc=rpc)

    seen_retry = False

    def model_fn(messages, info: AgentInfo):
        nonlocal seen_retry
        last_msg = messages[-1]
        for part in getattr(last_msg, "parts", []):
            if isinstance(part, ToolReturnPart):
                if getattr(part, "outcome", None) == "success":
                    return ModelResponse(parts=[TextPart("fixed and done")])
                elif getattr(part, "outcome", None) == "retried":
                    seen_retry = True
                    # Model self-corrects using valid enum
                    return ModelResponse(
                        parts=[ToolCallPart("search_filter_projects", {"status": "OPEN"})]
                    )

        # First turn: invalid enum value
        return ModelResponse(parts=[ToolCallPart("search_filter_projects", {"status": "BOGUS"})])

    with chat_agent.override(model=FunctionModel(model_fn)):
        result = await chat_agent.run("Find projects", deps=deps)

    assert result.output == "fixed and done"
    assert seen_retry is True
    assert len(rpc.calls) == 1
    assert rpc.calls[0][0] == "core.project.search"
    assert rpc.calls[0][1]["status"] == "OPEN"


@pytest.mark.asyncio
async def test_search_rpc_error_is_friendly_string(mock_user):
    rpc = FakeRpc(
        {
            "ok": False,
            "error": {"code": "SERVICE_UNAVAILABLE", "message": "Downstream RPC failed"},
        }
    )
    deps = AgentDeps(user=mock_user, rpc=rpc)

    tool_return_content = None

    def model_fn(messages, info: AgentInfo):
        nonlocal tool_return_content
        last_msg = messages[-1]
        for part in getattr(last_msg, "parts", []):
            if isinstance(part, ToolReturnPart):
                tool_return_content = part.content
                return ModelResponse(parts=[TextPart("received error")])
        return ModelResponse(parts=[ToolCallPart("search_filter_projects", {"keyword": "Python"})])

    with chat_agent.override(model=FunctionModel(model_fn)):
        result = await chat_agent.run("Find python", deps=deps)

    assert result.output == "received error"
    assert tool_return_content is not None
    assert "Downstream RPC failed" in tool_return_content
    assert "SERVICE_UNAVAILABLE" in tool_return_content


@pytest.mark.asyncio
async def test_get_project_valid_uuid(mock_user):
    target_uuid = "123e4567-e89b-12d3-a456-426614174000"
    rpc = FakeRpc({"ok": True, "data": {"id": target_uuid, "title": "Project Alpha"}})
    deps = AgentDeps(user=mock_user, rpc=rpc)

    model = scripted_model("get_project_detail", {"project_id": target_uuid})

    with chat_agent.override(model=model):
        result = await chat_agent.run(f"Get details for {target_uuid}", deps=deps)

    assert result.output == "done"
    assert len(rpc.calls) == 1
    assert rpc.calls[0] == ("core.project.get", {"projectId": target_uuid})


@pytest.mark.asyncio
async def test_get_project_invalid_uuid_no_rpc(mock_user):
    rpc = FakeRpc({"ok": True, "data": {}})
    deps = AgentDeps(user=mock_user, rpc=rpc)

    tool_return = None

    def model_fn(messages, info: AgentInfo):
        nonlocal tool_return
        last_msg = messages[-1]
        for part in getattr(last_msg, "parts", []):
            if isinstance(part, ToolReturnPart):
                tool_return = part.content
                return ModelResponse(parts=[TextPart("handled error")])
        return ModelResponse(
            parts=[ToolCallPart("get_project_detail", {"project_id": "not-a-valid-uuid"})]
        )

    with chat_agent.override(model=FunctionModel(model_fn)):
        result = await chat_agent.run("Get details for invalid id", deps=deps)

    assert result.output == "handled error"
    assert len(rpc.calls) == 0
    assert tool_return is not None
    assert "Validation error" in tool_return
    assert "not-a-valid-uuid" in tool_return


def test_tool_schema_exposes_field_descriptions():
    tools = chat_agent._function_toolset.tools
    assert "search_filter_projects" in tools
    assert "get_project_detail" in tools

    search_tool = tools["search_filter_projects"]
    schema = search_tool.tool_def.parameters_json_schema

    # Top-level properties flattened by Pydantic AI
    props = schema.get("properties", {})
    assert "status" in props
    assert "min_price" in props
    assert "experience_level" in props

    # Verify descriptions are attached for LLM guidance
    assert "minimum starting price" in props["min_price"].get("description", "").lower()

    # Enum defs
    defs = schema.get("$defs", {})
    assert "ProjectStatus" in defs
    assert defs["ProjectStatus"]["enum"] == ["OPEN", "CLOSED"]
    assert "ExperienceLevel" in defs
    assert defs["ExperienceLevel"]["enum"] == ["ENTRY", "INTERMEDIATE", "EXPERT"]
