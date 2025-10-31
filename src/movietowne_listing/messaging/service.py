"""Messaging service API and worker bootstrap."""
from fastapi import FastAPI

from movietowne_listing.config import get_settings

app = FastAPI(title="Movietowne Messaging Service")


@app.on_event("startup")
async def startup_event() -> None:
    settings = get_settings()
    app.logger.info(
        "Starting messaging service",
        extra={
            "env": settings.environment,
            "twilio_configured": bool(settings.twilio_account_sid),
        },
    )


@app.get("/health", tags=["health"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "messaging"}


__all__ = ["app"]
