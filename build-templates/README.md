# build-templates/ — where your engineering standards come from

This folder ships with the project starter kit. You don't edit these files by hand and you
don't run them. They're **source material**: when you run `/full-spec`, Claude reads the right
ones and assembles them into a new `PART 2 — Engineering Standards` section at the bottom of your
`CLAUDE.md`. From then on, every `/build` writes code to that standard.

## What's in here

| File | What it is | When it's used |
|---|---|---|
| `base.md` | Stack-agnostic standards that always apply (readable code, no secrets in code, no runtime LLM, how tests fit the loop) | **Always** — folded in for every stack |
| `python.md` | Standards for the **Python** path (Flask or Streamlit), including pytest | When you pick **Python + Flask** or **Streamlit** |
| `react.md` | Standards for the **React/Next.js** path, including Vitest | When you pick **React/Next.js** |

## How `/full-spec` uses them

1. Reads `base.md` (always).
2. Reads the template for the stack you chose (`python.md` **or** `react.md`).
3. Fills in this project's real values (the run command, the test command, the data table) so the
   standards are concrete, not generic.
4. Appends the result to `CLAUDE.md` as `PART 2 — Engineering Standards`.

You only need the template for the stack you actually pick — but keeping all of them here means
you can change your mind, or build a second project on the other stack later, without hunting for
files.

> If `/full-spec` ever says it can't find `build-templates/`, it means this folder isn't in your
> project folder yet. Copy it back in from the starter kit and run `/full-spec` again.
