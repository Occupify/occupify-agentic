from faststream.rabbit import RabbitBroker

from app.core.config import get_settings
from app.core.logging import log_step

_broker: RabbitBroker | None = None
_broker_connected: bool = False


def get_broker() -> RabbitBroker:
    global _broker
    if _broker is None:
        settings = get_settings()
        _broker = RabbitBroker(settings.RABBITMQ_URL)
    return _broker


def set_broker(broker: RabbitBroker) -> None:
    global _broker, _broker_connected
    _broker = broker
    _broker_connected = True


def is_broker_connected() -> bool:
    global _broker_connected
    return _broker_connected


async def start_broker() -> None:
    global _broker_connected
    broker = get_broker()
    try:
        await broker.start()
        _broker_connected = True
        log_step("broker.connected")
    except Exception as exc:
        _broker_connected = False
        log_step("broker.connect_failed", error_type=type(exc).__name__)


async def close_broker() -> None:
    global _broker, _broker_connected
    if _broker is not None:
        try:
            await _broker.close()
        except Exception:
            pass
        finally:
            _broker_connected = False
