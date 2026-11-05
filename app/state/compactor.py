from typing import Any

from app.core.logging import log_step
from app.memory.schemas import UserMemorySummary
from app.state.schemas import TaskCheckpointRead


class ContextCompactor:
    """
    Implements Rule 9 of Engineering Rules (doc/rule.md):
    Preserves all 9 essential fields:
    1. Original user goal.
    2. User-confirmed profile facts relevant to the goal.
    3. Constraints and preferences.
    4. Decisions already made and their rationale.
    5. Completed analysis or actions.
    6. Current task stage and progress.
    7. Open questions, blockers and risks.
    8. The next recommended action.
    9. References to supporting evidence and full session history.
    """

    def __init__(self, message_threshold: int = 12):
        self.message_threshold = message_threshold

    def should_compact(self, message_count: int) -> bool:
        return message_count >= self.message_threshold

    def build_compacted_state_card(
        self,
        checkpoint: TaskCheckpointRead | None,
        memory: UserMemorySummary | None,
        raw_message_count: int,
        evidence_references: list[str] | None = None,
    ) -> str:
        """
        Builds the canonical 9-field Markdown/XML state card from ground truth state.
        This provides a 100% deterministic foundation free from LLM summarization hallucinations.
        """
        goal = checkpoint.goal if checkpoint else "Career consulting and roadmap formulation"
        stage = checkpoint.stage if checkpoint else "DISCOVERY"
        seq = checkpoint.checkpoint_seq if checkpoint else 1
        constraints = checkpoint.constraints if checkpoint else []
        decisions = checkpoint.decisions if checkpoint else []
        completed = checkpoint.completed_steps if checkpoint else []
        pending = checkpoint.pending_steps if checkpoint else []
        blockers = checkpoint.blockers if checkpoint else []
        next_action = checkpoint.next_action if checkpoint else "Continue consulting discovery"

        # 2. User-confirmed profile facts
        confirmed_facts = []
        if memory and memory.items:
            for it in memory.items:
                if it.is_confirmed:
                    confirmed_facts.append(f"[{it.category}] {it.key}: {it.value}")
        confirmed_str = "; ".join(confirmed_facts) if confirmed_facts else "None recorded yet"

        # 9. Evidence references
        ev_refs = evidence_references or []
        ev_str = ", ".join(ev_refs) if ev_refs else "None attached"

        lines = [
            f'<COMPACTED_SESSION_STATE task_type="{checkpoint.task_type if checkpoint else "career_consulting"}" stage="{stage}" checkpoint_seq="{seq}">',
            f"1. ORIGINAL GOAL: {goal}",
            f"2. CONFIRMED PROFILE FACTS: {confirmed_str}",
            f"3. CONSTRAINTS & PREFERENCES: {constraints if constraints else 'None'}",
            f"4. DECISIONS MADE & RATIONALE: {decisions if decisions else 'None'}",
            f"5. COMPLETED WORK & ANALYSIS: {completed if completed else 'None'}",
            f"6. CURRENT STAGE & PROGRESS: {stage} (Pending: {pending})",
            f"7. OPEN QUESTIONS & BLOCKERS: {blockers if blockers else 'None'}",
            f"8. NEXT RECOMMENDED ACTION: {next_action}",
            f"9. EVIDENCE & HISTORY POINTERS: Full raw turns archived (count: {raw_message_count}); Evidence: [{ev_str}]",
            "</COMPACTED_SESSION_STATE>",
        ]
        card = "\n".join(lines)

        log_step(
            "state.compacted",
            stage=stage,
            checkpoint_seq=seq,
            raw_turns=raw_message_count,
            compacted_chars=len(card),
            preserved_decisions_count=len(decisions),
        )
        return card

    def compact_history(
        self,
        messages: list[Any],
        compacted_card: str,
        keep_recent_turns: int = 2,
    ) -> list[Any]:
        """
        Prunes middle turns of a dialogue history while keeping:
        - The first user turn (Anchor)
        - The compacted state card injected as system/context
        - The most recent N turns verbatim for conversational continuity.
        """
        if len(messages) <= keep_recent_turns + 2:
            return messages

        anchor_turn = messages[0]
        recent_turns = messages[-keep_recent_turns:]

        # Return anchor + recent turns (the state card is injected into prompt context)
        return [anchor_turn, *recent_turns]
