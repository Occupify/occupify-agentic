import json
from pathlib import Path

import jsonschema
import pytest

from app.messaging.mock_core import MockCoreRpc


@pytest.fixture
def rpc_schema() -> dict:
    schema_path = Path(__file__).parent / "core_project_rpc.schema.json"
    with open(schema_path, encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.asyncio
async def test_mock_replies_match_core_schema(rpc_schema):
    rpc = MockCoreRpc()

    # 1. Test search reply
    search_reply = await rpc.call("core.project.search", {"page": 0, "size": 10})
    jsonschema.validate(instance=search_reply, schema=rpc_schema)
    assert search_reply["ok"] is True
    assert "data" in search_reply["data"]
    assert "paging" in search_reply["data"]

    # Verify no employer anywhere in data
    for proj in search_reply["data"]["data"]:
        assert "employer" not in proj
        for job in proj.get("jobs", []):
            assert "employer" not in job

    # 2. Test get reply
    first_id = search_reply["data"]["data"][0]["id"]
    get_reply = await rpc.call("core.project.get", {"projectId": first_id})
    jsonschema.validate(instance=get_reply, schema=rpc_schema)
    assert get_reply["ok"] is True
    assert get_reply["data"]["data"]["id"] == first_id
    assert "employer" not in get_reply["data"]["data"]
    for job in get_reply["data"]["data"].get("jobs", []):
        assert "employer" not in job

    # 3. Test not found reply
    not_found_reply = await rpc.call(
        "core.project.get", {"projectId": "00000000-0000-0000-0000-000000000000"}
    )
    jsonschema.validate(instance=not_found_reply, schema=rpc_schema)
    assert not_found_reply["ok"] is False
    assert not_found_reply["error"]["code"] == "PROJECT_NOT_FOUND"
