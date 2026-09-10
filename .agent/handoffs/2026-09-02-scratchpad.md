---
thread: scratchpad
status: active
resume_hint: Deep research ledger fix committed in lane; open: Farrice checks AI Studio billing for the cost constant; merge lane when main is clean
branch: worktree-deep-research-ledger-fix
pin: false
---

## Purpose
Audit of the Gemini Deep Research path after a $0.50 run "errored out and lost the ledger." Root cause: the run completed fine (821s, 47 sources) but `research.py` printed only the receipt, the body was never saved, and the recovery re-fetch double-logged the spend.

## Current State
- Fixed in lane `worktree-deep-research-ledger-fix`, commit `9530f6730`: pending rows at interaction start (recoverable on timeout/kill), once-per-id charging, body persisted to `.tmp/research/gemini/<id>.md` + `.tmp/research/<ts>-<slug>.md`, poll cap 15→30 min, month rollover archives to `.agent/gemini-api-usage-archive/`.
- Proof: `python3 execution/verify_deep_research_ledger.py` 5/5, sabotage detected each; `verify_deep_research_os.py` still PASS. Live ledger de-duplicated ($1.00 → $0.50; backup in the archive dir).
- Policy doc `directives/google-api-usage-policy.md` records mechanics + open item.
- UNCERTAIN (finding 1): `EST_COST_PER_QUERY` $0.50/$1.50 is a guess; Google's doc says ~$1–3 standard, ~$3–7 max. 52 runs since June tracked at ~$8.50 under a $10 ceiling that should have tripped after ~5 runs at Google's rate. Only Farrice can resolve via AI Studio → Settings → Billing.
- Lane not merged: main dirty (90 tracked changes from other work) so auto-merge parks it.

## Remaining Priority
Farrice checks AI Studio billing; then either read real token usage from the Interactions response or set constants to Google's ranges. Merge lane when main is clean: `python3 execution/worktree_lane.py merge --lane worktree-deep-research-ledger-fix`.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-09-01-scratchpad.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
