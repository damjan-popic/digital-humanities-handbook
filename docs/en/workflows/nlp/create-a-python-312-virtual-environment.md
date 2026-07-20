---
title: "How do I create a Python 3.12 virtual environment?"
description: "Create and activate a project-specific Python 3.12 virtual environment."
category: "NLP"
difficulty: "beginner"
time: "15–30 min"
tags: [Python, venv, virtual environment, setup, beginner]
---

# How do I create a Python 3.12 virtual environment?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>15–30 min</span>
</div>

## What you are trying to do

A virtual environment is a small isolated Python space for one project. It keeps package installs separate, so one project does not break another.

For this handbook path, create virtual environments with **Python 3.12**. After the environment is active, use the plain command `python`, because it will point to the Python inside `.venv/`.

!!! quote "One-sentence version"
    One project gets one `.venv/`; activate it before installing packages or running scripts.

## You need

- Python 3.12 installed.
- A terminal.
- A project folder, for example `nlp-first-steps`.
- Basic comfort copying commands carefully.

## Tools

- `venv`: Python's built-in virtual environment tool.
- `pip`: the package installer used inside the environment.
- `requirements.txt`: a simple text file listing packages a project needs.

## Workflow

### Step 1: Enter the project folder

```bash
cd nlp-first-steps
```

If the folder does not exist yet:

```bash
mkdir nlp-first-steps
cd nlp-first-steps
```

### Step 2: Create the environment with Python 3.12

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv
    ```

=== "macOS/Linux"

    ```bash
    python3.12 -m venv .venv
    ```

This creates a folder called `.venv/`. Do not edit files inside it manually.

### Step 3: Activate the environment

=== "Windows PowerShell"

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

    If PowerShell blocks activation, use this only for the current terminal session:

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    .venv\Scripts\Activate.ps1
    ```

=== "Windows Command Prompt"

    ```cmd
    .venv\Scripts\activate.bat
    ```

=== "macOS/Linux"

    ```bash
    source .venv/bin/activate
    ```

### Step 4: Check that the right Python is active

```bash
python --version
python -m pip --version
```

Expected version:

```text
Python 3.12.x
```

The `pip` path should include `.venv`.

### Step 5: Upgrade packaging tools inside the environment

```bash
python -m pip install --upgrade pip setuptools wheel
```

### Step 6: Deactivate when finished

```bash
deactivate
```

You can reactivate the same environment later. You do not need to recreate it every time.

## Output

A `.venv/` folder inside your project and an activated environment where `python --version` reports Python 3.12.

## Check yourself

- Does your prompt show something like `(.venv)`?
- Does `python --version` show Python 3.12 after activation?
- Does `python -m pip --version` point to `.venv/`?
- Can you deactivate and reactivate the same environment?

## Common traps

- Creating the environment with the wrong Python version.
- Forgetting to activate the environment before installing packages.
- Running `pip install` instead of `python -m pip install` and accidentally using the wrong pip.
- Committing `.venv/` to Git.
- Deleting or moving `.venv/` and then wondering why commands stopped working.

## Practice task

Create a virtual environment in a new folder, activate it, run `python --version`, then deactivate it.

Write down the exact commands you used for your operating system.

## Useful extension

Create a `.gitignore` file and add:

```text
.venv/
__pycache__/
*.pyc
```

This prevents local Python clutter from entering Git.
