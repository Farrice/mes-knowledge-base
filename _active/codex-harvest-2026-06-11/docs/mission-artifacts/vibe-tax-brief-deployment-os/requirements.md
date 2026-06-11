# Requirements: Vibe Tax Brief Deployment OS

Created: 2026-05-11  
Mission: vibe-tax-brief-deployment-os

## Problem Frame

Turn The Vibe Tax Diagnostic and The Vibe Tax Brief into a daily deployment operating system with one command surface, a fresh-session bootstrap, research-proof discipline, Farrice voice, a first LinkedIn launch draft, and no unauthorized external action.

## Requirements

- R1. Provide `/vibe-tax-deploy` as the front door for deployment modes: `post`, `diagnostic`, `brief-demo`, `outreach`, and `daily`.
- R2. Extend existing `/vibe-tax-brief` and `/farrice-content-os`; do not create a competing OS.
- R3. Preserve a startup packet a fresh session can use without this chat history.
- R4. Require research citations or unavailable-state labels before public claims.
- R5. Require Farrice voice evidence before public/content drafting.
- R6. Require Hook Room, high-taste/anti-slop posture, and `/publishable-copy-gate` for public or revenue copy.
- R7. Keep all deployment output draft-only unless Farrice explicitly approves publishing, outreach, sharing, or external action.
- R8. Produce one first LinkedIn launch post introducing the Vibe Tax idea and diagnostic CTA.
- R9. Require mission package context resolution before any active `/vibe-tax-deploy` run drafts, routes, or hands off.
- R10. Make approved mission assets operationally mandatory, not merely documented: expert council, human resonance, stickiness, social distribution, sample brief, copy gate baseline, mission state, activation evidence, and deployment packet.

## Actors

- A1. Farrice: daily operator and final approver.
- A2. Codex session: runs `/vibe-tax-deploy` and composes outputs.
- A3. Vibe Tax buyer: solo B2B operator, consultant, agency, coach, creator, or service owner.
- A4. Validation layer: guards routing, research, copy quality, and external-action boundaries.

## Key Flows

- F1. Fresh session -> load bootstrap prompt -> run `/vibe-tax-deploy post` -> produce draft-only launch post.
- F1A. Fresh session -> run `mission_control.py context vibe-tax-brief-deployment-os` -> show Mission Handoff Receipt -> then run `/vibe-tax-deploy`.
- F2. Raw buyer/prospect context -> `/vibe-tax-deploy diagnostic` -> six-score diagnostic with paid-brief bridge.
- F3. Niche/prospect context -> `/vibe-tax-deploy brief-demo` -> proof demo with buyer phrases, hidden objections, proof gaps, and openers.
- F4. Prospect type -> `/vibe-tax-deploy outreach` -> manual qualified script with no automation.
- F5. Available time window -> `/vibe-tax-deploy daily` -> 1-4 hour execution loop.

## Acceptance Examples

- AE1. Given a fresh session with `BOOTSTRAP-PROMPT.md`, when the user asks for a Vibe Tax post, then Codex loads Vibe Tax, Farrice voice, research ledger, and copy gate before drafting.
- AE2. Given a public LinkedIn draft, when the work is finalized, then it includes Copy Gate Result and remains draft-only unless approved.
- AE3. Given a market claim, when it appears in public copy, then it is cited or labeled as local inference.
- AE4. Given a command search for Vibe Tax deployment, when `command_menu.py search` runs, then `/vibe-tax-deploy` appears.
- AE5. Given a fresh or resumed Vibe Tax deployment run, when the workflow starts, then it emits a Mission Handoff Receipt naming approved package files, activation evidence, proof artifacts, support gates, skipped items, and boundaries before drafting.
- AE6. Given a mission-backed workflow with only bootstrap and launch-post context, when validation runs, then the mission package handoff verifier fails.

## Scope Boundaries

- In scope: local workflows, command bridge, mission artifacts, startup packet, research ledger, launch draft, validation.
- Out of scope: publishing, auto-DMs, scraping, public sharing changes, paid-tool actions, or deleting prior plugin exports.

## Open Questions

- Blocking: none.
- Deferred: after first public response, calibrate language and CTA against real buyer replies.
