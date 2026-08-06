---
name: "Brad Bonanno — Explainer-Video Architecture"
description: 'Architects technical explainer videos using Brad Bonanno''s structural patterns — survives short attention spans, communicates complete systems (not just teasers), and functions as a channel-building artifact (one video pulls subscribers, not just views). Use when planning a long-form technical explainer (5-20 min) for YouTube, structuring an explanation of a complex system the user knows but can''t teach yet, balancing depth vs accessibility for a technical audience, or building an evergreen video meant to compound subscriber growth over years rather than spike then die. Trigger proactively whenever the user says "explainer video", "technical explainer", "how do I explain X", "long-form YouTube", "evergreen video", or has a complex system that needs to land with a non-expert. For Instagram-format shareworthy content use brock-johnson-shareworthy-content; for short-form video patterns use a TikTok/Reels-specific skill.'
version: "2.0"
format: "completion-engine"
workflows: 4
expert: "Brad Bonanno"
domain: "explainer-video architecture for technical creators"
---

# Brad Bonanno — Explainer-Video Architecture

## Expert Context

**Brad Bonanno** (`@bradbonanno`, Brad | AI & Automation) is an AI/automation YouTuber and indie maker. His real skill isn't the tools he ships — it's the meta-skill of structuring 5-10 minute explainer videos that compress technical systems into watchable artifacts that ALSO build a channel.

**What this skill captures**: The structural patterns behind Brad-style explainer videos:
1. The 15% Demo Rule — talking-head dominates; demo cuts are surgical
2. Single Source Demo Discipline — one flagship example across the whole video
3. The Matrix Moment — split-screen temporal proof for speed claims
4. Branded Infographic Frames — 2-4 trust anchors per video
5. Pre-empt the Skeptic — name objections in viewer's voice, rebut with infographic proof
6. The Compound Cliffhanger — close one loop, open a bigger promise tied to next video
7. Free + Open-Source as Positioning — give away the artifact, audience-build compounds

**First visual-aware extraction in the system**: 6 of 7 patterns required visual evidence to extract. Transcript-only ingestion would have missed the entire meta-skill.

**Corpus** (multi-source; extend here, never mint a duplicate Bonanno skill):
- `extractions/brad-bonanno/` — "My Claude Code Can INSTANTLY Watch Any Video" (QZMljuD10sU, 2026-05-03) — the explainer-architecture source behind this skill.
- `extractions/brad-bonanno-edit-bay/` — "My Claude Code Edits FULL Videos in One Shot" (mlhhZSHIS-w, 2026-08-06) — his 6-stage agentic EDITING pipeline (WhisperX → cuts → B-roll → HyperFrames → SFX → export + watch-loop QA). MES 3.0 report: `extraction-report.md` there. Operationalized as the Edit Bay: `skills/video-studio/`.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---|---|---|
| 01 | [The Pause Test Audit](workflows/01-pause-test-audit.md) | Frame-by-frame audit of an existing video draft + scorecard + top 3 structural rewrites | Pre-publish diagnostic for any explainer video. Catch dead pauses, missing infographics, and modality-mix failures before launch |
| 02 | [The Matrix Moment Architect](workflows/02-matrix-moment-architect.md) | Pre-recording demo strategy: source artifact selection, visual hierarchy, temporal proof beat structure, shot list | Generative pre-production. Lock the demo strategy before the camera rolls |
| 03 | [The Trust-Anchor Infographic Brief](workflows/03-trust-anchor-infographic-brief.md) | Design briefs for 2-4 branded infographic frames anchoring the highest-trust-impact claims in your script | Generative post-script, pre-motion-graphics. Hand-off-able to a designer |
| 04 | [The Compound Cliffhanger Closer](workflows/04-compound-cliffhanger-closer.md) | Engineered final 60-90 seconds: closure beat + pivot + bigger-promise tease + explicit handoff + subscribe close | When building a YouTube channel where individual videos need to compound. Skip for standalone evergreen videos |

## Genius Context

Read [genius.md](genius.md) before executing any workflow. It contains:
- 7 genius patterns with executable behaviors and success metrics
- 6 hidden-knowledge items (the structural insights only visual analysis surfaced)
- 3 hall-of-fame exemplars from the source video
- 1 anti-exemplar (what failure looks like)
- 5 signature moves
- 7-criterion quality rubric (1-5 scale, 35 total)
- Cross-expert stacking map

## Quick Reference

**The Quality Rubric** (audit ANY explainer video):
1. Modality Mix Discipline (target: 70-80% TH, 10-20% demo, 5-15% IG)
2. The Pause Test (every 5-second interval delivers value)
3. Single-Source Demo Discipline (one flagship artifact across all demos)
4. Pre-empted Objections (2+ named in viewer's voice + infographic-anchored proof)
5. Trust-Anchor Infographic Count (2-4 frames with consistent visual language)
6. Compound Cliffhanger (next-video promise + dashboard tease)
7. Bottom-Left PIP Discipline (face guides, doesn't compete with demo)

**Pass threshold**: 25/35. Top 10%: 30+/35.

## Stacking Guide

| When you're working on... | Pair this skill with |
|---|---|
| LinkedIn carousels | × Lara Acosta hook engineering — the Pause Test transfers as "every slide stands alone" |
| Brand strategy | × Creative Director / `/storyboard` — the Matrix Moment is a reusable storyboard archetype |
| Substack series (Parallax) | × Compound Cliffhanger Architecture — each edition closes one loop, opens the next |
| Long-form newsletters | × Nicolas Cole — the 15% Demo Rule transfers as "every paragraph must stand alone" |
| Sales pages | × Universal Pause Test — every section must summarize the offer |
| Course design | × Single-Source Discipline — one running example across all modules |

## When This Skill Doesn't Apply

- Long-form podcasts (45-90 min) — different cognitive contract
- Live event recordings — modality mix is constrained by physical setup
- Pure audio content — visual patterns don't transfer (but Pause Test does — applies to "is any 30-second segment skippable?")
- One-take vlogs without editing — these workflows assume post-production planning

## Source Material

- **Source video**: https://www.youtube.com/watch?v=QZMljuD10sU
- **Source extraction**: `extractions/brad-bonanno/extraction-report.md`
- **Visual context**: `extractions/brad-bonanno/visual-context.md` (398 lines, 80 frames)
- **Genius context**: [genius.md](genius.md)

## Activation

The skill auto-activates when the user's request involves:
- Auditing an existing video draft for structural quality
- Designing a demo strategy for an upcoming video
- Producing infographic briefs for trust-anchor claims
- Engineering a video close that drives next-video conversion
- Cross-domain transfers of the Pause Test, modality mix, or single-source discipline

Invoke directly via:
- `/brad-pause-test-audit <video-url-or-path>`
- `/brad-matrix-moment <thesis>`
- `/brad-trust-anchor <script-path>`
- `/brad-compound-close <video-context>`

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Brad Bonanno — The Compound Cliffhanger Closer** — `skills/brad-bonanno-explainer-architecture/references/prompts-v2/compound-cliffhanger-closer.md`
- **Brad Bonanno — The Matrix Moment Shot List** — `skills/brad-bonanno-explainer-architecture/references/prompts-v2/matrix-moment-shot-list.md`
- **Brad Bonanno — The Pause Test Audit** — `skills/brad-bonanno-explainer-architecture/references/prompts-v2/pause-test-audit.md`
- **Brad Bonanno — The Trust-Anchor Infographic Brief** — `skills/brad-bonanno-explainer-architecture/references/prompts-v2/trust-anchor-infographic-brief.md`

<!-- END:execution-prompts -->
