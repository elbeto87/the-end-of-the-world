from app.clients.nasa_neows_client import NASANeoWSClient
from app.clients.nasa_sentry_client import NASASentryClient
from app.schemas.impact_event import ImpactEvent


SCALE_FACTOR = 1_000_000


class AsteroidService:

    def __init__(self, nasa_neows_client: NASANeoWSClient, nasa_sentry_client: NASASentryClient) -> None:
        self.nasa_neows_client = nasa_neows_client
        self.nasa_sentry_client = nasa_sentry_client

    def get_all_asteroids(self) -> dict:
        response = self.nasa_neows_client.get_all_asteroids()
        return response

    def get_impact_data(self, impact_probability: str = "1e-3") -> list[ImpactEvent]:
        impact_events = self.nasa_sentry_client.get_impact_data(impact_probability)
        impact_events_list = [
            ImpactEvent(
                impact_event_id=impact_event["id"],
                asteroid_name=impact_event["des"],
                date=impact_event["date"],
                impact_probability=round(float(impact_event["ip"]), 4),
                energy=round(float(impact_event["energy"]), 4)*1000, # Expressed in kt
                dangerous_score=round(float(impact_event["ip"])*float(impact_event["energy"])*SCALE_FACTOR, 2),
            ) for impact_event in impact_events
        ]
        return sorted(impact_events_list, key=lambda x: x.dangerous_score, reverse=True)


    def get_top_risk_impact_data(self, count: int = 1) -> list[ImpactEvent]:
        return self.get_impact_data()[:count]
