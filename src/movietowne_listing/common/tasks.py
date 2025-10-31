"""Shared Celery application factory."""
from __future__ import annotations

from celery import Celery

from movietowne_listing.config import get_settings


def create_celery_app(name: str) -> Celery:
    """Create a configured Celery application."""

    settings = get_settings()
    app = Celery(name, broker=settings.redis_url, backend=settings.redis_url)
    app.conf.update(task_default_queue=f"{name}.default")
    return app


__all__ = ["create_celery_app"]
