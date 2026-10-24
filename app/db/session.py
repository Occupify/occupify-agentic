from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import get_settings

_engine = None
_sessionmaker = None


def set_engine(engine) -> None:
    global _engine, _sessionmaker
    _engine = engine
    _sessionmaker = None


def get_engine():
    global _engine
    if _engine is None:
        settings = get_settings()
        _engine = create_async_engine(
            settings.DATABASE_URL,
            echo=False,
            pool_pre_ping=True,
        )
    return _engine


def get_sessionmaker():
    global _sessionmaker
    if _sessionmaker is None:
        engine = get_engine()
        _sessionmaker = async_sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _sessionmaker


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    maker = get_sessionmaker()
    session = maker()
    try:
        yield session
    finally:
        import anyio

        with anyio.CancelScope(shield=True):
            await session.close()
