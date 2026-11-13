"""Exercise the agent adapter and local TeX compiler without touching OCI."""

import asyncio
import os
from types import SimpleNamespace

import pytest

from app.agents.deps import AgentDeps
from app.core.config import get_settings
from app.core.security import CurrentUser
from app.features.cv_generator.compiler import validate_pdf
from app.features.cv_generator.schemas import CvContent
from app.features.cv_generator.service import CvGeneratorService
from app.features.cv_generator.storage import S3CompatibleArtifactStorage
from app.features.cv_generator.tools import generate_cv
from tests.integration.cv_generator.test_compile import compile_in_container
from tests.unit.cv_generator.helpers import sample_payload
from tests.unit.cv_generator.test_storage import FakeS3


@pytest.mark.skipif(
    not os.environ.get("CV_COMPILER_TEST_IMAGE"),
    reason="Set CV_COMPILER_TEST_IMAGE to run real TeX",
)
async def test_agent_tool_through_local_compiler_and_s3_compatible_publication(monkeypatch):
    monkeypatch.setattr(get_settings(), "CV_GENERATOR_ENABLED", True)

    # Host test delegates to the same LocalCvCompiler inside the application TeX runtime.
    class ContainerCompiler:
        async def compile(self, tex):
            return await asyncio.to_thread(compile_in_container, tex)

    client = FakeS3()
    service = CvGeneratorService(
        ContainerCompiler(),
        S3CompatibleArtifactStorage(client, "synthetic-bucket"),
    )
    deps = AgentDeps(
        user=CurrentUser(user_id="synthetic-pipeline-owner"),
        session_id="synthetic-session",
        parent_run_id="synthetic-run",
        cv_generator_service=service,
    )
    result = await generate_cv(
        SimpleNamespace(deps=deps),
        "classic",
        "vi",
        CvContent.model_validate(sample_payload()["cv"]),
    )
    assert result.status == "succeeded", result.error
    assert result.page_count == 1
    assert {file.format for file in result.files} == {"tex", "pdf"}
    stored = {key.rsplit(".", 1)[-1]: body for key, (body, _) in client.objects.items()}
    assert "[YOUR NAME]" in stored["tex"].decode()
    assert "synthetic-pipeline-owner" not in stored["tex"].decode()
    assert validate_pdf(stored["pdf"]) == 1
