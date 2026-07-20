---
title: "How do I use the Python/NLP starter project?"
description: "Run the repository's small starter project for Python, pandas, and CLASSLA workflows."
category: "NLP"
difficulty: "beginner"
time: "30–60 min"
tags: [Python, starter project, NLP, CLASSLA, pandas]
---

# How do I use the Python/NLP starter project?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

The repository includes a small starter project with sample data and runnable scripts. Use it to see how the beginner Python/NLP workflows fit together in one folder.

Do not treat the starter project as a black box. Run the scripts, inspect the files they create, and then recreate the structure in your own project.

!!! quote "One-sentence version"
    Use the starter project as a working reference for folder structure, scripts, inputs, outputs, and `requirements.txt`.

## You need

- Python 3.12.
- A terminal.
- The handbook repository downloaded or cloned.
- Internet access if you install CLASSLA and download models.

## Tools

- `examples/python-nlp-first-steps/`: the starter project folder.
- `requirements.txt`: package list for the starter project.
- Python scripts in `scripts/`.
- Sample files in `data/`.

## Workflow

### Step 1: Open the starter project

From the repository root:

```bash
cd examples/python-nlp-first-steps
```

The folder should look like this:

```text
python-nlp-first-steps/
├── data/
│   ├── documents.csv
│   └── raw/
│       ├── sample-sl.txt
│       └── texts/
├── output/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

### Step 2: Create and activate a Python 3.12 environment

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

=== "macOS/Linux"

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### Step 4: Run the simplest scripts first

```bash
python scripts/hello.py
python scripts/clean_text.py
python scripts/read_csv.py
```

Inspect the files created in:

```text
output/
```

### Step 5: Run CLASSLA scripts only after installation works

First download the Slovene model:

```bash
python -c "import classla; classla.download('sl')"
```

Then run:

```bash
python scripts/test_classla.py
python scripts/annotate_classla_txt.py
python scripts/classla_folder_to_csv.py
```

### Step 6: Inspect the outputs

Expected output files include:

```text
output/hello.txt
output/sample-cleaned.txt
output/documents-cleaned.csv
output/sample-sl.tsv
output/classla-tokens.csv
```

## Output

A fully runnable miniature Python/NLP project that demonstrates environment setup, text handling, CSV handling, and basic CLASSLA annotation.

## Check yourself

- Does `python --version` show Python 3.12 inside `.venv/`?
- Did the non-CLASSLA scripts run before the CLASSLA scripts?
- Did each script create an output file?
- Can you explain which input file each script reads?
- Can you delete `output/` files and recreate them by rerunning scripts?

## Common traps

- Running scripts from the wrong folder.
- Installing dependencies outside `.venv/`.
- Running CLASSLA scripts before downloading the Slovene model.
- Treating the starter project as finished analysis rather than a learning scaffold.
- Copying the whole project without changing the README, data description, or output names.

## Practice task

Add a new file to:

```text
data/raw/texts/
```

Run:

```bash
python scripts/classla_folder_to_csv.py
```

Then open `output/classla-tokens.csv` and check whether your new file appears in the `source_file` column.

## Further reading or useful links

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [CLASSLA repository](https://github.com/clarinsi/classla)
