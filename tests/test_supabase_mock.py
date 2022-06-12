import json
from app import db
from app.services.supabase.supabase_mock import INIT_STATIC_PATH


def test_supabase_mock():
    with open(INIT_STATIC_PATH) as init_db_data_f:
        init_db_data = json.load(init_db_data_f)

    for table in ("Answers", "Audits"):
        assert table in init_db_data

    data = db.get("Answers")
    assert len(data) == len(init_db_data["Answers"])

    # check if all comments are different
    comments_found = []
    for answer in data:
        assert answer["comment"] not in comments_found
        comments_found.append(answer["comment"])

    audit_id = init_db_data["Answers"][0]["audit_id"]
    comment = init_db_data["Answers"][0]["comment"]

    data = db.get("Answers", eq={"audit_id": audit_id, "comment": comment})
    assert data

    assert len(data) == 1
    assert data[0]["audit_id"] == audit_id
    assert data[0]["comment"] == comment
