---
description: Build the ICP intelligence output — Consumer Posture Profile + Individual Finder + Internal World Stories from research data
---

# /icp-build — Consumer Intelligence Build Phase

Produce the full intelligence output from research data. Takes the output of `/icp-research` (or equivalent research context) and produces the 3D Consumer Posture Profile, Individual Consumer Finder, and Internal World Stories.

## Inputs Required

1. **Research data** — output from `/icp-research` OR equivalent consumer research context
2. **Brand context** — the 7 intake fields (brand name, category, essence, positioning, current consumer description, challenges, competitors)

If the user hasn't run `/icp-research` first, ask: "Do you have consumer research data ready, or should I run `/icp-research` first?"

## Steps

### 1. Load Expert Context
// turbo
Read these files in order:
1. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/genius.md`
2. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/consumer-posture-generator.md`
3. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/individual-consumer-finder.md`
4. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/internal-world-storytelling.md`

Internalize all three prompts before proceeding. You are Dai Media executing the Consumer Posture Framework.

### 2. Build the 3D Consumer Posture Profile

Using the `consumer-posture-generator.md` prompt and feeding all research data as context:

Produce:
- **The Individual** — vivid description, name, physical presence, vibe
- **Occupation in Your World** — role in the brand's ecosystem, energy, what makes them tick
- **Activity in Your World** — rituals, routines, identity-reinforcing behaviors, refusals
- **Thought Process in Your World** — internal logic, alignments, what feels authentic vs. inauthentic
- **Posture Synthesis** — unified portrait
- **The Prediction Test** — 5 hypothetical brand decisions with predicted consumer responses
- **Strategic Implications** — content voice, product decisions, experience design

**Validation**: Cross-reference the profile against VoC data. Does the profile match what actual consumers say? Adjust until it does.

### 3. Create the Individual Consumer Finder

Using the `individual-consumer-finder.md` prompt and the Posture Profile from Step 2:

Produce:
- **Signal Environments** — digital and physical spaces where this person appears (specific subreddits, forums, neighborhoods, events)
- **Recognition Criteria** — 5 positive markers, 5 negative markers
- **Search Methodology** — 7-day step-by-step protocol to find a real version
- **3 Candidate Profiles** — hypothetical-but-findable individuals
- **Validation Protocol** — questions to confirm they found the right person
- **The Coffee Test** — what a 20-minute conversation would reveal

### 4. Produce Internal World Stories

Using the `internal-world-storytelling.md` prompt, the Posture Profile, and VoC language data:

Produce:
- **Internal World Map** — the landscape of their mind (repeating thoughts, dominant feelings, the "Unspeakable Register")
- **3 Complete Story Drafts** following the Four Movements (Entry → Recognition → Permission → Possibility):
  - **Story 1**: LinkedIn post / social media format
  - **Story 2**: Email / long-form format
  - **Story 3**: Ad copy / landing page format
- **Recognition Markers** — moments designed for "how did they know?" reaction
- **Language Library** — phrases calibrated to their internal world (copy-ready)

### 5. Compile the Full Intelligence Report

Assemble all deliverables into one premium document:

1. **Executive Summary** (2 pages) — what we found, what it means, what to do
2. **Consumer Gap Diagnostic** (from research phase) — what you didn't know
3. **Voice of Customer Data Library** (from research phase) — real consumer language
4. **3D Consumer Posture Profile** — the full portrait
5. **Individual Consumer Finder** — search methodology + candidates
6. **Internal World Stories** — 3 ready-to-use content pieces
7. **Strategic Action Plan** — priority actions ranked by revenue impact

Save to: `_active/icp-intelligence-service/deliverables/[client-name]-intelligence-report.md`

## Quality Gate
- **The Kristen Stewart Test**: Would the actual person recognize themselves, or see a stereotype?
- **Individual vs. Group**: Does the profile describe ONE findable human, not "people who..."?
- **Emotional Outcome**: Is purchase motivation described as a feeling, not a problem solved?
- **Recognition Spike**: Would the target feel slightly uncomfortable with how well you know them?
- **VoC Grounding**: Are the stories and profile grounded in real consumer quotes?

## Output
The complete ICP Deep Dive Intelligence Report — 25-35 pages of consumer intelligence ready for client delivery.
