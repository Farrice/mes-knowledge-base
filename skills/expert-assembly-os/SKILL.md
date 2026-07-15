---
name: Expert Assembly OS
description: Hybrid expert panel system — roster selection + bespoke persona synthesis + multi-round deliberation + tiered implementation roadmap for any domain.
routing: long-tail
status: active
---

# Expert Assembly OS

Assemble a world-class expert panel for any task. The system detects domain coverage gaps in the 227-card roster, seats strong matches directly, synthesizes bespoke composite personas where coverage is thin, runs genuine multi-round deliberation, and emits a tiered roadmap (strategic 6–12mo / tactical 1–6mo / operational 0–30d) with observable success criteria.

This is the production-grade rebuild of Farrice's beloved claude.ai system prompt that made him confident in any domain.

## When to Use

- **Any unfamiliar domain**: "I don't know this space; I need world-class thinking."
- **Complex multi-perspective work**: Requires 3–5 distinct lenses colliding.
- **Roadmap + synthesis deliverables**: Task needs both analysis AND a tiered execution plan.
- **Composite credentials acceptable**: When fabricated stats are poisonous, synthesized methodology is gold.

## When NOT to Use

- Single expert question → `/[expert-name]` (direct expert dispatch)
- Roster only, no deliberation → `/convene` (lighter, faster council)
- Pure research, no panel synthesis → `/deep-research` or `execution/research.py`
- Exploration mode, no roadmap needed → `/wayfinder-work`

## Core Concepts

**Hybrid Casting**: `panel_cast.py` scores each required domain (strong/thin/absent) against the invocation-card roster. Strong domains get extracted experts. Thin/absent domains get synthesized bespoke personas.

**Coverage-Aware**: Three-tier status per domain:
- **Strong** (≥2 keyword hits + ≥50% ratio): seat roster expert directly
- **Thin** (≥1 keyword hit, lower ratio): synthesize composite lens
- **Absent** (no matches): synthesize composite lens focused on domain

**Governor Slots**: Panel slots pre-assigned (Spine/Mechanism/Differentiator/Craft/Risk Gate) so workflows can reference them. Farrice always Function Owner.

**Composite Personas**: Full McClain depth (backstory, methodology, worldview, voice, contradictions, messy details) with ZERO fabricated stats. Composite label explicit; authority from specificity, not numbers.

**Multi-Round Deliberation**: 
1. Diverge — each panelist gives their distinctive take
2. Deliberate Round A — cross-talk, builds, challenges, cross-pollination
3. Converge — synthesize crux, net-new principle, forks for decision-maker

**Observable Roadmap**: Three horizons with specific success criteria (not "improve" but "X reaches Y by DATE").

## Files

- `SKILL.md` (you are here)
- `references/persona-synthesis-prompt.md` — compressed McClain Steps 1–4+6
- `references/roadmap-schema.md` — output contract with all sections
- `references/lineage.md` — v1→Virtuoso design requirements → where each landed

## Workflows

- `/assemble` — full pipeline (Scope → Cast → Forge → Deliberate → Synthesize → Close)
- `/panel-sync` — reload pinned panel in a follow-up turn (continue deliberation/refinement)

## Sub-Agents & Parallel Surfaces

This skill is **Workflow-first, plugin-deferred**. Runs on the native `.agent/workflows/` engine (expert-assembly.workflow.js). Plugin packaging comes after production proof.

## Integration

Extends `/convene` (roster-only council) with:
- Coverage detection (thin/absent slots get synthesized)
- Persona-synthesis gate (lint-blocked fake credentials)
- Roadmap emission (3-horizon structured plan)
- Session pin recovery (`/panel-sync` reload)

Never pins Opus; uses strongest available model for conductor, Sonnet for execution (per orchestration-doctrine.md).

## Examples

### Example 1: Zero-Coverage Domain
Task: "competitive sailing rigging optimization"
Domains: "rigging engineering, sailing performance, composite materials"

→ All domains thin/absent in roster
→ 3 bespoke composites synthesized
→ Deliberation: collision between aerodynamics + materials science + competitive positioning
→ Roadmap: operational moves for rig audit + testing; tactical for prototyping; strategic for market positioning

### Example 2: Hybrid Coverage
Task: "LinkedIn content strategy for a premium coaching offer"
Domains: "linkedin growth, offer positioning, content strategy"

→ 2 strong matches (Tommy Clark, Ross McKay) from roster
→ 1 thin domain gets composite synthesis
→ Deliberation: roster voices + synthesized lens = integrated strategy
→ Roadmap: operational content calendar; tactical offer architecture; strategic brand positioning

## Verification Gate

Every persona synthesized is scanned by `persona_stat_lint.py`:
- Flags fabricated stats (% claims, $ figures, market sizes without disclaimer)
- Enforces composite label presence
- Blocks real company names in credentials
- If flagged: regenerate (1 retry), then strip to methodology-only if still blocked

Roadmap claims pass `grounding_guard.py --task-type Strategy` before delivery.

## Next Steps

Questions? See `/assemble` for the front-door workflow and full manual runbook.
