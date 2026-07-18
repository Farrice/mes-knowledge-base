---
description: Audit an existing brand name against Placek's comfort trap, sound symbolism, and competitive courage frameworks
---

# Name Audit Workflow

## Prerequisites
- Load `skills/david-placek-naming/SKILL.md` (Tier 1)

## Steps

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


### 1. Intake
Gather from the user:
- Current brand name
- Category/industry
- Primary competitors + their names
- How long the name has been in use
- Current business goal (growth, repositioning, launch?)

### 2. Comfort Trap Diagnosis
Deploy the `comfort-trap-audit` prompt:
- Score on the Placek evaluation framework (8 criteria)
- Classify: Invisible Zone / Middle Ground / Tension Zone
- Identify sound symbolism alignment/misalignment

### 3. Competitive Landscape Analysis
- Map all competitor names by strategy type
- Identify the naming "herd"
- Determine if the current name blends in or stands out

### 4. Sound Symbolism Quick Check
Deploy `sound-symbolism-scorer` on the current name:
- Analyze phoneme signals vs. intended brand attributes
- Score processing fluency and memorability

### 5. Deliverable
Present:
- Zone verdict with evidence
- Sound symbolism analysis
- Top 3 strengths and top 3 weaknesses of the current name
- 12-month compound test result
- Recommendation: Keep / Evolve / Rename

### 6. Next Steps
- If **Rename**: route to `naming-sprint` workflow
- If **Evolve**: identify specific phonemic or structural modifications
- If **Keep**: recommend other brand elements to invest in (tagline, positioning)

## Output Schema
The user receives a **Name Audit Verdict** containing:
1. **Zone Classification** — Invisible Zone / Middle Ground / Tension Zone, with the evidence that produced the call.
2. **8-Criterion Scorecard** — the Placek evaluation framework scored with a short justification per criterion.
3. **Sound Symbolism Analysis** — phoneme signals mapped against intended brand attributes, plus processing fluency and memorability scores.
4. **Top 3 Strengths / Top 3 Weaknesses** — specific to this name, not generic naming advice.
5. **12-Month Compound Test Result** — a one-paragraph projection of whether this name compounds or flattens with repeated exposure.
6. **Recommendation** — Keep / Evolve / Rename, with the routing (next workflow) named explicitly.

## Quality Gate
- [ ] Score completed on all 8 evaluation criteria
- [ ] Zone classification clearly justified
- [ ] Sound symbolism analysis included
- [ ] Actionable recommendation delivered (not vague advice)


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
