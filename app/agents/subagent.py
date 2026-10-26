import time
from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path
from typing import Any

from pydantic_ai import Agent, RunContext

from app.agents.deps import AgentDeps
from app.agents.skill_registry import SkillRegistry
from app.core.logging import get_current_context, log_step
from app.core.pricing import calculate_token_cost
from app.llm.glm import get_model

_skill_model_overrides: ContextVar[dict[str, Any]] = ContextVar(
    "_skill_model_overrides", default={}
)
_global_registry: SkillRegistry | None = None


def get_skill_registry() -> SkillRegistry:
    global _global_registry
    if _global_registry is None:
        _global_registry = SkillRegistry()
        skills_path = Path("skills")
        if skills_path.exists():
            _global_registry.scan(skills_path)
    return _global_registry


@contextmanager
def override_skill_models(overrides: dict[str, Any]):
    current = dict(_skill_model_overrides.get())
    current.update(overrides)
    token = _skill_model_overrides.set(current)
    try:
        yield
    finally:
        _skill_model_overrides.reset(token)


def _get_default_test_model(name: str) -> Any:
    from pydantic_ai.messages import ModelResponse, ToolCallPart
    from pydantic_ai.models.function import AgentInfo, FunctionModel

    from app.skill_schemas.candidate import CandidateProfile, RoleItem
    from app.skill_schemas.matching import (
        JobAssessment,
        ProjectAssessment,
        RequirementCheck,
        SkillMatchResult,
    )
    from app.skill_schemas.search import SearchDecision

    def fn(messages: list[Any], info: AgentInfo) -> ModelResponse:
        tool_name = info.output_tools[0].name if info.output_tools else "final_result"
        prompt_text = ""
        for m in messages:
            for part in getattr(m, "parts", []):
                if hasattr(part, "content") and isinstance(part.content, str):
                    prompt_text += part.content + "\n"

        if name == "extract-candidate-profile":
            known_skills = [
                "Java",
                "Spring Boot",
                "PostgreSQL",
                "Docker",
                "Git",
                "RESTful API",
                "Microservices",
                "Python",
                "FastAPI",
                "React",
                "NodeJS",
                "TypeScript",
                "SQL Optimization",
                "CI/CD",
                "JPA/Hibernate",
                "JUnit 5",
                "Mockito",
            ]
            found = [s for s in known_skills if s.lower() in prompt_text.lower()]
            if not found:
                import re

                lines = prompt_text.splitlines()
                for line in lines:
                    m_line = re.match(r"^\s*-\s*([^:]+)", line)
                    if m_line:
                        found.append(m_line.group(1).strip())
            if not found:
                found = ["Java", "Spring Boot", "PostgreSQL"]

            target_roles = (
                ["Backend Developer"]
                if any(s in found for s in ["Java", "Python", "Spring Boot"])
                else ["Software Engineer"]
            )
            profile = CandidateProfile(
                status="ok",
                language="vi",
                skills=found,
                roles=[
                    RoleItem(
                        title="Senior Backend Engineer",
                        skills_used=found[:5],
                    )
                ],
                target_roles=target_roles,
            )
            return ModelResponse(parts=[ToolCallPart(tool_name, profile.model_dump(mode="json"))])

        elif name == "match-skills":
            import re

            c_skills = []
            m_c = re.search(r"<candidate-skills>(.*?)</candidate-skills>", prompt_text, re.DOTALL)
            if m_c:
                for line in m_c.group(1).splitlines():
                    cleaned_line = line.strip().lstrip("- ").strip()
                    if cleaned_line:
                        c_skills.append(cleaned_line)

            job_verdicts: dict[str, list[dict[str, Any]]] = {}
            m_pj = re.search(r"<project-jobs>(.*?)</project-jobs>", prompt_text, re.DOTALL)
            if m_pj:
                current_job = None
                for line in m_pj.group(1).splitlines():
                    m_job = re.match(r"Job\s+([^\s:]+):", line.strip())
                    if m_job:
                        current_job = m_job.group(1)
                        job_verdicts[current_job] = []
                    elif current_job:
                        m_sk = re.match(r"-\s+(.+)$", line.strip())
                        if m_sk:
                            sk = m_sk.group(1).strip()
                            matched_cv = None
                            for cs in c_skills:
                                if (
                                    cs.lower() == sk.lower()
                                    or sk.lower() in cs.lower()
                                    or cs.lower() in sk.lower()
                                ):
                                    matched_cv = cs
                                    break
                            if matched_cv:
                                job_verdicts[current_job].append(
                                    {
                                        "job_skill": sk,
                                        "verdict": "exact",
                                        "cv_skill": matched_cv,
                                    }
                                )
                            else:
                                job_verdicts[current_job].append(
                                    {
                                        "job_skill": sk,
                                        "verdict": "missing",
                                        "cv_skill": None,
                                    }
                                )

            result = SkillMatchResult(job_verdicts=job_verdicts)
            return ModelResponse(parts=[ToolCallPart(tool_name, result.model_dump(mode="json"))])

        elif name == "assess-job-fit":
            import re

            jobs_found = re.findall(r"-\s*Job\s+([^\s:]+)", prompt_text)
            if not jobs_found:
                jobs_found = ["j1"]

            jobs_asmts = []
            for jid in jobs_found:
                req_refs = re.findall(rf"({jid.upper()}\.[RD]\d*)", prompt_text)
                req_checks = [
                    RequirementCheck(
                        ref=r,
                        req_id=r,
                        status="met",
                        note="Candidate profile demonstrates capability.",
                    )
                    for r in req_refs
                ]
                if not req_checks:
                    req_checks = [
                        RequirementCheck(
                            ref=f"{jid.upper()}.D",
                            req_id=f"{jid.upper()}.D",
                            status="met",
                            note="Fits requirements.",
                        )
                    ]

                jobs_asmts.append(
                    JobAssessment(
                        job=jid,
                        job_id=jid,
                        requirements=req_checks,
                        summary="Candidate demonstrates strong experience aligned with role requirements.",
                    )
                )

            asmt = ProjectAssessment(jobs=jobs_asmts)
            return ModelResponse(parts=[ToolCallPart(tool_name, asmt.model_dump(mode="json"))])

        elif name == "plan-job-search":
            decision = SearchDecision(action="done", query="", skills=[])
            return ModelResponse(parts=[ToolCallPart(tool_name, decision.model_dump(mode="json"))])

        return ModelResponse(parts=[ToolCallPart(tool_name, {})])

    return FunctionModel(fn)


def create_skill_agent(
    name: str,
    tools: list[Any] | None = None,
    model_settings: Any = None,
    prompt_mode: str = "skill",
    model: Any = None,
) -> Agent:
    if model is None:
        overrides = _skill_model_overrides.get()
        if name in overrides:
            model = overrides[name]
        else:
            from pydantic_ai import models

            if not models.ALLOW_MODEL_REQUESTS:
                model = _get_default_test_model(name)
            else:
                model = get_model()

    registry = get_skill_registry()
    meta = registry.get(name)
    output_type = meta.output_type if meta else None

    if prompt_mode == "plain":
        system_prompt = f"Perform {name}."
    else:
        system_prompt = meta.prompt if meta else ""

    agent = Agent(
        model=model,
        system_prompt=system_prompt,
        output_type=output_type,
        deps_type=AgentDeps,
        model_settings=model_settings,
        retries=3,
    )
    if tools:
        for t in tools:
            agent.tool(t)
    return agent


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
