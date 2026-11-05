from unittest.mock import MagicMock

import pytest
from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.db.repositories.chat import ChatRepository
from app.features.chat.agent import chat_agent
from app.features.chat.service import ChatService
from app.memory.schemas import MemoryItemCreate
from app.memory.service import MemoryService
from app.state.schemas import TaskStateUpdate
from app.state.task_progress import TaskProgressManager
from app.state.tools import record_user_memory, update_consulting_progress


@pytest.mark.asyncio
async def test_record_user_memory_tool(test_db, mock_user):
    deps = AgentDeps(user=mock_user, session_id="test-sess", db=test_db)
    ctx = RunContext(deps=deps, model=None, usage=None, prompt=None)

    result = await record_user_memory(
        ctx=ctx,
        category="career",
        key="target_role",
        value="Senior DevOps Engineer",
        is_confirmed=True,
        confidence=1.0,
        source="user_chat",
    )

    assert "Recorded memory [career] target_role: Senior DevOps Engineer (confirmed)" in result

    # Verify memory is persisted in DB
    mem_svc = MemoryService(test_db)
    summary = await mem_svc.get_active_memory(mock_user.user_id)
    assert len(summary.items) == 1
    assert summary.items[0].key == "target_role"
    assert summary.items[0].value == "Senior DevOps Engineer"
    assert summary.items[0].is_confirmed is True

    # Error handling when db is unavailable
    no_db_deps = AgentDeps(user=mock_user, session_id="test-sess", db=None)
    no_db_ctx = RunContext(deps=no_db_deps, model=None, usage=None, prompt=None)
    err_res = await record_user_memory(ctx=no_db_ctx, category="career", key="k", value="v")
    assert "Error:" in err_res


@pytest.mark.asyncio
async def test_update_consulting_progress_tool(test_db, mock_user):
    chat_repo = ChatRepository(test_db)
    chat_sess = await chat_repo.create_session(mock_user.user_id, "Career Consulting Checkpoint")

    progress_stages = []

    async def on_progress(stage: str):
        progress_stages.append(stage)

    deps = AgentDeps(
        user=mock_user,
        session_id=chat_sess.id,
        db=test_db,
        on_progress=on_progress,
    )
    ctx = RunContext(deps=deps, model=None, usage=None, prompt=None)

    result = await update_consulting_progress(
        ctx=ctx,
        stage="ASSESSMENT",
        goal="Transition from SysAdmin to DevOps",
        completed_step="Initial discovery completed",
        pending_steps=["Review CI/CD experience", "Define target cloud"],
        blocker="Uncertain about AWS vs GCP",
        decision="Target AWS first",
        decision_rationale="Broader demand in current market",
        next_action="Explore AWS certification path",
    )

    assert "Checkpoint saved (seq=1)" in result
    assert "stage=ASSESSMENT" in result
    assert "next_action=Explore AWS certification path" in result
    assert "ASSESSMENT" in progress_stages

    # Verify checkpoint stored in database
    state_mgr = TaskProgressManager(test_db)
    cp = await state_mgr.get_latest_checkpoint(chat_sess.id)
    assert cp is not None
    assert cp.checkpoint_seq == 1
    assert cp.stage == "ASSESSMENT"
    assert cp.goal == "Transition from SysAdmin to DevOps"
    assert "Initial discovery completed" in cp.completed_steps
    assert "Review CI/CD experience" in cp.pending_steps
    assert "Uncertain about AWS vs GCP" in cp.blockers
    assert len(cp.decisions) == 1
    assert cp.decisions[0]["decision"] == "Target AWS first"
    assert cp.decisions[0]["rationale"] == "Broader demand in current market"

    # Error handling when session_id is None
    no_sess_deps = AgentDeps(user=mock_user, session_id=None, db=test_db)
    no_sess_ctx = RunContext(deps=no_sess_deps, model=None, usage=None, prompt=None)
    err_res = await update_consulting_progress(ctx=no_sess_ctx, stage="ASSESSMENT")
    assert "Error:" in err_res


def test_chat_agent_tool_registration():
    tool_names = set(chat_agent._function_toolset.tools.keys())
    assert "record_user_memory" in tool_names
    assert "update_consulting_progress" in tool_names


@pytest.mark.asyncio
async def test_chat_service_turn_prompt_injection(test_db, mock_user):
    chat_repo = ChatRepository(test_db)
    chat_sess = await chat_repo.create_session(mock_user.user_id, "Test Injection Session")

    # Record user memory
    mem_svc = MemoryService(test_db)
    await mem_svc.record_fact(
        mock_user.user_id,
        MemoryItemCreate(
            category="career",
            key="target_role",
            value="Site Reliability Engineer",
            is_confirmed=True,
            confidence=1.0,
        ),
    )

    # Save a checkpoint
    state_mgr = TaskProgressManager(test_db)
    await state_mgr.update_and_checkpoint(
        session_id=chat_sess.id,
        user_id=mock_user.user_id,
        task_type="career_consulting",
        update=TaskStateUpdate(
            stage="PATH_EXPLORATION",
            goal="Become Senior SRE",
            completed_steps=["Assessed Linux and networking fundamentals"],
            pending_steps=["Evaluate Kubernetes and Terraform knowledge"],
            next_action="Run Kubernetes scenario assessment",
        ),
    )

    chat_service = ChatService(test_db)
    (
        session_id,
        new_session,
        final_prompt,
        attachments_info,
        history,
        lock_token,
        turn_documents,
        persisted_attachments,
    ) = await chat_service._prepare_turn(
        user=mock_user,
        message="What is our next milestone?",
        context="User prefers remote roles",
        session_id=chat_sess.id,
        files=None,
    )

    assert session_id == chat_sess.id
    assert not new_session
    # Verify memory injection
    assert "<ACTIVE_USER_MEMORY>" in final_prompt
    assert "[career] target_role: Site Reliability Engineer" in final_prompt
    # Verify task state injection
    assert (
        '<CURRENT_TASK_STATE task_type="career_consulting" stage="PATH_EXPLORATION" seq="1">'
        in final_prompt
    )
    assert "Run Kubernetes scenario assessment" in final_prompt
    # Verify external user context
    assert "User prefers remote roles" in final_prompt
    # Verify user message
    assert "What is our next milestone?" in final_prompt


@pytest.mark.asyncio
async def test_chat_service_turn_compaction_injection(test_db, mock_user):
    chat_repo = ChatRepository(test_db)
    chat_sess = await chat_repo.create_session(mock_user.user_id, "Compaction Test Session")

    # Simulate 14 message turns in the session to trigger compaction threshold (>= 12)
    for i in range(7):
        user_msg = MagicMock()
        user_msg.model_dump = MagicMock(
            return_value={"role": "user", "parts": [f"Turn question {i}"]}
        )
        asst_msg = MagicMock()
        asst_msg.model_dump = MagicMock(
            return_value={"role": "model", "parts": [f"Turn answer {i}"]}
        )
        await chat_repo.save_turn(
            session_id=chat_sess.id,
            user_id=mock_user.user_id,
            user_display_text=f"Question {i}",
            assistant_display_text=f"Answer {i}",
            user_model_messages=[{"role": "user", "content": f"Question {i}"}],
            assistant_model_messages=[{"role": "model", "content": f"Answer {i}"}],
            attachments=[],
            client_message_id=None,
            run_id=f"run-{i}",
            tokens_in=10,
            tokens_out=20,
            status="complete",
        )

    # Save a checkpoint so compactor state card has rich content
    state_mgr = TaskProgressManager(test_db)
    await state_mgr.update_and_checkpoint(
        session_id=chat_sess.id,
        user_id=mock_user.user_id,
        task_type="career_consulting",
        update=TaskStateUpdate(
            stage="ROADMAP_FORMULATION",
            goal="Become Lead Cloud Architect",
            next_action="Draft 30-60-90 day learning milestones",
        ),
    )

    chat_service = ChatService(test_db)
    (
        session_id,
        new_session,
        final_prompt,
        attachments_info,
        compacted_history,
        lock_token,
        turn_documents,
        persisted_attachments,
    ) = await chat_service._prepare_turn(
        user=mock_user,
        message="Can we finalize the roadmap now?",
        context=None,
        session_id=chat_sess.id,
        files=None,
    )

    # Compaction triggered: 9-field state card present in prompt
    assert "<COMPACTED_SESSION_STATE" in final_prompt
    assert "1. ORIGINAL GOAL: Become Lead Cloud Architect" in final_prompt
    assert "6. CURRENT STAGE & PROGRESS: ROADMAP_FORMULATION" in final_prompt
    assert "8. NEXT RECOMMENDED ACTION: Draft 30-60-90 day learning milestones" in final_prompt
    assert "9. EVIDENCE & HISTORY POINTERS: Full raw turns archived (count: 14)" in final_prompt

    # History was compacted
    assert len(compacted_history) < 14


@pytest.mark.asyncio
async def test_dev_state_inspection_endpoint(client, test_db, mock_user):
    chat_repo = ChatRepository(test_db)
    chat_sess = await chat_repo.create_session(mock_user.user_id, "Dev Inspection Test")

    # 1. Inspect session with no state yet
    res = await client.get(f"/ai/dev/state/{chat_sess.id}")
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["session_id"] == chat_sess.id
    assert data["latest_checkpoint"] is None
    assert data["checkpoints_history"] == []
    assert data["active_user_memory"] == []

    # 2. Record memory and checkpoints
    mem_svc = MemoryService(test_db)
    await mem_svc.record_fact(
        mock_user.user_id,
        MemoryItemCreate(
            category="career",
            key="years_experience",
            value=5,
            is_confirmed=True,
        ),
    )

    state_mgr = TaskProgressManager(test_db)
    await state_mgr.update_and_checkpoint(
        session_id=chat_sess.id,
        user_id=mock_user.user_id,
        task_type="career_consulting",
        update=TaskStateUpdate(
            stage="DISCOVERY",
            goal="Consulting Discovery",
            completed_steps=["Gathered initial goals"],
            next_action="Assess technical skill gaps",
        ),
    )
    await state_mgr.update_and_checkpoint(
        session_id=chat_sess.id,
        user_id=mock_user.user_id,
        task_type="career_consulting",
        update=TaskStateUpdate(
            stage="ASSESSMENT",
            completed_steps=["Skill gaps assessed"],
            next_action="Explore career options",
        ),
    )

    # 3. Inspect updated state
    res = await client.get(f"/ai/dev/state/{chat_sess.id}")
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["session_id"] == chat_sess.id

    latest = data["latest_checkpoint"]
    assert latest is not None
    assert latest["checkpoint_seq"] == 2
    assert latest["stage"] == "ASSESSMENT"
    assert latest["next_action"] == "Explore career options"

    history = data["checkpoints_history"]
    assert len(history) == 2
    assert history[0]["stage"] == "DISCOVERY"
    assert history[1]["stage"] == "ASSESSMENT"

    active_mem = data["active_user_memory"]
    assert len(active_mem) == 1
    assert active_mem[0]["key"] == "years_experience"
    assert active_mem[0]["value"] == 5
    assert active_mem[0]["is_confirmed"] is True
