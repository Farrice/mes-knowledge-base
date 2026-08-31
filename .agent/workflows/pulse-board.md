---
description: Open the LIVE Antigravity Pulse operator console (on-demand localhost server — click-to-complete missions, log outcomes, resume/archive threads) or republish the static snapshot as an artifact
status: superseded
superseded_by: homebase
---
> **RETIRED AS A SURFACE (2026-08-20, two-surfaces collapse).** The Homebase at
> http://127.0.0.1:8765/ absorbed this board's cards and actions; /pulse now
> redirects there. The generator survives as a library/CLI. Spec: .agent/workflows/homebase.md


# /pulse-board — Operator Console (live)

// turbo
```bash
python3 execution/pulse_serve.py --open
```

Starts (or reuses) the on-demand local server at `http://127.0.0.1:8765/` and opens the board. **Served = live**: the board regenerates on every load and the action buttons really write — ✓ done / park on missions (one-line prompt → `.agent/missions.jsonl`), log-outcome / snooze +14d / no-outcome on check-ins (→ `revenue_tracker`), archive on threads (→ handoff store). Idle 2h → server exits clean; nothing runs in the background after that. Opened as plain `file://` instead, every button degrades to copy-the-exact-command (`execution/pulse_actions.py …`) — nothing breaks.

Regenerate the static file only (no server): `python3 execution/pulse_dashboard.py`

## Artifact republish (optional)

Publish `.agent/pulse/pulse-board.html` via the Artifact tool (static snapshot — actions fall back to copy-command there).
- Same conversation as a prior publish: same file path keeps the URL.
- Different conversation: pass the existing artifact URL as `url` (find via Artifact list) — never mint a duplicate board.
- Favicon stays 🎛️ (stable tab identity).

Data sources (all deterministic): `.agent/missions.jsonl` (written by /go Stage 2.5 + `pulse_actions.py`) · `.agent/cos/goals.json` (sprint banner) · `.agent/jam/taste-ledger.jsonl` · `.agent/revenue-outcomes.json` (read directly — full deliverable strings) · `handoff_store.threads()` · `.agent/session.lock` · Briefing Room (fresh-intel row).

If a mission is missing from the board, it wasn't logged — fix the logging (Stage 2.5), not the board.
