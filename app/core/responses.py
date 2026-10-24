from typing import Any, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PagingMeta(BaseModel):
    page: int
    limit: int
    total: int
    totalPages: int


class SingleResponse[T](BaseModel):
    statusCode: int = 200
    message: str = "OK"
    data: T


class PageResponse[T](BaseModel):
    statusCode: int = 200
    message: str = "OK"
    data: list[T]
    paging: PagingMeta


class ErrorResponse(BaseModel):
    statusCode: int
    message: str
    errorCode: str


def success_response(data: Any, message: str = "OK", status_code: int = 200) -> dict[str, Any]:
    return {
        "statusCode": status_code,
        "message": message,
        "data": data,
    }


def page_response(
    data: list[Any],
    page: int,
    limit: int,
    total: int,
    message: str = "OK",
    status_code: int = 200,
) -> dict[str, Any]:
    total_pages = (total + limit - 1) // limit if limit > 0 else 1
    return {
        "statusCode": status_code,
        "message": message,
        "data": data,
        "paging": {
            "page": page,
            "limit": limit,
            "total": total,
            "totalPages": total_pages,
        },
    }
