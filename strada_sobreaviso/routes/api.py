from fastapi import APIRouter

from strada_sobreaviso.endpoints import health_check, squads

router = APIRouter()
router.include_router(health_check.router)
router.include_router(squads.router)
