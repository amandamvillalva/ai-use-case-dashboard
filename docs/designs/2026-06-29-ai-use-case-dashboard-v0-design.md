# AI Use Case Review Dashboard v0 — Design

**Author:** Amanda Villalva & Stephanie Jimenez   **Date:** 2026-06-29

## Problem

The AI Use Case Review Committee tracks all submitted use cases in Smartsheet, but that dashboard is
not visible to the broader People team or executive leaders. There is no way for stakeholders to see
how many use cases have been submitted, where they stand in the review process, or what the approved
agents actually do — without being given direct Smartsheet access.

## Who it's for

The entire Moody's People team, including executive leaders. Read-only. Accessible to @moodys.com
users only.

## What it does / shows

**Section 1 — Executive Summary (top of page)**
- Total number of use cases submitted
- Breakdown by status (e.g. Live, Approved, In Review, On Hold, Rejected)
- Visual status chart (e.g. donut or bar chart showing pipeline at a glance)
- Prominent "Submit a New Use Case" button linking to the Smartsheet form

**Section 2 — Department Breakdown**
- Chart showing how many submissions came from each Department/Team
- Makes it easy for leaders to see which parts of the org are most active

**Section 3 — Navi Impact View**
- Separate chart showing how many use cases are flagged "To be deleted with Navi launch"
- Gives leaders visibility into what will sunset when Enterprise Navigator goes live, without hiding those entries from the overall counts

**Section 4 — Use Case Details**
- Browsable list/cards of individual use cases with:
  - Use Case Name
  - Department/Team
  - Status
  - Description of what the agent does
  - Expected time savings
  - Recommendation (Approved / Not approved)
  - Score Band (P1, P2, etc.) — only shown for reviewed cases
  - Target Go-Live Date
- Excludes entries with no score/review data (`#INVALID VALUE`) from scored metrics

## The one thing that matters most

**Overall pipeline status** — the first thing a leader sees is a clear count of total submissions and
where they all stand (how many are live, approved, in review, etc.), followed immediately by the
department breakdown chart.

## Where the data comes from

- Source: Excel file (`AI Use Cases.xlsx`) exported from Smartsheet, dropped into the `data/` folder
- The app always reads the **most recently uploaded file** in that folder
- File is refreshed 1–2 times per week by the committee
- No secrets or credentials required for the data source (local file read)
- @moodys.com-only access enforcement: to be determined during build (likely requires Moody's hosting
  or an authentication layer)

## Success looks like

A People team member or executive opens the dashboard and within 10 seconds can answer:
- How many AI use cases have been submitted total?
- How many are live / approved / still in review?
- Which departments are most active?
- What does a specific agent actually do and how much time will it save?

## Non-goals (v0)

- No ability to submit, edit, or update use cases through the dashboard — users are directed to the
  Smartsheet form for submissions: https://app.smartsheet.com/b/form/019e46b887db7c1daebcc0c306b509f4
- No user commenting, voting, or feedback features
- No email notifications or alerts
- No filtering or search (may come in v1 if needed)
- No direct Smartsheet API connection — data comes from the manually refreshed Excel export

## Notes / unknowns

- Authentication: how @moodys.com-only access is enforced depends on where the app is hosted —
  needs to be resolved before shipping to the People team (governance consideration)
- `#INVALID VALUE` in the Band and Total Score columns means the use case has not yet been reviewed;
  these entries are excluded from all scoring metrics but still shown in status counts
- Entries marked "To be deleted with Navi launch" are included in all counts but broken out in a
  dedicated Navi Impact chart so leaders can see what will sunset when Enterprise Navigator launches
- File naming: if Smartsheet exports with a consistent filename, the "most recent file" logic will
  need to sort by file modification date or a timestamp in the filename
