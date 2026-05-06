from app.clients.nasa_neows_client import NASANeoWSClient
from app.clients.nasa_sentry_client import NASASentryClient


class AsteroidService:

    def __init__(self, nasa_neows_client: NASANeoWSClient, nasa_sentry_client: NASASentryClient) -> None:
        self.nasa_neows_client = nasa_neows_client
        self.nasa_sentry_client = nasa_sentry_client

    def get_all_asteroids(self) -> dict:
        response = self.nasa_neows_client.get_all_asteroids()
        return response

    def get_impact_data(self, impact_probability: str = "1e-3") -> dict:
        response = self.nasa_sentry_client.get_impact_data(impact_probability)
        return response.json()