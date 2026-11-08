from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class ConsultingStage(StrEnum):
    DISCOVERY = "DISCOVERY"
    ASSESSMENT = "ASSESSMENT"
    PATH_EXPLORATION = "PATH_EXPLORATION"
    ROADMAP_FORMULATION = "ROADMAP_FORMULATION"
    COMPLETED = "COMPLETED"


class TaskStateUpdate(BaseModel):
    stage: str | None = Field(default=None, description="Stage identifier, e.g. ASSESSMENT")
    goal: str | None = Field(default=None, description="Updated or refined goal")
    constraints_add: list[str] | None = Field(default=None, description="New constraints to append")
    completed_steps_add: list[str] | None = Field(
        default=None, description="Steps completed in this turn"
    )
    pending_steps: list[str] | None = Field(
        default=None, description="Explicit updated list of pending steps"
    )
    blockers_add: list[str] | None = Field(
        default=None, description="New blockers or open questions"
    )
    blockers_resolve: list[str] | None = Field(
        default=None, description="Blockers that were resolved"
    )
    decisions_add: list[dict[str, Any]] | None = Field(
        default=None,
        description="List of decisions with rationale, e.g. [{'decision': '...', 'rationale': '...'}]",
    )
    next_action: str | None = Field(default=None, description="Immediate next recommended action")


class TaskCheckpointRead(BaseModel):
    id: str
    session_id: str
    user_id: str
    task_type: str
    stage: str
    goal: str
    constraints: list[Any] = Field(default_factory=list)
    completed_steps: list[str] = Field(default_factory=list)
    pending_steps: list[str] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)
    decisions: list[dict[str, Any]] = Field(default_factory=list)
    next_action: str | None = None
    checkpoint_seq: int
    created_at: datetime

    def format_for_prompt(self) -> str:
        """Formats the current task checkpoint into a structured prompt context block."""
        lines = [
            f'<CURRENT_TASK_STATE task_type="{self.task_type}" stage="{self.stage}" seq="{self.checkpoint_seq}">',
            f"- Goal: {self.goal}",
        ]
        if self.constraints:
            lines.append(f"- Constraints: {self.constraints}")
        if self.completed_steps:
            lines.append(f"- Completed Steps: {self.completed_steps}")
        if self.pending_steps:
            lines.append(f"- Pending Steps: {self.pending_steps}")
        if self.blockers:
            lines.append(f"- Open Blockers/Questions: {self.blockers}")
        if self.decisions:
            lines.append(f"- Decisions Made: {self.decisions}")
        if self.next_action:
            lines.append(f"- Next Recommended Action: {self.next_action}")
        lines.append("</CURRENT_TASK_STATE>")
        return "\n".join(lines)
