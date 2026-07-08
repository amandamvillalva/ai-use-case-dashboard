---
name: test
description: Verify the phase just built — by hand against real and bad input, and (where it earns it) with real unit tests via pytest (Python) or Vitest (React). The "Test" in the Build->Test->Closeout loop.
---

# /test — Prove the phase works

Testing isn't a chore at the end — it's **how you know it works**. `/test` is the middle of the
loop: `/build` made the phase, `/test` proves it, `/closeout` records it. A tested phase is one you
can actually trust enough to put in front of real people.

`/test` has **two faces**, and which you use depends on the phase:

- **Every phase: verify it by hand.** Run the app, check the phase's success criterion from the
  full-spec, and try one piece of bad input to confirm it fails *gracefully* — a clear message, not a
  blank page or a crash.
- **Phases that deserve real coverage: write unit tests.** Repeatable tests that run with one
  command — `pytest` (Python) or `npm test` / Vitest (React) — per the standards in `CLAUDE.md PART 2`.

## Read this first

1. Read `CLAUDE.md` — Section 3 (the loop), Section 9 (hard rules), and **PART 2 — Engineering
   Standards** (the testing section names the framework, file names, and run command for this stack).
2. Read the **last 2-3 entries** of `PROJECT_HISTORY.md` to see which phase was just built.
3. Read the matching phase in the `FINAL` full-spec — its **Test:** line is your checklist.

If nothing has been built yet, say: "There's nothing to test yet — run `/build` first." Then stop.

## Face 1 — Verify the phase by hand (every phase)

Walk the builder through checking the phase's own **Test:** criterion. Be concrete about the command
to run and what they should see. For each check, also try the obvious bad input once — a wrong
address, a missing field, an empty file. The lesson: good software says *what went wrong* in plain
words instead of breaking. (This is also the QA habit the course taught — ask "does it do what I
asked? does it break under pressure? would a real user understand it?")

## Face 2 — Write real unit tests (where the phase earns it)

This is where testing graduates from "click around and look" to "the computer checks it for me, the
same way, every time." For someone newer to this, the concept lands best when it comes **before** any
code, when they **do** the key step themselves, and when the failure is in **plain English**.

### Step 1 — Lead with the idea, before any code appears

Ask first, then answer: *"You have a rule — every record must have [a required field] before it
saves. How do you know that rule is still enforced six months from now, after three people have
touched the code? A **test** is the answer: a script that checks that rule automatically, every time,
so nobody has to remember to look."* Then show the code. They have a frame before they see syntax.

### Step 2 — Write a small, meaningful suite

To the standards in `CLAUDE.md PART 2`, cover the few tests that matter (not 100% coverage):

- **Python (pytest):** tests in `tests/`, named `test_*.py`. Cover the core: the main read works; a
  **good** write/action succeeds; a **bad** input (missing a required field) is rejected with a clear
  message and changes **nothing**. Run with `pytest tests/`. Ensure `pytest` is in `requirements.txt`.
- **React/Next.js (Vitest + RTL):** tests alongside the code or in `tests/`. Cover the API/handler the
  same way, plus one component-behavior test if it fits. Run with `npm test`.

**One hard rule: tests must never touch live external systems** — not the production database, not a
billable API, not anything shared. Use a **test double** (a small fake, in-memory layer the app talks
to during tests) so the suite is fast, repeatable, and writes nothing real. Say it in one sentence:
"tests must be safe to run a thousand times, so they practice on a stand-in, not the real thing."

Show the green run.

### Step 3 — Translate the red BEFORE you break anything

A failing test prints something like `assert 201 == 400`, meaningless to a beginner. **Before**
showing a failure, translate it: *"This test asks: 'if I submit a record with no [required field],
does the app say NO?' It expects a 400 — 'rejected.' If it gets 201 — 'saved' — the test fails,
because the gate was supposed to stop this."* Now the numbers read as a sentence.

### Step 4 — Let the BUILDER break it (and predict first)

Have *them* comment out the rule that enforces the requirement, predict what the test will do, then
run it and watch it go red. Doing it themselves — and predicting first — is what makes it stick.
Then restore the rule and watch it go green again.

## Append to PROJECT_HISTORY.md

`/test` doesn't usually write its own entry — the "phase done (built + tested)" entry comes from
`/closeout`. If testing surfaced something worth remembering (a bug found, a decision made), note it
so `/closeout` can fold it in.
