from fastapi.testclient import TestClient
from app.main import app
from app.db_config import get_db_connection
from app.crud import get_all_cities, get_all_countries
from app.handler import get_temperature

client = TestClient(app)


def test_rota_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Server OK"


def test_all_countries():
    with get_db_connection() as conn:
        cities = {"countries": get_all_countries(conn)}
    response = client.get("/all/countries")
    assert response.status_code == 200
    assert response.json() == cities


def test_all_cities():
    with get_db_connection() as conn:
        cities = {"cities": get_all_cities(conn)}
    response = client.get("/all/cities")
    assert response.status_code == 200
    assert response.json() == cities


def test_temperature_city():
    temperature = get_temperature("brazil", "sao-paulo")
    response = client.get("/brazil/sao-paulo")
    assert response.status_code == 200
    assert response.json() == {"temperature": temperature}
