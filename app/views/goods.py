from app.views.blueprint import BlueprintApi
from flask import current_app as app
from supabase import create_client

# Set up Bluerints
api_docgen = BlueprintApi("/", __name__)


@api_docgen.get("/goods")
def get_goods():
    SUPABASE_URL = app.config.get("SUPABASE_URL")
    SUPABASE_API_KEY = app.config.get("SUPABASE_API_KEY")

    supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)
    query = supabase.table("testing_goods").select("*").execute()

    return {"key": query.data}, 200


@api_docgen.route("/new_item", methods=["GET", "POST"])
def new_item():
    SUPABASE_URL = app.config.get("SUPABASE_URL")
    SUPABASE_API_KEY = app.config.get("SUPABASE_API_KEY")

    supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)
    query = (
        supabase.table("testing_goods")
        .insert({"name": "Phone2", "price": "100"})
        .execute()
    )

    return {"key": query.data}, 200
