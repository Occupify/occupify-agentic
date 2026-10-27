import logging
from typing import Any

from app.agents import subagent
from app.agents.deps import AgentDeps
from app.agents.runner import run_agent
from app.core.security import CurrentUser
from app.features.job_match.criteria import matches
from app.features.job_match.ports import MatchCriteria
from app.privacy.detectors import remove_patterns
from app.skill_schemas.matching import JobAssessment, ProjectAssessment, RequirementCheck

logger = logging.getLogger(__name__)


def apply_assessment_to_ranked_items(
    pre_ranked: list[dict[str, Any]],
    assessments: dict[str, Any],
) -> list[dict[str, Any]]:
    """Applies assessment summaries and requirements to pre-ranked items while strictly preserving order."""
    final_items = []
    for item in pre_ranked:
        pid = item.get("project_id") or item.get("projectId")
        item_copy = dict(item)
        jobs = []
        proj_asmt = assessments.get(pid, {})
        for job in item.get("jobs", []):
            j_copy = dict(job)
            jid = j_copy.get("job_id") or j_copy.get("jobId")
            j_asmt = (
                proj_asmt.get(jid)
                if isinstance(proj_asmt, dict) and jid in proj_asmt
                else proj_asmt
            )
            if isinstance(j_asmt, dict):
                if "summary" in j_asmt:
                    j_copy["summary"] = j_asmt["summary"]
                if "requirements" in j_asmt:
                    j_copy["requirements"] = j_asmt["requirements"]
            # Strip forbidden keys that LLMs might try to inject
            j_copy.pop("score", None)
            j_copy.pop("order", None)
            jobs.append(j_copy)
        item_copy["jobs"] = jobs
        final_items.append(item_copy)
    return final_items


def validate_v3_criteria(
    items: list[dict[str, Any]],
    criteria: MatchCriteria,
) -> list[dict[str, Any]]:
    """V3 validator: Drops jobs and projects that fail the user's MatchCriteria."""
    filtered_items: list[dict[str, Any]] = []

    for item in items:
        jobs = item.get("jobs", [])
        matched_jobs = [job for job in jobs if matches(criteria, job)]
        if matched_jobs:
            item_copy = dict(item)
            item_copy["jobs"] = matched_jobs
            filtered_items.append(item_copy)

    return filtered_items


def validate_and_filter_assessment(
    raw_assessment: ProjectAssessment,
    valid_req_ids: dict[str, set[str]],
) -> ProjectAssessment:
    """V2 validator: Drops requirement checks referencing unknown refs not in the prompt."""
    cleaned_jobs: list[JobAssessment] = []
    cleaned_dict: dict[str, JobAssessment] = {}

    target_jobs = (
        raw_assessment.jobs
        if raw_assessment.jobs
        else list(raw_assessment.job_assessments.values())
    )

    for job_asmt in target_jobs:
        jid = job_asmt.job or job_asmt.job_id or ""
        valid_set = valid_req_ids.get(jid)
        if valid_set is None:
            for k, s in valid_req_ids.items():
                if (
                    jid.lower() in k.lower()
                    or k.lower() in jid.lower()
                    or k.lower().endswith(jid.lower().lstrip("j"))
                    or jid.lower().endswith(k.lower().lstrip("j"))
                ):
                    valid_set = s
                    break
        if valid_set is None and len(valid_req_ids) == 1:
            valid_set = next(iter(valid_req_ids.values()))
        if valid_set is None:
            valid_set = set()

        valid_reqs = [
            r for r in job_asmt.requirements if (r.ref in valid_set or r.req_id in valid_set)
        ]
        new_asmt = JobAssessment(
            job=jid,
            job_id=jid,
            requirements=valid_reqs,
            summary=job_asmt.summary,
            assessment=job_asmt.assessment,
        )
        cleaned_jobs.append(new_asmt)
        cleaned_dict[jid] = new_asmt

    return ProjectAssessment(jobs=cleaned_jobs, job_assessments=cleaned_dict)


def enforce_emptied_requirements_unclear(
    checks: list[RequirementCheck],
    requirements_input: list[dict[str, str]],
) -> list[RequirementCheck]:
    """Ensures requirements emptied during sanitization are marked 'unclear'."""
    empty_ids = {r.get("id") for r in requirements_input if not (r.get("text") or "").strip()}
    for check in checks:
        cid = check.ref or check.req_id
        if cid in empty_ids:
            check.status = "unclear"
            check.note = "Requirement sanitized (emptied), marked unclear."
    return checks


def clean_output_pii(text: str) -> str:
    """V5 validator: Cleans PII (emails, phone numbers, identifiers) from text."""
    cleaned, _ = remove_patterns(text)
    return cleaned


def _build_rules_fallback(
    project_jobs: dict[str, list[str]],
    lang: str = "vi",
) -> dict[str, Any]:
    assessment: dict[str, Any] = {}
    for job_id, req_list in project_jobs.items():
        req_checks = []
        for idx, _ in enumerate(req_list, 1):
            ref = f"{job_id.upper()}.R{idx}"
            req_checks.append(
                RequirementCheck(
                    ref=ref,
                    req_id=ref,
                    status="unclear",
                    note=(
                        "Đánh giá quy tắc (unclear)"
                        if lang == "vi"
                        else "Rules-based fallback (unclear)"
                    ),
                )
            )
        summary = (
            "Đánh giá quy tắc tự động dựa trên kỹ năng và yêu cầu công việc."
            if lang == "vi"
            else "Automated rules-based assessment based on skills and job requirements."
        )
        assessment[job_id] = {
            "assessment": "rules",
            "summary": summary,
            "requirements": req_checks,
        }
    return assessment


async def validate_assessment_with_retry(
    project_id: str,
    project_jobs: dict[str, list[str]],
    model: Any = None,
    lang: str = "vi",
    cv_profile: Any = None,
    matched_skills: Any = None,
    missing_skills: Any = None,
    budget: Any = None,
) -> tuple[dict[str, Any], list[str]]:
    """Evaluates project jobs against candidate profile with 1 retry before rules fallback."""
    warnings: list[str] = []

    # Attempt LLM assessment with 1 retry (max 2 attempts)
    agent = subagent.create_skill_agent(
        name="assess-job-fit",
        model=model,
        model_settings={"temperature": 0.0},
    )

    prompt = f"Project: {project_id}\nLanguage: {lang}\nJobs:\n"
    for jid, reqs in project_jobs.items():
        prompt += f"Job {jid}:\n"
        for idx, req in enumerate(reqs, 1):
            prompt += f"  {jid.upper()}.R{idx}: {req}\n"

    deps = AgentDeps(
        user=CurrentUser(user_id="system", email="system@example.com", role="USER"),
        session_id="assessment",
    )

    success = False
    assessment: dict[str, Any] = {}

    for attempt in range(2):
        try:
            res = await run_agent(
                agent=agent,
                prompt=prompt,
                deps=deps,
                use_case="job_match",
                agent_role="assessment",
                redact_errors=True,
            )
            out = res.output
            if isinstance(out, ProjectAssessment):
                # Validate that all jobs are covered
                target_jobs = out.jobs if out.jobs else list(out.job_assessments.values())
                if target_jobs:
                    for job_asmt in target_jobs:
                        jid = job_asmt.job or job_asmt.job_id
                        if jid:
                            assessment[jid] = {
                                "assessment": "llm",
                                "summary": job_asmt.summary,
                                "requirements": job_asmt.requirements,
                            }
                    success = True
                    break
        except Exception as exc:
            logger.warning(
                "Assessment attempt %d failed for project %s: %s",
                attempt + 1,
                project_id,
                type(exc).__name__,
            )

    if not success:
        warnings.append("ASSESSMENT_FALLBACK")
        assessment = _build_rules_fallback(project_jobs, lang=lang)

    return assessment, warnings
