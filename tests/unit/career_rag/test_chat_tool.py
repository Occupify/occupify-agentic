from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.core.security import CurrentUser
from app.features.career_rag.chat_tool import consult_career_knowledge
from app.features.career_rag.schemas import (
    CareerRecommendation,
    Citation,
    GroundedCareerResponse,
)


@pytest.mark.asyncio
async def test_chat_tool_consult_career_knowledge_with_db():
    """Verify consult_career_knowledge tool execution with DB session in AgentDeps."""
    mock_db = AsyncMock()
    user = CurrentUser(user_id="user-123", role="ROLE_USER", email="user@example.com")
    deps = AgentDeps(user=user, db=mock_db)

    # Mock RunContext
    mock_ctx = MagicMock(spec=RunContext)
    mock_ctx.deps = deps

    expected_resp = GroundedCareerResponse(
        answer="### Lộ trình học Backend\n- Chi tiết bài học...",
        recommendations=[
            CareerRecommendation(
                claim="Học Python & FastAPI",
                evidence_citations=[
                    Citation(
                        chunk_id="chunk-1",
                        source_id="roadmap.sh",
                        source_record_id="backend",
                        title="Backend Roadmap",
                        snippet="Python web framework",
                    )
                ],
                confidence_level="high",
            )
        ],
        citations=[
            Citation(
                chunk_id="chunk-1",
                source_id="roadmap.sh",
                source_record_id="backend",
                title="Backend Roadmap",
                snippet="Python web framework",
            )
        ],
        abstention=False,
    )

    with patch(
        "app.features.career_rag.chat_tool.CareerConsultantService.consult",
        new=AsyncMock(return_value=expected_resp),
    ) as mock_consult:
        res = await consult_career_knowledge(
            ctx=mock_ctx,
            query="Lộ trình học Backend cho người mới",
            domain="software",
        )
        assert mock_consult.called
        assert "### Lộ trình học Backend" in res
        assert "- Chi tiết bài học..." in res


@pytest.mark.asyncio
async def test_chat_tool_consult_career_knowledge_without_db_in_deps():
    """Verify fallback to get_sessionmaker when ctx.deps.db is None."""
    user = CurrentUser(user_id="user-123", role="ROLE_USER", email="user@example.com")
    deps = AgentDeps(user=user, db=None)

    mock_ctx = MagicMock(spec=RunContext)
    mock_ctx.deps = deps

    expected_resp = GroundedCareerResponse(
        answer="Thông tin nghề nghiệp ESCO...",
        recommendations=[],
        citations=[],
        abstention=False,
    )

    mock_session_inst = AsyncMock()
    mock_maker = MagicMock()
    mock_maker.return_value.__aenter__.return_value = mock_session_inst
    mock_maker.return_value.__aexit__.return_value = None

    with (
        patch(
            "app.features.career_rag.chat_tool.get_sessionmaker",
            return_value=mock_maker,
        ),
        patch(
            "app.features.career_rag.chat_tool.CareerConsultantService.consult",
            new=AsyncMock(return_value=expected_resp),
        ) as mock_consult,
    ):
        res = await consult_career_knowledge(
            ctx=mock_ctx,
            query="Tiêu chuẩn kỹ sư phần mềm",
        )
        assert mock_consult.called
        assert "Thông tin nghề nghiệp ESCO..." in res
