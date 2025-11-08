from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_get_all_loans():
    response = client.get("/loans/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 11


def test_endpoint_get_all_loans_active():
    response = client.get("/loans/active/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 5
