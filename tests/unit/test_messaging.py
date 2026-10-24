import pytest
from faststream.rabbit import RabbitBroker, RabbitExchange, TestRabbitBroker

from app.core.config import get_settings
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
    import asyncio

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
        assert reply["error"]["code"] == "RPC_TIMEOUT"
