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

#### Dimension 6: Lived Cultural Connotation (Added 2026-04-11)
*What does the target audience ALREADY feel when they hear this word — based on where they live, what they've experienced, and what emotions the word triggers in daily life?*
- **Test**: Put yourself in the body of someone who has lived in the target geography for 10+ years. Say the name. What's the FIRST image, memory, or feeling? Not the second. Not the "well, if you think about it differently." The first.
- **High score (8-10)**: First association is neutral-to-positive AND aligned with the brand's emotional territory (e.g., "Daybreaker" — first association is dawn, new energy. Positive and aligned).
- **Low score (1-4)**: First association is negative, painful, or misaligned with brand intent (e.g., "Lake Effect" in Chicago — first association is snow, frozen pipes, car won't start).
- **Auto-eliminate at 3 or below**: If the target audience's first association is negative, no amount of "reframing" saves it. The name fights the audience's lived experience on every impression.
- **Critical rule**: This dimension CANNOT be scored by the naming team alone. It requires validation from someone with lived experience in the target geography or culture. If no one on the team has that experience, ASK before presenting. A confident presentation of a culturally tone-deaf name is worse than a hesitant presentation of a mediocre one.
- **Origin**: Naming sprint produced "Lake Effect" and "Thaw" for a Chicago event brand. Both scored 8.6+ on dimensions 1-5. Both were immediately disqualified by a 30-year Chicago resident because the cultural connotations (winter misery, scraping windshields) were the opposite of the brand's intent. Rigorous methodology, 2/10 output.

#### Compounding Defensibility Score
- Calculate average across **6** dimensions
- **8+ = Compounding Asset** — this name will be worth MORE in 5 years than today
- **6-7 = Neutral** — name serves the brand but doesn't actively compound
- **Below 6 = Depreciating** — name will require increasing marketing spend to stay relevant
- **Auto-eliminate any name scoring below 4 on ANY single dimension** — one fatal weakness overrides overall average
- **Auto-eliminate any name scoring 3 or below on Dimension 6** — culturally tone-deaf names are trust-destroying

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
- [ ] Compounding Defensibility Audit completed for all finalists (all 6 dimensions)
- [ ] No finalist scores below 6 on Compounding Defensibility
- [ ] No finalist scores below 4 on any single compounding dimension
- [ ] **Dimension 6 (Lived Cultural Connotation) validated by someone with target-geography lived experience** — if no validator available, flag uncertainty explicitly in presentation
- [ ] **Emotional Alignment Check**: Do the finalists carry the same emotional energy the client originally fell in love with? If client loves rhythm/vibration and you're presenting weather words, you've failed regardless of scores
- [ ] **Confidence Calibration**: Score reflects output quality, not just process adherence. Ask: "Would I stake my reputation on recommending this name to a real person?" If hesitation, re-evaluate before presenting with high confidence

> **Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.

> **Added 2026-04-11**: Three new gate items after a naming sprint passed all original gates at 9.3/10 while producing culturally tone-deaf output. Process rigor ≠ output quality when inputs are flawed.
