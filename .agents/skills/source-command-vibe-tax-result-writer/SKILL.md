---
name: "source-command-vibe-tax-result-writer"
description: "Migrated source command `vibe-tax-result-writer`"
---

# source-command-vibe-tax-result-writer

Use this skill when the user asks to run the migrated source command `vibe-tax-result-writer`.

## Command Template

# /vibe-tax-result-writer

Generate native Codex Vibe Tax Reads from pasted diagnostic rows, Notion `Codex Input` blocks, rough drafts, or approved response-tracker scans.

Codex runtime source of truth:

```text
.agent/workflows/vibe-tax-result-writer.md
```

Use this command when Farrice wants to:

- paste one diagnostic response and get a concise Vibe Tax Read
- scan the Vibe Tax Diagnostic Lab tracker for `Reply Status = New`
- turn a Notion row into a better Codex result
- polish a rough read through the publishable-copy gate

Hard boundaries:

- no public posting
- no emails
- no DMs
- no database updates
- no Google Doc creation
- no external action without explicit approval

Buyer-facing result format:

```markdown
# Vibe Tax Read: [Name or Business]

## Snapshot
## What I Would Distrust First
## The Proof Gap
## Keep / Revise / Stop / Test
## Full Brief Bridge
```

For implementation details, read and execute `.agent/workflows/vibe-tax-result-writer.md`.
