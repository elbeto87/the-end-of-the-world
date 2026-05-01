import httpx

from app.config import settings


class NASAClient:

    def __init__(self, http_client: httpx.Client):
        self._client = http_client
        self._base_url = settings.NASA_BASE_URL
        self._api_key = settings.NASA_API_KEY

    def get_all_asteroids(self) -> dict:
        all_asteroids_url = f"{self._base_url}/neo/browse"
        response = self._client.get(
            all_asteroids_url,
            params={"api_key": self._api_key},
        )
        response.raise_for_status()
        return response.json()
