# PROJECT_HISTORY.md — The Project Journal

This file is the running story of how this project got built. Every meaningful step adds one entry to
the bottom. It exists because Claude Code's memory resets between sessions — this journal is how the
next session (or the next person, or future-you) picks up exactly where the last one left off.

**How to read it:** newest entries are at the bottom. To know where the project stands right now, read
the last 2–3 entries.

**How to write it:** every entry uses the same format. There's a worked example directly below — copy
its shape exactly. Append new entries; never overwrite old ones.

---

## Entry format (every entry looks like this)

```markdown
## YYYY-MM-DD — [Step Name]: [One-line summary]

**What we did:** 2–4 sentences in plain language.
**Key decisions:** Bulleted list of decisions (or "None").
**Files changed/created:** Bulleted list with relative paths.
**Open questions:** Bulleted list (or "None").
**Next:** One sentence pointing to the next step.
```

---

<!--
  ↓↓↓ FIRST REAL ENTRY GOES BELOW THIS LINE ↓↓↓
-->

## 2026-06-29 — Setup: Defined the project and personalized CLAUDE.md

**What we did:** Interviewed Amanda and Stephanie about what they're building. The project is an internal dashboard for the Moody's People team that surfaces AI use case pipeline status and department-level submission counts, driven by a Smartsheet data export dropped into a folder 1–2x per week. The existing Smartsheet dashboard is not visible outside the review committee, so the People team has no visibility into where things stand.

**Key decisions:**
- Core capability: show use case status and department breakdown using the most recently uploaded data file.
- Access restricted to @moodys.com users only — not public-facing.
- High-level overview only; no raw data dumps, no editing of source data, no AI at runtime.
- Data source is a file dropped into a folder (not a live Smartsheet API connection) for simplicity.
- Guided working mode — explain each step before moving forward.

**Files changed/created:**
- `CLAUDE.md` (Sections 1 and 8 updated)

**Open questions:**
- ~~What file format will the Smartsheet export be?~~ **Confirmed: Excel (.xlsx)**
- ~~Which specific data fields/columns are in the export?~~ **Confirmed: 58 columns, 75 rows. Key fields for dashboard: Use Case ID, Status, Requestor Name, Requestor Email FINAL, Department/Team, Use Case Name, Category, Recommendation, Total Score, Band, Lead Reviewer, Target Go-Live Date, Comments/Progress Notes. `#INVALID VALUE` in Band/Score = unreviewed entries — exclude from all scoring metrics and reporting.**
- ~~Where will the folder live?~~ **Confirmed: `data/` folder in the project**
- How will @moodys.com-only access be enforced? (May need an authentication layer or Moody's hosting.)

**Next:** Run `/brainstorm` to design v0 of the dashboard.

## 2026-06-29 — Brainstorm: Designed v0 of the AI Use Case Review Dashboard

**What we did:** Designed the v0 dashboard for the Moody's People team and executive leaders. The dashboard is read-only and shows overall pipeline status (total submissions + status breakdown with charts), a department-level breakdown chart, and individual use case detail cards including agent descriptions and expected time savings. A "Submit a New Use Case" button links out to the existing Smartsheet form.

**Key decisions:**
- Focal point: overall pipeline status first (counts + status chart), then department breakdown — this is what executives see first.
- Two layers: executive summary at the top, individual use case details below.
- Charts and visual graphs required — not a plain data table.
- Strictly read-only; all submissions go through the Smartsheet form link.
- Data source: Excel file in `data/` folder; app always reads the most recently uploaded file.
- `#INVALID VALUE` entries (unreviewed cases) excluded from scoring metrics but included in status counts.

**Files changed/created:**
- `docs/designs/2026-06-29-ai-use-case-dashboard-v0-design.md` (new)

**Open questions:**
- How will @moodys.com-only access be enforced? (Depends on hosting — governance consideration.)
- Some entries are marked "To be deleted with Navi launch" — should these be hidden or shown with a distinct status?
- File naming convention for the Excel export — will it always be the same name, or will the app need to sort by modification date?

**Next:** Run `/mvp-spec` to turn this design into an MVP build plan.

## 2026-06-29 — MVP Spec: Planned the smallest version that proves the idea

**What we did:** Scoped the design down to a 6-step MVP plan. The prototype will load real data from the Excel file in `data/`, render an executive summary with a status chart, a department breakdown chart, a Navi impact chart, and individual use case detail cards — all in a clean, browser-viewable layout with a Smartsheet submission link.

**Key decisions:**
- Using real data from the start (no stubs needed — file is already in place).
- App always reads the most recently modified `.xlsx` file in `data/` automatically.
- Authentication deferred to the full build phase.
- Filtering, search, and mobile optimization cut from MVP — iterate later.
- 6 steps, each ending in something visible and verifiable.

**Files changed/created:**
- `docs/plans/2026-06-29-ai-use-case-dashboard-v0-spec.md` (new, status: MVP)

**Open questions:**
- Authentication approach still to be resolved (depends on hosting environment).

**Next:** Run `/prototype` to build the working v0.
