from app import db


def test_docget_endpoint(client):
    def check_invalid_field(resp_json, field, type_field):
        assert resp_json[0]["loc"][0] == field
        assert resp_json[0]["msg"] == f"value is not a valid {type_field}"
        assert resp_json[0]["type"] == f"type_error.{type_field}"

    response = client.post("/api/v1/document", json=dict())
    assert response.status_code != 200
    assert response.json[0]["loc"][0] == "audit_id"
    assert response.json[0]["msg"] == "field required"
    assert response.json[0]["type"] == "value_error.missing"

    response = client.post("/api/v1/document", json=dict(audit_id=234,))
    assert response.status_code != 200
    check_invalid_field(response.json, "audit_id", "uuid")

    response = client.post("/api/v1/document", json=dict(audit_id="6f3ed662-be19-4e4a-90b1",))
    assert response.status_code != 200
    check_invalid_field(response.json, "audit_id", "uuid")

    audit = db.get("Audits", count=1)[0]
    assert audit
    assert "id" in audit

    response = client.post("/api/v1/document", json=dict(audit_id="6f3ed662-be19-4e4a-90b1-be3247a3aca4",))
    assert response.status_code == 200
    assert not response.json["success"]
    assert response.json["msg"] == "No audit with id: 6f3ed662-be19-4e4a-90b1-be3247a3aca4"

    response = client.post("/api/v1/document", json=dict(audit_id=audit["id"],))
    assert response.status_code == 200
    assert response.json["success"]
    assert response.json["msg"].startswith("Document generate started")
