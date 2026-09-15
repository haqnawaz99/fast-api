# Lecture 03: Path Parameters and Query Parameters in FastAPI

## Step 1: Return a list of products

Start with a small product dataset and an endpoint that returns every product. Then learn to read path and query parameters in URLs. Step 4 implements a path parameter in a separate Python example; step 6 adds a required query parameter.

## Learning objectives

- Store sample data in a separate Python file.
- Import a variable from another module.
- Return a list of dictionaries through a GET endpoint.
- Check the JSON response in a browser and the API documentation.
- Identify path parameters and query parameters in a URL.
- Distinguish sending a parameter from implementing behavior that uses it.

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

## Step 3: Understand query parameters

Imagine browsing a shop: `/products` opens the product collection. Query parameters can supply search criteria or display options to that endpoint, once its code supports them.

Consider:

```text
http://127.0.0.1:8000/products?id=1&title=mobile&count=10
```

### Break the URL into parts

| Part | Meaning |
| --- | --- |
| `http://127.0.0.1:8000` | The local server address. |
| `/products` | The endpoint path. |
| `?` | Starts the query string. |
| `id=1` | A parameter named `id` with value `1`. |
| `&` | Separates one parameter from the next. |
| `title=mobile` | A parameter named `title` with value `mobile`. |
| `count=10` | A third parameter named `count` with value `10`. |

A **query string** is the part after `?`. Each **query parameter** is a name-value pair. Use `=` between a name and value, and `&` between pairs. Use one `?` to begin the query string, not another `?` for each parameter.

This example contains three query parameters and two `&` separators.

The path remains `/products`. The query supplies additional information to the request; it does not create a new route.

### What do these parameters do?

An API could use `id` and `title` to filter products, but their names alone do not define the behavior. The endpoint must read the values and decide how to use them. For example, whether both criteria must match depends on the implementation.

An API could define `count=10` as a request for at most ten matching products. It would return fewer if fewer matches exist. `count` is a name chosen by the API author, not a built-in FastAPI command; the endpoint must implement the limit. It does not mean product ID 10.

Our mock data uses the field `name`, not `title`, and contains no product named `mobile`. This URL illustrates query syntax. A future implementation must choose whether to accept `name`, map `title` to `name`, or use a different dataset.

### Predict the current response

The current `get_products()` function takes no parameters and always returns `products`. Try these addresses with `lecture_03.py` running:

| Request path and query | Current result |
| --- | --- |
| `/products` | HTTP 200 with the complete product list. |
| `/products?id=1` | HTTP 200 with the same complete list. |
| `/products?id=1&title=mobile&count=10` | HTTP 200 with the same complete list. |
| `/products?count=1` | HTTP 200 with all three sample products; no limit is implemented. |
| `/products/100` | HTTP 404 because no matching path route exists. |

The current endpoint ignores the supplied query parameters. Adding them to a URL does not automatically filter the data.

In PowerShell, keep the full URL in quotation marks so `&` stays part of the URL:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/products?id=1&title=mobile&count=10"
```

### Three URL forms at a glance

All three examples use the server `http://127.0.0.1:8000`:

| URL after the server address | What it supplies |
| --- | --- |
| `/products` | The collection path, with no parameter values. |
| `/products/100` | A path value of `100` for a future `/products/{product_id}` route. |
| `/products?id=1&title=mobile&count=10` | The collection path plus three query values: `id`, `title`, and `count`. |

Read the final URL as: "Send a GET request to `/products`, supplying ID 1, title mobile, and count 10." The endpoint decides what those values mean and how they affect its response.

### Path parameters and query parameters compared

| Question | Path parameter | Query parameter |
| --- | --- | --- |
| Where is it? | Inside the path, such as `100` in `/products/100`. | After `?`, such as `id=1`. |
| How is it named? | By a placeholder in the route, such as `{product_id}`. | By the name before `=`, such as `id`. |
| Common purpose | Identify a particular resource. | Supply filters, search text, sorting, or pagination options. |
| Is it required? | A declared path segment must be present to match that route. | It can be required or optional, depending on the endpoint definition. |

These are common design choices, not automatic database operations. Both kinds of parameters need endpoint code to produce the intended response.

### Small details to remember

- For distinct names such as `id` and `title`, changing their order still supplies the same named values: `?title=mobile&id=1`.
- URL values arrive as text. FastAPI can convert and validate them when the endpoint declares types, such as `int` for an ID.
- Spaces and special characters in values need URL encoding. For example, `title=mobile%20phone` represents `mobile phone`.
- Query parameters are not always optional; the endpoint definition decides whether omitting one is allowed.

### Practice with answers

1. In `/products?id=2&title=Mouse`, identify the path and both name-value pairs.
2. Correct `/products?id=1?title=mobile`.
3. Does `/products?id=1` currently return only one product? Explain why.
4. How many query parameters are in `/products?id=1&title=mobile&count=10`?
5. Would `/products?count=1` currently limit the response to one product?

**Answers:**

1. Path: `/products`; pairs: `id=2` and `title=Mouse`.
2. `/products?id=1&title=mobile`.
3. No. The current function returns the complete list without using query parameters.
4. Three: `id`, `title`, and `count`.
5. No. The current endpoint ignores `count` and returns all three sample products.

## Step 4: Implement a path parameter with comments

Use [lecture_03_01.py](../lecture_03_01.py). It preserves the home and product-list endpoints and adds this small example:

```python
# Path parameter: {product_id} captures a value from the URL path.
# The @ makes this a decorator that registers the function as a GET endpoint.
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    # The argument name matches {product_id} in the route.
    # FastAPI converts the URL value to an integer before calling this function.
    # Invalid integer values, such as "abc", receive HTTP 422 automatically.
    # Return the received ID as JSON; this step does not look up a product.
    return {"id": product_id}
```

### Follow a request through the code

1. The browser requests `/product/100`.
2. The route `/product/{product_id}` matches and captures `100`.
3. `product_id: int` tells FastAPI to convert and validate the value as an integer.
4. FastAPI calls `get_one_product()` with the integer `100`.
5. The function returns a dictionary, which becomes the JSON response `{"id": 100}`.

The placeholder name and function argument must match. The colon in `product_id: int` introduces a Python type annotation. FastAPI uses this annotation for request conversion, validation, and documentation.

Keep the `@` before `app.get(...)`. Without it, that line does not decorate and register the function below it.

### Run and check

Stop the earlier server with `Ctrl+C`, then run from PowerShell:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03_01.py
```

Open <http://127.0.0.1:8000/product/100>:

```json
{"id": 100}
```

Expect HTTP `200 OK`. The value has no quotation marks because it is a JSON number.

| Request path | Expected behavior in this example |
| --- | --- |
| `/product/1` | HTTP 200 with `{"id": 1}`. |
| `/product/100` | HTTP 200 with `{"id": 100}`, even though the mock data has no product 100. |
| `/product/abc` | HTTP 422 with validation details: the value cannot be parsed as an integer. |
| `/product/1.5` | HTTP 422: a decimal value is not a valid integer here. |
| `/products` | HTTP 200 with the complete product list. |
| `/products/100` | HTTP 404: this example uses singular `/product/{product_id}`. |

Earlier conceptual URLs used `/products/{product_id}`. The implemented route in this step is `/product/{product_id}`. Both are possible naming choices, but the browser path must match the route you registered.

This function echoes the supplied ID. Its name does not make it search `mock.py`. Integer validation also does not check that a product exists or require a positive ID. Product lookup and additional rules are separate steps.

Open <http://127.0.0.1:8000/docs>, expand **GET /product/{product_id}**, and select **Try it out**. Enter `100` into the required `product_id` field, then select **Execute**.

### Practice

1. Request `/product/2` and predict the JSON before checking it.
2. Request `/product/abc` and compare its status with `/products/100`.
3. Explain why `/product/999` succeeds even though the dataset has only three products.

## Step 5: Find and return the matching product

Use [lecture_03_02.py](../lecture_03_02.py). This new example keeps `/` and `/products` and changes the single-product function from echoing an ID to searching the data. The previous examples remain available.

```python
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
```

### Understand each part

- `products` is the list imported from `mock.py`.
- `for one_product in products:` visits one dictionary at a time. `one_product` is a temporary variable for the current dictionary.
- `one_product.get("id")` reads that dictionary's ID. If the key is absent, `.get()` returns `None` instead of raising a `KeyError`.
- `==` compares the stored ID with the requested ID. It does not assign a value.
- `return one_product` sends the full matching dictionary back and immediately ends the function. No additional `break` is needed.
- The last `return` runs only if the loop finishes without a match. It also handles an empty product list.

The stored IDs and the validated `product_id` are integers, so they can be compared directly. A product ID is not a list index: the code checks the `id` field rather than assuming an item's position.

### Trace a request for product 2

1. FastAPI receives `/product/2` and converts the path value to integer `2`.
2. The loop checks Laptop: `1 == 2` is false, so it continues.
3. It checks Mouse: `2 == 2` is true.
4. The function returns the Mouse dictionary and stops before checking Keyboard.

For `/product/100`, none of the three IDs match, so the function reaches the error-message return after the loop.

### Why indentation matters

Keep the error-message return outside the `for` loop, at the same indentation level as `for`. If it is inside the loop, a nonmatching first product could end the search before later products are checked.

### Run and check

Stop the earlier server with `Ctrl+C`, then run:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03_02.py
```

Open <http://127.0.0.1:8000/product/2>. Expect HTTP 200 and:

```json
{"id": 2, "name": "Mouse", "price": 25}
```

Open <http://127.0.0.1:8000/product/100>. In this teaching step, expect HTTP 200 with:

```json
{"error": "Product not Found for this ID."}
```

An `error` key is just response content. Returning this dictionary does not automatically set HTTP status 404. A later error-handling step can introduce `HTTPException` to send a proper missing-product status.

| Request | Expected result in `lecture_03_02.py` |
| --- | --- |
| `/product/1` | HTTP 200 with Laptop. |
| `/product/2` | HTTP 200 with Mouse; confirms the search continues past the first item. |
| `/product/3` | HTTP 200 with Keyboard. |
| `/product/100` | HTTP 200 with the custom error message. |
| `/product/abc` | HTTP 422 before the lookup function runs. |
| `/products/100` | HTTP 404 because this path has no route. |

Use `/docs` to execute the same requests and inspect both the response body and status code.

### Practice

1. Request product 3 and explain which comparisons happen before it is returned.
2. In a practice copy, move the final return inside the loop. Predict and observe what happens when requesting product 2, then restore the indentation.
3. Explain the difference between an invalid integer, a valid integer with no matching product, and a URL with no matching route.

## Step 6: Greet a user with a query parameter

Use [lecture_03_03.py](../lecture_03_03.py). It keeps the previous endpoints and appends:

```python
# Query parameter: supply name after ? in the URL, e.g. /greet?name=Ali.
@app.get("/greet")
def greet_user(name: str):
    # name is a query parameter because it is not a placeholder in /greet.
    # str means text; with no default value, name is required.
    # The f-string inserts the supplied name into the greeting.
    return {"greet": f"Hello {name}, Hows You ?"}
```

### Understand the code

For `/greet?name=Ali`, the path is `/greet` and the query parameter is `name=Ali`. FastAPI reads the value and passes `"Ali"` to `greet_user()`.

`name: str` declares a text argument. Because `name` is not a placeholder in the route, FastAPI treats this simple argument as a query parameter. With no default value, it is required.

An **f-string** starts with `f` and inserts the value inside braces into the text. Here, `{name}` inserts the supplied name. These braces format a response string; they do not declare a URL path parameter.

### Run and check

Stop the earlier server with `Ctrl+C`, then run in PowerShell:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03_03.py
```

Open <http://127.0.0.1:8000/greet?name=Ali>. Expect HTTP 200 and:

```json
{"greet": "Hello Ali, Hows You ?"}
```

| Request | Expected result |
| --- | --- |
| `/greet?name=Sara` | HTTP 200 with `Hello Sara, Hows You ?` in the `greet` field. |
| `/greet` | HTTP 422: required `name` is missing. |
| `/greet?username=Ali` | HTTP 422: `username` does not supply `name`. |
| `/greet/Ali` | HTTP 404: this route takes the name in the query string. |
| `/greet?name=Ali%20Khan` | HTTP 200 with `Hello Ali Khan, Hows You ?`. |
| `/greet?name=` | HTTP 200 with `Hello , Hows You ?`. |

Required means the parameter must be present. `str` alone does not require nonempty text. Missing-value validation details identify `name` as a query parameter.

Open `/docs`, expand **GET /greet**, select **Try it out**, enter a name, and select **Execute**. The documentation marks `name` as required.

### Compare the endpoints

`/product/2` passes an ID in the path. `/greet?name=Ali` passes a name after `?`. Implementing `name` on `/greet` does not add filtering to `/products`; the product-list endpoint still returns every product.

### Practice

1. Request a greeting for your own name.
2. Omit `name`, then supply an empty value. Explain the difference in responses.
3. Explain why `/greet/Ali` does not call this function.

## Next small steps

Add product query filtering and HTTP error handling in later separate examples. Preserve each completed example as its own file.

## Reference

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI: Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI: Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
