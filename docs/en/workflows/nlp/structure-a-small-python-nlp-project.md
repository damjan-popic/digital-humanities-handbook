---
title: "How do I structure a small Python NLP project?"
description: "Use a simple folder structure that keeps data, scripts, outputs, and environment files separate."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, project structure, reproducibility, NLP]
---

# How do I structure a small Python NLP project?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

Small projects become confusing very quickly if data, scripts, outputs, notes, screenshots, and virtual environments all live in the same folder.

This structure gives you a clean default for beginner NLP work.

!!! quote "One-sentence version"
    Separate raw data, processed data, scripts, outputs, documentation, and environment files from the beginning.

## You need

- A project folder.
- Python 3.12.
- A virtual environment.
- A text editor.

## Tools

- Clear folder names.
- `README.md` for human documentation.
- `requirements.txt` for package documentation.
- `.gitignore` for files that should not be committed.

## Workflow

### Step 1: Create the folder structure

```text
my-nlp-project/
├── data/
│   ├── raw/
│   └── processed/
├── output/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

Commands:

=== "Windows PowerShell"

    ```powershell
    mkdir my-nlp-project
    cd my-nlp-project
    mkdir data, data\raw, data\processed, output, scripts
    New-Item README.md, requirements.txt, .gitignore -ItemType File
    ```

=== "macOS/Linux"

    ```bash
    mkdir -p my-nlp-project/data/raw my-nlp-project/data/processed my-nlp-project/output my-nlp-project/scripts
    cd my-nlp-project
    touch README.md requirements.txt .gitignore
    ```

### Step 2: Put files in the right places

Use this rule:

| Folder/file | Use |
|---|---|
| `data/raw/` | Original input files. Do not edit these directly. |
| `data/processed/` | Cleaned or transformed files. |
| `scripts/` | Python scripts. |
| `output/` | Generated tables, reports, charts, logs, exports. |
| `README.md` | Human explanation of the project. |
| `requirements.txt` | Python packages needed to run the project. |
| `.gitignore` | Local files excluded from Git. |

The `.venv/` directory is deliberately absent from the diagram: create it locally and ignore it. It is a disposable interpreter environment, not the environment specification. `requirements.txt` plus the README record how to recreate it.

### Step 3: Add a basic `.gitignore`

```text
.venv/
__pycache__/
*.pyc
.DS_Store
output/*.tmp
```

Do not ignore `output/` automatically unless you are sure outputs should not be shared. Some small outputs are useful for review.

### Step 4: Add a short README

````markdown
# My NLP project

## Goal

Describe the task in one paragraph.

## Python version

Use Python 3.12.

## Install

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python scripts/name-of-script.py
```

## Data

- `data/raw/`: original files
- `data/processed/`: cleaned files
- `output/`: generated results
````

For Windows PowerShell, replace the environment commands with `py -3.12 -m venv .venv` and `.\.venv\Scripts\Activate.ps1`.

### Step 5: Add package names to `requirements.txt`

Example:

```text
pandas
classla
```

Prefer a short reviewed list of direct requirements while developing. `python -m pip freeze` can capture the complete current environment for diagnosis or a tested snapshot, but review the result before treating it as a publication dependency file.

## Output

A project folder that can be understood, shared, reviewed, and rerun.

## Check yourself

- Can another person find the raw data without asking you?
- Can another person find the script that produced a result?
- Are generated files separate from original files?
- Is `.venv/` excluded from Git?
- Does the README explain how to install and run the project?

## Common traps

- Editing raw data directly without preserving the original.
- Saving scripts as `final_final_really_final.py`.
- Putting output files into the same folder as input files.
- Forgetting to document how results were produced.
- Committing a huge `.venv/` folder or local model cache.

## Practice task

Create this structure for a tiny corpus of three texts. Add a README that explains:

- what the data is,
- which Python version to use,
- which script should be run first,
- where the output appears.

## Useful extension

Once the workflow has more than one repeated command, add a `Makefile` or a small runner script. Do not add automation before you understand the manual steps.

## Sources checked

Accessed **23 July 2026**:

- [Python 3.12 documentation: `venv`](https://docs.python.org/3.12/library/venv.html)
- [Python Packaging User Guide: Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Git documentation: `.gitignore`](https://git-scm.com/docs/gitignore)

The directory creation commands and `.gitignore` behavior were tested in disposable PowerShell and Bash folders; the Python structure was rerun with Python 3.12.3 under Ubuntu 24.04/WSL 2.
