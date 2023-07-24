from fastapi import APIRouter, HTTPException, status

from strada_sobreaviso.database import config as _database
from strada_sobreaviso.database import models as _models
from strada_sobreaviso.main import SquadBase

router = APIRouter(prefix='/squads', tags=['squads'])


@router.get('/squads/')
def get_squads(db: _database.db_deps, skip: int = 0, limit: int = 100):
    return db.query(_models.Squads).offset(skip).limit(limit).all()


@router.get('/squads/{squad_id}')
def get_squads(squad_id: int, db: _database.db_deps):
    squad_name = (
        db.query(_models.Squads).filter(_models.Squads.id == squad_id).first()
    )

    if not squad_name:
        raise HTTPException(status_code=404, detail='Squad não existe')
    return squad_name


@router.post('/squads/create')
def create_squad(squad: SquadBase, db: _database.db_deps):
    squad_name = _models.Squads(name=squad.name)
    db.add(squad_name)
    db.commit()
