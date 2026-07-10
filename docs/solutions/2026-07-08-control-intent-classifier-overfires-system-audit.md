---
name: Control-Intent Classifier Overfires on Domain-Ambiguous Vocabulary
problem_signature: system-audit keeps firing as owner "for no apparent reason" on both Claude Code and Codex — content/client prompts mentioning "hook", "chain", "agent", "default" plus everyday words ("why", "issue", "wrong") get hijacked into control-plane repair
domain: system
tags: [routing, control-plane, classifier, false-positives, misfire, control_intent]
date: 2026-07-08
status: active
session: steering-loop-build
---

## Problem

`/system-audit` was being assigned as owner constantly, including on client
content work. Routing-intelligence evidence: "Repaired 6853 Willis Jen
recording pack", "Health Performance GEO automation prompt", and
"claim-safe-health-marketing skill shipped" all finalized under
`system-audit`. Both harnesses misfired because both import the same
classifier: `execution/control_intent.py` (via `skill_router_hook.py` on the
Claude side, `codex_operator_preflight.py`/`workflow_router.py` on Codex).

## Root Cause

`classify_control_intent`'s shape match was `any-surface-term AND
any-problem-term` with substring matching. The surface list contained words
that are CONTENT vocabulary in this workspace ("hook", "skill", "agent",
"chain", "default", "workflow") and the problem list contained everyday words
("why", "issue", "wrong", "what's going on"). One ambiguous word + one
everyday word → system-audit at confidence 90+. A 15-prompt labeled battery
showed 3/10 innocent content prompts misrouting (e.g. "why is this post not
converting, check the hook in line 1").

## Approach That Worked

Tiered evidence instead of flat term lists:

1. **Strong anchors** (unambiguous control-plane words: "router", "codex",
   "wiring", "system-audit", "parity", "preflight", "verifier"…) may fire with
   any problem/action word.
2. **"hook(s)" only counts near a system verb** (fires/blocks/injects/
   enforces/gates — regex `HOOK_SYSTEM_RE`); content hooks grip/convert, they
   never "fire".
3. **Weak surface terms** need aggregate evidence: ≥2 distinct lemmas + a
   problem + an action, AND no deliverable verb, AND no content-domain noun
   (post/email/copy/listing/workout…).
4. **Word-boundary matching** everywhere ("chain" must not hit "blockchain").
5. `repair_status_review` loses to content-domain context ("why wasn't the
   email fixed" is a revision complaint, not control-plane).

Locked with `execution/verify_control_intent.py` — a 20-case golden set (12
must-NOT-fire drawn from real misfires, 8 must-fire) that runs standalone and
fails loudly on regression.

## Dead Ends

- Requiring surface evidence for `repair_status_review` broke the
  operator-core probe contract ("nothing was fixed that I wanted" must stay
  with system-audit) — suppress on content context instead.
- Fixing only `skill_router_hook.py`'s phrase list would have left Codex
  misfiring — the shared classifier was the single root.

## Verification

`python3 execution/verify_control_intent.py` → 20/20 PASS.
`python3 execution/verify_google_operator_core.py` → PASS (all 26 router
probes, after also fixing its stale hook-count expectation 6→8 from the Wave 1
orphan-hook wiring). `python3 execution/verify_codex_claude_parity.py` → PASS.

## Weaker-Model Trap

Adds the misfiring word to a blocklist or deletes it from the surface list
outright, which silences REAL complaints that use that word ("the hooks are
blocking everything"). The crack is contextual disambiguation (system verb
proximity + domain guards), not term deletion.

## Pointers

- `execution/control_intent.py` (STRONG_ANCHOR_TERMS, HOOK_SYSTEM_RE, tiered
  shape match)
- `execution/verify_control_intent.py` (golden set — extend it with any future
  misfire before fixing)
- `.agent/routing-intelligence.json` routing_decisions (misfire evidence)
