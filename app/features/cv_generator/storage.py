"""Publish CV artifacts through OCI Object Storage's S3-compatible API."""

import asyncio
import hashlib
import re
import threading
from datetime import UTC, datetime, timedelta
from typing import Protocol
from urllib.parse import urlsplit

from app.core.logging import log_step
from app.features.cv_generator.schemas import ArtifactFile, CvGenerationError


class ArtifactStorage(Protocol):
    async def publish(
        self, artifact_id: str, owner_id: str, tex: bytes, pdf: bytes
    ) -> list[ArtifactFile]: ...


class S3CompatibleArtifactStorage:
    def __init__(self, client, bucket: str, *, ttl_seconds: int = 86400):
        self.client = client
        self.bucket = bucket
        self.ttl_seconds = ttl_seconds
        self._slots = asyncio.Semaphore(2)

    def _cleanup(self, keys, artifact_id):
        for key in keys:
            try:
                self.client.delete_object(Bucket=self.bucket, Key=key)
            except Exception:
                log_step("cv_generator.cleanup_failed", artifact_id=artifact_id, resource="object")

    async def publish(
        self, artifact_id: str, owner_id: str, tex: bytes, pdf: bytes
    ) -> list[ArtifactFile]:
        from app.features.cv_generator.compiler import MAX_PDF_BYTES, MAX_TEX_BYTES

        if len(tex) > MAX_TEX_BYTES or len(pdf) > MAX_PDF_BYTES:
            raise CvGenerationError("INVALID_INPUT")
        # Never allow a caller-controlled artifact path, even from another internal consumer.
        if not artifact_id or "/" in artifact_id or ".." in artifact_id:
            raise CvGenerationError("INVALID_INPUT")
        cancelled = threading.Event()
        keys = []

        def operation():
            import botocore.exceptions

            owner = hashlib.sha256(owner_id.encode()).hexdigest()
            prefix = f"cv-generator/{owner}/{artifact_id}"
            expires = datetime.now(UTC) + timedelta(seconds=self.ttl_seconds)
            stage = "UPLOAD_FAILED"
            files = []
            try:
                for fmt, body, content_type in (
                    ("tex", tex, "application/x-tex; charset=utf-8"),
                    ("pdf", pdf, "application/pdf"),
                ):
                    if cancelled.is_set():
                        raise CvGenerationError(stage)
                    key = f"{prefix}/cv.{fmt}"
                    keys.append(key)  # Include uncertain successful PUTs in compensation.
                    self.client.put_object(
                        Bucket=self.bucket,
                        Key=key,
                        Body=body,
                        ContentType=content_type,
                    )

                stage = "LINK_CREATION_FAILED"
                for fmt, content_type in (
                    ("tex", "application/x-tex; charset=utf-8"),
                    ("pdf", "application/pdf"),
                ):
                    if cancelled.is_set():
                        raise CvGenerationError(stage)
                    key = f"{prefix}/cv.{fmt}"
                    url = self.client.generate_presigned_url(
                        "get_object",
                        Params={"Bucket": self.bucket, "Key": key},
                        ExpiresIn=self.ttl_seconds,
                        HttpMethod="GET",
                    )
                    files.append(
                        ArtifactFile(
                            format=fmt,
                            filename=f"cv.{fmt}",
                            content_type=content_type,
                            download_url=url,
                            expires_at=expires,
                        )
                    )
                return files
            except Exception as exc:
                self._cleanup(keys, artifact_id)
                keys.clear()
                response = getattr(exc, "response", {})
                status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
                retryable = (
                    isinstance(exc, (TimeoutError, ConnectionError))
                    or isinstance(
                        exc,
                        (
                            botocore.exceptions.EndpointConnectionError,
                            botocore.exceptions.ConnectTimeoutError,
                            botocore.exceptions.ReadTimeoutError,
                            botocore.exceptions.ConnectionClosedError,
                        ),
                    )
                    or status in (408, 429)
                    or (isinstance(status, int) and status >= 500)
                )
                raise CvGenerationError(stage, retryable=retryable) from None

        async with self._slots:
            task = asyncio.create_task(asyncio.to_thread(operation))
            try:
                return await asyncio.shield(task)
            except asyncio.CancelledError:
                cancelled.set()

                # The SDK call runs in a thread; wait for it before deleting its objects.
                async def finish_and_clean():
                    try:
                        await task
                    except Exception:
                        pass
                    await asyncio.to_thread(self._cleanup, keys, artifact_id)

                cleanup = asyncio.create_task(finish_and_clean())
                while not cleanup.done():
                    try:
                        await asyncio.shield(cleanup)
                    except asyncio.CancelledError:
                        continue
                cleanup.result()
                raise


def create_s3_storage(settings) -> S3CompatibleArtifactStorage:
    import boto3
    from botocore.config import Config

    if not all(
        (
            settings.S3_ACCESS_KEY,
            settings.S3_SECRET_KEY.get_secret_value(),
            settings.OCI_NAMESPACE,
            settings.OCI_BUCKET,
            settings.OCI_REGION,
        )
    ):
        raise CvGenerationError("STORAGE_NOT_CONFIGURED")
    if (
        not re.fullmatch(r"[A-Za-z0-9._-]{1,255}", settings.OCI_BUCKET)
        or settings.OCI_BUCKET == settings.S3_SECRET_KEY.get_secret_value()
    ):
        raise CvGenerationError("STORAGE_NOT_CONFIGURED")
    try:
        endpoint = settings.S3_ENDPOINT.strip().rstrip("/") or (
            f"https://{settings.OCI_NAMESPACE}.compat.objectstorage."
            f"{settings.OCI_REGION}.oraclecloud.com"
        )
        parsed_endpoint = urlsplit(endpoint)
        if (
            parsed_endpoint.scheme != "https"
            or not parsed_endpoint.netloc
            or parsed_endpoint.path
            or parsed_endpoint.query
            or parsed_endpoint.fragment
        ):
            raise ValueError("Invalid S3 endpoint")
        client = boto3.client(
            "s3",
            endpoint_url=endpoint,
            region_name=settings.OCI_REGION,
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY.get_secret_value(),
            config=Config(
                signature_version="s3v4",
                s3={"addressing_style": "path"},
                connect_timeout=5,
                read_timeout=10,
                retries={"total_max_attempts": 1},
            ),
        )
        return S3CompatibleArtifactStorage(
            client,
            settings.OCI_BUCKET,
            ttl_seconds=settings.CV_GENERATOR_LINK_TTL_S,
        )
    except Exception:
        raise CvGenerationError("STORAGE_NOT_CONFIGURED") from None
