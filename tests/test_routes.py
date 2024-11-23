from http import HTTPStatus

import pytest
from flask.testing import FlaskClient

from src.app.app import app


@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

def test_index(client: FlaskClient):
    response = client.get('/ping')

    assert response.status_code == HTTPStatus.OK
    assert response.json == {'message': 'pong'}
