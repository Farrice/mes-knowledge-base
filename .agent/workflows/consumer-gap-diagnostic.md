---
description: Run the Consumer Posture Gap Diagnostic — audit what a brand doesn't know about its consumer
---

# /consumer-gap-diagnostic — Consumer Understanding Audit

Deploy Dai Media's Crown Jewel #3 — the "Stunned Brand Owner" diagnostic that exposes exactly what a brand doesn't know about its consumer, scores their understanding 0-100, and maps how each blind spot is costing them money.

## Inputs Required

Ask the user for (or extract from context):

1. **[BRAND NAME]**: The brand being diagnosed
2. **[BRAND CATEGORY]**: Industry/product category
3. **[CURRENT CONSUMER DESCRIPTION]**: How they currently describe their consumer
4. **[KNOWN CONSUMER INFORMATION]**: Any specific knowledge they have (optional but helpful)

## Steps

### 1. Load Expert Context
// turbo
Read these files in order:
1. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/genius.md`
2. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/consumer-gap-diagnostic.md`

Internalize the Consumer Posture framework. You reject demographics. You see ONE individual, not a segment.

### 2. Execute the Diagnostic

Following the prompt's execution protocol:

1. **ACKNOWLEDGE** — Validate the brand's stated understanding. Don't dismiss existing knowledge.
2. **DEPLOY** — Generate 25 Gap Questions across the three Consumer Posture dimensions:
   - **Occupation** (~8 questions) — Their role, status, energy in the brand world
   - **Activity** (~8 questions) — Rituals, routines, refusals, identity-reinforcing behaviors
   - **Thought Process** (~9 questions) — Internal logic, emotional outcomes, alignments
3. **DIAGNOSE** — For each question, identify whether the brand's knowledge is solid, weak, or nonexistent
4. **MAP** — Connect each gap to specific business consequences (how it's hurting decisions)
5. **PROVIDE** — Discovery pathways for each critical gap (how to find the answers)
6. **SCORE** — Overall Understanding Score (0-100 with dimension breakdown)

### 3. Deliver Output

Produce a structured deliverable containing:
- **Current Understanding Audit** (known vs. assumed)
- **25 Gap Questions** (organized by Occupation / Activity / Thought Process)
- **Gap Analysis** (Critical / Moderate / Minor classification)
- **Strategic Consequence Map** (how each gap affects decisions and revenue)
- **Discovery Protocols** (how to find the answers)
- **Understanding Score** (0-100 with breakdown)
- **Priority Action List** (top 3 things to discover in the next 72 hours)

## Quality Gate
- Does the brand owner have **clear visibility** into exactly what they don't know?
- Are the consequences **specific** (not generic "you'll miss opportunities")?
- Would the diagnostic **surprise** the brand owner with at least 3 non-obvious gaps?
- Do discovery protocols give **actionable** steps, not vague suggestions?

## Standalone vs. Pipeline
This command runs independently. For the full ICP pipeline, use `/icp-deep-dive`. To chain this into a research phase with VoC mining, use `/icp-research`.
