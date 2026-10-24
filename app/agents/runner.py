import asyncio
import time
import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any

from pydantic_ai import Agent
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
from pydantic_ai.usage import UsageLimits

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
        if "token limit" in msg or "finish reason" in msg or "length" in msg or "context" in msg:
            return ChatContextFullError()
    if isinstance(exc, ModelHTTPError):
        body = (getattr(exc, "body", None) or str(exc)).lower()
        if exc.status_code == 400 and ("context" in body or "length" in body or "token" in body):
            return ChatContextFullError()
    if isinstance(exc, (ModelTimeoutError, ModelRequestTimeout)):
        return LlmUnavailableError("Request to AI model timed out. Please try again.")

    err_str = str(exc).lower()
    if (
        "context_window" in err_str
        or "context window" in err_str
        or "too long" in err_str
        or ("length" in err_str and "limit" in err_str)
    ):
        return ChatContextFullError()
    if "sensitive" in err_str or "content filter" in err_str or "policy" in err_str:
        return ContentFilteredError()
    return LlmUnavailableError()


async def run_agent(
    agent: Agent,
    prompt: str,
    deps: AgentDeps,
    use_case: str,
    history: list[Any] | None = None,
    trace_id: str | None = None,
) -> AgentRunOutput:
    settings = get_settings()
    trace_id = trace_id or str(uuid.uuid4())
    run_id = str(uuid.uuid4())
    model_name = settings.model_for(use_case)

    bind_context(
        trace_id=trace_id,
        run_id=run_id,
        use_case=use_case,
        user_id=deps.user.user_id,
        session_id=deps.session_id,
    )

    steps_log: list[dict[str, Any]] = []

    def record_step(event: str, **fields: Any):
        step_entry = {"event": event, "ts": time.time(), **fields}
        steps_log.append(step_entry)
        log_step(event, **fields)

    record_step(
        "run.start",
        model=model_name,
        history_messages=len(history or []),
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

    validated_history = []
    if history:
        try:
            validated_history = ModelMessagesTypeAdapter.validate_python(history)
        except Exception as exc:
            log_step("history.parse_failed", error=str(exc))
            raise AppError(
                500, "Failed to load conversation history.", "HISTORY_PARSE_FAILED"
            ) from exc

    usage_limits = UsageLimits(request_limit=settings.GLM_MAX_REQUESTS_PER_RUN)
    start_time = time.perf_counter()

    try:
        record_step("llm.request", model=model_name, message_count=len(validated_history) + 1)
        res = await agent.run(
            prompt,
            message_history=validated_history,
            deps=deps,
            usage_limits=usage_limits,
        )
        duration_ms = int((time.perf_counter() - start_time) * 1000)

        all_new = res.new_messages()
        for m in all_new:
            if getattr(m, "finish_reason", None) == "length":
                raise ChatContextFullError()

        usage = res.usage
        tokens_in = getattr(usage, "input_tokens", 0) or 0
        tokens_out = getattr(usage, "output_tokens", 0) or 0
        record_step("llm.response", tokens_in=tokens_in, tokens_out=tokens_out, ms=duration_ms)

        user_msgs = [m for m in all_new if getattr(m, "kind", None) == "request"]
        asst_msgs = [m for m in all_new if getattr(m, "kind", None) == "response"]

        user_json = (
            ModelMessagesTypeAdapter.dump_python(user_msgs, mode="json") if user_msgs else []
        )
        asst_json = (
            ModelMessagesTypeAdapter.dump_python(asst_msgs, mode="json") if asst_msgs else []
        )

        record_step(
            "run.end", ms=duration_ms, tokens_total=tokens_in + tokens_out, steps=len(steps_log)
        )

        if deps.db:
            repo = RunRepository(deps.db)
            await repo.finish_success(
                run_id=run_id,
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                latency_ms=duration_ms,
                steps=steps_log,
            )

        return AgentRunOutput(
            output=res.output if isinstance(res.output, str) else str(res.output),
            user_model_messages=user_json,
            assistant_model_messages=asst_json,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            run_id=run_id,
            model=model_name,
            latency_ms=duration_ms,
        )

    except Exception as exc:
        duration_ms = int((time.perf_counter() - start_time) * 1000)
        record_step("run.error", ms=duration_ms, error_type=type(exc).__name__, error=str(exc))

        if deps.db:
            repo = RunRepository(deps.db)
            await repo.finish_failed(
                run_id=run_id,
                error_message=str(exc),
                latency_ms=duration_ms,
                steps=steps_log,
            )

        if isinstance(exc, AppError):
            raise exc
        raise _map_llm_exception(exc) from exc


async def stream_agent(
    agent: Agent,
    prompt: str,
    deps: AgentDeps,
    use_case: str,
    history: list[Any] | None = None,
    trace_id: str | None = None,
) -> AsyncIterator[AgentStreamMeta | AgentStreamDelta | AgentStreamDone]:
    settings = get_settings()
    trace_id = trace_id or str(uuid.uuid4())
    run_id = str(uuid.uuid4())
    model_name = settings.model_for(use_case)

    bind_context(
        trace_id=trace_id,
        run_id=run_id,
        use_case=use_case,
        user_id=deps.user.user_id,
        session_id=deps.session_id,
    )

    steps_log: list[dict[str, Any]] = []

    def record_step(event: str, **fields: Any):
        step_entry = {"event": event, "ts": time.time(), **fields}
        steps_log.append(step_entry)
        log_step(event, **fields)

    record_step(
        "run.start",
        model=model_name,
        history_messages=len(history or []),
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

    validated_history = []
    if history:
        try:
            validated_history = ModelMessagesTypeAdapter.validate_python(history)
        except Exception as exc:
            log_step("history.parse_failed", error=str(exc))
            raise AppError(
                500, "Failed to load conversation history.", "HISTORY_PARSE_FAILED"
            ) from exc

    yield AgentStreamMeta(run_id=run_id, model=model_name, trace_id=trace_id)

    usage_limits = UsageLimits(request_limit=settings.GLM_MAX_REQUESTS_PER_RUN)
    start_time = time.perf_counter()

    try:
        record_step("llm.request", model=model_name, message_count=len(validated_history) + 1)
        full_output_chunks: list[str] = []

        async with agent.run_stream(
            prompt,
            message_history=validated_history,
            deps=deps,
            usage_limits=usage_limits,
        ) as res:
            async for chunk in res.stream_text(delta=True):
                full_output_chunks.append(chunk)
                yield AgentStreamDelta(content=chunk)

            all_new = res.new_messages()
            for m in all_new:
                if getattr(m, "finish_reason", None) == "length":
                    raise ChatContextFullError()

            duration_ms = int((time.perf_counter() - start_time) * 1000)
            usage = res.usage
            tokens_in = getattr(usage, "input_tokens", 0) or 0
            tokens_out = getattr(usage, "output_tokens", 0) or 0
            record_step("llm.response", tokens_in=tokens_in, tokens_out=tokens_out, ms=duration_ms)

            user_msgs = [m for m in all_new if getattr(m, "kind", None) == "request"]
            asst_msgs = [m for m in all_new if getattr(m, "kind", None) == "response"]

            user_json = (
                ModelMessagesTypeAdapter.dump_python(user_msgs, mode="json") if user_msgs else []
            )
            asst_json = (
                ModelMessagesTypeAdapter.dump_python(asst_msgs, mode="json") if asst_msgs else []
            )

            record_step(
                "run.end", ms=duration_ms, tokens_total=tokens_in + tokens_out, steps=len(steps_log)
            )

            if deps.db:
                repo = RunRepository(deps.db)
                await repo.finish_success(
                    run_id=run_id,
                    tokens_in=tokens_in,
                    tokens_out=tokens_out,
                    latency_ms=duration_ms,
                    steps=steps_log,
                )

            yield AgentStreamDone(
                output="".join(full_output_chunks),
                user_model_messages=user_json,
                assistant_model_messages=asst_json,
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                latency_ms=duration_ms,
                run_id=run_id,
                model=model_name,
            )

    except asyncio.CancelledError:
        duration_ms = int((time.perf_counter() - start_time) * 1000)
        record_step("run.interrupted", ms=duration_ms)
        if deps.db:
            repo = RunRepository(deps.db)
            await repo.finish_failed(
                run_id=run_id,
                error_message="Client disconnected (interrupted)",
                latency_ms=duration_ms,
                steps=steps_log,
            )
        raise

    except Exception as exc:
        duration_ms = int((time.perf_counter() - start_time) * 1000)
        record_step("run.error", ms=duration_ms, error_type=type(exc).__name__, error=str(exc))

        if deps.db:
            repo = RunRepository(deps.db)
            await repo.finish_failed(
                run_id=run_id,
                error_message=str(exc),
                latency_ms=duration_ms,
                steps=steps_log,
            )

        if isinstance(exc, AppError):
            raise exc
        raise _map_llm_exception(exc) from exc
