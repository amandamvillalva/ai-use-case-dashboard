---
name: brainstorm
description: Interview the builder about their project and produce a design doc. Step 2 of the lifecycle.
---

# /brainstorm — Step 2: Design v0

You're going to design the v0 with the builder through conversation, then write a short design doc.
A design doc answers *what we're building and why* — not *how*. The "how" comes later in `/mvp-spec`.

## Read this first

1. Read `CLAUDE.md` — Section 1 (what the project is), Section 8 (who's building it and for whom).
2. Read `PROJECT_HISTORY.md` (skip the example block). If `/interview-me` hasn't been run (Section 8
   is still placeholders), pause and say: "Quick thing first — run `/interview-me` so I know what
   we're designing. It takes two minutes." Then stop.

## How to behave

- Ask the questions below **one at a time**, in order. Wait for each answer.
- **Push back on vague answers.** This is the most important thing you do here. "It should do
  everything" is not a design — narrow it: "If it could only show one thing at a glance, what would
  it be?"
- **Restate to confirm** after the big answers, so the builder knows you captured the heart of it.
- Stay honestly scoped to a **v0**: the smallest real version of the core idea. Richer features are
  coming — but v0 is "the one core thing, working, visible." Don't let them design something they
  can't see take shape early.
- Lean on what you know from Section 8 — their domain, their constraints, their working style.

## The questions (ask one at a time)

1. **"Let's restate the core: in one sentence, what's the heart of this thing?"**
   *Push if vague.* Tie it back to the problem from `/interview-me`.

2. **"Walk me through what a user actually sees or does. What's on the screen, or what's the flow?"**
   Get concrete — the main view, the key fields, the primary action. Help them cut if they list
   twenty things.

3. **"When someone opens this, what's the FIRST thing that should grab them? The one number, status,
   or action that matters most?"**
   *Why:* this becomes the focal point — the default view, the thing you emphasize.

4. **"Where does the data come from, and where does it live?"**
   A CSV they have? An existing export? A database or SaaS tool they'll connect to? Something the app
   creates itself? Note it — and if any secret/credential is involved, note that it'll go in `.env`.

5. **"What is this explicitly NOT going to do — for now? Name one or two things we're leaving out."**
   *Why:* non-goals are the most powerful tool in software. A v0 that does one thing well beats a v1
   that does five things badly. Steer toward the smallest honest version.

## What to produce

Get today's date from the system. Write the design doc to:
`docs/designs/YYYY-MM-DD-<project>-v0-design.md` (use a short project slug from Section 1).

Use this structure exactly:

```markdown
# [Project] v0 — Design

**Author:** [builder name]   **Date:** YYYY-MM-DD

## Problem
[1–2 sentences: the painful thing this solves, in their words.]

## Who it's for
[Primary user(s).]

## What it does / shows
[The core view or flow; the key fields or steps — list them.]

## The one thing that matters most
[The focal point / the default view / the primary action.]

## Where the data comes from
[Source: CSV, database, SaaS API, app-created. Note any secret -> goes in .env.]

## Success looks like
[How they'll know v0 worked: "I can open it and immediately X."]

## Non-goals (v0)
- [Thing we are deliberately not doing.]
- [Another.]

## Notes / unknowns
[Data quirks, integrations to confirm, anything flagged for later.]
```

Then tell the builder in plain language what you captured, and say: "Next step is `/mvp-spec` — I'll
turn this design into a small, doable build plan."

## Append to PROJECT_HISTORY.md (required)

Use the format from `CLAUDE.md` Section 7. Title it:
`## YYYY-MM-DD — Brainstorm: Designed v0`

- **What we did:** what the v0 will do and for whom.
- **Key decisions:** the focal point, the data source, the non-goals.
- **Files changed/created:** `docs/designs/YYYY-MM-DD-<project>-v0-design.md` (new).
- **Open questions:** anything unresolved.
- **Next:** "Run `/mvp-spec` to turn this design into an MVP build plan."
