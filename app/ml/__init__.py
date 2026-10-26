import asyncio
import time
from typing import Any

from app.core.config import get_settings
from app.core.errors import AppError
from app.core.logging import log_step
from app.ml.embedder import Embedder
from app.ml.fakes import FakeEmbedder, FakeReranker
from app.ml.reranker import Reranker


class EmbedderUnavailable(AppError):
    def __init__(self, message: str = "Embedder is unavailable"):
        super().__init__(503, message, "EMBEDDER_UNAVAILABLE")


class RerankerUnavailable(AppError):
    def __init__(self, message: str = "Reranker is unavailable"):
        super().__init__(503, message, "RERANKER_UNAVAILABLE")


_embedder: Any = None
_reranker: Any = None


def get_embedder() -> Embedder | FakeEmbedder:
    global _embedder
    settings = get_settings()
    if settings.APP_ENV == "test":
        if _embedder is None:
            _embedder = FakeEmbedder()
        return _embedder

    if not settings.ML_ENABLED:
        raise EmbedderUnavailable("ML is disabled by configuration (ML_ENABLED=false)")

    if _embedder is None:
        try:
            _embedder = Embedder()
        except Exception as e:
            raise EmbedderUnavailable(f"Failed to load embedder: {e}") from e
    return _embedder


def get_reranker() -> Reranker | FakeReranker:
    global _reranker
    settings = get_settings()
    if settings.APP_ENV == "test":
        if _reranker is None:
            _reranker = FakeReranker()
        return _reranker

    if not settings.ML_ENABLED:
        raise RerankerUnavailable("ML is disabled by configuration (ML_ENABLED=false)")

    if _reranker is None:
        try:
            _reranker = Reranker()
        except Exception as e:
            raise RerankerUnavailable(f"Failed to load reranker: {e}") from e
    return _reranker


async def _async_load_models() -> None:
    settings = get_settings()
    if not settings.ML_ENABLED or settings.APP_ENV == "test":
        return

    def _load():
        t0 = time.perf_counter()
        get_embedder()
        t1 = time.perf_counter()
        log_step("ml.loaded", model=settings.EMBEDDER_MODEL, ms=int((t1 - t0) * 1000))

        t2 = time.perf_counter()
        get_reranker()
        t3 = time.perf_counter()
        log_step("ml.loaded", model=settings.RERANKER_MODEL, ms=int((t3 - t2) * 1000))

    await asyncio.to_thread(_load)


def load_models_in_background() -> asyncio.Task[None] | None:
    settings = get_settings()
    if not settings.ML_ENABLED or settings.APP_ENV == "test":
        return None
    return asyncio.create_task(_async_load_models())


__all__ = [
    "Embedder",
    "Reranker",
    "FakeEmbedder",
    "FakeReranker",
    "EmbedderUnavailable",
    "RerankerUnavailable",
    "get_embedder",
    "get_reranker",
    "load_models_in_background",
]
