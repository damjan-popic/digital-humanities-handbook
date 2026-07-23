---
title: "How do I install and configure Git?"
description: "Install Git through an official platform route and configure an intentional commit identity."
category_id: "foundations"
category: "Foundations"
difficulty: "beginner"
time: "20–40 min"
tags: [Git, version control, identity, setup]
---

# How do I install and configure Git?

<div class="answer-meta" markdown>
<span>Foundations</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

A research project needs a traceable record of who made a change and when. You will install Git in the environment where you work, verify it, and configure the name and email written into future commits.

Git records local history. GitHub is a separate hosting service; no GitHub account or public repository is required here.

## You need

- permission to install software, or institutional support;
- the shell in which you will do project work;
- a name and an email policy appropriate for academic work.

If you use WSL for the course, install and configure Git **inside Ubuntu**, even if Git for Windows also exists. They are separate installations with separate configuration files.

## Workflow

### Step 1: Check before installing

Run in your project shell:

```bash
git --version
```

If this prints a version, continue to configuration. Do not reinstall merely to match a screenshot.

### Step 2: Choose the route for your platform

=== "Ubuntu / WSL"

    Run these only if `git --version` reports that Git is absent and you administer this Ubuntu environment:

    ```bash
    sudo apt update
    sudo apt install git
    ```

    These are operating-system installation commands. `sudo` grants administrative authority for this explicit package operation; it is not a remedy for later Git permission errors. On a managed device without permission, ask IT to install the distribution package.

=== "Windows (native)"

    Use the maintained **Git for Windows** installer linked from the official Git site, or the official page’s current WinGet route.

    **PowerShell:**

    ```powershell
    winget install --id Git.Git -e --source winget
    ```

    Open a new terminal after installation. This native route is separate from Git inside WSL.

=== "macOS"

    The official Git installation page lists Apple’s Command Line Tools:

    ```bash
    xcode-select --install
    ```

    It also lists Homebrew, if your institution already supports it:

    ```bash
    brew install git
    ```

    Do not install a second package manager only to avoid an institutional software request.

### Step 3: Verify the installation

Open a new shell and run:

```bash
git --version
```

Record the exact output. Projects generally do not require every student to have the same Git patch version.

### Step 4: Configure commit identity

Replace the examples with the identity you intend to publish in commit metadata:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.edu"
git config --global init.defaultBranch main
```

`--global` writes user-level configuration for repositories used by this operating-system account. It does not create an online profile.

Every commit records the configured name and email. If a repository will become public, decide whether your institutional address, another professional address, or a hosting service’s privacy address is appropriate. Do not invent another person’s identity. Ask the instructor when assessment and publication identities differ.

### Step 5: Inspect values and their origins

```bash
git config --list --show-origin
git config user.name
git config user.email
git config init.defaultBranch
```

`--show-origin` reveals which configuration file supplied a value. This matters when system, user and repository settings differ.

### Step 6: Use a repository-local override when justified

Inside an existing repository, omitting `--global` writes the repository-local value:

```bash
git config user.email "course-address@example.edu"
git config --show-origin user.email
```

Local `.git/config` values override global values for that repository. Use an actual approved address, then explain the override in the project documentation when identity is methodologically or institutionally consequential.

## Output

- a working `git` command;
- an intentional commit name and email;
- `main` as the initial branch for new repositories;
- an inspectable record of where configuration values originate.

## Check yourself

```bash
git --version
git config --list --show-origin
```

Read the output. Do not paste access tokens, credential-helper secrets or unrelated private paths into a public report.

## Common traps

- configuring Git for Windows while doing all work in WSL Ubuntu;
- copying a placeholder name or email literally;
- using `sudo git ...` inside a project and creating root-owned files;
- assuming a Git identity is authenticated proof of authorship;
- exposing a private email in a repository that will be public;
- changing system-wide configuration when a global or local setting is enough.

## Practice task

Record in `environment-check.md`:

```text
Git version:
Git executable environment: WSL Ubuntu / native Windows / macOS / Linux
Commit name checked:
Commit email privacy checked: yes
Default initial branch: main
```

Do not copy the email itself into a document that will be published unless that is intentional.

## Sources checked

Accessed **23 July 2026**:

- [Git: Install](https://git-scm.com/install/)
- [Git for Windows](https://git-scm.com/install/windows)
- [Git for macOS](https://git-scm.com/install/mac)
- [Git for Linux](https://git-scm.com/install/linux)
- [Pro Git: First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

The Ubuntu verification and configuration commands were tested with Git 2.43 in a disposable user configuration and repository. Native Windows and macOS installation routes were checked against the official pages but were not executed on the WSL audit host.
