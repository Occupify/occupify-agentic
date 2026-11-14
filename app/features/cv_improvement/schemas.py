from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from app.db.repositories.cv_improvement import CvDecisionType


class CreateCvSessionRequest(BaseModel):
    original_cv_text: str = Field(
        ..., description="Raw text of candidate's original CV", min_length=1
    )
    target_jd_text: str = Field(..., description="Job Description text", min_length=1)
    chat_session_id: str | None = Field(
        default=None, description="Optional linked chat session ID"
    )


class CvDecisionRequest(BaseModel):
    suggestion_id: str = Field(..., description="ID of the suggestion to decide on")
    decision: CvDecisionType = Field(
        ..., description="Decision: APPROVED, REJECTED, EDITED, or REQUEST_ALTERNATIVE"
    )
    user_text: str | None = Field(
        default=None, description="Custom text required when decision is EDITED"
    )


class BatchCvDecisionRequest(BaseModel):
    decisions: list[CvDecisionRequest] = Field(..., min_length=1)


class CvSessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str
    chat_session_id: str | None = None
    status: str
    step: str | None = None
    original_cv_text: str
    target_jd_text: str
    proposals: dict[str, Any] = {}
    user_decisions: dict[str, Any] = {}
    revised_resume_data: dict[str, Any] | None = None
    pdf_url: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

