---
title: "How do I use pipes, redirection and grep in Bash?"
description: "Build and inspect a small documented text pipeline with Bash."
category_id: "foundations"
category: "Foundations"
difficulty: "beginner"
time: "30–45 min"
tags: [Bash, pipes, redirection, grep, text]
---

# How do I use pipes, redirection and grep in Bash?

<div class="answer-meta" markdown>
<span>Foundations</span>
<span>beginner</span>
<span>30–45 min</span>
</div>

## What you are trying to do

You want to count and filter a tiny list of place mentions while preserving the steps that produced the result. A pipeline is a documented transformation from input to output, not magic punctuation and not an interpretation of the sources.

Run this workflow in Bash inside the disposable `~/technical-practice/` folder.

## Three streams

Most command-line programs can use:

- **standard input** (`stdin`): data read by the command;
- **standard output** (`stdout`): ordinary results;
- **standard error** (`stderr`): diagnostics and failure messages.

By default, output and errors both appear in the terminal. Bash can connect or redirect them, but you should still inspect errors rather than hide them.

## Workflow

### Step 1: Create a tiny humanities input

```bash
cd ~/technical-practice
mkdir -p pipeline-practice/texts
cd pipeline-practice
printf 'Ljubljana\nMaribor\nLjubljana\nCelje\nMaribor\nLjubljana\n' > "place mentions.txt"
cat "place mentions.txt"
```

The input is a teaching sample, not evidence about a real corpus.

### Step 2: Redirect output to a new file

```bash
grep 'Ljubljana' "place mentions.txt" > "Ljubljana mentions.txt"
cat "Ljubljana mentions.txt"
```

`>` sends standard output to a file and **replaces that file if it already exists**. Check the destination before using it with valuable work.

Append a provenance note without replacing the existing result:

```bash
printf '# filtered from place mentions.txt\n' >> "pipeline notes.txt"
```

`>>` appends. It does not make the operation correct; inspect the file for repeated accidental appends.

### Step 3: Connect commands with a pipe

```bash
grep 'Ljubljana' "place mentions.txt" | wc -l
```

`grep` writes matching lines to standard output. `|` makes that output the standard input of `wc -l`, which counts lines. Expected result:

```text
3
```

This is a description—three matching lines—not an interpretation of why Ljubljana appears.

### Step 4: Sort before counting unique values

```bash
sort "place mentions.txt" | uniq -c
```

Expected output:

```text
      1 Celje
      3 Ljubljana
      2 Maribor
```

`uniq` combines only adjacent equal lines, so `sort` is a necessary documented step here. Changing case, spelling or diacritics changes the counts; place-name resolution remains a research decision.

Save the result:

```bash
sort "place mentions.txt" | uniq -c > "place counts.txt"
cat "place counts.txt"
```

### Step 5: Quote patterns and filenames

```bash
grep -i 'ljubljana' "place mentions.txt"
grep 'Mari.*' "place mentions.txt"
```

Quote a `grep` pattern so Bash does not interpret its punctuation first. Quote a filename containing spaces so it remains one argument.

A **glob** is different: Bash expands it into matching pathnames before running the command.

```bash
cp "place mentions.txt" texts/places-1.txt
cp "place mentions.txt" texts/places-2.txt
head -n 1 texts/*.txt
```

Do not quote the entire `texts/*.txt` glob when you intend expansion. Before using a glob with a command that changes files, preview matches with `printf '%s\n' texts/*.txt`.

### Step 6: Keep errors separate when diagnosing

This deliberately refers to a missing file in the disposable folder:

```bash
cat "missing source.txt" > output.txt 2> errors.log
cat errors.log
```

`2>` redirects standard error. The failed command may still create an empty `output.txt` because Bash opens the redirection first. Check both the command’s message and its output before treating a file as a result.

## Output

- `Ljubljana mentions.txt`;
- `place counts.txt`;
- a short provenance note;
- `errors.log` demonstrating that an error is distinct from ordinary output.

## Check yourself

```bash
wc -l "place mentions.txt"
wc -l "Ljubljana mentions.txt"
cat "place counts.txt"
cat errors.log
```

Expected input count is 6 and filtered count is 3.

## Common traps

- using `>` when you meant `>>`, thereby replacing a file;
- assuming `uniq -c` groups non-adjacent values without `sort`;
- leaving a pattern unquoted and letting Bash expand it;
- quoting a glob that you intended Bash to expand;
- treating a frequency as an explanation;
- ignoring standard error because an output file exists.

## Practice task

Add two place mentions to a copy of the input. Write a four-command record that:

1. filters one place;
2. counts the matching lines;
3. produces a sorted frequency table;
4. saves outputs under new, descriptive names.

Record the input filename, exact commands and a sentence explaining what the counts do **not** establish.

## Sources checked

Accessed **23 July 2026**:

- [GNU Bash Reference Manual: pipelines and redirections](https://www.gnu.org/software/bash/manual/bash.html)
- [GNU Grep manual](https://www.gnu.org/software/grep/manual/grep.html)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)

The complete sequence was tested in a newly created disposable directory with GNU Bash 5.2.21, GNU grep and GNU coreutils on Ubuntu 24.04 under WSL 2.
