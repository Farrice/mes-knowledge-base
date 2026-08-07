# Mission Engineering Artifact Contract

Use this pattern when adapting external engineering-process ideas into Antigravity.

## Problem

An external repo or framework may contain useful software-engineering mechanics, but installing it wholesale can duplicate Antigravity's routers, commands, agents, and governance.

## Trigger

- The source offers a better planning, review, memory, or feedback loop.
- Antigravity already has an equivalent routing or command layer.
- Future work needs durable continuity across sessions.

## Working Solution

Adapt the mechanic as an optional Mission OS artifact contract rather than a parallel command suite.

For engineering missions, create:

- `strategy-anchor.md`
- `requirements.md`
- `plan.md` with stable U-IDs
- `review.md`
- `solution-capture.md`
- `pulse.md`

Use:

```bash
python3 execution/mission_control.py create --name "[mission]" --goal "[objective]" --mode code --librarian-required --artifact-contract engineering
```

## Why It Works

The system keeps one front door and one governance layer, while giving substantial code/system work better durable memory. It borrows compounding behavior without increasing command-selection burden.

## Prevention Rule

Do not install or clone an external process plugin just because it has useful rituals. First ask whether its value can be captured as:

- a Mission OS artifact contract
- a validation assertion
- a reusable solution doc
- a router or workflow enhancement
- a Knowledge Librarian surfacing rule
