# COMP1117 Tutorial

This Repo is used for in-class demo and practice material for **COMP1117** (HKU).

Every tutorial has its own folder and its own `README.md` with the workflow, the
tasks and the expected results. This file only explains how to get the repository
and how to read those guides.

> **Tutorial 5 practice line.** Edit this line on `main` and edit it differently
> on a feature branch to create a merge conflict on purpose.

## Getting the repository

### 1. Fork it (once)

1. Click **Fork** (top right), choose **your own account** as the owner, then
   click **Create fork**.
2. You now have your own copy at
   `github.com/<your-username>/COMP1117-Tutorial`.

You fork because you do **not** have write access to this repository. All your
changes go to your own copy.

### 2. Clone your fork in VS Code

1. On **your fork's** page, click the green **Code** button and copy the HTTPS
   URL.
2. In VS Code with no folder open: **Explorer → Clone Repository** (the Welcome
   tab and the Source Control panel have the same button).
3. Paste the URL, choose a folder on your computer, and click **Open**.

Terminal alternative:

```bash
git clone https://github.com/<your-username>/COMP1117-Tutorial.git
```

### 3. Read a guide

Open the folder of your tutorial in the Explorer panel, then its `README.md`.
Read it in **Markdown preview**, not as raw text — the tables, checklists and
code blocks only line up there.

- `Ctrl+Shift+V` (Windows/Linux) or `Cmd+Shift+V` (macOS), or
- right-click the file → **Open Preview**, or
- open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run
  **Markdown: Open Preview to the Side**.

If no preview appears, open the Extensions panel and install a Markdown extension
(for example **Markdown Preview Enhanced**), then right-click the file →
**Open Preview**.

## Which guide to open

| Folder | Session | Topic |
| --- | --- | --- |
| [`debugging/`](debugging/README.md) | Tutorial 3 | Reading errors and debugging |
| [`git_basics/`](git_basics/README.md) | Tutorial 4 | Git and GitHub basics |
| [`branching&merging/`](branching&merging/README.md) | Tutorial 5 | Fork, branch and Pull Request |
| [`functions/`](functions/README.md) | Tutorial 6 | Functions practice |

The Python examples need Python 3 only; nothing else has to be installed.

