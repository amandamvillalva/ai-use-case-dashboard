# Start Here — spin up your first project (~10 minutes to your first running v0 plan)

*A short walkthrough for building something new with this kit. Same rhythm as the bootcamp — one small
step at a time, all from inside Claude Code. If you get lost at any point, type `/guide`.*

## Step 0 — Open the folder

Put this `project-starter` folder wherever you keep projects (rename it to your project if you like —
e.g. `contract-tracker`). Open it in the **Claude Code desktop app**. Claude reads `CLAUDE.md` and
`PROJECT_HISTORY.md` automatically, so it already knows how to help you.

> **Tip:** type `/` to see all the commands, and read `COMMANDS.md` for what each one does.

## Step 1 — Tell Claude what you're building

```
/interview-me
```

Claude asks a few questions — the problem you're solving, who it's for, the one core thing it must do.
It writes your answers into the project's brain (`CLAUDE.md`). Two minutes, and now every suggestion
is about *your* project.

## Step 2 — Design it

```
/brainstorm
```

Claude designs v0 with you and writes a short design doc. Push past vague — the sharper the core idea,
the better what you build. Then plan the smallest real version:

```
/mvp-spec
```

## Step 3 — Build a working v0 and play with it

```
/prototype
```

Claude builds the smallest version that proves your idea, and shows you how to run it. Then **iterate**
— "make the status colored," "add a search box," "move that to the top." One change at a time, until it
feels right.

## Step 4 — Start backing up (do this early)

Once you've got something you'd hate to lose:

```
/save-setup     ← turns on Git safely (protects your .env first), makes your first save
/publish        ← create a PRIVATE repo on github.com, then Claude pushes your project to it
```

After that, `/save` anytime you finish a piece of work. The first push pops a one-time GitHub sign-in
in your browser — approve it; it only happens once per laptop.

> **Secrets:** if your project uses a database or an API key, copy `.env.example` to `.env` and put the
> real values there. Never in your code. It's already git-ignored, so it can't be pushed by accident.

## Step 5 — Build it for real, one phase at a time

```
/full-spec      ← pick your stack (Python or JS), install standards, break the build into phases
```

Then the loop, repeated for each phase:

```
/build          ← builds the next single phase
/test           ← proves it works (by hand, and with real tests)
/closeout       ← logs it and teaches it back
/save           ← back it up
```

When every phase is done, `/closeout` wraps the project and `/teach-me` reflects on what you learned.

## The whole thing on one line

**`/interview-me` → `/brainstorm` → `/mvp-spec` → `/prototype` → `/full-spec` → (`/build` → `/test` →
`/closeout` → `/save`) per phase.** Lost? `/guide`. That's it — go build something.

## One honest note

This kit makes you genuinely capable of building real tools. If yours will be used by other people or
touch sensitive data, it needs a Moody's governance tier before it ships widely — building it well and
clearing it to deploy are two different things. Claude will remind you when you're getting close.
