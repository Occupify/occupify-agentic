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


class ResilientCvCompiler:
    """Tries remote compiler URLs and adapts Docker container hostnames to localhost when running on host."""

    def __init__(self, primary_url: str | None = None, *, timeout_s: float = 35):
        urls: list[str] = []
        if primary_url:
            urls.append(primary_url)
            if "cv-compiler" in primary_url:
                urls.append("http://127.0.0.1:8190")
                urls.append("http://localhost:8190")
        else:
            urls.extend(["http://127.0.0.1:8190", "http://localhost:8190"])

        unique_urls = list(dict.fromkeys(urls))
        self.compilers = [RemoteCvCompiler(u, timeout_s=timeout_s) for u in unique_urls]

    async def compile(self, tex: str) -> bytes:
        last_exc: Exception | None = None
        for compiler in self.compilers:
            try:
                return await compiler.compile(tex)
            except Exception as exc:
                last_exc = exc
                continue

        try:
            from app.features.cv_generator.compiler import LocalCvCompiler

            local = LocalCvCompiler()
            return await local.compile(tex)
        except Exception:
            if last_exc is not None:
                raise last_exc
            raise

