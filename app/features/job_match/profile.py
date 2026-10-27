import uuid
from typing import Any

from pydantic_ai.settings import ModelSettings

from app.agents import subagent
from app.agents.budget import RunBudget
from app.agents.deps import AgentDeps
from app.agents.runner import run_agent
from app.core.security import CurrentUser
from app.features.job_match.ports import PipelineOptions
from app.features.job_match.schemas import JobMatchWarning, RunOutcome
from app.skill_schemas.candidate import CandidateProfile, SkillItem


def map_profile_to_outcome(profile: CandidateProfile) -> str:
    """Maps candidate profile extraction status and skill count to outcome string."""
    if profile.status == "not_a_cv":
        return "NOT_A_CV"
    if profile.status != "ok":
        return "INSUFFICIENT_PROFILE"

    skill_count = len(profile.skills)
    if skill_count < 2:
        return "INSUFFICIENT_PROFILE"

    return "OK"


def _wrap_in_boundary(text: str) -> tuple[str, str]:
    tag = f"CV_DATA_{uuid.uuid4().hex[:8]}"
    safe_lines = [line for line in text.splitlines() if not line.strip().startswith("<CV_DATA_")]
    wrapped = f"<{tag}>\n" + "\n".join(safe_lines) + f"\n</{tag}>"
    return wrapped, tag


def _compute_total_years(roles: list[Any]) -> float:
    # Estimate total years from role count or dates
    if not roles:
        return 0.0
    return min(30.0, float(len(roles)) * 1.5)


async def extract_profile(
    cleaned_cv: str,
    budget: RunBudget,
    user: CurrentUser,
    deps: AgentDeps | None = None,
    options: PipelineOptions | None = None,
    parent_run_id: str | None = None,
) -> tuple[CandidateProfile, RunOutcome, list[JobMatchWarning]]:
    """
    Extracts structured candidate profile from cleaned CV text using the
    extract-candidate-profile skill agent under RunBudget constraints.
    """
    prompt_mode = options.prompt_mode if options else "skill"
    agent = subagent.create_skill_agent(
        name="extract-candidate-profile",
        model_settings=ModelSettings(temperature=0.0),
        prompt_mode=prompt_mode,
    )

    wrapped_prompt, _ = _wrap_in_boundary(cleaned_cv)
    limits = budget.limits_for("profile")

    effective_deps = deps or AgentDeps(
        user=user,
        session_id=str(uuid.uuid4()),
        agent_role="profile",
        parent_run_id=parent_run_id,
    )

    res = await run_agent(
        agent=agent,
        prompt=wrapped_prompt,
        deps=effective_deps,
        use_case="job_match",
        usage=budget.usage,
        usage_limits=limits,
        agent_role="profile",
        parent_run_id=parent_run_id,
        redact_errors=True,
    )

    # res.output could be parsed CandidateProfile or JSON string
    if isinstance(res.output, CandidateProfile):
        profile = res.output
    elif isinstance(res.output, dict):
        profile = CandidateProfile.model_validate(res.output)
    else:
        try:
            profile = CandidateProfile.model_validate_json(str(res.output))
        except Exception:
            profile = CandidateProfile(
                status="insufficient_data",
                language="vi",
                skills=[],
                roles=[],
            )

    # Convert any raw string skills to SkillItem instances
    normalized_skills: list[SkillItem | str] = []
    for s in profile.skills:
        if isinstance(s, str):
            normalized_skills.append(SkillItem(name=s, source="stated"))
        else:
            normalized_skills.append(s)
    profile.skills = normalized_skills

    # Augment with total_years
    profile.total_years = _compute_total_years(profile.roles)

    outcome_str = map_profile_to_outcome(profile)
    warnings: list[JobMatchWarning] = []

    if outcome_str == "NOT_A_CV":
        return profile, RunOutcome.NOT_A_CV, warnings
    if outcome_str == "INSUFFICIENT_PROFILE":
        return profile, RunOutcome.INSUFFICIENT_PROFILE, warnings

    return profile, RunOutcome.OK, warnings
