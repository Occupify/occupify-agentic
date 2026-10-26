from app.core.config import get_settings
from app.messaging.mock_core import MockCoreRpc
from app.messaging.rpc import RpcClient


def get_core_rpc():
    """Returns MockCoreRpc or RpcClient according to settings.CORE_RPC_MODE."""
    settings = get_settings()
    if settings.CORE_RPC_MODE == "mock":
        return MockCoreRpc()
    return RpcClient()
