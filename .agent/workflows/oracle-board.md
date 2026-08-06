---
description: Render + open the Oracle dashboard — live view of the betting master's exam, gate progress, bankroll curve, CLV, and harness sensing
---

# /oracle-board — The Oracle Dashboard

// turbo
```bash
python3 execution/oracle_dashboard.py --open
```

Static local page (file://), $0 to run — reads `.agent/paper-trading.json`, the graduation gate (`live_trader.check_gate()`), event-listener state, and mission-queue counts. Re-run the command (or this workflow) any time to refresh; data is baked at render.

**What it shows:** stat tiles (bankroll, P/L, prospective hit rate, gate progress) · the four-criteria graduation gate with PASS/FAIL/PENDING badges · the integrity strip (backfills excluded — the trust feature, show it in every demo) · cumulative profit curve with hover crosshair + all/prospective filter · hit-rate-by-confidence bars (C5 flagged red until calibration ships) · CLV panel · recent bets.

**Demo use:** this page IS the proof-of-concept surface for the Oracle and the God Agent concept — never demo from the terminal. For a shareable/phone version, publish via the Artifact flow (embed data first; file:// links don't resolve remotely).

Related: `/picks-tonight` (nightly slate) · `python3 execution/paper_trader.py closes` (CLV capture) · `python3 execution/live_trader.py check` (gate verdict, terminal form).
