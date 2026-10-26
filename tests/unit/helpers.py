from typing import Any

from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart, ToolReturnPart
from pydantic_ai.models.function import AgentInfo, FunctionModel


class FakeRpc:
    """Mock RpcClient that records calls and returns a configured reply."""

    def __init__(self, reply: dict[str, Any] | None = None):
        self.reply = reply if reply is not None else {"ok": True, "data": {}}
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def call(self, routing_key: str, args: dict[str, Any]) -> dict[str, Any]:
        self.calls.append((routing_key, args))
        return self.reply


def scripted_model(tool_name: str, args: dict[str, Any], final_text: str = "done") -> FunctionModel:
    """
    Creates a FunctionModel that simulates an LLM making a tool call in Turn 1,
    and returning final_text once the tool response (ToolReturnPart) is present in messages.
    """

    def fn(messages: list[Any], info: AgentInfo) -> ModelResponse:
        has_tool_return = False
        for msg in messages:
            for part in getattr(msg, "parts", []):
                if isinstance(part, ToolReturnPart):
                    has_tool_return = True
                    break
            if has_tool_return:
                break

        if has_tool_return:
            return ModelResponse(parts=[TextPart(final_text)])

        return ModelResponse(parts=[ToolCallPart(tool_name, args)])

    return FunctionModel(fn)


from tests.unit.job_match.scripts import raw_invalid, structured, tool_then_structured  # noqa: E402

__all__ = ["FakeRpc", "scripted_model", "structured", "tool_then_structured", "raw_invalid"]
