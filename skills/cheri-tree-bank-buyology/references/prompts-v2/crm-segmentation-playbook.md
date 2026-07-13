---
name: "Cheri Tree — CRM Segmentation Playbook"
source_prompt: born-v2
skill: cheri-tree-bank-buyology
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are BANKifying a CRM on Cheri Tree's system. Hidden knowledge: **CRM is where B.A.N.K. becomes compounding** — if code insight stays in the seller's head, it disappears after the call; if it's stored and routed, the whole business sends better messages. But the plan must stay simple enough to maintain — an overbuilt segmentation scheme that nobody keeps updated is worse than a lightweight one that actually gets used.

## Input Required

- **[CRM OR LIST STRUCTURE]** — what tool/platform, current fields
- **[AVAILABLE FIELDS AND AUTOMATIONS]** — what the platform can actually do
- **[LEAD SOURCES, FUNNEL STAGES, OFFERS]**
- **[WHETHER B.A.N.K. CODE IS DIRECT, INFERRED, OR UNKNOWN]** — per lead source, if it varies

## Execution Protocol

1. **Define required fields and tags** — start from the minimum viable schema:
   - `bank_primary`
   - `bank_secondary`
   - `bank_code_confidence`
   - `bank_evidence`
   - `bank_next_test`
   - `bank_asset_route`
   - `bank_last_updated`
   Add fields beyond this minimum only if the input's CRM capability and campaign complexity justify it — do not overbuild by default.
2. **Create direct and inferred code capture paths** — direct (value-card ranking, self-assessment intake) and inferred (forensic reads, sales-call notes) both need a path into the same fields, tagged by source type.
3. **Map each code to sequences, sales notes, and content routes** — the routing map is the operational core of this deliverable: code -> which email/DM sequence -> which sales prep notes -> which content feed.
4. **Define confidence rules and re-scoring triggers** — when does a lead's code get re-scored (new evidence, contradicting behavior, a direct assessment finally completed)?
5. **Produce an implementation checklist and campaign examples** — concrete enough that someone could set this up today, plus 1-2 worked examples showing a lead moving through the system.

Minimum automations to include or explicitly scope out: route new leads to a code-specific welcome sequence; assign sales prep notes by primary code; tag content engagement by code signal; store direct self-assessment results when available; re-score when new evidence contradicts the current code.

## Output Contract

Deliver all six components:
1. **Field Schema** — field names and purpose
2. **Tagging Rules** — direct, inferred, unknown, confidence levels
3. **Routing Map** — code -> sequence -> sales action
4. **Data Capture Questions** — opt-in, form, call, or survey questions that populate the schema
5. **Automation Notes** — simple rules, matched to what the input's CRM can actually do
6. **Maintenance Checklist** — review and cleanup cadence

If the input's CRM cannot support complex routing, explicitly state that and provide the lightweight tag-and-note version instead of the full automation build.

## Output Skeleton

```
## Field Schema
| Field | Purpose |
|---|---|
| bank_primary | [...] |
| bank_secondary | [...] |
| bank_code_confidence | [...] |
| bank_evidence | [...] |
| bank_next_test | [...] |
| bank_asset_route | [...] |
| bank_last_updated | [...] |
[additional fields only if justified — name the justification]

## Tagging Rules
| Source Type | Tag | Confidence Default |
|---|---|---|
| Direct (self-assessment) | [...] | [...] |
| Inferred (forensic/call) | [...] | [...] |
| Unknown | [...] | [...] |

## Routing Map
| Code | Sequence | Sales Prep Note | Content Route |
|---|---|---|---|
[one row per code]

## Data Capture Questions
[opt-in / form / call / survey questions that populate bank_primary etc.]

## Automation Notes
[simple rules — matched to stated CRM capability; note if scoped down to lightweight tag-and-note]

## Maintenance Checklist
- [review cadence item]
- [cleanup item]
- [re-scoring trigger check]
```

## Quality Gate

- Does the Field Schema stay at or near the minimum viable set unless a stated reason justifies expanding it?
- Is direct vs. inferred code capture explicitly distinguished in the tagging rules (not merged into one undifferentiated "code" field)?
- Does the Routing Map name a specific sequence, sales note, and content route per code — not a shared default for all four?
- If the input's CRM can't support complex automation, does the output honestly scope down to the lightweight version rather than describing automations that can't be built?
- Does the Maintenance Checklist include a re-scoring trigger (what causes a lead's code to be revisited)?

## Deploy When

BANKifying a database or pipeline — setting up a new CRM's segmentation from scratch, or retrofitting code-awareness into an existing list/CRM structure.
