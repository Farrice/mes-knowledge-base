---
name: "Dr. Kriukow AI Humanization"
description: 'Humanizes AI-written prose using Dr. Kriukow''s diagnostic-first methodology — structural unpredictability (varying sentence rhythm, paragraph weight, transition mechanics in ways AI defaults don''t), detection-tool evasion patterns, and writing that survives algorithmic AI-prose detectors AND human "this feels AI" intuition. Use when AI-drafted content needs to pass GPTZero / Originality.ai / similar detectors before publication, content reads "technically fine but feels generated", a draft needs structural rhythm fixes (not just word swaps), or training the user''s eye on the structural patterns that betray AI authorship. Trigger proactively whenever the user says "this sounds AI-generated", "humanize this", "AI detection", "Originality.ai", "GPTZero", or shares a draft that needs the AI fingerprint removed at structural level. For phrase-level AI-tell scrubbing (em-dashes, "Here''s what" openers) use prose-check or slop-check; for the structural-tells ban list use the writers-room workflow.'
version: "2.0"
format: "completion-engine"
workflows: 2
---

# Dr. Kriukow AI Humanization

> **Extracted from**: Dr. Jaroslaw Kriukow — Qualitative researcher and AI text humanization specialist
> **Domain**: AI content humanization, detection evasion, structural unpredictability, writing quality optimization
> **System Role**: Diagnostic safety net — use when content lacks a strong writer voice or feels AI-detectable
This skill implements Dr. Kriukow's Statistical Unpredictability Principle (SUP): AI writing and AI detection both operate on statistical probability. The most effective

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| diagnostic | [Diagnostic Humanization Safety Net](workflows/diagnostic-humanization-safety-net.md) | AI Detection Risk Report & Humanized Draft | You have raw AI output and need to verify its predictability and apply a quick safety pass to reduce detection risk. |
| meaning | [Meaning-First Content Reconstruction](workflows/meaning-first-content-reconstruction.md) | Voice-Calibrated Humanized Manuscript | You are creating high-stakes content that requires a specific human voice and a deep, structural rewrite that preserves meaning while discarding AI syntax. |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived atomic prompts
