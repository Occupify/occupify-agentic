import json
import time
import uuid
from typing import Any

from faststream.rabbit import RabbitBroker

from app.core.config import get_settings
from app.core.logging import get_current_context, log_step
from app.messaging.broker import get_broker
from app.messaging.topology import RPC_EXCHANGE


class RpcClient:
    def __init__(self, broker: RabbitBroker | None = None):
        self._broker = broker

    @property
    def broker(self) -> RabbitBroker:
        if self._broker is not None:
            return self._broker
        return get_broker()

    async def call(
        self,
        routing_key: str,
        args: dict[str, Any],
    ) -> dict[str, Any]:
        settings = get_settings()
        timeout = float(settings.RABBITMQ_RPC_TIMEOUT_S)
        ctx = get_current_context()

        tool_call_id = uuid.uuid4().hex[:8]

        headers = {
            "x-trace-id": ctx.get("trace_id", ""),
            "x-run-id": ctx.get("run_id", ""),
            "x-tool-call-id": tool_call_id,
        }

        # Log IDs and argument keys only to prevent payload/PII leakage (F-18)
        log_ids = {
            k: v
            for k, v in args.items()
            if "id" in k.lower() or k in ("id", "userId", "jobId", "projectId")
        }
        start_time = time.perf_counter()
        log_step(
            "tool.call",
            tool=routing_key,
            tool_call_id=tool_call_id,
            ids=log_ids,
            arg_keys=list(args.keys()),
        )

        try:
            reply = await self.broker.request(
                message=args,
                exchange=RPC_EXCHANGE,
                routing_key=routing_key,
                timeout=timeout,
                headers=headers,
            )

            duration_ms = int((time.perf_counter() - start_time) * 1000)

            # Calculate raw result bytes if possible
            result_bytes = 0
            if hasattr(reply, "body") and reply.body:
                result_bytes = len(reply.body)

            # Decode reply
            if hasattr(reply, "decode"):
                decoded = await reply.decode()
            elif hasattr(reply, "body"):
                decoded = json.loads(reply.body.decode("utf-8"))
            else:
                decoded = reply

            if not result_bytes and decoded:
                try:
                    result_bytes = len(json.dumps(decoded).encode("utf-8"))
                except Exception:
                    result_bytes = len(str(decoded))

            if isinstance(decoded, dict) and "ok" in decoded:
                envelope = decoded
            elif isinstance(decoded, dict) and decoded.get("statusCode", 200) >= 400:
                envelope = {
                    "ok": False,
                    "error": {
                        "code": decoded.get("errorCode", "ERROR"),
                        "message": decoded.get("message", "Request failed"),
                    },
                }
            else:
                envelope = {"ok": True, "data": decoded}

            # Determine result_count and status_code
            result_count = 0
            if envelope.get("ok", True):
                data = envelope.get("data", decoded)
                if isinstance(data, list):
                    result_count = len(data)
                elif isinstance(data, dict):
                    if "content" in data and isinstance(data["content"], list):
                        result_count = len(data["content"])
                    elif "data" in data and isinstance(data["data"], list):
                        result_count = len(data["data"])
                    else:
                        result_count = 1
                else:
                    result_count = 1

            status_code = 200
            if isinstance(decoded, dict) and "statusCode" in decoded:
                try:
                    status_code = int(decoded["statusCode"])
                except (ValueError, TypeError):
                    status_code = 200
            elif not envelope.get("ok", True):
                status_code = 400

            if envelope.get("ok", True):
                log_step(
                    "tool.result",
                    tool=routing_key,
                    tool_call_id=tool_call_id,
                    ms=duration_ms,
                    ok=True,
                    status_code=status_code,
                    result_count=result_count,
                    result_bytes=result_bytes,
                )
            else:
                err = envelope.get("error", {})
                log_step(
                    "tool.result",
                    tool=routing_key,
                    tool_call_id=tool_call_id,
                    ms=duration_ms,
                    ok=False,
                    status_code=status_code,
                    error_code=err.get("code", "ERROR") if isinstance(err, dict) else "ERROR",
                    error_message=err.get("message", "Request failed")
                    if isinstance(err, dict)
                    else str(err),
                    result_bytes=result_bytes,
                )

            return envelope

        except TimeoutError:
            duration_ms = int((time.perf_counter() - start_time) * 1000)
            log_step(
                "tool.result",
                tool=routing_key,
                tool_call_id=tool_call_id,
                ms=duration_ms,
                ok=False,
                status_code=504,
                error_code="RPC_TIMEOUT",
                error_message=f"RPC call to `{routing_key}` timed out after {timeout} seconds.",
            )
            return {
                "ok": False,
                "error": {
                    "code": "RPC_TIMEOUT",
                    "message": f"RPC call to `{routing_key}` timed out after {timeout} seconds.",
                },
            }
        except Exception as exc:
            duration_ms = int((time.perf_counter() - start_time) * 1000)
            log_step(
                "tool.result",
                tool=routing_key,
                tool_call_id=tool_call_id,
                ms=duration_ms,
                ok=False,
                status_code=500,
                error_code="RPC_ERROR",
                error_message=str(exc) or "Failed to communicate with downstream service.",
            )
            return {
                "ok": False,
                "error": {
                    "code": "RPC_ERROR",
                    "message": "Failed to communicate with downstream service.",
                },
            }
