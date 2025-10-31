"""Admin service API scaffold."""
from fastapi import FastAPI

from movietowne_listing.config import get_settings

app = FastAPI(title="Movietowne Admin Service")


@app.on_event("startup")
async def startup_event() -> None:
    settings = get_settings()
    app.logger.info(
        "Starting admin service",
        extra={"env": settings.environment, "database": settings.database_url},
    )


@app.get("/health", tags=["health"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "admin"}


__all__ = ["app"]
