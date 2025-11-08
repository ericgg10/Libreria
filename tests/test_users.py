import test
from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_get_all_users():
    response = client.get("/users/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_get_users_by_id():
    test_user = "a37616bd-b662-439e-ae46-8dae630b4831"
    response = client.get(f"/users/{test_user}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 4


def test_endpoint_get_loans_users():
    test_user = "a37616bd-b662-439e-ae46-8dae630b4831"
    response = client.get(f"/users/{test_user}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 4
