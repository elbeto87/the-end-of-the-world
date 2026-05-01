from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NASA_API_KEY: str = "DEMO_KEY"
    NASA_BASE_URL: str = "https://api.nasa.gov"

    class Config:
        env_file = ".env"

settings = Settings()
