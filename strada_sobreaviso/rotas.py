from fastapi import APIRouter

from strada_sobreaviso.controllers import (
    colaboradores_controller as colaboradores,
)
from strada_sobreaviso.controllers import health_controller as health
from strada_sobreaviso.controllers import squads_controller as squads

router = APIRouter()

router.include_router(colaboradores.router, prefix='/colaboradores')
router.include_router(health.router, prefix='/health')
router.include_router(squads.router, prefix='/squads')
