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


def test_not_found(client: FlaskClient):
    params = {'action': 'not_found'}

    response = client.get('/ping', query_string=params)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json == {'message': 'Resource not found'}


def test_not_handled(client: FlaskClient):
    params = {'action': 'not_handled'}

    response = client.get('/ping', query_string=params)

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json == {'message': 'Internal Server Error'}
