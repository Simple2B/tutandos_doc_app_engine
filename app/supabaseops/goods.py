from flask import current_app as app
from supabase import create_client


class Good:
    def __init__(self) -> None:
        self.SUPABASE_URL = app.config.get("SUPABASE_URL")
        self.SUPABASE_API_KEY = app.config.get("SUPABASE_API_KEY")

    def get(self) -> list:
        supabase = create_client(self.SUPABASE_URL, self.SUPABASE_API_KEY)
        query = supabase.table("testing_goods").select("*").execute()

        return query.data

    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
