"""Explicit opt-in OCI S3 Compatibility smoke using synthetic data."""

import hashlib
import os
import uuid

import httpx
import pytest

from app.core.config import Settings
from app.features.cv_generator.storage import create_s3_storage
from tests.unit.cv_generator.helpers import make_pdf


@pytest.mark.skipif(os.environ.get("CV_GENERATOR_S3_SMOKE") != "1", reason="OCI smoke is opt-in")
async def test_live_oci_s3_publish_download_and_cleanup():
    # The shared pytest setup disables .env loading; this opt-in cloud test needs it.
    storage = create_s3_storage(Settings(_env_file=".env"))
    artifact_id = str(uuid.uuid4())
    owner = "synthetic-cv-smoke"
    prefix = f"cv-generator/{hashlib.sha256(owner.encode()).hexdigest()}/{artifact_id}/"
    expected = {"tex": b"synthetic smoke source", "pdf": make_pdf()}
    try:
        files = await storage.publish(artifact_id, owner, expected["tex"], expected["pdf"])
        async with httpx.AsyncClient(trust_env=False, timeout=20) as client:
            for file in files:
                response = await client.get(file.download_url)
                assert response.status_code == 200
                assert response.content == expected[file.format]
                assert response.headers["content-type"].startswith(file.content_type.split(";")[0])
    finally:
        storage._cleanup([f"{prefix}cv.tex", f"{prefix}cv.pdf"], artifact_id)
