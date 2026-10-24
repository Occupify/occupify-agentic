import json
import time
from typing import Any

from faststream.rabbit import RabbitBroker

from app.core.config import get_settings
from app.core.logging import get_current_context, log_step
from app.messaging.broker import get_broker
from app.messaging.topology import queue_name_for


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
        timeout_s: float | None = None,
    ) -> dict[str, Any]:
        settings = get_settings()
        timeout = timeout_s if timeout_s is not None else float(settings.RABBITMQ_RPC_TIMEOUT_S)
        ctx = get_current_context()

        headers = {
            "x-trace-id": ctx.get("trace_id", ""),
            "x-run-id": ctx.get("run_id", ""),
        }

        start_time = time.perf_counter()
        log_step("tool.call", tool=routing_key, args=args)

        try:
            # We can request against queue or exchange
            # By default FastStream supports routing via queue or exchange/routing_key
            target_queue = queue_name_for(routing_key)
            reply = await self.broker.request(
                message=args,
                queue=target_queue,
                timeout=timeout,
                headers=headers,
            )

            duration_ms = int((time.perf_counter() - start_time) * 1000)

            # Decode reply
            if hasattr(reply, "decode"):
                decoded = await reply.decode()
            elif hasattr(reply, "body"):
                decoded = json.loads(reply.body.decode("utf-8"))
            else:
                decoded = reply

            if isinstance(decoded, dict) and "ok" in decoded:
                envelope = decoded
            else:
                envelope = {"ok": True, "data": decoded}

            log_step("tool.result", tool=routing_key, ms=duration_ms, ok=envelope.get("ok", True))
            return envelope

        except TimeoutError:
            duration_ms = int((time.perf_counter() - start_time) * 1000)
            log_step(
                "tool.result", tool=routing_key, ms=duration_ms, ok=False, error_code="RPC_TIMEOUT"
            )
            return {
                "ok": False,
                "error": {
                    "code": "RPC_TIMEOUT",
                    "message": f"RPC call to `{routing_key}` timed out after {timeout} seconds.",
                },
            }
        except Exception as e:
            duration_ms = int((time.perf_counter() - start_time) * 1000)
            log_step(
                "tool.result", tool=routing_key, ms=duration_ms, ok=False, error_code="RPC_ERROR"
            )
            return {
                "ok": False,
                "error": {
                    "code": "RPC_ERROR",
                    "message": str(e),
                },
            }
