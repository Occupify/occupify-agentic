from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from pydantic_ai import RunContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.deps import AgentDeps
from app.core.security import CurrentUser
from app.core.storage import (
    CoreRpcStorageClient,
    LocalArtifactStorage,
    LocalStorageClient,
    set_storage_client,
)
from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)
from app.features.cv_generator.schemas import (
    ArtifactFile,
    CvContent,
    CvGenerationError,
    GenerateCvResult,
)
from app.features.cv_improvement.tools import (
    execute_cv_finalization,
    finalize_and_generate_cv,
    resume_data_to_cv_content,
)


@pytest.fixture
def current_user():
    return CurrentUser(
        user_id="user_test_123",
        email="test@example.com",
        name="Test User",
        roles=["user"],
    )


# ---------------------------------------------------------------------------
# Storage Tests
# ---------------------------------------------------------------------------


def test_local_storage_client(tmp_path):
    storage = LocalStorageClient(base_dir=tmp_path / "resumes", base_url="/download/cv")

    # Test path sanitization
    assert storage._sanitize_filename("../../etc/passwd") == "passwd"
    assert storage._sanitize_filename(".hidden") == "artifact"

    # Test get non-existent
    assert storage.get_file_path("not_found.pdf") is None


@pytest.mark.asyncio
async def test_local_storage_upload_and_get(tmp_path):
    storage = LocalStorageClient(
        base_dir=tmp_path / "resumes", base_url="/ai/cv-improvement/download"
    )

    url = await storage.upload_file(b"%PDF-1.4 test content", "test_cv.pdf")
    assert url == "/ai/cv-improvement/download/test_cv.pdf"

    path = storage.get_file_path("test_cv.pdf")
    assert path is not None
    assert path.read_bytes() == b"%PDF-1.4 test content"


@pytest.mark.asyncio
async def test_core_rpc_storage_client_success(tmp_path):
    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(return_value={"ok": True, "url": "https://cdn.example.com/cv.pdf"})

    client = CoreRpcStorageClient(rpc_client=mock_rpc)
    url = await client.upload_file(b"content", "doc.pdf")

    assert url == "https://cdn.example.com/cv.pdf"
    mock_rpc.call.assert_called_once()


@pytest.mark.asyncio
async def test_core_rpc_storage_client_fallback(tmp_path):
    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(side_effect=Exception("RPC timeout"))

    fallback = LocalStorageClient(base_dir=tmp_path, base_url="/local")
    client = CoreRpcStorageClient(rpc_client=mock_rpc, fallback=fallback)

    url = await client.upload_file(b"content", "doc.pdf")
    assert url == "/local/doc.pdf"
    assert (tmp_path / "doc.pdf").exists()


@pytest.mark.asyncio
async def test_local_artifact_storage_publish(tmp_path):
    local_client = LocalStorageClient(base_dir=tmp_path, base_url="/test/dl")
    artifact_storage = LocalArtifactStorage(storage_client=local_client)

    files = await artifact_storage.publish(
        artifact_id="art-123",
        owner_id="owner-456",
        tex=b"\\documentclass{article}",
        pdf=b"%PDF-1.4",
    )

    assert len(files) == 2
    tex_file = next(f for f in files if f.format == "tex")
    pdf_file = next(f for f in files if f.format == "pdf")

    assert tex_file.download_url == "/test/dl/art-123.tex"
    assert pdf_file.download_url == "/test/dl/art-123.pdf"
    assert (tmp_path / "art-123.tex").read_bytes() == b"\\documentclass{article}"
    assert (tmp_path / "art-123.pdf").read_bytes() == b"%PDF-1.4"


@pytest.mark.asyncio
async def test_local_artifact_storage_invalid_id():
    artifact_storage = LocalArtifactStorage()
    with pytest.raises(CvGenerationError):
        await artifact_storage.publish("../escape", "owner", b"tex", b"pdf")


# ---------------------------------------------------------------------------
# Data Adapter Tests
# ---------------------------------------------------------------------------


def test_resume_data_to_cv_content_standard():
    resume_data = {
        "full_name": "Nguyễn Văn A",
        "title": "Backend Engineer",
        "summary": "2 năm kinh nghiệm thiết kế RESTful API và cơ sở dữ liệu.",
        "skills": ["Python", "FastAPI", "PostgreSQL", "Docker"],
        "experiences": [
            {
                "company": "Công ty Công Nghệ ABC",
                "role": "Backend Developer",
                "period": "2022-01 - 2024-03",
                "bullet_points": [
                    "Xây dựng hệ thống API xử lý 10,000 requests/phút.",
                    "Tối ưu query PostgreSQL giảm latency 40%.",
                ],
            }
        ],
        "projects": [
            {
                "name": "E-Commerce Platform",
                "role": "Lead Backend",
                "tech_stack": ["FastAPI", "Redis"],
                "bullet_points": ["Tích hợp cổng thanh toán trực tuyến."],
            }
        ],
        "education": [
            {
                "institution": "Đại học Bách Khoa",
                "degree": "Kỹ sư",
                "period": "2018 - 2022",
            }
        ],
    }

    cv_content = resume_data_to_cv_content(resume_data)

    assert isinstance(cv_content, CvContent)
    assert cv_content.headline == "Backend Engineer"
    assert cv_content.summary == "2 năm kinh nghiệm thiết kế RESTful API và cơ sở dữ liệu."
    assert len(cv_content.skill_groups) == 1
    assert cv_content.skill_groups[0].items == [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Docker",
    ]

    assert len(cv_content.experience) == 1
    exp = cv_content.experience[0]
    assert exp.company == "Công ty Công Nghệ ABC"
    assert exp.roles == ["Backend Developer"]
    assert exp.start_date == "2022-01"
    assert exp.end_date == "2024-03"
    assert not exp.is_current
    assert len(exp.bullets) == 2

    assert len(cv_content.projects) == 1
    proj = cv_content.projects[0]
    assert proj.name == "E-Commerce Platform"
    assert proj.technologies == ["FastAPI", "Redis"]

    assert len(cv_content.education) == 1
    edu = cv_content.education[0]
    assert edu.institution == "Đại học Bách Khoa"
    assert edu.degree == "Kỹ sư"


def test_resume_data_to_cv_content_edge_cases():
    # Empty data should still create valid CvContent with sensible defaults (defaults to "Candidate")
    empty_data = {}
    cv_content = resume_data_to_cv_content(empty_data)
    assert isinstance(cv_content, CvContent)
    assert cv_content.headline == "Candidate"
    assert len(cv_content.skill_groups) == 1

    # When language="vi" explicitly passed, returns Vietnamese fallback
    cv_vi = resume_data_to_cv_content(empty_data, language="vi")
    assert cv_vi.headline == "Ứng viên"


def test_resume_data_to_cv_content_english_language():
    data = {
        "title": "Software Engineer",
        "skills": ["Python", "FastAPI"],
    }
    cv_content = resume_data_to_cv_content(data, language="en")
    assert isinstance(cv_content, CvContent)
    assert cv_content.headline == "Software Engineer"
    assert len(cv_content.skill_groups) == 1
    assert cv_content.skill_groups[0].label == "Technical Skills"


def test_resume_data_to_cv_content_with_additional_sections_and_certifications():
    data = {
        "title": "Backend Engineer",
        "certifications": [
            {"name": "AWS Certified Developer", "issuer": "Amazon", "issue_date": "2025"}
        ],
        "engineering_practices": [
            "Architecture: 3-layer architecture with Repository pattern",
            "Observability: Prometheus and Grafana",
        ],
        "additional_sections": [
            {
                "title": "AWARDS",
                "items": [{"label": "First Prize", "text": "Hackathon 2024"}],
            }
        ],
    }
    cv_content = resume_data_to_cv_content(data, language="en")
    assert len(cv_content.certifications) == 1
    assert cv_content.certifications[0].name == "AWS Certified Developer"
    assert len(cv_content.additional_sections) == 2
    titles = [s.title for s in cv_content.additional_sections]
    assert "AWARDS" in titles
    assert "ENGINEERING PRACTICES" in titles


# ---------------------------------------------------------------------------
# Tool Execution Tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_execute_cv_finalization_success(test_db: AsyncSession, current_user):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id=current_user.user_id,
        original_cv_text="CV gốc",
        target_jd_text="JD mẫu",
    )

    # Save suggestions and decisions
    await repo.save_suggestions(
        session.id,
        {
            "target_role": "Backend",
            "summary": "Tốt",
            "suggestions": [
                {
                    "id": "sug-1",
                    "section": "experience",
                    "target_original_text": "Làm CRUD",
                    "suggested_revised_text": "Tối ưu hóa API",
                    "reason": "Nâng cao chất lượng",
                }
            ],
        },
    )
    await repo.update_suggestion_decision(
        session_id=session.id,
        suggestion_id="sug-1",
        decision=CvDecisionType.APPROVED,
    )

    # Mock revised resume data
    await repo.save_revised_resume(
        session_id=session.id,
        resume_data={
            "full_name": "Nguyễn Văn A",
            "title": "Backend Dev",
            "summary": "Tóm tắt",
            "skills": ["Python"],
            "experiences": [
                {
                    "company": "Công ty A",
                    "role": "Dev",
                    "period": "2023",
                    "bullet_points": ["Tối ưu hóa API"],
                }
            ],
        },
    )

    # Mock generator service
    mock_service = MagicMock()
    mock_result = GenerateCvResult(
        status="succeeded",
        artifact_id="art-success",
        page_count=1,
        compiler="xelatex",
        files=[
            ArtifactFile(
                format="pdf",
                filename="cv.pdf",
                content_type="application/pdf",
                download_url="/download/art-success.pdf",
                expires_at=datetime.now(UTC),
            ),
            ArtifactFile(
                format="tex",
                filename="cv.tex",
                content_type="application/x-tex",
                download_url="/download/art-success.tex",
                expires_at=datetime.now(UTC),
            ),
        ],
    )
    mock_service.generate = AsyncMock(return_value=mock_result)

    ok, message, data = await execute_cv_finalization(
        db=test_db,
        session_id=session.id,
        user_id=current_user.user_id,
        service=mock_service,
    )

    assert ok is True
    assert "Xuất CV Hoàn Tất" in message
    assert "[cv.pdf](/download/art-success.pdf)" in message
    assert data["pdf_url"] == "/download/art-success.pdf"

    # Verify session updated in DB
    refreshed = await repo.get_session(session.id)
    assert refreshed.status == CvImprovementStep.PDF_GENERATED
    assert refreshed.pdf_url == "/download/art-success.pdf"


@pytest.mark.asyncio
async def test_execute_cv_finalization_no_decisions(test_db: AsyncSession, current_user):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id=current_user.user_id,
        original_cv_text="CV gốc",
        target_jd_text="JD mẫu",
    )

    ok, message, _ = await execute_cv_finalization(
        db=test_db,
        session_id=session.id,
        user_id=current_user.user_id,
    )

    assert ok is False
    assert "Chưa có gợi ý nào được người dùng chấp thuận" in message


@pytest.mark.asyncio
async def test_finalize_and_generate_cv_agent_tool(test_db: AsyncSession, current_user):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id=current_user.user_id,
        original_cv_text="CV gốc",
        target_jd_text="JD",
    )
    await repo.save_revised_resume(
        session_id=session.id,
        resume_data={
            "full_name": "A",
            "title": "Dev",
            "summary": "Summary",
            "skills": ["Java"],
        },
    )

    mock_service = MagicMock()
    mock_service.generate = AsyncMock(
        return_value=GenerateCvResult(
            status="succeeded",
            artifact_id="art-1",
            page_count=1,
            compiler="xelatex",
            files=[
                ArtifactFile(
                    format="pdf",
                    filename="cv.pdf",
                    content_type="application/pdf",
                    download_url="/dl/cv.pdf",
                    expires_at=datetime.now(UTC),
                )
            ],
        )
    )

    deps = AgentDeps(
        user=current_user,
        session_id=session.id,
        db=test_db,
        cv_generator_service=mock_service,
    )
    ctx = MagicMock(spec=RunContext)
    ctx.deps = deps

    res = await finalize_and_generate_cv(ctx, session_id=session.id)
    assert "Xuất CV Hoàn Tất" in res
    assert "[cv.pdf](/dl/cv.pdf)" in res


# ---------------------------------------------------------------------------
# API Route Tests (Download endpoint)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_download_endpoint(tmp_path, client):
    test_file = tmp_path / "sample_cv.pdf"
    test_file.write_bytes(b"%PDF-1.4 Mock PDF Content")

    # Set mock LocalStorageClient
    custom_storage = LocalStorageClient(base_dir=tmp_path)
    set_storage_client(custom_storage)

    try:
        # Success download
        res = await client.get("/ai/cv-improvement/download/sample_cv.pdf")
        assert res.status_code == 200
        assert res.content == b"%PDF-1.4 Mock PDF Content"
        assert res.headers["content-type"] == "application/pdf"

        # 404 for missing file
        res_404 = await client.get("/ai/cv-improvement/download/nonexistent.pdf")
        assert res_404.status_code == 404
    finally:
        set_storage_client(None)
