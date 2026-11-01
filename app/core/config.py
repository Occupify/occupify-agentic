from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_ENV: str = "production"
    APP_PORT: int = 8186
    LOG_LEVEL: str = "INFO"

    # GLM (z.ai)
    ZAI_API_KEY: str = ""
    ZAI_BASE_URL: str = "https://api.z.ai/api/paas/v4"
    # Default model; free models (glm-4.7-flash, glm-4.5-flash) must not be used (INV-9)
    GLM_MODEL: str = "glm-4.5-air"

    GLM_TIMEOUT_S: int = 120
    GLM_MAX_REQUESTS_PER_RUN: int = 10

    # Chat
    CHAT_MAX_MESSAGE_CHARS: int = 20000
    CHAT_MAX_CONTEXT_CHARS: int = 50000
    CHAT_MAX_FILES: int = 3
    CHAT_STREAM_HEARTBEAT_S: int = 15

    # PDF documents
    PDF_MAX_BYTES: int = 10485760  # 10 MB
    PDF_MAX_PAGES: int = 20
    PDF_EXTRACTOR: str = "doctr"
    OCR_LANGS: str = "vie,eng"

    # Database
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@occupify-postgres-agentic:5432/occupify_agentic"
    )

    # RabbitMQ
    RABBITMQ_URL: str = "amqp://guest:guest@occupify-rabbitmq:5672/"
    RABBITMQ_RPC_TIMEOUT_S: int = 10


@lru_cache
def get_settings() -> Settings:
    return Settings()
