---
title: "Technical workspace: terminal, WSL, Bash, Git, and Python"
description: "A beginner-safe route from a new computer to a documented and reproducible humanities project."
---

# Technical workspace: terminal, WSL, Bash, Git, and Python

## The research problem

How can another researcher retrace a computational transformation when your computer, operating system and package versions differ from theirs? A reproducible project needs more than a script: it needs a navigable workspace, a record of changes, and an environment that can be recreated.

This route builds those foundations with a tiny, disposable humanities project. It separates concepts from installation instructions so that you can recognize what a command changes before you run it.

## Learning outcomes

After completing the route, you should be able to:

- distinguish a terminal, shell, command line, Bash, PowerShell, WSL and a Linux distribution;
- navigate paths without confusing Windows and Linux file systems;
- describe what Git records and how Git differs from GitHub;
- create, activate and recreate a Python 3.12 virtual environment;
- record dependencies without committing `.venv/`;
- recover from ordinary mistakes and pause before destructive operations;
- produce a local technical-readiness artefact that an instructor can inspect.

## What everyone needs—and what is Windows-only

| Everyone needs | Windows students additionally need |
| --- | --- |
| A terminal running a known shell | WSL 2 with a supported Ubuntu distribution for the course Bash route |
| Bash for the shared command-line exercises | PowerShell for installing and managing WSL |
| Git, configured with an appropriate identity | A clear distinction between `PS C:\>` and `user@host:~$` commands |
| A Python 3.12 interpreter for the course-tested baseline | Awareness that `C:\Users\Name\...` and `/home/name/...` are different path systems |
| One virtual environment per project | Awareness that Windows files appear under `/mnt/c/...` in WSL |

macOS and Linux readers skip WSL installation. They still complete the Bash, Git and Python steps.

## Vocabulary before commands

| Term | Meaning in this route |
| --- | --- |
| **Terminal** | The application window that displays text and accepts input. Windows Terminal and the macOS Terminal app are examples. |
| **Shell** | The program that reads commands. Bash and PowerShell are different shells with different syntax. |
| **Command line** | The text interface where you enter a command and its arguments. It is not the name of one particular shell. |
| **Bash** | A shell common on GNU/Linux and available in Ubuntu under WSL. The shared file and pipeline exercises use Bash. |
| **PowerShell** | A Windows shell. In this route it manages WSL and demonstrates Windows-specific activation commands. |
| **WSL** | Windows Subsystem for Linux, which runs a Linux environment on supported Windows systems. |
| **Linux distribution** | A packaged Linux operating environment, such as Ubuntu. WSL is the platform; Ubuntu is the distribution installed in it. |
| **Repository** | A project directory whose history Git records in a local `.git/` directory. |
| **Remote repository** | A separately stored repository that Git can fetch from or push to. GitHub is one possible host, not Git itself. |
| **Python interpreter** | The executable that reads and runs Python code. `python`, `python3`, `python3.12` and `py -3.12` may select different interpreters. |
| **Package** | Installable software added to a Python environment, commonly with `python -m pip`. |
| **Virtual environment** | A project-specific Python interpreter context and package directory, conventionally `.venv/`. |
| **Project** | The human-readable whole: question, sources, code, environment specification, documentation, outputs and limits. |

## Installation is not daily use

Installation changes the computer: enabling WSL, installing a distribution, Git, or a Python interpreter. It may require an administrator or institutional support. Daily use happens inside a project: opening the correct shell, entering a directory, activating `.venv`, checking `git status`, running a script and deactivating the environment.

Do not repeat installation commands every time you study. Do not use `sudo`, loosen a security policy permanently, or reinstall software merely because a project command failed. Diagnose the current shell, path, permissions and active interpreter first.

## The complete route

Complete the steps in order the first time. Return directly to the relevant workflow later.

1. **Windows only:** [Install WSL and Ubuntu on Windows](../workflows/foundations/install-wsl-and-ubuntu-on-windows.md).
2. [Navigate files and directories with Bash](../workflows/foundations/navigate-files-and-directories-with-bash.md).
3. [Use pipes, redirection and grep in Bash](../workflows/foundations/use-pipes-redirection-and-grep-in-bash.md).
4. [Install and configure Git](../workflows/foundations/install-and-configure-git.md).
5. [Track a small project with Git](../workflows/foundations/track-a-small-project-with-git.md).
6. [Install Python 3.12 for NLP work](../workflows/nlp/install-python-312-for-nlp.md).
7. [Create a Python 3.12 virtual environment](../workflows/nlp/create-a-python-312-virtual-environment.md).
8. [Install Python packages with pip](../workflows/nlp/install-python-packages-with-pip.md).
9. [Run a Python script from the terminal](../workflows/nlp/run-a-python-script-from-terminal.md).
10. [Structure a small Python NLP project](../workflows/nlp/structure-a-small-python-nlp-project.md).
11. [Troubleshoot Python, venv and pip](../workflows/nlp/troubleshoot-python-venv-and-pip.md).
12. [Clone, run, change and commit a handbook project](../workflows/foundations/clone-run-change-and-commit-a-handbook-project.md).

The [Digital Slovenian Studies technical-readiness clinic](../learning-paths/digitalna-slovenistika.md#technical-readiness-clinic) turns these steps into one assessable preparation task.

## Recoverable and destructive actions

| Usually recoverable | Pause and check first |
| --- | --- |
| `cd` into the wrong directory | `rm`, which removes files without a desktop recycle bin |
| stage the wrong file with `git add` before committing | recursive removal such as `rm -r` or PowerShell `Remove-Item -Recurse` |
| make a local commit with an imperfect message | overwriting a file with `>` when it contains needed work |
| create a disposable `.venv/` that can be recreated | force pushing or rewriting shared history |
| move a sample file and move it back | running an administrative command copied from an unverified answer |

Keep backups of source material that cannot be reacquired. Git is useful history, but it is not a backup when the only repository is on one device.

## Environment specification is not `.venv/`

Never commit `.venv/`. It contains machine-specific files and absolute paths and is designed to be recreated. Commit the instructions and specifications instead:

```text
README.md
requirements.txt
.gitignore
```

A short, reviewed `requirements.txt` can name direct dependencies. `python -m pip freeze` records every installed distribution in the current environment; that snapshot can aid diagnosis, but an unreviewed raw freeze is not automatically an ideal publication lockfile.

## Boundaries that affect humanities data

- **Backups:** preserve irreplaceable scans, transcriptions and field data independently of Git.
- **Paths:** quote names containing spaces. In WSL, prefer projects under `/home/<user>/...` when using Linux tools; `/mnt/c/...` crosses into the Windows file system.
- **Permissions:** a permissions error is a diagnostic clue, not an instruction to prefix everything with `sudo`.
- **Line endings:** Windows commonly uses CRLF and Linux commonly uses LF. Avoid changing an entire corpus merely because an editor converted line endings.
- **Encoding:** keep text and scripts in UTF-8 and declare an encoding when Python reads or writes text.
- **Rights and privacy:** cloning or processing a source does not grant permission to publish it. Inspect the README, licence, data-use conditions and personal-data risks.

## Source and platform audit

All sources below were accessed **23 July 2026**.

| Platform or command family | Official source checked | Audit conclusion |
| --- | --- | --- |
| WSL installation, Ubuntu setup and file boundary | [Microsoft Learn: Install WSL](https://learn.microsoft.com/windows/wsl/install); [Set up a WSL development environment](https://learn.microsoft.com/windows/wsl/setup/environment) | `wsl --install` is the supported default route on eligible Windows 10/11 systems; new installs default to WSL 2, and `wsl --list --verbose` verifies the distribution and version. WSL installation was not repeated on the audit machine. |
| Bash syntax, pipelines, redirection, quoting, globs and history | [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) | The shared examples use Bash syntax and were run in GNU Bash 5.2.21 under WSL 2. |
| File and text utilities | [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html); [GNU Grep manual](https://www.gnu.org/software/grep/manual/grep.html) | File, counting, sorting and filtering examples were run only in a disposable directory. |
| Git installation and commands | [Git installation pages](https://git-scm.com/install/); [Pro Git](https://git-scm.com/book/en/v2) | The WSL/Linux route and all local repository exercises were tested with Git 2.43. Native Windows/macOS installers were source-audited but not executed. |
| Python 3.12 and virtual environments | [Python downloads](https://www.python.org/downloads/); [Python 3.12 `venv`](https://docs.python.org/3.12/library/venv.html) | The repository and CI use Python 3.12 as the course-tested baseline. Creation, activation, deactivation and recreation were tested with Python 3.12.3 under Ubuntu 24.04 in WSL 2. |
| Package installation | [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/) | The route uses an activated environment and `python -m pip`; it does not use `sudo pip`. Installation from a requirements file was tested in a disposable environment. |

## Readiness check

You are ready when you can explain—not merely copy—the command that:

- shows your current directory and shell;
- shows Git and Python versions;
- activates the project environment;
- installs the documented requirements;
- runs the small script;
- displays the change before you commit it.

Keep the resulting `environment-check.md`. It is evidence about one successful environment, not a claim that every platform was tested.
