from typing import Any

from fastapi import HTTPException


class AppError(HTTPException):
    def __init__(
        self,
        status_code: int,
        message: str,
        error_code: str,
        details: Any = None,
    ):
        super().__init__(status_code=status_code, detail=message)
        self.status_code = status_code
        self.message = message
        self.error_code = error_code
        self.details = details

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {
            "statusCode": self.status_code,
            "message": self.message,
            "errorCode": self.error_code,
        }
        if self.details is not None:
            data["details"] = self.details
        return data


class SessionNotFoundError(AppError):
    def __init__(self, message: str = "Failed to find this chat session."):
        super().__init__(404, message, "CHAT_SESSION_NOT_FOUND")


class ChatBusyError(AppError):
    def __init__(
        self,
        message: str = "Failed to send: the previous message is still being answered.",
    ):
        super().__init__(409, message, "CHAT_BUSY")


class FileInvalidError(AppError):
    def __init__(
        self,
        filename: str = "file.pdf",
        reason: str = "not a PDF / larger than 10 MB / more than 20 pages / password-protected.",
    ):
        super().__init__(400, f"Failed to read `{filename}`: {reason}", "FILE_INVALID")


class PiiRemovalFailedError(AppError):
    def __init__(
        self,
        source: str = "your message",
    ):
        super().__init__(
            422,
            f"Failed to remove personal data from {source}. Nothing was sent.",
            "PII_REMOVAL_FAILED",
        )


class ChatContextFullError(AppError):
    def __init__(
        self,
        message: str = "Failed to continue: this conversation is too long for the model. Please start a new session.",
    ):
        super().__init__(422, message, "CHAT_CONTEXT_FULL")


class ContentFilteredError(AppError):
    def __init__(
        self,
        message: str = "Failed to answer: the AI provider blocked this content.",
    ):
        super().__init__(422, message, "CHAT_CONTENT_FILTERED")


class LlmUnavailableError(AppError):
    def __init__(
        self,
        message: str = "Failed to reach the AI model. Please try again.",
    ):
        super().__init__(502, message, "LLM_UNAVAILABLE")
