# Base Engineering Standards (stack-agnostic)

These standards apply **no matter which stack you chose**. `/full-spec` folds this file together with
your stack template (`python.md` or `react.md`) to write the `PART 2 — Engineering Standards` section
of your `CLAUDE.md`. Every `/build` then writes code to these standards.

Keep them in plain sight; they're written to be read by a non-engineer.

## The non-negotiables (these match CLAUDE.md's hard rules)

- **No secrets in code, ever.** Database connection strings, passwords, and API keys — including any
  AI/model API keys — live in a `.env` file, read at runtime, never typed into code, docs, or a
  `PROJECT_HISTORY.md` entry. `.env` is git-ignored. A secret is a key to the building; you don't
  tape it to the front door.
- **Be deliberate about runtime AI.** The AI (Claude Code) helps *build* your app — that's always
  true. Whether the finished app *itself* calls an AI model at runtime is a real design choice. If it
  does, that's fine: keep the key in `.env`, handle the failure and latency cases, and don't put
  sensitive data into a model that shouldn't see it. If it doesn't need AI to run, don't add it by
  reflex — deterministic code is simpler to trust and maintain.
- **Write code a beginner can read.** Small functions. Clear, descriptive names. Comments that
  explain the **why**, not just the what. No cleverness for its own sake.
- **Stay in scope.** Build only the current phase. Don't add features, integrations, or polish that
  the current phase doesn't call for.

## Code quality

- **One job per function.** If a function does three things, it's probably three functions.
- **Name things for what they are.** `load_overdue_contracts()` beats `getData()`. A reader should
  guess what a name does before reading the body.
- **Comment the intent.** `# We trust the source's date column as-is for now; validate in a later
  phase` tells the next person *why*. `# loop over rows` does not.
- **Fail loudly and clearly.** When something goes wrong (a missing file, a bad input, a wrong
  address, an unreachable service), show a clear message — not a blank screen and not a stack-trace
  crash. "Couldn't reach the database — check your .env" beats a 500 error page.
- **Don't repeat yourself.** If the same block appears twice, lift it into one named helper.

## Project shape

- **Keep the three layers visible.** The screen (frontend), the logic/server (backend), and the data
  (a file, a database, an API — wherever it lives) stay in separate, obvious places. Part of building
  well is *seeing* the seams.
- **Data and config live in known places.** Data files in `data/`; secrets in `.env`; never pasted
  into code.
- **Tests live with the code** (`tests/` for Python, alongside components or `tests/` for React).

## How tests fit the loop

- Testing is **how you know it works**, not a chore bolted on at the end.
- Every phase ends with a **by-hand check** of its success criterion (open it, click it, confirm).
- The build closes with **unit tests** — a few small, repeatable checks that run with one command and
  cover the things that matter (the core read works; a good action succeeds; a bad input is rejected
  and changes nothing). Aim for *meaningful* coverage, not 100%.
- **Tests never touch live external systems** — not a production database, a billable API, or
  anything shared. Use a test double (a small in-memory fake) so the suite is safe to run a thousand
  times.
- The healthy rhythm for any real build (and the hackathon): **Build → Test → Closeout, one phase at
  a time.**

## How the build loop stays on track

- `PROJECT_HISTORY.md` is the project's memory and the **only record of where the build loop is.**
- `/build` reads it to find the next unbuilt phase. `/closeout` writes the entry that marks a phase
  done. Never skip the history write — without it, the next build doesn't know where to pick up.
- Keep entries honest and specific: name the real files and the real decisions.

## Error handling, in plain terms

- Anticipate the obvious bad input for each phase (a wrong web address, a blank required field, an
  empty data file, an unreachable service) and handle it with a clear message.
- A good rule: **the app should never show the user a crash.** If something fails, it should say, in
  words a person understands, what went wrong and (ideally) what to do next.
