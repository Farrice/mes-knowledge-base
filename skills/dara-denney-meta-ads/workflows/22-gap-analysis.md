---
description: "Dara's three-gap audit of a live ad account — persona gaps, awareness-level gaps, creative diversity gaps — cross-analyzed against the persona deck, with every proposed concept tracing to a named gap"
---

# `/dara-gap-analysis` — The Three-Gap Creative Ecosystem Audit

Where strategy actually lives: **"real creative strategy lies in the current gaps that your current strategy has."** This audit cross-analyzes the evidence-ranked persona deck against what's ACTUALLY running in the ad account, then names the gaps a roadmap must close. Every concept downstream must answer: why this creative? why this persona? why this angle? — is there a gap being filled?

## Genius Context (Load First)

Read `genius.md` — Creative Strategy OS layer:
- **Pattern 17**: Three-Gap Diagnosis Before Any Concept
- **Pattern 15**: Persona Injection for Net-New Audiences
- **Pattern 16**: Winner × Persona Replication
- Hidden knowledge: Meta Ad Library top-impressions ranking misleads — read past it to infer the real top performer
- Platform trends are macro (EGC, partnership ads) — a layer above formats

## Input Required

- **Persona deck** (from `/dara-persona-intel`)
- **Live account view**: client reporting export, OR public recon via Meta Ad Library (`/ad-spy` or Playwright — free; filter Active, note Library IDs, durations, "N ads use this creative")
- **Organic surfaces**: the brand's social channels (for the organic-echo check and creator-diversity read)

## Execution

1. **Inventory the live account** — for each running ad: persona targeted (infer from callouts/casting/messaging), awareness level (Schwartz ladder), format archetype, angle. Long-running ads + high "N ads use this creative" = likely winners. **Do not trust the impressions ranking** — infer the real top performer (longest-running + most duplicated + boring-but-persistent beats a flashy high-impression static).
2. **Gap 1 — Persona gaps**: deck vs account. Which evidence-ranked personas are untargeted? Which are over-indexed relative to their evidence volume/emotional intensity? Flag the hot-but-underrepresented quadrant as priority.
3. **Gap 2 — Awareness-level gaps**: distribution of ads across awareness levels. The classic finding: over-index on MOF/BOF, top performers are BOF/offer-oriented → diagnosis = build TOF to feed the ecosystem while keeping the BOF winners running.
4. **Gap 3 — Creative diversity gap**: does the account show multiple personas × 2-3 unique pillar angles each × a range of awareness levels per persona? Plus creator-program diversity: lifestyle, gender, age, jobs, vibes. (Rhode standard: ZERO partnership ads in the account = an easy format unlock hiding in plain sight.)
5. **Platform-trend scan** (macro, above formats): EGC/behind-the-scenes presence? Partnership ads? Whatever the current macro trends are — is the brand riding or absent?
6. **Organic-echo check**: is the paid strategy reflected in organic? A strategy that only exists in the ad account isn't validated yet.
7. **Synthesize** — ranked gap list, each with: the gap, its evidence (deck receipts + account inventory), the closing move (concept direction + entry format + persona), expected effect. Include the **winner × persona replication matrix** as the cheapest gap-closer when winners exist.

## Output Schema

- Account Inventory table (ad → persona / awareness / format / angle / winner-likelihood)
- Gap 1/2/3 findings, each: evidence → diagnosis → closing moves
- Platform-Trend + Organic-Echo verdicts
- Ranked Gap-Closing Concept Directions (each traces to a named gap — the Oats "FULLNESS CHASER ← satiety gap" standard)
- Handoff: "Feed to `/dara-creative-roadmap` for sequencing; `/dara-mission-doc` for the strategy narrative."

## Context Adaptations

| Context | Adaptation |
|---|---|
| Brand client (account access) | Full audit on real performance data |
| Prospect / spec work | Public-only version via Meta Ad Library + organic channels — this IS Dara's pre-pitch 5-minute move, scaled up; devastating in a pitch |
| Personal brand | "Account" = your content calendar; personas = audience segments; diversity gap = pillar × format × awareness coverage of your posts |

## Quality Gate

- All three gaps assessed (a persona-only audit = fail).
- Winner inference reasoned, not read off impressions.
- Every proposed concept direction names its gap — orphan concepts are cut.
- Hot-but-underrepresented persona quadrant explicitly addressed.
- STOP CONDITION: if there is no persona deck yet, run `/dara-persona-intel` first — a gap analysis against invented personas is theater.

## When to Return

- Monthly (roadmap input) · after each 30-day test cycle · pre-pitch (public version) · when "we need new ads" is said without anyone naming a gap.
