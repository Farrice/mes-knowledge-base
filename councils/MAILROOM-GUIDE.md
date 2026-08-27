# The Mailroom — Farrice's User Guide

**What it is, in one sentence:** a way to make several of your expert personas argue a hard
decision with each other before you get an answer — instead of one AI's first take.

**What you read from it:** one page. Do this / Don't do / We're wrong if. Nothing else reaches you.

## When it's worth using (the honest rule)

Almost never. Before any council runs, I have to try answering your question in one paragraph
myself, using your real reports. If I'm confident, you get the paragraph and we save the tokens.
The council only fires when I genuinely can't make the call — real tradeoffs, real stakes, no
obvious answer in the repo. Expect that once or twice a month, not weekly.

**Cost when it does run:** ~650k tokens (~4x a normal multi-expert pass), ~10 minutes, $0 cash.
Worth it only on decisions where being wrong costs you weeks.

## How to invoke

- Say: **"run a live roundtable on <question>"** — I'll first show you my one-paragraph answer
  and only convene if I can't make the call. Say "convene anyway" to override.
- Everything else (ideation, surveys of angles, single-expert work): the normal `/convene`,
  `/roundtable`, or direct expert — cheaper, usually better.

## What it produced on run 1 (2026-08-27) — after correcting the grounding

> **Do this:** (1) Follow up the warm channel first — it's your only proven cash source: $4,650
> collected, all from warm-network services (Josh & Katie $3,500, Andrea $600, Javier $300,
> 6Eight $250), last collection July 25. Close the three warm-intro asks opened July 31.
> (2) Send the three teardown DMs (Transparent Labs, Momentous, Puori): full teardown free,
> one P.S. — "If you want this fixed: $750 Angle Map, 10 days."
> **Don't do:** affiliate (needs an audience you don't have) or the KDP book (publish after 3
> Angle Maps sell) right now.
> **We're wrong if:** 15-20 sends over 2-3 weeks get zero substantive replies — then the message
> or targeting is broken and we rework, not the lane.

## What accumulates quietly (you never have to read these)

Persona memories, council decision logs, and a prediction ledger — the system nags me, not you,
when a prediction's outcome is due. Machinery lives in `directives/agent-mailroom.md`.
