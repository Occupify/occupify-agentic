from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any

_current_captures: ContextVar[list[list[Any]]] = ContextVar("_current_captures", default=[])


@contextmanager
def capture_model_requests() -> Iterator[list[Any]]:
    captured: list[Any] = []
    current = _current_captures.get()
    token = _current_captures.set(current + [captured])
    try:
        yield captured
    finally:
        _current_captures.reset(token)


def record_captured_request(payload: Any) -> None:
    for cap in _current_captures.get():
        cap.append(payload)
