---
name: build
description: Build the next unbuilt phase of the FINAL full-spec as real, production-quality code, following the engineering standards in CLAUDE.md PART 2. The durable sibling of /prototype. Builds ONE phase at a time.
---

# /build — Build the next phase

`/build` is the production sibling of `/prototype`. `/prototype` was fast and throwaway-shaped — it
proved the direction. `/build` is durable: it executes a **locked plan** to a much higher quality
bar, following the engineering standards now in `CLAUDE.md PART 2`.

**The one rule that defines this command: build ONE phase, the next unbuilt one. Not the whole app.
Not two phases. One.** Then hand off to `/test` and `/closeout`, and the loop comes back around for
the next phase.

## Read this first

1. Read `CLAUDE.md` — Section 3 (the Build->Test->Closeout loop), Section 4 (the supported stacks),
   Section 9 (hard rules — note rule 6: `/build` requires a FINAL full-spec; rule 4: no secrets in
   code; rule 7: beginner-readable code), and **all of PART 2 — Engineering Standards** (the bar you
   build to). Section 8 (who's building it).
2. Read the **most recent plan** in `docs/plans/` and check its **Status** line.
3. Read the **last 2-3 real entries** of `PROJECT_HISTORY.md` to see which phases are already done.

## The gate check (enforce this every time)

`/build` runs ONLY against a plan whose status is `FINAL` **and titled as a full-spec**
(`...-v1-full-spec.md`). Check the most recent plan:

- **If there's no full-spec, or the most recent plan is only `MVP`/`SUPERSEDED`:** refuse and say, in
  plain language:
  > "`/build` needs a **FINAL full-spec** — the plan that picks the stack and breaks the build into
  > phases. Right now I don't see one. Run `/full-spec` first; it'll ask you a few questions, install
  > the engineering standards, and write the phased plan. Then come back and run `/build`."
  Then stop.
- **If a `FINAL` full-spec exists:** good — proceed.

## Find the next unbuilt phase (the loop's position)

`PROJECT_HISTORY.md` is the only record of where the loop is. Read it:

- Look for the most recent `Closeout` (or `Build`) entries that name a completed phase ("Phase 1
  closed out," "Phase 2 done").
- The **next unbuilt phase** is the lowest-numbered phase in the full-spec that has NOT been closed
  out yet. Build **that one only**.
- If every phase is closed out, say so and point to `/closeout` (the project wrap) — don't invent new
  work.

State it plainly before you start: "Phases 1 and 2 are done per the journal, so today I'll build
**Phase 3 only**. Here's what that phase adds..."

## If the next phase connects to data behind a secret

Many builds reach a phase that connects to real data — a database, a SaaS API, anything needing a
connection string or key. Before building it, confirm the needed value exists in `.env` (e.g.
`DATABASE_URL`, `OPENAI_API_KEY`, whatever this project uses). If it's missing, say: "This phase
connects to [the thing] — add its connection string / key to `.env` first, then I'll build this
phase." Then build it reading the secret from `.env` (via `python-dotenv` / `process.env`), **never
hardcoding it, never writing it into a doc or the history.** Make failures legible: if the
connection can't be reached, the app should say so clearly, not crash silently.

## Build the phase (plan-mode discipline)

Build **only** the current phase, to the standards in `CLAUDE.md PART 2`:

1. **State the plan first** (plan mode). In plain English, list what you'll add for this phase, which
   files you'll create or change, and how the builder will check it works. Wait for approval.
2. **Honor the chosen stack** from the full-spec:
   - **Flask:** a small Python server (`app.py`) plus `requirements.txt`; run with `python app.py`
     and visit the local address it prints. Templates in `templates/`, static assets in `static/`,
     data in `data/`, tests in `tests/`.
   - **Streamlit:** a Python script that serves UI and logic together; run with `streamlit run`.
   - **React/Next.js:** components (`.jsx`/`.tsx`); dev server with `npm run dev`; API as route
     handlers; tests alongside, run with `npm test`.
3. **Write code a beginner can read** — small functions, clear names, comments that explain the
   *why*, sensible error handling. If this app calls an AI model or any API at runtime, that's a
   legitimate design choice — implement it cleanly and keep the key in `.env`.
4. **Secrets never go in code** — always read from `.env` (rule 4).
5. **Show the diff and run it.** After building, show what changed and tell the builder exactly how
   to see it working (the command to run, the address to visit, what they should see).

Then say: "Phase [N] is built. Next, run `/test` to verify it, then `/closeout` to log it and capture
what we just did. (And `/save` whenever you want to back up your progress.)"

## Do NOT

- **Do not build more than one phase.** Even if it's tempting, even if the next one is small.
- **Do not add features** that aren't in the current phase.
- **Do not put secrets in code**, ever.
- **Do not go outside the supported stack** unless the full-spec recorded a reason to.

## Append to PROJECT_HISTORY.md

`/build` does **not** write the "phase done" entry — that's `/closeout`'s job, and it's how the loop
knows a phase is finished. After building, leave the journal to closeout. (If the builder stops
mid-phase, you may add a short "Build in progress: Phase N partially built" note so the next session
can resume — but the official "done" entry comes from `/closeout`.)
