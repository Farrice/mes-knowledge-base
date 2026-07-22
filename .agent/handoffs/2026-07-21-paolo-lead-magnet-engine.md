---
thread: paolo-lead-magnet-engine
status: ready
resume_hint: Run /pt-lead-engine for Proof-to-Market sprint (command registers fresh session); Farrice blind pass promotes A-tier
unfinished: Proof-to-Market engine build not started; A-tier awaits Farrice-judged blind pass
branch: main
pin: true
---

# Paolo Trivellato Forge — Extraction Shipped (LinkedIn Lead Magnet Engine)

## Purpose
- **Next session should do:** Run `/pt-lead-engine` for the Proof-to-Market $2,500 sprint offer — pain map from supplement/performance-brand call transcripts, Farrice's authority line, first comment-gated magnet. (The command returned "Unknown command" at the end of the forge session only because freshly generated commands register at session start — `.agent/workflows/pt-lead-engine.md` exists and is indexed; a new session will fire it.)
- **Not in scope:** Rebuilding or extending the skill itself (forge is complete, committed `149d26736`); re-watching the source videos (temp dirs deleted; everything needed is extracted).

## Load First
- `skills/paolo-trivellato-lead-magnet-engine/genius.md` — the spine + verbatim templates + claims quarantine
- `skills/paolo-trivellato-lead-magnet-engine/workflows/pt-lead-engine.md` — the workflow to execute
- `skills/paolo-trivellato-lead-magnet-engine/references/prompts-v2/engine-30-day-plan.md` — the output contract
- `_active/linkedin-launch/02-offer/` — Proof-to-Market master doc (the offer the engine distributes)
- `_active/farrice-brand/voice/VOICE-CARD.md` — mandatory voice layer (binding farrice_voice_alignment)
- `FARRICE-MASTER-CONTEXT.md` — authority-line raw material

## Current State
- **Objective (parent session):** /watch + /extract-forge on two Paolo Trivellato videos → complete.
- **Already done:** skill `paolo-trivellato-lead-magnet-engine` (11 pt-* workflows, 9 born-v2 prompts, front door `/paolo-trivellato`), agent file, registries synced, renaissance audit 0 fail, heartbeat 6/6, blind pass EVAL-050 PASS (model-judged — **A-tier awaits a Farrice-judged pass**; corpus in `extractions/paolo-trivellato-lead-magnet-engine/reference-corpus/`), finalize composite 8.33, forge_gate recorded, committed + pushed to main.
- **Uncertain or stale:** location/existence of supplement-brand call transcripts for the pain map — if none exist, `pt-lead-engine`'s Pre-Flight makes Week 0 = 15-min market-research calls; do NOT fabricate pains. Kyle/Paolo numbers are self-reported (quarantined).
- **Latest proof/receipt:** commit `149d26736` on origin/main; Notion finalize log 2026-07-21; blind-pass ledger `extractions/paolo-trivellato-lead-magnet-engine/blind-pass-log.md`.

## Suggested Skills / Workflows
- `/pt-lead-engine` — the exact next route (full engine + 30-day plan)
- `/pt-x-acosta-reach` — craft pass on the first magnet post once the spine exists
- `/paolo-trivellato` — front door if a lighter persona-first pass is wanted
- Farrice blind pass (5 min, promotes A-tier): read `extractions/paolo-trivellato-lead-magnet-engine/blind-pass-generated-01.md` beside the two reference-corpus pieces, then `python3 execution/blind_pass.py record --expert paolo-trivellato-lead-magnet-engine --verdict PASS|FAIL --notes "..."`

## Exact Next Prompt
```text
/pt-lead-engine Proof-to-Market $2,500 10-day sprint for supplement/performance brands — build the full engine: pain map from our supplement-brand call transcripts (ask me where they live if not found in _active/linkedin-launch/ or projects/), my authority line, profile rebuild, and the first comment-gated lead magnet. VOICE-CARD layer on, compliance = outputs/time specificity, never income claims.
```

## Acceptance Criteria
- Engine document per engine-30-day-plan.md Output Contract: quoted pain map, authority line ≤8 words, profile directives, 7-day rotation, magnet #1 (post + resource outline), capture scripts, E1–E5 outline, ascension outline, 30-day plan — core ≤2 pages.
- Every pain quoted from real transcripts or explicitly deferred to Week-0 research calls.

## Risk Notes
- Compliance: supplement niche — no income/health claims; specificity moves to outputs/time (per the compliant-grip rule in the 2026-07-07 solution card).
- Voice: anything shipped under Farrice's name needs VOICE-CARD + dial; felt verdict wins.
- Self-reported numbers (Paolo/Kyle/Starborn site) must stay labeled self-reported in any client-facing material.
