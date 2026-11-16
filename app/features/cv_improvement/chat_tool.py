"""Chat tools for Use Case 2: CV Improvement and Human-in-the-Loop review."""

import json
import logging
import re
from typing import Any, Literal

from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.db.repositories.cv_improvement import CvDecisionType
from app.features.cv_improvement.tools import _resolve_latest_session_id
from app.features.cv_improvement.workflow import CvImprovementWorkflow
from app.features.job_match.chat_tool import _find_candidate_cv
from app.memory.schemas import MemoryItemCreate
from app.memory.service import MemoryService
from app.messaging.core_client import get_core_rpc
from app.state.schemas import TaskStateUpdate
from app.state.task_progress import TaskProgressManager

logger = logging.getLogger(__name__)


async def _resolve_jd_text(
    ctx: RunContext[AgentDeps],
    target_jd: str | None = None,
    job_id: str | None = None,
) -> str | None:
    """Extracts JD text from explicit string, project ID via RPC, or chat context."""
    if target_jd and target_jd.strip():
        return target_jd.strip()

    if job_id and job_id.strip():
        try:
            rpc = getattr(ctx.deps, "rpc", None) or get_core_rpc()
            res = await rpc.call("core.project.get", {"projectId": job_id.strip()})
            if isinstance(res, dict) and res.get("ok"):
                proj = res.get("data") or res.get("project") or {}
                desc_text = proj.get("description") or proj.get("title") or ""
                skills = proj.get("requiredSkills") or []
                skills_str = ", ".join(skills) if skills else ""
                return (
                    f"Tiêu đề: {proj.get('title', '')}\nMô tả: {desc_text}\nKỹ năng: {skills_str}"
                )
        except Exception as exc:
            logger.warning("Failed to fetch project detail via RPC for job_id %s: %s", job_id, exc)

    return None


async def _build_cv_from_memory(ctx: RunContext[AgentDeps]) -> str | None:
    """Reconstructs CV text from recorded user memory facts if no CV document exists."""
    if not ctx.deps.db or not ctx.deps.user or not ctx.deps.user.user_id:
        return None
    try:
        mem_service = MemoryService(ctx.deps.db)
        summary = await mem_service.get_active_memory(ctx.deps.user.user_id)
        if not summary.items:
            return None

        category_keywords = {
            "role": ("role", "target"),
            "objective": ("objective",),
            "skills": ("skill",),
            "experience": ("exp",),
            "projects": ("project",),
            "education": ("edu",),
        }
        facts: dict[str, list[str]] = {k: [] for k in category_keywords}

        for it in summary.items:
            cat_key = f"{it.category or ''} {it.key or ''}".lower()
            val_str = str(it.value).strip() if it.value else ""
            if not val_str:
                continue
            for field, keywords in category_keywords.items():
                if any(kw in cat_key for kw in keywords):
                    facts[field].append(val_str)
                    break

        if not any(facts.values()):
            return None

        lines = ["# HỒ SƠ ỨNG VIÊN (TỔNG HỢP TỪ CONTEXT & MEMORY)"]
        if facts["role"]:
            lines.append(f"**Vị trí mục tiêu:** {', '.join(facts['role'])}")
        if facts["objective"]:
            lines.append(f"**Mục tiêu nghề nghiệp:** {' '.join(facts['objective'])}")
        if facts["skills"]:
            lines.append(f"**Kỹ năng chuyên môn:** {', '.join(facts['skills'])}")
        if facts["experience"]:
            lines.append(
                "**Kinh nghiệm làm việc:**\n" + "\n".join(f"- {e}" for e in facts["experience"])
            )
        if facts["projects"]:
            lines.append("**Dự án tiêu biểu:**\n" + "\n".join(f"- {p}" for p in facts["projects"]))
        if facts["education"]:
            lines.append(
                "**Học vấn & Bằng cấp:**\n" + "\n".join(f"- {ed}" for ed in facts["education"])
            )

        return "\n\n".join(lines)
    except Exception as exc:
        logger.warning("Failed to construct CV from memory: %s", exc)
        return None


def _synthesize_starter_cv_from_jd(jd_text: str) -> str:
    """Synthesize a baseline candidate profile tailored to the JD when no CV is provided.

    Guarantees standard placeholder contact fields and relevant starter project/experience
    so the user can review and generate a starter CV immediately.
    """
    first_line = jd_text.strip().splitlines()[0] if jd_text.strip() else ""
    role_match = re.search(
        r"(?:vị trí|chức danh|role|position|title)?[:\s-]*([A-Za-z0-9\s/().+-]{4,40})",
        first_line,
        re.IGNORECASE,
    )
    role_title = role_match.group(1).strip() if role_match else "Software Engineer"
    if len(role_title) > 40 or len(role_title) < 3:
        role_title = "Software Engineer"

    return f"""# HỒ SƠ ỨNG VIÊN (KHỞI TẠO TỰ ĐỘNG TỪ JD)
Họ và tên: Your Full Name
Email: youremail@gmail.com | SĐT: +84 123 456 789
LinkedIn: linkedin.com/in/yourusername | GitHub: github.com/yourusername

## Vị trí mục tiêu
{role_title}

## Tóm tắt chuyên môn
Kỹ sư phần mềm định hướng phát triển chuyên sâu theo yêu cầu vị trí {role_title}. Có nền tảng vững chắc về tư duy giải thuật, kiến trúc hệ thống và quy trình phát triển phần mềm chuẩn mực.

## Kỹ năng chuyên môn
- Ngôn ngữ & Công nghệ: Khớp theo yêu cầu trọng tâm của mô tả công việc ({role_title})
- Cơ sở dữ liệu & Caching: PostgreSQL, Redis, Database Optimization
- Công cụ & Quy trình: Git, Docker, CI/CD, Automated Testing

## Kinh nghiệm làm việc
- Vị trí: Junior {role_title}
  Đơn vị: Your Previous Company | 2023 - Hiện tại
  * Tham gia phân tích thiết kế và hiện thực hóa các tính năng theo kiến trúc chuẩn.
  * Tối ưu hóa truy vấn cơ sở dữ liệu và xử lý bất đồng bộ, cải thiện độ trễ phản hồi hệ thống.

## Dự án tiêu biểu
- Tên dự án: Your Highlighted Project
  Vai trò: Developer chính | Công nghệ: Relevant Stack
  * Thiết kế và xây dựng các dịch vụ backend phục vụ nghiệp vụ chính.
  * Tích hợp kiểm thử tự động đạt độ bao phủ kiểm thử cao và triển khai qua CI/CD pipeline.

## Học vấn
- Bằng cấp: Cử nhân Công nghệ Thông tin / Khoa học Máy tính
  Trường: Đại học Công nghệ | 2020 - 2024
"""


async def review_and_improve_cv(
    ctx: RunContext[AgentDeps],
    target_jd: str | None = None,
    job_id: str | None = None,
    general_review: bool = False,
    raw_cv_text: str | None = None,
    create_starter: bool = False,
) -> str:
    """Analyze user's CV against a Job Description (JD) or general HR standards and produce structured improvement suggestions.

    Call this tool whenever the user asks to review, optimize, evaluate, or improve their CV
    (either for a specific job/JD, or for a general HR review without a JD).

    Parameters:
    - target_jd: Optional text of target Job Description or requirements.
    - job_id: Optional project ID on Occupify.
    - general_review: Set to True if user wants a general CV review according to HR standards without a specific JD.
    - raw_cv_text: Optional explicit CV text (e.g. collected via interview or chat when no PDF is uploaded).
    - create_starter: Set to True if user has no CV and requests to create/draft a new starter CV from the JD.

    CRITICAL STOPPING RULE: After presenting the suggestions returned by this tool, you MUST STOP
    your turn. Do NOT auto-approve suggestions or call finalize_and_generate_cv automatically.
    You MUST ask the user to review the suggestions (Approve, Reject, or Edit) first.
    """
    if not ctx.deps.user or not ctx.deps.user.user_id:
        return "Lỗi: Người dùng chưa được xác thực."
    if not ctx.deps.db:
        return "Lỗi: Kết nối cơ sở dữ liệu không khả dụng."

    # 1. Locate Target JD or apply General HR Review standards
    is_general = general_review or (
        bool(target_jd)
        and target_jd.lower().strip() in ("general", "chung", "tổng quát", "mặc định", "hr")
    )
    if is_general:
        jd_text = (
            "Tiêu chuẩn tuyển dụng chung (General HR Review): "
            "Đánh giá cấu trúc và độ chuyên nghiệp của hồ sơ, "
            "phát hiện và loại bỏ các mô tả CRUD cơ bản hoặc sáo rỗng, "
            "bổ sung số liệu định lượng theo công thức STAR/XYZ, "
            "làm nổi bật kỹ năng cốt lõi và nâng cao tác động thực tế của ứng viên."
        )
    else:
        jd_text = await _resolve_jd_text(ctx, target_jd=target_jd, job_id=job_id)

    # 2. Locate candidate CV
    cv_text = raw_cv_text.strip() if raw_cv_text and raw_cv_text.strip() else ""
    if not cv_text:
        cv_obj = await _find_candidate_cv(ctx)
        cv_text = (
            cv_obj.text.strip()
            if cv_obj and cv_obj.text.strip()
            else ((await _build_cv_from_memory(ctx)) or "")
        )

    # 3. Handle Cold-Start (No CV provided but JD is available)
    is_cold_start = False
    if not cv_text:
        if jd_text and create_starter:
            cv_text = _synthesize_starter_cv_from_jd(jd_text)
            is_cold_start = True
        else:
            return (
                "> ⚠️ **Vui lòng đính kèm file CV (PDF)** để mình có thể phân tích "
                "kinh nghiệm và đưa ra các đề xuất cải thiện phù hợp nhất.\n\n"
                "> 💡 **Nếu bạn chưa có CV:** Đừng lo lắng! Hãy yêu cầu mình **tạo mẫu CV từ JD** "
                "hoặc chia sẻ các thông tin về **kinh nghiệm làm việc**, **dự án**, **kỹ năng**, "
                "mình sẽ tự động thiết lập khung CV chuẩn chỉnh theo đúng yêu cầu công việc để bạn bắt đầu!\n"
                "> *(Lưu ý: Để bảo vệ quyền riêng tư, bạn không cần cung cấp các dữ liệu nhạy cảm như số CCCD, tài khoản ngân hàng hay địa chỉ nhà).* "
            )

    if not jd_text:
        return (
            "Vui lòng cung cấp mô tả công việc (JD), vị trí tuyển dụng mục tiêu hoặc mã dự án (job_id) "
            "để mình tiến hành đối chiếu và tối ưu hóa CV cho bạn."
        )

    # 4. Create session & run analysis
    async with ctx.deps.db_lock:
        workflow = CvImprovementWorkflow(ctx.deps.db)
        session = await workflow.start_session(
            user_id=ctx.deps.user.user_id,
            original_cv_text=cv_text,
            target_jd_text=jd_text,
            chat_session_id=ctx.deps.session_id,
        )
        analyzed_session = await workflow.analyze(
            session_id=session.id,
            user_id=ctx.deps.user.user_id,
            deps=ctx.deps,
        )

    proposals = analyzed_session.proposals or {}
    target_role = proposals.get("target_role") or (
        "Tiêu chuẩn HR chuyên nghiệp" if general_review else "Vị trí mục tiêu"
    )
    summary_text = proposals.get("summary") or "Đã phân tích hồ sơ theo tiêu chuẩn JD."
    strengths = proposals.get("strengths") or []
    missing_skills = proposals.get("missing_skills") or []
    suggestions = proposals.get("suggestions") or []

    # Update Task Checkpoint & User Memory (K4)
    if ctx.deps.session_id and ctx.deps.user and ctx.deps.user.user_id:
        try:
            async with ctx.deps.db_lock:
                state_mgr = TaskProgressManager(ctx.deps.db)
                await state_mgr.update_and_checkpoint(
                    session_id=ctx.deps.session_id,
                    user_id=ctx.deps.user.user_id,
                    task_type="career_consulting",
                    update=TaskStateUpdate(
                        stage="ASSESSMENT",
                        goal=f"Tối ưu hóa và review CV cho vị trí {target_role}",
                        completed_steps_add=["Phân tích kinh nghiệm và đối chiếu JD"],
                        pending_steps=[
                            "Xem xét và phê duyệt các đề xuất cải thiện",
                            "Xuất file PDF hoàn chỉnh",
                        ],
                        next_action="Chờ người dùng duyệt các đề xuất cải thiện CV",
                    ),
                )
                mem_svc = MemoryService(ctx.deps.db)
                mem_items = [
                    ("target_role", "role", target_role, True),
                    ("skills", "strengths", ", ".join(strengths[:3]) if strengths else None, True),
                    (
                        "skills",
                        "gaps",
                        ", ".join(missing_skills[:3]) if missing_skills else None,
                        False,
                    ),
                ]
                for cat, key, val, conf in mem_items:
                    if val:
                        await mem_svc.record_fact(
                            ctx.deps.user.user_id,
                            MemoryItemCreate(
                                category=cat,
                                key=key,
                                value=val,
                                is_confirmed=conf,
                                source="cv_improvement",
                            ),
                        )
        except Exception as exc:
            logger.warning("Failed to update task checkpoint or memory: %s", exc)

    # 4. Build Markdown Response
    lines = []
    if is_cold_start:
        lines.append(
            "> ℹ️ **Khởi tạo CV mẫu từ JD:** Mình đã tự động tạo khung CV khởi điểm phù hợp với vị trí tuyển dụng "
            "kèm các trường thông tin chuẩn (placeholder) để bạn có thể xem xét, tối ưu và xuất file ngay.\n"
        )
    lines.extend(
        [
            f"### 📋 Kết Quả Phân Tích & Đề Xuất Cải Thiện CV ({target_role})\n",
            f"**Đánh giá chung:** {summary_text}\n",
        ]
    )

    if strengths:
        lines.append("**Điểm mạnh phù hợp:**")
        for s in strengths:
            lines.append(f"- ✓ {s}")
        lines.append("")

    if missing_skills:
        lines.append("**Khoảng cách kỹ năng cần lưu ý theo JD:**")
        for m in missing_skills:
            lines.append(f"- ⚠️ {m}")
        lines.append("")

    lines.append(f"### 📝 Danh Sách Đề Xuất Chỉnh Sửa ({len(suggestions)} gợi ý)\n")
    for idx, sug in enumerate(suggestions, start=1):
        s_id = sug.get("id", f"sug-{idx}")
        section = sug.get("section", "Phần chung")
        orig = sug.get("target_original_text", "")
        revised = sug.get("suggested_revised_text", "")
        reason = sug.get("reason", "")

        lines.append(f"#### Gợi ý #{s_id} [{section}]")
        lines.append(f'- **Văn bản gốc:** *"{orig}"*')
        lines.append(f'- **Đề xuất mới:** **"{revised}"**')
        lines.append(f"- **Lý do cải thiện:** {reason}")
        lines.append("")

    # 5. Embed structured JSON block for interactive UI cards
    payload = {
        "sessionId": analyzed_session.id,
        "targetRole": target_role,
        "suggestions": suggestions,
    }
    json_block = json.dumps(payload, ensure_ascii=False)
    lines.append(f"<!-- CV_SUGGESTIONS_START\n{json_block}\nCV_SUGGESTIONS_END -->\n")

    lines.append(
        "👉 **Bước tiếp theo:** Bạn vui lòng xem các đề xuất trên và chọn **[Chấp thuận]**, "
        "**[Từ chối]** hoặc **[Chỉnh sửa]** trực tiếp trên thẻ tương tác (hoặc phản hồi qua tin nhắn chat). "
        "Sau khi duyệt xong, bạn có thể bấm **[Áp dụng & Xuất PDF]** để tạo file CV hoàn chỉnh."
    )

    return "\n".join(lines)


async def record_cv_decisions(
    ctx: RunContext[AgentDeps],
    session_id: str | None = None,
    action: Literal["approve_all", "reject_all", "custom"] = "approve_all",
    decisions: list[dict[str, Any]] | None = None,
) -> str:
    """Record user decisions (Approve, Reject, or Edit) on CV improvement suggestions.

    Call this tool when the user states their approval or rejection choices in chat
    (e.g., 'Tôi đồng ý tất cả gợi ý', 'Tôi chấp thuận gợi ý 1, từ chối gợi ý 2').
    """
    if not ctx.deps.user or not ctx.deps.user.user_id:
        return "Lỗi: Người dùng chưa được xác thực."
    if not ctx.deps.db:
        return "Lỗi: Kết nối cơ sở dữ liệu không khả dụng."

    target_session_id = await _resolve_latest_session_id(ctx, session_id)
    if not target_session_id:
        return "Không tìm thấy phiên làm việc CV nào đang mở để ghi nhận quyết định."

    async with ctx.deps.db_lock:
        workflow = CvImprovementWorkflow(ctx.deps.db)
        session = await workflow.get_session(target_session_id, user_id=ctx.deps.user.user_id)

        decisions_list: list[dict[str, Any]] = []
        suggestions = (session.proposals or {}).get("suggestions", [])

        if action in ("approve_all", "reject_all"):
            dec_type = (
                CvDecisionType.APPROVED if action == "approve_all" else CvDecisionType.REJECTED
            )
            decisions_list = [
                {"suggestion_id": s.get("id"), "decision": dec_type}
                for s in suggestions
                if s.get("id")
            ]
        elif decisions:
            decisions_list = decisions

        if not decisions_list:
            return "Chưa có quyết định nào được chỉ định."

        await workflow.batch_decide(
            session_id=target_session_id,
            decisions=decisions_list,
            user_id=ctx.deps.user.user_id,
        )

        # Checkpoint decisions in TaskProgressManager (K4/K5)
        if ctx.deps.session_id:
            try:
                state_mgr = TaskProgressManager(ctx.deps.db)
                await state_mgr.update_and_checkpoint(
                    session_id=ctx.deps.session_id,
                    user_id=ctx.deps.user.user_id,
                    task_type="career_consulting",
                    update=TaskStateUpdate(
                        stage="ASSESSMENT",
                        completed_steps_add=["Phê duyệt các đề xuất chỉnh sửa CV"],
                        pending_steps=["Xuất file PDF hoàn chỉnh"],
                        next_action="Xác nhận và xuất bản CV sang định dạng PDF",
                    ),
                )
            except Exception as exc:
                logger.warning("Failed to update task checkpoint for decisions: %s", exc)

    approved_count = sum(
        1
        for d in decisions_list
        if d.get("decision") in (CvDecisionType.APPROVED, CvDecisionType.EDITED)
    )
    return (
        f"Đã ghi nhận quyết định thành công ({approved_count}/{len(decisions_list)} gợi ý được áp dụng). "
        "Bạn có muốn mình tiến hành áp dụng thay đổi và xuất file PDF CV ngay bây giờ không?"
    )
