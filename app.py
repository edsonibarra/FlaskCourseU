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

  
