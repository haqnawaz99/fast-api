from fastapi import FastAPI
from mock import products

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"


@app.get("/products")
def get_products():
    return products


# Capture the product ID from the path and validate it as an integer.
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    # Check each product dictionary in the list, one at a time.
    for one_product in products:
        # Read its ID and compare it with the ID supplied in the URL.
        if one_product.get("id") == product_id:
            # A match ends the function immediately and returns the full product.
            return one_product

    # Outside the loop: return this only after every product has been checked.
    # A normal dictionary response still has HTTP status 200 in this step.
    return {"error": "Product not Found for this ID."}


# Query parameter: supply name after ? in the URL, e.g. /greet?name=Ali.
@app.get("/greet")
def greet_user(name: str):
    # name is a query parameter because it is not a placeholder in /greet.
    # str means text; with no default value, name is required.
    # The f-string inserts the supplied name into the greeting.
    return {"greet": f"Hello {name}, Hows You ?"}
