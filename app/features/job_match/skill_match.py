import uuid
from typing import Any

from pydantic_ai.settings import ModelSettings

from app.agents.budget import RunBudget
from app.agents.deps import AgentDeps
from app.agents.runner import run_agent
from app.agents.subagent import create_skill_agent
from app.core.security import CurrentUser
from app.features.job_match.normalize import normalize_skill_name
from app.features.job_match.ports import PipelineOptions
from app.skill_schemas.candidate import CandidateProfile
from app.skill_schemas.matching import JobSkillVerdict, SkillMatchResult


def compute_skill_coverage(verdicts: list[JobSkillVerdict]) -> float:
    """
    Computes coverage weight:
    exact = 1.0, equivalent = 1.0, inferred/implied = 0.8, missing = 0.0
    c = sum(weights) / len(verdicts)
    """
    if not verdicts:
        return 0.0

    weight_map = {
        "exact": 1.0,
        "equivalent": 1.0,
        "implied": 0.8,
        "inferred": 0.8,
        "missing": 0.0,
    }
    total = sum(weight_map.get(v.verdict, 0.0) for v in verdicts)
    return total / float(len(verdicts))


def _build_skill_match_prompt(
    candidate_skills: list[str],
    project_jobs: dict[str, list[str]],
) -> str:
    c_skills_block = "\n".join(f"- {s}" for s in candidate_skills)
    p_jobs_lines: list[str] = []
    for jid, skills in project_jobs.items():
        p_jobs_lines.append(f"Job {jid}:")
        for s in skills:
            p_jobs_lines.append(f"  - {s}")
    p_jobs_block = "\n".join(p_jobs_lines)

    return (
        f"<candidate-skills>\n{c_skills_block}\n</candidate-skills>\n\n"
        f"<project-jobs>\n{p_jobs_block}\n</project-jobs>"
    )


def _code_fallback_match(
    project_jobs: dict[str, list[str]],
    candidate_skills: list[str],
) -> dict[str, dict[str, Any]]:
    norm_candidate = {normalize_skill_name(s): s for s in candidate_skills}
    results: dict[str, dict[str, Any]] = {}

    for jid, skills in project_jobs.items():
        matched: list[dict[str, str]] = []
        missing: list[str] = []
        verdicts: list[JobSkillVerdict] = []

        for skill in skills:
            norm_s = normalize_skill_name(skill)
            if norm_s in norm_candidate:
                orig_cs = norm_candidate[norm_s]
                v_type = "exact" if orig_cs.lower() == skill.lower() else "equivalent"
                matched.append({"name": skill, "source": v_type, "cv_skill": orig_cs})
                verdicts.append(JobSkillVerdict(job_skill=skill, verdict=v_type, cv_skill=orig_cs))
            else:
                missing.append(skill)
                verdicts.append(JobSkillVerdict(job_skill=skill, verdict="missing", cv_skill=None))

        coverage = compute_skill_coverage(verdicts)
        results[jid] = {
            "matched": matched,
            "missing": missing,
            "coverage": coverage,
            "verdicts": verdicts,
        }
    return results


async def match_skills_for_project(
    project_id: str,
    project_jobs: dict[str, list[str]],
    profile: CandidateProfile,
    budget: RunBudget | None = None,
    options: PipelineOptions | None = None,
    deps: AgentDeps | None = None,
    parent_run_id: str | None = None,
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """
    Matches candidate skills against all jobs of a single project in one model call.
    Falls back to normalise-only code matching if validation fails.
    """
    candidate_skills: list[str] = []
    for s in profile.skills:
        if isinstance(s, str):
            candidate_skills.append(s)
        elif hasattr(s, "name"):
            candidate_skills.append(s.name)

    # Collect role skills too
    for r in profile.roles:
        candidate_skills.extend(r.skills_used or [])
    candidate_skills = list(dict.fromkeys(candidate_skills))  # dedupe preserving order

    prompt = _build_skill_match_prompt(candidate_skills, project_jobs)
    prompt_mode = options.prompt_mode if options else "skill"

    agent = create_skill_agent(
        name="match-skills",
        model_settings=ModelSettings(temperature=0.0),
        prompt_mode=prompt_mode,
    )

    effective_deps = deps or AgentDeps(
        user=CurrentUser(user_id="job-match-user", role="ROLE_USER"),
        session_id=str(uuid.uuid4()),
        agent_role="skill_match",
        parent_run_id=parent_run_id,
    )

    usage = budget.usage if budget else None
    limits = budget.limits_for("skill_match") if budget else None

    warnings: list[str] = []
    try:
        run_res = await run_agent(
            agent=agent,
            prompt=prompt,
            deps=effective_deps,
            use_case="job_match",
            usage=usage,
            usage_limits=limits,
            agent_role="skill_match",
            parent_run_id=parent_run_id,
            redact_errors=True,
        )

        output = run_res.output
        if isinstance(output, SkillMatchResult):
            match_result = output
        elif isinstance(output, dict):
            match_result = SkillMatchResult.model_validate(output)
        else:
            match_result = SkillMatchResult.model_validate_json(str(output))

        # Validate that model returned valid job skills matching candidate skills
        results: dict[str, dict[str, Any]] = {}
        for jid, expected_skills in project_jobs.items():
            j_verdicts = match_result.job_verdicts.get(jid)
            if not j_verdicts:
                raise ValueError(f"Missing verdicts for job {jid}")

            matched: list[dict[str, str]] = []
            missing: list[str] = []
            valid_j_verdicts: list[JobSkillVerdict] = []

            verdict_map = {v.job_skill: v for v in j_verdicts}
            for exp_s in expected_skills:
                if exp_s not in verdict_map:
                    raise ValueError(f"Job skill {exp_s} missing from verdicts")
                v = verdict_map[exp_s]
                if v.verdict != "missing":
                    # cv_skill must be in candidate skills
                    if not v.cv_skill or v.cv_skill not in candidate_skills:
                        raise ValueError(f"Unknown cv_skill {v.cv_skill}")
                    matched.append(
                        {
                            "name": exp_s,
                            "source": "inferred" if v.verdict == "implied" else v.verdict,
                            "cv_skill": v.cv_skill,
                        }
                    )
                else:
                    missing.append(exp_s)
                valid_j_verdicts.append(v)

            results[jid] = {
                "matched": matched,
                "missing": missing,
                "coverage": compute_skill_coverage(valid_j_verdicts),
                "verdicts": valid_j_verdicts,
            }

        return results, warnings

    except Exception:
        # Fall back to deterministic normalized code fallback
        warnings.append("SKILL_MATCH_FALLBACK")
        fallback_results = _code_fallback_match(project_jobs, candidate_skills)
        return fallback_results, warnings
