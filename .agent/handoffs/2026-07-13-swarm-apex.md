---
thread: swarm-apex
status: ready
resume_hint: Session 2: build claim_audit.py + gates.py, wire into swarm synthesis (apex Wave 2)
unfinished: S2 verifiers, S3 mission pattern + JCC head-to-head, S4 packaging + browser; Redline & Rescue Day-1 kill-switch; /cos weekly overdue
branch: main
pin: true
---

# Swarm Apex — Session 1 Build (swarm live + Solution Recorder + closeout spine)

## Purpose
- **Next session should do:** Swarm Apex Session 2 — wire `claim_audit.py` + `gates.py` verifiers (Harness Apex Wave 2) into the swarm synthesis phases; then Session 3 (mission pattern + JCC head-to-head). Separately on deck: execute the Named-Brand Claim Redline & Rescue (Day-1 kill-switch: find one funded sports-nutrition brand with live claim-exposed ads via Meta Ad Library + Crunchbase), and `/cos weekly` (overdue).
- **Not in scope:** rebuilding anything shipped today (swarm conductor/patterns, closeout spine, Solution Recorder are LIVE — extend only); browser pattern and packaging automation (Session 4); any repositioning (PATH DECISION incumbency holds).

## Load First
- `_active/swarm-apex-2026-07-07/PLAN.md` — the merged mission plan, 4-session build sequence, S1 marked shipped
- `strategy_briefs/2026-07-07-path-a-proof-of-work-heavy.md` — the heavy-run decision brief (Named-Brand Claim Redline & Rescue, 5 forks with resolvers, claim ledger)
- `research_outputs/2026-07-07-claim-safe-content-landscape.md` — Path A market research (enforcement shift to review/endorsement integrity)
- `docs/solutions/index.md` — 6 Solution Cards; read matching cards before re-solving anything
- `.agent/workflows/swarm.md` — /swarm conductor v2 flow (plan → gate → Workflow launch → receipt)

## Current State
- **Objective:** replace SuperGrok/Manus/Kimi/Perplexity subscriptions with native /swarm capability; make every cracked problem durable via the Solution Recorder.
- **What is already done:** /swarm conductor + heavy/research patterns live and proven (research: 15/15 agents, heavy: 16/16, both finalize 8.67 PASS, $0); end-session closeout spine + SessionEnd hook; Solution Recorder end-to-end (detection → /extract-approach → finalize latch → PRIOR SOLUTION injection, observed working in production); Step 6.5 in all 3 constitutions, compiler blessed; all committed and pushed (cd0ec1911).
- **What is uncertain or stale:** roster casting quality (invocation-card drift: 4 conflicting counts vs 221 actual dirs — live census is a queued continuous item); AI-citation-lift claim possibly backwards (test live before using in outreach); heavy verify REFUTED the "zero public proof" premise — never reuse that framing.
- **Latest proof/receipt:** `.agent/run-receipts/2026-07-07T184806Z0000-swarm-heavy.md` + two finalize traces at 8.67.

## Suggested Skills / Workflows
- `/swarm` — the conductor front door (plan → gate → unattended)
- `/extract-approach` — after any cracked problem; latch enforces it
- `/resume swarm-apex` — reload this thread
- `/system-audit` — owner route for wiring work (control-plane binding)

## Exact Next Prompt
```text
/resume swarm-apex — start Swarm Apex Session 2: build claim_audit.py and gates.py (Harness Apex Wave 2 spec in _active/harness-apex-2026-07-07/PLAN.md), wire claim_audit into swarm-heavy and swarm-research synthesis phases as a deterministic post-synthesis step, fixture-test both (known-PASS and known-FAIL artifacts), and check docs/solutions/index.md before solving anything that feels familiar.
```

## Acceptance Criteria
- claim_audit.py + gates.py exist with fixture tests (one PASS, one FAIL each)
- Both swarm pattern scripts call claim_audit deterministically post-synthesis
- A live swarm run shows the verifier's output lines in its report
- Finalize passes with anchors named; no learning debt left open

## Risk Notes
- Two-window concurrency: GOLDEN RULE — one tool per working tree; the finalize latch reads the newest ledger (4h freshness guard added, but don't run Codex + Claude Code simultaneously)
- Named-brand redline work carries defamation exposure if a flag is wrong — every flag must be citation-anchored; private delivery only; no legal review yet obtained
- Perplexity API is dead (never propose paid credits); research patterns use WebSearch only
