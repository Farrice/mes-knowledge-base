---
description: Mission Control — the live board of every working thread, needs-you first, with resume/close buttons
---

# /mission-control

The deciding surface. One card per live thread, blocked and stale work at the top, and
four actions on every card: **open brief** (the deep read), **resume** (copies the exact
resume command), **copy context** (the whole thread formatted to paste into Claude or
Codex), and **done / park / archive**.

```bash
# // turbo
if curl -s --max-time 2 http://127.0.0.1:8765/ping | grep -q pulse; then open "http://127.0.0.1:8765/missions"; else python3 execution/mission_board.py --open; fi
```

**Served = live**: regenerates on every load, buttons write for real, and the page reloads
itself when a sweep rewrites it underneath. Opened as plain `file://`, every button
degrades to copy-the-exact-command — nothing breaks.

The always-on daemon (`com.antigravity.pulse-serve`) keeps
<http://127.0.0.1:8765/missions> permanently available, so the probe above almost always
takes the served branch. All four boards share it:
`/` pulse · `/room` briefing room · `/missions` mission control · `/oracle` oracle.

## Data sources (all deterministic)

- `.agent/sweep/latest.json` — the fact bundle from `session_sweep.py` (Claude + Codex
  sessions, handoffs, the finalize ledger, missions, the asset manifest, git).
  **This board never re-derives a fact**; if a number looks wrong, fix the sweep.
- Writers are `execution/pulse_actions.py` (`done` / `park` / `thread-archive`) — the same
  ones the Pulse board uses, so a click and a typed command do identical things.

If a thread is missing, run `/sweep` — the board only shows what the last sweep saw.

## Not to be confused with

`/missions` (plural) is the **campaign queue** front door — CAMPAIGN.md continuity,
`new`/`next`/`done` subcommands. This is the **thread board**: what's in flight across
sessions, and how to pick it back up.

## Related

- `/sweep` — recollect now (also runs nightly at 02:45)
- `/briefing-room` — per-thread briefs, for reading rather than deciding
- `/pulse-board` — missions, outcomes, revenue check-ins
