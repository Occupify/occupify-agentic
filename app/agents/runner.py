import asyncio
import logging
import time
import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any

from pydantic_ai import Agent, capture_run_messages
from pydantic_ai.exceptions import (
    ContentFilterError,
    ModelContextWindowExceededError,
    ModelHTTPError,
    ModelRequestTimeout,
    ModelTimeoutError,
    UnexpectedModelBehavior,
    UsageLimitExceeded,
)
from pydantic_ai.messages import ModelMessagesTypeAdapter
from pydantic_ai.settings import ModelSettings
from pydantic_ai.usage import RunUsage, UsageLimits

from app.agents.deps import AgentDeps
from app.core.config import get_settings
from app.core.errors import (
    AppError,
    ChatContextFullError,
    ContentFilteredError,
    LlmUnavailableError,
)
from app.core.logging import bind_context, log_step
from app.db.repositories.runs import RunRepository
from app.llm.glm import get_model_settings


@dataclass
class AgentRunOutput:
    output: str
    user_model_messages: list[Any]
    assistant_model_messages: list[Any]
    tokens_in: int
    tokens_out: int
    run_id: str
    model: str
    latency_ms: int


@dataclass
class AgentStreamMeta:
    run_id: str
    model: str
    trace_id: str


@dataclass
class AgentStreamDelta:
    content: str


@dataclass
class AgentStreamDone:
    output: str
    user_model_messages: list[Any]
    assistant_model_messages: list[Any]
    tokens_in: int
    tokens_out: int
    latency_ms: int
    run_id: str
    model: str


@dataclass
class _RunContext:
    run_id: str
    trace_id: str
    model_name: str
    validated_history: list[Any]
    steps_log: list[dict[str, Any]]
    usage_limits: UsageLimits
    model_settings: ModelSettings
    start_time: float

    def record_step(self, event: str, level: int = logging.INFO, **fields: Any) -> None:
        step_entry = {
            "event": event,
            "ts": time.time(),
            "level": logging.getLevelName(level),
            **fields,
        }
        self.steps_log.append(step_entry)
        log_step(event, level=level, **fields)


def _extract_usage_from_messages(messages: list[Any]) -> RunUsage | None:
    run_usage = RunUsage()
    found = False
    for m in messages:
        req_usage = getattr(m, "usage", None)
        if req_usage is not None:
            found = True
            run_usage.incr(req_usage)
            run_usage.requests += 1
    return run_usage if found else None


def _extract_usage_fields(usage: Any, model_name: str) -> dict[str, Any]:
    if usage is None:
        return {
            "model": model_name,
            "tokens_in": 0,
            "tokens_out": 0,
            "tokens_cached": 0,
            "tokens_reasoning": 0,
            "tokens_total": 0,
            "requests": 0,
            "tokens_known": False,
        }
    tokens_in = getattr(usage, "input_tokens", 0) or 0
    tokens_cached = getattr(usage, "cache_read_tokens", 0) or 0
    tokens_out = getattr(usage, "output_tokens", 0) or 0
    tokens_reasoning = getattr(usage, "output_reasoning_tokens", 0) or 0
    tokens_total = tokens_in + tokens_out
    requests = getattr(usage, "requests", 0) or 0
    return {
        "model": model_name,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "tokens_cached": tokens_cached,
        "tokens_reasoning": tokens_reasoning,
        "tokens_total": tokens_total,
        "requests": requests,
        "tokens_known": True,
    }


def _map_llm_exception(exc: Exception) -> AppError:
    if isinstance(exc, ModelContextWindowExceededError):
        return ChatContextFullError()
    if isinstance(exc, ContentFilterError):
        return ContentFilteredError()
    if isinstance(exc, UsageLimitExceeded):
        return AppError(
            429, "Failed to complete: agent exceeded maximum request limit.", "LLM_USAGE_LIMIT"
        )
    if isinstance(exc, UnexpectedModelBehavior):
        msg = str(exc).lower()
        if (
            "context_window" in msg
            or "model_context_window_exceeded" in msg
            or "exceeded before any response was generated" in msg
            or ("token limit" in msg and "exceeded before" in msg)
            or "finish reason length" in msg
        ):
            return ChatContextFullError()
    if isinstance(exc, ModelHTTPError):
        code_str = ""
        msg_str = ""
        if isinstance(exc.body, dict):
            code_str = str(exc.body.get("code", "")).strip()
            msg_str = str(exc.body.get("message", "")).lower()
        elif isinstance(exc.body, str):
            msg_str = exc.body.lower()

        if exc.status_code == 400 and (
            code_str == "1261"
            or "context_window" in msg_str
            or "model_context_window_exceeded" in msg_str
        ):
            return ChatContextFullError()
        if exc.status_code == 400 and (code_str == "1301" or "sensitive" in msg_str):
            return ContentFilteredError()
        return LlmUnavailableError("Failed to reach the AI model. Please try again.")

    if isinstance(
        exc, (ModelTimeoutError, ModelRequestTimeout, TimeoutError, asyncio.TimeoutError)
    ):
        return LlmUnavailableError(
            "Failed to reach the AI model: request timed out. Please try again."
        )

    err_str = str(exc).lower()
    if (
        "context_window" in err_str
        or "context window" in err_str
        or "model_context_window_exceeded" in err_str
        or ("token limit" in err_str and "exceeded before" in err_str)
    ):
        return ChatContextFullError()
    if "sensitive" in err_str or "content filter" in err_str:
        return ContentFilteredError()
    return LlmUnavailableError("Failed to reach the AI model. Please try again.")


async def _setup_run(
    deps: AgentDeps,
    use_case: str,
    prompt: str,
    history: list[Any] | None,
) -> _RunContext:
    settings = get_settings()
    trace_id = str(uuid.uuid4())
    run_id = str(uuid.uuid4())
    model_name = settings.GLM_MODEL

    # 1. Parse and validate history BEFORE touching DB (F-27)
    validated_history = []
    if history:
        try:
            validated_history = ModelMessagesTypeAdapter.validate_python(history)
        except Exception as exc:
            log_step("history.parse_failed", error_type=type(exc).__name__)
            raise AppError(
                500, "Failed to load conversation history.", "HISTORY_PARSE_FAILED"
            ) from exc

    bind_context(
        trace_id=trace_id,
        run_id=run_id,
        use_case=use_case,
        user_id=deps.user.user_id,
        session_id=deps.session_id,
    )

    usage_limits = UsageLimits(request_limit=settings.GLM_MAX_REQUESTS_PER_RUN)
    model_settings = get_model_settings()
    start_time = time.perf_counter()

    ctx = _RunContext(
        run_id=run_id,
        trace_id=trace_id,
        model_name=model_name,
        validated_history=validated_history,
        steps_log=[],
        usage_limits=usage_limits,
        model_settings=model_settings,
        start_time=start_time,
    )

    ctx.record_step(
        "run.start",
        model=model_name,
        history_messages=len(validated_history),
        prompt_chars=len(prompt),
    )

    if deps.db:
        repo = RunRepository(deps.db)
        await repo.create_run(
            use_case=use_case,
            user_id=deps.user.user_id,
            session_id=deps.session_id,
            model=model_name,
            trace_id=trace_id,
            run_id=run_id,
        )

    return ctx


def _check_context_window(all_messages: list[Any]) -> None:
    for m in all_messages:
        provider_details = getattr(m, "provider_details", None) or {}
        raw_reason = ""
        if isinstance(provider_details, dict):
            raw_reason = str(
                provider_details.get("finish_reason") or provider_details.get("error") or ""
            ).lower()
        if "context_window" in raw_reason or "model_context_window_exceeded" in raw_reason:
            raise ChatContextFullError()
        if "sensitive" in raw_reason:
            raise ContentFilteredError()


async def _finish_run_success(
    deps: AgentDeps,
    ctx: _RunContext,
    usage: Any,
) -> tuple[int, dict[str, Any]]:
    duration_ms = int((time.perf_counter() - ctx.start_time) * 1000)
    u = _extract_usage_fields(usage, ctx.model_name)
    ctx.record_step(
        "run.end",
        ms=duration_ms,
        steps=len(ctx.steps_log) + 1,
        **u,
    )

    if deps.db:
        repo = RunRepository(deps.db)
        await repo.finish_success(
            run_id=ctx.run_id,
            tokens_in=u["tokens_in"],
            tokens_out=u["tokens_out"],
            latency_ms=duration_ms,
            steps=ctx.steps_log,
        )
    return duration_ms, u


async def _finish_run_failed(
    deps: AgentDeps,
    ctx: _RunContext,
    exc: Exception,
    usage: Any = None,
) -> None:
    duration_ms = int((time.perf_counter() - ctx.start_time) * 1000)
    safe_err = type(exc).__name__
    u = _extract_usage_fields(usage, ctx.model_name)
    ctx.record_step("run.error", level=logging.WARNING, ms=duration_ms, error_type=safe_err, **u)

    if deps.db:
        repo = RunRepository(deps.db)
        await repo.finish_failed(
            run_id=ctx.run_id,
            error_message=safe_err,
            latency_ms=duration_ms,
            steps=ctx.steps_log,
        )


async def run_agent(
    agent: Agent,
    prompt: str,
    deps: AgentDeps,
    use_case: str,
    history: list[Any] | None = None,
) -> AgentRunOutput:
    ctx = await _setup_run(deps, use_case, prompt, history)
    last_usage = None
    with capture_run_messages() as captured_messages:
        try:
            ctx.record_step(
                "llm.request",
                model=ctx.model_name,
                message_count=len(ctx.validated_history) + 1,
            )
            res = await agent.run(
                prompt,
                message_history=ctx.validated_history,
                deps=deps,
                usage_limits=ctx.usage_limits,
                model_settings=ctx.model_settings,
            )
            last_usage = getattr(res, "usage", None)
            all_new = res.new_messages()
            _check_context_window(all_new)

            usage = last_usage
            u = _extract_usage_fields(usage, ctx.model_name)
            ctx.record_step("llm.response", **u)

            user_msgs = [m for m in all_new if getattr(m, "kind", None) == "request"]
            asst_msgs = [m for m in all_new if getattr(m, "kind", None) == "response"]

            user_json = (
                ModelMessagesTypeAdapter.dump_python(user_msgs, mode="json") if user_msgs else []
            )
            asst_json = (
                ModelMessagesTypeAdapter.dump_python(asst_msgs, mode="json") if asst_msgs else []
            )

            duration_ms, u = await _finish_run_success(deps, ctx, usage)

            return AgentRunOutput(
                output=res.output if isinstance(res.output, str) else str(res.output),
                user_model_messages=user_json,
                assistant_model_messages=asst_json,
                tokens_in=u["tokens_in"],
                tokens_out=u["tokens_out"],
                run_id=ctx.run_id,
                model=ctx.model_name,
                latency_ms=duration_ms,
            )

        except Exception as exc:
            usage_to_log = last_usage or _extract_usage_from_messages(captured_messages)
            await _finish_run_failed(deps, ctx, exc, usage=usage_to_log)
            if isinstance(exc, AppError):
                raise exc
            raise _map_llm_exception(exc) from exc


async def stream_agent(
    agent: Agent,
    prompt: str,
    deps: AgentDeps,
    use_case: str,
    history: list[Any] | None = None,
) -> AsyncIterator[AgentStreamMeta | AgentStreamDelta | AgentStreamDone]:
    ctx = await _setup_run(deps, use_case, prompt, history)
    yield AgentStreamMeta(run_id=ctx.run_id, model=ctx.model_name, trace_id=ctx.trace_id)
    last_usage = None
    with capture_run_messages() as captured_messages:
        try:
            ctx.record_step(
                "llm.request",
                model=ctx.model_name,
                message_count=len(ctx.validated_history) + 1,
            )
            full_output_chunks: list[str] = []

            async with agent.run_stream(
                prompt,
                message_history=ctx.validated_history,
                deps=deps,
                usage_limits=ctx.usage_limits,
                model_settings=ctx.model_settings,
            ) as res:
                async for chunk in res.stream_text(delta=True, debounce_by=None):
                    full_output_chunks.append(chunk)
                    yield AgentStreamDelta(content=chunk)

                all_new = res.new_messages()
                last_usage = getattr(res, "usage", None)
                _check_context_window(all_new)

                usage = last_usage
                u = _extract_usage_fields(usage, ctx.model_name)
                ctx.record_step("llm.response", **u)

                user_msgs = [m for m in all_new if getattr(m, "kind", None) == "request"]
                asst_msgs = [m for m in all_new if getattr(m, "kind", None) == "response"]

                user_json = (
                    ModelMessagesTypeAdapter.dump_python(user_msgs, mode="json")
                    if user_msgs
                    else []
                )
                asst_json = (
                    ModelMessagesTypeAdapter.dump_python(asst_msgs, mode="json")
                    if asst_msgs
                    else []
                )

                duration_ms, u = await _finish_run_success(deps, ctx, usage)

                yield AgentStreamDone(
                    output="".join(full_output_chunks),
                    user_model_messages=user_json,
                    assistant_model_messages=asst_json,
                    tokens_in=u["tokens_in"],
                    tokens_out=u["tokens_out"],
                    latency_ms=duration_ms,
                    run_id=ctx.run_id,
                    model=ctx.model_name,
                )

        except asyncio.CancelledError:
            import anyio

            duration_ms = int((time.perf_counter() - ctx.start_time) * 1000)
            usage_to_log = last_usage or _extract_usage_from_messages(captured_messages)
            u = _extract_usage_fields(usage_to_log, ctx.model_name)
            ctx.record_step("run.interrupted", ms=duration_ms, **u)
            if deps.db:
                with anyio.CancelScope(shield=True):
                    repo = RunRepository(deps.db)
                    await repo.finish_failed(
                        run_id=ctx.run_id,
                        error_message="Client disconnected (interrupted)",
                        latency_ms=duration_ms,
                        steps=ctx.steps_log,
                    )
            raise

        except Exception as exc:
            usage_to_log = last_usage or _extract_usage_from_messages(captured_messages)
            await _finish_run_failed(deps, ctx, exc, usage=usage_to_log)
            if isinstance(exc, AppError):
                raise exc
            raise _map_llm_exception(exc) from exc
