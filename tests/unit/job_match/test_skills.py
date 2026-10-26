from pathlib import Path

import pytest
from app.features.job_match.pipeline import run_pipeline
from app.messaging.mock_core import MockCoreRpc

from app.features.job_match.ports import PipelineOptions, RunState


@pytest.mark.asyncio
async def test_each_stage_uses_its_library_skill(mock_user):
    # Verify that each stage invokes create_skill_agent with its canonical library skill
    used_skills: list[str] = []

    from app.agents import subagent

    orig_create = subagent.create_skill_agent

    def tracking_create(name: str, *args, **kwargs):
        used_skills.append(name)
        return orig_create(name, *args, **kwargs)

    subagent.create_skill_agent = tracking_create
    try:
        pdf_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()
        state = RunState()
        await run_pipeline(
            state=state,
            pdf_bytes=pdf_bytes,
            user=mock_user,
            core_rpc=MockCoreRpc(),
            options=PipelineOptions(),
        )

        assert "extract-candidate-profile" in used_skills
        assert "match-skills" in used_skills
        assert "assess-job-fit" in used_skills
    finally:
        subagent.create_skill_agent = orig_create


@pytest.mark.asyncio
async def test_skill_version_logged_and_stored(mock_user):
    pdf_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=pdf_bytes,
        user=mock_user,
        core_rpc=MockCoreRpc(),
        options=PipelineOptions(),
    )
    assert isinstance(res.skill_versions, dict)
    assert "extract-candidate-profile" in res.skill_versions
    assert "match-skills" in res.skill_versions
    assert "assess-job-fit" in res.skill_versions
    for name, v in res.skill_versions.items():
        assert len(v) == 12
