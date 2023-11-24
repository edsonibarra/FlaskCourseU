import uuid
from flask import Flask, request
from db import items, stores
from flask_smorest import abort
from custom_message import NOT_FOUND_MSG


"""
To run the app:
    - flask run
"""

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    """
    Endpoint to create a new store without items.
    """
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {
        "id": store_id,
        **store_data,
    }
    stores[store_id] = new_store
    return new_store, 201

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores.keys():
        return abort(404, message="Store not found.")
    item_id = uuid.uuid4().hex
    item = {
        **item_data,
        "id": item_id,
    }
    items[item_id] = item
    return item, 201

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    """
    Pull specific store and its items.
    """
    try:
        return stores[store_id], 200
    except KeyError:
        abort(404, message="Store not found.")
    
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id], 200
    except KeyError:
        abort(404, message="Item not found.")
