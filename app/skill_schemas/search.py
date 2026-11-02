from typing import Literal

from pydantic import BaseModel, ConfigDict


class SearchMoreArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str
    skills: list[str] = []


class SearchDecision(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action: Literal["done", "search"]
    reason: str
