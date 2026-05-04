---
description: Layered brand-design audit — LIFT score + anti-slop scan + flip-test + memory-encoding check across a brand's visual touchpoints. Comprehensive design diagnostic.
---

# /satori-brand-audit — Layered Brand Visual Audit (Multi-Workflow Stack)

A comprehensive design audit across multiple touchpoints of a brand. Combines LIFT scoring, anti-AI-slop scanning, flip-testing, and memory-encoding evaluation into a single defensible report. The deliverable is a Strategic Visual Brief — what's working, what's failing, what to ship next.

## Pre-Flight Gate

**Use this when**:
- Auditing your own brand (Farrice's brand, Parallax, my.bpm) for visual coherence and quality
- Auditing a client's brand before pitching a redesign or refresh
- Auditing a competitor's brand to identify positioning opportunities
- Pre/post-launch design QA across a launch suite (multiple touchpoints, single brand)

**Do NOT use this when**:
- Auditing a single piece (use `/satori-lift-audit` directly)
- Auditing a brand without authorization (competitive intel is fine; do not output unsolicited audits to a brand you don't represent)
- The brand is at concept stage (no shipped touchpoints yet — too early for audit; use `/satori-why-before-what` on briefs instead)

## Stacks With

- **`jack-roberts-design-mastery`** — particularly `/anti-slop` workflow; this audit chains into Jack Roberts' anti-slop diagnostic for AI-tells layer
- **`creative-direction`** (Creative Director agent) — for art direction recommendations downstream of the audit
- **`design-md`** — if the brand has an existing DESIGN.md, audit findings inform DESIGN.md updates

## Skill Acquisition

Load:
- `genius.md` — all 12 GPs (this audit uses the full Satori stack)
- `references/lift-system-decision-criteria.md`
- `references/source-quotes.md`

## Execution

### Step 1: Touchpoint Inventory

List the brand's visual touchpoints to audit. Group by category:

**Required minimum (≥4 touchpoints)**:
- Logo / brand mark
- Primary website / landing page hero
- Social media presence (1-3 representative posts/tiles)
- One marketing piece (poster, ad, email header)

**Recommended additional**:
- App icon (if applicable)
- Email signature / templates
- Pitch deck cover
- Merch / physical (if applicable)
- Listing card / product card
- Newsletter visual

For each, capture: file path / URL / screenshot, brief description.

### Step 2: Establish Brand Foundation

Document the brand's current foundation (gather from existing materials, brand book, or infer):

- **One-sentence brief**: what the brand promises (audit each touchpoint against this later)
- **Visual primitive**: which line type / geometry / motif dominates current materials
- **Voice / tone**: warm / cool / authoritative / playful / etc.
- **Predictive empathy intent**: what end-emotion the brand wants viewers to carry
- **Memory hook**: what's the ONE thing that lodges in memory about this brand?

If foundation is unclear or missing, **flag this as a top-level audit finding** before touchpoint scoring. Foundation gaps cause downstream visual incoherence.

### Step 3: Per-Touchpoint Scoring

For each touchpoint, run the full audit chain:

#### Layer 1 — LIFT Score (composition integrity)
- L (Leverage): score 1-10
- I (Eye Choreography): score 1-10
- F (Friction): score 1-10
- T (Transferability): score 1-10
- Composite + grade

#### Layer 2 — Anti-AI-Slop Scan
- Count of AI tells present (high-severity weight 2x, medium 1x)
- Imperfections present (count)
- Anti-slop signal: STRONG / MEDIUM / WEAK / ABSENT

#### Layer 3 — Flip-Test Findings
- 6-check structural audit
- High-severity issues count
- Pre-delivery readiness: READY / REWORK / MAJOR REWORK

#### Layer 4 — Memory Encoding Check
- Resolve-something present? Yes/No
- 24-hour predicted recall: specific element / nothing
- Stickiness verdict: ENCODED / FORGETTABLE

#### Layer 5 — Foundation Alignment
- One-sentence brief: aligned / contradicted / silent
- Visual primitive: aligned / contradicted / silent
- Voice / tone: aligned / contradicted / silent
- Predictive empathy intent: aligned / contradicted / silent

### Step 4: Cross-Touchpoint Coherence

After per-touchpoint scoring, audit cross-touchpoint patterns:

- **Visual primitive consistency**: Does the same primitive appear across touchpoints?
- **Palette discipline**: Are accent colors used in ≤1 zone per piece, AND consistent across pieces?
- **Type system**: Same type families across touchpoints? Scale ratios consistent?
- **Memory-hook coherence**: Do touchpoints reinforce ONE memory hook or do they fragment?
- **Voice / tone consistency**: Does the brand "sound the same" across pieces, or does it shift?

Each cross-touchpoint finding gets its own row in the report.

### Step 5: Pattern Analysis

Identify recurring failure patterns across the audit:

| Pattern | Touchpoints affected | Likely root cause |
|---|---|---|
| LIFT-T failure (transferability) | 3 of 5 touchpoints fail thumbnail | Hero photo always positioned bottom-right; doesn't survive crop |
| Predictive empathy: loud-default | 4 of 5 touchpoints over-loud | Brand inherited "we have to shout to be heard" assumption from old positioning |
| Memory encoding: hand-delivery | All 5 touchpoints score forgettable | No resolve-something move ever deployed; brand is "professionally clean" without lodge |
| Anti-AI-slop: weak | All 5 touchpoints AI-tell-heavy | System-level imperfections never specified; AI defaults dominate |
| ... | ... | ... |

Root causes drive the strategic recommendations in Step 6.

### Step 6: Strategic Recommendations

Produce 3-7 strategic recommendations ordered by impact:

For each recommendation:
- **Recommendation**: one-sentence directive
- **Why it matters**: linked to audit findings + business impact
- **Touchpoints affected**: list
- **Implementation level**: token (DESIGN.md edit) / component / piece-level
- **Sequencing**: do this 1st / 2nd / 3rd
- **Expected outcome**: what the audit would show 30-60 days post-implementation

**Example recommendation**:
> **R1 — Inject memory-encoding moves at the system level (DESIGN.md token addition).**
> Why: 5 of 5 touchpoints score "forgettable" — brand has no encoding discipline.
> Touchpoints affected: all.
> Implementation: token addition (1 day) + per-touchpoint application (2-3 weeks).
> Sequencing: 1st priority — touches everything.
> Expected outcome: at re-audit, 3+ touchpoints score ENCODED with specific recall.

### Step 7: Output the Brand Audit Report

```markdown
# Brand Visual Audit — [brand name]
**Date**: [...]
**Touchpoints audited**: [n]
**Auditor scope**: [self-audit / client / competitive intel]

## Executive Summary
- Overall composite LIFT grade: [A/B/C/D/F]
- Anti-AI-slop posture: [STRONG/MEDIUM/WEAK/ABSENT]
- Memory encoding posture: [ENCODED/FORGETTABLE]
- Foundation clarity: [CLEAR/PARTIAL/UNCLEAR]
- **Top finding**: [one sentence — the highest-impact pattern]

## Brand Foundation
- One-sentence brief: [...]
- Visual primitive: [...]
- Voice / tone: [...]
- Predictive empathy intent: [...]
- Memory hook: [...]
- Foundation gaps: [list, if any]

## Per-Touchpoint Audit

### Touchpoint 1 — [name]
| Layer | Finding | Score |
|---|---|---|
| LIFT | [composite + per-dimension] | [composite/40] [grade] |
| Anti-AI-slop | [tells / imperfections] | [STRONG/MED/WEAK/ABSENT] |
| Flip-test | [issues found] | [READY/REWORK/MAJOR] |
| Memory encoding | [hook present? recall?] | [ENCODED/FORGETTABLE] |
| Foundation alignment | [...] | [aligned/contradicted/silent] |

### Touchpoint 2 — [name]
[same structure]

[continue per touchpoint]

## Cross-Touchpoint Coherence
| Dimension | Finding |
|---|---|
| Visual primitive consistency | [...] |
| Palette discipline | [...] |
| Type system coherence | [...] |
| Memory-hook coherence | [...] |
| Voice / tone consistency | [...] |

## Pattern Analysis
| Pattern | Touchpoints affected | Root cause |
|---|---|---|
[multi-row]

## Strategic Recommendations

### R1 — [directive]
- Why: [...]
- Touchpoints: [...]
- Level: [token / component / piece]
- Sequence: [1st / 2nd / 3rd]
- Expected outcome: [...]

### R2 — [directive]
[same structure]

[continue]

## Next Workflows
- For each touchpoint scoring REWORK or worse, route to: [/satori-lift-audit, /satori-anti-ai-slop, /satori-memory-encoding, /satori-flip-test]
- For system-level recommendations: route to: [/satori-design-md-grid (if DESIGN.md exists), /satori-why-before-what (if foundation gaps)]
- For art direction across redesign: route to: [/art-direct (Creative Director)]

## Re-Audit Plan
- Recommended re-audit date: [30-60 days post-implementation]
- What to compare: [specific dimensions where recommendations should move scores]
```

## Content Type Adaptations

| Brand type | Audit emphasis |
|---|---|
| **Personal brand (creator)** | Voice/tone consistency across LinkedIn / newsletter / podcast cover; one memory hook |
| **E-commerce brand** | Product card consistency + email visuals + IG + storefront; transferability is critical |
| **SaaS / tech** | Web hero + dashboard + onboarding + docs; LIFT-I (clarity) over memory encoding |
| **Streetwear / lifestyle** | Capsule launch suite + IG + merch + posters; high anti-slop expectation; memory encoding mandatory |
| **Real estate broker** | Listing cards + agent profile + email signature + storefront; trust signals + LIFT-T |
| **Newsletter / publication** | Header + post visuals + Notes / social share images + paywall page; voice + memory |
| **Hospitality / restaurant** | Storefront + menu + IG + delivery packaging; warmth + transferability |
| **Children / family** | Anti-slop is delicate (warmth, not edginess); memory encoding via delight |
| **Premium / luxury** | LIFT-F (restraint) + LIFT-T + memory encoding via subtlety |
| **Real estate listing-suite (Jen)** | Cross-listing consistency + per-listing LIFT |

## Output Requirements

Report must include:
1. Executive summary (composite grades + top finding)
2. Brand foundation documented (gaps flagged if present)
3. Per-touchpoint scoring (≥4 touchpoints, all 5 layers each)
4. Cross-touchpoint coherence audit (5 dimensions)
5. Pattern analysis with root causes
6. 3-7 strategic recommendations (impact-ordered, with sequencing + expected outcomes)
7. Next-workflow routing recommendations per touchpoint
8. Re-audit plan

## Quality Gate (Genius Rubric)

- [ ] **≥4 touchpoints** audited
- [ ] **All 5 layers** scored per touchpoint (LIFT + anti-slop + flip + memory + foundation)
- [ ] **Cross-touchpoint coherence** examined (not just per-piece scoring)
- [ ] **Pattern analysis with root causes** (not just symptom listing)
- [ ] **Recommendations sequenced** by impact (highest impact first)
- [ ] **Implementation level specified** per recommendation (token / component / piece)
- [ ] **Re-audit plan** documented (specific dimensions to recheck)

## Source Grounding

This workflow combines the entire Satori stack:
- GP-01 (Why-Before-What) for foundation alignment
- GP-04 (Movement Ladder) absorbed into LIFT-I scoring
- GP-05 (Grid Taxonomy) absorbed into LIFT-I + transferability
- GP-06 (LIFT System) as the primary scoring layer
- GP-11 (Anti-AI-Slop) as Layer 2 scan
- GP-12 (Flip Test) as Layer 3 structural check
- GP-03 (Memory Encoding) as Layer 4 stickiness check
- GP-02 (Predictive Empathy) absorbed into foundation alignment

> *"A great design doesn't just look good once. It works across every format, every size, every platform."* — Satori on transferability, applied at brand-system scale here

## Memory Note

For self-audit of Farrice's own brand work, cross-reference auto-memory:
- `project_parallax-substack-live.md`
- `mybpm-streetwear-brand.md`
- `niche-positioning-locked.md`
- `deep-icp-primary-reference.md`

These provide the foundation context the audit measures touchpoints against.
