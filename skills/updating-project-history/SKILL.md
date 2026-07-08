---
name: updating-project-history
description: When to append to PROJECT_HISTORY.md, the exact entry format, and what separates a useful entry from a lazy one. This is the connective tissue across every work session.
triggers:
  - At the end of any meaningful step or work block
  - When finishing a slash command (interview-me, brainstorm, plan, prototype, etc.)
  - Before stopping for the day
---

# Updating PROJECT_HISTORY.md

`PROJECT_HISTORY.md` is the project's journal. It exists because your memory resets
between sessions — the journal is how the next session (or the next person) knows exactly
where things stand. It is the connective tissue that turns many separate work sessions into
one continuous engineering story. **Keeping it current is a hard rule, not a nicety.**

## You should

- **Append an entry at the end of every meaningful step.** Every lifecycle command ends with one. A "meaningful step" is anything that changed the project or a decision — a design, a plan, a build, a fix, the end of a work session.
- **Append to the bottom. Never overwrite earlier entries.** History is append-only. The old entries are the record of how you got here.
- **Use the exact format** (it's in `CLAUDE.md` Section 7 and demonstrated at the top of `PROJECT_HISTORY.md`):

```markdown
## YYYY-MM-DD — [Step Name]: [One-line summary]

**What we did:** 2–4 sentences in plain language.
**Key decisions:** Bulleted list (or "None").
**Files changed/created:** Bulleted list with relative paths.
**Open questions:** Bulleted list (or "None").
**Next:** One sentence pointing to the next step.
```

- **Get today's real date from the system.** Don't guess or reuse a stale date.
- **Write it so a stranger could resume.** The reader is future-you with no memory. Name the actual files, the actual decisions, the actual next move.

## You should not

- Skip the entry because "it was a small change." Small changes are exactly what gets forgotten.
- Write vague filler. "Made some updates" tells the next session nothing.
- Bury a real decision. If you chose to trust the CSV's date column instead of recomputing it, that belongs in **Key decisions** — it's the kind of thing someone will need to know later.

## Example — a GOOD entry

```markdown
## 2026-05-31 — Prototype: Built v0 MVP and proved the direction

**What we did:** Built the open-reqs table from the sample CSV, sorted by days_open
descending. Iterated three times: colored the priority column, added an "All / Active
only" toggle, and widened the role-title column. The learner showed it to a teammate,
then locked the final plan.
**Key decisions:** Priority colors (High=red, Medium=amber, Low=gray). Kept v0 read-only.
Defaulted the toggle to "Active only" because that's what they look at most.
**Files changed/created:** index.html, style.css, app.js (all new);
docs/plans/2026-05-31-project-v1-full-spec.md (new, FINAL);
docs/plans/2026-05-30-project-v0-spec.md (status → SUPERSEDED).
**Open questions:** None.
**Next:** Run /full-spec to choose the stack and phase the build, then /build.
```

Why it's good: a stranger could open the project tomorrow and know exactly what exists,
why each choice was made, and what to do next.

## Example — a LAZY entry

```markdown
## 2026-05-31 — Prototype: did the prototype

**What we did:** Built the app and made some changes.
**Key decisions:** None.
**Files changed/created:** a few files.
**Next:** keep going.
```

Why it's bad: no filenames, no decisions captured (there clearly were some), no real next
step. The next session learns nothing and has to re-derive everything. Never write this.

## The test

Read your entry as if you'd never seen this project. **Could you pick it up from just this
entry and the ones above it?** If not, add what's missing before you move on.
