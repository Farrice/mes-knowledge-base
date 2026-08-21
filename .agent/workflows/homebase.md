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

`/` homebase · `/room` briefs · `/assets` asset board · `/oracle` ·
`/repo/<path>` files. `/pulse` and `/missions` are RETIRED (two-surfaces
collapse, 2026-08-20) and 302-redirect here.

## The deep mission pages

Click **open brief ↗** on any Launch card → the thread's context-rich page:
instant summary (handoff Purpose), the state as the last session left it
(Current State + staleness warning), resume/park/**kill** decision + LIVE
buttons, copy-paste blocks (Exact Next Prompt, context pack, operator run
prompt), then numbers, assets (with generation prompts), deduped timeline
(with finalize notes), and the mission record (outcomes + verdicts).
Rich narrative comes from the thread's own handoff — a stub handoff degrades
honestly, so **writing a real /handoff at session close is what feeds this**.

`kill <slug> --reason "…"` = dead + hidden: ledger line + handoff archived;
never resurfaces (recover: `pulse_actions.py reopen` + `handoff_store.py
unarchive`). `park` = shelved + quiet: resumable, muted, never ranks urgent.

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
