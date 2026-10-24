from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api import dev, health
from app.core.config import get_settings
from app.core.errors import AppError
from app.core.logging import log_step, setup_logging
from app.db.init import init_db
from app.features.chat import router as chat_router
from app.messaging.broker import close_broker, start_broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    setup_logging()

    models_info = {
        "chat": settings.model_for("chat"),
        "roadmap": settings.model_for("roadmap"),
        "cv_match": settings.model_for("cv_match"),
        "applicant_ranking": settings.model_for("applicant_ranking"),
        "job_recommendation": settings.model_for("job_recommendation"),
        "project_draft": settings.model_for("project_draft"),
    }
    log_step("app.startup", env=settings.APP_ENV, port=settings.APP_PORT, models=models_info)

    # Initialize DB (tables + cleanup)
    try:
        await init_db()
    except Exception as e:
        log_step("db.init_error", error=str(e))

    # Initialize messaging broker
    await start_broker()

    yield

    # Teardown
    await close_broker()
    log_step("app.shutdown")


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="Occupify Agentic Service",
        description="Lightweight Python service hosting AI agents for Occupify",
        version="0.1.0",
        lifespan=lifespan,
    )

    # Custom exception handlers
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        return JSONResponse(status_code=exc.status_code, content=exc.to_dict())

    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "statusCode": 422,
                "message": "Validation failed.",
                "errorCode": "VALIDATION_ERROR",
                "details": exc.errors(),
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        log_step("app.unhandled_exception", error=str(exc))
        return JSONResponse(
            status_code=500,
            content={
                "statusCode": 500,
                "message": "Internal server error.",
                "errorCode": "INTERNAL_SERVER_ERROR",
            },
        )

    # Mount routers
    app.include_router(health.router)
    app.include_router(chat_router.router)

    if settings.APP_ENV == "local":
        app.include_router(dev.router)

    return app


app = create_app()
