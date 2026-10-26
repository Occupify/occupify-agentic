import os
import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.db.init import init_db
from app.db.session import set_engine


@pytest.fixture(scope="session")
def pg_url():
    url = os.getenv("TEST_PG_URL")
    if not url:
        if os.getenv("CI") == "true":
            pytest.fail("TEST_PG_URL environment variable is required in CI but not set!")
        pytest.skip("TEST_PG_URL not set; skipping Postgres integration tests locally.")
    return url


@pytest.fixture(scope="session")
async def pg_engine(pg_url):
    engine = create_async_engine(pg_url, echo=False)
    set_engine(engine)
    await init_db()
    yield engine
    await engine.dispose()


@pytest.fixture
async def pg_session(pg_engine):
    sessionmaker = async_sessionmaker(pg_engine, class_=AsyncSession, expire_on_commit=False)
    async with sessionmaker() as session:
        yield session
        # Truncate tables between tests
        await session.execute(
            text("TRUNCATE TABLE job_match_results, job_match_runs, job_index, index_meta CASCADE;")
        )
        await session.commit()
