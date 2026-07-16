from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_site():
    """Test creating a new site."""

    payload = {
        "name": "Test Site",
        "country": "Nigeria",
        "site_type": "Land",
        "latitude": 6.5244,
        "longitude": 3.3792,
    }

    response = client.post("/api/v1/sites/", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["country"] == payload["country"]
    assert data["site_type"] == payload["site_type"]
    assert data["status"] == "Planned"

    assert "id" in data
    assert "created_at" in data


def test_get_all_sites():
    """Test retrieving all sites."""

    response = client.get("/api/v1/sites/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_site_by_id():
    """Test retrieving a site by its ID."""

    payload = {
        "name": "Site For Lookup",
        "country": "Ghana",
        "site_type": "Land",
        "latitude": 5.6037,
        "longitude": -0.1870,
    }

    create_response = client.post("/api/v1/sites/", json=payload)

    created_site = create_response.json()

    response = client.get(f"/api/v1/sites/{created_site['id']}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == created_site["id"]
    assert data["name"] == payload["name"]


def test_get_unknown_site_returns_404():
    """Unknown site IDs should return 404."""

    unknown_id = "11111111-1111-1111-1111-111111111111"

    response = client.get(f"/api/v1/sites/{unknown_id}")

    assert response.status_code == 404
