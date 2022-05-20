from flask import json

testing_data = [
    {
        "created_at": "2022-05-18T13:41:36+00:00",
        "id": 1,
        "name": "Phone",
        "price": 300,
    },
    {
        "created_at": "2022-05-18T13:42:07+00:00",
        "id": 2,
        "name": "Laptop",
        "price": 1000,
    },
    {
        "created_at": "2022-05-18T13:42:56+00:00",
        "id": 3,
        "name": "Fridge",
        "price": 700,
    },
    {
        "created_at": "2022-05-19T08:16:19.294252+00:00",
        "id": 5,
        "name": "Iron",
        "price": 300,
    },
    {
        "created_at": "2022-05-19T10:00:19.663062+00:00",
        "id": 6,
        "name": "IPad",
        "price": 1500,
    },
]


def test_get_goods_routes(client, monkeypatch):
    from app import db

    def mock_get():
        return testing_data

    monkeypatch.setattr(db, "get", mock_get)
    response = client.get("/goods")
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    TESTING_NAME = "Phone"
    assert response.status_code == 200
    assert data[0]["name"] == TESTING_NAME

    # Get single item
    def mock_get_item(id):
        return [testing_data[0]]

    monkeypatch.setattr(db, "get_item", mock_get_item)
    response = client.get("/get_item/1")
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data[0]["id"] == 1


def test_insert_item_routes(client, monkeypatch):
    from app import db

    TESTING_NAME = "Testing Item"
    TESTING_PRICE = 370

    def mock_post(name, price):
        testing_data.append(
            {
                "created_at": "2022-05-18T13:42:56+00:00",
                "id": 7,
                "name": TESTING_NAME,
                "price": TESTING_PRICE,
            }
        )
        return [testing_data[-1]]

    monkeypatch.setattr(db, "post", mock_post)

    response = client.post(
        "/new_item",
        data=dict(
            name=TESTING_NAME,
            price=TESTING_PRICE,
        ),
    )
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data[0]["price"] == TESTING_PRICE


# def test_update_item_routes(client):
#     response = client.get("/goods")
#     data = json.loads(response.get_data(as_text=True))
#     TESTING_ID = data[0]["id"]
#     TESTING_NAME = "Testing Item"
#     TESTING_PRICE = 480
#     response = client.post(
#         f"/update_item/{TESTING_ID}",
#         data=dict(
#             name=TESTING_NAME,
#             price=TESTING_PRICE,
#         ),
#     )
#     assert response.status_code == 200
#     data = json.loads(response.get_data(as_text=True))
#     assert data[-1]["price"] == TESTING_PRICE


# def test_delete_item_routes(client):
#     response = client.get("/goods")
#     data = json.loads(response.get_data(as_text=True))
#     TESTING_ID = data[0]["id"]
#     response = client.post(
#         f"/delete_item/{TESTING_ID}",
#     )
#     assert response.status_code == 204
