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
def get_store():
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

@app.post("/item")
def create_item_in_store():
    request_data = request.get_json()
    # validate name and items exists in the payload
    new_store_name = request_data.get("name", None)
    new_items = request_data.get("items", None)
    
    if new_store_name is None or new_items is None:
        return {"message": "Invalid parameters"}, 400
    
    # Look up store name
    store_found = False
    for store in stores:
        if store["name"] == new_store_name:
            store_found = True
            store_items = store["items"]
            for item in new_items:
                print("Item:",item)
                store_items.append(item)

    if store_found:
        return {"message": "Item(s) created."}, 201
    else:
        return {"message": f"Store with name {new_store_name} was not found"}, 404