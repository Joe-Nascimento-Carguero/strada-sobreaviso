from typing import Annotated, List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from strada_sobreaviso.database import config as _database
from strada_sobreaviso.database import models as _models

app = FastAPI()

_database.Base.metadata.create_all(bind=_database.engine)


class ColaboradorBase(BaseModel):
    name: str
    squad_id: int


class SquadBase(BaseModel):
    id: int | None = Field(
        default=None, title='The description of the item', max_length=300
    )
    name: str


class SquadResponse(BaseModel):
    id: int | None = Field(
        default=None, title='The description of the item', max_length=300
    )
    name: str


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_deps = Annotated[Session, Depends(get_db)]


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    """Tratando mensagem de erro HTTP 422"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {'detail': 'O parâmetro informado não é um inteiro'}
        ),
    )


@app.get('/', status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'ok'}


@app.get('/health')
def health_check():
    return {'status': 'ok'}


@app.get('/squads/')
def get_squads(db: db_deps, skip: int = 0, limit: int = 100):
    return db.query(_models.Squads).offset(skip).limit(limit).all()


@app.get('/squads/{squad_id}')
def get_squads(squad_id: int, db: db_deps):
    squad_name = (
        db.query(_models.Squads).filter(_models.Squads.id == squad_id).first()
    )

    if not squad_name:
        raise HTTPException(status_code=404, detail='Squad não existe')
    return squad_name


@app.post(
    '/squads/create',
    status_code=status.HTTP_201_CREATED,
)
def create_squad(squad: SquadBase, db: db_deps, response_model=SquadResponse):
    squad_name = _models.Squads(name=squad.name)
    db.add(squad_name)
    db.commit()
    print(f'response_model = {squad_name.id}')
    return {
        'result': 'Squad criada com sucesso',
        'squad': squad.name,
        'id': squad_name.id,
    }


# if __name__ == '__main__':

#     uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info')
