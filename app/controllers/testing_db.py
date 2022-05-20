# flake8: noqa F501
from supabase import create_client
from flask import current_app as app

SUPABASE_URL = "https://utitytmrxlwyizpxegtv.supabase.co/rest/v1/testing_db?select=*"
# SUPABASE_URL = app.config["SUPABASE_URL"]
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV0aXR5dG1yeGx3eWl6cHhlZ3R2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTI4ODA5NDMsImV4cCI6MTk2ODQ1Njk0M30.40GTqnuw7QN9RxOyFpzl6yvNQ66brTUZPwg-Z42HcuY"
TESTING_ITEMS_NUMBER = 10

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)


def init_testing_db():
    for i in range(1, TESTING_ITEMS_NUMBER + 1):
        name = f"item_{i}"
        price = i * 100
        insert = (
            supabase.table("testing_db")
            .insert({"name": name, "price": price})
            .execute()
        )


def drop_testing_db():
    for i in range(1, TESTING_ITEMS_NUMBER + 1):
        name = f"item_{i}"
        price = i * 100
        supabase.table("testing_goods").delete().eq("name", name).execute()
