# Project Starter Kit

You just downloaded this. Here's what it is in 90 seconds.

## What is this folder?

It's a **starter kit for building almost anything with Claude Code** — the same brain, journal, and
process you used in the Vibe Coding bootcamp, but generalized so you can spin up a *new* project of
your own. Drop this folder into Claude Code, run one command, and you have a senior-engineer workflow
around you from the first minute.

You build *with* Claude Code. Claude is the engineer; you decide what gets built. This folder is
already set up so Claude knows how to help you well.

## What's inside

- **`CLAUDE.md`** — the project's *brain*. Claude reads it at the start of every session. It starts
  generic and becomes yours when you run `/interview-me`.
- **`PROJECT_HISTORY.md`** — the project's *journal*. Every step gets logged here so you (and Claude)
  always know where things stand.
- **`.claude/commands/`** — the *process*: slash commands for every step of building software.
- **`skills/`** — habits Claude applies automatically (planning before coding, reading diffs, keeping
  the journal honest, writing good prompts).
- **`build-templates/`** — the engineering standards `/full-spec` installs once you pick a stack.
- **`.gitignore` + `.env.example`** — set up so your secrets stay out of your code from hour one.

## How do I start?

1. **Open this folder in Claude Code** (the desktop app). Point Claude Code at this folder — it reads
   the setup automatically.
2. **Type `/` to see the commands.** Those are the steps of building software, one command each.
3. **Run `/guide`** if you're ever unsure what to do — it tells you where you are and what's next, and
   lets you choose how hands-on you want Claude to be.
4. **The very first thing to run is `/interview-me`** — it asks a few questions about what you're
   building so Claude can help like it knows your project.

See **`COMMANDS.md`** for the full list of commands and when to use each. See **`START-HERE.md`** for a
short walkthrough of your first project.

## The two rules worth remembering

1. **Secrets stay out of code.** Connection strings and API keys go in `.env` (already git-ignored),
   never in your code. Copy `.env.example` to `.env` and fill in real values.
2. **Prove it cheaply, then build it well.** Brainstorm → plan → prototype → *then* pick the stack and
   build for real, one small phase at a time. The process keeps a vibe-coded project from becoming
   something nobody can maintain.

## A note for tools that go to real people

This kit helps you *build*. If what you build will be used by actual people or touch sensitive data,
it needs a governance tier at Moody's (vibe-coded doesn't mean ungoverned). Claude will flag this when
your project looks headed for real users — follow the Moody's Maker governance process before you ship
widely.
