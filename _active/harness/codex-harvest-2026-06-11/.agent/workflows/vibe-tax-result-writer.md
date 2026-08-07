---
description: Generate native Codex Vibe Tax Reads from pasted diagnostic rows, Notion Codex Input blocks, or approved tracker scans
---

# /vibe-tax-result-writer - Native Vibe Tax Read Writer

## Objective

Turn one Vibe Tax Diagnostic response into a concise, human, sendable Vibe Tax Read.

Use this when Farrice pastes:

- one Google Form or Google Sheet response row
- one Notion `Codex Input` block
- one rough Notion AI result that needs to become sendable
- a request to scan the response tracker for `Reply Status = New`

This command is the native Codex result-writing surface. `/vibe-tax-brief` owns diagnosis. `/vibe-tax-deploy` owns public launch and outreach. `/vibe-tax-result-writer` owns the concierge result read.

## Source Stack

Use these in order when available:

1. `.agent/workflows/vibe-tax-brief.md`
2. `.agent/workflows/vibe-tax-deploy.md`
3. `_active/research-intelligence-entry-point/README.md`
4. `_active/research-intelligence-entry-point/LEAD-MAGNET.md`
5. `_active/research-intelligence-entry-point/HUMAN-RESONANCE-GATE.md`
6. `_active/research-intelligence-entry-point/RESEARCH-BRIEF-TEMPLATE.md`
7. `_active/research-intelligence-entry-point/COPY-GATE-RESULT.md`
8. `_active/research-intelligence-entry-point/06-system/vibe-tax-diagnostic-lab-portable-schema-2026-05-12.md`
9. `_active/research-intelligence-entry-point/04-deliverables/vibe-tax-google-ship-checklist-2026-05-12.md`

For launch/public copy, also apply `.agent/workflows/publishable-copy-gate.md`.

## Modes

```text
/vibe-tax-result-writer paste [response row or Codex Input block]
/vibe-tax-result-writer sheet [optional limit, default 3]
/vibe-tax-result-writer polish [rough read]
```

### paste

Parse the pasted row or Notion `Codex Input` block and produce one Vibe Tax Read.

If the response includes a real asset, link, pasted copy, buyer phrase, objection, or follow-up note, use only what is present. Do not invent missing business context.

### sheet

Read the approved Google Sheet tracker and find rows where `Reply Status = New`.

Approved tracker:

```text
https://docs.google.com/spreadsheets/d/1OfZQHim1l086D3XzCyBwVe94PrMl-WzTPKugxutHOzY/edit
```

Default behavior:

- generate drafts for up to 3 new rows
- do not update the Sheet
- do not send emails
- do not create Google Docs
- do not mark rows as sent

Only update tracker fields after Farrice explicitly approves the exact updates.

### polish

Improve a rough Vibe Tax Read so it is human, specific, and sendable.

Preserve:

- false signal
- proof gap
- keep, revise, stop, or test action
- paid brief bridge when appropriate

Remove:

- generic strategy language
- unsupported certainty
- AI-coded language
- fake urgency
- vague claims that do not change the reader's next move

## Input Contract

Expected fields:

```text
Name:
Email:
Business Type:
Decision:
Buyer Language Fit:
Shortlist Readiness:
Proof Gap:
False Signal Risk:
Human Resonance:
Social Repeatability:
Total Score:
Score Band:
Primary Leak:
Asset Or Decision:
Buyer Phrase:
Objection:
Follow-Up Notes:
```

If `Total Score`, `Score Band`, or `Primary Leak` is missing, calculate them from the six scored answers.

## Scoring Rules

Total score is `0-30`.

| Score | Band |
|---:|---|
| 0-9 | High Vibe Tax |
| 10-17 | Noisy Signal |
| 18-24 | Proof Gap |
| 25-30 | Shortlist Ready |

Primary leak is the lowest score. Use this tie-break order:

1. False Signal Risk
2. Proof Gap
3. Buyer Language Fit
4. Shortlist Readiness
5. Human Resonance
6. Social Repeatability

## Required Result Format

```markdown
# Vibe Tax Read: [Name or Business]

## Snapshot
- **Score:** [total] / 30
- **Band:** [band]
- **Primary leak:** [dimension]
- **Decision:** [offer/content/page/positioning/campaign/sales message]

## What I Would Distrust First
[One concise, specific read on the false signal most likely distorting the decision.]

## The Proof Gap
[What the buyer still cannot safely believe yet, and why that matters.]

## Keep / Revise / Stop / Test
- **Keep:** [one thing worth preserving]
- **Revise:** [one thing to tighten]
- **Stop:** [one weak signal to stop treating as truth]
- **Test:** [one small next market test]

## Full Brief Bridge
[Soft invitation to the 48-hour Vibe Tax Brief if the gap is deeper than the free read.]
```

Keep the read under 700 words unless Farrice asks for a deeper pass.

## Quality Gates

Before finalizing, check:

- **Truth:** Every claim is based on the pasted row, the score, or clearly marked inference.
- **Human resonance:** The reader feels seen, not judged.
- **Proof:** The read includes at least one false signal and one proof gap.
- **Action:** The read gives a concrete keep, revise, stop, and test move.
- **Bridge:** The paid brief feels like the logical next step, not a pressure tactic.
- **Copy:** No generic AI, strategy, or optimization language.

## Hard Rules

- Do not mention AI in the buyer-facing result.
- Do not invent facts from a link that was not opened or content that was not pasted.
- Do not use unsupported market stats in a personal result.
- Do not publish, send, DM, email, update databases, or create external documents without explicit approval.
- Do not treat the score like a grade. Treat it like a warning light.
- If the input is too thin for a meaningful read, say what is missing and produce a lighter read labeled as based on limited input.

## Recommended Prompts

Paste one response:

```text
Run Vibe Tax Result Writer on this diagnostic response.

Use /vibe-tax-brief for diagnosis and /vibe-tax-deploy voice boundaries. Do not send anything externally.

[PASTE ROW OR NOTION CODEX INPUT HERE]
```

Scan the tracker:

```text
Scan the Vibe Tax Diagnostic Lab response tracker.

Find rows where Reply Status is New. Generate Vibe Tax Reads for up to 3 rows. Do not update the Sheet, send emails, or create documents unless I approve after reviewing the drafts.
```

Polish a draft:

```text
Run publishable-copy-gate on this Vibe Tax Read. Keep it human, concise, and specific. Remove generic strategy language. Preserve the false signal, proof gap, and keep/revise/stop/test move.
```
