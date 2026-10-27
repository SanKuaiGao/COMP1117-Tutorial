# Git cheat sheet — Tutorial 4

The same actions in the terminal and in VS Code. You can do everything with the
buttons; the commands are here so you understand what the buttons do, and for
when VS Code is not available.

## Setup (once per computer)

| Task | Command |
| --- | --- |
| Check that Git is installed | `git --version` |
| Set your name | `git config --global user.name "Your Name"` |
| Set your email | `git config --global user.email "your-email@example.com"` |
| Show your settings | `git config --list` |

## The everyday actions

| Task | Terminal | VS Code |
| --- | --- | --- |
| Start tracking a folder | `git init` | **Source Control → Initialize Repository** |
| See what changed | `git status` | **Source Control** panel |
| See the actual lines that changed | `git diff` | Click the file under **Changes** |
| Stage a file | `git add README.md` | **+** next to the file |
| Stage everything | `git add .` | **+** next to **Changes** |
| Commit what is staged | `git commit -m "Add a new section"` | Message box, then the **✓** |
| Show the history | `git log --oneline` | `git log`, or the GitHub commits page |
| Create a GitHub repository and upload | (create it on GitHub, then `git push -u origin main`) | **Publish Branch** |
| Upload your commits | `git push` | **Sync Changes** |
| Download the latest changes | `git pull` | **Source Control → … → Pull** |
| Download a repository | `git clone <url>` | **Command Palette → Git: Clone** |
| See which GitHub repo you are linked to | `git remote -v` | The status bar / Source Control |
| Throw away uncommitted changes to a file | `git restore README.md` | Discard in the Source Control menu |

`Sync Changes` = pull, then push. It is the button you press most often.

## Letters you will see in the Source Control panel

| Letter | Meaning | What to do |
| --- | --- | --- |
| `U` | Untracked — Git has never seen this file | Stage it with **+** to start tracking it |
| `M` | Modified — tracked, changed since the last commit | Stage and commit |
| `A` | Added — staged for the first time | Commit |
| `D` | Deleted | Stage the deletion and commit |
| `!` | Conflict | See the [Tutorial 5 README](../branching&merging/README.md) |

## Commit messages

A commit message explains **why** the change exists. Write the subject in the
imperative, as if you were giving an instruction, and keep it under about 50
characters.

| Good | Why |
| --- | --- |
| `Add a new section to the README` | Says what the commit does |
| `Fix the average calculation` | Names the actual fix |
| `Rename temperature.py to celsius.py` | Small and specific |

| Avoid | Why |
| --- | --- |
| `update` | Nothing about what changed |
| `asdf`, `test`, `123` | No information at all |
| `Did some stuff and fixed things` | Too vague to search later |

If a commit needs more explanation, leave one blank line after the subject and
write a short paragraph below it.

## Common errors

| Message | Meaning | Fix |
| --- | --- | --- |
| `fatal: not a git repository` | The current folder is not tracked by Git | `cd` into the project folder, or `git init` |
| `Please tell me who you are` | Name and email are not configured | Run the two `git config --global` commands |
| `nothing to commit, working tree clean` | There is nothing new to commit | Edit a file, or check that you staged it |
| `error: pathspec 'x' did not match any file(s)` | The file name is wrong | `git status` to see the real names |
| `Permission denied (403)` | You are pushing to a repository you do not own | Fork it first ([Tutorial 5](../branching&merging/README.md)) |
| `! [rejected] ... (fetch first)` | GitHub has commits you do not have | `git pull`, then `git push` |
| `fatal: refusing to merge unrelated histories` | Two separate repositories are being joined | `git pull --allow-unrelated-histories` — only when you really mean it |

## Files that must never be committed

- Passwords, API keys, tokens, `.env` files
- Huge data files, videos, virtual environments
- The `.git` folder itself

If you commit a secret by accident, changing the file is **not** enough — it
stays in the history. Revoke the secret first, then ask for help cleaning the
history.
