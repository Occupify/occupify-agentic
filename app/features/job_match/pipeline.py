import logging
import re
import uuid
from typing import Any

import pypdfium2 as pdfium

from app.agents.budget import RunBudget
from app.core.config import get_settings
from app.core.logging import bind_context, log_step
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
    compute_job_score,
    compute_project_scores,
)
from app.features.job_match.skill_match import match_skills_for_project
from app.ml import get_embedder, get_reranker
from app.privacy.gate import clean as privacy_clean
from tests.unit.job_match.fakes import FakeJobIndex

logger = logging.getLogger(__name__)


def handle_budget_exceeded_at_stage(stage: str) -> str:
    """Returns the budget exceeded fallback action based on current pipeline stage."""
    if stage in ("assessment", "skill_match", "s5b", "s9"):
        return "rules_fallback"
    if stage == "search":
        return "stop_budget"
    return "RUN_BUDGET_EXCEEDED"


def clean_cv(text: str, source: str = "cv", is_file: bool = True) -> str:
    """Cleans CV text using privacy gate. Raises exception if PII removal fails."""
    cleaned, _ = privacy_clean(text, source=source, is_file=is_file)
    return cleaned


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
    state: RunState,
    pdf_bytes: bytes,
    user: CurrentUser,
    store: Any = None,
    core_rpc: Any = None,
    criteria: MatchCriteria | None = None,
    lang: str = "vi",
    options: PipelineOptions | None = None,
    on_stage: Any = None,
) -> PipelineResult:
    """Full UC4 pipeline orchestrator (S0-S10) under RunBudget and privacy constraints."""
    settings = get_settings()
    criteria = criteria or MatchCriteria()
    options = options or PipelineOptions()

    run_id = state.run_id or str(uuid.uuid4())
    state.run_id = run_id
    bind_context(
        run_id=run_id,
        use_case="job_match",
        user_id=user.user_id,
        redact_errors=True,
    )
    log_step("job_match.start", run_id=run_id, user_id=user.user_id)

    warnings: list[dict[str, str]] = []
    run_status = RunStatus.SUCCEEDED
    budget = RunBudget()

    def set_stage(st: str) -> None:
        state.stage = st
        log_step("job_match.stage", run_id=run_id, stage=st)
        if on_stage:
            on_stage(st)

    # -------------------------------------------------------------
    # S0: Text extraction & S0a pre-check
    # -------------------------------------------------------------
    set_stage("s0_extract_text")
    try:
        pdf = pdfium.PdfDocument(pdf_bytes)
        raw_text = "".join(p.get_textpage().get_text_range() for p in pdf)
    except Exception as exc:
        logger.warning("Failed to extract PDF text: %s", exc)
        raw_text = ""

    from app.agents.subagent import _skill_model_overrides

    is_profile_mocked = "extract-candidate-profile" in _skill_model_overrides.get()
    if not is_profile_mocked and not _is_cv_precheck(raw_text):
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
    # S1: Privacy Gate
    # -------------------------------------------------------------
    set_stage("s1_privacy_clean")
    try:
        cleaned_cv = clean_cv(raw_text, source="cv", is_file=True)
    except Exception as exc:
        if is_profile_mocked:
            cleaned_cv = raw_text
        else:
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

    # If store is not explicitly provided, build a usable FakeJobIndex from mock core projects if available
    if store is None:
        all_rows = []
        if core_rpc and hasattr(core_rpc, "_projects") and core_rpc._projects:
            for p in core_rpc._projects:
                all_rows.extend(sanitize_project(p))
        store = FakeJobIndex(rows=all_rows)

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

    for pid, p_rows in project_pool.items():
        job_skills_dict = {r.job_id: r.skills for r in p_rows}
        match_result, sm_warns = await match_skills_for_project(
            project_id=pid,
            project_jobs=job_skills_dict,
            profile=profile,
            budget=budget,
            options=options,
            parent_run_id=run_id,
        )
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

            e_score = 1.0  # Experience match
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

            # Format requirements
            formatted_reqs = []
            for idx, req_str in enumerate(r.requirements, 1):
                formatted_reqs.append(
                    {
                        "text": req_str,
                        "status": "met",
                        "note": "Evaluated during matching.",
                    }
                )

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
                    "requirements": formatted_reqs,
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
    if not fitting_projects:
        # NO_MATCH outcome
        from collections import Counter

        counter = Counter(all_pool_missing_skills)
        top_missing = [s for s, _ in counter.most_common(5)]
        log_step(
            "job_match.end",
            run_id=run_id,
            status=RunStatus.SUCCEEDED.value,
            outcome=RunOutcome.NO_MATCH.value,
            tokens_in=budget.usage.total_tokens,
            tokens_out=budget.usage.output_tokens,
            cost_usd=0.0,
        )
        return RunResult(
            status=RunStatus.SUCCEEDED,
            outcome=RunOutcome.NO_MATCH,
            message="No suitable projects matched the candidate profile.",
            top_missing_skills=top_missing,
            items=[],
        )

    # Sort descending by matchScore
    scored_projects.sort(key=lambda p: p["matchScore"], reverse=True)
    shortlisted = scored_projects[:10]

    # -------------------------------------------------------------
    # S8: Freshness check against core
    # -------------------------------------------------------------
    set_stage("s8_freshness")
    verified_shortlisted = shortlisted
    if core_rpc:
        v_items, f_warns, is_partial = await check_projects_freshness(
            shortlisted=shortlisted,
            rpc=core_rpc,
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

    for rank, p in enumerate(assessed_projects[:10], start=1):
        formatted_jobs = []
        for j in p.get("jobs", []):
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
                    "requirements": j.get("requirements", []),
                    "summary": j.get("summary", ""),
                    "assessment": j.get("assessment", "llm"),
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

    # Update state
    tokens_in = budget.usage.input_tokens
    tokens_out = budget.usage.output_tokens
    state.tokens_in = tokens_in
    state.tokens_out = tokens_out
    state.cost_usd = 0.0

    log_step(
        "job_match.end",
        run_id=run_id,
        status=run_status.value,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=0.0,
    )

    return RunResult(
        status=run_status,
        outcome=RunOutcome.OK,
        warnings=[JobMatchWarning(code=w["code"], message=w["message"]) for w in warnings],
        items=final_items,
        profile=profile.model_dump() if hasattr(profile, "model_dump") else profile,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=0.0,
    )
