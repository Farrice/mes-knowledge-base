---
description: Instantiate Dara's 6-part creative-strategy process for a brand — research → briefing/concepting → roadmapping (awareness balance) → weekly production sprints → QA → analytics with the winner-softening watch.
---

# `/adpsy-strategy-sprint` — The 6-Part Creative-Strategy Operating Process

Dara's agency cadence, instantiated for one brand. This is the machine that runs the six tactics repeatedly — not a one-off concept. Note: her analytics-tool references (Motion) carry an evangelist bias; the extractable asset is the **cadence**, tool-agnostic.

## Pre-Flight Gate

- Is this an operation (recurring creative for a live ad account), not a single ad? Single ad → `/adpsy-tactic-select`.
- Is there account access / performance data? Steps 3 and 6 are hollow without it — scope honestly if missing.

## Skill Acquisition

Read `genius.md` (6-Part Process, Awareness-Balance Roadmapping, Morning Softening Check) + `references/source-quotes.md` Process block. For test-matrix depth, cross-load `/dara-test-plan`.

## Input Required

- **[BRAND]** + product line, **[AD ACCOUNT STATE]**: what's running, spend, current winners
- **[CAPACITY]**: creatives producible per week
- **[RESEARCH ASSETS]**: reviews, personas, prior comment mines (or note gaps)

## Execution

1. **Research — reputation analysis.** "How the general public feels about my brand": reviews sweep, persona map, organic sentiment. Output: persona cards + inner-monologue lines (feeds workflow 01).
2. **Briefing & concepting.** Angles and specific concepts pulled ONLY from the research — each brief names its tactic (1-6) and its source evidence. No research-orphaned concepts.
3. **Roadmapping — against the live account.** Audit funnel distribution; correct the drift: "they're defaulting really heavy to lower funnel. We need to open up more of that top of funnel… problem-aware or even unaware type creatives." Output: roadmap with awareness-level quotas per sprint.
4. **Production — weekly sprints.** Fixed creative count per week per brand, matched to capacity. Each sprint mixes tactics per the roadmap, not per whim.
5. **QA.** Every asset passes its workflow's quality gate + (statics) the 1-second comprehension gate from `/dara-comprehension-audit`.
6. **Analytics — three cadences + the softening watch.** Daily: hero ads — "are results starting to soften? Is the click-through rate starting to decrease? Are hook and hold rates starting to soften?" (yesterday's data, not just 7/30-day). Weekly: sprint review. Monthly: format/tactic performance → feeds the next roadmap. Winners' comment sections → `/adpsy-comment-mine` on schedule.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Agency/multi-brand | One instance per brand; sprints share a production calendar |
| Solo founder | Halve the cadence, keep all six steps — skipping research or QA is how accounts drift |
| New account (no data) | Steps 3/6 start as hypotheses; first 30 days = `/dara-test-plan` matrix |
| Audit mode | Score an existing operation against the six steps; name the missing step and the drift |

## Output Requirements

Operating Doc: the six steps instantiated with owners, cadences, and this brand's specifics · awareness-quota roadmap for the next 4 sprints · softening-watch checklist (metrics + thresholds + daily ritual) · comment-mine schedule. ≤2 pages.

Execution prompt: `references/prompts-v2/10-strategy-sprint-doc.md`

## Quality Gate

Rubric: every concept in the roadmap traceable to research (inner-thought rooting ≥7); awareness quotas explicit; softening watch has named metrics. Automatic fail: concepts with no research source, a roadmap that's all lower-funnel, or tool names presented as required infrastructure.
