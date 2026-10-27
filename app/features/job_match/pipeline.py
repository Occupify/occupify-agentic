import asyncio
import logging
import re
import uuid
from typing import Any

import pypdfium2 as pdfium

from app.agents.budget import RunBudget, StopReason
from app.core.config import get_settings
from app.core.logging import bind_context, log_step
from app.core.pricing import calculate_token_cost
from app.core.security import CurrentUser
from app.features.job_match.assessment import assess_shortlisted_projects
from app.features.job_match.criteria import matches as criteria_matches
from app.features.job_match.freshness import check_projects_freshness
from app.features.job_match.ports import (
    IndexRow,
    MatchCriteria,
    PipelineOptions,
    PipelineResult,
    RunResult,
    RunState,
)
from app.features.job_match.profile import extract_profile
from app.features.job_match.retrieval import build_queries, compute_exhausted, rrf_fuse
from app.features.job_match.sanitize import sanitize_project
from app.features.job_match.schemas import ErrorCode, JobMatchWarning, RunOutcome, RunStatus
from app.features.job_match.scoring import (
    compute_experience_score,
    compute_job_score,
    compute_project_scores,
)
from app.features.job_match.search_agent import maybe_search_more
from app.features.job_match.skill_match import match_skills_for_project
from app.features.job_match.validators import validate_v3_criteria
from app.documents.cv_text import CvText, gate_cv_text
from app.ml import get_embedder, get_reranker
from app.privacy.gate import clean as privacy_clean

logger = logging.getLogger(__name__)


def handle_budget_exceeded_at_stage(stage: str) -> str:
    """Returns the budget exceeded fallback action based on current pipeline stage."""
    if stage in ("assessment", "s9_assessment", "skill_match", "s5b_skill_match"):
        return "rules_fallback"
    if stage in ("search", "s7_search_agent"):
        return "stop_budget"
    return "RUN_BUDGET_EXCEEDED"


def clean_cv(text: str, source: str = "cv", is_file: bool = True, user: CurrentUser | None = None) -> str:
    """Cleans CV text using privacy gate. Raises exception if PII removal fails."""
    cv_obj = gate_cv_text(text, user=user)
    return cv_obj.text



def sanitize_boundary_text(text: str, boundary_tag: str) -> str:
    """Strips boundary marker lines to protect against boundary collision or prompt injection."""
    lines = text.splitlines()
    clean_lines = []
    open_tag = f"<{boundary_tag}>"
    close_tag = f"</{boundary_tag}>"
    for line in lines:
        if open_tag in line or close_tag in line or "---BOUNDARY---" in line:
            continue
        clean_lines.append(line)
    return "\n".join(clean_lines)


def _is_cv_precheck(text: str) -> bool:
    """S0a pre-check: Verifies document contains at least one standard CV section header."""
    from app.privacy.sections import INCLUDED_SECTION_KEYWORDS, REMOVED_SECTION_KEYWORDS

    all_kws = INCLUDED_SECTION_KEYWORDS + REMOVED_SECTION_KEYWORDS
    for kw in all_kws:
        if re.search(r"\b" + kw + r"\b", text, re.IGNORECASE):
            return True
    return False


async def run_pipeline(
    cv_text: Any = None,
    user: CurrentUser | None = None,
    store: Any = None,
    core_rpc: Any = None,
    criteria: MatchCriteria | None = None,
    lang: str = "vi",
    options: PipelineOptions | None = None,
    on_stage: Any = None,
    state: RunState | None = None,
    pdf_bytes: bytes | None = None,
) -> PipelineResult:
    """Full UC4 pipeline orchestrator (S0a-S10) under RunBudget and privacy constraints."""
    settings = get_settings()
    state = state or RunState()
    criteria = criteria or MatchCriteria()
    options = options or PipelineOptions()
    if core_rpc is None:
        from app.messaging.core_client import get_core_rpc

        core_rpc = get_core_rpc()

    run_id = state.run_id or str(uuid.uuid4())
    state.run_id = run_id
    user_id = user.user_id if user else "anonymous"
    bind_context(
        run_id=run_id,
        use_case="job_match",
        user_id=user_id,
        redact_errors=True,
    )
    log_step("job_match.start", run_id=run_id, user_id=user_id)

    warnings: list[dict[str, str]] = []
    run_status = RunStatus.SUCCEEDED
    budget = RunBudget()

    def set_stage(st: str) -> None:
        state.stage = st
        log_step("job_match.stage", run_id=run_id, stage=st)
        if on_stage:
            on_stage(st)

    # -------------------------------------------------------------
    # S0a: CV text & pre-check
    # -------------------------------------------------------------
    set_stage("s0_extract_text")
    if cv_text is None and pdf_bytes is not None:
        try:
            pdf = pdfium.PdfDocument(pdf_bytes)
            raw_text = "".join(p.get_textpage().get_text_range() for p in pdf)
        except Exception as exc:
            logger.warning("Failed to extract PDF text: %s", exc)
            raw_text = ""

        set_stage("s0a_precheck")
        if not _is_cv_precheck(raw_text):
            log_step(
                "job_match.end",
                run_id=run_id,
                status=RunStatus.SUCCEEDED.value,
                outcome=RunOutcome.NOT_A_CV.value,
                tokens_in=0,
                tokens_out=0,
                cost_usd=0.0,
            )
            return RunResult(
                status=RunStatus.SUCCEEDED,
                outcome=RunOutcome.NOT_A_CV,
                message="Failed to recognize document as a valid CV: no standard CV sections found.",
            )

        try:
            cleaned_cv = clean_cv(raw_text, source="cv", is_file=True, user=user)
        except Exception as exc:
            logger.warning("Privacy gate failed: %s", type(exc).__name__)
            log_step(
                "job_match.end",
                run_id=run_id,
                status=RunStatus.FAILED.value,
                error_code=ErrorCode.PII_REMOVAL_FAILED.value,
                tokens_in=0,
                tokens_out=0,
                cost_usd=0.0,
            )
            return RunResult(
                status=RunStatus.FAILED,
                error_code=ErrorCode.PII_REMOVAL_FAILED,
                message=f"Privacy gate removal failed: {type(exc).__name__}",
            )
    else:
        cleaned_cv = cv_text.text if hasattr(cv_text, "text") else (cv_text or "")
        set_stage("s0a_precheck")
        if not _is_cv_precheck(cleaned_cv):
            log_step(
                "job_match.end",
                run_id=run_id,
                status=RunStatus.SUCCEEDED.value,
                outcome=RunOutcome.NOT_A_CV.value,
                tokens_in=0,
                tokens_out=0,
                cost_usd=0.0,
            )
            return RunResult(
                status=RunStatus.SUCCEEDED,
                outcome=RunOutcome.NOT_A_CV,
                message="Failed to recognize document as a valid CV: no standard CV sections found.",
            )

    # -------------------------------------------------------------
    # S2: Profile Extraction
    # -------------------------------------------------------------
    set_stage("s2_profile")
    profile, outcome, p_warns = await extract_profile(
        cleaned_cv=cleaned_cv,
        budget=budget,
        user=user,
        options=options,
        parent_run_id=run_id,
    )
    for pw in p_warns:
        warnings.append({"code": pw.code, "message": pw.message})

    if outcome == RunOutcome.NOT_A_CV:
        log_step(
            "job_match.end",
            run_id=run_id,
            status=RunStatus.SUCCEEDED.value,
            outcome=RunOutcome.NOT_A_CV.value,
            tokens_in=budget.usage.total_tokens,
            tokens_out=budget.usage.output_tokens,
            cost_usd=0.0,
        )
        return RunResult(
            status=RunStatus.SUCCEEDED,
            outcome=RunOutcome.NOT_A_CV,
            message="Failed to recognize document as a valid CV.",
            profile=profile.model_dump() if hasattr(profile, "model_dump") else profile,
        )

    if outcome == RunOutcome.INSUFFICIENT_PROFILE:
        log_step(
            "job_match.end",
            run_id=run_id,
            status=RunStatus.SUCCEEDED.value,
            outcome=RunOutcome.INSUFFICIENT_PROFILE.value,
            tokens_in=budget.usage.total_tokens,
            tokens_out=budget.usage.output_tokens,
            cost_usd=0.0,
        )
        return RunResult(
            status=RunStatus.SUCCEEDED,
            outcome=RunOutcome.INSUFFICIENT_PROFILE,
            message="Candidate profile has fewer than 2 recognizable skills.",
            profile=profile.model_dump() if hasattr(profile, "model_dump") else profile,
            items=[],
        )

    # -------------------------------------------------------------
    # S3: Build Queries
    # -------------------------------------------------------------
    set_stage("s3_build_queries")
    q0, queries, lexical = build_queries(profile)

    # -------------------------------------------------------------
    # S4: Retrieval
    # -------------------------------------------------------------
    set_stage("s4_retrieval")

    if store is None:
        is_store_usable = False
    else:
        is_store_usable = store.is_usable() if hasattr(store, "is_usable") else True

    import os

    app_env = os.getenv("APP_ENV") or settings.APP_ENV
    ml_env = os.getenv("ML_ENABLED")
    is_ml = (ml_env.lower() != "false") if ml_env is not None else settings.ML_ENABLED

    # Check ML environment override
    if app_env != "test" and not is_ml:
        is_store_usable = False

    pool_rows: list[IndexRow] = []
    exhausted = False

    if is_store_usable:
        dense_queries = []
        if options.dense:
            try:
                embedder = get_embedder()
                dense_queries = embedder.embed(queries)
            except Exception:
                dense_queries = []

        dense_lists, lex_hits = await store.hybrid_search(
            dense_queries=dense_queries,
            lexical=lexical,
            criteria=criteria,
            top=options.list_size,
        )
        exhausted = compute_exhausted(dense_lists, lex_hits, list_size=options.list_size)
        fused_hits = rrf_fuse(dense_lists + [lex_hits], k=60)
        top_hits = fused_hits[: options.pool_size]
        pool_rows = await store.get_rows([h.job_id for h in top_hits])
    else:
        # Fallback to core.project.search
        warnings.append(
            {
                "code": "INDEX_UNAVAILABLE",
                "message": "Search index is unavailable; falling back to core project search.",
            }
        )
        run_status = RunStatus.PARTIAL

        candidate_skill_names = [
            s if isinstance(s, str) else s.name for s in (profile.skills or [])
        ]
        projects_map = {}
        for skill in candidate_skill_names[:5]:
            if core_rpc:
                reply = await core_rpc.call("core.project.search", {"keyword": skill})
                if reply.get("ok"):
                    paged = reply.get("data", {}).get("data", [])
                    for p in paged:
                        projects_map[p["id"]] = p

        for p in projects_map.values():
            s_rows = sanitize_project(p)
            for sr in s_rows:
                if criteria_matches(criteria, sr):
                    pool_rows.append(sr)
        exhausted = True
    state.exhausted = exhausted
    state.pool_job_ids = [r.job_id for r in pool_rows]

    # Group pool rows by project_id
    project_pool: dict[str, list[IndexRow]] = {}
    for r in pool_rows:
        project_pool.setdefault(r.project_id, []).append(r)

    # -------------------------------------------------------------
    # S5: Reranker setup
    # -------------------------------------------------------------
    set_stage("s5_rerank")
    can_rerank = options.rerank
    reranker = None
    if can_rerank:
        try:
            reranker = get_reranker()
        except Exception:
            can_rerank = False
            warnings.append(
                {
                    "code": "RERANKER_UNAVAILABLE",
                    "message": "Reranker model is unavailable; using degraded rule-based scoring.",
                }
            )
            run_status = RunStatus.PARTIAL
    else:
        warnings.append(
            {
                "code": "RERANKER_UNAVAILABLE",
                "message": "Reranker is disabled; using degraded rule-based scoring.",
            }
        )
        run_status = RunStatus.PARTIAL

    # -------------------------------------------------------------
    # S5b: Skill matching & S6 Scoring
    # -------------------------------------------------------------
    set_stage("s5b_skill_match")
    scored_projects: list[dict[str, Any]] = []
    all_pool_missing_skills: list[str] = []

    sm_sem = asyncio.Semaphore(4)

    async def _match_single_project(pid_item: str, rows: list[IndexRow]):
        async with sm_sem:
            job_skills_dict = {r.job_id: r.skills for r in rows}
            res, sm_w = await match_skills_for_project(
                project_id=pid_item,
                project_jobs=job_skills_dict,
                profile=profile,
                budget=budget,
                options=options,
                parent_run_id=run_id,
            )
            return pid_item, res, sm_w

    match_tasks = [_match_single_project(pid, p_rows) for pid, p_rows in project_pool.items()]
    matched_results_list = await asyncio.gather(*match_tasks) if match_tasks else []
    match_by_project = {pid_item: (res, sm_w) for pid_item, res, sm_w in matched_results_list}

    for pid, p_rows in project_pool.items():
        match_result, sm_warns = match_by_project[pid]
        for sm_w in sm_warns:
            if not any(w["code"] == sm_w for w in warnings):
                warnings.append({"code": sm_w, "message": "Skill matching used code fallback."})

        evaluated_jobs = []
        p_title = p_rows[0].project_title

        for r in p_rows:
            j_eval = match_result.get(r.job_id, {})
            raw_matched = j_eval.get("matched", [])
            raw_missing = j_eval.get("missing", [])
            coverage = j_eval.get("coverage", 0.0)

            all_pool_missing_skills.extend(raw_missing)

            # Reranker score
            r_score: float | None = None
            if can_rerank and reranker:
                try:
                    r_score = reranker.score(q0, r.doc_text)
                except Exception:
                    r_score = None

            # Experience match (ADR-001 / design §6)
            profile_lvl = getattr(profile, "experience_level", None)
            project_lvl = getattr(r, "experience_level", None)
            e_score = compute_experience_score(profile_lvl, project_lvl)

            m_score, fits = compute_job_score(
                r=r_score,
                c=coverage,
                e=e_score,
                reranker_available=(can_rerank and r_score is not None),
            )

            # Format matchedSkills for API / tests
            formatted_matched = []
            for m in raw_matched:
                if isinstance(m, dict):
                    formatted_matched.append(
                        {
                            "name": m.get("name", ""),
                            "inferred": m.get("source") in ("inferred", "implied"),
                        }
                    )
                else:
                    formatted_matched.append({"name": str(m), "inferred": False})

            evaluated_jobs.append(
                {
                    "job_id": r.job_id,
                    "jobId": r.job_id,
                    "title": r.job_title,
                    "salary_type": r.salary_type,
                    "salaryType": r.salary_type,
                    "budget_min": float(r.budget_min) if r.budget_min else None,
                    "budgetMin": float(r.budget_min) if r.budget_min else None,
                    "budget_max": float(r.budget_max) if r.budget_max else None,
                    "budgetMax": float(r.budget_max) if r.budget_max else None,
                    "match_score": m_score,
                    "matchScore": m_score,
                    "fits": fits,
                    "matched_skills": [
                        m["name"] if isinstance(m, dict) else str(m) for m in raw_matched
                    ],
                    "matchedSkills": formatted_matched,
                    "missing_skills": raw_missing,
                    "missingSkills": raw_missing,
                    "requirements": r.requirements or [],
                    "summary": f"Job fit score: {m_score}.",
                    "assessment": "llm",
                }
            )

        proj_score, fitting_jobs = compute_project_scores(evaluated_jobs)
        scored_projects.append(
            {
                "project_id": pid,
                "projectId": pid,
                "project_title": p_title,
                "projectTitle": p_title,
                "match_score": proj_score,
                "matchScore": proj_score,
                "jobs": evaluated_jobs,
                "has_fits": len(fitting_jobs) > 0,
            }
        )

    # -------------------------------------------------------------
    # S6: Check for fitting projects
    # -------------------------------------------------------------
    set_stage("s6_scoring")
    fitting_projects = [p for p in scored_projects if p["has_fits"]]
    state.fitting_projects_count = len(fitting_projects)
    if not fitting_projects:
        # NO_MATCH outcome
        from collections import Counter

        counter = Counter(all_pool_missing_skills)
        top_missing = [s for s, _ in counter.most_common(5)]
        tokens_in = budget.usage.input_tokens
        tokens_out = budget.usage.output_tokens
        state.tokens_in = tokens_in
        state.tokens_out = tokens_out
        cost_info = calculate_token_cost(
            settings.GLM_MODEL,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
        )
        cost_usd = cost_info.get("cost_usd", 0.0)
        state.cost_usd = cost_usd
        log_step(
            "job_match.end",
            run_id=run_id,
            status=RunStatus.SUCCEEDED.value,
            outcome=RunOutcome.NO_MATCH.value,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            cost_usd=cost_usd,
        )
        return RunResult(
            status=RunStatus.SUCCEEDED,
            outcome=RunOutcome.NO_MATCH,
            message="No suitable projects matched the candidate profile.",
            top_missing_skills=top_missing,
            items=[],
        )

    # -------------------------------------------------------------
    # S7: Search Agent (AC-15, AC-16)
    # -------------------------------------------------------------
    target_k = min(10, options.list_size) if options.list_size else 10
    if options.search_agent and len(fitting_projects) < target_k and not state.exhausted:
        set_stage("s7_search_agent")
        called, stop_reason = await maybe_search_more(
            state=state,
            budget=budget,
            options=options,
            goal=target_k,
            user=user,
            parent_run_id=run_id,
        )
        if stop_reason and stop_reason != StopReason.GOAL_REACHED:
            run_status = RunStatus.PARTIAL
            state.stop_reason = (
                stop_reason.value if hasattr(stop_reason, "value") else str(stop_reason)
            )
            if not any(w["code"] == "SEARCH_STOPPED_EARLY" for w in warnings):
                warnings.append(
                    {
                        "code": "SEARCH_STOPPED_EARLY",
                        "message": f"Search agent stopped early: {state.stop_reason}.",
                    }
                )

    # Sort descending by matchScore
    scored_projects.sort(key=lambda p: p["matchScore"], reverse=True)
    shortlisted = scored_projects[:target_k]

    # -------------------------------------------------------------
    # S8: Freshness check against core
    # -------------------------------------------------------------
    set_stage("s8_freshness")
    verified_shortlisted = shortlisted
    if core_rpc:
        v_items, f_warns, is_partial = await check_projects_freshness(
            shortlisted=shortlisted,
            rpc=core_rpc,
            limit=target_k,
            all_candidates=scored_projects,
        )
        verified_shortlisted = v_items
        for fw in f_warns:
            if not any(w["code"] == fw for w in warnings):
                warnings.append(
                    {
                        "code": fw,
                        "message": "Some projects could not be verified with core service.",
                    }
                )
        if is_partial:
            run_status = RunStatus.PARTIAL

    # Check criteria.hours_per_day warning HOURS_UNKNOWN (AC-11)
    if criteria.hours_per_day is not None:
        has_unknown_hours = False
        for p in verified_shortlisted:
            pid = p.get("project_id") or p.get("projectId")
            p_rows = project_pool.get(pid, [])
            if any(r.hours_per_day is None for r in p_rows):
                has_unknown_hours = True
                break
        if has_unknown_hours and not any(w["code"] == "HOURS_UNKNOWN" for w in warnings):
            warnings.append(
                {
                    "code": "HOURS_UNKNOWN",
                    "message": "Hours-per-day filter set, but some matched projects have unknown hours.",
                }
            )

    # -------------------------------------------------------------
    # S9: Fit Assessment
    # -------------------------------------------------------------
    set_stage("s9_assessment")
    assessed_projects = verified_shortlisted
    if verified_shortlisted:
        a_projects, a_warns = await assess_shortlisted_projects(
            shortlisted=verified_shortlisted,
            profile=profile,
            lang=lang,
            parent_run_id=run_id,
        )
        assessed_projects = a_projects
        for aw in a_warns:
            if not any(w["code"] == aw for w in warnings):
                warnings.append({"code": aw, "message": "Fit assessment used fallback logic."})

    # -------------------------------------------------------------
    # S10: Finalization & formatting
    # -------------------------------------------------------------
    set_stage("s10_finalize")
    final_items: list[dict[str, Any]] = []

    for rank, p in enumerate(assessed_projects[:target_k], start=1):
        formatted_jobs = []
        for j in p.get("jobs", []):
            raw_req_checks = j.get("requirement_checks") or []
            req_checks = []
            for rc in raw_req_checks:
                req_checks.append(
                    {
                        "text": rc.get("text", ""),
                        "status": rc.get("status", "unclear"),
                        "note": rc.get("note", ""),
                    }
                )
            asmt_mode = j.get("assessment", "llm" if req_checks else "rules")
            formatted_jobs.append(
                {
                    "jobId": j.get("job_id") or j.get("jobId"),
                    "title": j.get("title", ""),
                    "salaryType": j.get("salary_type") or j.get("salaryType"),
                    "budgetMin": j.get("budget_min") or j.get("budgetMin"),
                    "budgetMax": j.get("budget_max") or j.get("budgetMax"),
                    "matchScore": j.get("match_score") or j.get("matchScore", 0),
                    "matchedSkills": j.get("matchedSkills") or j.get("matched_skills", []),
                    "missingSkills": j.get("missingSkills") or j.get("missing_skills", []),
                    "requirements": req_checks,
                    "summary": j.get("summary", ""),
                    "assessment": asmt_mode,
                }
            )

        final_items.append(
            {
                "rank": rank,
                "projectId": p.get("project_id") or p.get("projectId"),
                "projectTitle": p.get("project_title") or p.get("projectTitle", ""),
                "matchScore": p.get("match_score") or p.get("matchScore", 0),
                "verified": p.get("verified", True),
                "jobs": formatted_jobs,
            }
        )

    # Validator V3: drop jobs and projects that fail criteria
    final_items = validate_v3_criteria(final_items, criteria)

    # Update state
    tokens_in = budget.usage.input_tokens
    tokens_out = budget.usage.output_tokens
    state.tokens_in = tokens_in
    state.tokens_out = tokens_out
    cost_info = calculate_token_cost(
        settings.GLM_MODEL,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
    )
    cost_usd = cost_info.get("cost_usd", 0.0)
    state.cost_usd = cost_usd

    log_step(
        "job_match.end",
        run_id=run_id,
        status=run_status.value,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=cost_usd,
    )

    from app.agents.subagent import get_skill_registry

    registry = get_skill_registry()
    skill_versions: dict[str, str] = {}
    for sk in ["extract-candidate-profile", "match-skills", "assess-job-fit", "plan-job-search"]:
        meta = registry.get(sk)
        if meta and meta.skill_version:
            skill_versions[sk] = meta.skill_version

    return RunResult(
        status=run_status,
        outcome=RunOutcome.OK,
        warnings=[JobMatchWarning(code=w["code"], message=w["message"]) for w in warnings],
        items=final_items,
        profile=profile.model_dump() if hasattr(profile, "model_dump") else profile,
        skill_versions=skill_versions,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=cost_usd,
    )


run = run_pipeline
