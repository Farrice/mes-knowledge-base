---
name: "source-command-expert-composition-governor"
description: "Detect and prevent expert soup by composing many experts, skills, workflows, or agents into one owner-led outcome"
---

# source-command-expert-composition-governor

Use this skill when the user invokes `/expert-composition-governor`, says "expert soup," "too many agents," "not interwoven," "hammer instead of scalpel," wants the full arsenal, wants true end-to-end arsenal deployment, or asks how to compose many experts/skills/workflows without generic output.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/expert-composition-governor.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- prevent expert soup and full-arsenal sprawl
- use when more than three experts/routes are plausible or the user asks for the full arsenal
- one function owner integrates the final result
- specialists occupy bounded slots and return specific contributions, preservation notes, and downstream risk
- Composition Ledger shows accepted, skipped, or rejected contributions with evidence of change
- expert names are not proof; integration evidence is proof
- no real Codex subagents unless explicitly authorized
- broad broken-harness triage routes to `/autopilot` or `/system-audit`
- reusable source-to-system builds route to `/source-to-skill-system`
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/expert-composition-governor.md` - Expert Composition Governor.

Do not create `.docx`, HTML, Canva, Google Docs, Notion, or PDF exports unless explicitly requested.
