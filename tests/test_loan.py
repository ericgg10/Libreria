from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_get_all_loans():
    response = client.get("/")
    assert response.sta
