from pydantic_ai.models.zai import ZaiModel
from pydantic_ai.providers.zai import ZaiProvider

from app.core.config import get_settings


def get_model() -> ZaiModel:
    settings = get_settings()
    if not settings.ZAI_API_KEY and settings.APP_ENV != "test":
        raise ValueError("ZAI_API_KEY is required and cannot be empty in non-test environment.")

    provider = ZaiProvider(
        api_key=settings.ZAI_API_KEY or "dummy-key-for-test",
        base_url=settings.ZAI_BASE_URL,
    )
    return ZaiModel(settings.GLM_MODEL, provider=provider)
