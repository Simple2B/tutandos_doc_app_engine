from .utils import TOKEN_ID_FILEPATH
from flask_jwt_extended import decode_token

TEST_USER_ID = "DEnO9zw1PXTnHW16uhBXW1DZKHC2"


def test_firebase_login(client):
    with open(TOKEN_ID_FILEPATH, "r") as token_id_file:
        token_id = token_id_file.read()

        resp = client.post("/login", json={
            "id_token": token_id,
        })

        assert resp.status_code == 200
        assert resp.json["success"]
        assert "Authorization" in resp.headers
        assert resp.headers["Authorization"].startswith("Bearer ")

        jwt_token = resp.headers["Authorization"][len("Bearer "):]
        data = decode_token(jwt_token)
        assert data["sub"] == TEST_USER_ID
