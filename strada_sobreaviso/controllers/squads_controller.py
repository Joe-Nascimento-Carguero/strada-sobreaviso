from fastapi import APIRouter, HTTPException, status
from sqlalchemy.sql import select

from strada_sobreaviso.database.config import db_deps
from strada_sobreaviso.database.schemas import Squads
from strada_sobreaviso.models.squads import SquadBase, SquadResponse

router = APIRouter()


@router.get('/')
async def get_all_squads(db: db_deps):
    return db.query(Squads).offset(0).all()


@router.get('/{squad_id}')
def get_squad_by_id(squad_id: int, db: db_deps):
    squad_name = db.query(Squads).filter(Squads.id == squad_id).first()

    if not squad_name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Squad não existe',
        )
    return squad_name


@router.post(
    '/create',
    status_code=status.HTTP_201_CREATED,
)
def create_squad(db: db_deps, squad: SquadBase, response_model=SquadResponse):
    squad_model = Squads(name=squad.name)
    squads = select(Squads).where(squad_model.name == squad.name)
    result = db.execute(squads)

    for s in result.scalars():
        if squad_model.name == s.name:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Squad já ta lá fi',
            )

    db.add(squad_model)
    db.commit()
    return {
        'result': 'Squad criada com sucesso',
        'squad': squad.name,
        'id': squad_model.id,
    }
