from typing import Any

from pydantic import BaseModel
from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart, ToolReturnPart
from pydantic_ai.models.function import AgentInfo, FunctionModel


def structured(instance: BaseModel | dict[str, Any]) -> FunctionModel:
    """Returns a FunctionModel that emits a ToolCallPart for the agent's output tool."""
    dump = instance.model_dump(mode="json") if isinstance(instance, BaseModel) else instance

    def fn(messages: list[Any], info: AgentInfo) -> ModelResponse:
        tool_name = info.output_tools[0].name if info.output_tools else "final_result"
        return ModelResponse(parts=[ToolCallPart(tool_name, dump)])

    return FunctionModel(fn)


def tool_then_structured(
    tool_name: str,
    tool_args: dict[str, Any],
    instance: BaseModel | dict[str, Any],
) -> FunctionModel:
    """Simulates an LLM calling a tool first, then returning structured output once the tool returns."""
    dump = instance.model_dump(mode="json") if isinstance(instance, BaseModel) else instance

    def fn(messages: list[Any], info: AgentInfo) -> ModelResponse:
        has_tool_return = False
        for msg in messages:
            for part in getattr(msg, "parts", []):
                if isinstance(part, ToolReturnPart) and getattr(part, "tool_name", "") == tool_name:
                    has_tool_return = True
                    break
            if has_tool_return:
                break

        if has_tool_return:
            output_tool_name = info.output_tools[0].name if info.output_tools else "final_result"
            return ModelResponse(parts=[ToolCallPart(output_tool_name, dump)])

        return ModelResponse(parts=[ToolCallPart(tool_name, tool_args)])

    return FunctionModel(fn)


def raw_invalid(invalid_payload: dict[str, Any] | str) -> FunctionModel:
    """Returns a model that emits an invalid output tool call or text, for testing schema and validation retries."""

    def fn(messages: list[Any], info: AgentInfo) -> ModelResponse:
        if isinstance(invalid_payload, str):
            return ModelResponse(parts=[TextPart(invalid_payload)])
        tool_name = info.output_tools[0].name if info.output_tools else "final_result"
        return ModelResponse(parts=[ToolCallPart(tool_name, invalid_payload)])

    return FunctionModel(fn)
