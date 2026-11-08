from datetime import datetime

from app.memory.schemas import MemoryItemRead, UserMemorySummary
from app.state.compactor import ContextCompactor
from app.state.schemas import TaskCheckpointRead


def test_context_compactor_rule_9_integrity():
    """Verify that all 9 mandatory fields are preserved in the compacted state card."""
    compactor = ContextCompactor(message_threshold=10)

    checkpoint = TaskCheckpointRead(
        id="cp-1",
        session_id="sess-1",
        user_id="user-1",
        task_type="career_consulting",
        stage="PATH_EXPLORATION",
        goal="Transition from Junior Frontend to Senior DevOps",
        constraints=["100% remote", "budget max 10h/week"],
        completed_steps=["Skill discovery", "Linux fundamentals verified"],
        pending_steps=["Select CI/CD tooling", "Formulate milestone schedule"],
        blockers=["Waiting on confirmation of GitHub Actions experience"],
        decisions=[
            {"decision": "Adopt GitHub Actions over Jenkins", "rationale": "Preferred by user"}
        ],
        next_action="Ask user about Docker experience",
        checkpoint_seq=3,
        created_at=datetime.now(),
    )

    memory = UserMemorySummary(
        items=[
            MemoryItemRead(
                id="mem-1",
                user_id="user-1",
                category="career",
                key="target_role",
                value="Senior DevOps",
                is_confirmed=True,
                confidence=1.0,
                source="user_chat",
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        ]
    )

    card = compactor.build_compacted_state_card(
        checkpoint=checkpoint,
        memory=memory,
        raw_message_count=15,
        evidence_references=["ESCO:devops_engineer", "ROADMAP:devops_roadmap"],
    )

    # Assert all 9 Rule 9 fields are present:
    assert "1. ORIGINAL GOAL: Transition from Junior Frontend to Senior DevOps" in card
    assert "2. CONFIRMED PROFILE FACTS: [career] target_role: Senior DevOps" in card
    assert "3. CONSTRAINTS & PREFERENCES: ['100% remote', 'budget max 10h/week']" in card
    assert "4. DECISIONS MADE & RATIONALE:" in card
    assert "Adopt GitHub Actions over Jenkins" in card
    assert (
        "5. COMPLETED WORK & ANALYSIS: ['Skill discovery', 'Linux fundamentals verified']" in card
    )
    assert "6. CURRENT STAGE & PROGRESS: PATH_EXPLORATION" in card
    assert (
        "7. OPEN QUESTIONS & BLOCKERS: ['Waiting on confirmation of GitHub Actions experience']"
        in card
    )
    assert "8. NEXT RECOMMENDED ACTION: Ask user about Docker experience" in card
    assert "9. EVIDENCE & HISTORY POINTERS: Full raw turns archived (count: 15)" in card
    assert "Evidence: [ESCO:devops_engineer, ROADMAP:devops_roadmap]" in card


def test_context_compactor_pruning():
    compactor = ContextCompactor(message_threshold=10)
    assert compactor.should_compact(5) is False
    assert compactor.should_compact(12) is True

    messages = [f"turn_{i}" for i in range(16)]
    compacted_history = compactor.compact_history(
        messages, compacted_card="card", keep_recent_turns=2
    )
    # Kept first turn (turn_0) and last 2 turns (turn_14, turn_15)
    assert len(compacted_history) == 3
    assert compacted_history[0] == "turn_0"
    assert compacted_history[1] == "turn_14"
    assert compacted_history[2] == "turn_15"
