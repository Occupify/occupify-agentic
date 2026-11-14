"""Integration tests for Use Case 2: CV Improvement and Tailoring Agent.

Validates end-to-end flows:
- Full lifecycle: start -> analyze -> decide -> resume -> finalize PDF
- AgentRun tracing and database persistence
- Recovery and rollback consistency
- Leader's feedback: placeholder guardrails for missing email, phone, links, projects
- Cold-start CV generation from JD when user has no CV
"""

from datetime import UTC, datetime
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from pydantic_ai import RunContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.deps import AgentDeps
from app.db.models import AgentRun
from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)
from app.features.cv_generator.schemas import (
    ArtifactFile,
    GenerateCvResult,
)
from app.features.cv_improvement.chat_tool import review_and_improve_cv
from app.features.cv_improvement.tools import (
    execute_cv_finalization,
    resume_data_to_cv_content,
)
from app.features.cv_improvement.workflow import CvImprovementWorkflow
from app.skill_schemas.cv_improvement import (
    CvImprovementProposal,
    CvSuggestionItem,
    ResumeData,
    ResumeEducationItem,
    ResumeExperienceItem,
    ResumeProjectItem,
)


class MockSkillAgent:
    """Mock agent returning structured data matching skill schemas."""

    def __init__(self, mode: str = "suggest"):
        self.mode = mode

    async def run(self, prompt: str, deps: Any = None) -> Any:
        if self.mode == "suggest":
            return type(
                "RunRes",
                (),
                {
                    "output": CvImprovementProposal(
                        target_role="Python Backend Developer",
                        summary="Đã phân tích và đề xuất nâng cấp STAR.",
                        strengths=["Cơ sở dữ liệu tốt"],
                        missing_skills=["Docker", "Redis"],
                        suggestions=[
                            CvSuggestionItem(
                                id="sug-1",
                                section="Kinh nghiệm làm việc",
                                target_original_text="Viết API CRUD.",
                                suggested_revised_text="Thiết kế và tối ưu 15+ RESTful API hiệu năng cao với FastAPI, giảm 30% độ trễ.",
                                reason="Nâng cấp mô tả sang công thức STAR với số liệu cụ thể.",
                            ),
                            CvSuggestionItem(
                                id="sug-2",
                                section="Dự án tiêu biểu",
                                target_original_text="Làm tính năng giỏ hàng.",
                                suggested_revised_text="Hiện thực hóa module giỏ hàng xử lý 5.000 req/s với Redis cache và PostgreSQL.",
                                reason="Nhấn mạnh năng lực chịu tải theo yêu cầu JD.",
                            ),
                        ],
                    ),
                    "usage": lambda *args, **kwargs: type(
                        "Usage", (), {"request_tokens": 1100, "response_tokens": 400}
                    )(),
                },
            )()
        else:
            return type(
                "RunRes",
                (),
                {
                    "output": ResumeData(
                        full_name="Nguyễn Văn An",
                        title="Python Backend Developer",
                        contact_info="nguyenvan.an@example.com | 0912345678 | github.com/nguyenvanan",
                        summary="Kỹ sư Backend chuyên sâu Python/FastAPI.",
                        skills=["Python", "FastAPI", "PostgreSQL", "Redis", "Docker"],
                        experiences=[
                            ResumeExperienceItem(
                                company="TechSoft Solutions",
                                role="Junior Backend Developer",
                                period="2023 - 2024",
                                bullet_points=[
                                    "Thiết kế và tối ưu 15+ RESTful API hiệu năng cao với FastAPI, giảm 30% độ trễ."
                                ],
                            )
                        ],
                        projects=[
                            ResumeProjectItem(
                                name="Hệ thống Bán hàng Mini",
                                role="Backend Lead",
                                tech_stack=["Python", "FastAPI", "Redis"],
                                bullet_points=[
                                    "Hiện thực hóa module giỏ hàng xử lý 5.000 req/s với Redis cache và PostgreSQL."
                                ],
                            )
                        ],
                        education=[
                            ResumeEducationItem(
                                institution="Đại học Khoa học Tự nhiên",
                                degree="Cử nhân Kỹ thuật Phần mềm",
                                period="2019 - 2023",
                            )
                        ],
                        certifications=[],
                        additional_sections=[],
                    ),
                    "usage": lambda *args, **kwargs: type(
                        "Usage", (), {"request_tokens": 1400, "response_tokens": 550}
                    )(),
                },
            )()


def _create_mock_cv_generator(status: str = "succeeded") -> MagicMock:
    mock_service = MagicMock()
    mock_result = GenerateCvResult(
        status=status,
        artifact_id="art-integration-01",
        page_count=1,
        compiler="xelatex",
        files=[
            ArtifactFile(
                format="pdf",
                filename="improved_cv.pdf",
                content_type="application/pdf",
                download_url="/ai/cv-improvement/download/improved_cv.pdf",
                expires_at=datetime.now(UTC),
            ),
            ArtifactFile(
                format="tex",
                filename="improved_cv.tex",
                content_type="application/x-tex",
                download_url="/ai/cv-improvement/download/improved_cv.tex",
                expires_at=datetime.now(UTC),
            ),
        ],
    )
    mock_service.generate = AsyncMock(return_value=mock_result)
    return mock_service


@pytest.mark.asyncio
async def test_full_cv_improvement_lifecycle(test_db: AsyncSession, mock_user):
    """End-to-end integration: start -> analyze -> decide -> resume -> finalize PDF."""
    suggest_agent = MockSkillAgent("suggest")
    apply_agent = MockSkillAgent("apply")
    workflow = CvImprovementWorkflow(test_db, suggest_agent=suggest_agent, apply_agent=apply_agent)

    cv_text = """# NGUYEN VAN AN
Email: nguyenvan.an@example.com | SĐT: 0912345678
Kinh nghiệm: TechSoft Solutions - Viết API CRUD.
"""
    jd_text = "Python Backend Developer yêu cầu FastAPI, Redis, Docker."

    # 1. Start Session
    session = await workflow.start_session(
        user_id=mock_user.user_id,
        original_cv_text=cv_text,
        target_jd_text=jd_text,
    )
    assert session.status == CvImprovementStep.INIT

    # 2. Analyze (creates AgentRun record)
    analyzed = await workflow.analyze(session.id, user_id=mock_user.user_id)
    assert analyzed.status == CvImprovementStep.WAITING_USER_REVIEW
    assert len(analyzed.proposals.get("suggestions", [])) == 2

    # Check AgentRun created for analyze
    stmt = select(AgentRun).where(
        AgentRun.session_id == session.id,
        AgentRun.model == "suggest-cv-improvements",
    )
    run_analyze = (await test_db.execute(stmt)).scalar_one_or_none()
    assert run_analyze is not None
    assert run_analyze.status == "succeeded"
    assert run_analyze.tokens_in > 0

    # 3. User Review / Decide
    await workflow.decide(
        session_id=session.id,
        suggestion_id="sug-1",
        decision=CvDecisionType.APPROVED,
        user_id=mock_user.user_id,
    )
    await workflow.decide(
        session_id=session.id,
        suggestion_id="sug-2",
        decision=CvDecisionType.EDITED,
        user_text="Tối ưu luồng checkout với Redis queue xử lý hơn 10.000 req/s.",
        user_id=mock_user.user_id,
    )

    # 4. Resume & Apply (creates AgentRun record)
    resumed = await workflow.resume(session.id, user_id=mock_user.user_id)
    assert resumed.status == CvImprovementStep.APPLYING_CHANGES
    assert resumed.revised_resume_data is not None

    stmt_resume = select(AgentRun).where(
        AgentRun.session_id == session.id,
        AgentRun.model == "apply-cv-revisions",
    )
    run_resume = (await test_db.execute(stmt_resume)).scalar_one_or_none()
    assert run_resume is not None
    assert run_resume.status == "succeeded"

    # 5. Finalize and Compile PDF
    mock_gen = _create_mock_cv_generator()
    ok, message, data = await execute_cv_finalization(
        db=test_db,
        session_id=session.id,
        user_id=mock_user.user_id,
        service=mock_gen,
    )
    assert ok is True
    assert "Xuất CV Hoàn Tất" in message
    assert data["pdf_url"] == "/ai/cv-improvement/download/improved_cv.pdf"

    # Verify session transitioned to PDF_GENERATED
    repo = CvImprovementRepository(test_db)
    final_session = await repo.get_session(session.id)
    assert final_session.status == CvImprovementStep.PDF_GENERATED
    assert final_session.pdf_url == "/ai/cv-improvement/download/improved_cv.pdf"


@pytest.mark.asyncio
async def test_cv_improvement_recovery_and_rollback(test_db: AsyncSession, mock_user):
    """Verifies that rollback resets decisions, clears revised data, and preserves original text."""
    suggest_agent = MockSkillAgent("suggest")
    workflow = CvImprovementWorkflow(test_db, suggest_agent=suggest_agent)

    cv_text = "# CANDIDATE PROFILE\nOriginal non-mutated text."
    session = await workflow.start_session(
        user_id=mock_user.user_id,
        original_cv_text=cv_text,
        target_jd_text="Target JD",
    )
    await workflow.analyze(session.id, user_id=mock_user.user_id)

    # Approve suggestion
    await workflow.decide(session.id, "sug-1", CvDecisionType.APPROVED, user_id=mock_user.user_id)
    refreshed = await workflow.get_session(session.id)
    assert "sug-1" in refreshed.user_decisions

    # Trigger Recovery Rollback
    recovered = await workflow.recovery(session.id, user_id=mock_user.user_id)
    assert recovered.status == CvImprovementStep.WAITING_USER_REVIEW
    assert len(recovered.user_decisions) == 0
    assert recovered.revised_resume_data is None
    # Crucial check: original CV text must remain 100% intact
    assert recovered.original_cv_text == cv_text


@pytest.mark.asyncio
async def test_cv_improvement_placeholder_guardrails(test_db: AsyncSession, mock_user):
    """Leader's feedback: Missing email, phone, links, and projects must have standard placeholders."""
    sparse_resume = {
        "full_name": "Tran Thi Minh",
        "title": "Software Intern",
        "summary": "Passionate developer.",
        "skills": ["Python", "FastAPI"],
        "experiences": [],
        "projects": [],  # Completely missing projects
    }

    content = resume_data_to_cv_content(sparse_resume, language="en")

    # Assert projects section was injected with STAR starter project
    assert len(content.projects) == 1
    assert content.projects[0].name == "Your Highlighted Project"
    assert len(content.projects[0].bullets) >= 2

    # Assert experiences section was injected with starter experience
    assert len(content.experience) == 1
    assert content.experience[0].company == "Your Previous Company"

    # Test finalization with mock generator to verify contact placeholders passed to compiler
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id=mock_user.user_id,
        original_cv_text="Tran Thi Minh\nIntern without contact or projects.",
        target_jd_text="Backend Engineer JD",
    )
    await repo.save_revised_resume(session.id, sparse_resume)

    mock_service = MagicMock()
    mock_service.generate = AsyncMock(
        return_value=GenerateCvResult(
            status="succeeded",
            artifact_id="art-placeholder",
            page_count=1,
            compiler="xelatex",
            files=[
                ArtifactFile(
                    format="pdf",
                    filename="sparse_cv.pdf",
                    content_type="application/pdf",
                    download_url="/download/sparse_cv.pdf",
                    expires_at=datetime.now(UTC),
                )
            ],
        )
    )

    ok, message, _ = await execute_cv_finalization(
        db=test_db,
        session_id=session.id,
        user_id=mock_user.user_id,
        service=mock_service,
    )
    assert ok is True

    # Inspect call kwargs to ensure generator received standard placeholder contacts
    call_kwargs = mock_service.generate.call_args.kwargs
    contact = call_kwargs.get("contact")
    assert contact is not None
    assert contact["name"] == "Tran Thi Minh"
    assert contact["email"] == "youremail@gmail.com"
    assert contact["phone"] == "+84 123 456 789"
    assert contact["link"] == "github.com/yourusername"


@pytest.mark.asyncio
async def test_cv_improvement_cold_start_flow(test_db: AsyncSession, mock_user, monkeypatch):
    """User provides no CV, only JD. Agent synthesizes starter CV and completes workflow."""
    deps = AgentDeps(user=mock_user, session_id="chat-cold-flow", db=test_db)
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    # Mock candidate CV lookup returns None
    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool._find_candidate_cv",
        AsyncMock(return_value=None),
    )

    # Mock workflow analyze to avoid external model call
    async def mock_analyze(self, session_id, user_id=None, deps=None):
        repo = CvImprovementRepository(self.db)
        await repo.save_suggestions(
            session_id=session_id,
            proposals={
                "target_role": "Fullstack React/FastAPI Engineer",
                "summary": "Đã tổng hợp khung CV khởi điểm từ JD.",
                "strengths": ["Nền tảng kỹ thuật tốt"],
                "missing_skills": ["Docker", "Kubernetes"],
                "suggestions": [
                    {
                        "id": "sug-cold-1",
                        "section": "Dự án tiêu biểu",
                        "target_original_text": "Your Highlighted Project",
                        "suggested_revised_text": "Xây dựng nền tảng E-commerce với ReactJS và FastAPI, hỗ trợ 5.000 DAU.",
                        "reason": "Phù hợp JD Fullstack.",
                    }
                ],
            },
        )
        return await repo.get_session(session_id)

    monkeypatch.setattr(
        "app.features.cv_improvement.chat_tool.CvImprovementWorkflow.analyze",
        mock_analyze,
    )

    response = await review_and_improve_cv(
        ctx,
        target_jd="Tuyển dụng Fullstack React/FastAPI Engineer lương cao.",
        create_starter=True,
    )

    assert "Khởi tạo CV mẫu từ JD" in response
    assert "Fullstack React/FastAPI Engineer" in response
    assert "sug-cold-1" in response

    # Verify session in DB contains auto-synthesized CV
    repo = CvImprovementRepository(test_db)
    session = await repo.get_session("chat-cold-flow", user_id=mock_user.user_id)
    assert session is not None
    assert "HỒ SƠ ỨNG VIÊN (KHỞI TẠO TỰ ĐỘNG TỪ JD)" in session.original_cv_text
    assert "youremail@gmail.com" in session.original_cv_text
    assert "Your Highlighted Project" in session.original_cv_text
