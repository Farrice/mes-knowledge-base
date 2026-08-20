---
description: The Homebase — open the one command-center hub (Focus · Launch · Library) served live at http://127.0.0.1:8765/
---

# /homebase — The Command Center Hub (2026-08-20)

One page Farrice opens to work: **FOCUS** (sprint + money line, six tiles,
missions that need him), **LAUNCH** (resumable sweep threads with one-click
`/resume` copy), **LIBRARY** (fresh briefs, dark asset shelf, system counts).
Every other home base is one nav hop away — and on a served page the nav stays
inside the live server (surface_nav route rewrite, 2026-08-20).

## Open it

```bash
open "http://127.0.0.1:8765/"
```

The server is always-on via launchd (`com.antigravity.pulse-serve`, KeepAlive,
`--idle 0`). If it's somehow down:

```bash
launchctl kickstart -k gui/501/com.antigravity.pulse-serve
```

or fallback: `python3 execution/pulse_serve.py --open`.

## Routes (pulse_serve.py)

`/` homebase · `/pulse` operator console · `/missions` · `/room` briefs ·
`/assets` asset board (added 2026-08-20) · `/oracle` · `/repo/<path>` files.

## Refresh

The header's **↻ refresh data** button (or `python3 execution/pulse_actions.py
refresh`) re-runs the session sweep + asset index, then regenerates the boards;
the open page reloads itself when the data is actually fresh (mtime poll).
Sweep also runs nightly via `com.antigravity.session-sweep`.

## Regenerate manually

```bash
python3 execution/homebase_board.py
```

Doctrine: reads `.agent/sweep/latest.json` + existing ledgers only — never a
second collector (docs/solutions/2026-08-06-live-local-board-pattern.md).
Deferred by decision (2026-08-20 mission): asset-board register reconciliation,
deliverables librarian, workspace force-graph.
