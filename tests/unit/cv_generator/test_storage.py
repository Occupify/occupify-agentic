import asyncio

import pytest
from botocore.exceptions import ClientError

from app.features.cv_generator.schemas import CvGenerationError
from app.features.cv_generator.storage import S3CompatibleArtifactStorage


class FakeS3:
    def __init__(self, fail_at=None):
        self.objects = {}
        self.fail_at = fail_at
        self.calls = 0

    def _maybe_fail(self):
        self.calls += 1
        if self.calls == self.fail_at:
            raise RuntimeError("secret response details")

    def put_object(self, **kwargs):
        self._maybe_fail()
        self.objects[kwargs["Key"]] = (kwargs["Body"], kwargs["ContentType"])

    def generate_presigned_url(self, operation, **kwargs):
        self._maybe_fail()
        assert operation == "get_object"
        return f"https://objectstorage.test.invalid/{kwargs['Params']['Key']}?signed=secret"

    def delete_object(self, **kwargs):
        self.objects.pop(kwargs["Key"], None)


async def test_publish_scopes_presigned_urls_to_objects_without_owner_pii():
    client = FakeS3()
    storage = S3CompatibleArtifactStorage(client, "private-bucket", ttl_seconds=86400)
    files = await storage.publish("artifact-1", "private-user", b"tex", b"pdf")
    assert {f.format for f in files} == {"tex", "pdf"}
    assert all("private-user" not in key for key in client.objects)
    assert {obj[1] for obj in client.objects.values()} == {
        "application/pdf",
        "application/x-tex; charset=utf-8",
    }
    assert all("signed=secret" in file.download_url for file in files)
    assert all(file.expires_at.tzinfo is not None for file in files)


@pytest.mark.parametrize("fail_at", [1, 2, 3, 4])
async def test_partial_publication_is_compensated(fail_at):
    client = FakeS3(fail_at)
    with pytest.raises(CvGenerationError) as exc:
        await S3CompatibleArtifactStorage(client, "bucket").publish("id", "user", b"t", b"p")
    assert exc.value.code in {"UPLOAD_FAILED", "LINK_CREATION_FAILED"}
    assert "secret" not in str(exc.value)
    assert client.objects == {}


async def test_cancel_waits_for_s3_completion_and_removes_partial_objects():
    import threading

    entered = threading.Event()
    release = threading.Event()

    class SlowS3(FakeS3):
        def put_object(self, **kwargs):
            entered.set()
            release.wait(timeout=3)
            super().put_object(**kwargs)

    client = SlowS3()
    task = asyncio.create_task(
        S3CompatibleArtifactStorage(client, "bucket").publish("id", "user", b"t", b"p")
    )
    await asyncio.to_thread(entered.wait, 2)
    task.cancel()
    release.set()
    with pytest.raises(asyncio.CancelledError):
        await task
    assert not client.objects


async def test_permission_denied_is_not_reported_as_retryable():
    class ForbiddenS3(FakeS3):
        def put_object(self, **kwargs):
            raise ClientError(
                {
                    "Error": {"Code": "AccessDenied", "Message": "private details"},
                    "ResponseMetadata": {"HTTPStatusCode": 403},
                },
                "PutObject",
            )

    with pytest.raises(CvGenerationError) as exc:
        await S3CompatibleArtifactStorage(ForbiddenS3(), "bucket").publish("id", "u", b"t", b"p")
    assert exc.value.retryable is False
    assert "private" not in str(exc.value)
