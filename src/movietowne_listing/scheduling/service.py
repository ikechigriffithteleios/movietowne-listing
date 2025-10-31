"""Scheduling and orchestration service."""
from fastapi import FastAPI

from movietowne_listing.config import get_settings

app = FastAPI(title="Movietowne Scheduling Service")


@app.on_event("startup")
async def startup_event() -> None:
    settings = get_settings()
    app.logger.info(
        "Starting scheduling service",
        extra={"env": settings.environment, "queue": settings.redis_url},
    )


@app.get("/health", tags=["health"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "scheduling"}


__all__ = ["app"]
