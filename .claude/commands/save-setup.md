---
name: save-setup
description: One-time setup. Safely turns on Git for the project — but ONLY after confirming a .gitignore protects the builder's .env. Then makes the first commit. The safe on-ramp to version control.
---

# /save-setup — Turn on Git, safely (run once)

This command turns the builder's project folder into a Git project and makes the **first commit** —
the first save point. It is run **once, ever, per project.** Its defining job is to do this in the
**safe order**: protect the secret first, *then* commit. A first commit that includes `.env` is the
one mistake this command exists to prevent.

**The one rule that defines this command: never make the first commit until `.env` is provably
ignored.** If there's any doubt, stop and fix the `.gitignore` first.

## Read this first

1. Read `CLAUDE.md` — Section 4 (the lifecycle and version-control commands), Section 8 (the builder, for
   commit name/email), and Section 9 (hard rules — note rule 8: no secrets in code or anywhere they
   could leak).
2. Read the last 2–3 entries of `PROJECT_HISTORY.md` to confirm where the project stands.
3. Check whether Git is already initialized (a `.git` folder may exist — see the gate below).

## The gate check (enforce this every time — this is the point of the command)

Before doing anything else, confirm the secret is protected:

- **Is there a `.gitignore` at the top of the project folder, and does it list `.env`?**
  - **If NO `.gitignore`, or it does not ignore `.env`:** stop. Say, in plain language:
    > "Before I turn on Git, your `.env` (which holds your database password) must be protected, or
    > it could get uploaded to GitHub. Let's create a `.gitignore` that ignores `.env` first — that's
    > Lab 2. Want me to do that now?"
    Create the `.gitignore` (ignoring `.env`, plus `__pycache__/`, `*.pyc`, `node_modules/`,
    `.DS_Store`, `venv/`, `.venv/`) and **confirm with `git status` thinking** that `.env` is ignored
    before continuing.
  - **If a proper `.gitignore` exists and ignores `.env`:** good — proceed.

## Handle an existing `.git` folder

The shared project may contain a leftover `.git` folder (an artifact). Check:

- **If `.git` exists but has no commits** (no history): it's safe to use as-is, or you may treat this
  as a fresh start. Either is fine — just be transparent: "There's an existing Git folder with no
  history; I'll use it and make your first commit."
- **If `.git` exists with real history or a remote:** don't blow it away. Tell the builder what's
  there and ask how they'd like to proceed.
- **If no `.git`:** run `git init` to create one.

## Do it (plan-mode discipline)

State the plan in plain English first and wait for approval. Then, in order:

1. **Confirm Git identity.** Set `git config user.name` and `git config user.email` from
   `CLAUDE.md` Section 8 (the builder's name and Moody's email) if not already set. If Section 8
   lacks an email, ask for it.
2. **`git init`** if needed (skip if a usable repo already exists).
3. **Stage the project:** `git add` everything that isn't ignored.
4. **Show the diff before committing — REQUIRED.** List the files that will be in this first commit,
   in plain language, and **explicitly confirm `.env` is NOT among them.** Say something like:
   "Here's what your first save will include: `CLAUDE.md`, `app.py`, `data/`, `.gitignore`, … —
   and importantly, **not** your `.env`, so your password stays on your laptop. Look it over."
   If `.env` appears in the list, STOP, fix `.gitignore`, and re-stage before committing.
5. **Commit:** `git commit -m "Initial commit: project scaffold and current work"`
   (or a message that fits what the project actually has so far).
6. **Show `git log`** so the builder sees their first save point exists, and explain in one or two
   plain sentences what a commit is.

Then say: "Git is on and your first save is made. Next, in Lab 4, run `/publish` to back this up to
GitHub."

## Do NOT

- **Do not commit before confirming `.env` is ignored.** This is the one unforgivable error.
- **Do not connect to GitHub or push** — that's `/publish` (Lab 4). This command is local only.
- **Do not create branches or do anything beyond the first commit.**
- **Do not delete an existing `.git` folder with real history** without the builder's clear okay.

## Append to PROJECT_HISTORY.md

Add an entry in the standard format: Step "Save-setup", a one-line summary (Git initialized, first
commit made, `.env` confirmed ignored), files created (`.gitignore`), and **Next:** "Run `/publish`
to back the project up to GitHub."
