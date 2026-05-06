from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NASA_API_KEY: str = "DEMO_KEY"
    NASA_NEOWS_BASE_URL: str = "https://api.nasa.gov/neo/rest/v1"
    NASA_SENTRY_JPL_BASE_URL: str = "https://ssd-api.jpl.nasa.gov/sentry.api"

    class Config:
        env_file = ".env"

settings = Settings()
