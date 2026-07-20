---
title: "How do I read and write CSV files with pandas?"
description: "Load a CSV file, inspect it, add a simple column, and save a clean output table."
category: "NLP"
difficulty: "beginner"
time: "30–45 min"
tags: [Python, pandas, CSV, data, beginner]
---

# How do I read and write CSV files with pandas?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–45 min</span>
</div>

## What you are trying to do

Many NLP and digital humanities projects start with a CSV file: document metadata, annotation labels, OCR corrections, keyword lists, entity tables, or corpus inventories.

This workflow reads a small CSV file, inspects it, adds one derived column, and writes a new file.

!!! quote "One-sentence version"
    Load the CSV, inspect the columns, change one thing, and export a new file rather than silently overwriting the original.

## You need

- Python 3.12.
- An activated virtual environment.
- `pandas` installed.
- A small CSV file.

## Tools

- [pandas](https://pandas.pydata.org/): a Python library for tabular data.
- CSV: a simple table format that can be opened in spreadsheet tools and processed by scripts.
- `Path` from `pathlib`: keeps input and output paths readable.

## Workflow

### Step 1: Install pandas if needed

```bash
python -m pip install pandas
```

### Step 2: Create a small CSV file

Create:

```text
data/documents.csv
```

Add:

```csv
id,title,year,text
001,First text,2024,"This is a short text."
002,Second text,2025,"This is another short text."
003,Messy text,,"This row has a missing year."
```

The IDs use leading zeros on purpose. This lets you see why blindly opening files in spreadsheet software can be risky.

### Step 3: Create a script

Create:

```text
scripts/read_csv.py
```

Add this code:

```python
from pathlib import Path
import pandas as pd

input_path = Path("data/documents.csv")
output_path = Path("output/documents-cleaned.csv")
output_path.parent.mkdir(exist_ok=True)

# dtype keeps the id column as text, so 001 does not become 1.
df = pd.read_csv(input_path, dtype={"id": "string"})

print("Columns:", list(df.columns))
print("Rows:", len(df))
print(df.head())

# Add simple derived columns.
df["text_length"] = df["text"].str.len()
df["has_year"] = df["year"].notna()

df.to_csv(output_path, index=False)
print(f"Wrote {output_path}")
```

### Step 4: Run the script

```bash
python scripts/read_csv.py
```

### Step 5: Inspect the output

Open:

```text
output/documents-cleaned.csv
```

Check that:

- IDs still look like `001`, `002`, `003`.
- A new `text_length` column exists.
- A new `has_year` column exists.
- The original input file is unchanged.

## Output

A cleaned or enriched CSV file with added columns.

## Check yourself

- Are all expected columns present?
- Did the number of rows stay the same?
- Are missing values visible rather than hidden?
- Did `001` stay as `001`?
- Can the output CSV be opened in a spreadsheet editor?

## Common traps

- Forgetting `index=False` and adding a useless extra column.
- Letting a spreadsheet silently change dates, IDs, or leading zeros.
- Treating a missing value as if it were a real value.
- Mixing separators such as commas, semicolons, and tabs without checking.
- Overwriting the original CSV before you know the script works.

## Practice task

Add a column called `word_count` that counts the words in the `text` column.

Hint:

```python
df["word_count"] = df["text"].str.split().str.len()
```

Export the result and check whether the counts are plausible.

## Useful extension

Create a `metadata-report.md` file that lists:

- column names,
- number of rows,
- number of missing values per column,
- suspicious rows that need manual inspection.
