# Commands — what each one does and when to use it

These are your slash commands. Type `/` in Claude Code to see them. They follow the lifecycle below —
but you don't have to memorize it. **If you're ever unsure what to run, type `/guide`** and Claude
will tell you where you are and what's next.

## How guided do you want to be?

Run **`/guide`** anytime to set the working mode:

- **Guided** — Claude explains each step before doing it, works in small pieces, shows you what
  changed, and checks in before anything big. Best when you're learning or want to stay in control.
- **Autonomous** — Claude moves faster, makes reasonable calls, and only stops when something
  genuinely needs your decision. Best when you trust the flow and just want it built. (The safety
  rules still hold — no secrets in code, `/build` still needs a locked plan, and anything
  irreversible still gets shown to you first.)

You can switch modes whenever you like.

## The lifecycle (the normal order)

```
/interview-me → /brainstorm → /mvp-spec → /prototype → /full-spec → /build → /test → /closeout
   define         design        plan        build &      pick stack,   build    prove    log &
   the project    v0            the MVP     iterate v0   phase it      a phase  it       teach
                                                          (locks FINAL) └──── repeat per phase ────┘
```

## Building commands

| Command | What it does | When to use it |
|---|---|---|
| `/guide` | Tells you where you are and what's next; sets guided vs. autonomous mode | Anytime you're unsure — including right now |
| `/interview-me` | Asks about your project (problem, user, the one core thing) and writes it into `CLAUDE.md` | **First.** Always run this before anything else |
| `/brainstorm` | Designs v0 with you and writes a design doc (*what* you're building and why) | After `/interview-me` |
| `/mvp-spec` | Turns the design into the smallest plan that proves the idea | After `/brainstorm` |
| `/prototype` | Builds a quick working v0, then iterates with you until it feels right | After `/mvp-spec` |
| `/full-spec` | Picks your stack (Python or JS), installs engineering standards, breaks the build into small phases — produces the **FINAL** plan | After the prototype proves the direction |
| `/build` | Builds the **next single phase** for real, to the standards. Needs a FINAL plan | In the build loop, one phase at a time |
| `/test` | Verifies the phase — by hand, and with real unit tests where it earns them | After each `/build` |
| `/closeout` | Logs the finished phase and teaches it back; wraps the whole project once all phases are done | After each `/test` |
| `/teach-me` | Deep, whole-project reflection — the concepts you used and what to try next | When you've built something real |

## Version-control commands (back up your work)

| Command | What it does | When to use it |
|---|---|---|
| `/save-setup` | Turns on Git safely — protects your `.env` first, then makes your first save | **Once**, early. Worth doing right after your first real progress |
| `/publish` | Connects your project to a GitHub repo (you create it private in the browser) and pushes it | **Once**, after `/save-setup` |
| `/save` | The everyday loop: shows what changed, commits it, pushes to GitHub | **Often** — every time you finish a piece of work |

## The two habits that outlast any one project

1. **Save small and often** (`/save`) — frequent save points are your safety net.
2. **Prove cheaply, then build well** — the lifecycle exists so a fast idea becomes a maintainable
   tool, not a tangle nobody can support.
