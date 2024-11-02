import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items

app = Flask(__name__)


@app.get("/store")  # http://127.0.0.1:5000/store
def get_stores():
    return {"store": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure all required fields are filled.")

    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exists")

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/item")
def create_item():
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

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item

    return new_item, 201


@app.get("/item")
def get_all_item():
    return {"item": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


@app.get("/item/<string:item_id>")
def get_items(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")
