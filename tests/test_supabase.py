from flask import json


def test_get_goods(client_supabase_db):
    response = client_supabase_db.get("/goods")
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    TESTING_NAME = "item_1"
    assert data[0]["name"] == TESTING_NAME

    # Get single item
    TESTING_ID = data[0]["id"]
    response = client_supabase_db.get(f"/get_item/{TESTING_ID}")
    assert response.status_code == 200


def test_insert_item(client_supabase_db):
    TESTING_NAME = "Testing Item"
    TESTING_PRICE = 370
    response = client_supabase_db.post(
        "/new_item",
        data=dict(
            name=TESTING_NAME,
            price=TESTING_PRICE,
        ),
    )
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data[-1]["price"] == TESTING_PRICE


def test_update_item(client_supabase_db):
    response = client_supabase_db.get("/goods")
    data = json.loads(response.get_data(as_text=True))
    TESTING_ID = data[0]["id"]
    TESTING_NAME = "Testing Item"
    TESTING_PRICE = 480
    response = client_supabase_db.post(
        f"/update_item/{TESTING_ID}",
        data=dict(
            name=TESTING_NAME,
            price=TESTING_PRICE,
        ),
    )
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data[-1]["price"] == TESTING_PRICE


def test_delete_item(client_supabase_db):
    response = client_supabase_db.get("/goods")
    data = json.loads(response.get_data(as_text=True))
    TESTING_ID = data[0]["id"]
    response = client_supabase_db.post(
        f"/delete_item/{TESTING_ID}",
    )
    assert response.status_code == 204
