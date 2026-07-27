# System Primitives (Irreducible Parts)

> Extracted from CLAUDE.md 2026-06-09 (rebuild). Reference — read when composing or modifying system workflows.

Each row names who owns the responsibility and what triggers it. If a workflow reimplements a primitive's logic, that's drift — the source file is the contract.

| Primitive | Owns | Triggered By | Source File |
|---|---|---|---|
| `intent_to_package` | Outcome-class detection -> mission package | `/autopilot` Phase 1 | `execution/intent_to_package.py` |
| `routing_enforcer` | Runtime validation of Expected Routing table | **UserPromptSubmit hook (deterministic)** + `finalize` post-hoc | `execution/routing_enforcer.py` |
| `forge_gate` | Extraction usage TELEMETRY only (never gates — standing decision 2026-06-09) | `record` at end of extractions; `status` in monthly `/weekly-closeout` | `execution/forge_gate.py` |
| `cost_gate` | Pre-flight approval for paid APIs (Fal, Perplexity, NotebookLM, Gemini) | **PreToolUse(Bash) hook — HARD BLOCK** + `/autopilot` G2 (>$5) | `execution/cost_gate.py` + `execution/hooks/cost_gate_hook.py` |
| `session_ledger` | Finalize-debt tracking, measured sub-agent counts, routing warns, staleness | **UserPromptSubmit/PostToolUse/Stop hooks** | `execution/hooks/session_ledger_hook.py` |
| `anchor_memory` | Project-scoped persistent context anchors | `/supercomputer` + multi-deliverable missions (`--project` on finalize) | `execution/anchor_memory.py` |
| `taste_signature` | Bimodal taste filter atop calibrated rubric (Wave 2) | `finalize` after rubric scoring | `execution/taste_signature.py` |
| `excellence_predictor` | Pre-flight prediction + grade-inflation detector (Wave 3) | `/autopilot` Phase 1; calibration drift | `execution/excellence_predictor.py` |
| `orchestration_ledger` | Post-run trace: what fired, what's next, refinement prompts | End of `/autopilot` | `execution/orchestration_ledger.py` |
| `chain_runner.finalize` | Step 6: quality gate + caps + Notion log + protocol tracking + routing check | Step 6 of every expert deliverable — **enforced by Stop-hook ledger** | `execution/chain_runner.py` |
| `recall_logger` | Observability for Tier 1.5 grounding decisions | Every Recall attempt; deterministic backstop in `finalize` | `execution/recall_logger.py` |
| `eval_harness` | Score against anchored rubric; calibration drift detection | Manual scoring; weekly `evolution_orchestrator` (launchd-scheduled) | `execution/eval_harness.py` |
| `context_ethics_gate` | Deterministic Defense/Ethics backstop for `/ce-*` context-engineering output | Inside `/ce-design`/`/ce-build`/`/ce-honesty`; backstop in `finalize` (Step 11.9) | `execution/context_ethics_gate.py` |

## Skill Architecture — Atoms vs Systems

Two tiers. Naming the distinction makes the compounding layer visible. (Sub-classification underneath the primitives table, not a competing layer.)

**Atomic Skill** — Single tool, one job, reusable across compositions. Upgrading one atom upgrades every system using it.
Examples: `voice-document`, `mood-board`, `name-framework`, `prose-check`, `generate-image`
**Test**: One deliverable type, one workflow, no internal phase gates? -> atom.

**Skill System** — Multi-phase orchestrated composition. Has explicit phase structure and clear orchestrator.
Examples: `/extract-forge` (8 phases + Phase 0 gate), `/parallax` (Phase 2.5 gate), `/writers-room` (9-expert loadout), swarm workflows, brand builds
**Test**: Multiple interdependent phases, multiple expert lenses in sequence, gate-and-proceed structure? -> system.

Expert skills classify as atom or system depending on scope (single workflow = atom, multi-phase production = system). Sub-agents provide context isolation between atoms in a system — execution-time choice, not a tier. Frontmatter annotation (`tier: atom | system`) is advisory; unlabeled is fine.

Routing policy frontmatter (rebuild 2026-06-09): `routing: long-tail` demotes a skill in default routing (explicit invocation preferred); `status: archived` de-indexes it entirely while leaving it on disk.
