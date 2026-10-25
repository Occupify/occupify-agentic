from typing import Any


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
