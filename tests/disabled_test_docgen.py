from .utils import STATIC_PATH
import json

DOC_GENERATION_JSON = STATIC_PATH / "doc_gen.json"


def test_document_task_create(client_with_jwt):
    with open(DOC_GENERATION_JSON, "r") as doc_gen_data:
        response = client_with_jwt.post(
            "/document",
            json=json.load(doc_gen_data),
            headers={"Authorization": client_with_jwt.jwt_token},
        )
        assert response.status_code == 200
