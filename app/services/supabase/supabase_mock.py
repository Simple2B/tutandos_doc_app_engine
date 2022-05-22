from typing import List
from .supabase_interface import SupaBaseClientInterface


class SupabaseMock(SupaBaseClientInterface):
    def __init__(self):
        self.data = [
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

    def init_app(self, app) -> None:
        pass

    def get(self) -> List:
        query = self.data

        return query

    def get_item(self, id):
        for dictionary in self.data:
            if dictionary["id"] == id:
                return dictionary

    def post(self, name, price) -> list:
        insert = {
            "created_at": "2022-05-19T10:00:19.663062+00:00",
            "id": 7,
            "name": name,
            "price": int(price),
        }

        self.data.append(insert)

        return self.data

    def update(self, id, name=None, price=None):
        for index, dictionary in enumerate(self.data):
            if dictionary["id"] == id:
                dictionary["name"] = name
                dictionary["price"] = int(price)
                updated_index = index

        return self.data[updated_index]

    def delete(self, id):
        for dictionary in self.data:
            if dictionary["id"] == id:
                return 204
