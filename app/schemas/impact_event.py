from pydantic import BaseModel


class ImpactEvent(BaseModel):
    impact_event_id: str
    asteroid_name: str
    date: str
    impact_probability: float
    energy: float
    dangerous_score: float
