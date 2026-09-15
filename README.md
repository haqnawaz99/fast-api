# FastAPI Teaching

Lecture notes and runnable Python examples for learning FastAPI.

## Setup (Windows PowerShell)

Run these commands from the repository folder. The `.venv` environment already exists on this computer; create it only when setting up a fresh copy.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

If activation is blocked, use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Lectures

| Lecture | Notes | Python example |
| --- | --- | --- |
| 01: Installation and version check | [Notes](notes/lecture_01.md) | [main.py](main.py) |
| 02: First server and GET endpoints | [Notes](notes/lecture_02.md) | [Empty app](lecture_02.py), [home endpoint](lecture_02_01.py), [contact endpoint](lecture_02_02.py) |
| 03: Path and query parameters | [Notes](notes/lecture_03.md) | [Product list](lecture_03.py), [path parameter](lecture_03_01.py), [product lookup](lecture_03_02.py), [mock data](mock.py) |

Each small step has a separate Python example, preserving earlier steps for teaching.

## Run Lecture 02

After installing the requirements, run one example at a time from PowerShell:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_02.py
```

Open <http://127.0.0.1:8000/>; the empty app returns `404 Not Found`. Stop the server with `Ctrl+C`, then replace the filename with `lecture_02_01.py` to add the home endpoint or `lecture_02_02.py` to add `/contact`. Automatic API documentation is available at <http://127.0.0.1:8000/docs>.

## Run Lecture 03

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03.py
```

Stop any earlier server first. Open <http://127.0.0.1:8000/products> to see the sample product list from `mock.py`. This first step prepares the data and endpoint for later path and query parameter examples.

For the commented path-parameter example, stop the server and run:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03_01.py
```

Open <http://127.0.0.1:8000/product/100> to receive `{"id": 100}`. This step returns the supplied ID without looking up a product.

For product lookup, stop the server and run:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_03_02.py
```

Open <http://127.0.0.1:8000/product/2> to receive the Mouse product. A missing ID returns an error-message dictionary with HTTP 200 in this step; see the notes for the distinction between response content and HTTP status.
