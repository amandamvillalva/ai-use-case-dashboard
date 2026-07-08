# AI Use Case Review Dashboard v0 — MVP Spec

**Status:** MVP
**Author:** Amanda Villalva & Stephanie Jimenez   **Date:** 2026-06-29
**Based on design:** docs/designs/2026-06-29-ai-use-case-dashboard-v0-design.md

## The one thing this proves

A People team member (or executive) can open a browser, see the current state of all AI use case
submissions at a glance — pipeline status, department breakdown, and Navi impact — pulled live from
the most recently uploaded Excel file.

## Build steps (each small, each verifiable)

1. **Set up the project and load the Excel data**
   — *you'll be able to:* run the app locally and see it print the correct row count and column
   names from the most recently uploaded file in `data/`.

2. **Build the Executive Summary section**
   — *you'll be able to:* open the dashboard in a browser and see the total submission count plus
   a status breakdown (Live, Approved, In Review, etc.) displayed as a donut or bar chart.

3. **Build the Department Breakdown chart**
   — *you'll be able to:* see a second chart below the summary showing how many submissions came
   from each Department/Team.

4. **Build the Navi Impact chart**
   — *you'll be able to:* see a third chart showing how many use cases are flagged
   "To be deleted with Navi launch," broken out clearly from the rest.

5. **Build the Use Case detail cards, grouped by department**
   — *you'll be able to:* scroll down and see use case cards organized by Department/Team, so all
   submissions from a given team appear together. Each card shows: name, status, description,
   expected time savings, recommendation, and score band (scored entries only).

6. **Add the Smartsheet submission link and final layout polish**
   — *you'll be able to:* see a clear "Submit a New Use Case" button linking to the Smartsheet
   form, and the full dashboard looks clean and readable enough to show to a leader.

## Data for the prototype

- Real data from `data/AI Use Cases.xlsx` — no stub or sample needed, the file is already in place.
- The app reads the most recently modified `.xlsx` file in the `data/` folder automatically.
- No secrets or credentials required — local file read only.
- Authentication (@moodys.com restriction) is deferred to the build phase.

## Explicitly not in the MVP

- No authentication or access control (deferred to full build + hosting decision)
- No search or filtering of use cases
- No email notifications or alerts
- No ability to submit, edit, or comment on use cases through the dashboard
- No mobile optimization
- No direct Smartsheet API connection (file export only)
