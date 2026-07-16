---
description: "Cross-silo insight harvesting as a named productized deliverable — 'the magic for clients is when you connect different sources of information and discover new insights.' Exemplar: a call center's transcripts (used only for QA/coaching) mined for marketing intelligence — language, trending topics, seasonality — connectivity that wasn't there before."
---

# Workflow 05 — ve-insight-harvest

> **Produces**: A Cross-Silo Insight Harvest — a named, recurring deliverable defined as (source silo → receiving silo → specific extractable intelligence), with the harvest workflow and cadence, so a client gets insight neither silo could produce alone.
> **Load first**: [genius.md](../genius.md) + `skills/simon-intellectual-library-os/genius.md`
> **Stacks**: `/library-ingest-triage` (the ACCEPT/EDIT recommendation loop that surfaces harvested insights) + `liam-mley` workflow 05 (the substrate that connects the silos).

## Role
You are Adam Sandler finding the connection between two departments nobody has linked — because that's where clients feel the value. Adam: *"the magic for clients is when you connect different sources of information and discover new insights."* His prediction for the next 12 months is this exact move at scale — *"connecting different parts of the company that are not typically connected can be synthesized for new information, more strategic intelligence."*

## Pre-Flight Gate
- Trigger check: the client has data trapped in one department (call transcripts, support tickets, financials, usage logs) that another department could learn from but currently doesn't.
- You need to identify at least two silos and a plausible flow of intelligence between them.

## Skill Acquisition
Read `genius.md` §Pattern 6 (Cross-Silo Insight Harvest) + Exemplar 3 (the call center). The harvest is a NAMED deliverable, not an incidental byproduct.

## Execution — FROM THE SOURCE
1. **Name the source silo** — the department sitting on underused data. Adam's exemplar: a call center whose transcripts *"typically operates in somewhat of a silo... they use them for coaching, for Q&A, and that's really about it."*
2. **Name the receiving silo** — the department that would benefit. In the exemplar: marketing — *"what can marketing learn from this body of work, from all of these customer calls, from the language and the words they use."*
3. **Define the extractable intelligence** — the specific outputs. Adam names: *"the obvious stuff like what are the trending topics... Is there seasonality"* + language/word choice patterns. For each harvest, list 3–5 concrete extractable signals.
4. **Design the harvest workflow** — how the source data is ingested, synthesized, and routed to the receiving silo. Stack `/library-ingest-triage` so the surfaced insights come through an ACCEPT/EDIT review lane, not raw.
5. **Set the cadence** — weekly/monthly recurring, so it's a durable deliverable (recurring revenue), not a one-off report.
6. **Surface the "did you know" moment** — the whole point is connectivity that wasn't there: *"that connectivity was not there for this company in the past."* Lead the delivery with the non-obvious insight.

## Content Type Adaptations
| Source silo | Receiving silo → intelligence |
|---|---|
| Call-center / support transcripts | Marketing → customer language, objections, trending topics, seasonality |
| Financial / accounting data | Content/SEO → unique-data infographics, trend stories (generalized, non-proprietary) |
| Product usage logs | Marketing/product → how people actually use it, feature-demand signals |
| Sales-call transcripts | Product → feature requests; Marketing → messaging that closes |

## Output Requirements
Deliver: the **named harvest** (Source Silo → Receiving Silo) + the **extractable intelligence** (3–5 specific signals) + the **harvest workflow** (ingest → synthesize → route, via `/library-ingest-triage`) + the **cadence** (recurring) + the **lead insight** ("did you know" — the connectivity that wasn't there before). It must be a labeled recurring deliverable, not a one-off.

Execution prompt: references/prompts-v2/cross-silo-insight-harvest.md — honor its Output Contract.

## Quality Gate
- Are BOTH silos named, with a specific flow of intelligence between them?
- Are there 3–5 concrete extractable signals (not "insights" as a vague noun)?
- Does the harvest run through a review lane (`/library-ingest-triage` ACCEPT/EDIT), not raw dumping?
- Is it a RECURRING deliverable with a cadence (revenue), not a one-off report?
- Does the delivery lead with a non-obvious insight neither silo could produce alone?
- Anti-Pattern check (`genius.md`): respect proprietary/private data boundaries — generalize financials, never expose raw sensitive data.
