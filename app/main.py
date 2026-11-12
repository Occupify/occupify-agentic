import os

# Quiet environment defaults before importing AI/ML libraries (F-70, F-75)
os.environ.setdefault("PYDANTIC_AI_NO_BANNER", "1")
os.environ.setdefault("TQDM_DISABLE", "1")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")

import asyncio
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.agents.skill_registry import validate_skills_directory
from app.api import dev, health
from app.core.config import get_settings
from app.core.errors import AppError
from app.core.logging import log_step, setup_logging
from app.db.init import init_db
from app.features.chat import router as chat_router
from app.features.cv_improvement import router as cv_improvement_router
from app.messaging.broker import close_broker, start_broker
from app.ml import load_models_in_background

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    setup_logging()

    # Fail fast if ZAI_API_KEY is not set in non-test environment (F-09)
    if settings.APP_ENV != "test" and not settings.ZAI_API_KEY:
        raise RuntimeError("ZAI_API_KEY environment variable is required in non-test environments.")

    # Validate skill registry on startup (T-20, C-12)
    skills_dir = Path(settings.SKILLS_DIR)
    if not skills_dir.exists():
        raise RuntimeError(f"Skills directory is missing: {settings.SKILLS_DIR}")
    validate_skills_directory(skills_dir)

    log_step("app.startup", env=settings.APP_ENV, port=settings.APP_PORT, model=settings.GLM_MODEL)

    # Initialize DB (tables + cleanup). Fail startup if tables cannot be initialized (F-20)
    await init_db()

    # Initialize messaging broker only when CORE_RPC_MODE != mock
    if settings.CORE_RPC_MODE != "mock":
        import app.messaging.consumers  # noqa: F401

        await start_broker()

    # Background model loading
    load_models_in_background()

    # Launch background batch sync for job index (non-blocking)
    sync_task = None
    if settings.APP_ENV != "test":
        from app.features.job_match.index.sync import sync_all_jobs_in_background

        sync_task = asyncio.create_task(sync_all_jobs_in_background())

    yield

    # Teardown
    if sync_task and not sync_task.done():
        sync_task.cancel()
    if settings.CORE_RPC_MODE != "mock":
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

    # CORS is handled upstream by the API Gateway (occupify-gateway :8180).
    # Leaving downstream CORS disabled avoids duplicate Access-Control-Allow-Origin headers.

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
                "error": {"code": "VALIDATION_ERROR", "message": "Validation failed."},
                "details": exc.errors(),
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        log_step(
            "app.unhandled_exception",
            error_type=type(exc).__name__,
            error_message=str(exc),
            path=str(request.url.path),
        )
        return JSONResponse(
            status_code=500,
            content={
                "statusCode": 500,
                "message": "An unexpected error occurred. Please try again later.",
                "errorCode": "INTERNAL_SERVER_ERROR",
            },
        )

    # Mount routers
    app.include_router(health.router)
    app.include_router(chat_router.router)
    app.include_router(cv_improvement_router)

    if settings.APP_ENV in ("local", "test"):
        app.include_router(dev.router)

        frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
        if os.path.isdir(frontend_dir):
            from fastapi.responses import FileResponse, Response
            from fastapi.staticfiles import StaticFiles
            from starlette.types import Scope

            index_path = os.path.join(frontend_dir, "index.html")

            @app.get("/ui", include_in_schema=False)
            async def get_ui():
                if get_settings().APP_ENV not in ("local", "test"):
                    raise AppError(404, "Endpoint not found.", "NOT_FOUND")
                return FileResponse(
                    index_path,
                    headers={
                        "Cache-Control": "no-cache, no-store, must-revalidate",
                        "Pragma": "no-cache",
                        "Expires": "0",
                    },
                )

            class LocalOnlyStaticFiles(StaticFiles):
                async def get_response(self, path: str, scope: Scope) -> Response:
                    if get_settings().APP_ENV not in ("local", "test"):
                        return JSONResponse(
                            status_code=404,
                            content={
                                "statusCode": 404,
                                "message": "Endpoint not found.",
                                "errorCode": "NOT_FOUND",
                            },
                        )
                    res = await super().get_response(path, scope)
                    res.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
                    res.headers["Pragma"] = "no-cache"
                    res.headers["Expires"] = "0"
                    return res

            app.mount("/ui", LocalOnlyStaticFiles(directory=frontend_dir, html=True), name="ui")

    return app


app = create_app()
