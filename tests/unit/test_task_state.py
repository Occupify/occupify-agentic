import pytest

from app.db.models import ChatSession
from app.state.schemas import ConsultingStage, TaskStateUpdate
from app.state.task_progress import TaskProgressManager


@pytest.mark.asyncio
async def test_task_progress_manager_lifecycle(test_db):
    # 1. Create a parent session
    session = ChatSession(user_id="user-123", title="DevOps Consultation")
    test_db.add(session)
    await test_db.commit()
    await test_db.refresh(session)

    manager = TaskProgressManager(test_db)

    # 2. Initial checkpoint
    cp1 = await manager.update_and_checkpoint(
        session_id=session.id,
        user_id="user-123",
        task_type="career_consulting",
        update=TaskStateUpdate(
            stage=ConsultingStage.DISCOVERY,
            goal="Transition to Cloud DevOps Engineer",
            constraints_add=["Remote only"],
            completed_steps_add=["Profile discovery interview"],
            pending_steps=["Assess current Linux and Docker skills", "Identify gap to ESCO DevOps"],
            next_action="Ask user about current containerization experience",
        ),
    )
    assert cp1.checkpoint_seq == 1
    assert cp1.stage == "DISCOVERY"
    assert "Remote only" in cp1.constraints
    assert len(cp1.completed_steps) == 1
    assert len(cp1.pending_steps) == 2

    # 3. Transition to ASSESSMENT stage with decision and blocker
    cp2 = await manager.update_and_checkpoint(
        session_id=session.id,
        user_id="user-123",
        task_type="career_consulting",
        update=TaskStateUpdate(
            stage=ConsultingStage.ASSESSMENT,
            completed_steps_add=["Assess current Linux and Docker skills"],
            decisions_add=[
                {"decision": "Focus on Kubernetes first", "rationale": "High market demand in ESCO"}
            ],
            blockers_add=["User has not confirmed AWS account access"],
            next_action="Verify cloud sandbox availability",
        ),
    )
    assert cp2.checkpoint_seq == 2
    assert cp2.stage == "ASSESSMENT"
    assert len(cp2.completed_steps) == 2
    assert len(cp2.decisions) == 1
    assert len(cp2.blockers) == 1

    # 4. Resolve blocker and verify history
    cp3 = await manager.update_and_checkpoint(
        session_id=session.id,
        user_id="user-123",
        task_type="career_consulting",
        update=TaskStateUpdate(
            blockers_resolve=["User has not confirmed AWS account access"],
            next_action="Generate 4-week Kubernetes roadmap",
        ),
    )
    assert cp3.checkpoint_seq == 3
    assert len(cp3.blockers) == 0

    # 5. Recovery test: get latest checkpoint
    latest = await manager.get_latest_checkpoint(session.id, task_type="career_consulting")
    assert latest is not None
    assert latest.checkpoint_seq == 3
    assert latest.stage == "ASSESSMENT"
    assert latest.next_action == "Generate 4-week Kubernetes roadmap"

    # 6. Verify prompt formatting
    prompt_str = latest.format_for_prompt()
    assert (
        '<CURRENT_TASK_STATE task_type="career_consulting" stage="ASSESSMENT" seq="3">'
        in prompt_str
    )
    assert "Goal: Transition to Cloud DevOps Engineer" in prompt_str
    assert "Focus on Kubernetes first" in prompt_str
