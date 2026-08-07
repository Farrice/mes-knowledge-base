# Low-Cognitive-Load Message Gate

## Purpose

Use this primitive when a message, offer, draft, hook, homepage, pitch, content package, or sales asset needs to become easier to understand before downstream writing, content, or copy work begins.

The goal is not to make the writing prettier. The goal is to remove the mental work required to know:

- what problem is being solved
- who the message is for
- why the reader should care
- what the answer is
- what phrase should repeat everywhere

## Source Evidence

Newest source package:

- `extractions/video-context/SzugliCQ3XY/`
- Source URL: `https://www.youtube.com/watch?v=SzugliCQ3XY&t=100s`
- Source identity from local metadata: "This CEO Used Messaging to Scale to $100M" from StoryBrand With Donald Miller, published 2026-05-25. Donald Miller interviews Tricia Sciortino of BELAY.
- Correction note: this is not the Jay Schwedelson Guru Conference source; use the local metadata over the earlier planning assumption.
- Evidence policy: use observed spoken, visual, and OCR rows only when the local ledger contains them; preserve `uncertain_or_unavailable` rows.

Existing Donald Miller grounding:

- `extractions/donald-miller/storybrand-message-clarity-system/`
- `extractions/video-context/d4Pmq27udNc/`
- `extractions/video-context/5OJT1ph-yL4/`
- `skills/donald-miller-cognitive-load/`
- `skills/donald-miller-storybrand/`

## Operating Definition

Low-cognitive-load messaging means the reader can understand and repeat the message without decoding jargon, hidden context, stacked promises, or clever abstractions.

This primitive is a companion OS layer, not a replacement owner.

| Surface | Owner | How This Gate Helps |
|---|---|---|
| `/storybrand-message-clarity-system` | StoryBrand orchestrator | Checks one-problem, PEACE, hero/guide, and repeatability before producing the pack. |
| `/farrice-content-os` | Content system | Ensures source/product/offer content starts with one clear reader problem before hooks and packaging. |
| `/high-taste-writing-os` | Writing craft system | Prevents polishing cognitively heavy drafts. |
| `/publishable-copy-gate` | Public/revenue copy gate | Adds clarity as an upstream requirement before conversion scoring. |
| Writing Agent | Writing owner | Uses the gate when narrative or authority writing carries a brand/product/service message. |
| Copywriting Agent | Conversion owner | Uses the gate when an offer/copy asset is selling too many things or forcing interpretation. |

## Required Checks

| Check | Pass Standard | Failure |
|---|---|---|
| One-Hole Lock | One felt problem, no bundled pains | REWORK |
| PEACE Fit | Problem, Empathy, Answer, Change, End Result are present or drafted | REVISE |
| Hero/Guide Fit | Customer is hero; brand/product is guide, tool, or rope | REVISE or REWORK |
| Cognitive Load | Heavy phrases are named and simplified | REVISE |
| Repeatability | One exact phrase can repeat across channels | REVISE |
| Evidence Discipline | Source claims match local evidence limits | REWORK if overclaiming |

## Handoff Shape

```markdown
## Low-Cognitive-Load Handoff
- **Locked problem**:
- **PEACE status**:
- **Hero/guide correction**:
- **Heavy phrases to rewrite**:
- **Repeatability lock**:
- **Evidence limits**:
- **Verdict**:
- **Next owner**:
```

## Phrase Load Categories

| Category | Signal | Pass Standard |
|---|---|---|
| Jargon load | Internal or expert language. | Customer would say it naturally. |
| Abstract promise load | Big promise without concrete before/after. | Reader can picture the result. |
| Multi-problem load | One line carries several pains. | One problem is selected. |
| Cleverness load | Memorable but interpretive. | Clear before clever. |
| Hero confusion load | Brand or founder leads the story. | Customer remains the hero. |
| Product-first load | Offer arrives before the hole is felt. | Problem precedes answer. |

Use `0 lbs`, `25 lbs`, `50 lbs`, `75 lbs`, or `100 lbs`. A `0 lbs` phrase must be plain enough for a non-specialist to repeat after one read.

## Placement Rules

- Use before polishing, scoring, or publishing, not after the final draft is already locked.
- Keep the gate compact. It should produce a decision and handoff, not a full rewrite unless the missing clarity is small.
- Do not create a new Donald Miller expert package for this; use the existing Donald Miller skills and StoryBrand orchestrator.
- Do not hot-promote the workflow. Keep it cold/on-demand unless repeated use proves it should become a front-door route.
- Do not claim visual or on-screen evidence from `SzugliCQ3XY` unless the local full-mode package contains frame or OCR rows.

## Quality Bar

A passing message should let a non-specialist say:

- "This is for people like me."
- "This solves this one problem."
- "This guide knows what I am dealing with."
- "The answer is simple enough to remember."
- "I can repeat the phrase without sounding like a consultant."
