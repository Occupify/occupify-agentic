import asyncio
from types import SimpleNamespace

from pydantic_ai import Agent
from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart, ToolReturnPart
from pydantic_ai.models.function import FunctionModel

from app.agents.deps import AgentDeps
from app.core.config import get_settings
from app.core.security import CurrentUser
from app.features.cv_generator.schemas import CvContent, GenerateCvResult
from app.features.cv_generator.tools import generate_cv
from tests.unit.cv_generator.helpers import sample_payload


def context():
    return SimpleNamespace(
        deps=AgentDeps(
            user=CurrentUser(user_id="owner", email="must-not-print@example.invalid"),
            session_id="session",
            parent_run_id="turn-1",
        )
    )


async def test_disabled_tool_does_not_initialize_cloud(monkeypatch):
    monkeypatch.setattr(get_settings(), "CV_GENERATOR_ENABLED", False)
    payload = sample_payload()
    result = await generate_cv(
        context(),
        payload["template_id"],
        payload["language"],
        CvContent.model_validate(payload["cv"]),
    )
    assert result.error.code == "FEATURE_DISABLED"
    assert result.files == []


async def test_concurrent_identical_calls_share_operation_and_owner(monkeypatch):
    monkeypatch.setattr(get_settings(), "CV_GENERATOR_ENABLED", True)
    ctx = context()

    class Service:
        calls = 0

        async def generate(self, payload, owner_id):
            self.calls += 1
            assert owner_id == "owner"
            assert "must-not-print" not in payload.model_dump_json()
            await asyncio.sleep(0.01)
            return GenerateCvResult(status="succeeded", artifact_id="shared")

    service = Service()
    ctx.deps.cv_generator_service = service
    payload = sample_payload()
    cv = CvContent.model_validate(payload["cv"])
    a, b = await asyncio.gather(
        generate_cv(ctx, "classic", "vi", cv), generate_cv(ctx, "classic", "vi", cv)
    )
    assert a.artifact_id == b.artifact_id == "shared"
    assert service.calls == 1
    ctx.deps.parent_run_id = "turn-2"
    await generate_cv(ctx, "classic", "vi", cv)
    assert service.calls == 2


async def test_transient_failure_can_be_retried(monkeypatch):
    monkeypatch.setattr(get_settings(), "CV_GENERATOR_ENABLED", True)
    from app.features.cv_generator.schemas import CvGenerationError

    ctx = context()

    class Service:
        calls = 0

        async def generate(self, payload, owner_id):
            self.calls += 1
            if self.calls == 1:
                return GenerateCvResult.failure(CvGenerationError("UPLOAD_FAILED", retryable=True))
            return GenerateCvResult(status="succeeded", artifact_id="retry")

    ctx.deps.cv_generator_service = Service()
    cv = CvContent.model_validate(sample_payload()["cv"])
    assert (await generate_cv(ctx, "classic", "vi", cv)).status == "failed"
    assert (await generate_cv(ctx, "classic", "vi", cv)).artifact_id == "retry"


async def test_agent_sees_exact_three_top_level_arguments(monkeypatch):
    monkeypatch.setattr(get_settings(), "CV_GENERATOR_ENABLED", False)
    seen = {}

    def respond(messages, info):
        seen["schema"] = info.function_tools[0].parameters_json_schema
        if any(isinstance(part, ToolReturnPart) for part in messages[-1].parts):
            return ModelResponse(parts=[TextPart("Done")])
        return ModelResponse(parts=[ToolCallPart("generate_cv", sample_payload())])

    model = FunctionModel(respond)
    agent = Agent(model, deps_type=AgentDeps)
    agent.tool(generate_cv)
    await agent.run("Generate the CV", deps=context().deps)
    schema = seen["schema"]
    assert set(schema["properties"]) == {"template_id", "language", "cv"}
    assert "user_id" not in schema["properties"]
