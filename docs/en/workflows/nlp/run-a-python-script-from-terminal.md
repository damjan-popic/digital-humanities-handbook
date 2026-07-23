---
title: "How do I run a Python script from the terminal?"
description: "Write and run a first Python script inside a predictable project folder."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, terminal, scripts, beginner]
---

# How do I run a Python script from the terminal?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

Many reproducible NLP workflows are scripts, not screenshots. A script is a `.py` file that can be run again with the same input, settings, and output location.

The goal here is tiny: create one script, run it from the project root, and make it write one output file.

!!! quote "One-sentence version"
    Put code in `scripts/`, run it from the project root, and make the script create its own output.

## You need

- Python 3.12.
- An activated virtual environment.
- A text editor such as VS Code, Pulsar, Sublime Text, or any plain-code editor.
- A project folder.

## Tools

- Terminal or PowerShell.
- A code editor.
- `python scripts/name.py`: the basic command for running a script from the project root.
- `pathlib`: a built-in library for predictable file paths.

## Workflow

### Step 1: Create a basic project structure

```text
nlp-first-steps/
├── data/
├── output/
└── scripts/
```

In the terminal:

=== "Windows PowerShell"

    ```powershell
    mkdir data, output, scripts
    ```

=== "macOS/Linux"

    ```bash
    mkdir -p data output scripts
    ```

### Step 2: Create the script file

Create:

```text
scripts/hello.py
```

Add this code:

```python
from pathlib import Path
import sys

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

message = "Hello from a reproducible Python script."
run_info = f"{message}\nPython: {sys.version}\n"

print(message)
(output_dir / "hello.txt").write_text(run_info, encoding="utf-8")
```

### Step 3: Run the script from the project root

Your terminal should be inside `nlp-first-steps/`, not inside `scripts/`.

```bash
python scripts/hello.py
```

### Step 4: Check the output

The script should create:

```text
output/hello.txt
```

Open the file. It should contain the message and the Python version.

### Step 5: Run it again

Delete `output/hello.txt`, then run the command again. The same output file should be recreated.

## Output

A working Python script and a generated output file.

## Check yourself

- Did you run the script from the project root?
- Did the script create `output/hello.txt`?
- Can you delete the output file and recreate it by running the script again?
- Does the output record the Python version?

## Common traps

- Running the script from the wrong folder and breaking relative paths.
- Saving the file as `hello.py.txt` by accident.
- Editing one copy of a script and running another.
- Writing output manually instead of letting the script produce it.
- Forgetting to activate `.venv` before running the script.

## Practice task

Modify the script so that it writes:

- your name or initials,
- today's date,
- the Python version,
- the current working folder.

Save the result to:

```text
output/run-info.txt
```

## Useful extension

Add this diagnostic line when you are unsure where Python is running:

```python
from pathlib import Path
print("Current folder:", Path.cwd())
```

Keep source text in UTF-8 and preserve a separate copy of irreplaceable input. A successful script run shows that instructions executed; it does not validate the interpretation or grant rights to redistribute its input or output.

## Sources checked

Accessed **23 July 2026**:

- [Python 3.12 tutorial: using the interpreter](https://docs.python.org/3.12/tutorial/interpreter.html)
- [Python 3.12 `pathlib` documentation](https://docs.python.org/3.12/library/pathlib.html)

The script and output recreation were tested from a disposable project root with Python 3.12.3 under Ubuntu 24.04/WSL 2.
