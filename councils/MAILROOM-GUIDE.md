# The Mailroom — Farrice's User Guide

*Live councils: your expert personas as real teammates who DM each other, argue, concede, and
converge — instead of parallel takes frozen at exchange one. Protocol canon for agents:
`directives/agent-mailroom.md`. This page is yours: when to use it, what it costs, what you get.*

## The one decision rule

| Situation | Use | Cost |
|---|---|---|
| Real fork, taste-bearing, disagreement expected — you'd pay for the argument | **Live**: say "run a live roundtable on X" (or `/roundtable-live`) | ~650k tokens, ~10 min (run-1 measured) |
| Breadth, ideation, a survey of angles — you want takes, not a negotiation | **Frozen**: `/convene` / `/roundtable` / `/council` | ~150k tokens |
| One expert, clear task | Neither — invoke the expert directly | minimal |

Live mode never auto-fires. You invoke it on purpose, ~2-4/week is the sane ceiling.

## What happens when you say "run a live roundtable on X"

1. **Cast** — 4 seats (6 max), each loaded with their genius voice + their own memory of past
   councils. Weak keyword casts get re-seated by hand; you can swap any seat by name.
2. **Openings** — independent takes, no peeking (anti-anchoring).
3. **The meeting** — seats DM each other directly (`[NORMAL]/[PRIORITY]/[URGENT]`), challenge,
   concede, revise. Pass tokens kill chatter; max 3 rounds; your word relays as `[URGENT]` and
   outranks everything.
4. **Converge** — verdict + tripwires + any dissent PRESERVED as your fork, never blended.
5. **Close** — digest to `knowledge/council-sessions/`, each persona's position written to its
   own memory, prediction row appended to calibration, measured cost recorded.

## What accumulates (why run 5 beats run 1)

- **Persona memory** — Hormozi now remembers the position he took today; next council he starts
  from it. `agents/<name>/memory/context.md`.
- **Standing-council decision memory** — `councils/<name>/decisions.md` fills per session.
- **Calibration** — every session logs a falsifiable prediction; the council pulse
  (`execution/council_pulse.py`, wired into your session digest) nags when outcomes sit unclosed.
- **The Commons** — each session's shared reasoning file, `councils/commons/<date>-<slug>.md`,
  snapshot in the digest.

## Cost & effectiveness — run 1 receipts (2026-08-27, offer-path decision)

- **Measured:** ~655k subagent tokens (4 Sonnet seats, all peer DMs included), ~10 min wall clock,
  $0 marginal cash (subscription usage; no paid APIs). ~4x the frozen baseline.
- **What the 4x bought:** Cole caught Haynes conflating two offer rungs via [URGENT] DM →
  Haynes corrected his own position in-round; a three-way fork on first-touch mechanics was
  negotiated to convergence BY THE SEATS (with logged concessions), not blended by the conductor;
  verdict came with a falsifiable tripwire instead of vibes. None of that is possible frozen.
- **Review gate:** after 3 measured runs, you call keep/widen/kill on live mode. 1 of 3 done.

## Watch-outs

- Fast consensus = run the echo-chamber round (conductor does this automatically).
- `[URGENT]` between seats is only for factual errors / invalidated work — urgency inflation gets
  named in the digest.
- The council decides nothing you didn't ask; sends stay human, always.
- If a live session produces only restated agreement, that's a frozen-tier question — downgrade
  next time and save the tokens.
