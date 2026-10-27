import logging
import re
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

logger = logging.getLogger(__name__)

KNOWN_SKILLS_FOR_FALLBACK = [
    "Python",
    "FastAPI",
    "Django",
    "Flask",
    "Java",
    "Spring Boot",
    "Spring",
    "Hibernate",
    "JPA",
    "PostgreSQL",
    "Postgres",
    "MySQL",
    "MongoDB",
    "Redis",
    "Docker",
    "Kubernetes",
    "Linux",
    "Git",
    "CI/CD",
    "React",
    "ReactJS",
    "Next.js",
    "Vue",
    "Vue.js",
    "Angular",
    "TypeScript",
    "JavaScript",
    "HTML5",
    "CSS3",
    "Tailwind",
    "TailwindCSS",
    "Node.js",
    "NodeJS",
    "Express",
    "Flutter",
    "Dart",
    "Android",
    "iOS",
    "Swift",
    "Kotlin",
    "Golang",
    "Go",
    "C++",
    "C#",
    ".NET",
    "Rust",
    "REST API",
    "RESTful API",
    "GraphQL",
    "RabbitMQ",
    "Kafka",
    "Data Analyst",
    "Data Analysis",
    "SQL",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Deep Learning",
    "LangChain",
    "RAG",
    "LLM",
    "Figma",
    "UI/UX",
    "UI / UX",
    "Premiere Pro",
    "After Effects",
    "Video Editing",
    "Photoshop",
    "Illustrator",
    "Shopify",
    "Liquid",
    "E-commerce",
    "DevOps",
    "AWS",
    "GCP",
    "Azure",
]


def _code_fallback_profile(cleaned_cv: str) -> CandidateProfile:
    found_skills: list[SkillItem] = []
    seen = set()
    for s in KNOWN_SKILLS_FOR_FALLBACK:
        pattern = r"\b" + re.escape(s) + r"\b"
        if re.search(pattern, cleaned_cv, re.IGNORECASE):
            norm = s.lower()
            if norm not in seen:
                seen.add(norm)
                found_skills.append(SkillItem(name=s, source="stated"))

    status = "ok" if len(found_skills) >= 2 else "insufficient_data"
    return CandidateProfile(
        status=status,
        language="vi",
        skills=found_skills,
        roles=[],
        total_years=1.0 if status == "ok" else 0.0,
    )


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
    Falls back to regex/rule-based extraction if model fails or budget is exceeded.
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

    warnings: list[JobMatchWarning] = []
    profile = None

    try:
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
        if isinstance(res.output, CandidateProfile):
            profile = res.output
        elif isinstance(res.output, dict):
            profile = CandidateProfile.model_validate(res.output)
        else:
            profile = CandidateProfile.model_validate_json(str(res.output))
    except Exception as exc:
        logger.warning(
            "Profile extraction agent failed (%s: %s); applying rule-based fallback.",
            type(exc).__name__,
            exc,
        )
        profile = _code_fallback_profile(cleaned_cv)
        warnings.append(
            JobMatchWarning(
                code="PROFILE_FALLBACK",
                message=f"Profile extraction used code fallback due to {type(exc).__name__}.",
            )
        )

    # Convert any raw string skills to SkillItem instances
    normalized_skills: list[SkillItem | str] = []
    for s in profile.skills:
        if isinstance(s, str):
            normalized_skills.append(SkillItem(name=s, source="stated"))
        else:
            normalized_skills.append(s)
    profile.skills = normalized_skills

    # Augment with total_years if not already set
    if not getattr(profile, "total_years", 0.0):
        profile.total_years = _compute_total_years(profile.roles)

    outcome_str = map_profile_to_outcome(profile)

    if outcome_str == "NOT_A_CV":
        return profile, RunOutcome.NOT_A_CV, warnings
    if outcome_str == "INSUFFICIENT_PROFILE":
        return profile, RunOutcome.INSUFFICIENT_PROFILE, warnings

    return profile, RunOutcome.OK, warnings
