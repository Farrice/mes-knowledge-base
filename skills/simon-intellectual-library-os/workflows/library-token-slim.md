---
description: "Token-efficiency review of agent instructions, skills, or schema files — measurably shorter, clearer, every step preserved (the 55% pass)."
---

# Library Token Slim

The reflex pass after every instruction/skill draft: less to read, more clarity, steps intact. Simon's reference pass cut 55% with zero behavior loss.

## Pre-Flight Gate
- Load `genius.md` §Decision Framework #6.
- Target = a durable artifact (instructions, skill, CLAUDE.md, schema). Don't slim knowledge ENTRIES this way — atomization (`/library-ingest`) governs those.
- Capture the baseline: word count + a list of every behavioral step/rule the artifact encodes. The list is the regression test.

## Skill Acquisition
Read `genius.md` + the target artifact + (if it exists) the live-test transcript showing current behavior.

## Execution
1. **Inventory behaviors**: enumerate every rule, step, gate, and boundary the artifact encodes. This is the must-survive list.
2. **Cut categories**, in order: duplicated statements (same rule said twice differently) → narrative connective tissue ("it's important to remember that...") → examples that restate rather than calibrate → hedges and meta-commentary → over-specified phrasing (compress to imperative bullets).
3. **Compress structure**: prose → high-contrast bullets; keep the opening callout (purpose/north star) and the entry gate FIRST; merge overlapping sections (boundaries + handoffs + anti-drift often collapse into one block).
4. **Preserve calibration**: anchors/exemplars that set a quality ceiling stay; "kept compressed bullets" beats deleted.
5. **Verify against the inventory**: every must-survive behavior still explicitly present? Anything lost goes back in, in compressed form.
6. **Report the delta**: before/after word counts, % reduction, behaviors preserved (count), anything intentionally removed and why.
7. **Live retest** when possible: one representative task through the slimmed artifact; behavior unchanged = pass.

## Content Type Adaptations
| Artifact | Adaptation |
|---|---|
| Advisor instructions | Gate stays early; one-page ceiling enforced |
| Skills/playbooks | Steps keep their order; quality gates survive verbatim |
| CLAUDE.md / schema files | Folder roles + loop rules are non-negotiable survivors |
| Anything generic-sounding after slimming | Wrong fix — the problem is missing KB grounding, not length |

## Output Requirements
The slimmed artifact + delta report (counts, %, preserved-behavior inventory) + retest result. Never deliver a slim without the inventory check.

## Quality Gate
`genius.md` §Rubric Token Economy — ≥8 = shorter AND clearer AND retested. §Anti-Patterns: token bloat (the disease), but also over-cutting that loses a gate (worse than bloat).
