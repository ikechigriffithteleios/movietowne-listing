from fastapi.testclient import TestClient

from movietowne_listing.ingestion.service import app as ingestion_app
from movietowne_listing.scheduling.service import app as scheduling_app
from movietowne_listing.messaging.service import app as messaging_app
from movietowne_listing.admin.service import app as admin_app


def test_ingestion_health() -> None:
    client = TestClient(ingestion_app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "ingestion"


def test_scheduling_health() -> None:
    client = TestClient(scheduling_app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "scheduling"


def test_messaging_health() -> None:
    client = TestClient(messaging_app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "messaging"


def test_admin_health() -> None:
    client = TestClient(admin_app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "admin"
