from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import api_router


app = FastAPI(
    title=settings.APP_NAME,
    description="Cloud-native Operations Platform",
    version=settings.APP_VERSION
)


@app.get("/")
def root():
    return {
        "message": "Welcome to OpsSphere"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    api_router,
    prefix="/api/v1"
)
