# McRaney Belief Change Architecture — v3.0 Build Walkthrough

## Summary

Built 10 apex workflows for the David McRaney Belief Change skill, each grounded in the 26 patterns and 13 hidden knowledge items from `genius.md`. All research-dependent phases include Perplexity query templates. Registered all 10 as slash commands and updated SKILL.md from v2.1 (4 workflows) to v3.0 (14 workflows).

## What Was Built

### 10 Workflow Files

All in `skills/david-mcraney-belief-change/workflows/`:

| # | File | Slash Command | Key Innovation |
|---|------|--------------|----------------|
| 1 | [deep-canvassing-research-sprint.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/deep-canvassing-research-sprint.md) | `/mcraney-deep-canvass` | 5-phase pipeline with 3 parallel Perplexity stages producing a complete Belief Architecture Document |
| 2 | [persuasion-engineered-copy-engine.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/persuasion-engineered-copy-engine.md) | `/persuasion-copy` | McRaney × Luke Iha cross-stack — 6 phases from belief diagnosis through finished copy with accommodation audit |
| 3 | [accommodation-audit.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/accommodation-audit.md) | `/accommodation-audit` | 7-point quality gate scoring surprise, relevance, safety, route match, metacognition, staged delivery, accommodation |
| 4 | [belief-dissolution-copywriting.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/belief-dissolution-copywriting.md) | `/belief-dissolve-copy` | Lefkoe method origin trace → metacognitive activation → cognitive dissonance architecture → face-saving design |
| 5 | [resistance-matched-proof-rx.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/resistance-matched-proof-rx.md) | `/resistance-proof-rx` | Proof-type matching to resistance type with anti-backfire tables (each type has proof to USE and proof to AVOID) |
| 6 | [threshold-optimized-campaign.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/threshold-optimized-campaign.md) | `/threshold-campaign` | Full threshold equation with 30% calibration, binding constraint identification, one-variable-per-touchpoint architecture |
| 7 | [metacognitive-thought-leadership.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/metacognitive-thought-leadership.md) | `/metacognitive-content` | Platform-specific content architectures (LinkedIn/Newsletter/YouTube) with metacognitive question design |
| 8 | [elm-content-strategy.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/elm-content-strategy.md) | `/elm-content-strategy` | Platform × processing route matrix preventing the #1 structural content mismatch error |
| 9 | [social-permission-campaign.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/social-permission-campaign.md) | `/social-permission-campaign` | Social death calculation, pluralistic ignorance detection, permission architecture, face-saving design |
| 10 | [belief-layer-creative-brief.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/workflows/belief-layer-creative-brief.md) | `/belief-creative-brief` | Master 6-section intelligence document — the hub that feeds all downstream workflows |

### Hub Architecture

The creative brief is the center node. Run it once, reference everywhere:

```
                    /belief-creative-brief
                    (master document — run ONCE)
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  /mcraney-deep-canvass   Section 3         Section 2
  (feeds Section 1)     ┌───┴───┐         ┌───┴───┐
        │               ▼       ▼         ▼       ▼
        │    /elm-content   /resistance  /social-permission
        │    -strategy      -proof-rx    -campaign
        │
        ├──► /persuasion-copy
        ├──► /belief-dissolve-copy
        ├──► /threshold-campaign
        └──► /metacognitive-content
                    │
                    ▼
            /accommodation-audit
            (quality gate — run LAST)
```

### System Updates

- [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/david-mcraney-belief-change/SKILL.md) updated from v2.1 → v3.0 (4 → 14 workflows)
- 10 slash command stubs created in `.agent/workflows/`

## Pattern Coverage

All 26 genius.md patterns are deployed across the 10 workflows:

| Pattern | Primary Workflow(s) |
|---------|-------------------|
| P1 Resistance Hierarchy | Deep Canvass, Creative Brief |
| P2 Accommodation | Accommodation Audit, Metacognitive Content |
| P3 Pattern Interrupt | Threshold Campaign (evidence binding), Metacognitive Content |
| P5 Social Death | Social Permission Campaign, Creative Brief |
| P6 Pluralistic Ignorance | Social Permission Campaign |
| P7 Identity Bridge | Belief Dissolution, Social Permission |
| P8 Anxiety Detection | Social Permission, Threshold Campaign |
| P9 Production/Evaluation | Metacognitive Content |
| P10 Environment-First | Social Permission |
| P11 Face-Saving | Belief Dissolution, Social Permission, Creative Brief |
| P13 Threshold Equation | Threshold Campaign, Creative Brief |
| P15 Trust-Before-Persuasion | Threshold Campaign (trust binding) |
| P16 Staged Delivery | Threshold Campaign, Resistance Proof Rx |
| P17 Emotional Sediment | Belief Dissolution, Deep Canvass |
| P18 Minimum Viable Change | Social Permission, Threshold Campaign |
| P20 Cognitive Dissonance | Belief Dissolution |
| P21 Permission Architecture | Social Permission, Belief Dissolution |
| P22 Evaluation Mode | Metacognitive Content, Belief Dissolution |
| P24 ELM Route Selection | ELM Content Strategy, Persuasion Copy |
| P25 Rebuttal Detection | Resistance Proof Rx, Creative Brief |
| P26 Metacognitive Unlock | Metacognitive Content, Belief Dissolution |
| HK11 Lefkoe Method | Belief Dissolution (origin trace) |
| HK12 Accommodation Design | Accommodation Audit, Metacognitive Content |
| HK13 30% Calibration | Threshold Campaign, Creative Brief |

## Validation

- Every workflow with a research-dependent phase has Perplexity query templates baked in
- Every workflow ends with a quality gate table
- Cross-stack integrations specified (upstream, downstream, and pairs-with)
- All platform-specific architectures are differentiated by processing route (not just reformatted copies)
