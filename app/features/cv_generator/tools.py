import asyncio
import hashlib
import json
from dataclasses import dataclass
from typing import Literal

from pydantic import ValidationError
from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.core.config import get_settings
from app.features.cv_generator.remote_compiler import RemoteCvCompiler
from app.features.cv_generator.schemas import (
    CvContent,
    CvGenerationError,
    GenerateCvInput,
    GenerateCvResult,
)
from app.features.cv_generator.service import CvGeneratorService
from app.features.cv_generator.storage import create_s3_storage


@dataclass
class _Memo:
    task: asyncio.Task
    waiters: int = 0


async def generate_cv(
    ctx: RunContext[AgentDeps],
    template_id: Literal["classic"],
    language: Literal["vi", "en"],
    cv: CvContent,
) -> GenerateCvResult:
    """Create editable LaTeX and a PDF from finished CV content; return download links.

    Call only after preparing factual CV content matching the agreed schema. This tool does
    not analyze a JD or invent/edit content. The document has fixed personal-contact
    placeholders for the user to replace in the .tex file. At most two A4 pages are allowed.
    On CONTENT_TOO_LONG shorten content before calling again. Never invent a download URL.
    """
    settings = get_settings()
    if not settings.CV_GENERATOR_ENABLED:
        return GenerateCvResult.failure(CvGenerationError("FEATURE_DISABLED"))
    owner = ctx.deps.user.user_id
    if not owner or not owner.strip():
        return GenerateCvResult.failure(CvGenerationError("UNAUTHORIZED"))
    try:
        payload = GenerateCvInput(template_id=template_id, language=language, cv=cv)
    except ValidationError as exc:
        result = GenerateCvResult.failure(CvGenerationError("INVALID_INPUT"))
        result.error.fields = [
            ".".join(map(str, e["loc"])) for e in exc.errors(include_input=False)
        ]
        return result
    digest = hashlib.sha256(
        json.dumps(payload.model_dump(), sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()
    key = json.dumps([owner, ctx.deps.session_id, ctx.deps.parent_run_id, "classic-v1", digest])
    memo = ctx.deps.cv_generator_memo
    entry = memo.get(key)
    if entry is None:
        if len(memo) >= 30:
            return GenerateCvResult.failure(CvGenerationError("BUSY", retryable=True))

        async def operation():
            try:
                async with asyncio.timeout(settings.CV_GENERATOR_TIMEOUT_S):
                    service = ctx.deps.cv_generator_service
                    if service is None:
                        storage = await asyncio.to_thread(create_s3_storage, settings)
                        service = CvGeneratorService(
                            RemoteCvCompiler(settings.CV_COMPILER_URL),
                            storage,
                            timeout_s=settings.CV_GENERATOR_TIMEOUT_S,
                        )
                        ctx.deps.cv_generator_service = service
                    return await service.generate(payload, owner)
            except TimeoutError:
                return GenerateCvResult.failure(CvGenerationError("TOOL_TIMEOUT", retryable=True))
            except CvGenerationError as exc:
                return GenerateCvResult.failure(exc)
            except Exception:
                return GenerateCvResult.failure(CvGenerationError("UPLOAD_FAILED"))

        entry = _Memo(asyncio.create_task(operation()))
        memo[key] = entry
    entry.waiters += 1
    try:
        result = await asyncio.shield(entry.task)
        if result.status == "failed":
            memo.pop(key, None)
        return result
    except asyncio.CancelledError:
        if entry.waiters == 1:
            entry.task.cancel()
            while not entry.task.done():
                try:
                    await asyncio.shield(entry.task)
                except asyncio.CancelledError:
                    continue
            memo.pop(key, None)
        raise
    finally:
        entry.waiters -= 1
