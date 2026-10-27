# Tutorial 4 — Git Basics: GitHub and version control

A first repository, from an empty folder to a file that lives on GitHub.
By the end you can create a repository, commit, publish, clone, push and pull
from VS Code.

> **Do the practice in a new folder outside this repository.**
> This repository is already a Git repository, so `git init` inside it would
> create a repository inside a repository and confuse both you and VS Code.
> Make a folder such as `Documents/my-project` and open **that** folder in VS Code.

## What you need

| You need | Check |
| --- | --- |
| A GitHub account | <https://github.com> |
| Git installed | `git --version` in a terminal |
| VS Code installed | It opens and shows the Explorer panel |

## 1. What version control is

Version control tracks how a project changes over its whole life. Instead of
keeping copies of files, it keeps **one file** plus the history of every change.

Without version control, a project folder ends up looking like this:

```text
project_final.docx
project_final2.docx
project_final_reallyfinal.docx
project_final_reallyfinal_USE_THIS_ONE.docx
```

Which one is current? What changed between them? Who changed it, and when? No
one can tell.

Version control answers those questions:

- **History preservation** — a complete log of every change.
- **Rollback** — go back to a version that worked.
- **Collaboration** — several people edit the same project without overwriting
  each other's work.
- **Tracking** — see exactly what changed, when, and by whom.

Version control is not only for code: it works for documents, notes and any
project made of files.

## 2. Git is not GitHub

| | Git | GitHub |
| --- | --- | --- |
| What it is | A program installed on your computer | A website and online service |
| Where your files live | On your machine | On GitHub's servers |
| What it does | Records changes to files | Hosts Git repositories and helps people share them |
| Works without internet? | Yes | No |

Git tracks the changes; GitHub stores the repository online so you can share it
and work in a team. You can use Git with no GitHub account, but GitHub is useless
without Git.

## 3. Five terms you must know

| Term | Meaning |
| --- | --- |
| **Repository (repo)** | A project folder that Git is tracking |
| **Commit** | A saved snapshot of your changes, with a message |
| **Clone** | A copy of a repository downloaded to your computer |
| **Pull** | Download changes from GitHub to your computer |
| **Push** | Upload your commits from your computer to GitHub |

## 4. Set up once

### 4.1 Create a GitHub account

1. Go to <https://github.com>.
2. Click **Sign up**.
3. Enter a username, an email address and a password.
4. Verify your email address.
5. Log in.

### 4.2 Install Git

1. Download Git from <https://git-scm.com> and install it with the default
   settings.
2. Open a terminal and check the installation:

   - **macOS**: press `Command + Space`, type `Terminal`, press Return.
   - **Windows**: press `Win + R`, type `cmd`, press Enter.

   ```bash
   git --version
   ```

   You should see something like `git version 2.43.0`. If you see "command not
   found", Git is not installed, or (on Windows) it was not added to `PATH` —
   reinstall and keep the "Git from the command line" option.

### 4.3 Tell Git who you are

Every commit records an author, so Git needs a name and an email. Run this
**once** on your computer:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Use the same email address as your GitHub account.

Check what Git stored:

```bash
git config --list
```

These settings apply to every repository on your computer. Without them, Git
refuses to commit and asks you to configure them first.

### 4.4 Sign in to GitHub inside VS Code

1. Click the **Accounts** icon in the bottom-left corner of VS Code.
2. Choose **Sign in with GitHub** (it may say *Sign in to GitHub* or *Sign in to
   use GitHub Copilot*).
3. Click **Continue with GitHub** and sign in.
4. A browser page may ask you to **authorize VS Code** — click **Authorize**.

You only do this once. It lets VS Code create repositories and publish them
without asking for a password every time.

## 5. Create your first repository

### 5.1 Create the project folder

1. Create a folder on your computer, for example `my-project`.
2. In VS Code: **File → Open Folder**, choose `my-project`. If VS Code offers,
   click **Trust** — in Restricted Mode it cannot run Git commands.
3. Create a new file called `README.md` in the Explorer panel.

### 5.2 Write something in it

Put this in `README.md` and save the file (`Ctrl+S` / `Cmd+S`):

```markdown
# My Project

This is my first Git project using VS Code.
```

A `README.md` is the front page of a repository: it tells a reader what the
project is. Every repository should have one.

### 5.3 Initialize the repository

1. Click the **Source Control** icon in the left sidebar (`Ctrl+Shift+G` /
   `Cmd+Shift+G`).
2. The folder is not a Git repository yet, so VS Code shows a button:
   **Initialize Repository**. Click it.

VS Code has now created a local Git repository in that folder — in other words,
a hidden `.git` folder. Note that **nothing has been uploaded anywhere yet**: the
repository is local only.

### 5.4 Make your first commit

1. Open **Source Control** again. `README.md` is listed under **Changes** with a
   `U` (untracked) next to it.
2. Hover over the file and click the **+** icon. The file moves to **Staged
   Changes**. Staging means "include this file in the next commit".
3. At the top of the panel, type a message such as `This is my initial commit`.
4. Click the **checkmark** (Commit).

You have made your first commit. A commit saves a snapshot, adds a history
entry, and stores the message that explains the change.

### 5.5 Publish the repository to GitHub

1. Click **Publish Branch** in the Source Control panel.
2. VS Code asks for a **repository name** (`my-project` is fine) and whether the
   repository is **public** or **private**:

   - **Private**: only you and the people you invite can see it.
   - **Public**: anyone can see it.

3. Confirm. VS Code creates the GitHub repository and uploads your commit.

Refresh your GitHub page: the repository, the commit and `README.md` are there.

## 6. Clone a repository

**Clone** means downloading a GitHub repository to your computer. You clone when
the project already exists on GitHub — your own repository on a second computer,
a group member's repository, or a template like this one.

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Search for **Git: Clone** and choose it.
3. Pick the repository you want — here, `my-project`.
4. Choose the folder where the copy should be saved.
5. When VS Code offers, click **Open** to work on the cloned project.

What cloning does:

- downloads the repository,
- creates a local copy,
- links the copy to GitHub, so push and pull know where to go.

What is inside the cloned folder:

| Item | What it is |
| --- | --- |
| `README.md` | The project description |
| `.git/` | The hidden folder where Git keeps the entire history |

**Never edit or delete the `.git` folder by hand.** It is the repository. If you
delete it, the files stay but the whole history, the commits and the link to
GitHub are gone.

## 7. Edit, commit, push

Now change a file and send the change to GitHub.

### 7.1 Edit a file

Open `README.md`, add a section, and save:

```markdown
## A New Section

I added this section using VS Code.
```

Open **Source Control**: `README.md` appears under **Changes** with an `M`
(modified). Click the file to see the diff — green lines are additions, red lines
are deletions.

### 7.2 Stage and commit

1. Click **+** next to the file to stage it.
2. Type a message such as `Add a new section to the README`.
3. Click the **checkmark** to commit.

What a commit does:

- saves a snapshot of your work,
- creates an entry in the history,
- records your message explaining the change.

A commit is still local. GitHub does not have it yet.

### 7.3 Push

Click **Sync Changes** in the Source Control panel (this pulls first, then
pushes). Your commit is now on GitHub.

Push:

- sends your local commits to GitHub,
- updates the online repository.

Verify: refresh the GitHub page and check that `README.md` shows your new
section. Also look at the repository's **commits** list — your message is there.

## 8. Pull

Pulling downloads the latest changes from GitHub to your computer. You need it
when:

- you changed something directly on the GitHub website,
- a teammate pushed to the repository,
- you work from more than one computer.

In VS Code: open **Source Control**, click the **…** menu, choose **Pull**. VS
Code downloads and merges the changes into your files.

Pull **before** you start editing, not after. Starting from the latest version is
what prevents most conflicts.

## 9. Good practice for beginners

- **Pull before you start** any new task, so you work on the latest version.
- **Commit often**, in small pieces, while the change is still easy to describe.
- **Write meaningful messages**: `Fix the average calculation` tells a reader
  something; `update` and `asdf` do not.
- **Keep the README accurate** — it is the first thing anyone reads.
- **Read your own diff before pushing.** Look at what you are about to publish.
- Never edit the `.git` folder, and never commit passwords or API keys.

## 10. The everyday loop

```text
open the project in VS Code
  → pull (Sync Changes)
  → edit and save files
  → stage (+)
  → write a commit message and commit
  → push (Sync Changes)
```

That loop is 90% of everyday Git use. Branches, Pull Requests and merge
conflicts come next, in [Tutorial 5](../branching&merging/README.md).

## 11. If something does not work

| Symptom | Likely cause | What to do |
| --- | --- | --- |
| No **Initialize Repository** button | The folder is already a repository, or you opened the wrong folder | Check the folder path in the Explorer title bar; look for a `.git` folder |
| VS Code says *Restricted Mode* | The folder has not been trusted | Click **Trust** and reload the window |
| `fatal: not a git repository` | You are in the wrong folder, or `.git` was deleted | `cd` into the project folder; if `.git` is gone, initialize again (history is lost) |
| `Please tell me who you are` | `user.name` / `user.email` are not set | Run the two `git config --global` commands from section 4.3 |
| Commit button does nothing | Nothing is staged | Click **+** next to the file first |
| `Authentication failed` | VS Code is signed out of GitHub | Sign in again from the Accounts icon |
| `Push rejected / non-fast-forward` | GitHub has commits your computer does not | **Sync Changes** / **Pull**, then push |
| The GitHub page shows the old file | The commit is local only | **Sync Changes** to push |

A command-line check of where your repository points:

```bash
git remote -v          # the GitHub URL
git status             # what is staged, modified or untracked
git log --oneline      # your commits
```

## 12. Check yourself

- [ ] `git --version` prints a version.
- [ ] `git config --list` shows your name and email.
- [ ] You created `my-project`, initialized it, and made a commit.
- [ ] The repository exists on GitHub and shows your commit.
- [ ] You cloned a repository with **Git: Clone**.
- [ ] You edited a file, committed, and pushed with **Sync Changes**.
- [ ] You pulled with **Source Control → … → Pull**.

Everyday commands and their VS Code equivalents are in the
[cheat sheet](cheatsheet.md).
