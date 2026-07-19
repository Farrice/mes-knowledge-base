---
name: "Mike Taylor: Persona Grounding From Transcripts (+ Social-Listening Gap-Fill)"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running Mike Taylor's Voice-of-Customer engine, the upgrade from a cold-generated panel to a grounded one. "The real gold of AI is start to capture all of your unstructured data, record everything." Real customer call transcripts, loaded into a RAG-capable tool, become a queryable synthetic panel that roleplays as the actual interviewed customers, not inferred demographic archetypes. When no transcripts exist, a harvested social-listening corpus fills the gap at one tier lower (Tier 2.5) instead of falling straight to cold generation.

## Input Required

- [TRANSCRIPTS]: the real customer call/interview transcripts, loaded as full sources (not pre-summarized). If none exist, use [CORPUS] instead: a harvested voice-of-customer corpus at `councils/buyers/corpora/<panel-name>/` (see Gap-Fill Protocol)
- [TOOL]: the RAG-capable environment holding [TRANSCRIPTS] (NotebookLM or equivalent). Not required for [CORPUS], which is read directly
- [DECISION_QUESTION]: the thing being tested against these real customers
- [CALIBRATION_STATUS]: has this panel been calibrated against real response-matching (rare), or is it transcript/corpus-loaded only (standard)?

## Gap-Fill Protocol (when no transcripts exist)

1. Check `councils/buyers/corpora/<panel-name>/` for an existing corpus ≤45 days old. If fresh, use it as [CORPUS] directly.
2. If missing or stale, harvest: (a) Apify-first via `.agent/workflows/social-listen.md` when the cost gate clears it, for reviews, Reddit/forum threads, LinkedIn comment fields, and competitor ad comments; (b) $0 fallback ALWAYS available: `execution/research.py --depth quick` (Tavily-receipted), WebSearch, `mcp__recall__search`, existing `research_outputs/`. If Apify is denied, degrade to $0 sources immediately. Never stall, never bypass the gate.
3. Store two files: `raw-quotes.md` (every quote verbatim, with speaker, source URL, date; drop anything unverifiable rather than guess) and `zeitgeist-digest.md` (dominant worldview, live objections, live vocabulary, recent shifts).
4. Tag every seat grounded this way: `social-grounded (corpus: <path>, harvested <date>)`.

## Execution Protocol

**Step 1 — Load, don't summarize.** Confirm [TRANSCRIPTS] or [CORPUS] are loaded/read as full sources, not pre-summarized. Pre-summarization strips the texture that makes this grounded rather than cold.

**Step 2 — The roleplay instruction.** Query against the loaded sources: "Role play as each of my customers and tell me would they be happy to see [DECISION_QUESTION]." Against [CORPUS], ground each persona in a specific quoted voice/handle from the corpus, not a blend of all of it.

**Step 3 — State the grounding tier.** Tier 2 (transcript-grounded) when [TRANSCRIPTS] were used; **Tier 2.5 (social-grounded)** when [CORPUS] was used instead. Cite corpus path, harvest date, and source mix (Apify and/or $0). Tier 1 only if [CALIBRATION_STATUS] confirms actual real-response-matching calibration exists. Never claim Tier 1 confidence without calibration; never claim Tier 2 confidence for a Tier 2.5 (corpus-grounded, not private-transcript-grounded) run; never apply Tier 3 hedging to genuinely grounded output at either tier.

**Step 4 — Sense-check framing.** State explicitly what real follow-up conversation this output should arm and precede — never present it as a replacement for that conversation.

**Step 5 — Secret-source check.** Confirm the output surfaced something a cold-generated (Tier 3) panel could not have — if not, re-run quoting the transcript/corpus texture more directly into the query.

## Output Contract

- Grounding tier stated (2, 2.5 with corpus path + harvest date, or 1 only if calibrated) with source count
- Per-customer/segment responses traceable to real transcript or corpus language
- Explicit secret-source check result
- Explicit statement of the real follow-up this arms
- Next step named
- Tier 2.5 only: corpus freshness (≤45 days, or staleness flagged) stated

## Output Skeleton

```
PERSONA GROUNDING — [audience/decision] — [date]
GROUNDING TIER: 2 (transcript-grounded) — [n] sources, tool: [TOOL]
[or: TIER 2.5 (social-grounded), corpus: councils/buyers/corpora/<panel-name>/, harvested <date>, sources: [Apify/[$0 tools]]
[or: TIER 1, calibrated against real response matching]

PER-CUSTOMER RESPONSES
[Customer/segment]: [response grounded in real stated concerns/language]
[...]

SECRET-SOURCE CHECK: [what this surfaced that cold generation could not have]
REAL-ASK ARMING: [the specific follow-up conversation this should precede]
NEXT STEP: [proceed to real conversation | escalate via mt-synthetic-vs-real-decision.md]
```

## Quality Gate

- Transcripts (or corpus) loaded as sources, not pre-summarized
- Grounding tier stated and justified, including corpus path + harvest date for Tier 2.5
- Responses traceable to real customer language, not generic filler
- Output frames itself as arming a real follow-up, never replacing one
- Secret-source check confirms real added signal
- Tier 2.5: every corpus quote carries a real source URL; staleness (>45 days) flagged if present

## Deploy When

Real customer call/interview transcripts already exist for the audience in question and a new idea, feature, or message needs testing against them before real recontact. Or, no transcripts exist and the Gap-Fill Protocol has built/located a fresh social-listening corpus to ground against instead.
