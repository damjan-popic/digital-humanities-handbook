---
title: "How do I export CLASSLA results to CSV?"
description: "Turn CLASSLA annotation for several text files into a token-level CSV table."
category: "NLP"
difficulty: "intermediate"
time: "45–75 min"
tags: [CLASSLA, CSV, pandas, annotation, Slovene]
---

# How do I export CLASSLA results to CSV?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>intermediate</span>
<span>45–75 min</span>
</div>

## What you are trying to do

NLP results are easier to inspect, filter, and reuse when they are in a table.

This workflow processes several `.txt` files with CLASSLA and exports one CSV file with document ID, source file, sentence ID, token ID, token, lemma, and POS tag.

!!! quote "One-sentence version"
    Keep document provenance in the output table, otherwise annotation becomes detached from the source.

## You need

- Python 3.12.
- CLASSLA installed and tested.
- The Slovene CLASSLA model downloaded.
- `pandas` installed.
- A folder of UTF-8 plain-text files.

## Tools

- CLASSLA for annotation.
- pandas for table export.
- CSV for review in spreadsheet tools.
- `Path.glob()` for processing several `.txt` files.

## Workflow

### Step 1: Install required packages

```bash
python -m pip install classla pandas
```

### Step 2: Prepare input files

Put input files here:

```text
data/raw/texts/
```

Example:

```text
data/raw/texts/text-01.txt
data/raw/texts/text-02.txt
data/raw/texts/text-03.txt
```

Each file should be plain UTF-8 text.

### Step 3: Create the export script

Create:

```text
scripts/classla_folder_to_csv.py
```

Add:

```python
from pathlib import Path
import pandas as pd
import classla

input_dir = Path("data/raw/texts")
output_path = Path("output/classla-tokens.csv")
output_path.parent.mkdir(exist_ok=True)

if not input_dir.exists():
    raise SystemExit(f"Input folder does not exist: {input_dir}")

txt_files = sorted(input_dir.glob("*.txt"))
if not txt_files:
    raise SystemExit(f"No .txt files found in {input_dir}")

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")

rows = []

for txt_path in txt_files:
    doc_id = txt_path.stem
    text = txt_path.read_text(encoding="utf-8")
    doc = nlp(text)

    for sent_id, sentence in enumerate(doc.sentences, start=1):
        for word in sentence.words:
            rows.append(
                {
                    "doc_id": doc_id,
                    "source_file": txt_path.name,
                    "sent_id": sent_id,
                    "word_id": word.id,
                    "text": word.text,
                    "lemma": word.lemma,
                    "upos": word.upos,
                }
            )

df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)

print(f"Processed {len(txt_files)} files")
print(f"Wrote {len(df)} tokens to {output_path}")
```

### Step 4: Run the script

```bash
python scripts/classla_folder_to_csv.py
```

### Step 5: Open and inspect the CSV

Open:

```text
output/classla-tokens.csv
```

Check that each row has:

- `doc_id`,
- `source_file`,
- `sent_id`,
- `word_id`,
- `text`,
- `lemma`,
- `upos`.

### Step 6: Create a quick lemma frequency table

Optional script fragment:

```python
lemma_counts = (
    df.groupby(["lemma", "upos"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)
lemma_counts.to_csv("output/lemma-counts.csv", index=False)
```

Function words will probably dominate. That is not a failure; it is a reminder that frequency is not interpretation.

## Output

A CSV file where each row is one annotated token, plus optional frequency tables.

## Check yourself

- Does every row have a `doc_id` and `source_file`?
- Is the number of tokens plausible for the input texts?
- Are there empty lemmas or unexpected tags?
- Can you filter by `upos` in a spreadsheet?
- Can you trace a token back to the original file?

## Common traps

- Losing document identity by exporting only token and lemma.
- Mixing texts from different languages without a language column.
- Treating token-level output as if it were already analysis.
- Opening CSV in a spreadsheet and accidentally changing encoding, separators, IDs, or dates.
- Processing a large folder before testing on three files.

## Practice task

Process three short Slovene texts and create a frequency table of the 20 most frequent lemmas.

Then inspect the list and answer:

- Which words are content words?
- Which words are function words?
- Which items need filtering before interpretation?

## Useful extension

Add metadata by joining the token table with a separate `metadata.csv` using `doc_id`.

Example metadata table:

```csv
doc_id,title,year,source
text-01,First sample,2024,local example
text-02,Second sample,2025,local example
```
