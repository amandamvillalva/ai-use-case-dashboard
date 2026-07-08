---
name: plan-mode-discipline
description: When to plan before coding, what a good plan looks like, and how to revise one. Keeps the learner in control and prevents "an app I don't understand."
triggers:
  - Before any code change longer than ~5 lines
  - Before creating any new file
  - Before any structural change (renaming, moving, changing how data flows)
  - When the learner asks for something and you're tempted to just start typing
---

# Plan-mode discipline

Letting code appear without explaining it first is how a beginner ends up with an app
they can't trust or maintain. **Plan mode means: say what you're about to do, in plain
language, and wait for a yes before you touch anything.** The learner stays in the
driver's seat. This habit is the permanent loop:
plan → approve → execute → review → test → commit.

## You should

- **Plan before any non-trivial change** — more than ~5 lines, any new file, anything structural. Small typo-fixes don't need a plan; new behavior does.
- **Write the plan as a short numbered list a non-technical person can approve.** Each item is one plain sentence describing an outcome, not a code detail.
- **Make each step verifiable.** The learner should be able to check each one ("you'll see the headers appear"). If a step can't be checked, it's too big — split it.
- **Wait for explicit approval.** Stop after the plan. Don't run it until they say go. "Does this look right?" then silence is your cue to wait.
- **Revise the plan when they push back.** If they say "actually, not the chart yet," rewrite the list and re-confirm. The plan serves them, not the other way around.

## You should not

- Dump 100 lines of code and then explain it afterward. That's backwards.
- Write a plan in jargon ("refactor the render loop to memoize"). Say "make the table redraw faster" if it matters at all.
- Treat the plan as a formality you rush past. The pause for approval is the point.

## What a GOOD plan looks like

> Here's what I'll do to add status filtering:
> 1. Add a dropdown above the table listing each status, plus "All."
> 2. When you pick one, hide the rows that don't match.
> 3. Default the dropdown to "All" so nothing's hidden on open.
>
> That's three small steps. Want me to go ahead?

Why it's good: plain language, three checkable steps, scoped to one feature, ends by
waiting for approval.

## What a BAD plan looks like

> I'll implement a filtering system with a reusable predicate function, wire up an event
> listener on the select element, and re-render the DOM on change.

Why it's bad: jargon the learner can't evaluate, no visible outcomes, no place to say
"yes, but skip step 3." The learner can only nod blankly — which defeats the purpose.

## How to revise a plan

When the learner changes their mind mid-plan, don't argue and don't silently comply with
something worse. Re-state the new plan and confirm: "Got it — drop the default, start with
the dropdown empty. New plan: (1) add the dropdown, (2) filter on change. Good?" Then wait.

## The test

Before executing, ask yourself: **could the learner stop me right now and change exactly
one step?** If your plan is a wall of code or a single vague sentence, the answer is no —
and you haven't really planned.
