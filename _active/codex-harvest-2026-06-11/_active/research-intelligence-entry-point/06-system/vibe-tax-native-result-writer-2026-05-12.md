# Vibe Tax Native Result Writer

> Status: Active operating runbook
> Date: 2026-05-12
> Owner: Farrice
> Primary surface: Codex
> External action boundary: draft-only unless explicitly approved

## What This Is

The Vibe Tax Native Result Writer is the Codex-native brain for turning a diagnostic response into a concise, high-authority Vibe Tax Read.

It keeps the stack simple:

- **Google Form or Notion Form** collects responses.
- **Google Sheet or Notion database** stores and scores responses.
- **Codex** writes the actual result.
- **Farrice** manually reviews and sends the first reads.

Gemini is optional. Notion AI is optional. Codex stays the final writer because it has the Vibe Tax package, Farrice voice, proof gates, and copy boundaries.

## The Command

Use:

```text
/vibe-tax-result-writer
```

It supports three operating modes:

| Mode | Use When | Output |
|---|---|---|
| `paste` | You paste one response row or Notion `Codex Input` block | one Vibe Tax Read |
| `sheet` | You ask Codex to scan the Google tracker for `Reply Status = New` | up to 3 drafted reads |
| `polish` | You paste a rough read from Notion AI or a prior draft | sendable result copy |

## Fastest Working Loop

1. Someone completes the diagnostic.
2. You copy the row or Notion `Codex Input`.
3. You paste it into Codex with the prompt below.
4. Codex drafts the result.
5. You review it.
6. You send it manually.
7. You track whether they reply, ask about price, or request the full brief.

This is intentionally concierge. The first goal is buyer language and proof, not automation.

## Paste-One-Response Prompt

```text
Run Vibe Tax Result Writer on this diagnostic response.

Use /vibe-tax-brief for diagnosis and /vibe-tax-deploy voice boundaries. Do not send anything externally.

[PASTE ROW OR NOTION CODEX INPUT HERE]
```

## Google Sheet Scan Prompt

```text
Scan the Vibe Tax Diagnostic Lab response tracker.

Find rows where Reply Status is New. Generate Vibe Tax Reads for up to 3 rows. Do not update the Sheet, send emails, or create documents unless I approve after reviewing the drafts.
```

Approved tracker:

```text
https://docs.google.com/spreadsheets/d/1OfZQHim1l086D3XzCyBwVe94PrMl-WzTPKugxutHOzY/edit
```

Codex may read this tracker when asked. Codex may not update row status, create result docs, or send emails unless explicitly approved.

## Polish Prompt

```text
Run publishable-copy-gate on this Vibe Tax Read. Keep it human, concise, and specific. Remove generic strategy language. Preserve the false signal, proof gap, and keep/revise/stop/test move.

[PASTE DRAFT]
```

## Required Input Fields

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

If `Total Score`, `Score Band`, or `Primary Leak` is missing, Codex calculates it from the six scored answers.

## Scoring

| Score | Band | Meaning |
|---:|---|---|
| 0-9 | High Vibe Tax | decisions are likely being made from weak or misleading signals |
| 10-17 | Noisy Signal | some useful evidence exists, but the buyer truth is still muddy |
| 18-24 | Proof Gap | the idea is close, but trust and proof are not yet strong enough |
| 25-30 | Shortlist Ready | the buyer signal is strong enough to build from |

Primary leak is the lowest dimension, with this tie-break order:

1. False Signal Risk
2. Proof Gap
3. Buyer Language Fit
4. Shortlist Readiness
5. Human Resonance
6. Social Repeatability

## Result Structure

```markdown
# Vibe Tax Read: [Name or Business]

## Snapshot
- **Score:** [total] / 30
- **Band:** [band]
- **Primary leak:** [dimension]
- **Decision:** [decision]

## What I Would Distrust First
[The false signal most likely distorting the decision.]

## The Proof Gap
[What the buyer still cannot safely believe yet.]

## Keep / Revise / Stop / Test
- **Keep:** [what is worth preserving]
- **Revise:** [what needs sharper buyer language, proof, or framing]
- **Stop:** [what weak signal should stop being treated as truth]
- **Test:** [one small next market check]

## Full Brief Bridge
[Soft invitation to the 48-hour Vibe Tax Brief if the gap needs deeper research.]
```

## Quality Bar

A useful Vibe Tax Read must include:

- score, band, and primary leak
- one false signal
- one proof gap
- one keep, revise, stop, and test move
- one paid-brief bridge when appropriate
- no mention of AI
- no invented context
- no generic strategy language

## Notion Bridge

In the Notion database, create a formula or text property called `Codex Input`.

That property should return a clean block using the required input fields above. Copy that block into Codex when you want the final result.

The Notion row can be the intake and operations layer. Codex should remain the diagnostic writer.

## Tracker Fields To Update Only After Approval

After Farrice approves a result, Codex may be asked to update:

- `Reply Status`
- `Result Doc Link`
- `Paid Interest`
- `Buyer Phrase`
- `Objection`
- `Follow-Up Notes`

Default behavior is read-only. Updating is a separate approval step.

## First Test

Use a sample row with scores:

```text
Buyer Language Fit: 0
Shortlist Readiness: 1
Proof Gap: 3
False Signal Risk: 5
Human Resonance: 5
Social Repeatability: 3
```

Expected score:

```text
17 / Noisy Signal / Buyer Language Fit
```

Then paste the generated `Codex Input` block into Codex and confirm the result is stronger than a rough Notion AI draft.
