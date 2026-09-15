# Lecture 02: Your First FastAPI Server and GET Endpoint

## Step 1: Create and start the application

This first step creates a FastAPI application and starts a local development
server. We will add our first GET endpoint in a later step of this lecture.

## Learning objectives

- Import FastAPI and create an application object.
- Start and stop the development server.
- Open the application and its automatic documentation in a browser.
- Explain why an application without a root endpoint returns `Not Found`.

## Python example

The runnable example is [lecture_02.py](../lecture_02.py).

```python
from fastapi import FastAPI

app = FastAPI()
```

`from fastapi import FastAPI` imports the class used to create an application.
`app = FastAPI()` creates the application object. We will register endpoints on
this object in subsequent steps.

Creating the object does not start a server by itself. We use the FastAPI
development command to serve the application.

## Start the server

Open PowerShell in the project directory. Use the existing `.venv` environment:

```powershell
.\.venv\Scripts\Activate.ps1
fastapi dev lecture_02.py
```

If activation is unavailable, run the environment's executable directly:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_02.py
```

Keep the terminal running while using the application. Development mode reloads
the server when source files change. It is intended for local development.

Expected startup output includes a server address such as
`http://127.0.0.1:8000` and an application startup completion message. Exact log
formatting can vary by installed version.

## Open the application

Visit <http://127.0.0.1:8000> in your browser. At this stage, expect HTTP status
`404` with this JSON response:

```json
{"detail":"Not Found"}
```

This means the server received the request, but no endpoint matches the root
path `/`. It does not mean the server failed to start.

Opening this address in a browser sends a GET request. GET is an HTTP method
used to request data. An endpoint connects a method and path to a Python
function that handles the request. Our application has no custom endpoints yet.

Visit <http://127.0.0.1:8000/docs> to open the automatic interactive API
documentation. The documentation page is available, but has no custom
operations to display at this stage.

`127.0.0.1` refers to your own computer, and `8000` is the port used by the
development server. Press `Ctrl+C` in the server terminal to stop it.

## Common problems

| Problem | What to check |
| --- | --- |
| `fastapi` is not recognized | Activate `.venv` or use the executable path shown above. |
| The FastAPI executable is missing | Follow the dependency installation instructions in the project README. The CLI requires FastAPI's standard dependencies. |
| The source file cannot be found | Run the command from the directory containing `lecture_02.py`. |
| The browser cannot connect | Check that the server is still running and that the browser address matches the terminal output. |
| Port 8000 is already in use | Stop your earlier server with `Ctrl+C`, or run `fastapi dev lecture_02.py --port 8001` and visit port `8001`. |
| `/` returns `Not Found` | This is expected until a root endpoint is added. |

## Practice

1. Start the example and open `/` and `/docs`.
2. Explain why `/` returns a 404 response while `/docs` opens successfully.
3. Stop the server and observe what happens when you refresh the browser.
4. Restart the server using port `8001` and open its documentation.

## Reference

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

## Step 2: Add the home endpoint

Use [lecture_02_01.py](../lecture_02_01.py). Keep the previous file so each step can be run separately.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI Series !"
```

`@app.get("/")` is a decorator: it registers the function below it to handle GET requests to the root path `/`. FastAPI calls `home()` when that request arrives. The function returns a Python string, which FastAPI sends as a JSON string by default.

Stop the earlier server with `Ctrl+C`, then run:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_02_01.py
```

Open <http://127.0.0.1:8000/>. Expect HTTP status `200 OK` and this response body:

```json
"Welcome to FastAPI Series !"
```

The quotation marks belong to the JSON string format. The response is a string, not a JSON object with named fields.

## Step 3: Add the contact endpoint

Use [lecture_02_02.py](../lecture_02_02.py). It keeps the home endpoint and adds this code below it:

```python
@app.get("/contact")
def contact():
    return "You can connect us any time."
```

The decorator connects GET requests at `/contact` to `contact()`. Defining a function alone does not register an endpoint. The path in the decorator determines the URL; the function name does not.

Stop the earlier server with `Ctrl+C`, then run:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_02_02.py
```

Open <http://127.0.0.1:8000/contact>. Expect HTTP status `200 OK` and:

```json
"You can connect us any time."
```

The root URL still returns the welcome message. Open <http://127.0.0.1:8000/docs> to see both `GET /` and `GET /contact`. Expand an operation, select **Try it out**, and then **Execute** to inspect its response.

### Common problems with endpoints

- If `/contact` returns 404, check that you saved and started `lecture_02_02.py` and included its decorator.
- Keep each decorator directly above the function it registers.
- Indent each `return` statement by four spaces.
- Run one example at a time on port 8000 to avoid a port conflict.

### Practice with endpoints

1. Change the home message, save the file, and refresh the browser.
2. Visit both endpoints in step 3 and explain which function handles each request.
3. Try an unregistered path such as `/missing` and explain the 404 response.
