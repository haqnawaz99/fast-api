from fastapi import FastAPI
from mock import products

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"


@app.get("/products")
def get_products():
    return products


# Path parameter: {product_id} captures a value from the URL path.
# The @ makes this a decorator that registers the function as a GET endpoint.
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    # The argument name matches {product_id} in the route.
    # FastAPI converts the URL value to an integer before calling this function.
    # Invalid integer values, such as "abc", receive HTTP 422 automatically.
    # Return the received ID as JSON; this step does not look up a product.
    return {"id": product_id}
