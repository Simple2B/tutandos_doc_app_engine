from supabase import create_client
from typing import List
from .supabase_interface import SupaBaseClientInterface


class SupabaseClient(SupaBaseClientInterface):
    def init_app(self, app) -> None:
        SUPABASE_URL = app.config.get("SUPABASE_URL")
        SUPABASE_API_KEY = app.config.get("SUPABASE_API_KEY")
        self.supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

    def get(self, table: str, eq={}, count=None) -> List:
        query = self.supabase.table(table).select("*", count=count)

        for key, value in eq.items():
            query = query.eq(key, value)

        return query.execute().data

    def get_item(self, id):
        select = self.supabase.table("testing_goods").select("*").eq("id", id).execute()

        return select.data

    def create(self, name, price) -> list:
        insert = (
            self.supabase.table("testing_goods")
            .insert({"name": name, "price": price})
            .execute()
        )

        return insert.data

    def update(self, id, name=None, price=None):
        update = (
            self.supabase.table("testing_goods")
            .update({"price": price, "name": name})
            .eq("id", id)
            .execute()
        )

        return update.data

    def delete(self, id):
        deleting = self.supabase.table("testing_goods").delete().eq("id", id).execute()
        return deleting.data
