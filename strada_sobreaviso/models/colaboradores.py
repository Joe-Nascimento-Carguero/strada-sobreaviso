from pydantic import BaseModel, Field


class ColaboradorBase(BaseModel):
    id: int | None = Field(default=None, max_length=10)
    name: str
    squad_id: int
