from faker import Faker
from fastapi.testclient import TestClient

from strada_sobreaviso.database import models as _models
from strada_sobreaviso.main import app, db_deps

client = TestClient(app)

faker = Faker()


def test_deve_retorar_squad_por_id():
    response = client.get('/squads/85')
    assert response.status_code == 200
    assert response.json() == {
        'created_at': '2023-07-14T22:39:49.906404',
        'id': 85,
        'name': 'SRE',
    }


def test_deve_retorar_erro_quando_passar_squad_id_que_nao_existe():
    response = client.get('/squads/999999999999999999999999999999')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Squad não existe'}


def test_deve_retorar_erro_quando_passar_uma_string_no_parametro_de_squad_id():
    fake_string = faker.pystr()
    response = client.get(f'/squads/{fake_string}')
    assert response.status_code == 422
    assert response.json() == {
        'detail': 'O parâmetro informado não é um inteiro'
    }


def test_deve_retornar_status_ok():
    response = client.get('/health')
    assert response.json() == {'status': 'ok'}


def test_deve_criar_a_squad():
    fake_string = faker.pystr()
    fake_int = faker.pyint()
    response = client.post('/squads/create', json={'name': fake_string})
    squad_id = response.json()['id']
    assert response.status_code == 201
    assert response.json() == {
        'result': 'Squad criada com sucesso',
        'squad': fake_string,
        'id': squad_id,
    }


def test_deve_retornar_erro_quando_a_squad_ja_existir():
    fake_string = faker.pystr()
    fake_int = faker.pyint()
    response = client.post('/squads/create', json={'name': fake_string})
    squad_id = response.json()['id']
    assert response.status_code == 201
    assert response.json() == {
        'result': 'Squad criada com sucesso',
        'squad': fake_string,
        'id': squad_id,
    }
