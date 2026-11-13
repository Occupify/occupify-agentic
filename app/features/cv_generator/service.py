import asyncio
import uuid

from app.core.logging import log_step
from app.features.cv_generator.compiler import CvCompiler, validate_pdf
from app.features.cv_generator.renderer import render_cv
from app.features.cv_generator.schemas import CvGenerationError, GenerateCvInput, GenerateCvResult
from app.features.cv_generator.storage import ArtifactStorage


class CvGeneratorService:
    def __init__(self, compiler: CvCompiler, storage: ArtifactStorage, *, timeout_s: int = 90):
        self.compiler = compiler
        self.storage = storage
        self.timeout_s = timeout_s

    async def generate(self, payload: GenerateCvInput, owner_id: str) -> GenerateCvResult:
        if not owner_id or not owner_id.strip():
            return GenerateCvResult.failure(CvGenerationError("UNAUTHORIZED"))
        artifact_id = str(uuid.uuid4())
        stage = "RENDER_FAILED"
        log_step("cv_generator.start", artifact_id=artifact_id)
        try:
            async with asyncio.timeout(self.timeout_s):
                tex = render_cv(payload)
                log_step(
                    "cv_generator.rendered", artifact_id=artifact_id, size_bytes=len(tex.encode())
                )
                stage = "COMPILE_FAILED"
                pdf = await self.compiler.compile(tex)
                page_count = await asyncio.to_thread(validate_pdf, pdf)
                log_step("cv_generator.compiled", artifact_id=artifact_id, page_count=page_count)
                stage = "UPLOAD_FAILED"
                files = await self.storage.publish(artifact_id, owner_id, tex.encode(), pdf)
                if {f.format for f in files} != {"tex", "pdf"} or len(files) != 2:
                    raise CvGenerationError("UPLOAD_FAILED")
                log_step("cv_generator.completed", artifact_id=artifact_id, page_count=page_count)
                return GenerateCvResult(
                    status="succeeded",
                    artifact_id=artifact_id,
                    page_count=page_count,
                    compiler="xelatex",
                    files=files,
                    warnings=["PERSONAL_DETAILS_ARE_PLACEHOLDERS"],
                )
        except TimeoutError:
            error = CvGenerationError("TOOL_TIMEOUT", retryable=True)
        except CvGenerationError as exc:
            error = exc
        except Exception:
            error = CvGenerationError(stage)
        log_step("cv_generator.failed", artifact_id=artifact_id, code=error.code)
        return GenerateCvResult.failure(error)
