---
name: guide
description: Your compass. Reads where the project stands and tells you what to do next, in plain language. Also lets you choose how hands-on you want Claude to be — fully guided (step-by-step) or autonomous (just do it). Run it anytime you're unsure.
---

# /guide — Where am I, and what's next?

`/guide` is the command to run whenever you're not sure what to do — at the very start, or any time
you lose the thread. It does two things: it tells you **where you are and what the next step is**, and
it lets you set **how hands-on you want Claude to be** for the work ahead.

## Read this first

1. Read `CLAUDE.md` — Section 3 (the lifecycle), Section 8 (the project and the builder's working
   style), and whether Section 8 is still placeholders.
2. Read `PROJECT_HISTORY.md` — the last 2-3 real entries tell you exactly where the project stands.
3. Note whether key files exist yet: a design doc in `docs/designs/`, a plan in `docs/plans/` and its
   status (MVP vs FINAL), whether Git is set up (a `.git` folder / a remote).

## Part 1 — Tell them where they are and what's next

From the journal and files, work out the current position in the lifecycle and say it plainly, then
name the single next step. Use this map:

- **Section 8 still has placeholders / no history** -> "You're at the very start. Run `/interview-me`
  so I understand what we're building."
- **Interviewed, no design doc** -> "Next: `/brainstorm` to design v0."
- **Design doc exists, no plan** -> "Next: `/mvp-spec` to plan the smallest version."
- **MVP plan exists, no prototype built** -> "Next: `/prototype` to build and iterate a working v0."
- **Prototype built, no FINAL full-spec** -> "Next: `/full-spec` to choose your stack, install
  standards, and break the build into phases."
- **FINAL full-spec exists, phases remain** -> "You're in the build loop. Next: `/build` the next
  unbuilt phase, then `/test`, then `/closeout`." (Name which phase number is next, from the journal.)
- **All phases closed out** -> "You're done building. Run `/closeout` to wrap the project and
  `/teach-me` to capture what you learned."
- **Never set up version control** -> mention it: "Whenever you're ready, `/save-setup` turns on Git
  so your work is backed up — worth doing early."

Give the answer in two or three sentences. Don't dump the whole lifecycle table unless they ask.

## Part 2 — Offer to set the working mode

Ask, once: **"How do you want me to work with you on this — guided, or autonomous?"** Explain the two
in one line each, then honor their choice for the session (and note it so future sessions can ask
again):

- **Guided (default for newer builders):** "I'll explain each step before I do it, work in small
  pieces, show you what changed, and check in before anything big. Best if you want to learn as we go
  or stay in control." This maps to **plan mode on**, smaller steps, more teaching.
- **Autonomous (for when you trust the flow):** "I'll move faster — make reasonable calls, do several
  steps in a row, and only stop to ask when something genuinely needs your decision. Best when you
  just want it built." This maps to fewer check-ins — but the **hard rules still hold**: no secrets in
  code, `/build` still needs a FINAL plan, and I'll still show you anything irreversible before doing
  it.

If they already told you a working style in `/interview-me` (Section 8), suggest the matching mode as
the default rather than asking cold: "You mentioned you like to move fast — want me to run autonomous?"

Whatever they pick, restate it in one line so it's explicit: "Got it — guided mode. I'll talk you
through each step." Then point them at their next command from Part 1.

## Don't

- Don't change any files or build anything — `/guide` only orients and sets mode.
- Don't override the hard rules in autonomous mode. Faster, not reckless.
- Don't append to `PROJECT_HISTORY.md` — this is navigation, not a project step.
