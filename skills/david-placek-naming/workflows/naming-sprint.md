---
description: Run a complete brand naming sprint using David Placek's Lexicon methodology — from landscape intelligence through proof-of-concept presentation
---

# Naming Sprint Workflow

## Prerequisites
- Load `skills/david-placek-naming/SKILL.md` (Tier 1)
- For creative/complex naming: also load `genius.md` (Tier 2)

## Steps

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


### 1. Intake Brief
Gather from the user:
- What is being named (company, product, feature, content property)?
- Industry/category
- Target customer
- Competitors and their names
- What does "winning" look like?

### 2. Landscape Intelligence
Deploy the `brand-naming-sprint` prompt → Phase 1:
- Map competitive names
- Declare the no-go zone
- Study the product with fresh eyes
- Run the Strategic Question Sequence
- Articulate the creative framework

### 3. Treasure Hunting
Deploy the `brand-naming-sprint` prompt → Phase 2-3:
- Run three divergent creative frames
- Hunt across linguistic databases
- Generate 30+ candidates per frame (90+ total)
- Apply the Surprisingly Familiar test
- Score with sound symbolism

### 4. Sound Symbolism Scoring (Optional Enhancement)
If the user wants deeper linguistic analysis, deploy `sound-symbolism-scorer` prompt on the shortlisted names.

### 5. Proof-of-Concept Presentation
Deploy the `proof-of-concept-presenter` prompt:
- Package top 5 names in four real-world contexts each
- Run the one-second believability test
- Score energy assessment

### 6. Deliverable
Present:
- Top 3 recommended names with full rationale
- Sound symbolism analysis
- Proof-of-concept mockups
- Positioning line and short brand story for each
- Trademark/cross-language notes

## Quality Gate
- [ ] Minimum 90 raw candidates generated
- [ ] Top 5 shortlisted with scorecards
- [ ] All names presented in context (never on a list)
- [ ] At least one name sits in the tension zone (polarizing)
- [ ] Sound symbolism alignment verified for finalists


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
