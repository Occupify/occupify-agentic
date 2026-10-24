import pytest
from faststream.rabbit import RabbitBroker, TestRabbitBroker

from app.messaging.rpc import RpcClient
from app.messaging.topology import queue_name_for


@pytest.mark.asyncio
async def test_rpc_request_reply_success():
    broker = RabbitBroker()

    @broker.subscriber(queue_name_for("core.job.get"))
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

    @broker.subscriber(queue_name_for("identity.profile.get"))
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
async def test_rpc_timeout():
    import asyncio

    broker = RabbitBroker()

    @broker.subscriber(queue_name_for("core.slow.task"))
    async def handle_slow(msg: dict):
        await asyncio.sleep(0.5)
        return {"ok": True}

    async with TestRabbitBroker(broker) as br:
        client = RpcClient(broker=br)
        reply = await client.call("core.slow.task", {"id": 1}, timeout_s=0.05)
        assert reply["ok"] is False
        assert reply["error"]["code"] == "RPC_TIMEOUT"
