import os

import pytest
from httpx import ASGITransport, AsyncClient
from pydantic_ai import models
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Ensure no real model requests ever leave test runs
models.ALLOW_MODEL_REQUESTS = False
os.environ["APP_ENV"] = "test"
os.environ["ZAI_API_KEY"] = "mock-key-never-used"
os.environ["PDF_EXTRACTOR"] = "pdfium"
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"

from app.core.config import Settings, get_settings  # noqa: E402

Settings.model_config["env_file"] = None
get_settings.cache_clear()

from app.core.security import CurrentUser, get_current_user  # noqa: E402
from app.db.models import Base  # noqa: E402
from app.db.session import get_db_session, set_engine  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def test_db():
    # Use SQLite in-memory for fast unit testing with shared StaticPool
    from sqlalchemy.pool import StaticPool

    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=False,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    set_engine(engine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    sessionmaker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with sessionmaker() as session:
        yield session

    await engine.dispose()


@pytest.fixture
def mock_user() -> CurrentUser:
    return CurrentUser(
        user_id="test-user-uuid-123",
        role="ROLE_USER",
        email="john.doe@example.com",
    )


@pytest.fixture
async def client(test_db, mock_user):
    async def override_get_db():
        yield test_db

    async def override_get_user():
        return mock_user

    app.dependency_overrides[get_db_session] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_user

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
