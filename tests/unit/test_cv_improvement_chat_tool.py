from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from pydantic_ai import RunContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.deps import AgentDeps
from app.core.security import CurrentUser
from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)
from app.documents.cv_text import CvText
from app.features.chat.agent import chat_agent
from app.features.cv_generator.schemas import ArtifactFile, GenerateCvResult
from app.features.cv_improvement.chat_tool import (
    _resolve_jd_text,
    _resolve_latest_session_id,
    record_cv_decisions,
    review_and_improve_cv,
)
from app.features.cv_improvement.tools import finalize_and_generate_cv


@pytest.fixture
def current_user():
    return CurrentUser(
        user_id="user_chat_test",
        email="chat_user@example.com",
        name="Chat Tester",
        roles=["user"],
    )


# ---------------------------------------------------------------------------
# Helper resolution tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_resolve_latest_session_id(test_db: AsyncSession, current_user):
    repo = CvImprovementRepository(test_db)
    s1 = await repo.create_session(
        user_id=current_user.user_id,
        original_cv_text="CV 1",
        target_jd_text="JD 1",
        chat_session_id="chat-sess-1",
    )

    deps = AgentDeps(
        user=current_user,
        session_id="chat-sess-1",
        db=test_db,
    )
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    found_id = await _resolve_latest_session_id(ctx)
    assert found_id == s1.id


@pytest.mark.asyncio
async def test_resolve_jd_text():
    ctx = MagicMock(spec=RunContext)
    ctx.deps = MagicMock()

    # Direct target_jd
    jd = await _resolve_jd_text(ctx, target_jd="Backend Python Developer JD")
    assert jd == "Backend Python Developer JD"

    # Via RPC mock
    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(
        return_value={
            "ok": True,
            "data": {
                "title": "Senior Go Engineer",
                "description": "Building microservices",
                "requiredSkills": ["Go", "Kubernetes"],
            },
        }
    )
    ctx.deps.rpc = mock_rpc
    jd_rpc = await _resolve_jd_text(ctx, job_id="proj-123")
    assert "Senior Go Engineer" in jd_rpc
    assert "Kubernetes" in jd_rpc

    # None
    ctx.deps.rpc = None
    assert await _resolve_jd_text(ctx) is None


# ---------------------------------------------------------------------------
# review_and_improve_cv Tool tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_review_and_improve_cv_need_cv(test_db: AsyncSession, current_user):
    deps = AgentDeps(user=current_user, session_id="sess-1", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    res = await review_and_improve_cv(ctx, target_jd="Backend JD")
    assert "Vui lòng đính kèm file CV (PDF)" in res


@pytest.mark.asyncio
async def test_review_and_improve_cv_need_jd(test_db: AsyncSession, current_user, monkeypatch):
    deps = AgentDeps(user=current_user, session_id="sess-1", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    # Mock finding a candidate CV
    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool._find_candidate_cv",
        AsyncMock(return_value=CvText(text="CV Content with skills")),
    )

    res = await review_and_improve_cv(ctx, target_jd=None, job_id=None)
    assert "Vui lòng cung cấp mô tả công việc (JD)" in res


@pytest.mark.asyncio
async def test_review_and_improve_cv_success(test_db: AsyncSession, current_user, monkeypatch):
    deps = AgentDeps(user=current_user, session_id="chat-sess-100", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    # Mock finding candidate CV
    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool._find_candidate_cv",
        AsyncMock(return_value=CvText(text="Nguyen Van A - Python Dev with CRUD")),
    )

    # Mock CvImprovementWorkflow analyze output
    async def mock_analyze(self, session_id, user_id=None, deps=None):
        repo = CvImprovementRepository(self.db)
        return await repo.save_suggestions(
            session_id,
            {
                "target_role": "Backend Engineer",
                "summary": "CV khá phù hợp nhưng cần lượng hóa kinh nghiệm.",
                "strengths": ["Thành thạo Python", "Hiểu REST API"],
                "missing_skills": ["Docker", "Redis"],
                "suggestions": [
                    {
                        "id": "sug-1",
                        "section": "Kinh nghiệm",
                        "target_original_text": "Viết API CRUD cơ bản",
                        "suggested_revised_text": "Xây dựng hệ thống REST API xử lý 5,000 req/s",
                        "reason": "Bổ sung số liệu định lượng theo công thức STAR",
                    }
                ],
            },
        )

    monkeypatch.setattr(
        "app.features.cv_improvement.workflow.CvImprovementWorkflow.analyze",
        mock_analyze,
    )

    res = await review_and_improve_cv(
        ctx,
        target_jd="Yêu cầu: Backend Developer nắm vững FastAPI và Redis.",
    )

    # Verify structured content and stopping prompt
    assert "Kết Quả Phân Tích & Đề Xuất Cải Thiện CV" in res
    assert "Backend Engineer" in res
    assert "Thành thạo Python" in res
    assert "Docker" in res
    assert "Gợi ý #sug-1" in res
    assert "Viết API CRUD cơ bản" in res
    assert "Xây dựng hệ thống REST API xử lý 5,000 req/s" in res

    # Verify embedded payload for Frontend Suggestion Cards
    assert "<!-- CV_SUGGESTIONS_START" in res
    assert "CV_SUGGESTIONS_END -->" in res

    # Verify stopping prompt instructing user review
    assert "Bước tiếp theo:" in res
    assert "[Chấp thuận]" in res

    # Verify session saved in DB with status WAITING_USER_REVIEW
    repo = CvImprovementRepository(test_db)
    sessions = await repo.list_sessions(user_id=current_user.user_id)
    assert len(sessions) == 1
    assert sessions[0].status == CvImprovementStep.WAITING_USER_REVIEW


@pytest.mark.asyncio
async def test_review_and_improve_cv_general_review(
    test_db: AsyncSession, current_user, monkeypatch
):
    deps = AgentDeps(user=current_user, session_id="chat-sess-general", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool._find_candidate_cv",
        AsyncMock(return_value=CvText(text="Tran Van B - Senior Java Dev")),
    )

    async def mock_analyze(self, session_id, user_id=None, deps=None):
        repo = CvImprovementRepository(self.db)
        return await repo.save_suggestions(
            session_id,
            {
                "target_role": "Tiêu chuẩn HR chuyên nghiệp",
                "summary": "CV có cấu trúc tốt, cần làm nổi bật kỹ năng dẫn dắt.",
                "strengths": ["Java Core", "Spring Boot"],
                "missing_skills": [],
                "suggestions": [
                    {
                        "id": "sug-gen-1",
                        "section": "Kinh nghiệm",
                        "target_original_text": "Phát triển các module theo Jira",
                        "suggested_revised_text": "Thiết kế và phát triển 5+ microservices cốt lõi",
                        "reason": "Nhấn mạnh vai trò thiết kế kiến trúc",
                    }
                ],
            },
        )

    monkeypatch.setattr(
        "app.features.cv_improvement.workflow.CvImprovementWorkflow.analyze",
        mock_analyze,
    )

    # General review with no JD
    res = await review_and_improve_cv(ctx, general_review=True)
    assert "Kết Quả Phân Tích & Đề Xuất Cải Thiện CV" in res
    assert "Tiêu chuẩn HR chuyên nghiệp" in res
    assert "sug-gen-1" in res


@pytest.mark.asyncio
async def test_review_and_improve_cv_with_raw_text(
    test_db: AsyncSession, current_user, monkeypatch
):
    deps = AgentDeps(user=current_user, session_id="chat-sess-raw", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    # No uploaded PDF
    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool._find_candidate_cv",
        AsyncMock(return_value=None),
    )

    async def mock_analyze(self, session_id, user_id=None, deps=None):
        repo = CvImprovementRepository(self.db)
        return await repo.save_suggestions(
            session_id,
            {
                "target_role": "Frontend Developer",
                "summary": "Kinh nghiệm phong phú với React.",
                "strengths": ["React", "TypeScript"],
                "missing_skills": [],
                "suggestions": [
                    {
                        "id": "sug-raw-1",
                        "section": "Kỹ năng",
                        "target_original_text": "Làm web giao diện cơ bản",
                        "suggested_revised_text": "Xây dựng Single Page App với Next.js và TailwindCSS",
                        "reason": "Cụ thể hóa công nghệ",
                    }
                ],
            },
        )

    monkeypatch.setattr(
        "app.features.cv_improvement.workflow.CvImprovementWorkflow.analyze",
        mock_analyze,
    )

    res = await review_and_improve_cv(
        ctx,
        raw_cv_text="Ứng viên: Lê Văn C, Frontend Developer 2 năm kinh nghiệm.",
        general_review=True,
    )
    assert "Kết Quả Phân Tích & Đề Xuất Cải Thiện CV" in res
    assert "sug-raw-1" in res


@pytest.mark.asyncio
async def test_review_and_improve_cv_from_memory(test_db: AsyncSession, current_user, monkeypatch):
    from app.memory.schemas import MemoryItemCreate
    from app.memory.service import MemoryService

    # Store memory facts
    mem_service = MemoryService(test_db)
    await mem_service.record_fact(
        current_user.user_id,
        MemoryItemCreate(
            category="cv_role",
            key="target_role",
            value="Frontend Developer",
            is_confirmed=True,
        ),
    )
    await mem_service.record_fact(
        current_user.user_id,
        MemoryItemCreate(
            category="cv_experience",
            key="company_1",
            value="Công ty Tech A - 2 năm làm React/TypeScript",
            is_confirmed=True,
        ),
    )

    deps = AgentDeps(user=current_user, session_id="chat-sess-mem", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    # No uploaded PDF
    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool._find_candidate_cv",
        AsyncMock(return_value=None),
    )

    async def mock_analyze(self, session_id, user_id=None, deps=None):
        repo = CvImprovementRepository(self.db)
        return await repo.save_suggestions(
            session_id,
            {
                "target_role": "Frontend Developer",
                "summary": "Dữ liệu được tổng hợp từ phiên trao đổi.",
                "strengths": ["React", "TypeScript"],
                "missing_skills": [],
                "suggestions": [
                    {
                        "id": "sug-mem-1",
                        "section": "Kinh nghiệm",
                        "target_original_text": "Công ty Tech A",
                        "suggested_revised_text": "Lead Frontend tại Công ty Tech A",
                        "reason": "Làm rõ vị thế",
                    }
                ],
            },
        )

    monkeypatch.setattr(
        "app.features.cv_improvement.workflow.CvImprovementWorkflow.analyze",
        mock_analyze,
    )

    res = await review_and_improve_cv(ctx, general_review=True)
    assert "Kết Quả Phân Tích & Đề Xuất Cải Thiện CV" in res
    assert "sug-mem-1" in res


# ---------------------------------------------------------------------------
# record_cv_decisions Tool tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_record_cv_decisions_approve_all(test_db: AsyncSession, current_user):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id=current_user.user_id,
        original_cv_text="CV",
        target_jd_text="JD",
        chat_session_id="chat-sess-200",
    )
    await repo.save_suggestions(
        session.id,
        {
            "target_role": "Backend",
            "summary": "Phù hợp",
            "suggestions": [
                {
                    "id": "s-1",
                    "section": "exp",
                    "target_original_text": "A",
                    "suggested_revised_text": "B",
                    "reason": "C",
                },
                {
                    "id": "s-2",
                    "section": "skills",
                    "target_original_text": "X",
                    "suggested_revised_text": "Y",
                    "reason": "Z",
                },
            ],
        },
    )

    deps = AgentDeps(user=current_user, session_id="chat-sess-200", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    res = await record_cv_decisions(ctx, session_id=session.id, action="approve_all")
    assert "Đã ghi nhận quyết định thành công (2/2 gợi ý được áp dụng)" in res

    refreshed = await repo.get_session(session.id)
    assert refreshed.user_decisions["s-1"]["decision"] == CvDecisionType.APPROVED
    assert refreshed.user_decisions["s-2"]["decision"] == CvDecisionType.APPROVED


# ---------------------------------------------------------------------------
# finalize_and_generate_cv auto-approval and session lookup fallback
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_finalize_and_generate_cv_fallback_lookup(test_db: AsyncSession, current_user):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id=current_user.user_id,
        original_cv_text="CV",
        target_jd_text="JD",
        chat_session_id="chat-sess-300",
    )
    await repo.save_suggestions(
        session.id,
        {
            "target_role": "Backend",
            "summary": "Tốt",
            "suggestions": [
                {
                    "id": "s-1",
                    "section": "exp",
                    "target_original_text": "Old",
                    "suggested_revised_text": "New",
                    "reason": "Better",
                }
            ],
        },
    )
    await repo.save_revised_resume(
        session.id,
        {
            "full_name": "Nguyễn Văn A",
            "title": "Backend",
            "summary": "Tóm tắt",
            "skills": ["Python"],
        },
    )

    mock_service = MagicMock()
    mock_service.generate = AsyncMock(
        return_value=GenerateCvResult(
            status="succeeded",
            artifact_id="art-fallback",
            page_count=1,
            compiler="xelatex",
            files=[
                ArtifactFile(
                    format="pdf",
                    filename="cv.pdf",
                    content_type="application/pdf",
                    download_url="/download/art-fallback.pdf",
                    expires_at=datetime.now(UTC),
                )
            ],
        )
    )

    deps = AgentDeps(
        user=current_user,
        session_id="chat-sess-300",
        db=test_db,
        cv_generator_service=mock_service,
    )
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    # Call finalize_and_generate_cv without passing session_id (should auto-lookup)
    res = await finalize_and_generate_cv(ctx, session_id=None)
    assert "Xuất CV Hoàn Tất" in res
    assert "[cv.pdf](/download/art-fallback.pdf)" in res

    refreshed = await repo.get_session(session.id)
    assert refreshed.status == CvImprovementStep.PDF_GENERATED
    assert refreshed.pdf_url == "/download/art-fallback.pdf"


# ---------------------------------------------------------------------------
# Chat Agent registration check
# ---------------------------------------------------------------------------


def test_chat_agent_has_cv_improvement_tools():
    tool_keys = list(chat_agent._function_toolset.tools.keys())
    assert "review_and_improve_cv" in tool_keys
    assert "record_cv_decisions" in tool_keys
    assert "finalize_and_generate_cv" in tool_keys
