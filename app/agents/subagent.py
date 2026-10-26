import time
from typing import Any

from pydantic_ai import Agent, RunContext

from app.agents.deps import AgentDeps
from app.core.logging import get_current_context, log_step
from app.core.pricing import calculate_token_cost
from app.llm.glm import get_model

UNIVERSAL_SUBAGENT_PROMPT = """You are a capable, autonomous AI Subagent.
You execute focused tasks delegated by primary agents.
You have access to available tools to query services, search projects, inspect details, and synthesize results.
Analyze the instructions, utilize tools as needed, and return a clear, comprehensive answer.
"""


def create_subagent(
    tools: list[Any] | None = None,
    system_prompt: str = UNIVERSAL_SUBAGENT_PROMPT,
) -> Agent[AgentDeps, str]:
    """Factory to create a universal subagent equipped with available tools."""
    model = get_model()
    agent = Agent(
        model=model,
        system_prompt=system_prompt,
        deps_type=AgentDeps,
    )
    if tools:
        for tool in tools:
            agent.tool(tool)
    return agent


async def invoke_subagent(
    ctx: RunContext[AgentDeps],
    task: str,
    context: str | None = None,
) -> str:
    """
    Universal tool to spawn and execute an autonomous subagent for complex or multi-step tasks.
    The subagent has access to tools (such as project querying) and returns its synthesized response.

    Args:
        task: Clear instruction describing the task for the subagent to perform.
        context: Optional background data or constraints.
    """
    from app.features.projects.tools import get_project_detail, search_filter_projects

    current_ctx = get_current_context()
    parent_run_id = current_ctx.get("run_id")

    subagent_deps = AgentDeps(
        user=ctx.deps.user,
        session_id=ctx.deps.session_id,
        db=ctx.deps.db,
        rpc=ctx.deps.rpc,
        parent_run_id=parent_run_id,
        agent_role="subagent",
    )

    log_step(
        "subagent.start",
        task_summary=task[:80].strip(),
        parent_run_id=parent_run_id,
    )
    start_time = time.perf_counter()
    try:
        subagent = create_subagent(tools=[search_filter_projects, get_project_detail])
        prompt = f"Task: {task}"
        if context:
            prompt += f"\nContext: {context}"

        result = await subagent.run(prompt, deps=subagent_deps)
        duration_ms = int((time.perf_counter() - start_time) * 1000)
        output_str = result.output if isinstance(result.output, str) else str(result.output)
        usage = getattr(result, "usage", None)
        if callable(usage):
            usage = usage()
        input_tokens = getattr(usage, "input_tokens", 0) or 0
        output_tokens = getattr(usage, "output_tokens", 0) or 0
        cached_tokens = getattr(usage, "cache_read_tokens", 0) or 0
        total_tokens = getattr(usage, "total_tokens", 0) or (input_tokens + output_tokens)

        cost = calculate_token_cost(
            model="glm-4.5-air",
            tokens_in=input_tokens,
            tokens_out=output_tokens,
            tokens_cached=cached_tokens,
        )
        log_step(
            "subagent.end",
            ms=duration_ms,
            ok=True,
            output_chars=len(output_str),
            parent_run_id=parent_run_id,
            prompt_tokens=input_tokens,
            completion_tokens=output_tokens,
            total_tokens=total_tokens,
            cost_usd=cost["cost_usd"],
            cost_vnd=cost["cost_vnd"],
        )
        return output_str
    except Exception as exc:
        duration_ms = int((time.perf_counter() - start_time) * 1000)
        log_step(
            "subagent.end",
            ms=duration_ms,
            ok=False,
            error=str(exc),
            parent_run_id=parent_run_id,
        )
        raise
