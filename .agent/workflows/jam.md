---
description: Co-creative small-loop sessions — Claude carries the drafting, Farrice steers with 10-second gut verdicts; the taste ledger learns across sessions
---

# /jam — The Co-Creation Protocol

`/jam <artifact-or-path>` (revision jam — the default) · `/jam new "<spark>"` (from scratch)

## Why this exists (Farrice, 2026-07-08)

"I'm still doing so much directing and solo work. I need a creative partner in my
corner... AI and human become superhuman together." The failure modes this kills:
big-bang deliveries he has to mark up cold, alignment drift discovered only at the
end, open-ended questions when he's fried, and token-burning fleets for what should
be two people trading cuts. Jam is the third rhythm between "delegate to a fleet"
and "Farrice writes it himself."

## The Loop (each loop ≤ 2 minutes of Farrice's attention)

1. **Claude brings TWO takes** on the piece in play — genuinely different cuts
   (different bet, not cosmetic variants: e.g. "structured cards" vs "raw
   locker-room"), via AskUserQuestion with previews, plus a ONE-line
   recommendation with the reason.
2. **Farrice verdicts in gut grammar** — no essays required:
   - `A` / `B` — pick one
   - `A but <dial>` — dial words: rawer · warmer · tighter · slower · harder ·
     funnier · simpler · deeper
   - `mix: <what from each>`
   - `neither — <one word why>`
3. **Claude cuts again** from the verdict — edits live in the main thread, no
   agents, no fleet. Next loop goes one level smaller (doc → section → line).
4. **3-5 loops max, then ship.** If it's not converging by loop 5, the brief is
   wrong — stop and name what's actually unresolved (one question, not a menu).

## Hard Rules

- **ONE question per loop.** Never stack. Fatigue mode is the default, not the
  exception.
- **Claude drafts, Farrice reacts.** Never ask him to write the thing or describe
  the fix — show him the fix, let him verdict it.
- **Substance first.** Loop 1 is always real content (a finished take, not an
  outline or a plan). He reacts to work, not to descriptions of work.
- **Main-thread only during the jam.** Fleets run BEFORE (first pass) or AFTER
  (propagate the calibrated taste to the sibling assets). Mid-jam agents break
  flow and burn tokens on what one editor does better.
- **Opinion required.** Claude states which take it believes in and why, every
  loop. A partner with no stake is a vendor.
- **Disagreement is allowed once.** If Farrice's verdict trades away something
  load-bearing, say so in one line, then execute his call either way.

## Taste Ledger (the part that compounds)

Every verdict appends one line to `.agent/jam/taste-ledger.jsonl`:
`{ts, artifact, domain, take_a, take_b, verdict, dials, note}`
- At jam start, Claude reads the ledger and states the prior pattern in one line
  ("last 3 jams you picked the rawer cut and dialed 'tighter' — starting there").
- A dial/verdict pattern that repeats 3+ times graduates: propose a one-line
  addition to the relevant voice/taste memory (never silently).
- Feeds `/voice-ratchet` for voice domains; stays domain-tagged for the rest.

## When NOT to jam

Mechanical or deterministic work (filing, conversion, wiring) · research sweeps ·
anything with an objectively right answer · first passes on big multi-asset builds
(fleet those, then jam the flagship piece). Jam is for taste-bearing work: copy,
concepts, naming, strategy framing, design direction.

## Session shapes

- **Revision jam** (default): existing artifact → loops down doc → section → line
  → ship + finalize as usual.
- **Spark jam** (`/jam new`): Farrice's messy spark → Claude writes TWO opening
  takes immediately (no clarifying-question round unless a DICE dimension is
  fatally missing — one question max) → loop as above.
- **Morning-after jam**: a fleet staged Take A/Take B overnight (e.g.
  `_take-b/` files) → first loop is waiting when Farrice sits down.

## Exit

"Ship it" → normal Chain finalize (jam does not bypass gates; it front-loads
taste so gates confirm instead of surprise). Ledger line written. If the jam
produced a reusable taste rule, flag it in the close per the Steering Loop.
