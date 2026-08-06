---
description: Open the Oracle cockpit LIVE — clickable actions (capture closes, gate check, drop notes), harness activity, gate progress, bankroll curve, CLV
---

# /oracle-board — The Oracle Cockpit

Serve-first: reuse a healthy live server if one is up, else start one. Buttons on the page act instantly in live mode; on plain file:// they copy the exact command instead.

// turbo
```bash
if curl -s --max-time 2 http://127.0.0.1:8765/ping | grep -q pulse; then
  open "http://127.0.0.1:8765/oracle"
else
  (nohup python3 execution/pulse_serve.py >> .agent/pulse-serve.log 2>&1 &) && sleep 1 && open "http://127.0.0.1:8765/oracle"
fi
```

Static fallback (no server, still $0): `python3 execution/oracle_dashboard.py --open`

**Live actions on the page:** ↻ Refresh · ⏱ Capture closing lines (`paper_trader.py closes`) · ⚖ Run gate check · ✎ Drop a note to the overnight run (mints a mission card via the event listener) · ◉ Demo mode (blurs dollar amounts for showing outsiders). Every button has a copy-able CLI twin for offline mode.

**What it shows:** graduation gate w/ live badges · integrity strip (backfills excluded — lead with this in demos) · system activity (queued/done mission cards, click to open; listener runs) · cumulative profit curve w/ hover + prospective filter · hit-rate by confidence (click a bar to filter the bets table) · ROI splits by prop/direction · CLV + Odds API budget readout · lane waiting room (NBA dark / WNBA / Kalshi) · recent bets with click-to-expand decision receipts.

Cost: $0 — localhost only (127.0.0.1:8765, 2h idle auto-exit), reads local ledgers, zero network egress. The only metered thing it can trigger is ⏱ closes, which spends Odds API free-tier requests and shows the remaining quota on the page.

Related: `/pulse-board` · `/briefing-room` · `/assets-board` (the four-surface nav quad) · `/picks-tonight`.
