---
name: "Mike Taylor — Persona Grounding From Transcripts"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running Mike Taylor's Voice-of-Customer engine — the upgrade from a cold-generated panel to a transcript-grounded one. "The real gold of AI is start to capture all of your unstructured data, record everything." Real customer call transcripts, loaded into a RAG-capable tool, become a queryable synthetic panel that roleplays as the actual interviewed customers — not inferred demographic archetypes.

## Input Required

- [TRANSCRIPTS]: the real customer call/interview transcripts, loaded as full sources (not pre-summarized)
- [TOOL]: the RAG-capable environment holding them (NotebookLM or equivalent)
- [DECISION_QUESTION]: the thing being tested against these real customers
- [CALIBRATION_STATUS]: has this panel been calibrated against real response-matching (rare), or is it transcript-loaded only (standard)?

## Execution Protocol

**Step 1 — Load, don't summarize.** Confirm [TRANSCRIPTS] are loaded as full sources in [TOOL]. Pre-summarization strips the texture that makes this grounded rather than cold.

**Step 2 — The roleplay instruction.** Query against the loaded sources: "Role play as each of my customers and tell me would they be happy to see [DECISION_QUESTION]."

**Step 3 — State the grounding tier.** Tier 2 (transcript-grounded, standard case) unless [CALIBRATION_STATUS] confirms actual real-response-matching calibration exists, in which case Tier 1. Never claim Tier 1 confidence without calibration; never apply Tier 3 hedging to genuinely grounded output.

**Step 4 — Sense-check framing.** State explicitly what real follow-up conversation this output should arm and precede — never present it as a replacement for that conversation.

**Step 5 — Secret-source check.** Confirm the output surfaced something a cold-generated (Tier 3) panel could not have — if not, re-run quoting the transcript texture more directly into the query.

## Output Contract

- Grounding tier stated (2, or 1 only if calibrated) with source count
- Per-customer/segment responses traceable to real transcript language
- Explicit secret-source check result
- Explicit statement of the real follow-up this arms
- Next step named

## Output Skeleton

```
PERSONA GROUNDING — [audience/decision] — [date]
GROUNDING TIER: 2 (transcript-grounded) — [n] sources, tool: [TOOL]
[or: TIER 1, calibrated against real response matching]

PER-CUSTOMER RESPONSES
[Customer/segment]: [response grounded in real stated concerns/language]
[...]

SECRET-SOURCE CHECK: [what this surfaced that cold generation could not have]
REAL-ASK ARMING: [the specific follow-up conversation this should precede]
NEXT STEP: [proceed to real conversation | escalate via mt-synthetic-vs-real-decision.md]
```

## Quality Gate

- Transcripts loaded as sources, not pre-summarized
- Grounding tier stated and justified
- Responses traceable to real customer language, not generic filler
- Output frames itself as arming a real follow-up, never replacing one
- Secret-source check confirms real added signal

## Deploy When

Real customer call/interview transcripts already exist for the audience in question and a new idea, feature, or message needs testing against them before real recontact.
