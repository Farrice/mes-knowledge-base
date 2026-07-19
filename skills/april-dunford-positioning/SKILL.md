---
name: "April Dunford: B2B Positioning & Sales Pitch Architecture"
description: "Position any B2B product using the 5-component methodology, diagnose positioning failures, engineer buyer fear de-risk strategies, and construct sales pitches using the Setup → Follow-Through framework. The world's most actionable system for answering 'Why should customers pick us?'"
version: "3.0"
format: "completion-engine"
workflows: 13
---

# April Dunford: B2B Positioning & Sales Pitch Architecture

Expert extraction from April Dunford's positioning methodology and sales pitch framework, synthesized from two comprehensive interviews on Lenny's Podcast.
April Dunford's core genius: **Positioning is not messaging — it's context-setting.** Set the right context, and your product's value becomes self-evident. Get it wrong, and no amount of great marketing can save you.
She operates two interlocking systems:
1. **The 5-Component Positioning System** — deconstruct competitive alternatives, map differentiated value, sharpen target segments, select market categories, and architect the sales narrative.
2. **The Positioning Intelligence Engine** — diagnose failure modes, map buyer fear psychology, sequence market entry, and bridge positioning into downstream copy execution.

## Available Workflows

### Tier 1 — Foundation (Start Here)

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| diagnostic | [Positioning Diagnostic](workflows/dunford-positioning-diagnostic.md) | Positioning Health Scorecard & Root Cause Analysis | FIRST — before any repositioning. Determines whether the problem is actually positioning, or lead gen/sales execution/PMF. |
| product | [Product Positioning Blueprint](workflows/product-positioning-blueprint.md) | Comprehensive Positioning Strategy Document | Launching a new product, entering a new market, or when current marketing is failing to convert leads. |
| fear | [B2B Decision Fear Architecture](workflows/dunford-fear-architecture.md) | B2B Decision Fear Map & De-Risk Sales Strategy | 40-60% of deals end in no-decision. Maps buyer career risk, committee dynamics, and designs teaching-based de-risk counter-strategies. |
| context | [Market Context Engine](workflows/dunford-context-engine.md) | Market Context Narrative & Opening Scene Script | Build the "Apocalypse Now opening scene" — set Where, When, Who, Vibe before any product details surface. Deploys as sales script, landing page block, or conference opener. |

### Tier 2 — Practitioner

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| sales | [Sales Narrative & Pitch Deck](workflows/sales-narrative-pitch-deck.md) | Strategic Sales Pitch Deck & Narrative Script | The sales team is struggling to differentiate from competitors or the current pitch feels like a feature-dump. |
| deal | [Deal Acceleration & Champion Toolkit](workflows/deal-acceleration-champion-toolkit.md) | Internal Champion Enablement Kit | Deals are stalling in late stages or internal champions are failing to get executive buy-in due to buyer indecision. |
| category | [Category Decision Protocol](workflows/dunford-category-decision.md) | Category Strategy Decision Document | The critical "build or enter?" category decision. Uses the 90/10 rule — 90% of the time, enter and dominate a subsegment. |
| b2bvsb2c | [B2B vs B2C Positioning Bifurcation](workflows/dunford-b2b-vs-b2c.md) | B2B/B2C Positioning Strategy & Translation Guide | Diagnose whether you're playing the B2B or B2C game, catch misapplied playbooks, and handle PLG hybrids. |
| niche | [Niche Domination Sequencing](workflows/dunford-niche-domination.md) | Niche Selection & Bowling Pin Expansion Roadmap | Select the smallest viable niche where you're the ONLY credible answer, dominate it, then sequence expansion through bowling pins. |
| failures | [Positioning Failure Modes](workflows/dunford-failure-modes.md) | Positioning Failure Diagnosis & Recovery Plan | Growth stalled, deals dying, customer confusion increasing. Forensic autopsy of 6 distinct failure modes with recovery protocols. |

### Tier 3 — Strategic & Stacking

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| gtm | [GTM Validation & Expansion Roadmap](workflows/gtm-validation-expansion-roadmap.md) | Sequential GTM Roadmap & Pitch Testing Protocol | Scaling from a single niche to adjacent markets or validating a positioning pivot before a full rebrand. |
| siege | [Positioning Siege Test](workflows/positioning-siege-test.md) | Stress-Tested Positioning with Competitive Resilience Map | Positioning must survive competitive counter-moves, market shifts, and copy attempts. When defensibility matters more than speed. |
| copy-bridge | [Positioning-to-Copy Bridge](workflows/dunford-positioning-to-copy.md) | Copy Brief & Messaging Framework Anchored to Positioning | Translate finished positioning into a structured brief for downstream copy experts (Wiebe, Sultanic, Kallaway). |
| haynes-handshake | [Dunford → Haynes Handshake](workflows/dunford-handshake-haynes.md) | Temperature-Staged Cold-Offer Stack | Positioning is done but the same pitch is firing at cold strangers, warm engaged readers, and hot inbound leads alike — recompose the offer per audience temperature before scaling outbound. |
| godin-handshake | [Godin → Dunford Handshake](../seth-godin-marketing-mind/workflows/16-godin-handshake-dunford.md) | Cleared Premise Card + 5-Component Build | The positioning premise itself has never been interrogated — trap named, fuzzy word split, who's-it-for reset — before a full 5-component build runs on it. Run BEFORE `product`/`diagnostic` when the premise is suspect. |

## Cross-Expert Stacking Chains

| Chain | Sequence | Use Case |
|-------|----------|----------|
| Premise Gate → Positioning | Godin `godin-lens`/`premise-audit` → Dunford `godin-handshake` (5-component build on cleared premise) | Kill a broken premise before spending a full positioning workshop on it |
| Positioning → Cold Offer | Dunford `product` → Dunford `haynes-handshake` → Haynes `jh-value-crosscheck`/`jh-offer-to-copy` | Finished positioning → temperature-staged cold-offer stack → copy execution |
| Positioning → Copy | Dunford `product` → Dunford `copy-bridge` → Wiebe/Sultanic | Strategic positioning → production copy |
| Positioning → Content | Dunford `context` → Kallaway content psychology | Market context → high-retention content |
| Fear → Deal Close | Dunford `fear` → Dunford `deal` | Buyer fear map → champion enablement |
| Diagnostic → Full Rebuild | Dunford `diagnostic` → Dunford `product` → Dunford `siege` | Failure diagnosis → repositioning → stress test |
| Niche → GTM | Dunford `niche` → Dunford `gtm` | Pin 1 selection → expansion roadmap |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

13 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Positioning Diagnostic** — `skills/april-dunford-positioning/references/prompts-v2/01-positioning-diagnostic.md`
- **Competitive Alternative Mapper** — `skills/april-dunford-positioning/references/prompts-v2/02-competitive-alternative-mapper.md`
- **Differentiated Value Chain Builder** — `skills/april-dunford-positioning/references/prompts-v2/03-differentiated-value-chain.md`
- **Target Customer Sharpener** — `skills/april-dunford-positioning/references/prompts-v2/04-target-customer-sharpener.md`
- **Market Category Selector** — `skills/april-dunford-positioning/references/prompts-v2/05-market-category-selector.md`
- **Sales Pitch Architect** — `skills/april-dunford-positioning/references/prompts-v2/06-sales-pitch-architect.md`
- **Insight Reverse-Engineer** — `skills/april-dunford-positioning/references/prompts-v2/07-insight-reverse-engineer.md`
- **Perfect World Bridge Builder** — `skills/april-dunford-positioning/references/prompts-v2/08-perfect-world-bridge.md`
- **Champion Ammunition Kit** — `skills/april-dunford-positioning/references/prompts-v2/09-champion-ammunition.md`
- **Proof Stack Assembler** — `skills/april-dunford-positioning/references/prompts-v2/10-proof-stack-assembler.md`
- **Bowling Pin Strategy Planner** — `skills/april-dunford-positioning/references/prompts-v2/11-bowling-pin-strategy.md`
- **Pitch Testing Protocol** — `skills/april-dunford-positioning/references/prompts-v2/12-pitch-testing-protocol.md`
- **Buyer Indecision Reducer** — `skills/april-dunford-positioning/references/prompts-v2/13-buyer-indecision-reducer.md`

<!-- END:execution-prompts -->
