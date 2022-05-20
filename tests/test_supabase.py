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
