from fastapi import APIRouter, Depends

from app.api.dependencies import get_asteroid_service
from app.services import AsteroidService

router = APIRouter(
    tags=["asteroid"],
)

@router.get("")
def get_all_asteroids(asteroid_service: AsteroidService = Depends(get_asteroid_service)) -> dict:
    return asteroid_service.get_all_asteroids()
