from fastapi import FastAPI
from app.api.routes import asteroid

app = FastAPI(
    title="The end of the world",
    description="The end of the world",
    version="0.0.1",
    docs_url="/",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    docs_url_path="/docs",
    redoc_url_path="/redoc",
    openapi_path="/openapi.json"
)

app.include_router(asteroid.router, prefix="/asteroid")