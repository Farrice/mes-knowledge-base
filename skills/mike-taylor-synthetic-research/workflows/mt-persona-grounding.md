---
description: "/mt-persona-grounding — turn real customer call transcripts into a queryable synthetic panel: roleplay AS the actual interviewed customers instead of cold-generated personas. Mike Taylor's Voice-of-Customer engine (Vexpower/NotebookLM demo). Includes the Tier 2.5 social-listening gap-fill rung for when no transcripts exist."
---

# Persona Grounding From Transcripts (+ Social-Listening Gap-Fill)

"The real gold of AI is start to capture all of your unstructured data, record everything." This workflow is the upgrade path off a cold-generated (Tier 3) panel. Real interviews exist: go up to transcript-grounded (Tier 2). They don't: go sideways to social-grounded (**Tier 2.5**), built from a harvested voice-of-customer corpus. The shared discipline is never guessing what buyers think when a recorded, or at minimum a receipted-live, version of their own words is reachable.

## The Grounding Ladder (extended)

Confidence descends as the tier number rises. State the tier explicitly in every output; never report a lower tier with a higher tier's confidence language.

| Tier | Name | What it is | Confidence |
|---|---|---|---|
| 1 | Calibrated | Pre-built panel of real interviewed people, calibrated (e.g. DSPy) until responses match real response style/substance | Highest: "high 70s to 80%" (LIKELY, genius.md Pattern 6) |
| 2 | Transcript-grounded | Custom personas built from uploaded real call/interview transcripts | High, scales with transcript quality/quantity |
| **2.5** | **Social-grounded** (this rung, NEW) | Personas grounded in a harvested voice-of-customer corpus (verbatim quotes + receipts) when no first-party transcripts exist | Bounded: real current voice, but self-selected/public-only, never treat as transcript-equivalent |
| 3 | Cold-generated | Pure inferred personas, no real data | Lowest, approximately 60% (LIKELY) |

Tier 2.5 sits strictly between 2 and 3. It beats cold generation because every claim traces to a real, dated, sourced quote from a real person in the target audience. It never earns Tier 2's confidence because the corpus is public-surface voice-of-customer, not a private recorded interview: no follow-up probing, no context on who didn't post.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Pattern 11, Hidden Knowledge 1 & 3, Grounding Ladder Pattern 6).

> **Pre-Flight Gate**: Do real interview/call transcripts exist for this audience?
> - **Yes** → run the standard Tier 2 workflow below (Steps 1-5).
> - **No** → do NOT drop straight to Tier 3. First check `councils/buyers/corpora/<panel-name>/` for an existing, fresh (≤45 days) social-grounded corpus. If one exists, run the **Tier 2.5 Gap-Fill Protocol** below instead. If none exists or it's stale, run the Gap-Fill Protocol to build one, THEN proceed. Only fall through to `mt-persona-panel-triage.md` (Tier 3) if the gap-fill genuinely turns up nothing usable. Flag that explicitly in the output; it should be rare, since $0 search/Recall sources almost always surface something.

## Input Required
- The recorded customer transcripts (however many exist — 10-15 "is gold" per Taylor's own example; fewer still beats zero)
- The tool holding them (NotebookLM, or any RAG-capable environment that can hold multiple source transcripts and answer against them)
- The decision question — same shape as `mt-persona-panel-triage.md` (preference test, resonance check, feature validation), OR a latent-demand question (route the pain-mining shape to `mt-latent-demand-mining.md`)

## Tier 2.5 Gap-Fill Protocol (no transcripts exist)

Fires when the Pre-Flight Gate fails. Builds a voice-of-customer mini-corpus for the panel's buyer, then grounds personas from it exactly as Steps 1-5 below ground them from transcripts. The corpus IS the transcript-equivalent source.

**Step G1: Harvest.**
- (a) **Apify-first, when budget-approved**: route through `.agent/workflows/social-listen.md` (`/social-listen`) for reviews, Reddit/forum threads, LinkedIn comment fields, and competitor ad comments. This is the higher-yield path when the cost gate clears it.
- (b) **$0 fallback, ALWAYS available**: `execution/research.py` (Tavily-receipted; use `--depth quick` to stay on the free floor and skip the Gemini/Perplexity accelerators), WebSearch, `mcp__recall__search`, and existing `research_outputs/`. Cost-gate discipline: if Apify is denied or budget-blocked, degrade to $0 sources immediately. Never stall the workflow waiting on approval, and never bypass the gate to force Apify through.
- Prioritize real forum/review/comment text over marketing-copy pages. Reject anything that reads like an AI-generated search summary rather than an actual quoted person. Verbatim, or don't include it.

**Step G2: Store the corpus.** Save to `councils/buyers/corpora/<panel-name>/`:
- `raw-quotes.md`: every verbatim quote, each with speaker (name/handle or "anonymous [role]"), exact source URL, and date (or best-effort date estimate, labeled as such). Mark anything unverifiable UNCONFIRMED and prefer dropping it over guessing.
- `zeitgeist-digest.md`: a one-pager covering the dominant worldview(s), current live objections (verbatim-derived), current vocabulary (their words, not synonyms), and what's changed recently versus older assumptions about this audience.

**Step G3: Freshness rule.** Every corpus carries its harvest date at the top of both files. Older than **45 days** means re-harvest before any high-stakes run; zeitgeist drifts, and pricing objections, platform behavior, and live vocabulary all move faster than 45 days in most consumer/DTC categories. Low-stakes/directional runs may reuse a stale corpus if flagged as stale in the output.

**Step G4: Ground and tag.** Run the roleplay instruction (Step 2 below) against the corpus instead of transcripts. Every seat grounded this way gets the tag `social-grounded (corpus: councils/buyers/corpora/<panel-name>/, harvested <date>)`. This tag is mandatory in the panel file and in any output that cites the seat.

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
- **Tier 2.5** (gap-fill case, no transcripts existed): custom personas grounded from a harvested social-listening corpus per the Gap-Fill Protocol above. Cite the corpus path and harvest date, and note the source mix (Apify actors used, and/or $0 sources: Tavily/WebSearch/Recall)
- **Tier 1** (rare, requires calibration infrastructure like DSPy-tuned response matching against a pre-built panel of real interviewed people): only claim this tier if the panel has actually been calibrated against real response data, not just loaded with transcripts

Never let a Tier 2 or Tier 2.5 grounded panel get reported with Tier 1 confidence language, and never let either get reported with Tier 3 (cold-generation) hedging. Both earn real but bounded confidence. Tier 2.5 is bounded tighter than Tier 2: it's public/self-selected voice, not a private recorded interview, so hedge accordingly (LIKELY, not VERIFIED, on any individual persona's predicted reaction).

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
[Gap-fill case: TIER 2.5 (social-grounded), corpus: councils/buyers/corpora/<panel-name>/, harvested <date>, sources: [Apify actors and/or $0: Tavily/WebSearch/Recall]]
[If calibration infrastructure was used: TIER 1, calibrated against real response matching]

PER-CUSTOMER RESPONSES (named where transcripts allow; Tier 2.5: by handle/role from the corpus)
[Customer/segment]: [response, grounded in their actual stated concerns/language]
...

SECRET-SOURCE CHECK: [what this output surfaced that a cold-generated panel could not have]

REAL-ASK ARMING: [the specific follow-up conversation this output should precede, and why the team is now primed for it]
NEXT STEP: [proceed to real conversation | escalate stakes → mt-synthetic-vs-real-decision.md]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] Transcripts (or, Tier 2.5, the harvested corpus) were loaded as sources, not pre-summarized before querying
- [ ] Grounding tier stated explicitly (2, 2.5 with corpus path + harvest date, or 1 only if actually calibrated)
- [ ] Responses are traceable to real customer language/concerns, not generic persona filler
- [ ] Output frames itself as arming a real follow-up, never replacing one
- [ ] The secret-source check confirms grounding added real signal vs. a cold-generated equivalent would have
- [ ] Tier 2.5 only: every corpus quote carries a real source URL; the corpus harvest date is ≤45 days old or the staleness is flagged explicitly

## Common Pitfalls
- **Summarizing the transcripts first.** Kills the texture that makes this Tier 2 instead of Tier 3 with extra steps.
- **Claiming Tier 1 confidence without calibration.** Loading transcripts is not the same as calibrating response-matching against them.
- **Treating grounded output as the final pitch.** It's rehearsal for the real conversation, not a replacement for it.
- **Skipping straight to Tier 3 when transcripts are absent.** The Gap-Fill Protocol exists precisely so "no transcripts" doesn't default to cold generation. Check/build the Tier 2.5 corpus first.
- **Running Tier 2.5 on a stale corpus without flagging it.** Zeitgeist drifts; a silently reused 90-day-old corpus reports today's confidence on yesterday's vocabulary.

Execution prompt: `references/prompts-v2/persona-grounding.md`
