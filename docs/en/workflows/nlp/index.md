# NLP

Small, reproducible workflows for text processing, linguistic annotation, named entities, embeddings, and Python-based NLP work.

## Python/NLP first steps

This path starts with the Python layer: installing the course baseline, creating a virtual environment, running a script, reading files, writing tables, and using CLASSLA on a small Slovene text. If terminals, Bash or Git are new to you, begin with the [technical workspace foundations route](../../foundations/technical-workspace.md).

Use **Python 3.12.x** as the course-tested baseline for this path. Later versions may work, but use 3.12 when reproducing the documented teaching environment unless a project records another tested version.

<div class="grid cards" markdown>

-   **1. Install and check Python 3.12**

    Start here if the terminal cannot yet run Python reliably.

    [:octicons-arrow-right-24: Install Python 3.12](install-python-312-for-nlp.md)

-   **2. Create one virtual environment per project**

    Keep packages isolated and make commands predictable.

    [:octicons-arrow-right-24: Create a venv](create-a-python-312-virtual-environment.md)

-   **3. Install packages and record them**

    Use `python -m pip`, test imports, and keep `requirements.txt` useful.

    [:octicons-arrow-right-24: Install with pip](install-python-packages-with-pip.md)

-   **4. Run scripts instead of clicking around**

    Learn the smallest repeatable script workflow.

    [:octicons-arrow-right-24: Run a script](run-a-python-script-from-terminal.md)

-   **5. Process files and tables**

    Read text files, preserve UTF-8, and export CSV files with pandas.

    [:octicons-arrow-right-24: Read text files](read-and-write-text-files-in-python.md)

-   **6. Annotate Slovene with CLASSLA**

    Install CLASSLA, test one sentence, annotate one file, then export token tables.

    [:octicons-arrow-right-24: Install CLASSLA](install-and-test-classla.md)

</div>

## Recommended order

| Step | Question | Output |
|---:|---|---|
| 1 | [How do I install Python 3.12 for NLP work?](install-python-312-for-nlp.md) | A working Python 3.12 command |
| 2 | [How do I create a Python 3.12 virtual environment?](create-a-python-312-virtual-environment.md) | A `.venv/` folder inside one project |
| 3 | [How do I install Python packages with pip?](install-python-packages-with-pip.md) | Installed packages and `requirements.txt` |
| 4 | [How do I run a Python script from the terminal?](run-a-python-script-from-terminal.md) | A script that creates an output file |
| 5 | [How do I read and write text files in Python?](read-and-write-text-files-in-python.md) | A cleaned text file |
| 6 | [How do I read and write CSV files with pandas?](read-and-write-csv-files-with-pandas.md) | A modified CSV table |
| 7 | [How do I structure a small Python NLP project?](structure-a-small-python-nlp-project.md) | A reusable folder structure |
| 8 | [How do I troubleshoot Python venv and pip problems?](troubleshoot-python-venv-and-pip.md) | A diagnosis checklist |
| 9 | [How do I use the Python/NLP starter project?](use-the-python-nlp-starter-project.md) | A ready-to-run mini project |
| 10 | [How do I install and test CLASSLA with Python 3.12?](install-and-test-classla.md) | CLASSLA installed and tested on one sentence |
| 11 | [How do I annotate a small text with CLASSLA?](annotate-a-small-text-with-classla.md) | A token/lemma/POS TSV file |
| 12 | [How do I export CLASSLA results to CSV?](export-classla-results-to-csv.md) | A token-level CSV for several texts |

## Starter code

The repository includes a small runnable starter project:

```text
examples/python-nlp-first-steps/
```

It contains sample data, scripts, and a `requirements.txt` for the Python and CLASSLA workflows above. Use it as a reference structure, not as a magic folder. Recreate the steps manually at least once before copying the whole example.

## Existing NLP workflows

| Question | Difficulty | Time | Tags |
|---|---|---|---|
| [How do I annotate a corpus with UDPipe?](annotate-a-corpus-with-udpipe.md) | intermediate | 30–60 min | UDPipe, POS tagging, lemmatization |
| [How do I compare meanings across languages with fastText embeddings?](compare-meanings-across-languages-with-fasttext-embeddings.md) | advanced | 60–120 min | fastText, embeddings, cross-lingual |
| [How do I extract named entities with spaCy?](extract-named-entities-with-spacy.md) | intermediate | 30–60 min | spaCy, NER, named entities |
