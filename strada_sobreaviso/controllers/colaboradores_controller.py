from fastapi import APIRouter, HTTPException, status
from sqlalchemy.sql import select

from strada_sobreaviso.database.config import db_deps
from strada_sobreaviso.database.schemas import Colaboradores
from strada_sobreaviso.models.colaboradores import ColaboradorBase

router = APIRouter()


@router.get('/')
async def get_all_colaboradores(db: db_deps):
    return db.query(Colaboradores).offset(0).all()


@router.get('/{colaborador_id}')
def get_colaborador_by_id(colaborador_id: int, db: db_deps):
    colaborador_name = (
        db.query(Colaboradores)
        .filter(Colaboradores.id == colaborador_id)
        .first()
    )

    if not colaborador_name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Colaborador não existe',
        )
    return colaborador_name
