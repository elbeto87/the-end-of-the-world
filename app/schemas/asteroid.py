from pydantic import BaseModel


class AsteroidSchema(BaseModel):
    asteroid_id: str
    name: str
    diameter_min: float
    diameter_max: float
    is_potentially_hazardous: bool