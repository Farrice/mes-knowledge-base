---
name: paddy-galloway-youtube-strategy
description: "Use when a YouTube idea needs audience fit, stronger packaging, a promise-first intro, or an evidence-based performance diagnosis; also for explicit transfer of these methods into original short-form content."
version: "1.1"
format: completion-engine
expert: Paddy Galloway
domain: YouTube strategy, CCN audience, idea selection, thumbnails, titles, retention, creative analysis, outlier research
when_to_use: "Before filming; choosing an idea; briefing thumbnails; rewriting an intro; diagnosing views; adapting references without copying."
workflows: 14
primary_workflow: pg-creative-sprint
---
# Paddy Galloway — YouTube Strategy

One expert system, fourteen focused workflows. Load one workflow at a time, or use `/pg-creative-sprint` to connect them. Start with [genius.md](genius.md). Full source: `extractions/paddy-galloway/youtube-masterclass/`.

## Direct access to Paddy

Start with `/paddy-galloway` (Codex skill: `$paddy-galloway`), or say
“Paddy, help me with [the content decision].” Read `agents/paddy-galloway/AGENT.md`
for the named expert's entry behavior. If a task is supplied, execute the matching
workflow immediately; a full creative project uses `pg-creative-sprint`.

Each `pg-*` workflow below also has its own Codex skill entry and Claude command.
These are direct doors into the same source-grounded intelligence, not separate
copies of the methods. [Plain-language menu](references/direct-access.md).
For a teaching request, explain the matching source pattern, example, decision
rule, exception and one application exercise. Other experts are optional support;
Paddy's own methods can be used independently. No new Gemini call is needed to use
the already extracted knowledge.

## When NOT to Use
- Nutrition, legal or financial factual advice: route to the appropriate domain owner; this skill supplies communication structure only.
- Actual video perception: use `youtube-video-context-analysis`; a prose skill cannot inspect an unseen video.
- Ready-to-publish metadata only: use the existing `mkt-youtube-content-package` route after the strategic package is locked.
- Claims of proven virality, automatic scraping, posting or paid execution: this source supplies hypotheses and workflows, not permission or guaranteed outcomes.

## Tier 1 — Foundation

| Workflow | Produces | Command |
|---|---|---|
| [Channel Diagnosis](workflows/pg-channel-diagnosis.md) | One diagnosis with goal | `/pg-channel-diagnosis` |
| [CCN Audience and Slate](workflows/pg-ccn-slate.md) | A slate table with CCN reasons | `/pg-ccn-slate` |
| [Outlier Reference Analysis](workflows/pg-reference-analysis.md) | A reference dossier with baseline math or missing-data flag | `/pg-reference-analysis` |
| [100 to 10 to 1 Idea Funnel](workflows/pg-idea-funnel.md) | Raw idea pool | `/pg-idea-funnel` |

## Tier 2 — Practitioner

| Workflow | Produces | Command |
|---|---|---|
| [Title Lab](workflows/pg-title-lab.md) | Ten titles | `/pg-title-lab` |
| [Thumbnail Concept Briefs](workflows/pg-thumbnail-concepts.md) | Three visual briefs with composition | `/pg-thumbnail-concepts` |
| [Packaging Capture Plan](workflows/pg-packaging-capture.md) | A shoot-ready thumbnail capture checklist and design handoff | `/pg-packaging-capture` |
| [Promise-First Intro](workflows/pg-intro-rewrite.md) | One finished intro with visual cues | `/pg-intro-rewrite` |
| [Audience-Relevant Stakes](workflows/pg-stakes-design.md) | Three stakes candidates | `/pg-stakes-design` |
| [Launch Expectations and Test Plan](workflows/pg-launch-experiment.md) | A pre-publish forecast | `/pg-launch-experiment` |
| [Retention Diagnosis](workflows/pg-retention-diagnosis.md) | A timestamped diagnostic table | `/pg-retention-diagnosis` |

## Tier 3 — Stacking

| Workflow | Produces | Command |
|---|---|---|
| [Long-Form to Short-Form Transfer](workflows/pg-platform-transfer.md) | One original short-form script | `/pg-platform-transfer` |
| [Connected Creative Strategy Sprint](workflows/pg-creative-sprint.md) | A production packet with decision chain | `/pg-creative-sprint` |
| [Content Analyst Learning Bank](workflows/pg-learning-bank.md) | A searchable reference ledger and a small next-job retrieval packet | `/pg-learning-bank` |

## Stacking Guide
Briar supplies evidence-qualified outlier/transfer inputs; Paddy makes audience and package decisions; Kallaway/Jenny owns platform-native short-form craft when selected; the existing visual owner renders assets; voice and factual-domain owners retain authority. See [cross-domain boundaries](references/cross-domain-patterns.md).

## Proof and Cost Boundary
Source coverage is one full 02:45:08 interview. Source-derived methods and original applied exercises are distinct. No expert endorsement, held-out human blind pass, published test or measured growth is claimed. This skill never calls Gemini automatically. The separate $10 video trial is fixed to this source/job; it creates no recurring allowance.

## Quick Reference
[Patterns](references/genius-patterns.md) · [Hidden knowledge](references/hidden-knowledge.md) · [Claim ledger](references/source-quotes.md) · [Source ledger](references/source-ledger.md) · [Full sprint](workflows/pg-creative-sprint.md)

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

14 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Paddy Galloway — CCN Audience and Slate** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-ccn-slate.md`
- **Paddy Galloway — Channel Diagnosis** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-channel-diagnosis.md`
- **Paddy Galloway — Connected Creative Strategy Sprint** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-creative-sprint.md`
- **Paddy Galloway — 100 to 10 to 1 Idea Funnel** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-idea-funnel.md`
- **Paddy Galloway — Promise-First Intro** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-intro-rewrite.md`
- **Paddy Galloway — Launch Expectations and Test Plan** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-launch-experiment.md`
- **Paddy Galloway — Content Analyst Learning Bank** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-learning-bank.md`
- **Paddy Galloway — Packaging Capture Plan** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-packaging-capture.md`
- **Paddy Galloway — Long-Form to Short-Form Transfer** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-platform-transfer.md`
- **Paddy Galloway — Outlier Reference Analysis** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-reference-analysis.md`
- **Paddy Galloway — Retention Diagnosis** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-retention-diagnosis.md`
- **Paddy Galloway — Audience-Relevant Stakes** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-stakes-design.md`
- **Paddy Galloway — Thumbnail Concept Briefs** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-thumbnail-concepts.md`
- **Paddy Galloway — Title Lab** — `skills/paddy-galloway-youtube-strategy/references/prompts-v2/pg-title-lab.md`

<!-- END:execution-prompts -->
