from fastapi.testclient import TestClient

from strada_sobreaviso.main import app

client = TestClient(app)


def test_deve_retornar_o_status_code_200_health():
    response = client.get('/health')
    assert response.status_code == 200


def test_deve_retornar_status_ok_health():
    response = client.get('/health/')
    assert response.json() == {'status': 'ok'}
