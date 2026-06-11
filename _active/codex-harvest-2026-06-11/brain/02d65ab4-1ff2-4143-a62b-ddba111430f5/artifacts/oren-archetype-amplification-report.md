# Amplification Report: Oren — Brand Social Media Archetypes

## Coverage Summary

| Metric | Count |
|--------|-------|
| Techniques in source | 22 |
| Currently captured (in workflows) | 15 (68%) |
| Latent (in genius.md, no dedicated workflow) | 4 |
| Missed entirely | 3 |

---

## Scan A: Gap Scan — What's Missing?

### MISSED 1: The Boring Industry Excavation Protocol

**Status**: LATENT — Referenced in genius.md Pattern 5 and extraction Pattern 5, but no standalone workflow exists.

**Source quote**: "I don't think anything is too boring. There's a story behind every screw, every bolt, every welding piece."

**Why it matters**: This is the #1 objection from B2B, manufacturing, SaaS, and professional services brands. It's also the #1 diagnostic unlock — the moment a client stops saying "our industry is boring" and starts seeing content gold. Currently, this protocol is embedded inside `/oren-archetype-diagnostic` as a sub-step, but it deserves a standalone workflow because it's a **client-acquisition tool** in its own right. You can run this for a prospect before they even become a client.

**Workflow potential**: HIGH
**Proposed name**: `/oren-boring-industry-excavation`

---

### MISSED 2: The Two-Account Architect

**Status**: LATENT — Documented in genius.md Pattern 4 and extraction Pattern 6, but no workflow builds the actual two-account system.

**Source quote**: "In this two-account method, you're able to post your typical content on main... but then his social media is the real driver."

**Why it matters**: The two-account method is an architectural decision that produces TWO content strategies, TWO editorial calendars, and a cross-pollination system. This is a full engagement — not a sub-step of Oracle. Many founder-led brands need this as a standalone deliverable.

**Workflow potential**: HIGH
**Proposed name**: `/oren-two-account-architect`

---

### MISSED 3: The Archetype-to-Revenue Bridge

**Status**: MISSED — Not in any current workflow or genius.md.

**Source quote** (composite): Oren maps each archetype to a distinct funnel mechanic (Oracle → education → trust → purchase; Helper → ambient recognition → paid ad lift → purchase; etc.) but no workflow exists to translate archetype selection into revenue architecture.

**Why it matters**: This is where the archetype system stops being "content strategy" and becomes "business strategy." The user specifically wants to offer this as an arbitrage service — turning raw concepts into real businesses. The bridge from "you're an Oracle" to "here's your revenue model" is the highest-value deliverable in the chain. It connects Oren's archetype selection to Kallaway's Revenue Ramp, Cole's product vehicles, and the user's own service tier architecture.

**Workflow potential**: HIGH
**Proposed name**: `/oren-archetype-revenue-bridge`

---

### MISSED 4: The Archetype Pitch Deck Generator

**Status**: MISSED — Not captured anywhere.

**Why it matters**: The user wants to productize this as a service. Clients need a deliverable they can hand to leadership, investors, or team members. Oren's "Exercise-as-Deliverable" model produces buy-in in the room — but the client also needs a **leave-behind document** that codifies the archetype selection, resource audit, content roadmap, exemplar proof, and revenue bridge into a professional presentation.

**Workflow potential**: HIGH
**Proposed name**: `/oren-archetype-pitch-deck`

---

### MISSED 5: The Full-Service Brand Architect Pipeline

**Status**: MISSED — No end-to-end workflow exists that chains the entire Oren archetype system from intake to delivery.

**Why it matters**: This is the **productized service workflow**. When the user says "I help someone who has a raw concept and turn it into one of these structured archetypes and plans," THIS is the workflow that orchestrates the full sequence: intake → resource audit → archetype diagnostic → archetype-specific content architecture → revenue bridge → pitch deck → handoff. Currently, the user would need to manually chain 5-6 workflows. This pipeline automates the orchestration.

**Workflow potential**: CRITICAL
**Proposed name**: `/oren-brand-architect-pipeline`

---

## Scan B: Depth Scan — What Could Be Deeper?

### Depth Candidate 1: `/oren-archetype-diagnostic` → Split

**Current state**: Single workflow covering resource audit + archetype matching + content idea generation.

**Split opportunity**:
- `/oren-resource-audit` already exists as a standalone ✅
- The archetype MATCHING logic (cross-referencing resources against archetypes) could be more granular — currently it's "eliminate what doesn't fit" but doesn't score fit quality
- **Proposal**: Add a **fit-scoring matrix** to the diagnostic that rates each archetype 1-10 based on resource alignment, not just pass/fail. This prevents the "well, you could do Oracle OR Helper" ambiguity.

### Depth Candidate 2: `/oren-catalyst-helper-architect` → Split

**Current state**: Combined workflow for two distinct archetypes.

**Split opportunity**: Catalyst and Helper are fundamentally different engagement types:
- Catalyst = aspirational, community-driven, shared because it inspires
- Helper = practical, utility-driven, shared because it solves

These produce different content formats, different engagement metrics, and different funnel mechanics. Combining them in one workflow creates a 50/50 split where neither gets full depth.

**Proposal**: Split into `/oren-catalyst-architect` and `/oren-helper-architect`.

### Depth Candidate 3: `/oren-exemplar-library` → Expand

**Current state**: Provides exemplar examples for client presentations.

**Expansion opportunity**: The library is static. It should include:
- A **research protocol** for finding new exemplars in the client's specific vertical
- An **anti-exemplar diagnostic** (brands doing the WRONG archetype — what it looks like when a brand forces Performer without narrative, or Oracle without expertise)
- A **competitive exemplar scan** — finding what archetype the client's direct competitors are running

**Proposal**: Add "Competitive Archetype Map" sub-section and "Exemplar Research Protocol" to the existing workflow.

### Depth Candidate 4: `/oren-archetype-workshop` → Production Upgrade

**Current state**: Facilitation guide for running the exercise.

**Expansion opportunity**: The workshop workflow describes WHAT to do but not the production assets needed to run it professionally:
- Slide templates / visual aids for presenting each archetype
- Printable worksheets for the resource audit
- Timer/pacing guide for different session lengths (30-min, 60-min, half-day)
- Virtual vs. in-person facilitation differences

**Proposal**: Add "Workshop Production Kit" section with asset specifications.

---

## Scan C: Cross-Expert Stacking Scan — Top Chains

> [!NOTE]
> The genius.md already has a 16-row stacking guide. The following chains are NEW — not currently documented — and specifically oriented toward the user's arbitrage service model.

### Stack 1: Archetype Pipeline × Dai Media Consumer Posture = "Identity-First Brand Architecture"

```
CHAIN: /oren-brand-architect-pipeline → /consumer-posture-profile → /oren-archetype-diagnostic
What it produces: Brand strategy where the archetype is selected not just from resources
  but from the consumer's identity posture — ensuring content speaks to who they ARE,
  not just what they need.
Deploy when: Premium client engagements where "who is your customer?" hasn't been answered.
Steps:
  1. Run /consumer-posture-profile to build the radical individual
  2. Feed consumer posture into /oren-resource-audit (adds a 5th dimension: audience fit)
  3. Run /oren-archetype-diagnostic with consumer + resource data
  4. Select archetype that matches both resource reality AND consumer identity
```

### Stack 2: Archetype Revenue Bridge × Kallaway Revenue Ramp = "Archetype-to-Cash Pipeline"

```
CHAIN: /oren-archetype-revenue-bridge → Kallaway Ramp Architecture → /offer-stack
What it produces: Complete revenue system — from archetype selection through content funnel
  through product/service offer architecture.
Deploy when: Client wants to know "how does this make money?"
Steps:
  1. Run /oren-archetype-revenue-bridge (maps archetype → funnel mechanic)
  2. Apply Kallaway's 4 Blockers to diagnose which funnel stage needs work
  3. Design the content testing protocol (Kallaway batched testing)
  4. Run /offer-stack to build the product/service the funnel converts into
```

### Stack 3: Boring Industry Excavation × Wright Thompson Detail = "Hidden Drama Content"

```
CHAIN: /oren-boring-industry-excavation → /wright-detail → /wright-scene
What it produces: B2B/manufacturing content that reads like magazine-quality narrative —
  not "here's our process" but "here's the story behind the process."
Deploy when: B2B brands that have agreed their industry isn't boring but need
  help making the content compelling, not just informative.
Steps:
  1. Run /oren-boring-industry-excavation to surface 10+ content angles
  2. Select the 3 most dramatic and run /wright-detail (find the one detail that does the work of 50)
  3. Build narrative architecture with /wright-scene
```

### Stack 4: Two-Account Architect × Lara Acosta Revenue Bridge = "Founder + Brand LinkedIn Engine"

```
CHAIN: /oren-two-account-architect → /profile-conversion → /high-dwell
What it produces: Complete LinkedIn implementation of the two-account method —
  founder account optimized for attention, brand account optimized for conversion.
Deploy when: Oracle brands with strong founder personality deploying on LinkedIn.
Steps:
  1. Run /oren-two-account-architect (define account roles, content split)
  2. Optimize founder profile with /profile-conversion (Acosta framework)
  3. Create founder content calendar with /high-dwell (dwell-time optimization)
  4. Build cross-pollination system (founder → brand → conversion)
```

### Stack 5: Archetype Diagnostic × Dunford Positioning = "Positioning-First Archetype"

```
CHAIN: /dunford-positioning-diagnostic → /oren-archetype-diagnostic → archetype architect
What it produces: Archetype selection informed by competitive positioning analysis —
  ensuring the brand doesn't choose the same archetype as every competitor.
Deploy when: Crowded markets where differentiation matters more than execution.
Steps:
  1. Run /dunford-positioning-diagnostic (is the problem actually positioning?)
  2. Map competitor archetypes (competitive exemplar scan)
  3. Select the archetype that creates maximum differentiation
  4. Build content architecture from differentiated archetype
```

### Stack 6: World Builder Architect × Grace Andrews Media Company = "Full Media Brand Build"

```
CHAIN: /oren-world-builder-architect → /grace-city-blueprint → /grace-content-series
What it produces: The World Builder archetype deployed as a full media company —
  not just content, but an entire media property.
Deploy when: Brands with the budget and ambition for the highest-risk, highest-reward archetype.
Steps:
  1. Run /oren-world-builder-architect (creative brief + risk assessment)
  2. Apply /grace-city-blueprint (build the media ecosystem around the brand world)
  3. Design episodic content series with /grace-content-series
```

### Stack 7: Oracle Architect × Sinem Günel Substack = "Expert Newsletter Empire"

```
CHAIN: /oren-oracle-architect → /sinem-publication-setup → /sinem-revenue-architect
What it produces: Oracle-archetype content deployed as a Substack publication with
  the full 4-layer revenue architecture.
Deploy when: Oracle brands or personal brands that want to own their audience,
  not just rent it on social platforms.
Steps:
  1. Run /oren-oracle-architect (3-layer funnel: education → process → product)
  2. Translate to Substack with /sinem-publication-setup
  3. Build revenue layers with /sinem-revenue-architect
```

### Stack 8: Archetype Pipeline × StoryBrand = "Brand Story + Archetype = Complete Positioning"

```
CHAIN: /storybrand → /oren-brand-architect-pipeline
What it produces: Complete brand positioning — StoryBrand provides the narrative
  (hero, guide, plan, call to action), Oren provides the content execution strategy.
Deploy when: New brands or brands undergoing repositioning that need BOTH story and strategy.
Steps:
  1. Run /storybrand for the SB7 BrandScript (who is the hero, what do they want)
  2. Feed BrandScript insights into /oren-resource-audit
  3. Run /oren-archetype-diagnostic (archetype that best serves the brand story)
  4. Build content architecture from archetype
```

### Stack 9: Performer Architect × Georgi Dopamine Hooks = "Addictive Entertainment Content"

```
CHAIN: /oren-performer-architect → /georgi-hook → /georgi-copy
What it produces: Performer-archetype content engineered for dopamine response —
  hooks that stop scrolling + entertainment that builds brand affinity.
Deploy when: Performer brands that need to compete with pure entertainment creators,
  not just other brands.
Steps:
  1. Run /oren-performer-architect (show concept + episode bible)
  2. Engineer hooks with /georgi-hook (dopamine mechanics)
  3. Write episode scripts with omnipresence integration
```

### Stack 10: Archetype Pipeline × Junyuh Identity = "Creator-as-Brand Architecture"

```
CHAIN: /junyuh-identity → /oren-brand-architect-pipeline
What it produces: Personal brand architecture where the creator IS the brand —
  Junyuh's "I Am The Niche" identity mapped to an Oren archetype.
Deploy when: Solopreneurs, coaches, consultants who ARE their business.
Steps:
  1. Run /junyuh-identity (build the identity DNA)
  2. Feed identity into /oren-resource-audit (the person IS the resource)
  3. Select archetype from personal strengths (most solopreneurs → Oracle or Catalyst)
  4. Build content architecture optimized for personal brand
```

### Stack 11: Resource Audit × Rory Sutherland Perception = "Perception-First Resource Reframe"

```
CHAIN: /oren-resource-audit → Rory Sutherland Perception Engineering
What it produces: Resource audit where perceived limitations are reframed as
  strategic advantages — a "boring" factory becomes a "behind-the-scenes" content goldmine.
Deploy when: Brands that HAVE resources but perceive them as liabilities.
```

### Stack 12: Archetype Pitch Deck × Nicolas Cole Digital Product = "Archetype-as-Product"

```
CHAIN: /oren-archetype-pitch-deck → Cole's Vehicle Selection
What it produces: The archetype deliverable itself packaged as a sellable product —
  a diagnostic quiz, a mini-course, or a workshop-in-a-box.
Deploy when: Scaling the arbitrage service beyond 1:1 engagements.
```

---

## Scan D: Non-Obvious Applications

### Application 1: The Archetype Arbitrage Service (CLIENT SERVICE)

**Which technique**: The entire archetype pipeline
**How it applies**: The user packages the full chain — intake → consumer posture → resource audit → archetype diagnostic → content architecture → revenue bridge → pitch deck — as a **productized consulting service**. Price point: $2,500–$5,000 per engagement. Deliverable: a complete brand strategy brief with archetype selection, 20+ content ideas, production specs, and revenue architecture. The client walks away with a **real business plan for their content**, not just "post more."

**Service name suggestion**: "Brand Architect Sprint" or "Archetype Sprint"

**Why this is arbitrage**: The user has 96 expert agents that produce boardroom-quality output in hours. A traditional agency charges $15K–$50K for this work and takes 4–6 weeks. The user delivers the same quality in 48 hours at a fraction of the cost.

### Application 2: The Archetype Self-Assessment Quiz (LEAD MAGNET)

**Which technique**: Resource-Reality Gate + Archetype Decision Architecture
**How it applies**: Build a self-service quiz (5–8 questions mapping to the resource audit + archetype qualifying questions) that prospects take BEFORE engaging. The quiz produces a preliminary archetype recommendation, demonstrates the framework's power, and qualifies the lead. This is the top-of-funnel for the Archetype Arbitrage Service.

### Application 3: The Ghostwriting Archetype Layer (GHOSTWRITING)

**Which technique**: Single-Archetype Discipline + Expert-Adjacency Funnel
**How it applies**: Before writing for any ghostwriting client, run `/oren-archetype-diagnostic` to determine which archetype their content should embody. Currently, the ghostwriting service uses voice matching — but voice without strategic archetype means posts can drift between educational, motivational, and practical without coherence. The archetype becomes the **strategic constraint** that makes every post unmistakably part of a larger system.

### Application 4: Antigravity Expert Onboarding (SYSTEM)

**Which technique**: Exercise-as-Deliverable Model
**How it applies**: Apply Oren's facilitation model to how Antigravity onboards new expert extractions. Instead of presenting a finished extraction to the user, structure it as a facilitated exercise — present options, run diagnostics together, let the user generate deployment ideas. This creates ownership over the extraction and increases the likelihood of actual deployment.

### Application 5: The Archetype Audit for Existing Brands (UPSELL SERVICE)

**Which technique**: Single-Archetype Discipline + Anti-Exemplar
**How it applies**: A lighter-weight service for established brands — audit their current social feed, diagnose which archetype(s) they're accidentally running, identify strategic incoherence, and prescribe a single archetype with transition plan. Price point: $500–$1,500. This is the "foot in the door" offer that leads to the full Brand Architect Sprint.

### Application 6: The Archetype Certification (SCALE PRODUCT)

**Which technique**: The Archetype Workshop
**How it applies**: Package the entire archetype methodology as a certification program for other strategists. The workshop facilitation guide, resource audit template, exemplar library, and pitch deck generator become the curriculum. Other creators, agencies, or freelancers pay to become "Archetype-Certified Brand Strategists." This is the Nicolas Cole "Context Multiplier" — the same IP deployed as a training product.

---

## Proposed New Workflows

| # | Name | Source Technique | Impact | Pairs With |
|---|------|-----------------|--------|-----------|
| 1 | `/oren-brand-architect-pipeline` | Full service chain | CRITICAL | Dai Media, Kallaway, Cole, StoryBrand |
| 2 | `/oren-boring-industry-excavation` | Pattern 5: Nothing Is Too Boring | HIGH | Wright Thompson, Connelly |
| 3 | `/oren-two-account-architect` | Pattern 6: Two-Account Method | HIGH | Acosta, Diandra |
| 4 | `/oren-archetype-revenue-bridge` | Archetype-to-Funnel Translation | HIGH | Kallaway, Cole, Offer Stack |
| 5 | `/oren-archetype-pitch-deck` | Exercise-as-Deliverable exit | HIGH | StoryBrand, Dunford |
| 6 | `/oren-catalyst-architect` | Catalyst split from combined | MEDIUM | Dai Media, Sinem |
| 7 | `/oren-helper-architect` | Helper split from combined | MEDIUM | Junyuh, Noske, Kallaway |

## Depth Expansion Candidates

| Current Workflow | Expansion | Why |
|-----------------|-----------|-----|
| `/oren-archetype-diagnostic` | Add fit-scoring matrix (1-10 per archetype) | Prevents ambiguous "you could be Oracle or Helper" outcomes |
| `/oren-catalyst-helper-architect` | Split into two workflows | Fundamentally different content psychology |
| `/oren-exemplar-library` | Add Competitive Archetype Map + Research Protocol | Makes exemplar discovery systematic, not static |
| `/oren-archetype-workshop` | Add Workshop Production Kit section | Enables professional facilitation at scale |

## Recommended Actions (Priority Order)

1. **BUILD `/oren-brand-architect-pipeline`** — The master orchestration workflow for the arbitrage service. This is the revenue engine.
2. **BUILD `/oren-archetype-revenue-bridge`** — Connects archetype selection to money. Without this, the system is "content strategy" not "business strategy."
3. **BUILD `/oren-boring-industry-excavation`** — Standalone client acquisition tool and diagnostic intervention.
4. **BUILD `/oren-two-account-architect`** — High-demand deliverable for founder-led brands.
5. **BUILD `/oren-archetype-pitch-deck`** — The leave-behind document that makes the service feel premium.
6. **SPLIT `/oren-catalyst-helper-architect`** into two dedicated workflows.
7. **UPDATE `genius.md`** — Add the new stacking chains from this report.
8. **UPDATE `SKILL.md`** — Register all new workflows.
