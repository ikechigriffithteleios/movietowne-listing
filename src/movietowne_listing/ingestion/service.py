"""Content ingestion service entry points."""
from fastapi import FastAPI

from movietowne_listing.config import get_settings

app = FastAPI(title="Movietowne Ingestion Service")


@app.on_event("startup")
async def startup_event() -> None:
    settings = get_settings()
    app.logger.info("Starting ingestion service", extra={"env": settings.environment})


@app.get("/health", tags=["health"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "ingestion"}


__all__ = ["app"]
