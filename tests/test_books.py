import test
from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_get_all_books():
    response = client.get("/books/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 30


def test_endpoint_get_books_attributes():
    response = client.get("/books/search")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_get_books_attributes():
    response = client.get("/books/search")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_get_books_id():
    test_id = "c4a0e3dd-9fb8-47c8-915b-2fb2f50612ca"
    response = client.get(f"/books/{test_id}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 7


def test_endpoint_get_loans_books():
    test_id = "c4a0e3dd-9fb8-47c8-915b-2fb2f50612ca"
    response = client.get(f"/books/{test_id}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 7
