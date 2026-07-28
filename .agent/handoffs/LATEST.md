# Latest Handoff

**Thread:** opus5-adaptation-layer  
**Full path:** .agent/handoffs/2026-07-28-opus5-adaptation-layer.md  
**Date:** 2026-07-28 (today)  
**Status:** ready  
**Title:** Opus 5 Adaptation Layer — Model-Dialect Resilience v2 (injector + dead-channel layer SHIPPED)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume opus5-adaptation-layer` for this one.

---

---
thread: opus5-adaptation-layer
status: ready
resume_hint: Triage 66 execution orphans (wire/archive/bless), then probe Fable 5 for claude-fable-5.md dialect card
unfinished: Orphan triage + Fable dialect card; first 06:00 run of rewired daily-health-audit unverified
branch: main
pin: true
---

# Opus 5 Adaptation Layer — Model-Dialect Resilience v2 (injector + dead-channel layer SHIPPED)

## Purpose
- **Next session should do:** (1) triage the 66 execution-class wiring orphans — wire, archive, or bless each with Farrice (they are the ENTIRE dead pile; everything else proved wired); (2) probe Fable 5 and write `directives/model-dialects/claude-fable-5.md` with a `machine-dialect` JSON block so the bound injector lights up on Fable seats (it is honestly silent there now).
- **Not in scope:** rebuilding anything below — the layer is shipped, verified, and committed. Extend only.

## Load First
- `docs/solutions/2026-07-28-opus5-adaptation-bound-injector.md` — § MERGE OUTCOME is the authoritative final-shape record (two concurrent sessions built this on one tree; accept→repair→dedupe)
- `guides/2026-07-28-opus5-adaptation-layer.md` — Part 2 = operator guide (commands, mental model, honest edges)
- `directives/model-dialects/claude-opus-5.md` — the card format to replicate for Fable (JSON `machine-dialect` block at the end)
- `python3 execution/wiring_audit.py status` — live orphan list (do not work from a stale copy)

## Current State
- **Objective:** model releases survivable without harness rebuilds; every asset provably wired.
- **What is already done (commits `2397327cf` + `7c0d77cc3`, 2026-07-28):**
  - Bound injector in `steering_loop_hook.py`: active-model resolution (payload→env→transcript→cache→default), JSON dialect-card block, deliverable/conversational classes, exemplar calibration, NO number tables (Farrice's binding call), kill switch `DIALECT_INJECTOR_OFF=1` / `.agent/dialect-injector.off`.
  - 5 classify-only detectors in `self_heal.py`: dead_hooks (evidence mtimes + unmapped-hook completeness), dead_launchd (loaded + log cadence + new-plist grace), stale_feeds, core_surface_bypass (≥3 sessions/7d, pinned), wiring_orphans.
  - `wiring_audit.py` tier-3 ratchet: 3,579 assets, read-only by AST guarantee, FULL backlog drained day one in 1.6s → 66 orphans, all execution-class. Daily 150/day via `com.antigravity.daily-health-audit` (06:00, rewired `daily_health_audit.py`); weekly 400-batch in /weekly-closeout.
  - Verifiers: `verify_dialect_injector.py` (26), `verify_dead_channels.py` (23), `verify_wiring_audit.py` (21) — 12 sabotage negative controls, all caught both directions; existing suites regressed green.
  - Deleted as superseded: `verify_loop_integrity.py`, `verify_core_surface.py`, `verify_birth_wiring.py` (its PostToolUse trigger was never registered), `daily_backlog_drain.py` (declared a launchd job that never existed).
- **What is uncertain or stale:** a THIRD session was live this morning writing `writers-room.md` / `VOICE-CARD.md` — foreign uncommitted files may sit in the tree; accept→repair→dedupe, never revert. `daily-health-audit` launchd job has not yet had its first 06:00 run with the rewired orchestrator — check `.agent/health/daily-audit.json` tomorrow.
- **Latest proof/receipt:** all three suites green as of commit `7c0d77cc3`; `wiring_audit.py status` = 100% coverage, 66 orphans.

## Suggested Skills / Workflows
- `/weekly-closeout` — the orphan triage lives in its Step 1 wiring deep pass
- `/system-audit` — control-plane route for any wiring complaint (routing binding fires on this)
- `directives/model-dialects/` + `test_model_compliance` probes — the Fable probe should follow the P1–P9 battery used for Opus 5

## Exact Next Prompt
```text
/resume opus5-adaptation-layer

Two tasks, in order. 1) Run python3 execution/wiring_audit.py status and walk me
through the 66 execution orphans in batches of ~15: for each, propose wire (add the
missing reference), archive (move to _archived, deliberate), or bless (add an
exemption with reason). Nothing executes without my yes. 2) Then probe Fable 5
(P1-P9 battery per directives/model-dialects/claude-opus-5.md) and write
claude-fable-5.md with a machine-dialect JSON block — same format, Fable's
pathologies. Do not rebuild the injector or detectors; extend only.
```

## Acceptance Criteria
- Orphan count in `wiring_audit.py status` reaches 0 via deliberate wire/archive/bless decisions (no silent deletions).
- `claude-fable-5.md` exists with a parsing `machine-dialect` block; `verify_dialect_injector.py` still 26/26; a Fable-seat prompt shows the MODEL DIALECT block injected.

## Risk Notes
- Concurrent sessions on one tree caused three collisions today — claim `session_lock` AND confirm no sibling is live before multi-file work; if files change that this session didn't write: accept→repair→dedupe (docs/solutions/2026-07-15).
- The wiring prover's proof rules are curated — a new asset class (e.g. councils/) is invisible until added to `wiring_audit.inventory()`.
- Never "fix" an orphan by weakening its proof rule — that is laundering, structurally forbidden in the self-heal layer.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

