import pytest

from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)
from app.skill_schemas.cv_improvement import CvImprovementProposal, CvSuggestionItem


@pytest.mark.asyncio
async def test_create_and_get_session(test_db):
    repo = CvImprovementRepository(test_db)

    # 1. Create a session with nullable chat_session_id
    session = await repo.create_session(
        user_id="user-xyz-01",
        original_cv_text="Python Developer with 2 years experience building basic CRUD APIs.",
        target_jd_text="Senior Backend Engineer requiring FastAPI, PostgreSQL, Redis, Docker.",
        chat_session_id=None,
    )

    assert session.id is not None
    assert session.user_id == "user-xyz-01"
    assert session.chat_session_id is None
    assert session.status == CvImprovementStep.INIT
    assert session.step == CvImprovementStep.INIT
    assert session.proposals == {}
    assert session.user_decisions == {}
    assert session.revised_resume_data is None

    # 2. Get session by ID
    fetched = await repo.get_session(session.id)
    assert fetched is not None
    assert fetched.id == session.id
    assert fetched.original_cv_text.startswith("Python Developer")

    # 3. Get session with matching user_id
    matched = await repo.get_session(session.id, user_id="user-xyz-01")
    assert matched is not None

    # 4. Get session with wrong user_id returns None
    unmatched = await repo.get_session(session.id, user_id="wrong-user")
    assert unmatched is None


@pytest.mark.asyncio
async def test_save_suggestions_and_step_transition(test_db):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id="user-xyz-02",
        original_cv_text="Wrote CRUD APIs in Flask",
        target_jd_text="Backend Engineer",
    )

    # Save suggestions using Pydantic schema
    proposal = CvImprovementProposal(
        target_role="Backend Engineer",
        summary="Highlight async performance and caching.",
        strengths=["Flask basics"],
        missing_skills=["Redis", "FastAPI"],
        suggestions=[
            CvSuggestionItem(
                id="sugg-1",
                section="experience",
                target_original_text="Wrote CRUD APIs in Flask",
                suggested_revised_text="Architected RESTful endpoints in Flask, improving response latency by 25%",
                reason="Turn generic CRUD into measurable impact.",
            )
        ],
    )

    updated = await repo.save_suggestions(session.id, proposal)
    assert updated is not None
    assert updated.status == CvImprovementStep.WAITING_USER_REVIEW
    assert updated.step == CvImprovementStep.WAITING_USER_REVIEW
    assert len(updated.proposals["suggestions"]) == 1
    assert updated.proposals["suggestions"][0]["id"] == "sugg-1"

    # Transition step explicitly
    revising = await repo.transition_step(session.id, CvImprovementStep.REVISING)
    assert revising.status == CvImprovementStep.REVISING
    assert revising.step == CvImprovementStep.REVISING


@pytest.mark.asyncio
async def test_update_decisions(test_db):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id="user-xyz-03",
        original_cv_text="CV Text",
        target_jd_text="JD Text",
    )

    # User approves suggestion 1
    s1 = await repo.update_suggestion_decision(
        session_id=session.id,
        suggestion_id="sugg-1",
        decision=CvDecisionType.APPROVED,
    )
    assert s1.user_decisions["sugg-1"]["decision"] == "APPROVED"
    assert s1.user_decisions["sugg-1"]["final_text"] is None

    # User edits suggestion 2 with customized text
    s2 = await repo.update_suggestion_decision(
        session_id=session.id,
        suggestion_id="sugg-2",
        decision=CvDecisionType.EDITED,
        user_text="Engineered microservices using FastAPI and Redis caching.",
    )
    assert s2.user_decisions["sugg-2"]["decision"] == "EDITED"
    assert "FastAPI" in s2.user_decisions["sugg-2"]["final_text"]

    # User rejects suggestion 3
    s3 = await repo.update_suggestion_decision(
        session_id=session.id,
        suggestion_id="sugg-3",
        decision=CvDecisionType.REJECTED,
    )
    assert s3.user_decisions["sugg-3"]["decision"] == "REJECTED"

    # Batch update decisions
    batch = {
        "sugg-4": {"decision": "APPROVED", "final_text": None},
        "sugg-5": {"decision": "REJECTED", "final_text": None},
    }
    s_batch = await repo.update_all_decisions(session.id, batch)
    assert "sugg-4" in s_batch.user_decisions
    assert "sugg-5" in s_batch.user_decisions


@pytest.mark.asyncio
async def test_save_revised_resume_and_cv_generator_contract(test_db):
    """Verify storing revised CV data compatible with CV_GENERATOR_TOOL_INPUT.md contract."""
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id="user-xyz-04",
        original_cv_text="CV Text",
        target_jd_text="JD Text",
    )

    # Contract payload matching CV_GENERATOR_TOOL_INPUT.md
    cv_generator_payload = {
        "template_id": "classic",
        "language": "vi",
        "cv": {
            "headline": "Senior Backend Developer",
            "summary": "Lập trình viên backend có kinh nghiệm Spring Boot, PostgreSQL, Docker.",
            "skill_groups": [{"label": "Backend", "items": ["Python", "FastAPI", "PostgreSQL"]}],
            "experience": [
                {
                    "company": "Công ty Công nghệ ABC",
                    "roles": ["Backend Developer"],
                    "employment_type": "Full-time",
                    "location": "Hà Nội, Việt Nam",
                    "start_date": "2024-01",
                    "end_date": None,
                    "is_current": True,
                    "team_size": 5,
                    "bullets": [
                        "Xây dựng REST API xử lý 10,000 yêu cầu/phút bằng FastAPI.",
                        "Tối ưu hóa cơ sở dữ liệu PostgreSQL giảm độ trễ truy vấn 30%.",
                    ],
                }
            ],
            "projects": [],
            "education": [],
            "certifications": [],
            "additional_sections": [],
        },
    }

    saved = await repo.save_revised_resume(
        session_id=session.id,
        resume_data=cv_generator_payload,
        pdf_url="https://storage.occupify.vn/resumes/revised_123.pdf",
    )
    assert saved is not None
    assert saved.revised_resume_data["template_id"] == "classic"
    assert saved.revised_resume_data["cv"]["headline"] == "Senior Backend Developer"
    assert saved.pdf_url == "https://storage.occupify.vn/resumes/revised_123.pdf"


@pytest.mark.asyncio
async def test_rollback_and_reset(test_db):
    repo = CvImprovementRepository(test_db)
    session = await repo.create_session(
        user_id="user-xyz-05",
        original_cv_text="CV Text",
        target_jd_text="JD Text",
    )

    await repo.update_suggestion_decision(session.id, "s1", CvDecisionType.APPROVED)
    await repo.save_revised_resume(
        session.id, {"dummy": "data"}, pdf_url="http://example.com/a.pdf"
    )
    await repo.transition_step(session.id, CvImprovementStep.PDF_GENERATED)

    # Rollback decisions when user rejects all or cancels
    reset_session = await repo.reset_decisions(session.id)
    assert reset_session.user_decisions == {}
    assert reset_session.revised_resume_data is None
    assert reset_session.pdf_url is None
    assert reset_session.status == CvImprovementStep.WAITING_USER_REVIEW


@pytest.mark.asyncio
async def test_list_and_delete_sessions(test_db):
    repo = CvImprovementRepository(test_db)
    user_id = "user-xyz-06"

    s1 = await repo.create_session(user_id=user_id, original_cv_text="CV 1", target_jd_text="JD 1")
    s2 = await repo.create_session(user_id=user_id, original_cv_text="CV 2", target_jd_text="JD 2")

    sessions = await repo.list_sessions(user_id=user_id)
    assert len(sessions) == 2
    session_ids = {s.id for s in sessions}
    assert s1.id in session_ids
    assert s2.id in session_ids

    # Delete s1
    deleted = await repo.delete_session(s1.id, user_id=user_id)
    assert deleted is True

    # Confirm s1 is gone
    check = await repo.get_session(s1.id)
    assert check is None
