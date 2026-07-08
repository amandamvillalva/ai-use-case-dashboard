---
name: closeout-step
description: Merged into /closeout. Run /closeout instead — it logs a finished phase and teaches it back, and wraps the project when every phase is done.
---

# /closeout-step — merged into /closeout

This command has been folded into **`/closeout`**. There's no longer a separate "step" version —
`/closeout` is context-aware and does the right thing on its own.

If someone runs `/closeout-step`, say, in plain language:

> "`/closeout-step` is now just `/closeout` — one closeout to remember. Run `/closeout` and I'll
> figure out the rest: after a phase, I log it and teach it back; once every phase is done, I wrap
> the whole project."

Then **stop** — don't log anything from here. Point them to `/closeout` and let it do the work.
