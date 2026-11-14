"""Agent tool and helpers to finalize approved CV revisions and compile PDF."""

import re
from typing import Any, Literal

from pydantic import BaseModel
from pydantic_ai import RunContext
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.deps import AgentDeps
from app.core.config import get_settings
from app.core.logging import log_step
from app.core.storage import LocalArtifactStorage
from app.db.models import CvImprovementSession
from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)
from app.features.cv_generator.remote_compiler import ResilientCvCompiler
from app.features.cv_generator.schemas import (
    AdditionalItem,
    AdditionalSection,
    Certification,
    CvContent,
    Education,
    Experience,
    GenerateCvInput,
    GenerateCvResult,
    Project,
    SkillGroup,
)
from app.features.cv_generator.service import CvGeneratorService
from app.features.cv_generator.storage import create_s3_storage
from app.features.cv_improvement.workflow import CvImprovementWorkflow
from app.state.schemas import TaskStateUpdate
from app.state.task_progress import TaskProgressManager


def _normalize_additional_items(raw_items: list[Any]) -> list[AdditionalItem]:
    """Helper to convert heterogeneous item formats into AdditionalItem models."""
    items: list[AdditionalItem] = []
    for it in raw_items:
        if isinstance(it, BaseModel):
            it = it.model_dump()
        if isinstance(it, dict):
            text = it.get("text") or it.get("description") or str(it)
            items.append(AdditionalItem(label=it.get("label") or it.get("title"), text=str(text)))
        elif isinstance(it, str) and it.strip():
            lbl, has_colon, txt = it.partition(":")
            items.append(
                AdditionalItem(
                    label=lbl.strip() if has_colon else None,
                    text=txt.strip() if has_colon else it.strip(),
                )
            )
    return items[:30]


def _parse_dates(period: str | None) -> tuple[str | None, str | None, bool]:
    """Parse start_date, end_date, is_current from a loose period string."""
    if not period or not (matches := re.findall(r"\b\d{4}(?:-\d{2})?\b", period)):
        return "2024", None, True

    is_current = any(kw in period.lower() for kw in ("present", "hiện", "nay", "current", "now"))
    if len(matches) == 1 or is_current:
        return matches[0], None, True

    start, end = sorted(matches[:2])
    return start, end, False


def resume_data_to_cv_content(
    raw_data: dict[str, Any] | BaseModel,
    language: Literal["vi", "en"] = "en",
) -> CvContent:
    """Convert raw resume dictionary or ResumeData model into strict CvContent."""
    data = raw_data.model_dump() if isinstance(raw_data, BaseModel) else dict(raw_data)

    # If data is already in CvContent format
    if "skill_groups" in data and "experience" in data:
        return CvContent.model_validate(data)

    is_en = language == "en"
    headline = data.get("title") or data.get("full_name") or ("Candidate" if is_en else "Ứng viên")
    summary = data.get("summary") or (
        "Experienced professional dedicated to delivering high-impact results."
        if is_en
        else "Chuyên viên giàu kinh nghiệm và trách nhiệm."
    )

    # Skills mapping
    raw_skills = data.get("skills") or []
    skill_label = "Technical Skills" if is_en else "Kỹ năng chuyên môn"
    if isinstance(raw_skills, list) and raw_skills:
        skill_groups = [
            SkillGroup(
                label=skill_label,
                items=[str(s) for s in raw_skills if str(s).strip()][:30] or [skill_label],
            )
        ]
    else:
        skill_groups = [SkillGroup(label=skill_label, items=[skill_label])]

    # Experience mapping
    raw_exp = data.get("experiences") or []
    experiences = []
    for exp in raw_exp:
        role = exp.get("role") or ("Role" if is_en else "Vai trò")
        company = exp.get("company") or ("Company" if is_en else "Công ty")
        period = exp.get("period")
        start_date, end_date, is_current = _parse_dates(period)
        bullets = [b for b in (exp.get("bullet_points") or []) if b.strip()]
        if not bullets:
            bullets = [
                "Responsible for core development and project deliverables."
                if is_en
                else "Đảm nhiệm các công việc chuyên môn và dự án theo yêu cầu."
            ]

        experiences.append(
            Experience(
                company=company,
                roles=[role],
                employment_type=None,
                location=None,
                start_date=start_date,
                end_date=end_date if not is_current else None,
                is_current=is_current,
                team_size=None,
                bullets=bullets[:30],
            )
        )

    # Project mapping
    raw_proj = data.get("projects") or []
    projects = []
    for proj in raw_proj:
        name = proj.get("name") or ("Project" if is_en else "Dự án")
        role = proj.get("role") or ("Role" if is_en else "Vai trò")
        tech = proj.get("tech_stack") or (["Technologies"] if is_en else ["Công nghệ"])
        bullets = [b for b in (proj.get("bullet_points") or []) if b.strip()]
        if not bullets:
            bullets = [
                "Participated in system architecture, implementation, and optimization."
                if is_en
                else "Tham gia thiết kế, phát triển và tối ưu hóa hệ thống."
            ]

        projects.append(
            Project(
                name=name,
                roles=[role],
                technologies=[t for t in tech if t.strip()][:30]
                or (["Technologies"] if is_en else ["Công nghệ"]),
                start_date="2024",
                end_date=None,
                is_current=False,
                team_size=None,
                bullets=bullets[:30],
            )
        )

    # Education mapping
    raw_edu = data.get("education") or []
    education = []
    for edu in raw_edu:
        inst = edu.get("institution") or ("University" if is_en else "Đại học")
        degree = edu.get("degree") or ("Bachelor" if is_en else "Cử nhân")
        period = edu.get("period")
        start_date, end_date, is_current = _parse_dates(period)

        education.append(
            Education(
                institution=inst,
                degree=degree,
                major=None,
                location=None,
                start_date=start_date,
                end_date=end_date if not is_current else None,
                is_current=False,
                is_expected=False,
                gpa=None,
                highlights=[],
            )
        )

    # Certifications mapping
    raw_certs = data.get("certifications") or data.get("certificates") or []
    certifications = []
    for cert in raw_certs:
        if isinstance(cert, BaseModel):
            cert = cert.model_dump()
        if isinstance(cert, dict):
            name = cert.get("name") or cert.get("title")
            if name:
                certifications.append(
                    Certification(
                        name=str(name),
                        issuer=cert.get("issuer"),
                        issued_date=cert.get("issued_date")
                        or cert.get("issue_date")
                        or cert.get("date"),
                        expiry_date=cert.get("expiry_date"),
                        result=cert.get("result"),
                    )
                )
        elif isinstance(cert, str) and cert.strip():
            certifications.append(
                Certification(
                    name=cert.strip(),
                    issuer=None,
                    issued_date=None,
                    expiry_date=None,
                    result=None,
                )
            )

    # Additional sections mapping
    additional_sections: list[AdditionalSection] = []
    for sec in data.get("additional_sections") or []:
        s = sec.model_dump() if isinstance(sec, BaseModel) else sec
        if isinstance(s, dict) and (title := s.get("title")):
            if items := _normalize_additional_items(s.get("items") or []):
                additional_sections.append(AdditionalSection(title=str(title), items=items))

    # Auto-extract well-known extra sections if present in raw_data
    extra_field_titles = [
        ("engineering_practices", "ENGINEERING PRACTICES" if is_en else "THỰC HÀNH KỸ THUẬT"),
        ("awards", "AWARDS & HONORS" if is_en else "GIẢI THƯỞNG"),
        ("activities", "ACTIVITIES" if is_en else "HOẠT ĐỘNG"),
        ("languages", "LANGUAGES" if is_en else "NGOẠI NGỮ"),
        ("publications", "PUBLICATIONS" if is_en else "CÔNG TRÌNH NGHIÊN CỨU"),
    ]
    for field_key, default_title in extra_field_titles:
        if (extra_val := data.get(field_key)) and isinstance(extra_val, list):
            if sec_items := _normalize_additional_items(extra_val):
                additional_sections.append(AdditionalSection(title=default_title, items=sec_items))

    return CvContent(
        headline=headline,
        summary=summary,
        skill_groups=skill_groups,
        experience=experiences,
        projects=projects,
        education=education,
        certifications=certifications,
        additional_sections=additional_sections,
    )


def _get_cv_generator_service(deps: AgentDeps | None = None) -> CvGeneratorService:
    """Resolve CvGeneratorService with S3 storage or local fallback."""
    if deps and deps.cv_generator_service:
        return deps.cv_generator_service

    settings = get_settings()

    # Storage: Prefer OCI/S3, fallback to LocalArtifactStorage
    try:
        storage = create_s3_storage(settings)
    except Exception:
        storage = LocalArtifactStorage(ttl_seconds=settings.CV_GENERATOR_LINK_TTL_S)

    compiler = ResilientCvCompiler(settings.CV_COMPILER_URL)

    service = CvGeneratorService(compiler, storage, timeout_s=settings.CV_GENERATOR_TIMEOUT_S)
    if deps:
        deps.cv_generator_service = service
    return service


async def _resolve_latest_session_id(
    ctx: RunContext[AgentDeps],
    candidate_id: str | None = None,
) -> str | None:
    """Finds the active CvImprovementSession ID for this chat turn or candidate ID.

    Handles candidate_id being either a CvImprovementSession.id or a chat_session_id,
    with fallback to current turn's chat_session_id or latest user CV session.
    """
    if not ctx.deps.db or not ctx.deps.user or not ctx.deps.user.user_id:
        return None

    user_id = ctx.deps.user.user_id

    # 1. If candidate_id is provided, check if it directly matches a CvImprovementSession.id
    if candidate_id and candidate_id.strip():
        cid = candidate_id.strip()
        stmt_direct = select(CvImprovementSession.id).where(
            CvImprovementSession.id == cid,
            CvImprovementSession.user_id == user_id,
        )
        res = await ctx.deps.db.execute(stmt_direct)
        if found := res.scalar_one_or_none():
            return str(found)

        # Candidate might be a chat_session_id
        stmt_chat = (
            select(CvImprovementSession.id)
            .where(
                CvImprovementSession.chat_session_id == cid,
                CvImprovementSession.user_id == user_id,
            )
            .order_by(desc(CvImprovementSession.updated_at))
            .limit(1)
        )
        res = await ctx.deps.db.execute(stmt_chat)
        if found := res.scalar_one_or_none():
            return str(found)

    # 2. Check current turn's chat_session_id
    if ctx.deps.session_id:
        chat_stmt = (
            select(CvImprovementSession.id)
            .where(
                CvImprovementSession.chat_session_id == ctx.deps.session_id,
                CvImprovementSession.user_id == user_id,
            )
            .order_by(desc(CvImprovementSession.updated_at))
            .limit(1)
        )
        res = await ctx.deps.db.execute(chat_stmt)
        found_id = res.scalar_one_or_none()
        if found_id:
            return str(found_id)

    # 3. Fall back to user's most recent CV session
    stmt = (
        select(CvImprovementSession.id)
        .where(CvImprovementSession.user_id == user_id)
        .order_by(desc(CvImprovementSession.updated_at))
        .limit(1)
    )
    res = await ctx.deps.db.execute(stmt)
    found_id = res.scalar_one_or_none()
    return str(found_id) if found_id else None


async def execute_cv_finalization(
    db: AsyncSession,
    session_id: str,
    user_id: str,
    deps: AgentDeps | None = None,
    template_id: Literal["classic"] = "classic",
    language: Literal["vi", "en"] = "en",
    service: CvGeneratorService | None = None,
) -> tuple[bool, str, dict[str, Any]]:
    """Core logic to finalize CV improvement session and generate PDF artifacts."""
    workflow = CvImprovementWorkflow(db)
    session = await workflow.get_session(session_id, user_id=user_id)

    # Step 1: Apply approved revisions if not already applied
    if not session.revised_resume_data:
        if not session.user_decisions:
            # If user asks to finalize without manual itemized choices, auto-approve proposals
            suggestions = (session.proposals or {}).get("suggestions", [])
            if suggestions:
                auto_decisions = [
                    {"suggestion_id": s.get("id"), "decision": CvDecisionType.APPROVED}
                    for s in suggestions
                    if s.get("id")
                ]
                session = await workflow.batch_decide(
                    session_id=session.id,
                    decisions=auto_decisions,
                    user_id=user_id,
                )
            else:
                return (
                    False,
                    "Không thể xuất CV: Chưa có gợi ý nào được người dùng chấp thuận.",
                    {},
                )
        try:
            session = await workflow.resume(session_id, user_id=user_id, deps=deps)
        except Exception as exc:
            log_step("cv_improvement.resume_error", error=str(exc))
            return (
                False,
                f"Quá trình áp dụng thay đổi vào CV thất bại: {exc}. Bạn có thể thử lại.",
                {"error": str(exc)},
            )

    if not session.revised_resume_data:
        return (
            False,
            "Không thể tạo CV: Không tìm thấy dữ liệu CV sau khi áp dụng thay đổi.",
            {},
        )

    # Step 2: Convert to CvContent schema
    cv_content = resume_data_to_cv_content(session.revised_resume_data, language=language)

    # Step 3: Run CV generator service
    generator_service = service or _get_cv_generator_service(deps)
    payload = GenerateCvInput(template_id=template_id, language=language, cv=cv_content)
    result: GenerateCvResult = await generator_service.generate(payload, owner_id=user_id)

    if result.status != "succeeded":
        error_code = result.error.code if result.error else "UNKNOWN_ERROR"
        return (
            False,
            f"Quá trình sinh file PDF thất bại với mã lỗi: {error_code}.",
            {"error_code": error_code},
        )

    # Step 4: Extract artifact links
    pdf_file = next((f for f in result.files if f.format == "pdf"), None)
    tex_file = next((f for f in result.files if f.format == "tex"), None)
    pdf_url = pdf_file.download_url if pdf_file else None

    # Step 5: Update session state in DB
    repo = CvImprovementRepository(db)
    await repo.save_revised_resume(
        session_id=session.id,
        resume_data=session.revised_resume_data,
        pdf_url=pdf_url,
    )
    await repo.transition_step(session.id, CvImprovementStep.PDF_GENERATED)

    # Checkpoint completed task progress in TaskProgressManager (K4/K5)
    try:
        active_session_id = session.chat_session_id or session.id
        state_mgr = TaskProgressManager(db)
        await state_mgr.update_and_checkpoint(
            session_id=active_session_id,
            user_id=user_id,
            task_type="career_consulting",
            update=TaskStateUpdate(
                stage="COMPLETED",
                goal="Tối ưu hóa và xuất bản CV",
                completed_steps_add=["Phê duyệt đề xuất cải thiện", "Biên dịch LaTeX và xuất PDF"],
                pending_steps=[],
                next_action="Tải file PDF CV hoàn chỉnh để ứng tuyển",
            ),
        )
    except Exception as exc:
        log_step("cv_improvement.checkpoint_error", error=str(exc))

    # Step 6: Construct markdown report
    approved_count = sum(
        1
        for d in (session.user_decisions or {}).values()
        if d.get("decision") in (CvDecisionType.APPROVED, CvDecisionType.EDITED)
    )

    lines = [
        "## Xuất CV Hoàn Tất",
        f"- **Trạng thái:** Thành công ({result.page_count} trang A4)",
        f"- **Số thay đổi đã áp dụng:** {approved_count} gợi ý",
    ]
    if pdf_url:
        lines.append(f"- **Tải CV (PDF):** [{pdf_file.filename}]({pdf_url})")
    if tex_file and tex_file.download_url:
        lines.append(f"- **Mã nguồn LaTeX (.tex):** [{tex_file.filename}]({tex_file.download_url})")

    lines.append(
        "\nBạn có thể tải file PDF về để nộp hồ sơ hoặc mở file .tex để tiếp tục tùy biến theo nhu cầu."
    )
    message = "\n".join(lines)

    log_step(
        "cv_improvement.finalized",
        session_id=session_id,
        pdf_url=pdf_url,
        pages=result.page_count,
    )

    return (
        True,
        message,
        {
            "pdf_url": pdf_url,
            "page_count": result.page_count,
            "session_id": session.id,
        },
    )


async def finalize_and_generate_cv(
    ctx: RunContext[AgentDeps],
    session_id: str | None = None,
    template_id: Literal["classic"] = "classic",
    language: Literal["vi", "en"] = "en",
) -> str:
    """Finalize approved CV improvements, compile LaTeX/PDF, and return download link.

    Call after the user has reviewed and approved CV suggestions, or when user explicitly asks
    to finalize, apply changes, and export/download the updated CV.
    """
    if not ctx.deps.user or not ctx.deps.user.user_id:
        return "Lỗi: Người dùng chưa được xác thực."

    if not ctx.deps.db:
        return "Lỗi: Kết nối cơ sở dữ liệu không khả dụng."

    target_session_id = await _resolve_latest_session_id(ctx, session_id)
    if not target_session_id:
        return "Lỗi: Không tìm thấy phiên làm việc CV nào đang mở để xuất file."

    async with ctx.deps.db_lock:
        ok, message, _ = await execute_cv_finalization(
            db=ctx.deps.db,
            session_id=target_session_id,
            user_id=ctx.deps.user.user_id,
            deps=ctx.deps,
            template_id=template_id,
            language=language,
        )
        return message
