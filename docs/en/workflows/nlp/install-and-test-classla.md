---
title: "How do I install and test CLASSLA with Python 3.12?"
description: "Install CLASSLA in a Python 3.12 virtual environment and test it on one Slovene sentence."
category: "NLP"
difficulty: "beginner"
time: "30–60 min"
tags: [Python, CLASSLA, Slovene, NLP, installation]
---

# How do I install and test CLASSLA with Python 3.12?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

CLASSLA is a Python toolkit for linguistic annotation of South Slavic languages, including Slovene. This workflow installs it in a clean **Python 3.12** virtual environment and tests one sentence before doing anything ambitious.

Even if newer Python versions are available, use Python 3.12 for this handbook path. It keeps the environment consistent across machines and exercises.

!!! quote "One-sentence version"
    Use Python 3.12, install CLASSLA inside `.venv/`, download the Slovene model, and test one sentence before processing files.

## You need

- Python 3.12, not higher for this path.
- An activated Python 3.12 virtual environment.
- Internet access for installing packages and downloading models.
- Enough disk space for language models.
- Patience with first-time model downloads.

## Tools

- [CLASSLA](https://github.com/clarinsi/classla): linguistic annotation toolkit for South Slavic languages.
- `pip`: Python package installer.
- `classla.download("sl")`: downloads the Slovene model.
- `classla.Pipeline("sl")`: creates a Slovene annotation pipeline.

## Workflow

### Step 1: Create and activate a Python 3.12 virtual environment

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

### Step 2: Confirm the Python version

```bash
python -c "import sys; print(sys.version); assert sys.version_info[:2] == (3, 12)"
```

If this fails, recreate the environment with Python 3.12.

### Step 3: Upgrade packaging tools

```bash
python -m pip install --upgrade pip setuptools wheel
```

### Step 4: Install CLASSLA

```bash
python -m pip install classla
```

Check that the package is installed:

```bash
python -m pip show classla
python -c "import classla; print('CLASSLA import OK')"
```

### Step 5: Download the Slovene model

```bash
python -c "import classla; classla.download('sl')"
```

This can take time. The model is downloaded to a local cache. Do not commit model files to Git.

### Step 6: Create a test script

Create:

```text
scripts/test_classla.py
```

Add:

```python
import classla

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp("To je kratek preizkus slovenskega jezikovnega označevanja.")

for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.lemma, word.upos, sep="\t")
```

### Step 7: Run the test

```bash
python scripts/test_classla.py
```

You should see one token per line, with token, lemma, and UPOS tag separated by tabs.

## Output

A working CLASSLA installation and terminal output similar to:

```text
To      to      DET
je      biti    AUX
kratek  kratek  ADJ
...
```

Exact tags and lemmas may differ depending on the installed model version.

## Check yourself

- Does `python --version` show Python 3.12 inside the environment?
- Does `python -m pip show classla` show an installed package?
- Did CLASSLA download the Slovene model successfully?
- Does the test script print one token per line?
- Are Slovene characters displayed correctly?

## Common traps

- Using Python 3.13 or higher when the exercise expects 3.12.
- Forgetting to activate the virtual environment before installing CLASSLA.
- Downloading a model once and assuming it is included in Git.
- Starting with a large corpus before testing one sentence.
- Confusing package installation with model download. You need both.

## Practice task

Change the test sentence, rerun the script, and identify the lemma and POS tag of three Slovene words.

Then add `classla` to your `requirements.txt`:

```text
classla
```

## Useful extension

After the test works, save the full installed package list:

```bash
python -m pip freeze > requirements.txt
```

For a teaching or starter project, a shorter hand-written file may be clearer:

```text
classla
pandas
```

## Further reading or useful links

- [CLASSLA GitHub repository](https://github.com/clarinsi/classla)
- [CLASSLA on PyPI](https://pypi.org/project/classla/)
- [CLARIN.SI knowledge centre](https://www.clarin.si/info/k-centre/)
