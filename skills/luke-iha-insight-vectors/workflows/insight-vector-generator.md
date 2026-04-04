---
description: Generate 10-15+ insight vectors from systems-grammar analysis of any market/product
---

# Insight Vector Generator

Systematically generate insight vectors for any product, offer, or market using the complete systems grammar. Produces a ranked, SIN-filtered shortlist ready for deployment as mechanisms, hooks, content angles, or campaign concepts.

---

## Inputs Required

1. **Product/Offer** — What are we selling? What does it actually DO?
2. **Core Problem** — What pain does the audience experience?
3. **Audience Intelligence** — What does the audience already believe? What have they tried? What do they half-suspect?
4. **Market Context** — How sophisticated is this market? How many competing claims exist?
5. **Desired Output** — Mechanisms? Hooks? Content angles? Campaign concepts? (Determines emphasis.)

---

> **🔒 Pre-Flight Gate**: Load `genius.md` § Decision Framework. Answer all 5 diagnostic questions before executing.

## Phase 1: Mental Model Snapshot

Before generating a single vector, map the audience's current mental model:

| Model Layer | What They Believe | Source of Belief | Structural Weakness |
|------------|-------------------|------------------|---------------------|
| **Causal Beliefs** | "X causes my problem" | [where they learned this] | [is the arrow right?] |
| **Solution Beliefs** | "Y should fix it" | [past attempts] | [why it failed] |
| **Control Point Beliefs** | "The bottleneck is Z" | [their self-diagnosis] | [is Z the real constraint?] |
| **Pattern Beliefs** | "People like me tend to..." | [identity + peer group] | [is the type real?] |

**Output**: 2-3 sentence summary of the audience's operating map + identified structural weaknesses.

---

## Phase 2: Suspicion Audit

Before mining the grammar, identify what the audience already half-suspects:

1. What advice have they received that "didn't feel right"?
2. What have they tried that should have worked but didn't?
3. What do they say in forums with phrases like "I always felt like..." or "Something is off about..."?
4. What do they secretly blame that they haven't told anyone?

**Output**: 3-5 suspicion candidates ranked by prevalence and emotional charge.

---

## Phase 3: Systems Grammar Mining

Work through ALL 4 categories. For each, generate 2-4 candidate vectors specific to this market:

### Category 1: CAUSALITY VECTORS
- **Reverse Causation**: Can you flip a causal arrow the audience takes for granted?
- **Multiple Causation**: Can you show convergent causes where they see a single one?
- **Hidden Condition**: Is there a universally accepted piece of advice that only works CONDITIONALLY?

### Category 2: PATTERN VECTORS
- **System Archetypes**: Can you create a typing system? ("What's your ______ type?")
- **Virtuous Cycle**: Can you show an upward spiral your product initiates?
- **Vicious Cycle**: Can you make an invisible trap visible?

### Category 3: CONTROL POINT VECTORS
- **Leading Indicator**: Can you reveal an early warning signal they're not tracking?
- **Hidden Constraint**: Is the real bottleneck different from what they think?
- **False Assumption**: Is there a "more A = more B" assumption that's wrong?
- **Missing Variable**: Is there a variable that actually matters that nobody's tracking?

### Category 4: MODEL STRUCTURE VECTORS
- **Model Limitation Reframe**: Can a perceived weakness be flipped into an advantage?
- **Structural Revelation**: Is there a hidden process you can anthropomorphize and name?

**For each candidate, write:**
- The vector in one sentence
- Which vector TYPE it is
- Which audience suspicion it taps (from Phase 2)
- Initial SIN intuition (does it feel Simple + Intuitive + New?)

---

## Phase 4: SIN Filter

Score each candidate (minimum 8 candidates entering this phase):

| # | Vector (1 sentence) | Type | Simple (1-10) | Intuitive (1-10) | New (1-10) | Total /30 | Pass? |
|---|---------------------|------|---------------|-------------------|------------|-----------|-------|
| 1 | | | | | | | ≥21? |

- **Simple**: 12-year-old could understand it in one sentence
- **Intuitive**: Audience would nod before seeing proof
- **New**: Audience hasn't heard this framing before

**Kill rule**: <15 → abandon. 15-20 → refine. ≥21 → proceed to shortlist.

---

## Phase 5: Shortlist + Stack Design

From SIN survivors, select **3-5 vectors** that:
1. Point to the same conclusion from different angles (creates convergent certainty)
2. Cover different categories (causality + pattern + control point > three of the same type)
3. Include at least one that taps a top suspicion from Phase 2

**For each shortlisted vector, add:**
- A characterization NAME (2-3 words, visual, emotional, enemy-coded)
- A 60-second "discovery story" seed (how would you tell this in conversation?)
- Downstream deployment: mechanism? hook? content angle? all three?

---

## Output Format

```markdown
## Audience Mental Model Summary
[2-3 sentences from Phase 1]

## Suspicion Audit
[3-5 ranked suspicions]

## Full Vector Candidates ([N] generated)
[Numbered list with type, SIN scores]

## Shortlisted Vectors (3-5, SIN ≥21)

### [Vector Name 1] — [Type]
- **Vector**: [one sentence]
- **SIN Score**: [X/30]
- **Suspicion tapped**: [which one]
- **Discovery story seed**: [60-second narrative hook]
- **Deploy as**: [mechanism / hook / content angle / campaign concept]

### [Vector Name 2] — [Type]
[same format]

## Stack Map
[How the 3-5 shortlisted vectors work together — what convergent conclusion do they create?]

## Runner-Up Vectors
[2-3 that didn't make the shortlist but are worth holding for future campaigns]
```

---

## Quality Gate

Before delivering:
- ☐ Minimum 10 raw candidates generated across at least 3 of 4 categories
- ☐ Minimum 3 candidates passed SIN ≥21
- ☐ Shortlisted vectors tap at least one audience suspicion
- ☐ All shortlisted vectors have characterization names
- ☐ Stack map shows convergent logic (not random collection)
- ☐ No fabricated research, fake biology, or invented mechanisms

> **🛡️ Anti-Pattern Check**: Review output against `genius.md` § Anti-Patterns. Flag fabricated systems, claimed vectors (not earned), and complexity without clarity.
