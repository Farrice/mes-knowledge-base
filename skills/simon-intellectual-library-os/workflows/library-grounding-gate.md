---
description: "Install or retrofit the mandatory grounding gate on an agent — KB-read-before-answering instructions + the empty-KB refusal acceptance test."
---

# Library Grounding Gate

Make groundedness a testable behavior on any agent: it must read its KB before answering, refuse honestly when the KB is empty, and label any ungrounded fallback.

## Pre-Flight Gate
- Load `genius.md` §Mandatory Grounding Gate + §Empty-KB Refusal Test.
- Target agent must have a designated KB. No KB = run `/library-kb-design` first; gating an agent to nothing just breaks it.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md` §Advisor instruction page.

## Execution
1. **Audit current instructions**: does a KB reference exist? Is it EARLY and MANDATORY ("read this before you do anything — this is your purpose and your north star"), or buried/optional?
2. **Install the gate**, early in the instructions: purpose/north star sentence → mandatory step: read the linked KB view (filtered to the agent's categories) before answering anything → confidence behavior: weight Proven > Tested > Untested; if the KB lacks coverage, SAY SO and label any fallback opinion as ungrounded with a confidence level.
3. **Anti-drift protocol**: scope boundaries, handoff rules to other modes, "do not answer outside your lanes" — compressed bullets.
4. **Token-slim** the result (gate must not bloat the page).
5. **Refusal test**: ask a real question the KB cannot answer (or test pre-ingestion). PASS = "my knowledge base has nothing on this; I can't answer from it" + optional labeled fallback. FAIL = generic confident answer → tighten gate language (move it earlier, make it imperative), retest.
6. **Grounded test** (if KB seeded): real question → answer must cite entries by name and apply them to the user's actual context.
7. **Record both test transcripts** with the instructions (they're the agent's acceptance certificate).

## Content Type Adaptations
| Agent type | Adaptation |
|---|---|
| Notion personal-agent mode | Gate = linked DB view on the instruction page + "mandatory entry gate" section |
| Claude (CLAUDE.md/skills) | Gate = CLAUDE.md rule + path to KB index; refusal test via fresh session |
| Antigravity expert skill | Gate = SKILL.md pre-flight "load genius.md/references first"; refusal = "never produce expert output without loading the expert" |
| Custom/scheduled agent | Gate in the agent instructions; test via manual trigger run |

## Output Requirements
Updated instructions (slimmed) + both test transcripts + pass/fail verdicts. A FAIL ships only as a flagged known-issue, never silently.

## Quality Gate
`genius.md` §Rubric Groundedness — ≥8 REQUIRES the refusal test on record (name the anchor). §Anti-Patterns: un-gated advisor, trust-by-default.
