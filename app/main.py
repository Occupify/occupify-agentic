import os

# Quiet environment defaults before importing AI/ML libraries (F-70, F-75)
os.environ.setdefault("PYDANTIC_AI_NO_BANNER", "1")
os.environ.setdefault("TQDM_DISABLE", "1")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")

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

    # Fail fast if ZAI_API_KEY is not set in non-test environment (F-09)
    if settings.APP_ENV != "test" and not settings.ZAI_API_KEY:
        raise RuntimeError("ZAI_API_KEY environment variable is required in non-test environments.")

    log_step("app.startup", env=settings.APP_ENV, port=settings.APP_PORT, model=settings.GLM_MODEL)

    # Initialize DB (tables + cleanup). Fail startup if tables cannot be initialized (F-20)
    await init_db()

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
                return FileResponse(index_path)

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
                    return await super().get_response(path, scope)

            app.mount("/ui", LocalOnlyStaticFiles(directory=frontend_dir, html=True), name="ui")

    return app


app = create_app()
