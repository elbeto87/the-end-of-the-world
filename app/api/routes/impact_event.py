from fastapi import Depends, APIRouter

from app.api.dependencies import get_asteroid_service
from app.schemas.impact_event import ImpactEvent
from app.services.asteroid_service import AsteroidService


router = APIRouter(
    tags=["impact_event"],
)


@router.get("/impact_data")
def get_all_impact_data(asteroid_service: AsteroidService = Depends(get_asteroid_service)) -> list[ImpactEvent]:
    return asteroid_service.get_impact_data()


@router.get("/top_risk")
def get_top_risk_impact_data(asteroid_service: AsteroidService = Depends(get_asteroid_service)) -> list[ImpactEvent]:
    impact_data = asteroid_service.get_top_risk_impact_data(count=1)
    return impact_data
