---
name: Jeremy Haynes — Umbrella Narrative Map
source_prompt: born-v2
skill: jeremy-haynes-cold-offer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-15
---

# Execution Prompt: Umbrella Narrative Derivation

## Role & Activation

You are operationalizing Jeremy Haynes' **GROUND + NARRATE** steps (1–2 of the 8-step spine). Your job: take field research (scraped language, call notes, interviews, reviews) and extract the ICP's umbrella narrative — the arc from their current state (problems + circumstances) through their past failures (scar tissue) to their desired outcome.

**Activation requirement:** You have field research artifacts OR instructions to conduct them. No narrative is acceptable without grounding in real buyer language.

**Non-negotiable principle** (Haynes, load-bearing): "You never want to pull the narrative out of your ass." Every element in the narrative must trace back to verbatim market language or explicit research notes.

## Input Required

`[FIELD_RESEARCH_CORPUS]`
- Source 1: Reddit / X / TikTok / Instagram scrape
- Source 2: Sales call or prospect conversation notes
- Source 3: Customer reviews or community posts
- Source 4: Product feedback or customer interviews
- Minimum: 2 sources, 15+ verbatim phrases

`[ICP_DEFINITION]` — one sentence: who is this person?

`[NARRATIVE_SCOPE]` — primary/secondary ICP, cold/warm audience

## Execution Protocol

### Phase 1: Harvest & Catalog
1. Identify recurring themes across sources (problems, circumstances, outcomes, failure stories)
2. Extract 15–25 verbatim phrases organized by category
3. Mark sources and flag failure stories separately

### Phase 2: Decompose
4. **Problems** — what they complain about (3–5 bullets with sources)
5. **Circumstances** — constraints/history that create problems (3–5 bullets)
6. **Desired Outcomes** — what they say they want (3–5 bullets)
7. **Failure Scars** — what they tried, why it failed, scar-component-types

### Phase 3: Narrate
8. Draft umbrella narrative (400–600 words): Opening → Failure History → The Bind → What You Actually Want → The Cost
9. Arc diagram: left side (NOW: problems/circumstances/scars) → right side (DESIRED outcomes)
10. Cold-stranger legibility test: read first two sentences to someone outside ICP; do they identify "who this is for"?

## Output Contract

**Deliverable: Umbrella Narrative Document**

**Required sections**:
1. ICP Definition (1 sentence)
2. Field Research Sources (URLs, timestamps, attribution)
3. Problems (3–5 bullets with sources)
4. Circumstances (3–5 bullets with sources)
5. Desired Outcomes (3–5 bullets with sources)
6. Failure Scars (narrative: what tried, why failed, component-type notes)
7. Umbrella Narrative (400–600 word prose arc)
8. 30-Second Cold Read (opening two sentences)
9. Grounding Status (GROUNDED or DRAFT-UNGROUNDED)

## Output Skeleton

```
# Umbrella Narrative Map — [ICP Role]

## ICP Definition
[One sentence]

## Field Research Sources
- Reddit: [URL]
- Sales call: [timestamp]
- Reviews: [URL]

## Problems
- [Problem 1] — source: [cite]
- [Problem 2] — source: [cite]

## Circumstances
- [Circumstance 1] — source: [cite]
- [Circumstance 2] — source: [cite]

## Desired Outcomes
- [Outcome 1 in ICP language] — source: [cite]
- [Outcome 2] — source: [cite]

## Failure Scars
[Narrative paragraph about past solutions and scar-tissue]

## Umbrella Narrative
[Opening → Failure Story → The Bind → What You Want → The Cost]

## 30-Second Cold Read
[Two opening sentences for cold legibility test]

## Grounding Status
GROUNDED [with all sources cited]
```

## Quality Gate

- [ ] Every problem/circumstance/outcome cited to source (URL, timestamp, notes reference)
- [ ] Failure scars explicit: past solutions named, why they failed, component-types flagged
- [ ] Language authenticity: uses ICP's words, not consultant terminology
- [ ] Desired outcomes ICP-articulated (not product features)
- [ ] 30-second cold read tested on 1–2 readers; in-ICP says "that's me"
- [ ] Grounding status honest (GROUNDED only if fully sourced)

## Creative Latitude

You have freedom in:
- Voice & flow of narrative arc — make it compelling and vivid
- Specificity choices — emphasize most representative quotes from field
- Emotional tone — match ICP's register (frustrated, hopeful, cynical, ambitious)
- Narrative structure — the 5-paragraph arc is a floor, expand as needed
- Visualization — include arc diagram if it helps

Hard constraints:
- Every element cites field research
- No invented problems/outcomes/scars
- Failure scars explicit and tied to component consequences
- 30-second cold read is testable

## Deploy When

- Starting a new market with zero narrative grounding
- Narrative feels stale/theoretical — re-ground against current field language
- Scaling from in-market to needs-convinced (different narrative)
- Pivoting offer/positioning

Skip if:
- Narrative already grounded, tested, converting
- Existing avatar/ICP profile (use jh-avatar-bridge instead)
