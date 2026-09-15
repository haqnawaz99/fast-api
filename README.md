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

Each lecture will have numbered notes linked to its Python examples. As later lectures extend `main.py`, completed examples can be preserved in numbered lecture folders.
