---
title: "How do I install WSL and Ubuntu on Windows?"
description: "Install the supported WSL 2 route, create an Ubuntu user, and verify where Bash commands run."
category_id: "foundations"
category: "Foundations"
difficulty: "beginner"
time: "20–60 min plus restart"
tags: [WSL, Ubuntu, Windows, Bash, setup]
---

# How do I install WSL and Ubuntu on Windows?

<div class="answer-meta" markdown>
<span>Foundations</span>
<span>beginner</span>
<span>20–60 min plus restart</span>
</div>

## What you are trying to do

You need one shared Bash environment for a course project whose texts, scripts and checks should behave predictably. On supported Windows systems, WSL 2 runs an Ubuntu Linux distribution without requiring a preview version of Windows.

If you use macOS or Linux, skip this workflow. Continue with [navigating files and directories with Bash](navigate-files-and-directories-with-bash.md).

## You need

- Windows 11 or Windows 10 version 2004 (build 19041) or later;
- permission to enable Windows features and install software;
- an internet connection and time for a restart;
- a chosen Linux username that does not need to match your Windows account.

On an institution-managed computer, check with IT before starting. If you do not have administrator permission, ask for WSL 2 and the supported Ubuntu distribution to be installed for you. Do not work around policy by disabling security controls or downloading an unofficial image.

## Before the command: know which shell you are in

The installation command runs in an **administrator PowerShell** window:

```text
PS C:\>
```

Daily course commands later run inside **Ubuntu Bash**:

```text
student@computer:~$
```

The prompts, path syntax and commands are not interchangeable.

## Workflow

### Step 1: Open PowerShell as administrator

Open Start, search for **PowerShell** or **Windows Terminal**, right-click it and choose **Run as administrator**. This elevated window is for WSL installation, not routine project work.

### Step 2: Install the supported default WSL route

**PowerShell (administrator):**

```powershell
wsl --install
```

On an eligible computer where WSL is not yet installed, this enables the required Windows components, installs WSL, selects WSL 2 for new installations and installs Ubuntu. Restart when Windows asks.

If the command displays WSL help because WSL already exists, first inspect the supported distributions:

```powershell
wsl --list --online
```

Then install the course distribution:

```powershell
wsl --install -d Ubuntu
```

Do not add `--pre-release`, join an Insider channel, or replace the supported teaching distribution merely to get newer features.

### Step 3: Create the Linux user

After the restart, open **Ubuntu** from Start. The first launch expands the distribution and asks you to create:

1. a Linux username;
2. a Linux password.

The username and password belong to this Ubuntu distribution, not to your Windows account. Nothing appears while you type the password; this is normal. Store the password safely. The account can perform administrative work with `sudo`, but that does not make `sudo` an everyday prefix or a general solution to permission errors.

### Step 4: Verify WSL 2 from PowerShell

Close Ubuntu or open a separate ordinary PowerShell tab.

**PowerShell:**

```powershell
wsl --list --verbose
```

Expected shape:

```text
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

The distribution name may include a version. The important evidence is an Ubuntu entry with `VERSION` equal to `2`.

### Step 5: Verify the Ubuntu shell

Open Ubuntu again.

**Ubuntu Bash:**

```bash
whoami
printf '%s\n' "$SHELL"
pwd
cat /etc/os-release
```

You should see your Linux username, a Bash path such as `/bin/bash`, a home directory such as `/home/student`, and Ubuntu release information.

### Step 6: Create course work in the Linux file system

**Ubuntu Bash:**

```bash
mkdir -p ~/projects
cd ~/projects
pwd
```

Microsoft recommends storing projects in the same file system as the tools that use them. For this Bash/Python route, use `/home/<user>/projects/...`. Windows files are accessible under `/mnt/c/...`, but repeatedly running Linux package or Git operations across that boundary can be slower and makes paths, permissions and line endings harder to reason about.

## Output

- a supported Ubuntu distribution running under WSL 2;
- a non-root Linux user;
- a Bash home directory and `~/projects/` folder;
- terminal output showing the distribution, WSL version and shell.

## Check yourself

- Does `wsl --list --verbose` show Ubuntu with version 2?
- Does the Ubuntu prompt use Linux-style paths?
- Does `printf '%s\n' "$SHELL"` show Bash?
- Can you explain why `C:\Users\Name\Project` differs from `/home/name/projects/project`?

## Common traps

| Symptom | Safe next step |
| --- | --- |
| Windows reports that the command is unsupported | Record the Windows version and contact IT; use Microsoft’s documented manual route only if the institution approves it. |
| Administrator approval is unavailable | Stop and request installation. Do not bypass device management. |
| Virtualization is unavailable or blocked | Record the exact message and ask IT whether the device supports the required virtualization features. |
| Ubuntu asks for a password but shows no characters | Continue typing and press Enter; Linux password entry is deliberately invisible. |
| The distribution shows WSL version 1 | Ask the instructor or IT before changing a managed computer; record the output as evidence. |

## Practice task

Create `environment-check.md` later in the readiness project and record:

```text
Operating system: Windows … with Ubuntu … under WSL 2
Shell: /bin/bash
Project location: /home/…/projects/…
```

Do not record your password, Windows account token or other credentials.

## Sources checked

Accessed **23 July 2026**:

- [Microsoft Learn: How to install Linux on Windows with WSL](https://learn.microsoft.com/windows/wsl/install)
- [Microsoft Learn: Set up a WSL development environment](https://learn.microsoft.com/windows/wsl/setup/environment)
- [Microsoft Learn: Basic commands for WSL](https://learn.microsoft.com/windows/wsl/basic-commands)

The installation and first-user prompts are platform-specific and were source-audited, not rerun during this documentation change. Verification and Bash commands were tested on Ubuntu 24.04 under WSL 2.
