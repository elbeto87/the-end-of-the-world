import httpx

from app.config import settings


class NASASentryClient:

    def __init__(self, http_client: httpx.Client):
        self._client = http_client
        self.base_url = settings.NASA_SENTRY_JPL_BASE_URL

    def get_impact_data(self, impact_probability: str = "1e-3") -> list[dict]:
        params = {
            "all": 1,
            "ip-min": impact_probability,
        }
        return self._client.get(self.base_url, params=params).json()["data"]
