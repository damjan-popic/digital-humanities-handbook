---
title: "How do I clone, run, change and commit a handbook project?"
description: "Integrate Git and Python in one small instructor-provided readiness repository."
category_id: "foundations"
category: "Foundations"
difficulty: "beginner"
time: "45–75 min"
tags: [Git, Python, venv, clone, readiness]
---

# How do I clone, run, change and commit a handbook project?

<div class="answer-meta" markdown>
<span>Foundations</span>
<span>beginner</span>
<span>45–75 min</span>
</div>

## What you are trying to do

You want to prove that a small humanities computation can move from a documented repository to a successful local run and an inspectable change. This workflow combines skills; it does not introduce public contribution.

Use the small starter-repository URL or institutional path supplied by your instructor. A public GitHub repository is not required, and you should stop before opening a pull request unless the instructor explicitly asks for one.

## Starter contract

The supplied repository should contain at least:

```text
technical-readiness/
├── README.md
├── environment-check.md
├── hello.py
├── requirements.txt
└── output/
```

It should also state its licence in `LICENSE` or clearly in `README.md`, and ignore `.venv/`. The script should contain one harmless label that the README invites you to change.

## Workflow

### Step 1: Clone rather than initialize

Replace the entire placeholder with the instructor-provided HTTPS URL or approved local path.

**Bash:**

```bash
cd ~/projects
git clone "<starter-repository-url>" technical-readiness
cd technical-readiness
```

**PowerShell (native Windows project):**

```powershell
Set-Location "$HOME\Projects"
git clone "<starter-repository-url>" technical-readiness
Set-Location technical-readiness
```

Do not run `git init` inside the clone. `git clone` has already created the local repository and recorded its source as a remote.

### Step 2: Inspect before executing

```bash
git status
git remote -v
ls -la
less README.md
```

Inspect the licence file named by the README, for example:

```bash
less LICENSE
```

Press `q` to leave `less`. A licence describes permissions and conditions; it does not override privacy, data-protection, consent or third-party rights.

Read `hello.py` and `requirements.txt` before running them:

```bash
cat hello.py
cat requirements.txt
```

If the repository or dependency source is unexpected, stop and ask the instructor.

### Step 3: Confirm `.venv/` is ignored

```bash
git check-ignore -v .venv/
```

If this does not identify an ignore rule, add `.venv/` to `.gitignore` and inspect the change before proceeding. Never commit `.venv/`.

### Step 4: Create the course-tested environment

=== "Bash (WSL/macOS/Linux)"

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows PowerShell"

    ```powershell
    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

If PowerShell blocks the activation script, follow the current-session diagnostic in the [virtual-environment workflow](../nlp/create-a-python-312-virtual-environment.md). Do not permanently disable execution-policy protections.

### Step 5: Verify and install the declared requirements

```bash
python --version
python -m pip --version
python -m pip install -r requirements.txt
```

The Python version should start with `3.12`, and the pip path should be inside `.venv`. Package installation uses network access and executes installation tooling; use only the reviewed course file.

### Step 6: Run the unchanged script

```bash
python hello.py
```

Inspect the documented output:

```bash
ls -la output
```

Record the successful command and output location in `environment-check.md`.

### Step 7: Branch and change one harmless value

```bash
git switch -c readiness-practice
git status
```

Open `hello.py` in a plain-text editor. Change only the label identified by the README—for example, a project label from `technical readiness` to a short course label. Do not change source data, paths, package versions or licence text.

Run and inspect:

```bash
python hello.py
git diff -- hello.py
git status
```

The diff should contain only the intended label change.

### Step 8: Complete the environment record

In `environment-check.md`, record:

```text
Operating system:
Shell:
Git version:
Python version:
Activation command:
Successful script command:
Output checked:
```

Do not record usernames, tokens, passwords or sensitive absolute paths. Inspect the change:

```bash
git diff -- environment-check.md
```

### Step 9: Stage and commit locally

```bash
git add hello.py environment-check.md
git diff --staged
git commit -m "Complete the technical-readiness run"
git status
git log --oneline --decorate --max-count=3
```

If `.venv/` appears in `git status` as staged or tracked, stop and correct `.gitignore` before committing.

### Step 10: Stop before public contribution

Do **not** run `git push`, create a public fork, or open a pull request unless the instructor has explicitly defined that next activity and its privacy/licensing conditions. The readiness assessment can be inspected locally or submitted through the institution’s approved system.

Deactivate the environment:

```bash
deactivate
```

## Output

- the required `technical-readiness/` artefact;
- a recreated `.venv/` excluded from Git;
- one successful script output;
- one branch and local commit containing only the harmless label and environment record.

## Check yourself

```bash
git status
git log --oneline --decorate --all
git ls-files .venv
```

`git ls-files .venv` should print nothing.

## Common traps

| Symptom | Safe next step |
| --- | --- |
| Clone requests credentials unexpectedly | Check the exact instructor URL; do not paste a token into chat or shell history. |
| README or licence is absent | Stop and ask for a complete starter; do not infer reuse permission. |
| Python is not 3.12 | Deactivate and recreate `.venv/` with the platform-specific 3.12 command. |
| Package installation fails | Preserve the full error, Python/pip versions and platform; do not use `sudo pip`. |
| Script writes outside `output/` | Stop, inspect the code and report the mismatch before rerunning. |
| Diff contains many files or line-ending changes | Do not stage; check editor encoding and line-ending settings. |

## Sources checked

Accessed **23 July 2026**:

- [Pro Git: Getting a Git Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
- [Python 3.12 `venv` documentation](https://docs.python.org/3.12/library/venv.html)
- [Python Packaging User Guide: Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)

The integrated clone, branch, virtual-environment, install, run and commit sequence was tested with a disposable local starter and bare remote under Ubuntu 24.04/WSL 2. The instructor URL, native Windows activation and native macOS environment remain platform/course-specific and were not executed on that host.
