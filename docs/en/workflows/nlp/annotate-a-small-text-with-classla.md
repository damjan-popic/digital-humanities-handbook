---
title: "How do I annotate a small text with CLASSLA?"
description: "Tokenize, lemmatize, and POS-tag one UTF-8 Slovene text file with CLASSLA."
category: "NLP"
difficulty: "beginner"
time: "30–60 min"
tags: [CLASSLA, Slovene, tokenization, lemmatization, POS tagging]
---

# How do I annotate a small text with CLASSLA?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You have a short Slovene text and want to produce linguistic annotation: sentence IDs, token IDs, word forms, lemmas, and part-of-speech tags.

Start with one file before trying a whole corpus. The point is not to process a lot of text; the point is to check whether the workflow is understandable, repeatable, and inspectable.

!!! quote "One-sentence version"
    Process one plain-text file, export the annotation, inspect it manually, and only then scale up.

## You need

- Python 3.12.
- CLASSLA installed and tested.
- The Slovene CLASSLA model downloaded.
- One UTF-8 plain-text file.
- A project folder with `data/raw/`, `output/`, and `scripts/`.

## Tools

- CLASSLA for tokenization, lemmatization, and POS tagging.
- `pathlib` for input and output paths.
- Plain text as the safest first input format.
- TSV output for easy inspection.

## Workflow

### Step 1: Create one input text

Create:

```text
data/raw/sample-sl.txt
```

Add:

```text
Digitalna humanistika povezuje jezik, podatke in interpretacijo.
Majhni preizkusi preprečijo velike napake.
```

### Step 2: Create the annotation script

Create:

```text
scripts/annotate_classla_txt.py
```

Add:

```python
from pathlib import Path
import classla

input_path = Path("data/raw/sample-sl.txt")
output_path = Path("output/sample-sl.tsv")
output_path.parent.mkdir(exist_ok=True)

text = input_path.read_text(encoding="utf-8")

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp(text)

rows = ["sent_id\tword_id\ttext\tlemma\tupos"]

for sent_id, sentence in enumerate(doc.sentences, start=1):
    for word in sentence.words:
        rows.append(
            f"{sent_id}\t{word.id}\t{word.text}\t{word.lemma}\t{word.upos}"
        )

output_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"Wrote {output_path}")
```

### Step 3: Run the script

```bash
python scripts/annotate_classla_txt.py
```

### Step 4: Inspect the output

Open:

```text
output/sample-sl.tsv
```

Look at the first rows. They should contain:

- sentence ID,
- token ID,
- surface form,
- lemma,
- UPOS tag.

### Step 5: Manually check a small sample

Select 10–20 tokens and check whether:

- sentence boundaries make sense,
- punctuation is handled as expected,
- common nouns have plausible lemmas,
- verbs are not obviously wrong,
- Slovene characters are preserved.

## Output

A TSV file with sentence ID, word ID, token text, lemma, and UPOS tag.

## Check yourself

- Are sentence boundaries correct?
- Are Slovene characters preserved?
- Do common nouns and verbs have plausible lemmas?
- Did punctuation become separate tokens?
- Can you trace every output row back to the input file?

## Common traps

- Feeding PDF or Word files directly into the NLP pipeline instead of extracting clean text first.
- Assuming the first output is automatically correct.
- Forgetting that token IDs may become more complex when multi-word tokens are involved.
- Processing too much text before inspecting a small sample.
- Losing the source file name when scaling up.

## Practice task

Annotate a 5–10 sentence Slovene text. Select 20 random tokens and manually check whether their lemmas look correct.

Write a short note listing:

- three correct annotations,
- one uncertain annotation,
- one thing you would check before trusting the output.

## Useful extension

Add document metadata columns such as `doc_id`, `title`, and `source_file` before combining many annotated files.

For multiple files, continue with [How do I export CLASSLA results to CSV?](export-classla-results-to-csv.md).
