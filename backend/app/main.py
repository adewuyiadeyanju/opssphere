from fastapi import FastAPI
from app.core.config import settings

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
