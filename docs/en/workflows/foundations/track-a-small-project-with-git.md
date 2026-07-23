---
title: "How do I track a small project with Git?"
description: "Practise the inspect, stage and commit cycle in a disposable humanities project."
category_id: "foundations"
category: "Foundations"
difficulty: "beginner"
time: "40–60 min"
tags: [Git, repository, commit, branch, reproducibility]
---

# How do I track a small project with Git?

<div class="answer-meta" markdown>
<span>Foundations</span>
<span>beginner</span>
<span>40–60 min</span>
</div>

## What you are trying to do

You want to preserve the reasoning behind changes to a small source-description project. Git will let you inspect a change, select it for the next snapshot and commit it with an explanation.

This is a local exercise. It does not require GitHub or any remote repository.

## Two distinct starting points

- `git init` starts history for an existing local project directory.
- `git clone <url>` creates a local copy of an existing repository and records its remote address.

Do not run both as interchangeable setup commands. This exercise uses `git init`; the integrated workflow later uses `git clone`.

## Vocabulary

| Term | Meaning |
| --- | --- |
| **Working tree** | The files currently visible in the project directory. |
| **Staging area** | The proposed contents of the next commit. `git add` updates it. |
| **Commit** | A saved snapshot plus metadata and a message. |
| **Branch** | A movable name for a line of commits. |
| **Remote** | A named address of another repository, often `origin`. |
| **Push** | Send local commits to a remote; this changes external state. |
| **Pull** | Fetch remote work and integrate it into the current branch. |

## Workflow

### Step 1: Create a disposable project

```bash
mkdir -p ~/technical-practice/git-practice
cd ~/technical-practice/git-practice
printf '# Place-name notes\n\nA teaching project; no research claims yet.\n' > README.md
printf '.venv/\n__pycache__/\n*.pyc\n' > .gitignore
```

The `.gitignore` file states which matching untracked files Git should normally leave out. It does not delete them and does not retroactively untrack files already committed.

### Step 2: Initialize and inspect

```bash
git init
git status
```

With `init.defaultBranch main` configured, the initial branch is `main`. If it is not, stop and inspect your configuration rather than silently following a different branch name through the course.

### Step 3: Inspect the first change

```bash
git diff
git status --short
```

New untracked files do not appear in ordinary `git diff`; `git status` names them. Read files before staging them:

```bash
cat README.md
cat .gitignore
```

### Step 4: Stage only the intended files

```bash
git add README.md .gitignore
git diff --staged
git status
```

`git add` does not mean “upload.” It copies the current file content into the staging area. A later edit to the same file will remain unstaged until you add it again.

If you staged the wrong tracked file before committing, `git restore --staged <path>` removes it from the proposed commit without deleting the working file. Read `git status` after any recovery command.

### Step 5: Commit with a reason

```bash
git commit -m "Document the place-name practice project"
git status
git log --oneline --decorate
```

A useful message explains the bounded purpose of the snapshot. It does not need to narrate every keystroke.

### Step 6: Repeat the small cycle

```bash
printf '\n## Source note\n\nThe sample list is synthetic and UTF-8 encoded.\n' >> README.md
git diff
git add README.md
git diff --staged
git commit -m "Record the source and encoding limits"
git log --oneline --decorate --max-count=3
```

The cycle is:

```text
change → inspect → stage → inspect staged content → commit → verify
```

### Step 7: Make one safe branch

```bash
git switch -c notes/source-description
printf '\nNo personal data is included.\n' >> README.md
git diff
git add README.md
git diff --staged
git commit -m "Add a privacy note"
git switch main
git merge notes/source-description
git status
```

The branch gave the change a separate name while you prepared it. The merge integrates it into `main`. This beginner exercise does not delete the branch, rewrite history or force any update.

## What remotes change

Inspecting remotes is read-only:

```bash
git remote -v
```

This local repository has no remote unless you add one. `git push` changes a remote repository; `git pull` integrates remote work locally. Do not copy either command until you know the repository, branch, permissions and collaboration rules. Force push, history rewriting and remote-branch deletion are deliberately outside this workflow.

## Output

A local repository with:

- a documented `.gitignore`;
- at least three small commits;
- a safe branch exercise integrated into `main`;
- a clean `git status`.

## Check yourself

```bash
git status
git log --oneline --decorate --all
git diff
git diff --staged
```

The final two commands should be empty when the working tree and staging area match the last commit.

## What Git does not replace

- **Backups:** one repository on one disk can still be lost.
- **Licences:** history does not grant reuse or publication rights.
- **Documentation:** commit messages do not replace a README, data dictionary or method statement.
- **Ethical review:** a traceable harmful dataset remains harmful.
- **Interpretation:** Git records changes, not the meaning of evidence.

Line-ending or encoding conversions can make a whole text file appear changed. Before committing, inspect the diff and confirm that UTF-8 content and intended line endings were preserved.

## Common traps

- using `git add .` without checking which files it selects;
- assuming untracked files appear in `git diff`;
- committing `.venv/`, credentials, private data or large derived files;
- confusing `commit` with backup or `push`;
- working on the wrong branch because `git status` was skipped;
- treating a clean Git history as proof of lawful or ethical research.

## Practice task

Add a `sources.md` file with one synthetic source description and a rights note. Use the full change → inspect → stage → inspect → commit cycle. Submit `git log --oneline --decorate --all` and explain which evidence remains outside Git.

## Sources checked

Accessed **23 July 2026**:

- [Pro Git: Getting a Git Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
- [Pro Git: Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Pro Git: Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git reference documentation](https://git-scm.com/docs)

The complete repository and branch sequence was tested with Git 2.43 in a newly created disposable directory. No remote push, force operation, history rewrite or remote deletion was performed.
