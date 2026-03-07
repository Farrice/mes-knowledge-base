---
description: Run the complete ICP Deep Dive pipeline end-to-end — research through intelligence delivery in one shot
---

# /icp-deep-dive — Full ICP Intelligence Pipeline

// turbo-all

The complete ICP Deep Dive service pipeline. Combines `/icp-research` and `/icp-build` into a single end-to-end execution. Use when you have all the client intake information and want to produce the full intelligence report in one session.

## Inputs Required

Collect from the user (or extract from context):

1. **Brand/Business Name**
2. **Category/Industry**
3. **Brand Essence** (2-3 sentences — what they stand for)
4. **Price Point / Positioning** (where they sit in market)
5. **Current Consumer Description** (how they describe their customer today)
6. **Top 3 Business Challenges** (what's not working)
7. **3-5 Competitors** (optional but helpful)

If ANY of these are missing, ask before proceeding. Don't assume.

## Pipeline Execution

### PHASE A: SKILL ACQUISITION

Read these files in order before doing ANYTHING else:

1. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/genius.md`
2. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/consumer-gap-diagnostic.md`
3. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/consumer-posture-generator.md`
4. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/individual-consumer-finder.md`
5. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/internal-world-storytelling.md`

After reading, you must be able to answer:
- What are the 3 Posture dimensions and how do they differ?
- What is the Kristen Stewart Test and why does it matter?
- What are the Four Movements of Internal World Storytelling?
- Why does the framework reject demographics entirely?

### PHASE B: RESEARCH (Maps to `/icp-research`)

**Step 1: Consumer Gap Diagnostic**
Run the full diagnostic using the `consumer-gap-diagnostic.md` prompt:
- 25 probing questions across 3 dimensions
- Gap Analysis (Critical / Moderate / Minor)
- Understanding Score (0-100)
- Strategic Consequence Map
- Priority Discovery List

**Step 2: Voice-of-Customer Deep Mining**
Conduct live research using Perplexity and web search:

- **Reddit**: Search for threads where the target consumer discusses their problems. Extract 30-50 verbatim quotes.
- **Reviews**: Mine Amazon, G2, Trustpilot, app stores for competitor products. Extract loves, hates, wishes.
- **Communities**: Facebook groups, Quora, niche forums. Extract decision language and objections.
- **Industry Research**: Trends, emerging needs, competitive positioning via Perplexity.

Compile into:
- Voice of Customer Data Library (organized by theme)
- Consumer Language Glossary (copy-ready phrases)
- Anti-Preference Map (what they reject)
- Unmet Needs Inventory

### PHASE C: INTELLIGENCE BUILD (Maps to `/icp-build`)

**Step 3: 3D Consumer Posture Profile**
Using `consumer-posture-generator.md` + all research data:
- The Individual (vivid portrait)
- Occupation, Activity, Thought Process in brand's world
- Posture Synthesis
- Prediction Test (5 scenarios)
- Strategic Implications

**Step 4: Individual Consumer Finder**
Using `individual-consumer-finder.md` + Posture Profile:
- Signal Environments
- Recognition Criteria
- 7-day Search Methodology
- 3 Candidate Profiles
- The Coffee Test

**Step 5: Internal World Storytelling**
Using `internal-world-storytelling.md` + Posture Profile + VoC language:
- Internal World Map
- 3 Complete Story Drafts (LinkedIn, email, ad/landing page)
- Recognition Markers
- Language Library

### PHASE D: PACKAGE & DELIVER

**Step 6: Compile the Full Report**

Assemble into one document with these sections:

1. **Executive Summary** (2 pages)
2. **Consumer Gap Diagnostic Report** (5-7 pages)
3. **Voice of Customer Data Library** (3-5 pages)
4. **3D Consumer Posture Profile** (5-7 pages)
5. **Individual Consumer Finder** (4-5 pages)
6. **Internal World Stories** (3-5 pages, with 3 content pieces)
7. **Strategic Action Plan** (2-3 pages, prioritized by revenue impact)

Save to: `_active/icp-intelligence-service/deliverables/[client-name]-full-report.md`

### PHASE E: QUALITY GATE (Mandatory)

Run 5 checks before delivering:

| Check | Pass Criteria |
|---|---|
| **Kristen Stewart Test** | Would the actual person feel "seen" — not stereotyped? |
| **Individual vs. Group** | Does the profile describe ONE human, not "people who..."? |
| **VoC Grounding** | Are conclusions supported by real quotes? |
| **Recognition Spike** | Would the target feel slightly uncomfortable with how well we know them? |
| **Emotional Outcome** | Is purchase motivation a feeling accessed, not a problem solved? |

If any check fails → revise that section before delivering.

## Time & Effort Estimate

| Phase | Est. Time |
|---|---|
| Skill Acquisition | 15 min |
| Research | 3-4 hours |
| Intelligence Build | 4-6 hours |
| Package & QA | 1-2 hours |
| **Total** | **8-12 hours** |

With AI system leverage: **5-8 hours** of actual work.

## Pricing Reference
- Core (Phases A-B + Step 3 only): $500 ($350 launch)
- Complete (All phases): $750 ($500 launch)
- Complete + Content Pack (add 5 extra content pieces): $1,000 ($750 launch)
