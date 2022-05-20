import pytest
from flask import json
from app import create_app
from app.controllers import init_testing_db, drop_testing_db


@pytest.fixture
def client():
    app = create_app(environment="testing")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        init_testing_db()
        yield client
        drop_testing_db()
        app_ctx.pop()


def test_get_goods(client):
    response = client.get("/goods")
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    TESTING_NAME = "item_1"
    assert data[0]["name"] == TESTING_NAME

    # Get single item
    TESTING_ID = data[0]["id"]
    response = client.get(f"/get_item/{TESTING_ID}")
    assert response.status_code == 200


def test_insert_item(client):
    TESTING_NAME = "Testing Item"
    TESTING_PRICE = 370
    response = client.post(
        "/new_item",
        data=dict(
            name=TESTING_NAME,
            price=TESTING_PRICE,
        ),
    )
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data[-1]["price"] == TESTING_PRICE


def test_update_item(client):
    response = client.get("/goods")
    data = json.loads(response.get_data(as_text=True))
    TESTING_ID = data[0]["id"]
    TESTING_NAME = "Testing Item"
    TESTING_PRICE = 480
    response = client.post(
        f"/update_item/{TESTING_ID}",
        data=dict(
            name=TESTING_NAME,
            price=TESTING_PRICE,
        ),
    )
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data[-1]["price"] == TESTING_PRICE


def test_delete_item(client):
    response = client.get("/goods")
    data = json.loads(response.get_data(as_text=True))
    TESTING_ID = data[0]["id"]
    response = client.post(
        f"/delete_item/{TESTING_ID}",
    )
    assert response.status_code == 204
