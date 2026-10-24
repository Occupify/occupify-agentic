from faststream.rabbit import RabbitBroker

from app.core.config import get_settings

_broker: RabbitBroker | None = None


def get_broker() -> RabbitBroker:
    global _broker
    if _broker is None:
        settings = get_settings()
        _broker = RabbitBroker(settings.RABBITMQ_URL)
    return _broker


def set_broker(broker: RabbitBroker) -> None:
    global _broker
    _broker = broker


async def start_broker() -> None:
    broker = get_broker()
    try:
        await broker.start()
    except Exception:
        # In test environments or when RabbitMQ is not up, keep broker in offline mode
        pass


async def close_broker() -> None:
    global _broker
    if _broker is not None:
        try:
            await _broker.close()
        except Exception:
            pass
