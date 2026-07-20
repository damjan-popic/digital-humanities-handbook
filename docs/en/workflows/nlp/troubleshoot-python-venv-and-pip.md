---
title: "How do I troubleshoot Python venv and pip problems?"
description: "Diagnose common beginner Python environment problems before debugging the code itself."
category: "NLP"
difficulty: "beginner"
time: "15–45 min"
tags: [Python, venv, pip, troubleshooting, beginner]
---

# How do I troubleshoot Python venv and pip problems?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>15–45 min</span>
</div>

## What you are trying to do

Most beginner Python problems are not deep programming problems. They are environment problems: wrong Python version, inactive virtual environment, wrong `pip`, wrong folder, missing package, or a script being run from the wrong place.

Before debugging code, diagnose the environment.

!!! quote "One-sentence version"
    Check Python version, environment activation, current folder, package location, and the full error message before changing code.

## You need

- A terminal.
- A project folder.
- Python 3.12.
- The ability to copy the exact error message.

## Tools

- `python --version`: checks active Python.
- `python -m pip --version`: checks which pip belongs to active Python.
- `pwd` or `cd`: checks the current folder.
- `dir` or `ls`: lists files.
- `python -c "..."`: runs a one-line Python diagnostic.

## Workflow

### Step 1: Check the Python version

```bash
python --version
```

Expected inside the virtual environment:

```text
Python 3.12.x
```

If you see Python 3.13 or higher, stop and recreate the environment with Python 3.12.

### Step 2: Check whether the environment is active

Look for `(.venv)` in your terminal prompt.

Then run:

```bash
python -m pip --version
```

The path should contain `.venv`.

### Step 3: Check the current folder

=== "Windows"

    ```cmd
    cd
    dir
    ```

=== "macOS/Linux"

    ```bash
    pwd
    ls
    ```

You should be in the project root, where folders such as `data/`, `scripts/`, and `output/` live.

### Step 4: Check whether the script exists

=== "Windows"

    ```cmd
    dir scripts
    ```

=== "macOS/Linux"

    ```bash
    ls scripts
    ```

If the file is not listed, the command cannot run it.

### Step 5: Check whether a package is installed

For pandas:

```bash
python -c "import pandas; print(pandas.__version__)"
```

For CLASSLA:

```bash
python -c "import classla; print('CLASSLA import OK')"
```

If the import fails, install the package inside the active environment:

```bash
python -m pip install pandas
```

or:

```bash
python -m pip install classla
```

### Step 6: Use a diagnostic script

Create:

```text
scripts/check_environment.py
```

Add:

```python
import sys
from pathlib import Path

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Current folder:", Path.cwd())
```

Run:

```bash
python scripts/check_environment.py
```

This tells you which Python is running and from where.

### Step 7: Recreate the environment if necessary

If the environment is confused, delete `.venv/` and recreate it.

=== "Windows PowerShell"

    ```powershell
    deactivate
    Remove-Item -Recurse -Force .venv
    py -3.12 -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip setuptools wheel
    python -m pip install -r requirements.txt
    ```

=== "macOS/Linux"

    ```bash
    deactivate
    rm -rf .venv
    python3.12 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip setuptools wheel
    python -m pip install -r requirements.txt
    ```

## Output

A clearer diagnosis: wrong Python, inactive environment, missing package, wrong folder, missing script, or a real code error.

## Check yourself

- Does `python --version` show 3.12?
- Does `python -m pip --version` point inside `.venv/`?
- Are you running the command from the project root?
- Does the script exist at the path you typed?
- Did you copy the full error message, not just the final line?

## Common traps

- Searching the internet for the last error line while ignoring earlier, more useful lines in the traceback.
- Installing a package with one Python and running code with another.
- Creating several `.venv/` folders and activating the wrong one.
- Assuming the problem is CLASSLA when the actual problem is the environment.
- Running a script from inside `scripts/` and then wondering why `data/` cannot be found.

## Practice task

Intentionally deactivate your environment and try to import `pandas`:

```bash
deactivate
python -c "import pandas"
```

Then activate the environment and try again. Explain the difference.

## Useful extension

Keep this quick checklist in your README:

```text
1. Activate .venv
2. Check python --version
3. Check python -m pip --version
4. Run from project root
5. Copy the full error message
```

## Common errors and fixes

| Error or symptom | Likely cause | First fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'pandas'` | Package not installed in active environment | `python -m pip install pandas` |
| `ModuleNotFoundError: No module named 'classla'` | CLASSLA not installed in active environment | `python -m pip install classla` |
| `Python 3.13.x` appears | Wrong Python version | Recreate `.venv/` with Python 3.12 |
| `No such file or directory` | Wrong folder or wrong path | Check `pwd`/`cd` and `ls`/`dir` |
| Output goes missing | Script writes to a different folder | Print `Path.cwd()` |
| PowerShell blocks activation | Execution policy for current session | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` |
