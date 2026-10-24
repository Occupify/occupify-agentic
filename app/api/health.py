from fastapi import APIRouter, Response, status
from sqlalchemy import text

from app.db.session import get_engine
from app.messaging.broker import get_broker

router = APIRouter(tags=["health"])


@router.get("/health")
async def health():
    return {"status": "UP"}


@router.get("/ready")
async def readiness(response: Response):
    db_status = "DOWN"
    broker_status = "DOWN"

    # Check Database
    try:
        engine = get_engine()
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        db_status = "UP"
    except Exception:
        db_status = "DOWN"

    # Check Broker
    try:
        broker = get_broker()
        # If broker is connected or test broker
        if hasattr(broker, "_connection") and broker._connection is not None:
            broker_status = "UP"
        else:
            broker_status = "UP"  # in local mode or stub
    except Exception:
        broker_status = "DOWN"

    is_ready = db_status == "UP"
    if not is_ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "UP" if is_ready else "DOWN",
        "checks": {
            "database": db_status,
            "broker": broker_status,
        },
    }
