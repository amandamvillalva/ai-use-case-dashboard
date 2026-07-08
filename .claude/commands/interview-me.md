---
name: interview-me
description: Interview the builder about the project they want to build, and personalize CLAUDE.md Section 8 with that context. Step 1 of the lifecycle — run it first.
---

# /interview-me — Step 1: Set up (define the project)

You're about to interview the builder **about the project they want to build** — the problem, the
user, the one core thing it must do. The goal is to fill in Section 8 of `CLAUDE.md` so that for the
rest of the project you build like an engineer who understands what this is and who it's for.

This is grounded in how the course taught design: **start with the problem, not the solution.** Don't
let the conversation jump to "let's build X with Y" before you understand what's actually being solved.

## Read this first

1. Read `CLAUDE.md`, especially Section 8 (Project context) — that's what you're filling in.
2. Read `PROJECT_HISTORY.md`. If the only dated entry is the example block, this is a brand-new
   project with no real history yet.

## How to behave

- Ask the questions below **one at a time.** Wait for each answer before asking the next. Never dump
  them all at once — that overwhelms.
- Keep it warm and short. You're a friendly senior colleague helping someone shape an idea.
- After each answer, reflect it back in one line so they know you heard it.
- **Push gently on vague answers** — but only once each. "An app for my team" isn't a problem
  statement; "my team rebuilds the same status report every Monday by hand" is. If they're vague,
  ask one sharpening follow-up, then move on.
- Don't start designing here. That's `/brainstorm`. This is about understanding the project and who's
  building it.

## The questions (ask one at a time)

1. **"In one or two sentences — what are you trying to build, and what problem does it solve?"**
   *Push if vague.* Good: "A page that shows my team which vendor contracts are past their review
   date, so we stop missing renewals." Bad: "A contracts tool." If they lead with a solution
   ("I want a dashboard"), ask: "What problem would that dashboard fix for you?"

2. **"Who's it for? Just you, your team, a whole department — or people outside Moody's?"**
   *Why:* this shapes how polished and self-explanatory it must be, and whether governance matters
   (see the note at the end).

3. **"If it could only do ONE thing well, what would that be? The single capability that makes it
   worth building."**
   *Why:* this becomes the core of the MVP. Get one clear answer, not a list.

4. **"Is there anything it must avoid, must integrate with, or must stay within? Existing data, a
   system it has to talk to, a rule it can't break, something it should explicitly NOT do?"**
   *Why:* constraints and non-goals are the most useful thing you can capture early. Includes whether
   it needs to call an AI model, connect to a database or SaaS tool, etc.

5. **"Who's building it — just you, or a team? And how do you like to work: want me to explain every
   step, or move fast and tell you the important bits?"**
   *Why:* capture working style and team so you honor it the whole way through.

## What to produce

**Update `CLAUDE.md` Section 8 (Project context)** in place — replace each placeholder with the real
answer, keeping the bullet labels. **Also fill in Section 1's one-line "This project is:"** with a
clean one-sentence description drawn from answer 1. Example result for Section 8:

```markdown
- **What we're building:** A web page that flags vendor contracts past their review date.
- **The problem it solves:** The team misses renewal windows because no one view shows what's overdue.
- **Who it's for:** The vendor-management team (4 people); the lead reviews it weekly.
- **The one core thing it must do:** Show every contract sorted by how overdue its review is.
- **Constraints / must-nots:** Reads from the existing contracts export; no editing the source system; no AI at runtime.
- **Who's building it:** Jordan (solo); wants the "why" but kept brief; learns by seeing it.
```

Then confirm in plain language: "I've saved this to the project's brain. From now on I'll build with
this in mind. Ready to design it? Run `/brainstorm`." If the project sounds like it'll be used by real
people or touch sensitive data, add one calm line: "Heads-up — since real people will use this, it'll
likely need a governance tier later; I'll flag that when we get closer to shipping."

## Append to PROJECT_HISTORY.md (required)

Use the exact format from `CLAUDE.md` Section 7. Title it:
`## YYYY-MM-DD — Setup: Defined the project and personalized CLAUDE.md`

- **What we did:** one or two sentences naming the project, the problem, and who it's for.
- **Key decisions:** the one core thing; key constraints/non-goals; working-style preference.
- **Files changed/created:** `CLAUDE.md` (Sections 1 and 8).
- **Open questions:** anything still fuzzy.
- **Next:** "Run `/brainstorm` to design v0."

This is the project's first real entry. **Delete the example block** (everything from the
`⬇️ EXAMPLE ENTRY` marker through the `⬆️ END EXAMPLE ENTRY` marker, inclusive) now — it has served
its purpose — and write this entry below the `FIRST REAL ENTRY GOES BELOW` marker.
