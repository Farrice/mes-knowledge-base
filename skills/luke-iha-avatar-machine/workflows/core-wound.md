---
description: Excavate a market's Core Wound via the Ontological Resource Matrix, predict the wound, and write rub-salt messaging
tier: 1
stacks_with: luke-iha-vsl-leads, mcraney, dai-media
---

# Core Wound Excavator

Finds the single fear under all of a market's pain. Every market refracts the universal Core Wound (annihilation/abandonment/death) through the specific **Ontological Resources** it leans on to feel safe.

## Pre-Flight Gate
- Market named + at least a rough pain picture (run `/pain-matrix` first if not).
- Don't stop at "fear of failure" — that's the floor. Push to the *specific refraction* tied to ranked resources.
- The wound is real human pain. Excavate it to *serve* the market better, not to manipulate (the system's stated ethic: this is used to guide prospects toward decisions in their interest).

## PHASE 0 — GROUND (auto-fires; skip with `--no-ground`)
Per `references/research-spine.md`. The wound + Ontological Resource ranking must come from the market's OWN fear language, not invention.
- If the dossier exists, mine `voc-pack.md` for the rawest fear/shame soundbites (Reddit is the best source for taboo fears).
- Standalone & not `--no-ground` — route through the ONE grounding chokepoint (it fires Gemini synthesis + free Reddit/HN + Apify VOC in one pass, reuses a fresh dossier at **$0**, cold-starts paid only on a cache miss):
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --tier deep 2>/dev/null \
  || echo "DEGRADE → mcp__perplexity-ask__perplexity_research for verbatim fear quotes; else [MODELED]"
```
- Rank the Ontological Resources off real fear-of-loss signal. The rub-salt message reuses verbatim phrasing where possible.

## Skill Acquisition
Load `references/framework-library.md` § C (12 resources, the matrix structure). Load genius.md Pattern 2 + Signature Move 2.

## Execution
1. **Build the Ontological Resource Matrix** — for each relevant resource (from the 12), a row:
   `Resource | Inherent or Earned | Intensity (1–10) | Fear-of-Loss vs Desire-to-Gain | Description (this market)`.
   Include only resources that actually load for this market; rank by intensity.
2. **Core Wound prediction** — one tight paragraph: the specific refraction (e.g., "fear of being replaced by younger men," "fear of becoming invisible/irrelevant"). Name the top inherent-resource-lost — that's usually the epicenter.
3. **Rub-salt message** — a short, vivid passage that threatens the highest-intensity fear-of-loss resources (this becomes Dark-Night / agitation fuel). Keep it sensory and specific, never clinical.
4. **Garden-of-Eden seed** — one line describing the *reverse* of the wound (feeds `/anti-hero-journey`).
5. **Desire Daisy-Chain seed** — chain the wound's inverse: benefit → feeling → relationship → identity.

## Content Type Adaptations
| Market | Likely epicenter |
|---|---|
| Aging / beauty | Youth + attractiveness (inherent, fear-of-loss) → invisibility/replacement |
| Men's health / dating | Vitality + power + status → replacement/emasculation |
| MMO / biz-opp | Independence + status + power → entrapment/failure-as-provider |
| Parenting | Relationships (the child) → failure as guardian |

## Output Requirements
- Resource matrix table (ranked) + 1-paragraph wound prediction + rub-salt passage + Eden seed + daisy-chain seed.

## Quality Gate
Rubric criterion 2 (Core Wound depth) ≥8: specific refraction tied to a ranked resource matrix, not a generic fear. Auto-fail: "fear of failure/missing out" with no resource grounding; rub-salt that reads like clinical copy instead of felt threat.
