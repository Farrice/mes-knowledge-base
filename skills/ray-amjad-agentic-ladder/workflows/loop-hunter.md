---
description: Mine recurring manual work for loops and routines — outputs routine specs with hard constraints and approval gates
---

# Loop Hunter — Break Your Work Into Loops and Routines

Implements the 2→3 clause "break up your work into loops and routines" plus Ray's Loop Discovery Engine: loops are found by observing actual behavior, not by brainstorming from memory.

## Pre-Flight Gate

Load `genius.md` (patterns 9, 11, 12). Require at least one evidence source of real recurring behavior: session history/episodic memory, screen observations, chat logs, ticket queues, or a direct operator account of "things I check every day/week." Zero evidence → interview for concrete recurrences; never invent loops.

## Skill Acquisition

- `genius.md` — Loop Discovery Engine, Manual-Once Rule, Vision as Autonomy Filter, Capped Repair Loops
- `extractions/ray-amjad/extraction-report.md` — worked routines (PlanetScale weekly query optimization; PostHog friction→redesign; the 30-40-connector daily-recommendations loop; "find loops" meta-loop)

## Execution

1. **Harvest recurrences**: from the evidence, list behaviors matching the shape *[human periodically pulls data from X] → [judges] → [kicks off work]*. Ray's canonical catch: "checking LinkedIn DMs every day looking for feedback about shipped features."
2. **Convert each to a routine spec**: trigger/cadence · data pull (connector/source) · processing instruction · output form (report / draft / HTML mock / opened task) · delivery channel.
3. **Gate by vision**: aligned-with-vision actions may auto-execute; everything else gets a one-tap approval stage ("react with a thumbs up and I'll start implementing").
4. **Add hard constraints** per routine (his routines carry "a bunch of hard constraints"): scope limits, spend/token caps, do-not-touch lists, cadence ceilings.
5. **Install the meta-loop**: a standing find-loops routine that watches ongoing behavior and proposes new routine specs on a daily/weekly cadence — recommendations only, human picks.

## Content Type Adaptations

| Domain | Adaptation |
|---|---|
| Engineering | DB/query optimization, error triage, dependency maintenance loops |
| Product | Session-replay friction → redesign proposals; user-request → feature-draft loops |
| Business ops | Multi-connector daily-recommendations loop; inbox/DM monitoring with reply drafts |
| Content | Mention monitoring → suggested replies + draft assets |

## Output Requirements

Routine sheet: per routine — name · cadence · source pull · instruction · hard constraints · output+channel · autonomy class (auto vs approval-gated) — plus the meta-loop spec. Every routine traceable to observed evidence.
Execution prompt: `references/prompts-v2/loop-hunter.md` — honor its Output Contract.

## Quality Gate

Reject if: any routine lacks evidence of the recurrence; no hard constraints; proactive execution without a vision filter or approval stage; meta-loop empowered to create (rather than propose) routines.
