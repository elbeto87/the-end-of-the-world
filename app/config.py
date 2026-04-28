from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    nasa_api_key: str = "DEMO_KEY"
    nasa_base_url: str = "http://api.nasa.gov"

    class Config:
        env_file = ".env"

settings = Settings()
