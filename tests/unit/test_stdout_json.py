import json

import pytest
from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel

import app.documents.extract as extract_mod
from app.agents.deps import AgentDeps
from app.agents.runner import run_agent
from app.core.security import CurrentUser
from tests.unit.test_documents import generate_sample_pdf


@pytest.mark.docling
@pytest.mark.asyncio
async def test_stdout_only_json_lines(capsys, test_db, monkeypatch):
    monkeypatch.setattr(extract_mod.get_settings(), "PDF_EXTRACTOR", "docling")
    content = generate_sample_pdf(
        pages=1, text="Nguyen Van A\n## Experience\nSenior Backend Engineer"
    )
    text, pages, extractor = extract_mod.extract_pdf_text(content)
    assert extractor == "docling"
    assert "Senior Backend Engineer" in text

    user = CurrentUser(user_id="user-stdout", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-stdout", db=test_db)

    agent = Agent(model=TestModel())
    await run_agent(agent, "test output", deps, use_case="chat")

    captured = capsys.readouterr()
    stdout_lines = [line.strip() for line in captured.out.splitlines() if line.strip()]

    for line in stdout_lines:
        if line.startswith("INFO:") or line.startswith("WARNING:") or line.startswith("ERROR:"):
            # Uvicorn standard log format
            continue
        # Must parse as JSON
        try:
            data = json.loads(line)
            assert isinstance(data, dict)
            assert "ts" in data or "event" in data
        except json.JSONDecodeError:
            pytest.fail(f"Non-JSON line found on stdout: {line}")
