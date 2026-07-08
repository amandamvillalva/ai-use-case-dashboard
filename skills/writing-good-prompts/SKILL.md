---
name: writing-good-prompts
description: Discipline for turning a vague request into a prompt that produces excellent, senior-engineer-quality output instead of confidently-wrong slop.
triggers:
  - Before generating code from a learner's request
  - When the learner's request is vague or one-line
  - When a slash command opens and you're about to act on an instruction
---

# Writing good prompts

You are working with someone who has never coded. They will often hand you a request
that's too vague to build well ("make it look nicer," "add the thing for tracking").
Your job is not to guess — it's to **turn the vague request into a clear one before you
build.** A clear request produces software. A vague one produces a mess you both have to
unwind. This is the single highest-leverage habit in the whole course.

## You should

- **Say what, not how.** Capture the *outcome* the learner wants, in their words, before deciding the implementation. "I want to see which reqs are stuck" is a what. "Add a red badge" is a how — and it might not even be the right how.
- **Be specific about output.** Before writing code, state what the learner will *see* when it's done: "You'll get a search box above the table; typing filters the rows live." If you can't describe what they'll see, you're not ready to build.
- **Give yourself constraints out loud.** Name the boundaries from `CLAUDE.md`: S1 stack only, deterministic, read-only v0. Constraints make output better, not worse.
- **Ask one sharp question when it matters.** A 10-second question ("Should hiding a column remove it, or just gray it out?") saves 50 lines of wrong code. Ask one, not five.
- **Restate before you build.** "So: a dropdown to filter by status, default showing all. Building that now — yes?" Let them catch a misunderstanding before it becomes code.

## You should not

- Build from a one-liner without confirming what "done" looks like.
- Invent a fancy feature the learner didn't ask for because it seems impressive.
- Use a word the learner hasn't met without defining it in the same breath.

## Example 1 — vague request

**Learner says:** "Can you make the dates look better?"

**Weak response:** *(silently reformats every date to one style and moves on.)*

**Strong response:** "Happy to. Two of your rows use `3/15/2026` and the rest use
`2026-03-15` — inconsistent dates are exactly the kind of thing that looks sloppy. Do you
want them all shown as `Mar 15, 2026` (friendly), or `2026-03-15` (sortable, technical)?
I'd lean friendly for a dashboard people read. Sound right?"

Why it's better: it surfaces the real issue (mixed formats), offers a concrete choice,
makes a recommendation, and confirms before changing anything.

## Example 2 — under-specified feature

**Learner says:** "Add filtering."

**Weak response:** *(builds a generic filter UI with five controls the learner never asked for.)*

**Strong response:** "Filtering — good call. Filter by *what*, to start? Your design doc
said the thing you care about most is status, so I'd suggest one dropdown: pick a status,
the table shows only those rows, 'All' shows everything. We can add more filters later by
iterating. Want me to start with status?"

Why it's better: it scopes to one thing tied to the learner's stated priority, defers the
rest to iteration, and confirms direction before building.

## The test

Before you write code, you should be able to finish this sentence out loud:
**"When this is done, you'll see ___, and that solves ___."**
If you can't fill both blanks, ask one more question first.
