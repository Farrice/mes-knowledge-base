---
description: "/mt-persona-grounding — turn real customer call transcripts into a queryable synthetic panel: roleplay AS the actual interviewed customers instead of cold-generated personas. Mike Taylor's Voice-of-Customer engine (Vexpower/NotebookLM demo)."
---

# Persona Grounding From Transcripts

"The real gold of AI is start to capture all of your unstructured data, record everything." This workflow is the upgrade path from a cold-generated (Tier 3) panel to a transcript-grounded (Tier 2) one — the difference between guessing what buyers think and asking the recorded version of buyers who actually told you.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Pattern 11, Hidden Knowledge 1 & 3, Grounding Ladder Pattern 6).

> **Pre-Flight Gate**: Do real interview/call transcripts exist for this audience? If not, this workflow doesn't apply — use `mt-persona-panel-triage.md` (Tier 3) and flag the grounding gap in the output.

## Input Required
- The recorded customer transcripts (however many exist — 10-15 "is gold" per Taylor's own example; fewer still beats zero)
- The tool holding them (NotebookLM, or any RAG-capable environment that can hold multiple source transcripts and answer against them)
- The decision question — same shape as `mt-persona-panel-triage.md` (preference test, resonance check, feature validation), OR a latent-demand question (route the pain-mining shape to `mt-latent-demand-mining.md`)

## Workflow

### Step 1: Load, Don't Summarize First
Load the full transcripts as sources — do not pre-summarize them before querying. Summarization strips the texture (specific phrasing, specific complaints) that makes the grounded roleplay differ from a cold-generated one.

### Step 2: The Roleplay Instruction
Issue the grounding instruction directly against the loaded sources:
> "Role play as each of my customers and tell me would they be happy to see [the thing you're testing]."

This is structurally the same two-step shape as Pattern 3 (scene already set by the loaded transcripts; the question comes second), but the "personas" are now specific real people the tool has actual transcript data on, not inferred demographic archetypes.

### Step 3: State the Grounding Tier
Report which tier this panel is actually running at:
- **Tier 2** (this workflow, standard case): custom personas built from uploaded real transcripts — accuracy scales with transcript quality and quantity (LIKELY, secondary corroboration)
- **Tier 1** (rare, requires calibration infrastructure like DSPy-tuned response matching against a pre-built panel of real interviewed people): only claim this tier if the panel has actually been calibrated against real response data, not just loaded with transcripts

Never let a Tier 2 grounded panel get reported with Tier 1 confidence language, and never let it get reported with Tier 3 (cold-generation) hedging either — it earns real but bounded confidence.

### Step 4: Sense-Check Before the Real Ask
Frame the output as arming a real follow-up, not replacing it: "it at least gives me a bit of conviction... I know that when I go back to them that they're going to be primed to really like the ideas that I pitched to them." State explicitly what real conversation this output should precede.

### Step 5: The Secret-Source Check
Confirm this output is doing something a generic prompt to a stock chatbot couldn't — if the same verdict would come out of a cold-generated panel with no real transcripts, the grounding didn't add anything and the workflow should be re-run with the actual transcript texture more directly quoted into the query.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| New feature/course/product validation against existing customers | Direct application — "would they be happy to see [X]" |
| Message/positioning test against real segments | Combine with `mt-concept-headline-triage.md`'s two-option format, grounded instead of cold |
| Churn/retention diagnosis | Query the transcripts for stated objections/complaints first, then roleplay the response to a proposed fix |
| Sales-call objection rehearsal | Roleplay the specific objecting customer before a real follow-up call — this is Pattern 12's sense-check in its sharpest form |

## Output Format
```
PERSONA GROUNDING — [audience/decision] — [date]
GROUNDING TIER: 2 (transcript-grounded) — [n] real sources loaded, tool: [NotebookLM/other]
[If calibration infrastructure was used: TIER 1, calibrated against real response matching]

PER-CUSTOMER RESPONSES (named where transcripts allow)
[Customer/segment]: [response, grounded in their actual stated concerns/language]
...

SECRET-SOURCE CHECK: [what this output surfaced that a cold-generated panel could not have]

REAL-ASK ARMING: [the specific follow-up conversation this output should precede, and why the team is now primed for it]
NEXT STEP: [proceed to real conversation | escalate stakes → mt-synthetic-vs-real-decision.md]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] Transcripts were loaded as sources, not pre-summarized before querying
- [ ] Grounding tier stated explicitly (2, or 1 only if actually calibrated)
- [ ] Responses are traceable to real customer language/concerns, not generic persona filler
- [ ] Output frames itself as arming a real follow-up, never replacing one
- [ ] The secret-source check confirms grounding added real signal vs. a cold-generated equivalent would have

## Common Pitfalls
- **Summarizing the transcripts first.** Kills the texture that makes this Tier 2 instead of Tier 3 with extra steps.
- **Claiming Tier 1 confidence without calibration.** Loading transcripts is not the same as calibrating response-matching against them.
- **Treating grounded output as the final pitch.** It's rehearsal for the real conversation, not a replacement for it.

Execution prompt: `references/prompts-v2/persona-grounding.md`
