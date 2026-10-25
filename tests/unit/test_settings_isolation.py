from app.core.config import get_settings


def test_tests_ignore_developer_env_file(tmp_path, monkeypatch):
    # Simulate a developer .env file with custom overrides
    env_file = tmp_path / ".env"
    env_file.write_text("GLM_MODEL=glm-developer-custom\nAPP_ENV=developer-env\n")

    monkeypatch.chdir(tmp_path)
    get_settings.cache_clear()

    # Settings used by tests has env_file disabled in conftest
    settings = get_settings()
    assert settings.GLM_MODEL != "glm-developer-custom"
    assert settings.APP_ENV != "developer-env"
