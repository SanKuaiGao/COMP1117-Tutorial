# Tutorial 5—Advanced GitHub(Branching, forking and merging

 By the end of this session you can fork a
template repository, clone your fork, work on a feature branch, open a Pull
Request, and resolve a merge conflict.

## What you will learn

- The difference between **forking**, **cloning** and **branching**.
- How to fork a template repository on GitHub and clone it with VS Code.
- How to create, switch and publish a feature branch.
- How to open, review and merge a Pull Request (PR).
- How to resolve a merge conflict with the VS Code diff editor.

## Clone, branch, fork

| Action | Where it happens | What it does | When to use it |
| --- | --- | --- | --- |
| **Clone** | GitHub → your computer | Downloads a local copy of a remote repository | You want a working copy on your machine |
| **Branch** | Inside the same repository | Creates an isolated line of work from the current history | A new feature, a bug fix, an experiment — always |
| **Fork** | GitHub account → another GitHub account | Makes your own server-side copy of someone else's repository | You have no write access to the original, e.g. this template or an open-source project |

## Your task: add a greeting

**Goal:** a merged Pull Request that adds one file,
`branching&merging/greetings/<YourName>.txt`, containing one or two sentences
about you.

### 1. Fork the template(you should have done this before, so just ignore)

1. Open <https://github.com/gracezhou7/COMP1117-Tutorial>.
2. Click **Fork** in the top-right corner.
3. Under **Owner**, select your own account.
4. Keep **Copy the main branch only** selected.
5. Click **Create fork**.

You now have `github.com/<your-username>/COMP1117-Tutorial`.

> If you skip the fork, your push is refused with `Permission denied (403)` —
> you cannot write to the template itself.

### 2. Clone your fork in VS Code(Also ignore if you already did this)

1. On **your fork**, click the green **Code** button and copy the HTTPS URL.
2. In VS Code, with no folder open, use **Explorer → Clone Repository**
   (the Source Control panel and the Welcome tab have the same button).
3. Paste the URL into the prompt and press Enter.
4. Choose a local folder, then click **Open** when VS Code offers it.

Check that you cloned **your** fork, not the template: the status bar at the
bottom left should show `main`, and the Source Control panel should show no
pending changes.

### 3. Create a feature branch

1. Click the current branch name (`main`) in the bottom-left status bar.
2. Choose **+ Create new branch...** from the Command Palette.
3. Type a descriptive name and press Enter: `feature-add-greeting`.

Branch names describe the job, not the author:

| Good | Less useful |
| --- | --- |
| `feature-add-greeting` | `test` |
| `bugfix/fix-average-formula` | `mybranch2` |
| `docs/update-readme` | `new` |

Recommended prefixes: `feature/`, `bugfix/`, `docs/`.

### 4. Add your file

In the Explorer panel, create `greetings/YourName.txt` inside this folder and
write one or two lines about yourself. Keep the name recognisable, for example
`ChanTaiMan.txt`.

From the terminal:

```bash
git switch -c feature-add-greeting   # if you have not created the branch yet
echo "Hi, my name is ... and I am a year 1 student studying ..." > "greetings/YourName.txt"
```

Your change stays on the branch. `main` in your fork is untouched until the PR
is merged.

### 5. Stage, commit, publish

1. Open the **Source Control** panel (`Ctrl+Shift+G` / `Cmd+Shift+G`).
2. Click **+** next to your new file to stage it.
3. Type a meaningful message, for example `Add greeting for <name>`.
   (You may use Copilot or another AI tool to draft the message — read it and
   make sure it is accurate before you commit. You are responsible for it!)
4. Click **Commit**.
5. Click **Publish Branch** to upload the branch to GitHub.

Refresh your fork on GitHub: the branch now appears in the branch dropdown.

### 6. Open and merge the Pull Request

1. On your fork's page, click the **Compare & pull request** banner.
2. Check that the arrow points **from your fork's branch into the template's
   `main`** (base repository: `gracezhou7/COMP1117-Tutorial`).
3. Write a title and a short summary of what you changed.
4. Click **Create pull request**, then **Merge pull request → Confirm merge**.
5. Optional but good practice: click **Delete branch** afterwards.

### Done when…

- [ ] Your branch exists on GitHub.
- [ ] The PR is merged into `main`.
- [ ] `branching&merging/greetings/` contains your file.
- [ ] Your local `main` is up to date (switch to `main`, then **Sync Changes**).

## Merge conflict exercise

A conflict happens when two branches change **the same lines of the same file**
in different ways. Git cannot guess which version you want, so it stops and asks.

1. On `main`, edit the *Tutorial 5 practice line* at the top of the root
   `README.md` — for example append `(edited on main)` — then commit and push.
2. Switch back to your feature branch and edit the **same line** differently,
   for example append `(edited on my branch)`, then commit.
3. Switch to `main` and merge the branch: **… menu → Branch → Merge…**, or
   `git merge feature-add-greeting`.
4. VS Code reports the file under **Merge Changes** in the Source Control panel.
   Open it and you will see the markers:

   ```text
   <<<<<<< Current Change (main)
   ...your version...
   =======
   ...incoming version...
   >>>>>>> Incoming Change (feature branch)
   ```

5. Pick **Accept Current Change**, **Accept Incoming Change**, or edit the text
   yourself to keep both — then save the file.
6. Click **+** to stage `README.md`, type a message, and click **Continue**.

The markers must all be gone before you stage the file. `<<<<<<<`, `=======` and
`>>>>>>>` are never valid content to leave in a document.

## Troubleshooting

| You see… | Likely cause | How to fix |
| --- | --- | --- |
| `Permission denied (403)` when pushing | You are pushing to a repository you do not have write access to | Fork it, push to your fork, then open a PR |
| `Push rejected / non-fast-forward` | The remote branch has commits your laptop does not have | Click **Sync Changes** (or `git pull`) first, then push |
| You accidentally edited code on `main` | You forgot to switch to a feature branch first | Click `main` in the status bar → **+ Create new branch**: VS Code carries your uncommitted edits over |
| `<<<<<<<` markers inside a file | An unresolved merge conflict | Open the file, accept current or incoming, stage with **+**, commit |
| The PR shows dozens of unrelated files | You compared the wrong branches | Check the base and compare branch names at the top of the PR page |

## Good practice

- **Keep `main` clean.** Every change starts on a feature branch and arrives
  through a Pull Request.
- **Pull before you branch.** Update `main` first so your branch starts from the
  latest version.
- **Name branches for the work,** not for yourself.
- **Delete branches after merging** so the branch list stays readable.
- **Commit often, in small pieces,** with messages that explain *why*.

## Typical workflow

```text
fork (if you have no write access)
  → clone your fork in VS Code
  → pull on main
  → create and switch to feature/<name>
  → edit, stage, commit
  → publish branch
  → open a Pull Request
  → resolve any conflict
  → merge into main
  → pull on main again
```
