import json
from typing import List
from .supabase_interface import SupaBaseClientInterface

INIT_STATIC_PATH = "tests/static/supabase_init_data.json"


class SupabaseMock(SupaBaseClientInterface):
    def __init__(self):
        print("Supabase mock init")
        with open(INIT_STATIC_PATH) as init_data_f:
            self.data = json.load(init_data_f)

    def init_app(self, app) -> None:
        ...

    def get(self, table: str, eq={}, count=None) -> List:
        # TODO simulate behavior "no such table"
        # TODO simulate behavior "no such column"

        result = []
        for element in self.data[table]:
            if count and len(result) >= count:
                return result

            eq_flag = True
            for key, value in eq.items():
                if key in ("id", "audit_id"):
                    value = str(value)

                if element[key] != value:
                    eq_flag = False
                    break

            if eq_flag:
                result.append(element)

        return result

    def get_item(self, id):
        for dictionary in self.data:
            if dictionary["id"] == id:
                return dictionary

    def create(self, name, price) -> list:
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
