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

You want a Python installation that can be used safely for small NLP projects. For this handbook path, use **Python 3.12.x** as the course-tested baseline.

This is a reproducibility choice, not a claim that later Python versions are inherently unusable. Other versions may work, but the repository and teaching checks target 3.12. Python 3.12 is now in its security-fixes-only phase; instructors should review the baseline each semester rather than leaving it fixed indefinitely.

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
- `py -3.12`: selects Python 3.12 through the Windows Python install manager or legacy launcher.
- `python3.12`: explicitly selects Python 3.12 on the supported macOS/Linux routes.
- `python3`: commonly selects a distribution's default Python 3, which is not always 3.12.
- `python`: may select another interpreter outside an environment; after activation it should select `.venv`'s interpreter.

## Workflow

### Step 1: Install Python 3.12

Choose one option for your operating system.

=== "Windows"

    1. Obtain the current [Python install manager](https://www.python.org/downloads/) from Python.org or the Microsoft Store, following the [official Windows guide](https://docs.python.org/3/using/windows.html).
    2. Open a new PowerShell window and inspect the available 3.12 runtime:

        ```powershell
        py list --online 3.12
        ```

    3. Install the selected 3.12 runtime:

        ```powershell
        py install 3.12
        ```

    4. The older signed Python 3.12.10 installer remains available from the [official 3.12.10 release page](https://www.python.org/downloads/release/python-31210/) for managed contexts that do not yet use the install manager. Ask institutional IT which route it supports.

=== "macOS"

    Use the signed universal2 installer from the official [Python 3.12.10 release page](https://www.python.org/downloads/release/python-31210/), the last 3.12 release with binary installers. Later 3.12 security releases are source-only. Open a new Terminal window after installation.

    If your institution already manages Python through Homebrew, its platform-specific alternative is:

    ```bash
    brew install python@3.12
    ```

    Record which provider you used; do not install a second package manager simply to follow this page.

=== "Linux"

    Use your distribution package manager if it provides a maintained Python 3.12 package. Ubuntu 24.04—the repository-tested WSL environment—provides Python 3.12:

    ```bash
    sudo apt update
    sudo apt install python3.12 python3.12-venv
    ```

    These are explicit operating-system installation commands for an Ubuntu environment you administer, not a universal permissions fix. There is no `python3.12-pip` package in the tested Ubuntu 24.04 repositories; `python3.12-venv` bootstraps pip inside each new environment. Package names and available versions differ on other distributions, so use their official package documentation or ask institutional IT.

### Step 2: Check the version

=== "Windows"

    ```powershell
    py -3.12 --version
    py list
    ```

    The first command should print something like:

    ```text
    Python 3.12.x
    ```

    The second command lists runtimes known to the current Windows Python manager. Older launchers also accept `py -0p`.

=== "macOS/Linux/WSL"

    ```bash
    python3.12 --version
    which python3.12
    ```

    The version should start with:

    ```text
    Python 3.12
    ```

### Step 3: Create a project folder

=== "Windows PowerShell"

    ```powershell
    New-Item -ItemType Directory -Name nlp-first-steps
    Set-Location nlp-first-steps
    ```

=== "Bash (macOS/Linux/WSL)"

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

- Treating the course-tested 3.12 baseline as proof that every later release is unusable.
- Installing packages globally before creating a virtual environment.
- Having several Python versions installed and not knowing which one the terminal is using.
- Copying Windows commands into macOS/Linux, or macOS/Linux commands into PowerShell.
- Forgetting to open a new terminal after installation.
- Using `sudo` or a global pip install to work around an environment problem.

## Practice task

Create a folder called `nlp-first-steps`, open a terminal inside it, and write down the exact command that shows Python 3.12 on your machine.

Then create a file called `README.md` and record the version:

```markdown
# NLP first steps

Python version used: 3.12.x
Python command on this computer: py -3.12
```

Change the command if you are on macOS or Linux.

## Sources checked

Accessed **23 July 2026**:

- [Python downloads and active release status](https://www.python.org/downloads/)
- [Python 3.12.10 release and signed installers](https://www.python.org/downloads/release/python-31210/)
- [Using Python on Windows](https://docs.python.org/3/using/windows.html)
- [Using Python on a Mac](https://docs.python.org/3.12/using/mac.html)
- [Python 3.12 `venv` documentation](https://docs.python.org/3.12/library/venv.html)

The Linux/WSL route was tested with Ubuntu 24.04.4 LTS and its maintained Python 3.12.3 package. Native Windows and macOS installation routes were checked against the official sources but not executed on the WSL audit host.
