import uuid
from flask import Flask, request
from db import items, stores


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

@app.post("/store/<string:store_name>/item")
def create_item(store_name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == store_name:
            new_item = {
                "name": request_data["name"],
                "amount": request_data["amount"]
            }
            store["items"].append(new_item)
            return new_item, 201
    return {"message": f"Store {store_name} was not found"}, 404

@app.get("/store/<string:store_id>")
def get_store(store_id):
    """
    Pull specific store and its items.
    """
    try:
        return stores[store_id], 200
    except KeyError:
        return {"message": f"store with id {store_id} not found"}, 404
