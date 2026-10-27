from fastapi import APIRouter, Response, status
from sqlalchemy import text

from app.core.config import get_settings
from app.db.session import get_engine
from app.features.job_match.index import index_state, models_loaded
from app.messaging.broker import is_broker_connected

router = APIRouter(tags=["health"])


@router.get("/health")
async def health():
    return {"status": "UP"}


@router.get("/ready")
async def readiness(response: Response):
    settings = get_settings()
    db_status = "DOWN"

    # 1. Check Database
    try:
        engine = get_engine()
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        db_status = "UP"
    except Exception:
        db_status = "DOWN"

    # 2. Check Broker connection state
    broker_status = "UP" if is_broker_connected() else "DOWN"

    # 3. Informational index and models_loaded checks
    try:
        idx_state = await index_state()
    except Exception:
        idx_state = "missing"

    m_loaded = models_loaded()

    is_ready = (db_status == "UP") and (broker_status == "UP")
    if not is_ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "UP" if is_ready else "DOWN",
        "checks": {
            "database": db_status,
            "broker": broker_status,
            "index": idx_state,
            "models_loaded": m_loaded,
        },
    }
