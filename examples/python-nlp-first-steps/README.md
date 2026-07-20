# Python/NLP first steps

A small runnable starter project for the Python and CLASSLA workflows in the Digital Humanities Handbook.

Use **Python 3.12**.

## Install

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

macOS/Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

## Run

Start with the non-CLASSLA scripts:

```bash
python scripts/hello.py
python scripts/clean_text.py
python scripts/read_csv.py
```

Then download the Slovene CLASSLA model:

```bash
python -c "import classla; classla.download('sl')"
```

Run the CLASSLA scripts:

```bash
python scripts/test_classla.py
python scripts/annotate_classla_txt.py
python scripts/classla_folder_to_csv.py
```

## Outputs

Generated files appear in `output/`.

The project is intentionally small. It is meant to be inspected, changed, broken, fixed, and reused.
