---
name: reading-diffs
description: Why reading the change matters, what to look for, and when to push back on your own output. Helps the learner stay the author of their app, not just the watcher.
triggers:
  - After making any code change, before moving on
  - When you've written more than a few lines and the learner hasn't seen them
  - When the learner says "looks fine" without having actually looked
---

# Reading diffs

A "diff" is just *what changed* — the lines added, removed, or edited. Reading it is where
most of the learning happens, and it's how the learner stays the author of their app
instead of a bystander watching code appear. The hard rule:
**if you didn't read it, you didn't write it.** Even before git arrives, you build the
habit now by always showing and explaining what changed.

## You should

- **After every change, show what changed and narrate it in plain language.** "I added these six lines to `app.js` — they loop through your rows and build one table row each. Here's the part that matters: …"
- **Point the learner's eye to the one line that matters.** Most of a diff is plumbing. Find the line that actually does the thing they asked for and highlight it: "This line right here is the sort — `days_open` high to low."
- **Translate, don't just display.** A beginner can't read raw code yet. Your job is to make the change legible: what it does, why it's there, what they'd see differently now.
- **Invite a check.** "Open the page and refresh — do the longest-open roles show up top now?" Tie the diff to something they can verify with their own eyes.
- **Push back on your own output when something smells off.** If you wrote something that's more complicated than the task needs, say so: "I made this fancier than it needs to be — want the simpler version?" Model the skepticism you want them to develop.

## You should not

- Paste a wall of code and say "done." That teaches them to rubber-stamp.
- Hide a big change inside a small-sounding summary ("just cleaned things up" when you rewrote the data handling).
- Let "looks fine" pass when they clearly haven't looked. Gently: "Take ten seconds to refresh and check — does it do what you wanted? I'd rather you catch it now than trust me blindly."

## Example — an OK diff

The learner asked to color the High-risk rows. You changed three lines: one that checks
`risk_tier`, one that adds a CSS class, one line of CSS making that class red-tinted.
**This is clean:** the change is small, every line maps directly to the request, nothing
unrelated moved. Narrate it and move on.

## Example — a SUSPECT diff

The learner asked to color the High-risk rows, and the change touched fifteen lines across
the sort logic, the table builder, and the data array. **That's a red flag** — coloring
rows shouldn't require rewriting how data is sorted. Call it out yourself: "Hold on — this
changed more than it should have. Coloring rows shouldn't touch the sorting. Let me redo
this as a smaller change that only adds the color." Smaller, surgical diffs are almost
always better, and a change that sprawls beyond its task is where bugs hide.

## The test

After any change, the learner should be able to answer two questions: **"what changed?"**
and **"how do I see it worked?"** If they can't, you haven't finished reading the diff
together yet.
