---
name: "Ghostwriting Voice Engine"
description: "Purpose-built system for capturing a coach's authentic voice and producing LinkedIn content that sounds like them on their sharpest day. Combines 5 expert methodologies: Lara Acosta (voice extraction), Mitch Albom (character embodiment), Erica Mallet (voice crystallization), Nicolas Cole (sentence refinement), Ward Farnsworth (rhetorical elevation)."
version: "1.0"
format: "completion-engine"
workflows: 3
---

# Ghostwriting Voice Engine

> Capture a coach's voice from a 30-minute call (or public content). Produce LinkedIn posts that sound like them — not like a ghostwriter, not like AI. The complete pipeline from intake to delivery.

This is a standalone delivery system for LinkedIn ghostwriting. It is **completely separate from MES** — different input (voice calls vs. transcripts), different output (client posts vs. skills/agents), different pipeline.

**Directive**: `directives/ghostwriting-delivery.md` — the full SOP governing this skill.
**Workflow command**: `/ghostwrite capture|produce|demo`

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 01 | [Voice Capture Pipeline](workflows/01-voice-capture.md) | Completed Voice Profile | You have a call transcript + intake assets (or public content samples) and need to build a deployable voice profile. |
| 02 | [Content Production Pipeline](workflows/02-content-production.md) | 3-5 LinkedIn Posts in Client Voice | You have a completed Voice Profile and need to produce posts that pass the 10-point Voice Authenticity Standard. |
| 03 | [Unsolicited Demo Pipeline](workflows/03-unsolicited-demo.md) | Before/After Demo Package + Warm Lead | You want to prove the system using a coach's public content (no call needed) — creates proof, content, and leads simultaneously. |

## Expert Stack

| Agent | Role | Deployed In |
|-------|------|-------------|
| **Lara Acosta** | 5-dimension voice extraction | Workflow 01, 03 |
| **Mitch Albom** | Character embodiment + belief mapping | Workflow 01, 03 |
| **Erica Mallet** | Voice crystallization + spectrum positioning | Workflow 01, 03 |
| **Nicolas Cole** | Sentence refinement + voice preservation | Workflow 02 |
| **Ward Farnsworth** | Rhetorical elevation (optional, premium) | Workflow 02 |

## Client-Facing Templates

| Template | Path | Used For |
|----------|------|----------|
| Call Script | `_active/offers/call-script.md` | The 30-minute structured voice capture call |
| Intake Form | `_active/offers/intake-form-questions.md` | Pre-call intake (5 questions for Google Form) |
| Voice Profile | `_active/offers/voice-profile-template.md` | Blank per-client voice profile template |
| Demo Workflow | `_active/offers/demo-workflow.md` | Manual SOP for running unsolicited demos |
| Before/After | `_active/offers/before-after-template.md` | 3 post templates for demo content |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Directive**: `directives/ghostwriting-delivery.md` — delivery SOP
- **Workflow Command**: `.agent/workflows/ghostwrite.md` — `/ghostwrite` routing
