import pytest
from sqlalchemy import select

from app.core.errors import AppError
from app.db.models import AgentRun
from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)
from app.features.cv_improvement.workflow import (
    CvImprovementWorkflow,
    format_decisions_for_prompt,
)
from app.skill_schemas.cv_improvement import (
    CvImprovementProposal,
    CvSuggestionItem,
    ResumeData,
    ResumeEducationItem,
    ResumeExperienceItem,
)


class MockAgent:
    def __init__(self, output):
        self.output = output

    async def run(self, prompt, deps=None):
        class Result:
            def __init__(self, out):
                self.output = out

        return Result(self.output)


@pytest.fixture
def sample_proposal():
    return CvImprovementProposal(
        target_role="Senior Python Engineer",
        summary="CV needs more impact metrics and less basic CRUD statements.",
        strengths=["Python basics", "FastAPI"],
        missing_skills=["Redis", "Docker", "CI/CD"],
        suggestions=[
            CvSuggestionItem(
                id="s1",
                section="Experience",
                target_original_text="Viết API CRUD cho sản phẩm",
                suggested_revised_text="Thiết kế và tối ưu RESTful API bằng FastAPI, giảm 30% latency.",
                reason="Thay đổi CRUD chung chung bằng số liệu định lượng.",
            ),
            CvSuggestionItem(
                id="s2",
                section="Experience",
                target_original_text="Tạo bảng trong cơ sở dữ liệu MySQL",
                suggested_revised_text="Thiết kế schema và đánh chỉ mục MySQL phục vụ 100k người dùng.",
                reason="Nhấn mạnh quy mô và kiến trúc DB.",
            ),
            CvSuggestionItem(
                id="s3",
                section="Projects",
                target_original_text="Làm giỏ hàng đơn giản",
                suggested_revised_text="Xây dựng luồng checkout an toàn xử lý 500 đơn hàng đồng thời.",
                reason="Bổ sung metric và tính phức tạp.",
            ),
        ],
    )


@pytest.fixture
def sample_revised_resume():
    return ResumeData(
        full_name="Nguyễn Văn A",
        title="Senior Python Backend Engineer",
        contact_info="nguyenvana@example.com | 0901234567",
        summary="Backend Engineer giàu kinh nghiệm tối ưu hóa REST API và kiến trúc cơ sở dữ liệu.",
        skills=["Python", "FastAPI", "MySQL", "Redis", "Docker"],
        experiences=[
            ResumeExperienceItem(
                company="Công ty Công nghệ ABC",
                role="Backend Developer",
                period="2023 - Nay",
                bullet_points=[
                    "Thiết kế và tối ưu RESTful API bằng FastAPI, giảm 30% latency.",
                    "Tạo bảng trong cơ sở dữ liệu MySQL",
                ],
            )
        ],
        projects=[],
        education=[
            ResumeEducationItem(
                institution="Đại học Công nghệ",
                degree="Kỹ sư Phần mềm",
                period="2019 - 2023",
            )
        ],
    )


@pytest.mark.asyncio
async def test_workflow_analysis_to_waiting_review(test_db, sample_proposal):
    mock_suggest = MockAgent(output=sample_proposal)
    workflow = CvImprovementWorkflow(test_db, suggest_agent=mock_suggest)

    # 1. Start session
    session = await workflow.start_session(
        user_id="user-hitl-1",
        original_cv_text="Viết API CRUD cho sản phẩm\nTạo bảng trong cơ sở dữ liệu MySQL",
        target_jd_text="Senior Python Backend Developer with FastAPI & Redis",
    )
    assert session.status == CvImprovementStep.INIT

    # 2. Run analysis
    analyzed_session = await workflow.analyze(session.id, user_id="user-hitl-1")
    assert analyzed_session.status == CvImprovementStep.WAITING_USER_REVIEW
    assert len(analyzed_session.proposals["suggestions"]) == 3
    assert analyzed_session.proposals["suggestions"][0]["id"] == "s1"


@pytest.mark.asyncio
async def test_workflow_decisions_and_validation(test_db, sample_proposal):
    workflow = CvImprovementWorkflow(test_db)
    repo = CvImprovementRepository(test_db)

    session = await repo.create_session(
        user_id="user-hitl-2",
        original_cv_text="CV original text",
        target_jd_text="JD text",
    )
    await repo.save_suggestions(session.id, sample_proposal)

    # Approve s1
    res1 = await workflow.decide(
        session_id=session.id,
        suggestion_id="s1",
        decision=CvDecisionType.APPROVED,
        user_id="user-hitl-2",
    )
    assert res1.user_decisions["s1"]["decision"] == "APPROVED"

    # Reject s2
    res2 = await workflow.decide(
        session_id=session.id,
        suggestion_id="s2",
        decision=CvDecisionType.REJECTED,
        user_id="user-hitl-2",
    )
    assert res2.user_decisions["s2"]["decision"] == "REJECTED"

    # Edit s3 with custom user text
    res3 = await workflow.decide(
        session_id=session.id,
        suggestion_id="s3",
        decision=CvDecisionType.EDITED,
        user_text="Tối ưu luồng checkout với Redis queue.",
        user_id="user-hitl-2",
    )
    assert res3.user_decisions["s3"]["decision"] == "EDITED"
    assert res3.user_decisions["s3"]["final_text"] == "Tối ưu luồng checkout với Redis queue."

    # Request alternative
    res4 = await workflow.decide(
        session_id=session.id,
        suggestion_id="s1",
        decision=CvDecisionType.REQUEST_ALTERNATIVE,
        user_id="user-hitl-2",
    )
    assert res4.user_decisions["s1"]["decision"] == "REQUEST_ALTERNATIVE"

    # Validation: EDITED without user_text raises AppError
    with pytest.raises(AppError) as exc_info:
        await workflow.decide(
            session_id=session.id,
            suggestion_id="s1",
            decision=CvDecisionType.EDITED,
            user_text="   ",
            user_id="user-hitl-2",
        )
    assert exc_info.value.error_code == "USER_TEXT_REQUIRED"

    # Validation: invalid decision value
    with pytest.raises(AppError) as exc_info2:
        await workflow.decide(
            session_id=session.id,
            suggestion_id="s1",
            decision="INVALID_STATUS",
            user_id="user-hitl-2",
        )
    assert exc_info2.value.error_code == "INVALID_DECISION"


@pytest.mark.asyncio
async def test_workflow_resume_and_recovery(test_db, sample_proposal, sample_revised_resume):
    mock_apply = MockAgent(output=sample_revised_resume)
    workflow = CvImprovementWorkflow(test_db, apply_agent=mock_apply)
    repo = CvImprovementRepository(test_db)

    session = await repo.create_session(
        user_id="user-hitl-3",
        original_cv_text="Viết API CRUD",
        target_jd_text="FastAPI Backend Engineer",
    )
    await repo.save_suggestions(session.id, sample_proposal)

    # User decides: approve s1, reject s2
    await workflow.decide(session.id, "s1", CvDecisionType.APPROVED, user_id="user-hitl-3")
    await workflow.decide(session.id, "s2", CvDecisionType.REJECTED, user_id="user-hitl-3")

    # Resume: applies changes and saves revised resume
    resumed = await workflow.resume(session.id, user_id="user-hitl-3")
    assert resumed.status == CvImprovementStep.APPLYING_CHANGES
    assert resumed.revised_resume_data is not None
    assert resumed.revised_resume_data["full_name"] == "Nguyễn Văn A"

    # Guard: Cannot resume if not in WAITING_USER_REVIEW
    with pytest.raises(AppError) as exc_info:
        await workflow.resume(session.id, user_id="user-hitl-3")
    assert exc_info.value.error_code == "INVALID_SESSION_STATE"

    # Recovery / Rollback: user decides to reject all and roll back
    recovered = await workflow.recovery(session.id, user_id="user-hitl-3")
    assert recovered.status == CvImprovementStep.WAITING_USER_REVIEW
    assert recovered.user_decisions == {}
    assert recovered.revised_resume_data is None
    assert recovered.pdf_url is None

    # After rollback, can decide again and resume cleanly
    await workflow.decide(
        session.id,
        "s1",
        CvDecisionType.EDITED,
        user_text="Tự sửa nội dung câu s1.",
        user_id="user-hitl-3",
    )
    resumed_again = await workflow.resume(session.id, user_id="user-hitl-3")
    assert resumed_again.status == CvImprovementStep.APPLYING_CHANGES
    assert resumed_again.revised_resume_data is not None


@pytest.mark.asyncio
async def test_format_decisions_for_prompt(sample_proposal):
    user_decisions = {
        "s1": {"decision": "APPROVED", "final_text": None},
        "s2": {"decision": "REJECTED", "final_text": None},
        "s3": {
            "decision": "EDITED",
            "final_text": "Xây dựng hệ thống giỏ hàng đồng thời.",
        },
    }
    result_text = format_decisions_for_prompt(sample_proposal.model_dump(), user_decisions)
    assert '- Gợi ý s1: APPROVED\n  Nội dung mới: "' in result_text
    assert "- Gợi ý s2: REJECTED (Giữ nguyên văn bản gốc)" in result_text
    assert (
        '- Gợi ý s3: EDITED (Người dùng tự sửa)\n  Nội dung mới: "Xây dựng hệ thống giỏ hàng đồng thời."'
        in result_text
    )


@pytest.mark.asyncio
async def test_cv_improvement_api_endpoints(client, test_db, sample_proposal):
    repo = CvImprovementRepository(test_db)

    # 1. POST /ai/cv-improvement/sessions
    resp_create = await client.post(
        "/ai/cv-improvement/sessions",
        json={
            "original_cv_text": "Lập trình viên backend",
            "target_jd_text": "Tuyển dụng Backend Engineer",
        },
    )
    assert resp_create.status_code == 200 or resp_create.status_code == 201
    data_create = resp_create.json()["data"]
    session_id = data_create["id"]
    assert data_create["status"] == "INIT"

    # Pre-populate suggestions for review test
    await repo.save_suggestions(session_id, sample_proposal)

    # 2. GET /ai/cv-improvement/{session_id}
    resp_get = await client.get(f"/ai/cv-improvement/{session_id}")
    assert resp_get.status_code == 200
    assert resp_get.json()["data"]["status"] == "WAITING_USER_REVIEW"

    # 3. POST /ai/cv-improvement/{session_id}/decide
    resp_decide = await client.post(
        f"/ai/cv-improvement/{session_id}/decide",
        json={"suggestion_id": "s1", "decision": "APPROVED"},
    )
    assert resp_decide.status_code == 200
    assert resp_decide.json()["data"]["user_decisions"]["s1"]["decision"] == "APPROVED"

    # 4. POST /ai/cv-improvement/{session_id}/batch-decide
    resp_batch = await client.post(
        f"/ai/cv-improvement/{session_id}/batch-decide",
        json={
            "decisions": [
                {"suggestion_id": "s2", "decision": "REJECTED"},
                {
                    "suggestion_id": "s3",
                    "decision": "EDITED",
                    "user_text": "Custom bullet point",
                },
            ]
        },
    )
    assert resp_batch.status_code == 200
    decisions = resp_batch.json()["data"]["user_decisions"]
    assert decisions["s2"]["decision"] == "REJECTED"
    assert decisions["s3"]["decision"] == "EDITED"

    # 5. POST /ai/cv-improvement/{session_id}/recovery
    resp_recovery = await client.post(f"/ai/cv-improvement/{session_id}/recovery")
    assert resp_recovery.status_code == 200
    recovered_data = resp_recovery.json()["data"]
    assert recovered_data["user_decisions"] == {}
    assert recovered_data["revised_resume_data"] is None

    # 6. Access control check: user-456 cannot access user-123's session
    resp_forbidden = await client.get(
        f"/ai/cv-improvement/{session_id}",
        headers={"X-User-Id": "other-user-456"},
    )
    assert resp_forbidden.status_code == 403


class FailingMockAgent:
    async def run(self, prompt, deps=None):
        raise RuntimeError("LLM request timed out")


@pytest.mark.asyncio
async def test_workflow_resume_rollback_on_failure(test_db, sample_proposal):
    workflow = CvImprovementWorkflow(test_db, apply_agent=FailingMockAgent())
    repo = CvImprovementRepository(test_db)

    session = await repo.create_session(
        user_id="user-fail-1",
        original_cv_text="Viết API CRUD",
        target_jd_text="FastAPI Backend Engineer",
    )
    await repo.save_suggestions(session.id, sample_proposal)
    await workflow.decide(session.id, "s1", CvDecisionType.APPROVED, user_id="user-fail-1")

    # Resume fails -> status must rollback to WAITING_USER_REVIEW
    with pytest.raises(RuntimeError, match="LLM request timed out"):
        await workflow.resume(session.id, user_id="user-fail-1")

    current = await workflow.get_session(session.id, user_id="user-fail-1")
    assert current.status == CvImprovementStep.WAITING_USER_REVIEW
    assert current.revised_resume_data is None


@pytest.mark.asyncio
async def test_workflow_auto_recovery_from_stuck_applying_changes(
    test_db, sample_proposal, sample_revised_resume
):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id="user-stuck-1",
        original_cv_text="Viết API CRUD",
        target_jd_text="FastAPI Backend Engineer",
    )
    await repo.save_suggestions(session.id, sample_proposal)
    # Simulate a session manually left in APPLYING_CHANGES without revised data
    await repo.transition_step(session.id, CvImprovementStep.APPLYING_CHANGES)

    # 1. batch_decide auto-recovers to WAITING_USER_REVIEW instead of crashing
    workflow = CvImprovementWorkflow(test_db)
    updated = await workflow.batch_decide(
        session.id,
        [{"suggestion_id": "s1", "decision": CvDecisionType.APPROVED}],
        user_id="user-stuck-1",
    )
    assert updated.status == CvImprovementStep.WAITING_USER_REVIEW
    assert updated.user_decisions["s1"]["decision"] == "APPROVED"

    # Put back into APPLYING_CHANGES
    await repo.transition_step(session.id, CvImprovementStep.APPLYING_CHANGES)

    # 2. resume allows retry when revised_resume_data is None
    mock_apply = MockAgent(output=sample_revised_resume)
    workflow_retry = CvImprovementWorkflow(test_db, apply_agent=mock_apply)
    resumed = await workflow_retry.resume(session.id, user_id="user-stuck-1")
    assert resumed.status == CvImprovementStep.APPLYING_CHANGES
    assert resumed.revised_resume_data is not None


@pytest.mark.asyncio
async def test_workflow_agent_run_tracing(test_db, sample_proposal, sample_revised_resume):
    mock_suggest = MockAgent(output=sample_proposal)
    mock_apply = MockAgent(output=sample_revised_resume)
    workflow = CvImprovementWorkflow(test_db, suggest_agent=mock_suggest, apply_agent=mock_apply)

    session = await workflow.start_session(
        user_id="user-trace-1",
        original_cv_text="CV Text",
        target_jd_text="JD Text",
    )

    # 1. Analyze tracing
    analyzed = await workflow.analyze(session.id, user_id="user-trace-1")
    assert analyzed.status == CvImprovementStep.WAITING_USER_REVIEW

    runs_stmt = select(AgentRun).where(
        AgentRun.session_id == session.id,
        AgentRun.model == "suggest-cv-improvements",
    )
    res = await test_db.execute(runs_stmt)
    analyze_run = res.scalar_one_or_none()
    assert analyze_run is not None
    assert analyze_run.use_case == "cv_improvement"
    assert analyze_run.status == "succeeded"
    assert analyze_run.trace_id is not None
    assert len(analyze_run.steps) >= 2

    # 2. Resume tracing
    await workflow.decide(session.id, "s1", CvDecisionType.APPROVED, user_id="user-trace-1")
    resumed = await workflow.resume(session.id, user_id="user-trace-1")
    assert resumed.status == CvImprovementStep.APPLYING_CHANGES

    runs_stmt_resume = select(AgentRun).where(
        AgentRun.session_id == session.id,
        AgentRun.model == "apply-cv-revisions",
    )
    res2 = await test_db.execute(runs_stmt_resume)
    resume_run = res2.scalar_one_or_none()
    assert resume_run is not None
    assert resume_run.use_case == "cv_improvement"
    assert resume_run.status == "succeeded"
    assert resume_run.trace_id is not None
    assert len(resume_run.steps) >= 2
