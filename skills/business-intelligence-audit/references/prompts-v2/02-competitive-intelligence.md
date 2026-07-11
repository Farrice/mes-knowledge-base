---
name: "Competitive Intelligence"
source_prompt: "skills/business-intelligence-audit/references/prompts/02-competitive-intelligence.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 02: Competitive Intelligence

> Map the competitive landscape to identify positioning opportunities.

---

## Purpose

Understand where the business sits relative to competitors. Identify differentiation gaps and positioning opportunities.

---

## Input Required

- **Business Scan output** (from Prompt 01)
- **Competitor names** (if known) OR industry category for discovery

---

## Execution Protocol

```
You are conducting competitive intelligence analysis for a consulting engagement.

Based on the Business Scan for [COMPANY], map their competitive landscape.

## Instructions

1. If competitors are known, analyze 3-5 of them
2. If unknown, use search_web to identify top competitors:
   - Search: "[industry] + [service type] + competitors"
   - Search: "alternatives to [company name]"
3. For each competitor, extract key positioning elements
4. Synthesize into competitive positioning map
```

---

## Output Contract

- **Competitor coverage:** 3-5 competitor profiles, each with URL, value prop, audience, price positioning, differentiator, proof/credibility, and weakness/gap
- **Positioning Map:** one table comparing client vs. all profiled competitors across price point, target segment, primary benefit, proof quality, content strategy
- **XYZ Analysis:** at least one XYZ statement per meaningfully different dimension
- **Positioning Gaps:** three named categories — underserved segments, underused proof, underexplored channels
- **Recommendations:** minimum 3, each traceable to a specific gap or XYZ statement above it

---

## Output Skeleton

```
### Competitor Profiles

#### [Competitor Name]
- URL: [url]
- Primary Value Prop: [claim]
- Target Audience: [audience]
- Price Positioning: [premium / mid / budget]
- Key Differentiator: [what they lead with]
- Proof/Credibility: [what proof they show]
- Weakness/Gap: [where they're vulnerable]

[repeat for each of 3-5 competitors]

### Competitive Positioning Map

| Dimension | [Client] | Comp 1 | Comp 2 | Comp 3 |
|-----------|----------|--------|--------|--------|
| Price Point | [value] | [value] | [value] | [value] |
| Target Segment | [value] | [value] | [value] | [value] |
| Primary Benefit | [value] | [value] | [value] | [value] |
| Proof Quality | [value] | [value] | [value] | [value] |
| Content Strategy | [value] | [value] | [value] | [value] |

### XYZ Analysis

- "[Client] does [X — observed behavior], but [Competitor] does [Y — observed behavior], which means the opportunity is [Z — strategic implication]."
[repeat per dimension worth flagging]

### Positioning Gaps

1. Underserved Segments: [who competitors are ignoring]
2. Underused Proof: [what credibility could be leveraged]
3. Underexplored Channels: [where competition is weak]

### Recommendations

1. [Specific positioning opportunity, tied to a gap above]
2. [Differentiation angle, tied to a gap above]
3. [Quick win vs. competitors, tied to a gap above]
```

---

## Quality Gate

- [ ] 3-5 competitors profiled with all seven fields filled per profile
- [ ] Positioning Map has no blank cells
- [ ] Every XYZ statement follows the exact X/Y/Z structure and names a real, specific implication (not a generic "improve marketing")
- [ ] Each of the 3 Recommendations maps to a named gap or XYZ line above it
- [ ] Direct competitors (same offer, same audience) are prioritized over aspirational ones

---

## Pro Tips

- Focus on **direct competitors** (same offer, same audience) first
- Note **aspirational competitors** (where they want to be) second
- Look for **anti-positioning** opportunities (opposite of competition)
