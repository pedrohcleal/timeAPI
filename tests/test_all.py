from fastapi.testclient import TestClient
from app.main import app  # Importa sua instância do FastAPI

client = TestClient(app)


def test_rota_get():
    response = client.get("/")
    assert response.status_code == 200  # Verifica se o status HTTP está correto
    assert response.json() == "Server OK"  # Verifica se o retorno está correto
