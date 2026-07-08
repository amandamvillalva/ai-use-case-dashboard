---
name: full-spec
description: Turn the proven prototype into a stack decision, install engineering standards into CLAUDE.md from build-templates/, and write a FINAL plan broken into small, independently buildable phases. Runs after /prototype and before /build. Step 5 of the lifecycle.
---

# /full-spec — Step 5: Pick the stack, phase the build, write the full spec

The prototype proved the *direction*. The full-spec decides *how it gets built for real*. It does
three jobs, in order:

1. **Choose the stack** — deliberately, by asking a few decision questions and mapping the answers to
   a recommendation, staying within the supported families (Python or JavaScript).
2. **Install the engineering standards** — assemble `CLAUDE.md`'s `PART 2 — Engineering Standards`
   from `build-templates/` (the common base + the chosen stack's template), with this project's
   TODOs filled in.
3. **Break the build into small, tightly scoped phases** — each independently buildable and testable,
   so the `/build -> /test -> /closeout` loop has clean units to chew through, one at a time.

This is the hinge: it turns a proven prototype into a real plan.

## Read this first

1. Read `CLAUDE.md` — Section 3 (the lifecycle + the Build->Test->Closeout loop), Section 4 (the
   supported stacks and the stay-in-the-lane rule), Section 5 (file conventions), Section 8 (the
   project and who's building it).
2. Read the **most recent plan** in `docs/plans/`. You need a prototype that's been built and iterated.
3. Read the **last 2-3 real entries** of `PROJECT_HISTORY.md`.
4. Confirm the `build-templates/` folder exists at the repo root. You need `build-templates/base.md`
   plus `build-templates/python.md` and/or `build-templates/react.md`. If it's missing, tell the
   builder to add it back from the starter kit, then stop.

If there's no built prototype yet, say: "Let's get a working prototype first — run `/prototype`." Then
stop. The full-spec specs something that already exists and works; it doesn't invent from scratch.

---

## PART 1 — Choose the stack (ask, then recommend)

Tell the builder: *"Before we build for real, we pick the tools. I'll ask you five quick questions,
then recommend a stack and explain why. You can override me — it's your call, as long as we stay in
the supported set so this stays maintainable."*

Ask these **one at a time**, in plain language. Restate what you heard after each.

### The five decision questions

1. **How interactive does the screen need to be?** "Do people mostly *read* a page that updates now
   and then — or do they click, drag, type, and expect instant changes without reloads?"
   *(read-mostly -> simpler frontend · highly interactive -> richer frontend)*

2. **What does your team already know?** "If you handed this off to maintain, are they more
   comfortable with Python, or with JavaScript and modern web tools? Or neither — I'll pick the
   gentlest path?"

3. **How many people use it at once?** "A handful? A whole department? Or hundreds hitting it
   simultaneously?"

4. **Is it data/AI-heavy, or screen-heavy?** "Is the hard part crunching data — charts,
   spreadsheets, models, an AI call — or a slick, app-like screen?"

5. **Polished consumer product, or internal tool?** "Does it need to look like a public,
   consumer-grade product — or is it an internal tool where 'clean and clear' beats 'beautiful'?"

### The mapping (answers -> recommendation)

Weigh the answers together; no single one decides it. Stay within the supported families.

| Signal from answers | Points toward |
|---|---|
| Read-mostly · Python-comfortable · internal · small team | **Python + Flask** <- *the safe default* |
| Data/AI-heavy · Python-comfortable · UI can be simple · fast to stand up | **Streamlit (Python)** |
| Highly interactive, app-like · JS-comfortable · polished/consumer · many concurrent users | **React / Next.js** |
| Mixed / unsure / "just make it work" | **Python + Flask** |

State the recommendation and the *why* in one short paragraph the builder can follow. Record whatever
they actually choose. **If they want something outside Python/JS or outside these frameworks,** don't
silently refuse — explain the maintainability reason for the lane, and if they still have a genuine
need, honor it and **record the reason in the spec** so the next person understands the call.

### What changes by stack (reflect in Part 3)

- **React/Next.js:** the frontend is **components** (`.jsx`/`.tsx`), not one HTML file; dev server is
  `npm run dev`; the API can be Next.js route handlers; standards template is `react.md`; tests use
  **Vitest + React Testing Library**.
- **Streamlit:** UI and logic live in one Python script, so early phases collapse — shorter phase
  list. Template `python.md`; tests use pytest.
- **Flask:** `app.py` + `requirements.txt`; run `python app.py`; template `python.md`; tests pytest.

---

## PART 2 — Install the engineering standards into CLAUDE.md

Upgrade the project's brain so every `/build` writes to a real standard. Assemble a new section,
**`PART 2 — Engineering Standards`**, and append it to the bottom of `CLAUDE.md`. (Everything above
stays untouched.)

1. **Start with the common base.** Read `build-templates/base.md` — the stack-agnostic standards
   (readable code, comment the *why*, small functions, no secrets in code, how tests fit the loop,
   how the build loop reads PROJECT_HISTORY).
2. **Add the stack template.** Read `build-templates/python.md` or `build-templates/react.md` and fold
   it in.
3. **Fill in the project's TODOs.** Replace placeholders (package name, run command, test command,
   data source) with this project's real values, so the standards are concrete. Flask: run
   `python app.py`, test `pytest tests/`. React: run `npm run dev`, test `npm test`. Streamlit: run
   `streamlit run app.py`, test `pytest tests/`.
4. **Keep it readable.** Trim standards that don't apply to this project; don't paste a wall of text
   about tools it'll never use.

Append exactly like this:

```markdown

---

# PART 2 — Engineering Standards
*(Installed by /full-spec on YYYY-MM-DD. Everything above this line is the original project brain.
Everything below is the engineering standard every /build writes code to.)*

**Chosen stack:** [Python + Flask | Streamlit (Python) | React/Next.js]

[...assembled from build-templates/base.md + the stack template, with this project's TODOs filled in...]
```

Then tell the builder, plainly, what just happened: "I added an engineering-standards section to your
CLAUDE.md. From now on, every time I build, I follow these rules — readable code, comments that
explain *why*, tests that prove it works, and never putting secrets in code."

---

## PART 3 — Break the build into small, scoped phases

Take the proven prototype, the chosen stack, and the standards, and write a **numbered list of
phases**. Each phase MUST be:

- **Small** — buildable in roughly one focused sitting.
- **Independently buildable** — doesn't require a later phase to exist first.
- **Testable on its own** — ends in something you can open, click, or check.
- **Ordered so each phase exposes the limitation the next one fixes** — the same teaching spine as the
  prototype arc.

There's no fixed phase set here — it depends on the project. But a common, healthy shape for a
typical web tool is:

```
Phase 1 — Stand up the real app shell on the chosen stack.
          Serve the core view from a real server (Flask) / run the dev server with the page as a
          component (React) / a running Streamlit script. No new features — just the prototype's
          core, running properly on the production stack.
          Test: it runs at a local address; a wrong route fails cleanly.

Phase 2 — Make the data real (read path).
          Wire the app to its actual data source — a file, a database, or a SaaS/API call. The
          connection/keys go in .env, never in code. The view fills from the real source.
          Test: the view shows real data; the source can be confirmed directly.

Phase 3 — The core action (write/do path), if the project has one.
          The one core thing from the spec — saving a record, triggering the workflow, producing the
          output. Validate input; fail gracefully on bad input.
          Test: the action works end to end; bad input is rejected with a clear message.

Phase 4 — Prove it with tests, per the standards.
          Unit tests (pytest / Vitest) covering the read, a good action, and a rejected bad action —
          using a test double, never touching live external systems.
          Test: the suite runs green; break one rule and watch a test go red.
```

Adapt freely: a read-only dashboard may have no write phase; an AI-powered tool adds a phase for the
model call (key in `.env`, handle the failure/latency cases); a Streamlit tool collapses phases 1-2.
Keep every phase small, ordered, and independently testable. Note each phase's rough size and any
dependency.

**On storage and external systems:** this starter ships with none. Whatever the project connects to —
the builder's own database, a local SQLite file, a SaaS API, an AI model — name it in the phase,
require its credentials in `.env`, and make the failure mode legible. Don't assume a database exists.

---

## What to produce

Get today's date. Write/update **two** documents:

1. **`CLAUDE.md`** — with the appended `PART 2 — Engineering Standards`.
2. **`docs/plans/YYYY-MM-DD-<project>-v1-full-spec.md`** — the phased plan, **status FINAL** (this is
   what `/build` requires).

Use this structure:

```markdown
# [Project] v1 — Full Spec

**Status:** FINAL
**Author:** [builder]   **Date:** YYYY-MM-DD
**Based on prototype plan:** [exact filename]

## Stack decision
**Chosen stack:** [Python + Flask | Streamlit (Python) | React/Next.js]
**Why (from the decision questions):** [2-3 sentences tying answers to the choice.]
**Answers on record:** interactivity = ... · team knows = ... · concurrency = ... · data/AI = ... · polish = ...
**Standards template installed:** [python.md | react.md] (folded into CLAUDE.md PART 2)
**(If outside the supported lane:)** reason recorded here.

## Data / external systems
[What this connects to — file, database, SaaS, AI model — and that credentials live in .env.]

## The one feature we carry end to end
[One sentence — the core thing from /interview-me, proven through every layer.]

## Build phases (each small, independently buildable, independently testable)
### Phase 1 — [name]   _(size: small)_
- **Builds:** [what exists after this phase]
- **Test:** [the check that proves it]
- **Exposes next:** [the limitation that motivates Phase 2]

### Phase 2 — [name]   _(size: ..., depends on: Phase 1)_
...

## Out of scope for now
- [Anything deferred — auth, extra features, scale, etc.]

## How the build loop uses this
`/build` builds the next unbuilt phase (reads PROJECT_HISTORY.md to see which are done), `/test`
verifies it, `/closeout` records it, then the loop repeats.
```

If a `FINAL` prototype plan already exists, mark the old one superseded:
`> Superseded for build by docs/plans/YYYY-MM-DD-<project>-v1-full-spec.md`.

Then tell the builder, plainly: "Here's the full spec — the stack we picked, the standards now in
CLAUDE.md, and the build broken into [N] small phases. Next, run `/build` and I'll build **Phase 1
only**, then we test it, close it out, and come back for Phase 2." Remind them they can `/save-setup`
to start backing up now if they haven't.

## Append to PROJECT_HISTORY.md (required)

Format from `CLAUDE.md` Section 7. Title:
`## YYYY-MM-DD — Full-spec: Chose [stack], installed standards, broke the build into [N] phases`

- **What we did:** picked the stack via the decision questions; assembled standards into CLAUDE.md
  PART 2; broke the prototype into N small, testable phases.
- **Key decisions:** the stack and *why*; the standards template; what each phase covers; what's deferred.
- **Files changed/created:** `CLAUDE.md` (PART 2 appended), `docs/plans/...-v1-full-spec.md` (new, FINAL).
- **Open questions:** anything unresolved in the stack choice.
- **Next:** "Run `/build` to build Phase 1, then `/test`, then `/closeout`."
