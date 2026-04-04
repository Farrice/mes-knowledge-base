---
description: Map the complete mental model of a target audience — causal beliefs, pattern beliefs, control-point assumptions, and structural gaps
---

# Mental Model Mapper

Produce a comprehensive map of how a target audience THINKS about their problem — every cause-and-effect story, every pattern they recognize, every control point they believe in, and every structural gap where an insight vector can be inserted.

This workflow is the DIAGNOSTIC that precedes all insight vector generation. Map first, mine second.

---

## Inputs Required

1. **Audience Definition** — Who specifically? (Beyond demographics — their relationship with the problem)
2. **Problem Domain** — What problem space are we mapping? (Health, money, relationships, career, etc.)
3. **Available Intelligence** — Reddit threads, Amazon reviews, support tickets, survey data, forum posts, competitor copy, or intuition-based description of the audience
4. **Market Sophistication Level** — Have they been marketed to heavily? Are they skeptical?

---

> **🔒 Pre-Flight Gate**: This workflow produces the INPUT for `/insight-vectors`. Run this FIRST when you don't yet understand the audience's belief architecture.

## Phase 1: Belief Excavation

For each layer, excavate what the audience believes:

### Layer 1: Causal Beliefs (What They Think Causes Their Problem)
Mine for every "X causes Y" statement the audience holds:

| # | Causal Belief | Source | Strength (1-10) | Accuracy |
|---|--------------|--------|-----------------|----------|
| 1 | "[Audience thinks] X causes Y" | [where they learned it] | [how deeply held] | [actually true / partially true / false / reversed] |

**Mining prompts**:
- "When I ask them 'why do you have [problem]?' — what do they say?"
- "What have they been told by doctors/experts/influencers?"
- "What do they tell their friends about their problem?"

### Layer 2: Solution Beliefs (What They Think Should Fix It)
Map every "if I just did X, I'd be fine" story:

| # | Solution Belief | Tried? | Result | Why It Failed (Reality) |
|---|----------------|--------|--------|------------------------|
| 1 | "[Audience thinks] doing X will fix it" | [yes/no] | [outcome] | [actual reason for failure — becomes vector material] |

### Layer 3: Control Point Beliefs (What They Think Is The Bottleneck)
What do they believe is the #1 thing holding them back?

| # | Perceived Bottleneck | Is It Real? | Actual Constraint |
|---|---------------------|-------------|-------------------|
| 1 | "[Audience thinks] the real problem is Z" | [yes/no/partially] | [what's actually constraining them — insight vector territory] |

### Layer 4: Pattern Beliefs (How They Classify Themselves)
What types, categories, or identities do they use?

| # | Self-Classification | "I'm the kind of person who..." | Structural Implications |
|---|-------------------|--------------------------------|------------------------|
| 1 | [how they type themselves] | [identity statement] | [what this enables/prevents] |

### Layer 5: Emotional Beliefs (What They've Concluded About Themselves)
The meta-belief layer — conclusions they've drawn from repeated failure:

| # | Emotional Conclusion | Based On | Insight Vector Opportunity |
|---|---------------------|----------|---------------------------|
| 1 | "[Audience concludes] I'm just not..." | [repeated experience] | [this conclusion is the REAL thing to dissolve] |

---

## Phase 2: Gap Analysis

For each belief layer, identify structural gaps where insight vectors can be inserted:

### Causal Gaps
- Which causal arrows are REVERSED from reality?
- Which "single cause" beliefs mask multiple converging causes?
- Which universally-accepted advice only works CONDITIONALLY?

### Solution Gaps
- Which failed solutions failed for reasons the audience doesn't understand?
- Where has effort been wasted on the wrong lever?

### Control Point Gaps
- Is the perceived bottleneck the REAL bottleneck?
- What hidden constraint is the actual limiter?
- What leading indicator are they not tracking?

### Pattern Gaps
- Are their self-classifications accurate? Or limiting?
- Could a new typing system make them feel more understood?

### Emotional Gaps
- Which self-conclusions are based on wrong causal models?
- What would change if they understood the REAL reason for past failure?

---

## Phase 3: Suspicion Map

Overlay the gap analysis with what the audience already half-suspects:

| Gap Type | Audience Suspicion | Suspicion Strength (1-10) | Vector Opportunity |
|----------|-------------------|--------------------------|-------------------|
| [Causal/Solution/Control/Pattern/Emotional] | "I've always felt like..." | [how many people share this] | [which vector type would hit this] |

---

## Output Format

```markdown
# Mental Model Map: [Audience] × [Problem Domain]

## Executive Summary
[3-5 sentences: What this audience believes, where their map is broken, and what types of insight vectors will work best]

## Belief Architecture
### Causal Beliefs [table from Phase 1, Layer 1]
### Solution Beliefs [table from Phase 1, Layer 2]
### Control Point Beliefs [table from Phase 1, Layer 3]
### Pattern Beliefs [table from Phase 1, Layer 4]
### Emotional Beliefs [table from Phase 1, Layer 5]

## Structural Gaps (Ranked by Insight Potential)
1. [Highest-leverage gap] — [which vector type exploits this]
2. [Second gap] — [vector type]
3. [Third gap] — [vector type]

## Suspicion Map
[Table from Phase 3]

## Recommended Vector Types
Based on this audience's specific model structure:
- **Primary**: [Which 2-3 vector types will hit hardest]
- **Secondary**: [Which 2-3 are good supporting vectors]
- **Avoid**: [Which vector types won't work for this audience and why]

## Next Steps
→ Feed this map into `/insight-vectors` for full vector generation
→ Or feed specific gaps into `/reverse-cause` or `/archetype-factory` for specialized mining
```

---

## Quality Gate

- ☐ All 5 belief layers excavated (even if some are sparse)
- ☐ At least 3 structural gaps identified with vector-type recommendations
- ☐ Suspicion map has at least 2 entries
- ☐ Executive summary is specific to THIS audience (not generic)
- ☐ No invented audience beliefs — everything grounded in available intelligence

> **🛡️ Anti-Pattern Check**: Review `genius.md` § Anti-Patterns. Do not assume beliefs without evidence. If intelligence is sparse, flag gaps explicitly.
