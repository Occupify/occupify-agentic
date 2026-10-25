from fastapi import Request
from pydantic import BaseModel

from app.core.config import get_settings
from app.core.errors import AppError


class CurrentUser(BaseModel):
    user_id: str
    role: str = "ROLE_USER"
    email: str = ""


async def get_current_user(request: Request) -> CurrentUser:
    user_id = request.headers.get("X-User-Id")
    role = request.headers.get("X-User-Role", "ROLE_USER")
    email = request.headers.get("X-User-Email", "")

    if user_id:
        return CurrentUser(user_id=user_id, role=role, email=email)

    settings = get_settings()
    if settings.APP_ENV == "local":
        return CurrentUser(user_id="local-dev-user", role="ROLE_USER", email="dev@occupify.local")

    raise AppError(
        status_code=401,
        message="Failed to authenticate: missing X-User-Id header.",
        error_code="UNAUTHORIZED",
    )
