from fastapi import APIRouter, HTTPException, status
from sqlalchemy.sql import select

from strada_sobreaviso.database.config import db_deps
from strada_sobreaviso.database.schemas import Colaboradores
from strada_sobreaviso.models.colaboradores import ColaboradorBase
from strada_sobreaviso.controllers.utils.entity_not_exists import (
    entity_not_exists,
)

router = APIRouter()


@router.get('/')
def get_all_colaboradores(db: db_deps):
    return db.query(Colaboradores).offset(0).all()


@router.get('/{colaborador_id}')
@entity_not_exists
async def get_colaborador_by_id(colaborador_id: int, db: db_deps):
    colaborador_name = (
        db.query(Colaboradores)
        .filter(Colaboradores.id == colaborador_id)
        .first()
    )

    if not colaborador_name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return colaborador_name


@router.post(
    '/create',
    status_code=status.HTTP_201_CREATED,
)
def create_colaborador(db: db_deps, colaborador: ColaboradorBase):
    colaborador_model = Colaboradores(name=colaborador.name, squad_id=colaborador.squad_id)
    colaboradores = select(Colaboradores).where(
        colaborador_model.name == colaborador.name
    )
    result = db.execute(colaboradores)

    for s in result.scalars():
        if colaborador_model.name == s.name:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Colaborador já ta lá fi',
            )

    db.add(colaborador_model)
    db.commit()
    return {
        'result': 'Colaborador criada com sucesso',
        'colaborador': colaborador.name,
        'id': colaborador_model.id,
    }
