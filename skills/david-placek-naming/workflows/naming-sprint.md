---
description: Run a complete brand naming sprint using David Placek's Lexicon methodology — from landscape intelligence through proof-of-concept presentation. Includes Compounding Defensibility Audit (Phase 4.5) to stress-test which names accumulate strategic advantage over time.
---

# Naming Sprint Workflow

## Prerequisites
- Load `skills/david-placek-naming/SKILL.md` (Tier 1)
- For creative/complex naming: also load `genius.md` (Tier 2)

## Steps

> **Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` Decision Framework. Confirm all diagnostic questions are answered.


### 1. Intake Brief
Gather from the user:
- What is being named (company, product, feature, content property)?
- Industry/category
- Target customer
- Competitors and their names
- What does "winning" look like?

### 2. Landscape Intelligence
Deploy the `brand-naming-sprint` prompt Phase 1:
- Map competitive names
- Declare the no-go zone
- Study the product with fresh eyes
- Run the Strategic Question Sequence
- Articulate the creative framework

### 3. Treasure Hunting
Deploy the `brand-naming-sprint` prompt Phase 2-3:
- Run three divergent creative frames
- Hunt across linguistic databases
- Generate 30+ candidates per frame (90+ total)
- Apply the Surprisingly Familiar test
- Score with sound symbolism

### 4. Sound Symbolism Scoring (Optional Enhancement)
If the user wants deeper linguistic analysis, deploy `sound-symbolism-scorer` prompt on the shortlisted names.

### 4.5. Compounding Defensibility Audit

**Purpose**: Predict which shortlisted names accumulate strategic advantage over time versus which names peak at launch. Most naming evaluation tests present-state qualities (originality, fluency, surprise). This phase stress-tests for TEMPORAL compounding — the property that makes a name harder to compete with every year it exists.

**Run on the top 5-8 shortlisted names from Phase 3/4. Score each 1-10 on five dimensions:**

#### Dimension 1: Repetition Reward
*Does the name get BETTER the 1,000th time someone hears it, or does it flatten?*
- **Test**: Say the name aloud 10 times rapidly. Does it reveal new sonic textures, or does it become noise?
- **High score (8-10)**: Name has phonemic layers that unfold over repetition (e.g., "Swiffer" — the initial SW-glide, then the crisp FF, then the playful -er). Each repetition reinforces a different quality.
- **Low score (1-4)**: Name is fully consumed on first hearing. No depth. Descriptive names ("FastClean") score low here — the meaning is exhausted immediately.
- **Red flag**: If the name is a pun or wordplay, it WILL flatten. Puns are one-time cognitive rewards.

#### Dimension 2: Semantic Territory Expansion
*Can the name stretch to adjacent meanings as the brand grows, or is it locked?*
- **Test**: Imagine the brand in 3 new categories it doesn't serve today. Does the name still work?
- **High score (8-10)**: Name is evocative but not descriptive — it owns a FEELING or CONCEPT that travels across categories (e.g., "Amazon" — started with books, now means everything-store, because the name evokes vastness, not books).
- **Low score (1-4)**: Name describes the current product literally. "CoachCopy" can never be anything but copywriting for coaches.
- **Decision input**: If the naming brief includes growth ambitions beyond the initial product, weight this dimension 2x.

#### Dimension 3: Competitive Moat Score
*How hard is it for competitors to bracket, dilute, or echo this name?*
- **Test**: Imagine three competitors launching similar products next year. Can they create names that neutralize yours?
- **High score (8-10)**: Name occupies a unique conceptual space that can't be approximated without looking derivative (e.g., "Impossible" for plant-based meat — any competitor using "impossibility" language now sounds like a knockoff).
- **Low score (1-4)**: Name uses category-common modifiers or structures that invite bracketing ("ProCoach" invites "EliteCoach," "MasterCoach," etc.).
- **Key question**: Does this name CREATE a category or DESCRIBE membership in one?

#### Dimension 4: Cultural Drift Resistance
*Will this name age well or is it anchored to a trend?*
- **Test**: Imagine reading this name in a 2035 context. Does it feel dated?
- **High score (8-10)**: Name is anchored to timeless human concepts — nature, sensation, emotion, spatial metaphors (e.g., "Feather" will never feel dated because lightness is permanent).
- **Low score (1-4)**: Name references current slang, tech terminology, or cultural moments that will date (e.g., "MetaCoach" is anchored to 2021-2024 metaverse hype).
- **Era markers to avoid**: AI/Meta/Crypto/Viral/Hack/Disrupt — all signal a specific era.

#### Dimension 5: Network Referral Friction
*How easy is it for someone to tell a friend this name from memory?*
- **Test**: Whisper the name to someone once in a noisy room. Can they spell it? Can they Google it? Can they text it?
- **High score (8-10)**: Name survives the telephone test — one hearing, accurate reproduction, findable via search (e.g., "Sonos" — 5 letters, phonetically unambiguous, no spelling variants).
- **Low score (1-4)**: Name requires spelling out, is easily confused with existing words/brands, or has multiple plausible spellings.
- **Compound effect**: Every referral that fails because someone can't remember or spell the name is LOST compounding. This is the most undervalued dimension in naming.

#### Compounding Defensibility Score
- Calculate average across 5 dimensions
- **8+ = Compounding Asset** — this name will be worth MORE in 5 years than today
- **6-7 = Neutral** — name serves the brand but doesn't actively compound
- **Below 6 = Depreciating** — name will require increasing marketing spend to stay relevant
- **Auto-eliminate any name scoring below 4 on ANY single dimension** — one fatal weakness overrides overall average

#### Integration Rule
If the top-scoring name from Phase 3/4 (creative evaluation) has a Compounding Defensibility Score below 6, ESCALATE: return to the treasure hunting pool and pull the next 5 candidates for this audit. The best name TODAY is not the best name if it depreciates.

### 5. Proof-of-Concept Presentation
Deploy the `proof-of-concept-presenter` prompt:
- Package top 5 names in four real-world contexts each
- Run the one-second believability test
- Score energy assessment

### 6. Deliverable
Present:
- Top 3 recommended names with full rationale
- Sound symbolism analysis
- **Compounding Defensibility Scorecard for each finalist**
- Proof-of-concept mockups
- Positioning line and short brand story for each
- Trademark/cross-language notes

## Quality Gate
- [ ] Minimum 90 raw candidates generated
- [ ] Top 5 shortlisted with scorecards
- [ ] All names presented in context (never on a list)
- [ ] At least one name sits in the tension zone (polarizing)
- [ ] Sound symbolism alignment verified for finalists
- [ ] Compounding Defensibility Audit completed for all finalists
- [ ] No finalist scores below 6 on Compounding Defensibility
- [ ] No finalist scores below 4 on any single compounding dimension

> **Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
