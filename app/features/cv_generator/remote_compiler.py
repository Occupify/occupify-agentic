"""HTTP client used by agentic to call the isolated compiler service."""

import httpx

from app.features.cv_generator.compiler import MAX_PDF_BYTES, MAX_TEX_BYTES
from app.features.cv_generator.schemas import CvGenerationError


class RemoteCvCompiler:
    def __init__(self, url: str, *, timeout_s: float = 35):
        self.url = url.rstrip("/") + "/compile"
        self.timeout_s = timeout_s

    async def compile(self, tex: str) -> bytes:
        body = tex.encode("utf-8")
        if len(body) > MAX_TEX_BYTES:
            raise CvGenerationError("INVALID_INPUT")
        try:
            async with httpx.AsyncClient(timeout=self.timeout_s, trust_env=False) as client:
                response = await client.post(
                    self.url, content=body, headers={"Content-Type": "application/x-tex"}
                )
        except httpx.TimeoutException:
            raise CvGenerationError("COMPILE_TIMEOUT", retryable=True) from None
        except httpx.RequestError:
            raise CvGenerationError("COMPILER_UNAVAILABLE", retryable=True) from None
        if response.status_code != 200:
            allowed = {
                "INVALID_INPUT",
                "BUSY",
                "COMPILER_UNAVAILABLE",
                "COMPILE_TIMEOUT",
                "COMPILE_FAILED",
                "LAYOUT_INVALID",
            }
            try:
                code = response.json().get("code")
            except ValueError:
                code = None
            if code not in allowed:
                code = "COMPILER_UNAVAILABLE" if response.status_code >= 500 else "COMPILE_FAILED"
            raise CvGenerationError(
                code,
                retryable=code in {"BUSY", "COMPILER_UNAVAILABLE", "COMPILE_TIMEOUT"},
            )
        if not response.content.startswith(b"%PDF-") or len(response.content) > MAX_PDF_BYTES:
            raise CvGenerationError("PDF_INVALID")
        return response.content
