from app.core.config import Settings


def test_model_fallback():
    settings = Settings(
        GLM_MODEL_DEFAULT="glm-4.7",
        GLM_MODEL_CHAT="",
        GLM_MODEL_ROADMAP="glm-5.3",
    )
    assert settings.model_for("chat") == "glm-4.7"
    assert settings.model_for("cv_match") == "glm-4.7"
    assert settings.model_for("roadmap") == "glm-5.3"


def test_custom_overrides():
    settings = Settings(
        GLM_MODEL_DEFAULT="glm-4.7",
        GLM_MODEL_CHAT="glm-4.7-flash",
    )
    assert settings.model_for("chat") == "glm-4.7-flash"
    assert settings.model_for("unknown") == "glm-4.7"


def test_chat_and_pdf_defaults():
    settings = Settings()
    assert settings.CHAT_MAX_MESSAGE_CHARS == 20000
    assert settings.CHAT_MAX_CONTEXT_CHARS == 50000
    assert settings.CHAT_MAX_FILES == 3
    assert settings.PDF_MAX_BYTES == 10485760
    assert settings.PDF_MAX_PAGES == 20
