"""Application configuration models and helpers."""
from functools import lru_cache
from typing import Literal

from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    """Base configuration shared across services."""

    environment: Literal["development", "staging", "production"] = Field(
        default="development", description="Active deployment environment"
    )
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO", description="Global log level"
    )
    database_url: str = Field(
        default="postgresql+psycopg://user:password@localhost:5432/movietowne",
        description="SQLAlchemy-compatible PostgreSQL URL",
    )
    redis_url: str = Field(
        default="redis://localhost:6379/0", description="Redis connection URL"
    )
    twilio_account_sid: str = Field(default="", description="Twilio account SID")
    twilio_auth_token: str = Field(default="", description="Twilio auth token")
    sendgrid_api_key: str = Field(default="", description="SendGrid API key")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> AppSettings:
    """Return cached application settings."""

    return AppSettings()


__all__ = ["AppSettings", "get_settings"]
