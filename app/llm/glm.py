from pydantic_ai.models.zai import ZaiModel
from pydantic_ai.providers.zai import ZaiProvider
from pydantic_ai.settings import ModelSettings

from app.core.config import get_settings


def get_model_settings() -> ModelSettings:
    settings = get_settings()
    return ModelSettings(
        timeout=float(settings.GLM_TIMEOUT_S),
        thinking=False,
    )


def get_model() -> ZaiModel:
    settings = get_settings()
    if not settings.ZAI_API_KEY:
        if settings.APP_ENV != "test":
            raise RuntimeError(
                "ZAI_API_KEY environment variable is required in non-test environments."
            )
        api_key = "dummy-key-for-test"
    else:
        api_key = settings.ZAI_API_KEY

    provider = ZaiProvider(
        api_key=api_key,
        base_url=settings.ZAI_BASE_URL,
    )
    return ZaiModel(settings.GLM_MODEL, provider=provider)
