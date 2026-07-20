---
title: "How do I read and write text files in Python?"
description: "Read UTF-8 text, apply one visible transformation, and write a new file without overwriting the original."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, text files, UTF-8, pathlib, beginner]
---

# How do I read and write text files in Python?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

Before NLP becomes models and annotation, it is mostly reading files, cleaning strings, and saving results. This workflow shows the smallest useful text-processing script.

The core rule is simple: preserve the original input and write changed text to a new output file.

!!! quote "One-sentence version"
    Read text as UTF-8, transform it in a visible way, and write a new file without destroying the original.

## You need

- Python 3.12.
- An activated virtual environment.
- A project folder with `data/`, `output/`, and `scripts/`.
- One plain-text file saved as UTF-8.

## Tools

- `pathlib`: a built-in Python library for file paths.
- `.read_text()` and `.write_text()`: simple methods for reading and writing text.
- UTF-8 encoding: the default choice for multilingual text work.

## Workflow

### Step 1: Create an input file

Create:

```text
data/sample.txt
```

Add a few lines:

```text
Digital humanities starts with small, inspectable steps.
Python can read this file.
Python can also write a changed version.
Č, Š, Ž, č, š, ž should survive the workflow.
```

### Step 2: Create a script

Create:

```text
scripts/clean_text.py
```

Add this code:

```python
from pathlib import Path

input_path = Path("data/sample.txt")
output_path = Path("output/sample-cleaned.txt")
output_path.parent.mkdir(exist_ok=True)

text = input_path.read_text(encoding="utf-8")

# A tiny visible transformation.
lines = [line.strip() for line in text.splitlines() if line.strip()]
cleaned = "\n".join(lines)

output_path.write_text(cleaned + "\n", encoding="utf-8")
print(f"Read {input_path}")
print(f"Wrote {output_path}")
```

### Step 3: Run the script

```bash
python scripts/clean_text.py
```

### Step 4: Compare input and output

Open both files:

```text
data/sample.txt
output/sample-cleaned.txt
```

The original should still exist. The output should be a cleaned copy.

### Step 5: Add one transformation at a time

For example, add lowercase conversion only after the first version works:

```python
cleaned = cleaned.lower()
```

Do not stack ten cleaning operations at once. That is how tiny scripts become haunted furniture.

## Output

A new cleaned text file. The original input file remains unchanged.

## Check yourself

- Does the script preserve the original input file?
- Does the output display Slovene characters correctly?
- Can you explain each cleaning step?
- Can you rerun the script and recreate the output?

## Common traps

- Overwriting the original file before checking the result.
- Forgetting `encoding="utf-8"` and getting broken characters.
- Thinking that lowercasing is always safe. It may destroy useful information in names and abbreviations.
- Doing too many cleaning steps at once, then not knowing which step caused an error.
- Feeding PDF or Word files directly into a script that expects plain text.

## Practice task

Create a script that reads `data/sample.txt`, counts the number of characters, words, and lines, and writes the results to:

```text
output/text-report.txt
```

The report should look roughly like:

```text
characters: 196
words: 31
lines: 4
```

## Useful extension

Save intermediate versions when you test new cleaning steps:

```text
sample-cleaned-01-stripped.txt
sample-cleaned-02-lowercase.txt
sample-cleaned-03-no-extra-spaces.txt
```
