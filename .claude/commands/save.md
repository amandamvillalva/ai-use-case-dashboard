---
name: save
description: The everyday save loop. Shows the builder what changed, commits it with a clear message, and pushes to GitHub. Run every time the builder finishes a piece of work. The habit that becomes permanent.
---

# /save — Save your work and back it up (run often)

This is the command the builder will use for the rest of this project and beyond. It runs the everyday
loop: **show what changed → commit it with a clear message → push it to GitHub.** Small, frequent
saves are the single best habit in software; this command makes that habit one word.

**Prerequisites:** `/save-setup` and `/publish` have both been run (Git is on, a GitHub remote
exists, the one-time sign-in is done). If not, point the builder there first.

## Read this first

1. Read `CLAUDE.md` — Section 8 (the builder), Section 9 (hard rule 4: secrets never leak).
2. Run a status check to see what's changed since the last commit.
3. Confirm `.env` is still git-ignored (it should be, from `/save-setup`) — never let it slip in.

## Do it (plan-mode discipline + the reading-diffs habit)

1. **Show what changed — REQUIRED.** Before committing, show the builder what changed since their
   last save, in plain language: which files, and the one or two changes that matter. This is the
   *reading-diffs* habit: "if you didn't read it, you didn't write it." Confirm `.env` is **not**
   among the changed files being staged.
   - If there are **no changes**, say so plainly: "Nothing's changed since your last save, so there's
     nothing to save right now. Make a change first, then run `/save`." Then stop.
2. **Propose a clear commit message** that describes the change in plain English (e.g. "Add subtitle
   with a last-updated date to the header"). Let the builder approve or reword it. Good messages are
   specific and human — never "update" or "changes."
3. **Stage, commit, push** in sequence: `git add` (everything not ignored) → `git commit -m "<message>"`
   → `git push`. Run them for the builder.
4. **Confirm** and invite a check: "Saved and pushed. Refresh your repo on github.com — you'll see
   your updated file and a new entry in the history with this message."

> **No sign-in window now.** The one-time GitHub approval happened during `/publish`; `/save` pushes
> silently. If a push ever *does* prompt for auth, the credential may have expired — re-approve and
> retry.

## Keep it a habit, not a chore

End by reinforcing the rhythm when it fits: "That's the loop — finish a piece of work, `/save`. Small
and often means you can always get back to a working version." Don't lecture every time; a light
touch keeps the habit welcome.

## Do NOT

- **Do not commit `.env`** or any secret. Re-confirm it's ignored every time.
- **Do not commit with a vague message.** A save you can't identify later isn't much of a save.
- **Do not bundle unrelated changes** silently — if a lot changed, note it, and offer to describe it
  accurately in the message rather than hiding it behind "misc updates."
- **Do not create branches or open PRs here** — that's the stretch lab's flow, done explicitly.
- **Do not use the GitHub CLI (`gh`) or offer to open a pull request from the terminal.** It isn't
  installed in this environment and will fail. If the builder asks for a pull request, explain in
  plain language that PRs are created on **github.com in the browser** (Lab 6) — and that even
  making a branch and pushing it is something the lab walks them through deliberately. Point them to
  the lab rather than attempting it yourself.

## Append to PROJECT_HISTORY.md

For routine saves, a `PROJECT_HISTORY.md` entry is optional (the Git history *is* the log). Add one
only when the save marks a meaningful milestone the builder would want narrated later — and if so,
use the standard format.
