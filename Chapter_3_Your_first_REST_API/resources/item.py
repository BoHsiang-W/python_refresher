import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items

blp = Blueprint("Items", __name__, description="Item operations")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted successfully"}
        except KeyError:
            abort(404, message="Item not found")

    def put(self, item_id):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Bad request. Ensure all required fields are filled.")

        try:
            item = items[item_id]
            item.update(item_data)  # Update the item with the new data
            return item
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"item": list(items.values())}

    def post(self):
        item_data = request.get_json()
        if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort(400, message="Bad request. Ensure all required fields are filled.")

        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists in the store")

        item_id = uuid.uuid4().hex
        new_item = {**item_data, "id": item_id}
        items[item_id] = new_item

        return new_item, 201
