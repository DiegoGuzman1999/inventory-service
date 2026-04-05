from fastapi import FastAPI
from app.zone.settings import settings

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health():
    return {
        "service": settings.app_name,
        "env": settings.app_env,
        "status": "ok"
    }