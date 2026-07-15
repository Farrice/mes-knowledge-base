# Expert Assembly OS — Design Lineage

How Farrice's claude.ai system prompt (v1→Virtuoso) became a production-grade skill.

---

## Original System (claude.ai, 2024–2025)

**Capability**: Generate a bespoke panel of 3–5 world-class experts for ANY domain, run genuine deliberation, deliver synthesis + tiered implementation roadmap.

**Proof**: ~29 conversations across wildly diverse domains (creative strategy, nonprofit scaling, AI ethics, fitness coaching, real estate, spirituality). Consistently outperformed single-expert advice.

**Design iterations**:
- v1: Basic roster panel + synthesis
- v2: Added panel persistence across turns, evidence validation, proactive guidance
- v3/v4: Added metacognitive monitoring, adaptive depth, collaborative checkpoints
- Unified Virtuoso: Integrated all feedback

---

## Design Requirements (Extracted from Iterations)

### Requirement 1: Panel Persistence Across Turns
**Origin**: v2 feedback showed one-shot panels lost continuity. Farrice wanted to say "continue with this panel" in a follow-up message.

**How It Landed**: Session pins in `.tmp/assemble/<slug>/panel.json` + `/panel-sync` command for reload. `handoff_store.py` + `chain_runner.py finalize` wire the persistence.

### Requirement 2: Never Fabricate Evidence
**Origin**: v3 audit found personas padding credentials (fake percentages, company names, attributions). Authority became suspect.

**How It Landed**: `persona_stat_lint.py` gate blocks $ claims, % figures, real company names, false org attributions without URLs. Composite label explicit. Mechanism-led instead of stats-led.

### Requirement 3: Always Guide Proactively
**Origin**: v3/v4 users wanted "here's what to do" alongside "here are perspectives." Synthesis ≠ roadmap.

**How It Landed**: Three-horizon roadmap (Operational/Tactical/Strategic) with Observable Success Criteria (Law 2 of orchestration-doctrine.md). "Improve X" became "X reaches Y by DATE."

### Requirement 4: Self-Monitor Blind Spots
**Origin**: v4 feedback: panels were confident in ways they shouldn't be. Added explicit "what we can't see" section.

**How It Landed**: "Blind Spots the Panel Flagged" section in roadmap-schema.md. Not apologetic, but aware. Surfaced at Converge phase.

### Requirement 5: Operate in ANY Domain
**Origin**: Virtuoso proved it worked for obscure niches (maritime rigging, invisible coaching, spiritual retreats). Never broke when domain was unfamiliar.

**How It Landed**: Hybrid casting via `panel_cast.py`. When roster can't cover a domain (thin/absent), synthesize a bespoke persona rather than forcing a poor match or going empty. Coverage-aware, not roster-constrained.

---

## Architecture Decision: Hybrid Casting

**The Problem**: The 227-card roster covers many domains, but not all. Some tasks need expertise that doesn't exist yet in the extracted roster.

**The Solution**: Coverage-aware casting. Three-tier per domain:
- **Strong** (≥2 keyword hits + ≥50% match ratio): seat roster expert directly
- **Thin** (low hits/ratio): synthesize composite lens
- **Absent** (no matches): synthesize composite lens

This keeps the system "ANY domain" while preserving the extracted-expert quality where possible.

**Implementation**: `panel_cast.py` → `build_panel_plan()` emits roster seats + bespoke slots → `expert-assembly.workflow.js` Phase Forge synthesizes personas → `persona_stat_lint.py` blocks fake credentials → panel deliberates together.

---

## Architecture Decision: Governor Slots

**The Problem**: Panels need structure. Workflows need to reference seats (e.g., "the Risk Gate perspective" in a crisis briefing).

**The Solution**: Pre-assign governor slots (Spine/Mechanism/Differentiator/Craft/Risk Gate) per seat in the panel plan. Farrice always Function Owner.

**Implementation**: `panel_cast.py` Phase Cast pre-assigns slots. `expert-assembly.workflow.js` Phase Diverge references them. Composition Ledger in roadmap shows the assignment.

---

## Architecture Decision: Lint Gate for Personas

**The Problem**: Synthesizing personas risks the same credential-inflation bug that plagued v3.

**The Solution**: Every forged persona is scanned by `persona_stat_lint.py` before use. Flags stats, fake attributions, real company names, missing composite label. If flagged: regenerate (1 retry). If still flagged: strip to methodology-only (keep voice + worldview + signature move, drop stats/backstory).

**Implementation**: `expert-assembly.workflow.js` Phase Forge calls lint gate immediately after synthesis. Workflow logs the verdict. No persona enters Diverge phase if flagged.

---

## Architecture Decision: Roadmap Schema

**The Problem**: v3 "synthesis" was sometimes just summary, not decision-grade roadmap. Users wanted: "here's what to do, in what order, with what success looks like."

**The Solution**: Structured roadmap with three horizons and observable criteria. Claims table for factual grounding. Composition ledger for transparency. Blind spots for meta-awareness.

**Implementation**: `roadmap-schema.md` (output contract). `expert-assembly.workflow.js` Phase Synthesize calls `grounding_guard.py --task-type Strategy` before emission.

---

## Files Mapping: v1→Virtuoso → Skill OS

| Virtuoso Capability | Skill Component | File |
|---|---|---|
| Panel convening | Hybrid casting | `panel_cast.py` + `council_cast.py` imports |
| Roster expertise | Extracted experts | `invocation-cards.md` (227-card roster) |
| Persona synthesis | Bespoke composites | `expert-assembly.workflow.js` Phase Forge |
| Credential blocking | Lint gate | `persona_stat_lint.py` |
| Deliberation | Cross-talk + converge | `expert-assembly.workflow.js` Phases Diverge/Deliberate |
| Roadmap emission | Decision-grade output | `expert-assembly.workflow.js` Phase Synthesize |
| Panel persistence | Session pins | `handoff_store.py` + `/panel-sync` |
| Blind spot tracking | Meta-awareness | `roadmap-schema.md` "Blind Spots" section |

---

## What Changed (vs. claude.ai Original)

### Improvements
- **Deterministic caster** (`panel_cast.py`) replaces LLM-estimated roster picks
- **Lint-gated personas** block credential fabrication automatically
- **Observable roadmap** with success criteria (vs. narrative synthesis)
- **Composition ledger** shows why each seat was filled (transparency)
- **Explicit blind-spot section** surfaces meta-uncertainty

### Constraints Lifted
- No longer restricted to claude.ai system prompt format
- Personas run through deterministic validation gates (not optional)
- Roadmap structure enforced by schema (not left to LLM choice)
- Session persistence via local pins (not dependent on conversation continuity)

### Constraints Added
- Hard no-fabrication rules ($ claims, real company names, false attributions)
- Composite label mandatory (vs. optional transparency)
- Grounding gate on roadmap claims (vs. unverified synthesis)
- Governor slot pre-assignment (structure, but less flexibility)

---

## Next Phases (Deferred)

**Phase 4 — Plugin Packaging**: Once production proof exists (real Farrice usage logging positive outcomes), wrap this as a JCC plugin for multi-agent orchestration.

**Multi-Agent Orchestration**: Expand to swarm-scale (10+ panels running in parallel for mega-missions). Currently 1-panel-per-turn, but foundation supports scaling.

**Continuous Learning**: Panel feedback → solution cards → future panel selection (meta-improvement loop). Documented in Evolution Engine but not yet wired.

---

## Verification Proof Points

The design landed correctly if:

1. ✓ Zero-coverage domains (sailing rigging) get 3 bespoke composites, not empty panel
2. ✓ Hybrid domains (LinkedIn coaching) get 2 roster + 1 bespoke, not all bespoke
3. ✓ Personas flagged by lint gate are regenerated before use
4. ✓ Roadmap emits observable success criteria, not vague narratives
5. ✓ Panel persists via `/panel-sync` across multiple turns
6. ✓ Deliberation produces net-new principles (not just summaries)
7. ✓ Blind spots are authentic (not template checklist)
8. ✓ Router ranks `/assemble` above `/convene` for "panel" + "roadmap" queries
