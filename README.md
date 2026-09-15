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

Each small step has a separate Python example, preserving earlier steps for teaching.

## Run Lecture 02

After installing the requirements, run one example at a time from PowerShell:

```powershell
.\.venv\Scripts\fastapi.exe dev lecture_02.py
```

Open <http://127.0.0.1:8000/>; the empty app returns `404 Not Found`. Stop the server with `Ctrl+C`, then replace the filename with `lecture_02_01.py` to add the home endpoint or `lecture_02_02.py` to add `/contact`. Automatic API documentation is available at <http://127.0.0.1:8000/docs>.
