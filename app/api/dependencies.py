from typing import Generator

import httpx
from fastapi import Depends

from app.clients.nasa_client import NASAClient
from app.services import AsteroidService


def get_nasa_client() -> Generator[NASAClient, None, None]:
    with httpx.Client() as client:
        yield NASAClient(client)

def get_asteroid_service(nasa_client: NASAClient = Depends(get_nasa_client)) -> AsteroidService:
    return AsteroidService(nasa_client=nasa_client)
