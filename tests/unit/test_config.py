from app.core.config import Settings


def test_model_setting():
    settings = Settings(GLM_MODEL="glm-5.3")
    assert settings.GLM_MODEL == "glm-5.3"


def test_model_default():
    settings = Settings()
    assert settings.GLM_MODEL == "glm-4.7"


def test_chat_and_pdf_defaults():
    settings = Settings()
    assert settings.CHAT_MAX_MESSAGE_CHARS == 20000
    assert settings.CHAT_MAX_CONTEXT_CHARS == 50000
    assert settings.CHAT_MAX_FILES == 3
    assert settings.PDF_MAX_BYTES == 10485760
    assert settings.PDF_MAX_PAGES == 20
