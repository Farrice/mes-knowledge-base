---
thread: execution
status: active
resume_hint: Homebase 2.0 cockpit LIVE at 127.0.0.1:8765 — get Farrice's triad verdict, then v2 Google widgets + client reskin
branch: main
pin: false
---

# Homebase 2.0 — Agentic OS Cockpit

## Purpose
Harvested Jay E's ARMS-framework video (youtube 8NSyI-npJCU) and rebuilt the Homebase at 127.0.0.1:8765 as Farrice's full command center in Ink+Steel Blue — portal → /brain workspace graph, artifacts ring, guarded Skills Deck, routines board — extending homebase_board.py, never a parallel dashboard.

## Current State
Shipped and pushed to main (commit 0bf552a5d): `board_theme.py` (one skin, all boards), cockpit at `/` (drag widgets, live clock, ring search), `/brain` (brain_graph.py, 1,293 curated nodes, fingerprint cache), `skill_deck_runner.py` + `run_skill` verb (index-only params, FORBIDDEN_RE, token-based session_lock — release bug found and fixed in verification), routines widget (29 plists, next-fire, health-joined). Proof: two live deck runs with measured cost ($0.90 sonnet, $0.22 haiku), refusal walls + lock contention + sabotage passes all verified in browser; nav self-test 9/9. Uncertain: browser-pane screenshots glitch on scrolled positions (capture artifact only — DOM verified); Farrice has not yet given his felt verdict on the cockpit.

## Remaining Priority
Get Farrice's Feedback Triad on the live cockpit, then v2: Google email/calendar widgets + the client-reskin demo through board_theme.py (deferred by his explicit call, 2026-08-21). Plan file: ~/.claude/plans/https-www-youtube-com-watch-v-8nsyi-npjc-purrfect-flamingo.md.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-08-10-execution.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
