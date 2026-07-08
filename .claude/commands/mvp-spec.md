---
name: mvp-spec
description: Read the latest design doc and produce a small, MVP-scoped, step-by-step build plan. Produces docs/plans/...-spec.md. Step 3 of the lifecycle.
---

# /mvp-spec — Step 3: Plan the MVP

You're turning the design into a **deliberately small** step-by-step plan. The plan's job is to
answer one question: *what is the smallest version of this that proves the direction works?* Not the
best version. The smallest one that's real.

## Read this first

1. Read `CLAUDE.md` — Section 4 (supported stacks), Section 5 (file conventions), Section 8 (the project).
2. Read the **most recent** design doc in `docs/designs/`. That's your source of truth.
3. Read the last 2-3 real entries of `PROJECT_HISTORY.md` (ignore the example block). If no design
   doc exists, say: "Let's design first — run `/brainstorm`." Then stop.

## The MVP mindset (this is the whole point)

A plan written by a beginner-with-a-genie tends to balloon. Your job is the opposite: **cut.** The
MVP is the one core thing from the design, working and visible, and almost nothing else. Extra
features are *iterations* the builder will ask for during `/prototype` — they are NOT in this plan.

If the design lists ten features, the MVP plan includes the two or three that prove the core idea.
Say so out loud: "I'm scoping this down hard on purpose. We'll add the rest by iterating on the
working prototype — that's faster, and you'll see each change as it happens."

## How to behave

- Write steps **small enough to verify one at a time.** Each step ends in something the builder can
  see or check. "You'll be able to open it and see the main view with real data" is verifiable.
  "Build the app" is not.
- Keep it to **roughly 4-7 steps.** More than that for a v0 means you haven't cut enough.
- Don't pick the production stack here — the prototype stays light and fast (a simple, runnable v0).
  The deliberate stack decision happens in `/full-spec`, after the prototype proves the direction.
  For most prototypes, the simplest thing that runs and shows the idea is right.
- Note any data the prototype needs. If it needs a secret to reach real data, note that the real
  connection comes later (in the build) and the prototype can use sample or stubbed data for now.

## What to produce

Get today's date from the system. Write the plan to:
`docs/plans/YYYY-MM-DD-<project>-v0-spec.md`

Use this structure exactly:

```markdown
# [Project] v0 — MVP Spec

**Status:** MVP
**Author:** [builder name]   **Date:** YYYY-MM-DD
**Based on design:** [exact filename of the design doc you read]

## The one thing this proves
[One sentence: the core idea this MVP demonstrates.]

## Build steps (each small, each verifiable)
1. [Step] -- *you'll be able to:* [the visible check]
2. [Step] -- *you'll be able to:* [the visible check]
3. ...

## Data for the prototype
[Sample/stub/real-but-read-only. Note any secret deferred to the build.]

## Explicitly not in the MVP
- [Feature deferred to iteration / later.]
- [Another.]
```

Then tell the builder: "Here's the smallest plan that proves your idea. Next, run `/prototype` and
I'll build it — then we iterate on it together until it feels right."

## Append to PROJECT_HISTORY.md (required)

Use the format from `CLAUDE.md` Section 7. Title it:
`## YYYY-MM-DD — MVP Spec: Planned the smallest version that proves the idea`

- **What we did:** scoped the design down to a small, verifiable MVP plan.
- **Key decisions:** what's in, what got cut to iteration.
- **Files changed/created:** `docs/plans/YYYY-MM-DD-<project>-v0-spec.md` (new, status MVP).
- **Open questions:** anything still open.
- **Next:** "Run `/prototype` to build the working v0."
