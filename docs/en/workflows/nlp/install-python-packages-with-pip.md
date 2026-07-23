---
title: "How do I install Python packages with pip?"
description: "Install packages inside a virtual environment and record them in requirements.txt."
category: "NLP"
difficulty: "beginner"
time: "15–30 min"
tags: [Python, pip, packages, requirements, beginner]
---

# How do I install Python packages with pip?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>15–30 min</span>
</div>

## What you are trying to do

Python packages add extra functionality. For NLP work, you may need packages such as `pandas`, `classla`, `spacy`, or `matplotlib`.

Install packages inside an activated virtual environment, not globally. Use `python -m pip` so that the package installer belongs to the active Python.

!!! quote "One-sentence version"
    Activate `.venv`, install packages with `python -m pip install ...`, test imports, and record dependencies in `requirements.txt`.

## You need

- Python 3.12.
- An activated Python 3.12 virtual environment.
- Internet access.
- A terminal.
- A clear idea of which package you need.

## Tools

- `python -m pip`: the safest way to call pip from the active Python environment.
- [PyPI](https://pypi.org/): the main package index for Python packages.
- `requirements.txt`: a portable list of project dependencies.

## Workflow

### Step 1: Activate the environment

=== "Windows PowerShell"

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

=== "macOS/Linux"

    ```bash
    source .venv/bin/activate
    ```

### Step 2: Check Python and pip

```bash
python --version
python -m pip --version
```

Expected:

- Python version starts with `3.12`.
- The pip path contains `.venv`.

### Step 3: Install one small package

```bash
python -m pip install pandas
```

### Step 4: Test the package import

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

If this prints a version number, the package is installed in the active environment.

### Step 5: Create a simple requirements file

For beginner projects, prefer a short hand-written `requirements.txt`:

```text
pandas
classla
```

You can install everything from it with:

```bash
python -m pip install -r requirements.txt
```

### Step 6: Record exact installed versions when needed

For diagnosis or an exact snapshot of the current environment, you can write:

```bash
python -m pip freeze > requirements.txt
```

Use this with care. A frozen file may contain many indirect dependencies, platform-specific packages and unrelated experiments. Review it before committing. A raw freeze is evidence about one environment, not automatically an ideal cross-platform publication lockfile.

## Output

An installed package and a `requirements.txt` file that documents what the project needs.

## Check yourself

- Did you activate `.venv` before installing?
- Does `python -m pip --version` point inside `.venv/`?
- Can you import the installed package with `python -c "import package_name"`?
- Can another person see which packages the project needs?

## Common traps

- Running `pip install` with the wrong Python environment.
- Installing packages globally and then not knowing why another project broke.
- Sharing code without `requirements.txt`.
- Freezing hundreds of packages when the project only needs two or three direct dependencies.
- Installing a package but running the script in a different terminal where `.venv` is not active.

## Practice task

Create a virtual environment, install `pandas`, test the import, and create a `requirements.txt` file.

Then, only in this disposable practice project, deactivate and recreate the environment before reinstalling from the file. Follow the platform-specific creation and activation commands in the [virtual-environment workflow](create-a-python-312-virtual-environment.md), then run:

```bash
python -m pip install -r requirements.txt
```

This proves that the requirements file is useful.

## Useful extension

Add this installation section to your project `README.md`:

````markdown
## Install

Use Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
````

For Windows, replace the first two commands with:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Sources checked

Accessed **23 July 2026**:

- [Python Packaging User Guide: Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [pip documentation: Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
- [pip documentation: `pip freeze`](https://pip.pypa.io/en/stable/cli/pip_freeze/)

Package installation, import checking and installation from `requirements.txt` were tested in a disposable Python 3.12 virtual environment under Ubuntu 24.04/WSL 2. No global or `sudo pip` installation was used.
