from app.clients.nasa_client import NASAClient


class AsteroidService:

    def __init__(self, nasa_client: NASAClient):
        self.nasa_client = nasa_client

    def get_all_asteroids(self) -> dict:
        response = self.nasa_client.get_all_asteroids()
        return response
