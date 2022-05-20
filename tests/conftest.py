import pytest
from app import create_app
from .utils import TOKEN_ID_FILEPATH
from app.controllers import init_testing_db, drop_testing_db


def get_test_app():
    app = create_app(environment="testing")
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(scope="function"):
    app = get_test_app()

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        yield client
        app_ctx.pop()


@pytest.fixture()
def client_with_jwt(scope="function"):
    app = get_test_app()

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()

        with open(TOKEN_ID_FILEPATH, "r") as token_id_file:
            token_id = token_id_file.read()

            resp = client.post("/login", json={"id_token": token_id})
            client.jwt_token = resp.headers["Authorization"]
            yield client
            app_ctx.pop()


@pytest.fixture
def client_supabase_db():
    app = create_app(environment="testing")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        init_testing_db()
        yield client
        drop_testing_db()
        app_ctx.pop()
