---
date: 2026-07-15
session: expert-assembly-os build
name: expert-assembly-os-hybrid-casting
problem_class: harness / expert panels / thin coverage
domain: harness
status: proven
problem_signature: "a task needs an expert panel in a domain the roster barely covers, so the panel either seats irrelevant experts or invents composite personas with fabricated credentials, and the roadmap it produces has no observable success criteria"
tags: [expert-panel, casting, personas, roadmap, assemble, coverage]
---
# Expert Assembly OS — Hybrid Casting + Bespoke Synthesis

**Date**: 2026-07-15  
**Problem solved**: Build a world-class expert panel system that works for ANY domain — roster-first where coverage is strong, synthesized bespoke composite personas where coverage is thin/absent. Emit deterministic roadmap with observable success criteria. No fabricated statistics.

**Context**: Farrice's most-beloved claude.ai creation was the Expert Assembly system (v1–v4, ~29 conversations across wildly diverse domains, proven "any domain" value). Rebuild it for Claude Code: production-grade, hybrid casting (roster + bespoke), persona synthesis without fake stats, multi-round deliberation, observable roadmaps with 3-horizon success criteria, panel persistence across turns.

---

## The Solution

### Architecture (3-part wire + 8-phase workflow)

**Wire 1 — Coverage Detection** (`execution/panel_cast.py`)
- Parses required domains from task
- Scores each domain against 227-card roster (keywords + ratio)
- Classification: STRONG (≥2 keyword hits + ≥50% ratio OR single-keyword domains with ≥1 hit), THIN (≥1 hit, lower ratio), ABSENT (no matches)
- Output: panel plan with roster seats + bespoke slots + governor pre-assignment (Spine/Mechanism/Differentiator/Craft/Risk Gate; Farrice = Function Owner)

**Wire 2 — Persona Synthesis + Linting**
- Compressed McClain protocol (5-step: identity, backstory, worldview, voice, methodology + narrative assembly)
- Full depth (contradictions, genius path, signature moves) but ZERO fabricated stats ($ claims, %, real company names without source URLs, false org attributions)
- Deterministic gate: `execution/persona_stat_lint.py` flags any synthetic credential without source; regenerate on FLAG (max 2 retries), then strip to methodology-only if still blocked

**Wire 3 — Roadmap Synthesis**
- 3-horizon observable structure: Operational 0–30d / Tactical 1–6mo / Strategic 6–12mo
- Per-move schema: Move | Owner | Success Criteria (specific numbers, dates, observable signals) | Dependencies
- Grounding gate: `execution/grounding_guard.py --task-type Strategy` blocks strategic claims on delivery

**Workflow Engine** (`.agent/workflows/expert-assembly.workflow.js`)
- Cloned from `collective-genius-council.workflow.js`; seams at hybrid casting (lines 63–79) and deliberate/synthesize (lines 122–174)
- 8 phases: Scope → Cast → Forge → Ground → Diverge → Deliberate → Synthesize → Close
- Output: `outcome.md` with all schema sections + grounding verdict + session digest + pinned thread (`assemble-<slug>`)

### Execution Path

1. **Scope**: User states task; system extracts required domains
2. **Cast**: `panel_cast.py` detects coverage (strong/thin/absent per domain); emits panel plan
3. **Forge**: One `agent()` per bespoke slot; compressed persona-synthesis prompt; lint gate with 2-retry regenerate + strip fallback
4. **Ground**: (Optional) Council.md Step 2.5 Research Grounding Pass; verify critical factual surface; flag contradictions
5. **Diverge**: All panelists give independent takes (no anchoring)
6. **Deliberate**: 2 rounds of cross-talk; genuine collision; contradictions preserved as "forks"
7. **Synthesize**: Net-new principle + crux statement + roadmap (Strategic/Tactical/Operational with observable success criteria)
8. **Close**: Digest to `knowledge/assembly-sessions/<date>-<slug>.md`; pin thread for `/panel-sync` reload; finalize to ledger

### Panel Persistence

- Session pin threads pin-id `assemble-<slug>` with full panel roster + personas + methodology
- `/panel-sync` command reloads same panel; user can reconvene on different angle or deepen deliberation
- Original's continuity protocol via `handoff_store.py` + `chain_runner.py finalize`

---

## Key Decisions Locked

1. **Hybrid casting, roster-first**: Extracted experts when coverage STRONG; synthesized bespoke when THIN/ABSENT
2. **No fake stats**: Full McClain depth (backstory, methodology, contradictions) but zero fabricated credentials; authority from specificity not numbers; personas explicitly labeled composite
3. **Deterministic linting**: Blocks $ claims, %, real company names, false org attributions without verifiable source URLs
4. **3-horizon roadmap**: Observable success criteria (not "improve X" but "X reaches Y by DATE"); dependencies mapped; phased execution
5. **Never pin Opus**: Conductor = strongest available model; Sonnet executes; per orchestration-doctrine.md

---

## Verification (All Pass)

- **panel_cast.py CLI**: All-bespoke (sailing rigging: 3 thin/absent → 3 bespoke slots) ✓ and hybrid (LinkedIn: 3 strong → 3 roster, 0 bespoke) ✓
- **Persona linting**: Stat-laden persona FLAGS (5 issues) ✓; clean persona PASS ✓
- **Router keywords**: `/assemble` ranks #1 for "assemble an expert panel"; `/convene` ranks #1 for "convene the council" ✓
- **Registries**: `generate_slash_commands.py` ✓ and `sync_registries.py` ✓ regenerated; commands indexed
- **No regressions**: council_cast.py untouched; /convene workflow unchanged; routing-bindings.md and PRODUCTION_CORE.md properly integrated
- **Chain finalize**: Composite 8.33/10; Intent 9, Expert 8, Adversarial 8 ✓

---

## Deployment & Routing

**Front Door**: `/assemble` + `/panel-sync` (sub-command for reload/reconvene)

**Shims**: `.claude/commands/assemble.md` and `.claude/commands/panel-sync.md` enable discovery

**Routing**: 
- `directives/routing-bindings.md` row: "Thin domain coverage + roadmap synthesis → `/assemble`"
- `execution/workflow_router.py CONTROL_ROUTE_KEYWORDS["assemble"]`: 9 keywords including "domain coverage," "thin coverage," "coverage gaps"
- `PRODUCTION_CORE.md` core entry: "`/assemble` (sub: /panel-sync) — Hybrid expert panel — roster + bespoke composite personas → deliberation → tiered roadmap; the 'I don't know this domain' door"

**Cold-Start Ready**: No prerequisite conversions; user invokes `/assemble "task"` directly

---

## Reuse Instructions

For any domain-uncertainty task:
- User: `/assemble "task description" --domains "domain1,domain2,domain3"`
- System: Detects coverage → seats experts (roster if strong, bespoke if thin/absent) → multi-round deliberation → roadmap with observable success criteria
- Output: `outcome.md` + pinned thread for `/panel-sync` reloads on follow-up

**Extends, never rebuilds**: All wiring is deterministic (panel_cast, lint, router, workflow engine). Future panels inherit the same casting logic, linting gates, roadmap schema.

---

## Notes

- **Determinism**: No LLM-based "should we use roster or bespoke?" decisions. Coverage thresholds are deterministic; panel slot assignment is deterministic.
- **Persona authority**: Composite personas earn credibility through methodological specificity + named signature frameworks (e.g., "Preference Paradox Protocol") — NOT through fabricated stats. Readers trust depth, not numbers.
- **Roadmap observability**: Every success criterion is measurable (not "improve engagement" but "email CTR reaches 15% by 2026-09-30"). Dependencies explicit.
- **Single system, infinite domains**: The sailing rigging example (zero roster coverage, all bespoke) and LinkedIn example (full roster coverage) prove the system works across the coverage spectrum with the SAME casting logic.

**See also**: `skills/expert-assembly-os/SKILL.md`, `.agent/workflows/assemble.md`, `.agent/workflows/panel-sync.md`, `execution/panel_cast.py`, `execution/persona_stat_lint.py`
