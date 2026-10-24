import pytest
from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel

from app.agents.deps import AgentDeps
from app.agents.runner import run_agent
from app.core.security import CurrentUser


@pytest.mark.asyncio
async def test_runner_with_test_model(test_db):
    test_agent = Agent(
        model="zai:glm-4.7",
        system_prompt="You are a helpful test assistant.",
        deps_type=AgentDeps,
    )

    user = CurrentUser(user_id="user-999", role="ROLE_USER", email="u@example.com")
    deps = AgentDeps(user=user, session_id="sess-123", db=test_db)

    # Use TestModel override
    with test_agent.override(model=TestModel(custom_output_text="Test response")):
        res = await run_agent(
            agent=test_agent,
            prompt="Hello agent",
            deps=deps,
            use_case="chat",
        )

        assert res.output == "Test response"
        assert res.model == "glm-4.7"
        assert res.run_id is not None

        from app.db.models import AgentRun

        run_record = await test_db.get(AgentRun, res.run_id)
        assert run_record is not None
        assert run_record.status == "succeeded"
        assert run_record.user_id == "user-999"
        assert len(run_record.steps) >= 3  # run.start, llm.request, llm.response, run.end
