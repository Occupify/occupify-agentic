from pydantic_ai.models.zai import ZaiModel
from pydantic_ai.providers.zai import ZaiProvider

from app.core.config import get_settings


def model_for(use_case: str) -> ZaiModel:
    settings = get_settings()
    model_id = settings.model_for(use_case)
    provider = ZaiProvider(
        api_key=settings.ZAI_API_KEY or "dummy-key-for-test",
        base_url=settings.ZAI_BASE_URL,
    )
    return ZaiModel(model_id, provider=provider)
