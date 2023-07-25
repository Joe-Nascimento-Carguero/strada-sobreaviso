from pydantic import BaseModel, Field, field_validator


class SquadBase(BaseModel):
    id: int | None = Field(default=None, max_length=10)
    name: str


class SquadResponse(BaseModel):
    id: int | None = Field(default=None, max_length=10)
    name: str

    @field_validator('id')
    def validate_id_type(cls, v):
        if not isinstance(v, int):
            raise ValueError('TIPO TA ERRADO')
