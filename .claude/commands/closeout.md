---
name: closeout
description: Close out the build. After a phase, it logs what you did to PROJECT_HISTORY.md and teaches it back; once every phase is done, it wraps the whole project. It figures out which from where you are. The "Closeout" in the Build->Test->Closeout loop.
---

# /closeout — Close out (the phase, or the project)

`/closeout` is the **third beat of the build loop**: `/build` makes a phase, `/test` proves it,
`/closeout` records it and teaches it. Run it **after every phase**. When the last phase is done, the
same command wraps the whole project.

**It is context-aware.** You don't pick a mode — `/closeout` reads where the project stands and does
the right thing, and always says which it's doing:

- **Phase closeout** (the common case): a phase just finished and more remain. Log it and teach it back.
- **Project closeout** (once, at the end): every phase is done. Wrap the whole project — summary,
  what's next, clean handoff.

## Read this first

1. Read the **last 2-3 entries** of `PROJECT_HISTORY.md` so your new entry continues the story (no
   duplicates, consistent voice) and you can see which phase was just built.
2. Read the `FINAL` full-spec in `docs/plans/` — it tells you the **total number of phases** and which
   was just finished, so you can tell phase-closeout from project-wrap.
3. Glance at `CLAUDE.md` Section 7 (entry format) and Section 8 (working style — match it).

## Decide the mode (and say it out loud)

- If phases remain unbuilt → **Phase closeout.**
- If the phase just finished is the **last** one, or the builder says "wrap it / we're done" →
  **Project closeout.**

State which, briefly. If you genuinely can't tell what was just done, ask **one** question: "What
should I record — what did we just do?"

---

## MODE A — Phase closeout (after each phase)

1. **Log it.** Append a `PROJECT_HISTORY.md` entry (format from Section 7) titled
   `## YYYY-MM-DD — Closeout: Phase [N] done — [one-line summary]`, covering what the phase built,
   key decisions, files changed, open questions, and **Next:** the next phase (or `/test` if not yet
   run).
2. **Teach it back** — two or three plain-language sentences on what this phase actually did and the
   concept behind it (a server, an API, a database read/write, the .env habit, a test). Tie it to the
   builder's project, not generic theory. Match their working style from Section 8.
3. **Point to the next step:** "Next, run `/build` for Phase [N+1]" — and remind them they can `/save`
   to back up progress.

---

## MODE B — Project closeout (once, at the end)

Every phase is done. Wrap it:

1. **Write a closing `PROJECT_HISTORY.md` entry** titled
   `## YYYY-MM-DD — Project closeout: [project] v1 complete` — what got built end to end, the final
   shape, what's deferred, and any known limitations.
2. **Summarize for the builder** in plain language: what they built, the layers it touches, and what
   it can and can't do.
3. **Run the full reflection** — invoke the logic in `/teach-me` (the whole-project lesson), or tell
   them to run `/teach-me` next.
4. **Flag the road to real if relevant:** if this tool will be used by actual people or touch
   sensitive data, remind them — calmly — that it likely needs a Moody's governance tier, and that
   going live (deployment) is its own step beyond this build. Don't invent specifics; point them to
   the Maker governance process.
5. **Remind them to `/save`** so the finished project is backed up.

## Match the builder's voice

Whichever mode, write the way they like to be talked to (Section 8) — terse or detailed, lots of why
or just the headline. Never condescend.
