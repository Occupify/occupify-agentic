from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_ENV: str = "local"
    APP_PORT: int = 8186
    LOG_LEVEL: str = "INFO"
    LOG_PAYLOADS: bool = False

    # GLM (z.ai)
    ZAI_API_KEY: str = ""
    ZAI_BASE_URL: str = "https://api.z.ai/api/paas/v4"
    GLM_MODEL_DEFAULT: str = "glm-4.7"
    GLM_THINKING: bool = False

    GLM_MODEL_CHAT: str = ""
    GLM_MODEL_ROADMAP: str = ""
    GLM_MODEL_CV_MATCH: str = ""
    GLM_MODEL_APPLICANT_RANKING: str = ""
    GLM_MODEL_JOB_RECOMMENDATION: str = ""
    GLM_MODEL_PROJECT_DRAFT: str = ""

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
    PDF_EXTRACTOR: str = "docling"
    OCR_LANGS: str = "vie,eng"
    PDF_ALLOWED_HOSTS: str = ""

    # Database
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@occupify-postgres-agentic:5432/occupify_agentic"
    )

    # RabbitMQ
    RABBITMQ_URL: str = "amqp://guest:guest@occupify-rabbitmq:5672/"
    RABBITMQ_RPC_TIMEOUT_S: int = 10

    def model_for(self, use_case: str) -> str:
        mapping = {
            "chat": self.GLM_MODEL_CHAT,
            "roadmap": self.GLM_MODEL_ROADMAP,
            "cv_match": self.GLM_MODEL_CV_MATCH,
            "applicant_ranking": self.GLM_MODEL_APPLICANT_RANKING,
            "job_recommendation": self.GLM_MODEL_JOB_RECOMMENDATION,
            "project_draft": self.GLM_MODEL_PROJECT_DRAFT,
        }
        val = mapping.get(use_case)
        if val and val.strip():
            return val.strip()
        return self.GLM_MODEL_DEFAULT.strip()


@lru_cache
def get_settings() -> Settings:
    return Settings()
