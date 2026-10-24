import time
import uuid
from dataclasses import dataclass
from typing import Any

from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded
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


def _map_llm_exception(exc: Exception) -> AppError:
    err_str = str(exc).lower()
    if "context_window" in err_str or "context window" in err_str or "too long" in err_str:
        return ChatContextFullError()
    if "sensitive" in err_str or "content filter" in err_str or "policy" in err_str:
        return ContentFilteredError()
    if isinstance(exc, UsageLimitExceeded):
        return AppError(
            429, "Failed to complete: agent exceeded maximum request limit.", "LLM_USAGE_LIMIT"
        )
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

    # Insert agent_runs row
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

    # Prepare message history
    validated_history = []
    if history:
        try:
            validated_history = ModelMessagesTypeAdapter.validate_python(history)
        except Exception:
            validated_history = []

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

        usage = res.usage
        tokens_in = getattr(usage, "input_tokens", 0) or 0
        tokens_out = getattr(usage, "output_tokens", 0) or 0
        record_step("llm.response", tokens_in=tokens_in, tokens_out=tokens_out, ms=duration_ms)

        # Extract new messages for this turn
        all_new = res.new_messages()
        # Separate user and assistant messages
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
