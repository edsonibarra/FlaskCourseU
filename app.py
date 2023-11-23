from flask import Flask, request

"""
To run the app:
    - flask run
"""

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 100
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    """
    Endpoint to create a new store without items.
    """
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
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
