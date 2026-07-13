---
description: Regenerate + republish the Antigravity Pulse operator console (missions, verdicts waiting, outcomes due, threads)
---

# /pulse-board — Operator Console Refresh

// turbo
```bash
python3 execution/pulse_dashboard.py
```

Then republish `.agent/pulse/pulse-board.html` via the Artifact tool.
- Same conversation as a prior publish: same file path keeps the URL.
- Different conversation: pass the existing artifact URL as `url` (find via Artifact list) — never mint a duplicate board.
- Favicon stays 🎛️ (stable tab identity).

Data sources (all deterministic): `.agent/missions.jsonl` (written by /go Stage 2.5) · `.agent/cos/goals.json` (sprint banner) · `.agent/jam/taste-ledger.jsonl` · `revenue_tracker.py due` · `handoff_store.py list` · `.agent/session.lock`.

If a mission is missing from the board, it wasn't logged — fix the logging (Stage 2.5), not the board.
