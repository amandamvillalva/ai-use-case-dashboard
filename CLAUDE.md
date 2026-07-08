# CLAUDE.md — The Project Brain

<!--
  This is the most important file in the project. Claude Code reads it automatically
  at the start of every session. It is the project's memory — Claude's memory resets
  between sessions, but this file does not. Everything Claude needs to behave like a
  senior engineer who has worked on THIS project before lives here.

  This is a STARTER brain. It begins generic. You make it yours by running
  /interview-me (fills in Section 8 — the project) and /full-spec (appends PART 2 —
  the engineering standards for your chosen stack). You don't need to hand-edit anything.
-->

## 1. What this project is

<!-- /interview-me fills this in. Until then it holds a placeholder. -->

**This project is:** A file-driven internal dashboard that lets the Moody's People team see the status and department breakdown of AI use case submissions reviewed by the AI Use Case Review Committee.

Whatever it turns out to be, every app you build has the same three layers, and it helps to keep them straight:

- **Data** — the information the app works with (a CSV, a database, a file, an API you call).
- **Logic** — the code that loads, transforms, and decides what to do with that data.
- **Interface** — what a human (or another system) actually interacts with.

**One honest principle, kept from how we learned to build:** know whether the AI is in the *building* or in the *running*. Claude Code (you) is the engineer who builds this. That's always true. Whether the finished app *itself* calls an AI model at runtime is a real design decision — some projects should, many shouldn't. If this app does call an LLM or any other API at runtime, that's fine — just be deliberate about it, and keep every key in `.env` (Section 9, rule 4). Don't add AI to the running app by reflex; add it when it earns its place.

## 2. Read this first, every session

**Before doing anything in a session, read these two files in order:**

1. **This file (`CLAUDE.md`)** — what the project is, the rules, the chosen stack.
2. **`PROJECT_HISTORY.md`** — the journal of what's been done so far. Read the **last 2–3 entries** to know where the project stands. If it has no real entries yet, this is a brand-new project and you're starting from the beginning.

Do not start writing code or asking questions until you've read both. If Section 8 is still full of placeholders, your first suggestion should be: "Run `/interview-me` so I know what we're building." If the person seems unsure what to do at any point, suggest `/guide`.

## 3. The lifecycle

Projects are built by walking this lifecycle. Each step has a slash command. **The steps build on each other — prove the idea cheaply before you build it well.**

| # | Step | Command | Produces |
|---|------|---------|----------|
| 1 | Set up | `/interview-me` | A project-specific CLAUDE.md and the first history entry |
| 2 | Brainstorm | `/brainstorm` | A design doc in `docs/designs/` (what we're building and why) |
| 3 | Plan | `/mvp-spec` | An MVP plan in `docs/plans/` (status: `MVP`) — the smallest version that proves the idea |
| 4 | Prototype | `/prototype` | A working v0, iterated until you're happy |
| 5 | Full-spec | `/full-spec` | Stack chosen, engineering standards installed, the build broken into small phases — produces a `FINAL` plan |
| 6 | Build | `/build` | The next phase, built for real — **requires a `FINAL` plan** |
| 7 | Test | `/test` | The phase verified — by hand and with real tests |
| 8 | Closeout | `/closeout` (+ `/teach-me`) | The phase recorded; learnings captured |

**Save your work as you go** with the version-control commands — `/save-setup` (once), `/publish` (once), then `/save` whenever you finish a piece of work. **`/closeout-step`** logs a milestone to `PROJECT_HISTORY.md` any time. **`/guide`** tells you where you are and what to do next, and lets you choose how hands-on you want Claude to be.

**The discipline this lifecycle teaches:** Brainstorm → Plan (MVP) → Prototype ↔ iterate → (show one person) → lock a FINAL plan → Build → Test → Closeout, one phase at a time. You prove a direction *cheaply* with a prototype before committing to build it *well*. `/build` will refuse to run until a `FINAL`-status plan exists. That refusal is a feature, not a bug — it's what keeps a vibe-coded project from sprawling into something no one can maintain.

## 4. Tech stack — choose deliberately, and stay in the lane

Unlike a course, there's no session gate here — you can build the whole thing. But there **is** one deliberate constraint, and it's worth keeping: **stay within two language families, and the frameworks we know.**

| Family | Frameworks we support | Good for |
|--------|----------------------|----------|
| **Python** | **Flask** (a small web app + API) · **Streamlit** (fastest path for data/analytics tools) | Read-mostly tools, data/analytics-heavy work, internal tools, teams that lean Python |
| **JavaScript** | **React / Next.js** | Highly interactive, app-like screens; polished, consumer-grade products; teams that lean JS |

**Why the constraint?** Picking from a small, shared set keeps projects reviewable and maintainable long after the hackathon — anyone who knows the house stack can pick up anyone else's project. A sprawl of exotic frameworks is how internal tools become orphaned. `/full-spec` walks you through choosing among these with five plain-English questions. **If you have a genuine reason to go outside this set, you can** — but say why in the spec, so the next person understands the call. Default when unsure: **Python + Flask.**

**Storage is open-ended.** This starter ships with no database. Your project might read a CSV, use a local SQLite file, connect to your own database, or call a SaaS API — all fine. Whatever it is, the connection details and keys go in `.env`, never in code (Section 9).

## 5. File conventions

| What | Where it goes |
|------|---------------|
| Design docs (`/brainstorm` output) | `docs/designs/YYYY-MM-DD-<project>-v0-design.md` |
| Plans (`/mvp-spec`, `/full-spec` output) | `docs/plans/YYYY-MM-DD-<project>-v0-spec.md`, `…-v1-full-spec.md` |
| The app itself | At the repo root (or in the structure your chosen stack expects — `/full-spec` sets this) |
| Data files (if any) | `data/` |
| Secrets (connection strings, API keys) | `.env` at the repo root — **never committed** (it's in `.gitignore`) |
| Session journal | `PROJECT_HISTORY.md` (repo root) |

Always use `YYYY-MM-DD` in filenames. Get today's date from the system if unsure — don't guess.

## 6. When to use plan mode

Plan mode means: **say what you're about to do, in plain language, and wait for approval — before you touch any code.** Use it:

- Before **any** code change longer than ~5 lines.
- Before creating **any** new file.
- Before **any** structural change (moving things, renaming, changing how data flows).
- Whenever you're unsure what the person actually wants.

A good plan is a short numbered list a non-technical person can read and say "yes, do that" or "no, not that." See the `plan-mode-discipline` skill for what good and bad plans look like.

## 7. How to update PROJECT_HISTORY.md

**Hard rule: at the end of every meaningful step, append one entry to `PROJECT_HISTORY.md`.** Append to the bottom; never overwrite earlier entries. Use exactly this format:

```markdown
## YYYY-MM-DD — [Step Name]: [One-line summary]

**What we did:** 2–4 sentences in plain language.
**Key decisions:** Bulleted list of decisions (or "None").
**Files changed/created:** Bulleted list with relative paths.
**Open questions:** Bulleted list (or "None").
**Next:** One sentence pointing to the next step.
```

There's a worked example at the top of `PROJECT_HISTORY.md` — copy its shape. See the `updating-project-history` skill for good vs. lazy entries.

## 8. Project context

<!--
  This section is filled in by /interview-me. Until then it holds placeholders.
  If you (Claude) see placeholders here, your first move in any session is to
  suggest the person run /interview-me.
-->

- **What we're building:** An internal web dashboard that reads a regularly-refreshed Smartsheet data export and displays a high-level view of AI use case submissions — their status and distribution across departments.
- **The problem it solves:** The AI Use Case Review Committee's Smartsheet dashboard is not visible to others; the broader People team has no way to see where use cases stand or how many are being worked on by department.
- **Who it's for:** The entire Moody's People team (internal, @moodys.com users only); read-only access.
- **The one core thing it must do:** Show a clean, easy-to-read view of AI use case pipeline status and department-level breakdown, always using the most recently uploaded data file.
- **Constraints / must-nots:** Accessible to @moodys.com users only — not public. Data sourced from a file dropped into a folder (refreshed 1–2x per week); app always picks up the most recent file. No raw data dumps or overwhelming detail — high-level overview only. No editing of source data. No AI at runtime.
- **Who's building it:** Amanda (amanda.villalva@moodys.com) and Stephanie (stephanie.jimenez@moodys.com), both on the People team. Amanda is new to building apps; wants each step explained clearly before moving forward. Guided mode.

Once filled, use this to anchor every suggestion. Match the builder's working style. Keep examples and language in their domain. This context is *why* the scaffolding produces senior-engineer-quality output instead of generic slop.

## 9. Hard rules

These are not suggestions. Follow them every time.

1. **ALWAYS read `PROJECT_HISTORY.md` at the start of a session** before doing anything else.
2. **ALWAYS append a `PROJECT_HISTORY.md` entry at the end of any meaningful step**, in the exact format above.
3. **When unsure, ASK before generating code.** A 10-second clarifying question beats 50 lines of wrong code. Treat the person as a serious operator, not a coder — explain the *why* in plain language, never condescend.
4. **NEVER put secrets in code, prompts, or any committed file.** Connection strings, API keys, tokens, passwords — all go in `.env`, which is git-ignored. A secret is like a key to the building; you'd never tape it to the front door. This applies fully to any AI/API keys if the app calls a model at runtime.
5. **Stay in the supported stack** (Section 4) unless the spec records a clear reason to go outside it.
6. **`/build` requires a `FINAL` plan.** If the most recent plan is `MVP` or `SUPERSEDED`, refuse and point back to `/prototype` → `/full-spec`.
7. **Write code a beginner can read.** Comment the *why*, not just the *what*. Small functions. Clear names. No cleverness for its own sake.
8. **Read what you produce — you own the output.** Claude can be confidently wrong, won't know the business unless told, and matches patterns that sometimes don't fit. Surface uncertainty; don't bluff.
9. **If this tool will be used by real people at Moody's, it needs governance.** Vibe-coded doesn't mean ungoverned. Tools that go beyond personal/experimental use get assigned a risk tier (Self-Managed → Guided → Co-Built → IT-Delivered) with requirements that scale to the risk. When a project looks headed for real users or sensitive data, say so plainly and point the builder to Moody's Maker governance process. Don't invent the specifics — just don't let a real tool ship as if it were a toy.
