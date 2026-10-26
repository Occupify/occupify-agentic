import asyncio

import pytest
from faststream.rabbit import RabbitBroker, RabbitExchange, RabbitMessage, TestRabbitBroker

from app.core.config import get_settings
from app.core.logging import bind_context
from app.messaging.rpc import RpcClient
from app.messaging.topology import RPC_EXCHANGE


@pytest.mark.asyncio
async def test_rpc_request_reply_success():
    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    @broker.subscriber("core.job.get", exchange=exchange)
    async def handle_job(msg: dict):
        return {"ok": True, "data": {"jobId": msg.get("jobId"), "title": "Senior Python Dev"}}

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.job.get", {"jobId": "job-101"})
        assert reply["ok"] is True
        assert reply["data"]["title"] == "Senior Python Dev"


@pytest.mark.asyncio
async def test_rpc_request_reply_error_envelope():
    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    @broker.subscriber("identity.profile.get", exchange=exchange)
    async def handle_profile(msg: dict):
        return {
            "ok": False,
            "error": {"code": "PROFILE_NOT_FOUND", "message": "Profile does not exist"},
        }

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("identity.profile.get", {"userId": "user-404"})
        assert reply["ok"] is False
        assert reply["error"]["code"] == "PROFILE_NOT_FOUND"


@pytest.mark.asyncio
async def test_rpc_timeout(monkeypatch):
    monkeypatch.setattr(get_settings(), "RABBITMQ_RPC_TIMEOUT_S", 0.05)
    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    @broker.subscriber("core.slow.task", exchange=exchange)
    async def handle_slow(msg: dict):
        await asyncio.sleep(0.5)
        return {"ok": True}

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.slow.task", {"id": 1})
        assert reply["ok"] is False


@pytest.mark.asyncio
async def test_rpc_logs_tool_call_and_result_fields(monkeypatch):
    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    logged_steps = []

    def mock_log_step(event, **fields):
        logged_steps.append((event, fields))

    monkeypatch.setattr("app.messaging.rpc.log_step", mock_log_step)

    @broker.subscriber("core.project.search", exchange=exchange)
    async def handle_search(msg: dict):
        return {
            "statusCode": 200,
            "content": [{"id": "p1"}, {"id": "p2"}, {"id": "p3"}],
            "totalElements": 3,
        }

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.project.search", {"keyword": "backend", "projectId": "p1"})
        assert reply["ok"] is True

    call_events = [f for e, f in logged_steps if e == "tool.call"]
    result_events = [f for e, f in logged_steps if e == "tool.result"]

    assert len(call_events) == 1
    assert len(result_events) == 1

    call_f = call_events[0]
    result_f = result_events[0]

    # Verify tool_call_id is shared between tool.call and tool.result
    assert "tool_call_id" in call_f
    assert len(call_f["tool_call_id"]) == 8
    assert call_f["tool_call_id"] == result_f["tool_call_id"]

    # Verify call logging fields
    assert call_f["tool"] == "core.project.search"
    assert call_f["ids"] == {"projectId": "p1"}
    assert set(call_f["arg_keys"]) == {"keyword", "projectId"}

    # Verify result logging fields
    assert result_f["tool"] == "core.project.search"
    assert result_f["ok"] is True
    assert result_f["status_code"] == 200
    assert result_f["result_count"] == 3
    assert result_f["result_bytes"] > 0
    assert result_f["ms"] >= 0


@pytest.mark.asyncio
async def test_rpc_sends_tool_call_id_header(monkeypatch):
    bind_context(trace_id="trace-hdr-123", run_id="run-hdr-456")

    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    captured_headers = {}

    @broker.subscriber("core.header.check", exchange=exchange)
    async def handle_headers(msg: dict, msg_obj: RabbitMessage):
        captured_headers.update(msg_obj.headers)
        return {"ok": True, "data": "received"}

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.header.check", {"sample": 1})
        assert reply["ok"] is True

    assert captured_headers.get("x-trace-id") == "trace-hdr-123"
    assert captured_headers.get("x-run-id") == "run-hdr-456"
    assert "x-tool-call-id" in captured_headers
    assert len(captured_headers["x-tool-call-id"]) == 8


@pytest.mark.asyncio
async def test_rpc_error_envelope_logs_error_fields(monkeypatch):
    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    logged_steps = []

    def mock_log_step(event, **fields):
        logged_steps.append((event, fields))

    monkeypatch.setattr("app.messaging.rpc.log_step", mock_log_step)

    @broker.subscriber("core.project.error", exchange=exchange)
    async def handle_error(msg: dict):
        return {
            "statusCode": 404,
            "errorCode": "PROJECT_NOT_FOUND",
            "message": "Project with specified ID does not exist",
        }

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.project.error", {"projectId": "missing-uuid"})
        assert reply["ok"] is False
        assert reply["error"]["code"] == "PROJECT_NOT_FOUND"

    result_events = [f for e, f in logged_steps if e == "tool.result"]
    assert len(result_events) == 1
    res_f = result_events[0]

    assert res_f["ok"] is False
    assert res_f["status_code"] == 404
    assert res_f["error_code"] == "PROJECT_NOT_FOUND"
    assert res_f["error_message"] == "Project with specified ID does not exist"
    assert res_f["result_bytes"] > 0


@pytest.mark.asyncio
async def test_rpc_timeout_logs_504(monkeypatch):
    monkeypatch.setattr(get_settings(), "RABBITMQ_RPC_TIMEOUT_S", 0.05)
    broker = RabbitBroker()
    exchange = RabbitExchange(RPC_EXCHANGE, auto_delete=True)

    logged_steps = []

    def mock_log_step(event, **fields):
        logged_steps.append((event, fields))

    monkeypatch.setattr("app.messaging.rpc.log_step", mock_log_step)

    @broker.subscriber("core.slow.endpoint", exchange=exchange)
    async def handle_slow(msg: dict):
        await asyncio.sleep(0.5)
        return {"ok": True}

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.slow.endpoint", {"projectId": "timeout-1"})
        assert reply["ok"] is False

    result_events = [f for e, f in logged_steps if e == "tool.result"]
    assert len(result_events) == 1
    res_f = result_events[0]

    assert res_f["ok"] is False
    assert res_f["status_code"] == 504
    assert res_f["error_code"] == "RPC_TIMEOUT"
    assert "timed out" in res_f["error_message"]
