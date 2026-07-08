---
name: publish
description: One-time command. Connects the builder's local Git project to a GitHub repository they created in the browser, and pushes their first commit to the cloud. Handles the one-time GitHub sign-in.
---

# /publish — Back up your project to GitHub (run once)

This command connects the builder's local project to a **GitHub repository** and pushes their saved
work to the cloud for the first time. Run **once per project.** After this, `/save` handles every
future push silently.

**Prerequisite:** the builder has already run `/save-setup` (so Git is on and a first commit exists),
and has **created an empty repository on github.com** under the `moodyssharedservices` org, set to
**Private**, with no README/.gitignore/license. They will paste its URL.

## Read this first

1. Read `CLAUDE.md` — Section 4, Section 9 (hard rule 4: secrets never leak).
2. Confirm a local commit exists (`git log` should show at least one). If not, point the builder to
   `/save-setup` first.
3. Confirm `.env` is git-ignored (re-check; this is the last line before the secret could go to the
   cloud). If `.env` is *not* ignored, STOP and fix it before any push.

## Get the repository URL

Ask the builder to paste the URL of the **empty GitHub repo they created in the browser.** It looks
like `https://github.com/moodyssharedservices/<name>.git`.

- If they haven't created it yet, walk them through it (Lab 4, Step 1): github.com → **+** → New
  repository → Owner `moodyssharedservices` → name it (suggest `<initials>-<project>`) → **Private** →
  no README/.gitignore/license → Create → copy the URL.
- **Recommend Private.** If they ask, explain: Private = only they and invitees can see it (safest
  while learning secrets). Internal = anyone at Moody's can view it. Private is the course default.

## Do it (plan-mode discipline)

State the plan plainly and wait for approval. Then:

1. **Connect the remote:** `git remote add origin <url>` (if an `origin` already exists pointing
   elsewhere, tell the builder and confirm before changing it).
2. **Name the main branch** `main` if it isn't already (`git branch -M main`).
3. **Push:** `git push -u origin main`.

> **Flag the one-time sign-in BEFORE pushing.** Tell the builder, in plain language: "The first time
> we push, a **browser window will pop up** to sign in to GitHub and approve access (single sign-on,
> then a 'Git Credential Manager wants to access your account' prompt). That's expected — approve it.
> It only happens once on this laptop; every save after this is silent. If you don't see the window,
> check behind your other windows." Then run the push.

4. **Confirm success** and tell the builder to **refresh their repo page on github.com** to see their
   files — and to **confirm `.env` is NOT in the file list there.** Make this check explicit:
   "Look at the files on GitHub — you should see everything *except* `.env`. That absence is your
   password staying safe on your laptop. Confirm it before we move on."

Then say: "Your project is backed up on GitHub. From now on, `/save` will save and upload your work —
no more sign-in windows. Next is Lab 5."

## If the push fails

- **Auth failure / window never appeared:** the sign-in window may be hidden — have them look behind
  other windows and approve it. If credentials were entered wrong, retry the push to re-trigger it.
- **"Repository not empty" / "rejected (fetch first)":** the GitHub repo was created *with* a README
  or `.gitignore`. Simplest fix: have them delete it and create a truly empty repo (no extras), then
  retry. (Or, if they prefer, `git pull --rebase origin main` then push — but the empty-repo path is
  cleaner for a beginner.)
- **Wrong/typo'd URL:** confirm the remote with `git remote -v` and fix with
  `git remote set-url origin <correct-url>`.

## Do NOT

- **Do not push if `.env` is not confirmed git-ignored.** Last gate before the cloud.
- **Do not create the GitHub repo via API/CLI** — the builder creates it in the browser so they
  consciously choose Private visibility. That choice is part of the lesson.
- **Do not make it Public.** Private (or Internal if they explicitly choose) only.

## Append to PROJECT_HISTORY.md

Standard-format entry: Step "Publish", one-line summary (connected to GitHub repo `<name>`, first
push succeeded, `.env` confirmed absent from remote), and **Next:** "Use `/save` to save and push
future work."
