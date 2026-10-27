import asyncio
import logging
from decimal import Decimal
from typing import Any

from pydantic_ai import RunContext
from pydantic_ai.exceptions import ModelRetry

from app.agents.deps import AgentDeps
from app.core.config import get_settings
from app.core.logging import log_step
from app.db.repositories.chat import ChatRepository
from app.documents.cv_text import CvText, get_cv_text
from app.features.job_match.index import index_state, models_loaded
from app.features.job_match.pipeline import _is_cv_precheck, run_pipeline
from app.features.job_match.ports import MatchCriteria, PipelineOptions, RunState
from app.features.job_match.schemas import (
    ExperienceLevelFilter,
    HoursPerDayFilter,
    SalaryTypeFilter,
)
from app.messaging.core_client import get_core_rpc

logger = logging.getLogger(__name__)


def _format_skills(skills: list[Any]) -> str:
    if not skills:
        return "Đang cập nhật"
    formatted: list[str] = []
    for s in skills:
        if isinstance(s, dict):
            name = s.get("name") or s.get("skill") or s.get("title") or ""
            if name:
                formatted.append(str(name))
        elif s:
            formatted.append(str(s))
    return ", ".join(formatted) if formatted else "Đang cập nhật"


def _format_salary(j: dict[str, Any] | Any) -> str:
    if isinstance(j, dict):
        b_min = j.get("budgetMin") or j.get("budget_min")
        b_max = j.get("budgetMax") or j.get("budget_max")
        s_type = j.get("salaryType") or j.get("salary_type")
        raw_sal = j.get("salary")
    else:
        b_min = getattr(j, "budget_min", None) or getattr(j, "budgetMin", None)
        b_max = getattr(j, "budget_max", None) or getattr(j, "budgetMax", None)
        s_type = getattr(j, "salary_type", None) or getattr(j, "salaryType", None)
        raw_sal = getattr(j, "salary", "")

    if raw_sal:
        return str(raw_sal)

    try:
        f_min = float(b_min) if b_min is not None else None
        f_max = float(b_max) if b_max is not None else None
    except (ValueError, TypeError):
        f_min, f_max = None, None

    if f_min is not None or f_max is not None:
        if f_min is not None and f_max is not None:
            sal_str = f"{f_min:,.0f} - {f_max:,.0f} VND"
        elif f_min is not None:
            sal_str = f"Từ {f_min:,.0f} VND"
        else:
            sal_str = f"Đến {f_max:,.0f} VND"
        if s_type:
            sal_str += f" ({s_type})"
        return sal_str

    return ""


def render_job_match_markdown(
    items: list[Any],
    criteria_applied: dict[str, Any],
    warnings: list[Any],
    outcome: str,
    lang: str = "vi",
) -> str:
    """Renders a deterministic Markdown block for job match results in vi or en."""
    is_vi = lang.lower() == "vi"

    lines: list[str] = ["\n"]

    if outcome == "NEED_CV":
        lines.append(
            "> ⚠️ **Vui lòng đính kèm CV (PDF)** để mình có thể phân tích kỹ năng và tìm kiếm công việc phù hợp nhất cho bạn."
            if is_vi
            else "> ⚠️ **Please attach your CV (PDF)** so I can analyze your skills and find the best matching jobs for you."
        )
        return "\n".join(lines) + "\n"

    if outcome == "MODELS_LOADING":
        lines.append(
            "> ⏳ **Hệ thống AI đang tải mô hình tính toán**, vui lòng đợi trong giây lát và thử lại."
            if is_vi
            else "> ⏳ **AI models are currently loading**, please wait a moment and try again."
        )
        return "\n".join(lines) + "\n"

    if outcome == "INDEX_UNAVAILABLE":
        lines.append(
            "> ⚠️ **Hệ thống dữ liệu việc làm hiện chưa sẵn sàng**. Vui lòng liên hệ quản trị viên."
            if is_vi
            else "> ⚠️ **Job search index is currently unavailable**. Please contact the administrator."
        )
        return "\n".join(lines) + "\n"

    if outcome == "RUN_TIMEOUT":
        lines.append(
            "> ⏱️ **Quá trình tìm kiếm việc làm vượt quá thời gian cho phép**. Vui lòng thử lại với các tiêu chí cụ thể hơn."
            if is_vi
            else "> ⏱️ **Job search timed out**. Please try again with more specific criteria."
        )
        return "\n".join(lines) + "\n"

    if not items or outcome == "NO_MATCH":
        lines.append(
            "### Kết quả tìm kiếm công việc phù hợp\n\nKhông tìm thấy công việc nào phù hợp với CV và tiêu chí đã chọn."
            if is_vi
            else "### Matching Job Opportunities\n\nNo suitable jobs found matching your CV and the specified criteria."
        )
        return "\n".join(lines) + "\n"

    # Header
    lines.append(
        "### 🎯 Danh sách công việc phù hợp nhất với hồ sơ của bạn\n"
        if is_vi
        else "### 🎯 Best Matching Job Opportunities for Your Profile\n"
    )

    for idx, item in enumerate(items, start=1):
        if isinstance(item, dict):
            rank = item.get("rank", idx)
            score = item.get("matchScore") or item.get("match_score") or item.get("score", 0.0)
            proj_title = item.get("projectTitle") or item.get("project_title", "Dự án")
            jobs = item.get("jobs", [])
            if jobs:
                for j in jobs:
                    j_title = j.get("title") or j.get("job_title", "Vị trí tuyển dụng")
                    j_score = j.get("matchScore") or j.get("match_score", score)
                    pct = int(round(j_score * 100)) if j_score <= 1.0 else int(round(j_score))
                    salary = _format_salary(j)
                    skills = j.get("matchedSkills") or j.get("matched_skills") or j.get("skills", [])
                    skills_str = _format_skills(skills)
                    assessment = j.get("summary") or j.get("assessment", "")

                    if is_vi:
                        lines.append(f"#### {rank}. {j_title} — {proj_title} (Độ phù hợp: {pct}%)")
                        if salary:
                            lines.append(f"- **Ngân sách / Lương:** {salary}")
                        lines.append(f"- **Kỹ năng phù hợp:** {skills_str}")
                        if assessment:
                            lines.append(f"- **Đánh giá:** {assessment}")
                    else:
                        lines.append(f"#### {rank}. {j_title} — {proj_title} (Match: {pct}%)")
                        if salary:
                            lines.append(f"- **Budget / Salary:** {salary}")
                        lines.append(f"- **Matched Skills:** {skills_str}")
                        if assessment:
                            lines.append(f"- **Assessment:** {assessment}")
                    lines.append("")
            else:
                pct = int(round(score * 100)) if score <= 1.0 else int(round(score))
                job_title = item.get("job_title") or item.get("title", "Vị trí tuyển dụng")
                salary = _format_salary(item)
                skills = item.get("matched_skills") or item.get("skills", [])
                skills_str = _format_skills(skills)
                assessment = item.get("assessment", "")

                if is_vi:
                    lines.append(f"#### {rank}. {job_title} — {proj_title} (Độ phù hợp: {pct}%)")
                    if salary:
                        lines.append(f"- **Ngân sách / Lương:** {salary}")
                    lines.append(f"- **Kỹ năng phù hợp:** {skills_str}")
                    if assessment:
                        lines.append(f"- **Đánh giá:** {assessment}")
                else:
                    lines.append(f"#### {rank}. {job_title} — {proj_title} (Match: {pct}%)")
                    if salary:
                        lines.append(f"- **Budget / Salary:** {salary}")
                    lines.append(f"- **Matched Skills:** {skills_str}")
                    if assessment:
                        lines.append(f"- **Assessment:** {assessment}")
                lines.append("")
        else:
            rank = getattr(item, "rank", idx)
            score = getattr(item, "score", 0.0) or getattr(item, "match_score", 0.0)
            pct = int(round(score * 100)) if score <= 1.0 else int(round(score))
            job_title = getattr(item, "job_title", "Vị trí tuyển dụng")
            proj_title = getattr(item, "project_title", "Dự án")
            salary = _format_salary(item)
            skills = getattr(item, "matched_skills", []) or getattr(item, "skills", [])
            skills_str = _format_skills(skills)
            assessment = getattr(item, "assessment", "")

            if is_vi:
                lines.append(f"#### {rank}. {job_title} — {proj_title} (Độ phù hợp: {pct}%)")
                if salary:
                    lines.append(f"- **Ngân sách / Lương:** {salary}")
                lines.append(f"- **Kỹ năng phù hợp:** {skills_str}")
                if assessment:
                    lines.append(f"- **Đánh giá:** {assessment}")
            else:
                lines.append(f"#### {rank}. {job_title} — {proj_title} (Match: {pct}%)")
                if salary:
                    lines.append(f"- **Budget / Salary:** {salary}")
                lines.append(f"- **Matched Skills:** {skills_str}")
                if assessment:
                    lines.append(f"- **Assessment:** {assessment}")
            lines.append("")

    return "\n".join(lines) + "\n"


async def _find_candidate_cv(
    ctx: RunContext[AgentDeps],
) -> CvText | None:
    """Finds the newest valid CV from current turn's documents or earlier session turns."""
    # 1. Check current turn documents first (newest first)
    for sha in reversed(ctx.deps.turn_documents):
        cv_obj = await get_cv_text(sha, session=ctx.deps.db)
        if cv_obj and _is_cv_precheck(cv_obj.text):
            return cv_obj

    # 2. Check previous turns of the same session and user
    if ctx.deps.session_id and ctx.deps.db:
        chat_repo = ChatRepository(ctx.deps.db)
        messages, _ = await chat_repo.get_messages(
            ctx.deps.session_id, ctx.deps.user.user_id, page=1, limit=50
        )
        for msg in reversed(messages):
            for att in reversed(msg.attachments or []):
                if isinstance(att, dict):
                    sha = att.get("sha256")
                    if sha:
                        cv_obj = await get_cv_text(sha, session=ctx.deps.db)
                        if cv_obj and _is_cv_precheck(cv_obj.text):
                            return cv_obj

    return None


async def match_jobs_for_cv(
    ctx: RunContext[AgentDeps],
    salary_type: SalaryTypeFilter | None = None,
    min_budget: Decimal | None = None,
    max_budget: Decimal | None = None,
    experience_level: ExperienceLevelFilter | None = None,
    hours_per_day: HoursPerDayFilter | None = None,
    lang: str = "vi",
) -> dict[str, Any]:
    """Matches candidate CV against open recruiting jobs using the hybrid matching pipeline.

    Call this tool whenever the user asks to find, match, or recommend jobs for their CV or profile.
    Write one short preamble line BEFORE calling this tool. Do NOT re-list or score jobs in your text;
    the formatted list of matching opportunities will be appended automatically.
    """
    # 1. Idempotent per-turn memo
    if ctx.deps.job_match_memo is not None:
        return ctx.deps.job_match_memo

    # 2. Criteria validation
    if min_budget is not None and max_budget is not None and min_budget > max_budget:
        raise ModelRetry("min_budget cannot be greater than max_budget. Please correct the budget range.")

    criteria_applied: dict[str, Any] = {}
    if salary_type is not None:
        criteria_applied["salary_type"] = salary_type.value
    if min_budget is not None:
        criteria_applied["min_budget"] = float(min_budget)
    if max_budget is not None:
        criteria_applied["max_budget"] = float(max_budget)
    if experience_level is not None:
        criteria_applied["experience_level"] = experience_level.value
    if hours_per_day is not None:
        criteria_applied["hours_per_day"] = hours_per_day.value

    # 3. Locate CV text
    cv_obj = await _find_candidate_cv(ctx)
    if cv_obj is None:
        summary = {
            "outcome": "NEED_CV",
            "itemCount": 0,
            "warnings": ["NEED_CV"],
            "topMissingSkills": [],
            "criteriaApplied": criteria_applied,
            "items": [],
        }
        ctx.deps.job_match_memo = summary
        ctx.deps.job_match_block = render_job_match_markdown([], criteria_applied, [], "NEED_CV", lang=lang)
        return summary

    # 4. Readiness checks
    if not models_loaded():
        summary = {
            "outcome": "MODELS_LOADING",
            "itemCount": 0,
            "warnings": ["MODELS_LOADING"],
            "topMissingSkills": [],
            "criteriaApplied": criteria_applied,
            "items": [],
        }
        ctx.deps.job_match_memo = summary
        ctx.deps.job_match_block = render_job_match_markdown([], criteria_applied, [], "MODELS_LOADING", lang=lang)
        return summary

    idx_st = await index_state(session=ctx.deps.db)
    if idx_st != "ok":
        summary = {
            "outcome": "INDEX_UNAVAILABLE",
            "itemCount": 0,
            "warnings": ["INDEX_UNAVAILABLE"],
            "topMissingSkills": [],
            "criteriaApplied": criteria_applied,
            "items": [],
        }
        ctx.deps.job_match_memo = summary
        ctx.deps.job_match_block = render_job_match_markdown([], criteria_applied, [], "INDEX_UNAVAILABLE", lang=lang)
        return summary

    # 5. Progress handler
    def on_stage(stage: str) -> None:
        if ctx.deps.on_progress:
            if asyncio.iscoroutinefunction(ctx.deps.on_progress):
                asyncio.create_task(ctx.deps.on_progress(stage))
            else:
                ctx.deps.on_progress(stage)

    # 6. Execute pipeline with deadline
    settings = get_settings()
    criteria = MatchCriteria(
        salary_type=salary_type,
        min_budget=min_budget,
        max_budget=max_budget,
        experience_level=experience_level,
        hours_per_day=hours_per_day,
    )
    state = RunState()

    try:
        async with asyncio.timeout(settings.JOB_MATCH_TOOL_TIMEOUT_S):
            run_res = await run_pipeline(
                state=state,
                cv_text=cv_obj,
                user=ctx.deps.user,
                criteria=criteria,
                core_rpc=ctx.deps.rpc or get_core_rpc(),
                options=PipelineOptions(),
                on_stage=on_stage,
            )
    except TimeoutError:
        summary = {
            "outcome": "RUN_TIMEOUT",
            "itemCount": 0,
            "warnings": ["RUN_TIMEOUT"],
            "topMissingSkills": [],
            "criteriaApplied": criteria_applied,
            "items": [],
        }
        ctx.deps.job_match_memo = summary
        ctx.deps.job_match_block = render_job_match_markdown([], criteria_applied, [], "RUN_TIMEOUT", lang=lang)
        return summary
    except Exception as exc:
        logger.exception("Error executing match_jobs_for_cv: %s", exc)
        summary = {
            "outcome": "INTERNAL_ERROR",
            "itemCount": 0,
            "warnings": ["INTERNAL_ERROR"],
            "topMissingSkills": [],
            "criteriaApplied": criteria_applied,
            "items": [],
        }
        ctx.deps.job_match_memo = summary
        ctx.deps.job_match_block = render_job_match_markdown([], criteria_applied, [], "INTERNAL_ERROR", lang=lang)
        return summary

    # 7. Telemetry & token accounting
    ctx.deps.pipeline_tokens_in += run_res.tokens_in
    ctx.deps.pipeline_tokens_out += run_res.tokens_out
    log_step(
        "job_match.end",
        run_id=state.run_id,
        parent_run_id=ctx.deps.parent_run_id,
        status=run_res.status.value if hasattr(run_res.status, "value") else str(run_res.status),
        outcome=run_res.outcome.value if hasattr(run_res.outcome, "value") else str(run_res.outcome),
        tokens_in=run_res.tokens_in,
        tokens_out=run_res.tokens_out,
        cost_usd=run_res.cost_usd,
    )

    # 8. Render markdown block
    outcome_str = run_res.outcome.value if hasattr(run_res.outcome, "value") else str(run_res.outcome or "MATCH_FOUND")
    block = render_job_match_markdown(
        items=run_res.items,
        criteria_applied=criteria_applied,
        warnings=run_res.warnings,
        outcome=outcome_str,
        lang=lang,
    )
    ctx.deps.job_match_block = block

    # 9. Return model summary (IDs only, no titles, scores, or CV text)
    item_summaries = [
        {
            "rank": it.get("rank", idx) if isinstance(it, dict) else getattr(it, "rank", idx),
            "projectId": it.get("projectId") or it.get("project_id", "") if isinstance(it, dict) else (getattr(it, "project_id", None) or getattr(it, "projectId", "")),
        }
        for idx, it in enumerate(run_res.items, start=1)
    ]
    missing_skills = [
        m.get("name") or str(m) if isinstance(m, dict) else str(m)
        for m in (run_res.missing_skills or [])[:5]
    ]
    warnings_list = [
        w.get("code") if isinstance(w, dict) else str(w) for w in (run_res.warnings or [])
    ]

    summary = {
        "outcome": outcome_str,
        "itemCount": len(run_res.items),
        "warnings": warnings_list,
        "topMissingSkills": missing_skills,
        "criteriaApplied": criteria_applied,
        "items": item_summaries,
    }
    ctx.deps.job_match_memo = summary
    return summary
