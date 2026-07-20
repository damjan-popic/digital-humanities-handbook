---
title: "How do I install Python 3.12 for NLP work?"
description: "Install and verify Python 3.12 as a stable baseline for beginner NLP workflows."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, Python 3.12, setup, NLP, beginner]
---

# How do I install Python 3.12 for NLP work?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

You want a Python installation that can be used safely for small NLP projects. For this handbook path, use **Python 3.12.x** as the standard version.

Do **not** use Python 3.13 or higher for these exercises unless a code-example page explicitly says it has been tested with that version. New Python releases are good, but NLP packages sometimes need time to catch up. The aim here is predictable teaching and reproducible work, not heroic dependency archaeology.

!!! quote "One-sentence version"
    Install Python 3.12, check that the terminal can find it, and only then create project-specific virtual environments.

## You need

- A computer where you are allowed to install software.
- A terminal:
  - Windows: PowerShell or Windows Terminal.
  - macOS: Terminal.
  - Linux: any shell terminal.
- Python **3.12.x**.
- A project folder where you can safely experiment.

## Tools

- [Python](https://www.python.org/): the programming language used in these workflows.
- `py -3.12`: Windows Python launcher command.
- `python3.12`: common macOS/Linux command for Python 3.12.
- `python --version`: checks the Python version after a virtual environment is active.

## Workflow

### Step 1: Install Python 3.12

Choose one option for your operating system.

=== "Windows"

    1. Download the Python 3.12 installer from [python.org](https://www.python.org/downloads/).
    2. Run the installer.
    3. If the installer offers **Add python.exe to PATH**, enable it.
    4. Keep the Python launcher enabled. It lets you run `py -3.12` even if several Python versions are installed.
    5. Open a **new** PowerShell window after installation.

=== "macOS"

    Use either the official installer from [python.org](https://www.python.org/downloads/) or Homebrew.

    With the official installer, open a new Terminal window after installation and check the command below.

    With Homebrew:

    ```bash
    brew install python@3.12
    ```

=== "Linux"

    Use your distribution package manager if it provides Python 3.12.

    On Ubuntu/Debian-style systems, try:

    ```bash
    sudo apt update
    sudo apt install python3.12 python3.12-venv python3.12-pip
    ```

    Package names may differ between distributions. The important part is that `python3.12` and `venv` are available.

### Step 2: Check the version

=== "Windows"

    ```powershell
    py -3.12 --version
    py -0p
    ```

    The first command should print something like:

    ```text
    Python 3.12.x
    ```

    The second command lists Python versions known to the Windows launcher.

=== "macOS/Linux"

    ```bash
    python3.12 --version
    which python3.12
    ```

    The version should start with:

    ```text
    Python 3.12
    ```

### Step 3: Create a project folder

```bash
mkdir nlp-first-steps
cd nlp-first-steps
```

This folder will later contain a virtual environment, scripts, input data, and output files.

### Step 4: Do not install NLP packages globally

At this stage, only confirm that Python 3.12 exists. Install packages later, inside a virtual environment.

## Output

A working Python 3.12 installation and a clean project folder ready for a virtual environment.

## Check yourself

- Does `py -3.12 --version` or `python3.12 --version` show Python 3.12?
- Can you open a new terminal and get the same result?
- Do you know which command starts Python 3.12 on your machine?
- Are you inside a project folder, not Downloads, Desktop, or a random system directory?

## Common traps

- Installing Python 3.13 or higher and then hitting package compatibility problems.
- Installing packages globally before creating a virtual environment.
- Having several Python versions installed and not knowing which one the terminal is using.
- Copying Windows commands into macOS/Linux, or macOS/Linux commands into PowerShell.
- Forgetting to open a new terminal after installation.

## Practice task

Create a folder called `nlp-first-steps`, open a terminal inside it, and write down the exact command that shows Python 3.12 on your machine.

Then create a file called `README.md` and record the version:

```markdown
# NLP first steps

Python version used: 3.12.x
Python command on this computer: py -3.12
```

Change the command if you are on macOS or Linux.

## Further reading or useful links

- [Python downloads](https://www.python.org/downloads/)
- [Python documentation: venv](https://docs.python.org/3/library/venv.html)
- [Packaging Python Projects: installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
