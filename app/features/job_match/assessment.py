import asyncio
import logging
import uuid
from typing import Any

from app.agents import subagent
from app.agents.deps import AgentDeps, CurrentUser
from app.agents.runner import run_agent
from app.features.job_match.validators import (
    _build_rules_fallback,
    clean_output_pii,
    enforce_emptied_requirements_unclear,
    validate_and_filter_assessment,
)
from app.skill_schemas.matching import ProjectAssessment

logger = logging.getLogger(__name__)


async def assess_single_project(
    project_item: dict[str, Any],
    profile: Any,
    lang: str = "vi",
    model_override: Any = None,
    parent_run_id: str | None = None,
) -> tuple[dict[str, Any], list[str]]:
    """Runs assess-job-fit skill for a single project's jobs with boundary isolation and rules fallback."""
    project_id = project_item.get("project_id") or project_item.get("id", "unknown")
    jobs = project_item.get("jobs", [])
    warnings: list[str] = []

    if not jobs:
        return project_item, warnings

    # Prepare requirement map and valid ref ids
    # e.g. valid_req_ids = { "j1": {"J1.R1", "J1.R2"} }
    valid_req_ids: dict[str, set[str]] = {}
    project_jobs_req_texts: dict[str, list[str]] = {}
    job_req_inputs: dict[str, list[dict[str, str]]] = {}

    for j_idx, job in enumerate(jobs, 1):
        jid = job.get("job_id") or job.get("id") or f"j{j_idx}"
        raw_reqs = job.get("requirements") or []
        valid_req_ids[jid] = set()
        project_jobs_req_texts[jid] = []
        job_req_inputs[jid] = []

        if raw_reqs:
            for r_idx, r in enumerate(raw_reqs, 1):
                ref = f"J{j_idx}.R{r_idx}"
                valid_req_ids[jid].add(ref)
                text = r if isinstance(r, str) else r.get("text", "")
                project_jobs_req_texts[jid].append(text)
                job_req_inputs[jid].append({"id": ref, "text": text})
        else:
            ref = f"J{j_idx}.D"
            valid_req_ids[jid].add(ref)
            desc = job.get("description", "")
            project_jobs_req_texts[jid].append(desc)
            job_req_inputs[jid].append({"id": ref, "text": desc})

    # Build prompt with boundary tags
    boundary = f"BOUNDARY_{uuid.uuid4().hex[:8]}"
    prompt_lines = [
        f"<{boundary}>",
        f"Project ID: {project_id}",
        f"Language: {lang}",
        "Candidate Profile:",
    ]
    if hasattr(profile, "model_dump_json"):
        prompt_lines.append(profile.model_dump_json())
    elif isinstance(profile, dict):
        prompt_lines.append(str(profile))
    else:
        prompt_lines.append(str(profile))

    prompt_lines.append("Jobs to evaluate:")
    for j_idx, job in enumerate(jobs, 1):
        jid = job.get("job_id") or job.get("id") or f"j{j_idx}"
        title = job.get("title", "")
        matched = job.get("matched_skills") or job.get("matchedSkills") or []
        missing = job.get("missing_skills") or job.get("missingSkills") or []
        prompt_lines.append(f"- Job {jid} (Alias: J{j_idx}): {title}")
        prompt_lines.append(f"  Matched Skills: {', '.join(matched)}")
        prompt_lines.append(f"  Missing Skills: {', '.join(missing)}")
        prompt_lines.append("  Requirements:")
        for r_input in job_req_inputs[jid]:
            prompt_lines.append(f"    - {r_input['id']}: {r_input['text']}")

    prompt_lines.append(f"</{boundary}>")
    prompt = "\n".join(prompt_lines)

    agent = subagent.create_skill_agent(
        name="assess-job-fit",
        model=model_override,
        model_settings={"temperature": 0.0},
    )

    deps = AgentDeps(
        user=CurrentUser(user_id="system", email="system@example.com", role="USER"),
        session_id="job_match_assessment",
        agent_role="assessment",
        parent_run_id=parent_run_id,
    )

    success = False
    asmt_dict: dict[str, Any] = {}

    for attempt in range(2):
        try:
            res = await run_agent(
                agent=agent,
                prompt=prompt,
                deps=deps,
                use_case="job_match",
                agent_role="assessment",
                parent_run_id=parent_run_id,
                redact_errors=True,
            )
            raw_out = res.output
            if isinstance(raw_out, ProjectAssessment):
                cleaned_asmt = validate_and_filter_assessment(raw_out, valid_req_ids)
                target_jobs = (
                    cleaned_asmt.jobs
                    if cleaned_asmt.jobs
                    else list(cleaned_asmt.job_assessments.values())
                )
                if target_jobs:
                    for ja in target_jobs:
                        key = ja.job or ja.job_id
                        clean_summary = clean_output_pii(ja.summary or "")
                        # Map J1/J2 alias back to actual jid if needed
                        matched_jid = None
                        if key in valid_req_ids:
                            matched_jid = key
                        else:
                            for idx, j in enumerate(jobs, 1):
                                if key in (f"J{idx}", f"j{idx}"):
                                    matched_jid = j.get("job_id") or j.get("id")
                                    break
                        if not matched_jid:
                            for j in jobs:
                                actual_id = j.get("job_id") or j.get("id") or ""
                                if (
                                    key.lower() in actual_id.lower()
                                    or actual_id.lower().endswith(key.lower().lstrip("j"))
                                    or key.lower().lstrip("j") in actual_id.lower()
                                ):
                                    matched_jid = actual_id
                                    break
                        if not matched_jid and len(jobs) == 1:
                            matched_jid = jobs[0].get("job_id") or jobs[0].get("id")
                        if not matched_jid:
                            matched_jid = key

                        enforced_reqs = enforce_emptied_requirements_unclear(
                            ja.requirements, job_req_inputs.get(matched_jid, [])
                        )
                        ref_to_text = {
                            item["id"]: item["text"] for item in job_req_inputs.get(matched_jid, [])
                        }
                        reqs = []
                        for r in enforced_reqs:
                            d = r.model_dump()
                            cid = d.get("ref") or d.get("req_id")
                            d["text"] = ref_to_text.get(cid, "")
                            reqs.append(d)

                        asmt_dict[matched_jid] = {
                            "assessment": "llm",
                            "summary": clean_summary,
                            "requirements": reqs,
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
        rules_asmt = _build_rules_fallback(project_jobs_req_texts, lang=lang)
        for jid, data in rules_asmt.items():
            ref_to_text = {item["id"]: item["text"] for item in job_req_inputs.get(jid, [])}
            reqs = []
            for r in data["requirements"]:
                d = r.model_dump() if hasattr(r, "model_dump") else dict(r)
                cid = d.get("ref") or d.get("req_id")
                d["text"] = ref_to_text.get(cid, "")
                reqs.append(d)
            asmt_dict[jid] = {
                "assessment": "rules",
                "summary": data["summary"],
                "requirements": reqs,
            }

    # Attach assessment back to project jobs
    updated_jobs = []
    for job in jobs:
        j_copy = dict(job)
        jid = j_copy.get("job_id") or j_copy.get("id")
        if jid in asmt_dict:
            j_copy["assessment"] = asmt_dict[jid].get("assessment", "llm")
            j_copy["summary"] = asmt_dict[jid].get("summary", "")
            j_copy["requirement_checks"] = asmt_dict[jid].get("requirements", [])
        updated_jobs.append(j_copy)

    updated_project = dict(project_item)
    updated_project["jobs"] = updated_jobs
    return updated_project, warnings


async def assess_shortlisted_projects(
    shortlisted: list[dict[str, Any]],
    profile: Any,
    lang: str = "vi",
    model_override: Any = None,
    concurrency: int = 4,
    parent_run_id: str | None = None,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Concurrently assesses shortlisted projects with controlled concurrency."""
    if not shortlisted:
        return [], []

    sem = asyncio.Semaphore(concurrency)
    all_warnings: list[str] = []

    async def _bound_assess(p: dict[str, Any]) -> dict[str, Any]:
        async with sem:
            assessed_p, warns = await assess_single_project(
                project_item=p,
                profile=profile,
                lang=lang,
                model_override=model_override,
                parent_run_id=parent_run_id,
            )
            for w in warns:
                if w not in all_warnings:
                    all_warnings.append(w)
            return assessed_p

    tasks = [_bound_assess(p) for p in shortlisted]
    results = await asyncio.gather(*tasks)
    return list(results), all_warnings
