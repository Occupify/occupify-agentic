from functools import lru_cache
from typing import Any

from pydantic import Field, SecretStr
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

    # File Storage
    CV_GENERATOR_ENABLED: bool = False
    CV_GENERATOR_TIMEOUT_S: int = Field(default=90, ge=45, le=240)
    CV_GENERATOR_LINK_TTL_S: int = Field(default=86400, ge=60, le=604800)
    CV_COMPILER_URL: str = "http://cv-compiler:8190"
    S3_ACCESS_KEY: str = ""
    S3_SECRET_KEY: SecretStr = SecretStr("")
    S3_ENDPOINT: str = ""
    OCI_REGION: str = ""
    OCI_NAMESPACE: str = ""
    OCI_BUCKET: str = ""

    # Database
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@occupify-postgres-agentic:5432/occupify_agentic"
    )

    # RabbitMQ
    RABBITMQ_URL: str = "amqp://guest:guest@occupify-rabbitmq:5672/"
    RABBITMQ_RPC_TIMEOUT_S: int = 10

    # UC4 Job Matching & ML Settings (§2.6)
    SKILLS_DIR: str = "skills"
    CORE_RPC_MODE: str = "mock"
    CORE_MOCK_PATH: str = "app/features/job_match/mock/core_projects.json"
    CORE_MOCK_GET_OVERLAY: str = ""
    EMBEDDING_MODEL: str = "BAAI/bge-m3"
    EMBEDDING_DIM: int = 1024
    RERANKER_MODEL: str = "BAAI/bge-reranker-v2-m3"
    HF_MODELS_DIR: str = "/opt/hf_models"
    ML_THREADS: int = 4
    ML_ENABLED: bool = True
    JOB_MATCH_TOOL_TIMEOUT_S: int = 200
    JOB_MATCH_MAX_REQUESTS: int = 150
    JOB_MATCH_AGENT_MAX_REQUESTS: int = 40
    JOB_MATCH_MAX_SEARCH_CALLS: int = 15
    JOB_MATCH_MAX_INPUT_TOKENS: int = 2000000
    JOB_MATCH_MAX_OUTPUT_TOKENS: int = 300000
    JOB_MATCH_LLM_CONCURRENCY: int = 4

    def model_post_init(self, __context: Any) -> None:
        assert self.JOB_MATCH_TOOL_TIMEOUT_S <= 240, "JOB_MATCH_TOOL_TIMEOUT_S must be <= 240"

    @property
    def EMBEDDER_MODEL(self) -> str:
        return self.EMBEDDING_MODEL


@lru_cache
def get_settings() -> Settings:
    return Settings()
