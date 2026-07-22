---
description: Set up the create → schedule → opt-in auto-DM backbone for an account (TweetHunter-class). AI-batch posts with a human claim-edit gate, schedule on autopilot, and auto-DM only on like/comment opt-in.
---

# `/suzuki-automate` - Automation Engine

## When To Use
- "Set up auto-posting and auto-DM for this account."
- Move from manual posting to a scheduled, autopilot funnel.
- Build the opt-in auto-DM that delivers the free asset/link at scale.

## Load
1. `skills/alex-suzuki-digital-product-revenue-os/SKILL.md`
2. `skills/alex-suzuki-digital-product-revenue-os/workflows/15-automation-engine.md`
3. `skills/alex-suzuki-digital-product-revenue-os/references/scaling-mechanics.md`
4. `skills/alex-suzuki-digital-product-revenue-os/references/compliance-gate.md`

## Execute
Run the Automation Engine. Separate create / schedule / convert. The auto-DM fires ONLY on an opt-in trigger (like/comment) — never cold mass-DM. Insert the human claim-edit gate between generation and scheduling. Provide opt-out and a platform-ToS note.

## Usage
```text
/suzuki-automate [platform] [offer] [free asset] [cadence]
```

## Required Output
- Create plan (batch-gen + human claim-edit gate)
- Schedule plan (cadence, queue, autopilot windows)
- Auto-DM map (opt-in trigger → value lane / purchase lane)
- Compliance block (opt-in only, opt-out, rate/ToS, per-platform)
- Human-escalation rules
- Metrics + kill/keep rule

**Execution prompts**: before producing the deliverable, check `skills/alex-suzuki-digital-product-revenue-os/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
