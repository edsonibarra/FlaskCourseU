from flask import Flask

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

@app.route("/")
def home():
    return "<h1>Flask Udemy Course</h1>"

@app.route("/store")
def get_store():
    return {"stores": stores}
