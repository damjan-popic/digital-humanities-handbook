---
title: "How do I navigate files and directories with Bash?"
description: "Practise safe Bash navigation and file operations in a disposable humanities folder."
category_id: "foundations"
category: "Foundations"
difficulty: "beginner"
time: "30–45 min"
tags: [Bash, terminal, paths, files, WSL]
---

# How do I navigate files and directories with Bash?

<div class="answer-meta" markdown>
<span>Foundations</span>
<span>beginner</span>
<span>30–45 min</span>
</div>

## What you are trying to do

Before transforming a corpus, you must know which directory a command will read from and write to. You will create a disposable folder, move through it, inspect small UTF-8 files and practise reversible file operations.

Run every command on this page in **Bash**, not PowerShell.

## You need

- Bash on macOS, Linux, or Ubuntu under WSL;
- no irreplaceable files in the practice location;
- a terminal whose prompt resembles `student@computer:~$`.

## Workflow

### Step 1: Ask where you are

```bash
pwd
```

`pwd` prints the absolute path of the working directory. An **absolute path** starts at `/`, such as `/home/student`. A **relative path** starts from the current directory, such as `technical-practice/texts`.

### Step 2: Create one disposable teaching folder

```bash
mkdir -p ~/technical-practice/texts
cd ~/technical-practice
pwd
```

Everything below stays inside `~/technical-practice/`. Do not substitute a research-data directory while learning.

### Step 3: List visible and hidden entries

```bash
ls
ls -la
```

`ls` lists visible entries. `ls -a` also shows names beginning with `.`, which are hidden by convention. The entries `.` and `..` mean the current directory and its parent:

```bash
ls .
ls ..
```

### Step 4: Create small files

```bash
touch "reading notes.txt"
touch texts/poem.txt
printf 'jutro\nmesto\njutro\n' > texts/poem.txt
```

`touch` creates an empty file when it does not exist. The final command writes three lines to the disposable file; `>` replaces that file’s previous content. Quoting `"reading notes.txt"` keeps the space inside one filename.

### Step 5: Inspect text without editing it

```bash
cat texts/poem.txt
head -n 2 texts/poem.txt
tail -n 2 texts/poem.txt
less texts/poem.txt
```

- `cat` prints a short file;
- `head` and `tail` show the beginning and end;
- `less` lets you scroll through a longer file without changing it; press `q` to leave.

### Step 6: Copy and move reversible examples

```bash
cp texts/poem.txt "copy of poem.txt"
mv "copy of poem.txt" texts/poem-copy.txt
ls -la texts
```

`cp` leaves the source and creates a copy. `mv` relocates or renames one entry. Before either command, check whether the destination already exists: an overwrite may lose work.

### Step 7: Practise relative navigation

```bash
cd texts
pwd
cd ..
pwd
cd ./texts
cd ..
```

`..` means the parent directory; `.` means the current directory. `cd` changes the shell’s working directory but does not move files.

### Step 8: Use completion and history

Type `cd te` and press **Tab** rather than finishing the name. Bash can complete an unambiguous path. Press the **Up arrow** to recall a command, edit it, and press Enter only after rereading it.

To inspect recorded commands:

```bash
history
```

History can contain sensitive arguments. Do not put passwords or tokens directly in commands.

### Step 9: Recognize Windows and Linux paths in WSL

These names refer to different locations:

```text
Windows: C:\Users\Student\Documents\corpus
WSL:     /mnt/c/Users/Student/Documents/corpus
Linux:   /home/student/projects/corpus
```

Use Linux paths in Bash. For Linux Git and Python work, prefer `/home/student/projects/...`. Quote a mounted Windows path containing spaces:

```bash
cd "/mnt/c/Users/Student/My Documents"
```

Replace the example only if that directory really exists.

## A deliberate warning about removal

`rm` removes files without using the desktop recycle bin. It is not an “undo” command and `rm -r` can remove a directory tree. This beginner workflow does not use recursive removal.

Only after confirming that you are inside the disposable folder:

```bash
pwd
ls "reading notes.txt"
rm "reading notes.txt"
```

If `pwd` is not your `technical-practice` directory or the listed name is unexpected, stop. Keep irreplaceable material backed up.

## Output

```text
technical-practice/
└── texts/
    ├── poem-copy.txt
    └── poem.txt
```

## Check yourself

- Can you identify the absolute path printed by `pwd`?
- Can you explain `.` and `..` without calling them file names?
- Do quoted paths with spaces work?
- Can you inspect a file with `less` and leave with `q`?
- Before `cp`, `mv` or `rm`, do you know the exact source and destination?

## Common traps

- copying a PowerShell path such as `C:\...` directly into Bash;
- running from `/mnt/c/...` without realizing that you crossed the file-system boundary;
- omitting quotes around a name with spaces;
- treating hidden files as absent;
- using `rm -r` as casual cleanup instead of checking the target.

## Practice task

Inside `~/technical-practice/`, create `sources/` and `notes/`. Make one tiny UTF-8 file, copy it, rename the copy and inspect the first and last line. Record the commands in `notes/commands.txt`; do not include credentials or private source text.

## Sources checked

Accessed **23 July 2026**:

- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [Microsoft Learn: WSL file storage guidance](https://learn.microsoft.com/windows/wsl/setup/environment#file-storage)

The sequence, including the single-file `rm`, was tested in a newly created disposable directory with GNU Bash 5.2.21 and GNU coreutils on Ubuntu 24.04 under WSL 2.
