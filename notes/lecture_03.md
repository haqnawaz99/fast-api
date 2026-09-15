# Lecture 03: Path Parameters and Query Parameters in FastAPI

## Step 1: Return a list of products

Before adding parameters, create a small product dataset and an endpoint that returns every product. Path and query parameters will be added in later small steps.

## Learning objectives

- Store sample data in a separate Python file.
- Import a variable from another module.
- Return a list of dictionaries through a GET endpoint.
- Check the JSON response in a browser and the API documentation.

## 1. Create the mock data

Create [mock.py](../mock.py) next to the application file:

```python
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Keyboard", "price": 75},
]
```

Mock data is made-up data used for learning or testing. These prices are fictional numbers for practice, with no currency assigned.

`products` is a Python list. Each item is a dictionary containing an `id`, a `name`, and a `price`. Each product has a different ID. This file stores data; it does not start a server or connect to a database.

## 2. Create the application

Create [lecture_03.py](../lecture_03.py):

```python
from fastapi import FastAPI
from mock import products

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"


@app.get("/products")
def get_products():
    return products
```

`from mock import products` imports the variable from `mock.py`. Omit `.py` in the import statement. Keep both files in the same directory.

`@app.get("/products")` registers the function below it for GET requests to `/products`. When a request arrives, `get_products()` returns the imported list. FastAPI converts the list and its dictionaries to a JSON array containing JSON objects.

The home endpoint still returns the welcome message. The earlier lecture files remain available as separate examples.

## 3. Start the server

Stop any earlier server with `Ctrl+C`. From the project directory in PowerShell, use the existing environment:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03.py
```

If project dependencies have not been installed, follow the [README setup instructions](../README.md#setup-windows-powershell) first. No new dependencies are needed for this step.

## 4. Check the response

Open <http://127.0.0.1:8000/products>. Expect HTTP status `200 OK` and this JSON response (spacing may differ):

```json
[
  {"id": 1, "name": "Laptop", "price": 1200},
  {"id": 2, "name": "Mouse", "price": 25},
  {"id": 3, "name": "Keyboard", "price": 75}
]
```

You can also request it from another PowerShell terminal:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/products"
```

PowerShell converts the JSON response into objects and may display them as a table.

Open <http://127.0.0.1:8000/docs>, expand **GET /products**, select **Try it out**, then **Execute**. This step has no request parameters to enter.

## Common problems

| Problem | What to check |
| --- | --- |
| Python cannot import `mock` | Put `mock.py` beside `lecture_03.py` and run from the project directory. |
| Python cannot import `products` | Check that the variable in `mock.py` is named exactly `products`. |
| `/products` returns 404 | Save the files, start `lecture_03.py`, and check the path spelling. |
| A syntax error appears in the data | Check commas between dictionaries and matching brackets and quotation marks. |
| Port 8000 is already in use | Stop the previous server with `Ctrl+C` before running this example. |

## Practice

1. Add a fourth product with a unique ID in `mock.py`, save, and refresh `/products` after the development server reloads.
2. Change one product name and check the new response.
3. Visit `/` and `/products` and explain why their response structures differ.

## Step 2: Understand path parameters

Compare these two addresses:

| URL | Intended meaning |
| --- | --- |
| `http://127.0.0.1:8000/products` | Request the complete product list. |
| `http://127.0.0.1:8000/products/100` | Request the product whose ID is `100`, once a matching endpoint is implemented. |

### Read the URL in small parts

- `http://` is the protocol used for the request.
- `127.0.0.1:8000` is the local server address and port.
- `/products` identifies the product collection.
- `/100` adds a value identifying a particular product.

A **path parameter** is a variable part of a URL path. In FastAPI, a route pattern such as `/products/{product_id}` declares a placeholder named `product_id`.

For a request to `/products/100`, FastAPI captures `100` and passes it to the matching endpoint function as `product_id`. A request to `/products/2` supplies `2` instead. We write braces in the route definition; we put the actual value in the browser URL.

The ID is a product identifier, not a list position or the number of products to return. Capturing an ID does not automatically search `products`; the endpoint function must perform that lookup.

### What happens with our current example?

`lecture_03.py` currently registers only `/` and `/products`. Visiting `/products/100` therefore returns HTTP `404 Not Found` with:

```json
{"detail":"Not Found"}
```

This happens because the parameterized route has not been added yet. Also, our sample data contains IDs `1`, `2`, and `3`, so `100` is only an illustration of a URL value, not an existing product.

### Quick practice

1. In `/products/2`, identify the fixed part of the path and the parameter value.
2. For the pattern `/products/{product_id}`, what value would `/products/3` supply?
3. Explain why typing `/products/100` does not automatically create an endpoint.

## Next small steps

Implement a path parameter in a new Python example, then introduce query parameters. The current runnable example still returns the complete product list.

## Reference

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI: Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
