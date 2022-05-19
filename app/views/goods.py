from app.views.blueprint import BlueprintApi
from app.supabaseops import Good

# Set up Bluerints
api_docgen = BlueprintApi("/", __name__)


@api_docgen.get("/goods")
def get_goods():
    goods = Good()
    query_data = goods.get()
    return {"key": query_data}, 200


@api_docgen.route("/get_item/<int:item_id>", methods=["GET", "POST"])
def get_item(item_id):
    goods = Good()
    update_data = goods.get_item(id=item_id)

    return {"key": update_data}, 200


@api_docgen.route("/new_item", methods=["GET", "POST"])
def new_item():
    goods = Good()
    name_hardcoded = "Iron"
    price_hardcoded = 300
    insert_data = goods.post(name=name_hardcoded, price=price_hardcoded)

    return {"key": insert_data}, 201


@api_docgen.route("/update_item/<int:item_id>", methods=["GET", "POST"])
def update_item(item_id):
    goods = Good()
    price_hardcoded = 350
    update_data = goods.update(id=item_id, price=price_hardcoded)

    return {"key": update_data}, 200


@api_docgen.route("/delete_item/<int:item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    goods = Good()
    delete_data = goods.delete(id=item_id)

    return {"key": delete_data}, 204
