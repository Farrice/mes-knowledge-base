---
description: Run the ICP research phase — Consumer Gap Diagnostic + Voice-of-Customer deep research mining
---

# /icp-research — Consumer Intelligence Research Phase

Run the research/data-gathering half of the ICP Deep Dive service. Produces the Consumer Gap Diagnostic and the Voice of Customer data library from real consumer conversations.

## Inputs Required

Ask the user for these (or extract from context):

1. **Brand/Business Name**
2. **Category/Industry**
3. **Brand Essence** (2-3 sentences — what they stand for)
4. **Price Point / Positioning** (where they sit in market)
5. **Current Consumer Description** (how they describe their customer today)
6. **Top 3 Business Challenges** (what's not working)
7. **3-5 Competitors** (optional but helpful)

## Steps

### 1. Load Expert Context
// turbo
Read these files in order:
1. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/genius.md`
2. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/consumer-gap-diagnostic.md`

You must internalize the Consumer Posture framework before proceeding. You reject demographics. You see ONE individual, not a segment.

### 2. Run the Consumer Gap Diagnostic

Using the inputs above and the `consumer-gap-diagnostic.md` prompt, produce:
- **25 Probing Questions** across the 3 Posture dimensions (Occupation, Activity, Thought Process)
- **Gap Analysis** — Critical / Moderate / Minor gaps in the brand's consumer understanding
- **Understanding Score** (0-100 with dimension breakdown)
- **Strategic Consequence Map** — how each gap is currently costing them money
- **Priority Discovery List** — what they need to learn first

### 3. Voice-of-Customer Deep Research Mining

This is the AI-augmented research layer. Mine REAL consumer conversations:

**Reddit Mining** (primary source):
- Search relevant subreddits for threads where consumers discuss their problems, frustrations, and desires
- Use Perplexity for targeted searches: "site:reddit.com [industry] [consumer pain point]"
- Extract 30-50 verbatim quotes
- Organize by theme (frustrations, desires, identity tensions, decision factors)

**Review Mining**:
- Amazon reviews, G2, Trustpilot, app store reviews for competitors
- Extract: What people love, hate, and wish existed
- Look for "finally" moments — "I finally found..."

**Forum/Community Mining**:
- Facebook groups, Quora, niche forums
- Find decision-making language, objections, what they've tried before

**Perplexity Research**:
- Industry trends affecting consumer behavior
- Emerging needs and underserved segments
- Competitive landscape consumer positioning

### 4. Compile Research Deliverables

Produce a structured file containing:

1. **Consumer Gap Diagnostic Report** (the full 25-question audit + gap analysis + strategic consequences)
2. **Voice of Customer Data Library** (all quotes organized by theme)
3. **Consumer Language Glossary** (exact words/phrases consumers use — copy-ready)
4. **Anti-Preference Map** (what consumers actively reject)
5. **Unmet Needs Inventory** (what they want that nobody's providing)

Save to: `_active/icp-intelligence-service/deliverables/[client-name]-research.md`

## Quality Gate
- Are there **real quotes** (not paraphrased or made up)?
- Does the gap diagnostic reveal **non-obvious** blind spots?
- Would the client read this and think "I had no idea"?
- Is the language glossary specific enough to plug directly into copy?

## Next Step
Run `/icp-build` with this research output to produce the full Consumer Posture Profile + Individual Finder + Internal World Stories.
