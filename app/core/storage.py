"""Storage clients and adapters for saving and serving CV artifacts."""

import base64
from abc import ABC, abstractmethod
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from app.core.logging import log_step
from app.features.cv_generator.schemas import ArtifactFile, CvGenerationError


class BaseStorageClient(ABC):
    @abstractmethod
    async def upload_file(
        self,
        file_bytes: bytes,
        filename: str,
        content_type: str = "application/pdf",
    ) -> str:
        """Upload file bytes and return a public/download URL."""
        ...


class LocalStorageClient(BaseStorageClient):
    """Local filesystem storage client for development, offline, or fallback mode."""

    def __init__(
        self,
        base_dir: str | Path = "data/resumes",
        base_url: str = "/ai/cv-improvement/download",
    ):
        self.base_dir = Path(base_dir)
        self.base_url = base_url.rstrip("/")
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _sanitize_filename(self, filename: str) -> str:
        # Strip directories to prevent path traversal
        clean = Path(filename).name
        if not clean or clean.startswith("."):
            clean = "artifact"
        return clean

    async def upload_file(
        self,
        file_bytes: bytes,
        filename: str,
        content_type: str = "application/pdf",
    ) -> str:
        safe_name = self._sanitize_filename(filename)
        dest = self.base_dir / safe_name
        dest.write_bytes(file_bytes)
        return f"{self.base_url}/{safe_name}"

    def get_file_path(self, filename: str) -> Path | None:
        safe_name = self._sanitize_filename(filename)
        path = self.base_dir / safe_name
        if path.is_file():
            return path
        return None


class CoreRpcStorageClient(BaseStorageClient):
    """Storage client delegating file persistence to Tuan's Core RPC microservice."""

    def __init__(
        self,
        rpc_client: Any = None,
        fallback: BaseStorageClient | None = None,
    ):
        self.rpc_client = rpc_client
        self.fallback = fallback or LocalStorageClient()

    async def upload_file(
        self,
        file_bytes: bytes,
        filename: str,
        content_type: str = "application/pdf",
    ) -> str:
        if self.rpc_client is not None:
            try:
                payload = {
                    "filename": filename,
                    "contentType": content_type,
                    "data": base64.b64encode(file_bytes).decode("ascii"),
                }
                res = await self.rpc_client.call("core.storage.upload", payload)
                if isinstance(res, dict) and res.get("ok"):
                    url = res.get("url") or res.get("data", {}).get("url")
                    if url:
                        return url
            except Exception as exc:
                log_step("storage.rpc_failed", error=str(exc))

        # Fallback to local storage if RPC not available or failed
        return await self.fallback.upload_file(file_bytes, filename, content_type)


class LocalArtifactStorage:
    """ArtifactStorage protocol implementation using local disk storage for CvGeneratorService."""

    def __init__(
        self,
        storage_client: LocalStorageClient | None = None,
        ttl_seconds: int = 86400,
    ):
        self.storage_client = storage_client or LocalStorageClient()
        self.ttl_seconds = ttl_seconds

    async def publish(
        self, artifact_id: str, owner_id: str, tex: bytes, pdf: bytes
    ) -> list[ArtifactFile]:
        if not artifact_id or "/" in artifact_id or ".." in artifact_id:
            raise CvGenerationError("INVALID_INPUT")

        expires = datetime.now(UTC) + timedelta(seconds=self.ttl_seconds)

        tex_filename = f"{artifact_id}.tex"
        pdf_filename = f"{artifact_id}.pdf"

        tex_url = await self.storage_client.upload_file(
            tex, tex_filename, content_type="application/x-tex; charset=utf-8"
        )
        pdf_url = await self.storage_client.upload_file(
            pdf, pdf_filename, content_type="application/pdf"
        )

        return [
            ArtifactFile(
                format="tex",
                filename="cv.tex",
                content_type="application/x-tex; charset=utf-8",
                download_url=tex_url,
                expires_at=expires,
            ),
            ArtifactFile(
                format="pdf",
                filename="cv.pdf",
                content_type="application/pdf",
                download_url=pdf_url,
                expires_at=expires,
            ),
        ]


_default_storage: BaseStorageClient | None = None


def get_storage_client() -> BaseStorageClient:
    global _default_storage
    if _default_storage is None:
        _default_storage = LocalStorageClient()
    return _default_storage


def set_storage_client(client: BaseStorageClient | None) -> None:
    global _default_storage
    _default_storage = client
