---
description: Threshold-Optimized Campaign Builder — runs the full Threshold Equation with 30% calibration, identifies the binding constraint, and designs a multi-touchpoint campaign where each piece targets a specific variable
---

# Threshold-Optimized Campaign Builder

**Produces**: A multi-touchpoint campaign architecture where each touchpoint targets a specific variable in the change threshold equation, with content briefs for every piece.

> **Load before executing**: `skills/david-mcraney-belief-change/genius.md`

> [!IMPORTANT]
> Phases 1-2 fire Perplexity research to ground threshold scoring in real data. Scoring threshold variables from assumptions produces campaigns that target the WRONG constraint.

## When to Deploy

- Planning a launch campaign, drip sequence, or multi-touch nurture
- Content strategy that needs to move cold traffic through a belief shift
- When you've been adding evidence but nothing's changing (likely wrong binding constraint)
- Designing a phased approach to a market with heavy resistance
- Any campaign where "more content" isn't working and you need smarter content

## Inputs Required

- **Goal**: What change are we trying to produce? (purchase, signup, belief shift, adoption)
- **Audience**: Who needs to change?
- **Product/Offer** (optional): What they're changing toward
- **Campaign Type**: Email sequence / Content series / Ad funnel / Launch sequence / Drip
- **Existing Research** (optional): Output from `/mcraney-deep-canvass` or `/belief-creative-brief`

---

## Phase 1: Intelligence Gathering 🔬

**Uses**: McRaney Patterns 1, 5, 14

> Skip if you have output from `/mcraney-deep-canvass`. Use that data directly.

### Research Step 🔬

Fire 2 parallel Perplexity queries:

**Query 1 — Conversion Triggers**:
```
Search for: What convinced [audience] who DID [desired action] to do it?
Find: Testimonials, "why I switched" posts, "what changed my mind" posts, case studies.
Looking for: The SPECIFIC trigger, not general satisfaction.
Return: 10-15 conversion trigger quotes with source attribution.
```

**Query 2 — Social/Environmental Context**:
```
Search for: The social context around [audience] and [category/product].
Find: What do [audience's] peers think? What's the community consensus?
Are there public debates? Thought leaders on each side?
Is there a dominant narrative they'd have to go against?
Return: 8-12 social context signals with source attribution.
```

---

## Phase 2: Threshold Equation Scoring

**Uses**: McRaney Pattern 13 (Threshold Equation), HK 13 (30% Calibration)

### Execute

Score each variable 1-10 based on research data:

**Change DRIVERS** (forces pushing toward change):

| Variable | Score (1-10) | Evidence |
|----------|-------------|----------|
| **Trigger Strength** — How compelling is the reason to change? | [X] | [cite research] |
| **Source Trust** — Do they trust anyone who advocates the new position? | [X] | [cite] |
| **Social Safety** — How safe is it to change in their social context? | [X] | [cite] |
| **Identity Bridge** — Can they change without losing identity? | [X] | [cite] |
| **Driver Total** | [sum] | |

**Change RESISTORS** (forces blocking change):

| Variable | Score (1-10) | Evidence |
|----------|-------------|----------|
| **Investment** — How much have they invested in current position? | [X] | [cite] |
| **Social Risk** — What do they stand to lose socially? | [X] | [cite] |
| **Identity Threat** — How much does changing threaten "who they are"? | [X] | [cite] |
| **Uncertainty** — How uncertain is the outcome of changing? | [X] | [cite] |
| **Resistor Total** | [sum] | |

### 30% Calibration

Calculate:
- **Evidence Available**: Estimate what % of counter-evidence (vs belief strength) is currently available to this audience (0-100%)
- **Social Cost Sum**: Social Risk + Identity Threat = [X]
- **Cost Tier**: Low (<8) / Medium (8-14) / High (>14)
- **Effective Threshold**: 
  - Low cost: ~30% evidence needed
  - Medium cost: ~50% evidence needed
  - High cost: ~70-80% evidence needed
- **Current Position**: Are we above or below the effective threshold?

### Binding Constraint Identification

**The binding constraint** = the single variable that, if improved by 2-3 points, would tip the balance from Resistors > Drivers to Drivers > Resistors.

Decision logic:
- If Resistor Total > Driver Total AND Social Risk + Identity Threat > 12:
  → **Binding constraint is social/identity cost** → Campaign must REDUCE cost, not add evidence
- If Resistor Total > Driver Total AND evidence available < effective threshold:
  → **Binding constraint is evidence** → Campaign must ADD evidence
- If Resistor Total > Driver Total AND Source Trust < 4:
  → **Binding constraint is trust** → Campaign must BUILD trust before anything else
- If Resistor Total > Driver Total AND Uncertainty > 7:
  → **Binding constraint is uncertainty** → Campaign must REDUCE risk
- If Resistor Total ≤ Driver Total:
  → **Tipping point reached** → Campaign needs a TRIGGER, not more persuasion

### Output

```
## Threshold Analysis

Driver Total: [X]/40 | Resistor Total: [X]/40 | Gap: [+/-X]
Evidence Available: ~[X]% | Social Cost: [Low/Medium/High]
Effective Threshold: ~[X]%
Current Position: [Below/Above/At threshold]

BINDING CONSTRAINT: [Variable Name]
Strategic Implication: [1-2 sentences explaining what this means for campaign design]
```

---

## Phase 3: Campaign Architecture

**Uses**: McRaney Patterns 16 (Staged Delivery), 15 (Trust-Before-Persuasion), 18 (Minimum Viable Change)

### Execute

Design the campaign based on the binding constraint:

### If Binding Constraint = EVIDENCE:

```
Touchpoint Sequence:
1. Curiosity Trigger → Pattern interrupt that creates "wait, what?" (Pattern 3)
2. Single Best Proof Point → Your most verifiable, specific evidence
3. Demonstration → Show it working (video, case study, live walkthrough)
4. Third-Party Validation → Independent verification they can check
5. Concession + Redirect → "Here's where critics are right. Here's where the data diverges."
6. Decision Point → Clear CTA with risk reversal
```

### If Binding Constraint = SOCIAL/IDENTITY COST:

```
Touchpoint Sequence:
1. Normalization → Surface pluralistic ignorance: "Many [peers] are quietly exploring this" (Pattern 6)
2. Identity Bridge → Show that changing is CONSISTENT with who they are (Pattern 7)
3. Face-Saving Narrative → "You were right to think [old way] given [old info]..." (Pattern 11)
4. Social Proof → Others LIKE THEM who've made this change
5. Permission Architecture → Self + social + authority permission stack (Pattern 21)
6. Low-Cost First Step → Minimum viable change path (Pattern 18)
```

### If Binding Constraint = TRUST:

```
Touchpoint Sequence:
1. Credibility Establishment → Share value before asking for anything (Pattern 15)
2. Vulnerability Proof → Acknowledge limitations honestly
3. Reciprocity → Free value delivery with zero pitch
4. [Wait — do NOT pitch until touchpoints 1-3 have landed]
5. Soft Introduction → Present opportunity without pressure
6. Full Presentation → Now make the case with established trust
```

### If Binding Constraint = UNCERTAINTY:

```
Touchpoint Sequence:
1. Risk Acknowledgment → "Here's what you're probably worried about" (Pattern 8)
2. Worst-Case Scenario → Name it, quantify it, show it's survivable
3. Reversibility Proof → Show how to undo the change if needed
4. Small-Win Demonstration → Show results from the smallest possible first step
5. Graduated Commitment → Offer a trial/pilot/low-stakes entry
6. Success Path → Clear, specific steps from here to outcome
```

### Output

```
## Campaign Architecture

Binding Constraint: [variable]
Campaign Type: [Evidence / Social Permission / Trust-Building / Risk-Reduction]
Number of Touchpoints: [X]

Touchpoint Map:
| # | Objective | McRaney Pattern | Content Type | Key Message |
|---|-----------|----------------|-------------|-------------|
| 1 | [objective] | [pattern] | [email/post/ad/video] | [1-line message] |
| 2 | ... | ... | ... | ... |
```

---

## Phase 4: Content Briefs for Each Touchpoint

### Execute

For each touchpoint in the campaign, produce a content brief:

```
## Touchpoint [#]: [Title]

**Objective**: [Single variable this touchpoint targets]
**Format**: [Email / LinkedIn post / Ad / Video / Article]
**McRaney Pattern(s)**: [Pattern numbers and names]
**Key Message**: [1-2 sentence core message]
**Accommodation Design**:
  - Surprise: [what's genuinely unexpected in this piece]
  - Relevance: [specific personal stake]
  - Safety: [face-saving element if applicable]
**Proof Type**: [from resistance diagnosis — which proof type deploys here]
**Success Metric**: [How do we know this touchpoint worked? What does the audience do/think/feel after?]
**Transition to Next**: [How does this set up the next touchpoint?]
```

---

## Phase 5: Campaign Summary

### Output

```
## Campaign Summary

### The Story in One Sentence
[1 sentence describing the belief journey from first touchpoint to last]

### Threshold Shift Prediction
Before Campaign: Drivers [X]/40 vs Resistors [X]/40 = Gap [X]
After Campaign: Drivers [X]/40 vs Resistors [X]/40 = Gap [X]
Target: Flip [binding constraint variable] by [X] points

### Sequence Map
[Touchpoint 1] → [Touchpoint 2] → ... → [Decision Point]
[Variable shifted] → [Variable shifted] → ... → [Threshold crossed]

### Anti-Patterns (What NOT to Do)
1. [Specific anti-pattern based on the diagnosis]
2. [Another anti-pattern]
```

---

## Output Schema

**Deliverable**: A Campaign Summary (Phase 5 block: Story in One Sentence, Threshold Shift Prediction, Sequence Map, Anti-Patterns) sitting on top of the full Campaign Architecture (Phase 3) and per-touchpoint Content Briefs (Phase 4) — the summary is a front door, not a replacement for the architecture beneath it.

- **Structure**: Threshold Analysis (Phase 2) → Campaign Architecture branch matched to the binding constraint (Evidence/Social-Identity/Trust/Uncertainty, Phase 3) → Content Briefs (Phase 4, one per touchpoint) → Campaign Summary (Phase 5).
- **Numeric consistency**: The Threshold Shift Prediction's before/after Driver-Resistor gap must match the binding constraint identified in Phase 2 — a summary predicting a shift in a variable the architecture never targeted fails the Binding Constraint Accuracy gate.
- **One variable per touch**: Each Content Brief must name exactly one variable it moves — campaigns that shift multiple variables per touchpoint fail the Quality Gate below.

---

## Quality Gate

| Test | Question | Pass? |
|------|----------|-------|
| **Research Grounding** | Are threshold scores based on real audience data, not intuition? | |
| **Binding Constraint Accuracy** | Is the campaign targeting THE limiting factor, or just adding more evidence by default? | |
| **One Variable Per Touch** | Does each touchpoint shift exactly ONE variable, not multiple? | |
| **Sequence Logic** | Does each touchpoint build on the previous? Would the sequence break if re-ordered? | |
| **Accommodation Design** | Does at least one touchpoint contain genuine surprise that breaks the default model? | |
| **Anti-Pattern Check** | Does the campaign avoid deploying proof that BACKFIRES for this resistance type? | |

---

## Integration

- **Upstream**: Accepts research from `/mcraney-deep-canvass`, `/belief-creative-brief`
- **Downstream**: Each content brief feeds into `/persuasion-copy`, `/metacognitive-content`, or any content engine
- **Related**: `/social-permission-campaign` (specialized version for social-cost binding constraint)
