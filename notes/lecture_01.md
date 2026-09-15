# Lecture 01: Installing FastAPI and checking its version

## Overview

This lesson covers setting up a Python virtual environment, installing FastAPI, and checking its installed version with a simple Python program. Commands use Windows PowerShell.

## Learning objectives

By the end of this lesson, students should be able to:

- Explain why a project uses a virtual environment.
- Install FastAPI into that environment.
- Import a Python package and display its version.
- Run a Python file from the terminal.

## 1. Prepare the virtual environment

A virtual environment gives this project its own installed packages. Installing a package here keeps the project's dependencies separate from other projects.

Our environment is named `.venv`. On a fresh copy of the repository, create it with:

```powershell
py -m venv .venv
```

Activate it from the repository folder:

```powershell
.\.venv\Scripts\Activate.ps1
```

The terminal usually displays `(.venv)` after activation. The name in parentheses identifies the active environment.

## 2. Install FastAPI

With the virtual environment activated, run:

```powershell
python -m pip install "fastapi[standard]"
```

`python -m pip` runs pip using the selected Python interpreter. `install` adds a package, and `[standard]` requests FastAPI's standard optional dependencies. Keep the quotation marks around the package specification.

See the [official FastAPI documentation](https://fastapi.tiangolo.com/tutorial/#install-fastapi) for additional installation guidance.

For the version recorded in this repository, install from the dependency file instead:

```powershell
python -m pip install -r requirements.txt
```

`requirements.txt` pins FastAPI's version. Its additional dependencies are resolved by pip and are not individually pinned.

## 3. Create main.py

Create [main.py](../main.py) with the following code:

```python
import fastapi

print(fastapi.__version__)
```

| Code | Explanation |
| --- | --- |
| `import fastapi` | Makes the installed FastAPI package available in this file. |
| `fastapi.__version__` | Reads the package's version string; there are two underscores on each side of `version`. |
| `print(...)` | Displays that value in the terminal. |

## 4. Run the file

```powershell
python main.py
```

This repository pins FastAPI to `0.141.1`, so its expected output is:

```text
0.141.1
```

A different version number can simply mean a different release was installed. This script checks installation and then exits. It does not yet create an API application or start a web server.

## 5. Common problems

| Problem | What to check |
| --- | --- |
| `ModuleNotFoundError: No module named 'fastapi'` | Install dependencies using the same interpreter that runs the script. |
| PowerShell blocks activation | Run `.\.venv\Scripts\python.exe main.py` directly; activation is optional. |
| VS Code cannot resolve the import | Choose `.venv\Scripts\python.exe` using **Python: Select Interpreter**. |
| Python cannot find `main.py` | Open the terminal in the repository folder. |
| Import behaves unexpectedly | Do not name your own file `fastapi.py`; that can hide the installed package. |

To confirm which interpreter is running:

```powershell
python -c "import sys; print(sys.executable)"
```

Its path should end in `.venv\Scripts\python.exe`. To leave the activated environment, run `deactivate`.

## Practice

1. Run `main.py` and record the installed FastAPI version.
2. Change the print statement to `print("FastAPI version:", fastapi.__version__)` and run it again.
3. Explain why installing a package in one Python environment may not make it available in another.
4. Does this program start a web server? Explain your answer.

## Recap

Create or activate the environment, install FastAPI, import it in `main.py`, and print its version to confirm that the package is available.
