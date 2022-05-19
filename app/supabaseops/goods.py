from flask import current_app as app
from supabase import create_client

# from pydantic import parse_obj_as
# from app.pydantic_models.basic_models import SupabaseItems


class Good:
    def __init__(self) -> None:
        self.SUPABASE_URL = app.config.get("SUPABASE_URL")
        self.SUPABASE_API_KEY = app.config.get("SUPABASE_API_KEY")
        self.supabase = create_client(self.SUPABASE_URL, self.SUPABASE_API_KEY)

    def get(self) -> list:
        query = self.supabase.table("testing_goods").select("*").execute()
        # print(type(query.data))

        return query.data

    def get_item(self, id):
        select = self.supabase.table("testing_goods").select("*").eq("id", id).execute()

        return select.data

    def post(self, name, price) -> list:
        insert = (
            self.supabase.table("testing_goods")
            .insert({"name": name, "price": price})
            .execute()
        )

        return insert.data

    def update(self, id, name=None, price=None):
        update = (
            self.supabase.table("testing_goods")
            .update({"price": price})
            .eq("id", id)
            .execute()
        )

        return update.data

    def delete(self, id):
        deleting = self.supabase.table("testing_goods").delete().eq("id", id).execute()
        return deleting.data
