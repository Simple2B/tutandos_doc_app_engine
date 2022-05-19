from app.views.blueprint import BlueprintApi
from flask import current_app as app
from supabase import create_client
from app.supabaseops import Good

# Set up Bluerints
api_docgen = BlueprintApi("/", __name__)


@api_docgen.get("/goods")
def get_goods():
    goods = Good()
    query_data = goods.get()
    return {"key": query_data}, 200


@api_docgen.route("/new_item", methods=["GET", "POST"])
def new_item():
    goods = Good()
    name_hardcoded = "Iron"
    price_hardcoded = 300
    insert_data = goods.post(name=name_hardcoded, price=price_hardcoded)

    return {"key": insert_data}, 200
