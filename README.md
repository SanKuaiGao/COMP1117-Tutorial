# COMP1117 Tutorial

In-class demo and practice material for **COMP1117** (HKU).

This repository is also the **template** for the Tutorial 5 GitHub exercise: you
fork it, clone your own copy, add a file on a feature branch, and merge that
branch back with a Pull Request.

> **Tutorial 5 practice line.** This sentence exists so that you have a safe
> place to practise a merge conflict. Edit it on `main`, edit it differently on
> your feature branch, then merge the two. Change nothing else about it.

## Contents

| Folder | Session | Topic |
| --- | --- | --- |
| [`debugging/`](debugging/README.md) | Tutorial 3 | Read error messages, inspect values, use the VS Code debugger |
| [`branching&merging/`](branching&merging/README.md) | Tutorial 5 | Fork, branch, commit, Pull Request, merge conflict |
| [`functions/`](functions/README.md) | Tutorial 9 | Coding practice: parameters, return values, testing |

Sessions are listed in teaching order. Each folder has its own README with the
workflow, the tasks and the expected results.

## Quick start

### 1. Fork this repository (once)

1. Open <https://github.com/gracezhou7/COMP1117-Tutorial>.
2. Click **Fork** (top right), choose **your own account** as the owner, keep
   *Copy the main branch only* selected, then click **Create fork**.
3. You now have your own copy at `github.com/<your-username>/COMP1117-Tutorial`.

Forking is needed because you do **not** have write access to this repository.

### 2. Clone your fork in VS Code

1. On your fork's page, click the green **Code** button and copy the HTTPS URL.
2. In VS Code: **Explorer → Clone Repository** (or the Welcome tab).
3. Paste the URL, choose a folder on your computer, and click **Open**.

Terminal alternative:

```bash
git clone https://github.com/<your-username>/COMP1117-Tutorial.git
```

### 3. Create a branch before you type anything

Click the current branch name (`main`) in the bottom-left status bar →
**+ Create new branch...** → `feature-add-greeting`.

```bash
git switch -c feature-add-greeting
```

### 4. Add your greeting

Create `branching&merging/greetings/<YourName>.txt` containing one or two lines
about yourself. For the greeting task, do **not** edit the root `README.md` or
another student's file — many branches editing one shared file is exactly what
the merge-conflict exercise is about.

### 5. Commit and publish

Open the **Source Control** panel, click **+** next to each changed file, type a
short message such as `Add greeting for <name>`, click **Commit**, then
**Publish Branch**.

### 6. Open and merge a Pull Request

On GitHub: **Compare & pull request** → write a title and a one-line summary →
**Create pull request** → **Merge pull request** → **Confirm merge**.

The full walkthrough, including the conflict exercise and troubleshooting, is in
[`branching&merging/README.md`](branching&merging/README.md).

## Running the Python code

Python 3 only, standard library only — there is nothing to install.

```bash
cd debugging
python3 demo/hello.py            # works
python3 demo/marks.py            # runs, but the average is wrong
python3 demo/marks_print.py      # the same bug, diagnosed with print()
```

On Windows, use `python` (or `py`) instead of `python3`. In VS Code you can also
open any file and use **Run Python File**.

| I want to… | Open |
| --- | --- |
| check that Python works | [`debugging/demo/hello.py`](debugging/demo/hello.py) |
| see a SyntaxError | [`debugging/demo/hello_syntax.py`](debugging/demo/hello_syntax.py) |
| see a TypeError caused by `input()` | [`debugging/demo/age.py`](debugging/demo/age.py) |
| see a logic error with no error message | [`debugging/demo/marks.py`](debugging/demo/marks.py) |
| practise debugging | [`debugging/practice/marks.py`](debugging/practice/marks.py) |
| practise debugging with a breakpoint | [`debugging/practice/temperature.py`](debugging/practice/temperature.py) |
| practise functions | [`functions/tutorial9.py`](functions/tutorial9.py) |

## Answers

Worked answers live in the `solutions/` folders:

- [`debugging/solutions/`](debugging/solutions/) — the repaired Task 1 and Task 2
  programs, with each bug explained.
- [`functions/solutions/tutorial9_solutions.py`](functions/solutions/tutorial9_solutions.py)
  — all seven functions plus assertions you can run.

Try the task first. Reading an answer feels easy, but it teaches very little.

## If something does not work

| You see… | Likely cause | What to do |
| --- | --- | --- |
| `python3: command not found` | Python is not on your `PATH` | On Windows try `python` or `py`; otherwise revisit the Tutorial 1 setup |
| `Permission denied (403)` when pushing | You are trying to push to a repository you do not own | Push to **your fork**, then open a Pull Request |
| `! [rejected] ... (non-fast-forward)` | GitHub has commits your laptop does not | **Sync Changes** / `git pull` first, then push |
| `<<<<<<<` markers inside a file | An unresolved merge conflict | See the conflict section of the [Tutorial 5 README](branching&merging/README.md) |
| A breakpoint never pauses | You ran the file instead of debugging it | Use **Run → Start Debugging** (`F5`) |
| The debugger asks for input but nothing happens | The program is waiting in the Terminal | Click the **Terminal** panel, type the value, press Enter |

## Asking questions

Post on the Moodle forum with the **last few lines of the error message** or a
screenshot of the terminal, plus what you expected to happen. Please do not paste
a whole program into the forum.
