from flask import request, jsonify
from app.views.blueprint import BlueprintApi
from app.services import db

# Set up Bluerints
api_docgen = BlueprintApi("/", __name__)


@api_docgen.get("/goods")
def get_goods():
    query_data = db.get()
    return jsonify(query_data)


@api_docgen.route("/get_item/<int:item_id>", methods=["GET", "POST"])
def get_item(item_id):
    update_data = db.get_item(id=item_id)

    return jsonify(update_data), 200


@api_docgen.route("/new_item", methods=["GET", "POST"])
def new_item():
    name = request.form["name"]
    price = request.form["price"]
    insert_data = db.post(name=name, price=price)

    return jsonify(insert_data), 201


@api_docgen.route("/update_item/<int:item_id>", methods=["GET", "POST", "PUT"])
def update_item(item_id):
    name = request.form["name"]
    price = request.form["price"]
    update_data = db.update(id=item_id, name=name, price=price)

    return jsonify(update_data), 200


@api_docgen.route("/delete_item/<int:item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    delete_data = db.delete(id=item_id)

    return {"key": delete_data}, 204
