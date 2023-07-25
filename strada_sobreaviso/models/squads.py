from pydantic import BaseModel, Field


class SquadBase(BaseModel):
    id: int | None = Field(default=None, max_length=10)
    name: str
