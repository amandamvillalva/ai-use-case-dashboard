---
name: prototype
description: Read the MVP spec and build a working v0, then iterate with the builder until it's right. Step 4 of the lifecycle.
---

# /prototype — Step 4: Build the working v0

You're going to build the smallest real version of the project from the MVP spec, get it running so
the builder can see it, and then **iterate with them** until it feels right. The prototype proves the
*direction* cheaply. Building it *well* — the real stack, the standards, the phases — comes next in
`/full-spec`.

## Read this first

1. Read `CLAUDE.md` — Section 1 (the project), Section 4 (supported stacks), Section 6 (plan mode),
   Section 8 (working style).
2. Read the **most recent** MVP spec in `docs/plans/`. That's what you're building.
3. Read the last 2-3 real entries of `PROJECT_HISTORY.md`. If no MVP spec exists, say: "Let's plan
   first — run `/mvp-spec`." Then stop.

## How to behave

- **Keep the prototype simple and runnable.** The goal is to see the core idea working as fast as
  possible — not to build production architecture. Pick the lightest thing that runs and shows the
  idea. (Production structure is `/full-spec`'s job.)
- **Use plan mode.** Before building, lay out a short numbered plan of what you'll create and wait for
  approval. Build the MVP steps in order; show the builder how to run/open it after each meaningful
  piece.
- **Then make it a conversation.** Once it runs, invite iteration: "Open it and tell me what to
  change — a color, a column, the layout, a feature." Make each change small, show what changed
  (the reading-diffs habit), and keep going until they're happy.
- **Never put a secret in the prototype.** If it needs real data behind a credential, stub or sample
  the data for now and note that the real connection lands in the build.
- Honor the supported-stack lane (Section 4) even for the prototype where it's natural; but a quick
  throwaway HTML/JS prototype to prove a UI idea is fine — just flag that the real stack gets chosen
  deliberately in `/full-spec`.

## Iterating well

- One change at a time. Show it, let them react.
- If they ask for something big or structural, drop back into plan mode first.
- If they ask for something out of the supported stack, build the prototype anyway if it's the
  fast way to prove the idea, but note it for the stack decision in `/full-spec`.

## When they're happy

Offer the same fork the course taught: "Want to lock this direction in, or keep iterating?"
- **Lock it** -> mark the plan's status note that the direction is proven, and point to `/full-spec`
  to choose the real stack and phase the build.
- **Keep iterating** -> stay in the loop; locking can happen later. Both are fine.

Don't change the plan's status to FINAL here — that's `/full-spec`'s job. `/prototype` proves the
direction; `/full-spec` commits to building it for real.

## Append to PROJECT_HISTORY.md (required)

Use the format from `CLAUDE.md` Section 7. Title it:
`## YYYY-MM-DD — Prototype: Built and iterated v0`

- **What we did:** what you built, and the main iterations the builder asked for.
- **Key decisions:** anything that came up that will matter for the real build / stack choice.
- **Files changed/created:** list them with paths.
- **Open questions:** anything to resolve before building for real.
- **Next:** "Run `/full-spec` to choose the stack, install standards, and phase the build."
