---
name: "Mike Taylor — Synthetic Customer Research OS"
description: "Research-design depth behind synthetic customer panels: the roleplay-then-aggregate mechanism, the grounding ladder (cold-generated, social-grounded via listening gap-fill, transcript-grounded, calibrated), the distribution-vs-individual accuracy split, sycophancy/bias correction, and the research-budget triage that decides which questions synthetic panels answer and which ones still need the real $8-12K focus group. 17 genius patterns, 7 workflows across 3 tiers. Co-author, O'Reilly's Prompt Engineering for Generative AI; co-founder, Ask Rally (synthetic-audience simulator)."
version: "1.0"
format: "completion-engine"
workflows: 7
primary_workflow: workflows/mt-persona-panel-triage.md
extracted_from: "1 Marketing Against the Grain video (33:13, 6,916-word transcript, 20 frames, WATCHED) plus secondary corroboration from Vexpower/Ask Rally public material, 2026-07-19 forge"
tier: system
---

# Mike Taylor — Synthetic Customer Research OS

A direct question to a chatbot returns "the stock answer, kind of the average of the internet." Mike Taylor's fix is a two-step move: generate a panel of distinct personas, get each to answer independently, then instruct the model to combine their answers "as if these people had collaborated in writing a joint anonymous answer." That mechanism is the surface. This skill is the research-design layer underneath it: how deep to ground a panel before trusting it, when an aggregate verdict is reliable and when an individual prediction is a hallucination wearing a plausible costume, and how to triage the "hundred times more questions than you can afford to answer" between synthetic panels and the real $8-12K focus group.

> **Where this sits**: `/buyer-council` (`skills/geoff-woods-ai-thought-partner/workflows/17-buyer-council.md`) is the LIVE operational front door. Its TRIAGE mode already runs this skill's core mechanic (Patterns 1-5) in about 5 minutes with dissent-preserved verdict machinery built in. This skill goes deeper: research design, grounding theory, calibration discipline, and the multi-question research-budget triage buyer-council doesn't attempt. Load `/buyer-council` for a fast single-artifact gut-check. Load this skill when the call needs grounding-tier discipline, latent-demand discovery, or a real research-budget decision.

> **Grounding rule**: The core mechanism (persona generation, two-step prompt architecture, aggregation phrasing, the $8-12K frame) is VERIFIED, watched directly in the primary source video. The accuracy percentages, the three-tier Grounding Ladder, the self-consistency ceiling, and the sycophancy/vegan-problem findings are LIKELY, corroborated third-party attribution rather than primary-verified. Deploy the method and label the numbers per `references/source-quotes.md`.

## Available Workflows

### Tier 1: Foundation (the core mechanism)
| Command | Workflow | Produces | Use When |
|---------|----------|----------|----------|
| `/mt-persona-panel-triage` | [Persona Panel Triage](workflows/mt-persona-panel-triage.md) | Panel verdict: persona list, per-role dissent, joint anonymous answer, directional call | Any decision question needs a fast, cold-generated directional read |
| `/mt-persona-grounding` | [Persona Grounding From Transcripts](workflows/mt-persona-grounding.md) | Transcript-grounded (Tier 2) panel verdict, per-customer responses, real-ask arming — or, when no transcripts exist, a Tier 2.5 social-grounded panel via the built-in gap-fill protocol (harvests a receipted voice-of-customer corpus instead of falling to cold generation) | Real customer call transcripts exist for this audience, OR no transcripts exist but a live-market grounding is still worth more than a cold-generated panel |
| `/mt-latent-demand-mining` | [Latent Demand Mining](workflows/mt-latent-demand-mining.md) | Pain-point surface scan plus a drilled-down product-opportunity finding | Discovering an unmet need or product opportunity, not validating one |

### Tier 2: Practitioner (technique-specific)
| Command | Workflow | Produces | Use When |
|---------|----------|----------|----------|
| `/mt-concept-headline-triage` | [Concept / Headline Triage](workflows/mt-concept-headline-triage.md) | Directional preference verdict across 2-4 real copy/concept variants, attributed dissent | Real variants already exist and need a fast directional read before spend |
| `/mt-personalized-message-cascade` | [Personalized Message Cascade](workflows/mt-personalized-message-cascade.md) | Angle-discovery draft plus a human-written final for individual/segment outreach | A validated top-level message needs individual or segment-specific positioning |
| `/mt-distribution-calibration-check` | [Distribution & Calibration Check](workflows/mt-distribution-calibration-check.md) | Validity audit: grounding tier, ceiling, distribution-vs-individual, sycophancy, thread-contamination | Any panel output is about to inform a real decision above trivial stakes |

### Tier 3: Stacking (research-budget decision and cross-expert)
| Command | Workflow | Produces | Use When |
|---------|----------|----------|----------|
| `/mt-synthetic-vs-real-decision` | [Synthetic vs. Real Research Decision](workflows/mt-synthetic-vs-real-decision.md) | Question-by-question triage, research-stack tool sequencing, real-budget allocation | Multiple open questions need routing between synthetic panels and real research |

## Quick Reference
- **Genius Context**: [genius.md](genius.md). Load before any workflow (17 patterns, hidden knowledge, exemplars, decision framework, rubric, anti-patterns).
- **Source Quotes and Claims Ledger**: [references/source-quotes.md](references/source-quotes.md). Verbatim timestamped quote bank with VERIFIED/LIKELY/UNCONFIRMED labels.
- **Extraction Report**: `extractions/mike-taylor/extraction-report.md`. Source fidelity, expert identification, pattern frequency.

## Stacking Guide

- **`/buyer-council`**. TRIAGE mode is this skill's fast operational front door for a single artifact. This skill is the deep source for research design: grounding tiers, latent-demand mining, and the research-budget triage buyer-council doesn't attempt. Never duplicate the council/verdict machinery here. Escalate stakes-appropriate calls from `mt-synthetic-vs-real-decision.md` into buyer-council COUNCIL mode.
- **Geoff Woods (stakeholder simulation, anti-sycophancy)**. Taylor's Sycophancy/Bias Trap (Pattern 9) and Woods' anti-sycophancy discipline are the same failure mode named independently. Cross-pollinate the adversarial-casting instinct both ways.
- **Jeremy Haynes cold-offer stakeholder handshake**. The dissent-preservation discipline in the Haynes-Woods handshake and this skill's Distribution vs. Individual Accuracy split (Pattern 8) are the same guardrail against consensus-averaging. Useful cross-reference when a panel prompt must not smooth away real disagreement.
- **Corey McClain persona engineering**. McClain's narrative-prose persona depth is the natural Tier 2 to Tier 1 grounding upgrade path when a Taylor panel needs more depth than an 80-120 word card can carry.
- **Copy/positioning skills (Luke Iha, Georgi, Nicolas Cole)**. This skill validates and finds angles. It never replaces the craft of writing the shipped sentence. `mt-personalized-message-cascade.md`'s discipline (angle-discovery, human-written final) is the explicit handoff point.

Inverting the order, treating a synthetic panel's raw output as finished copy, or skipping grounding-tier discipline on a high-stakes call, produces confident-sounding research that is actually just a well-dressed guess.

## Deployment Targets
- **`/buyer-council` integration** (live). Buyer-council's Lineage footer points here as the deep source for TRIAGE mode's mechanics.
- **Farrice's own highest-return workflow.** This process was rated among Farrice's highest-return uses before this forge. It was nearly lost, with only a Recall card (`ce789f0b-9c63-4775-b0b7-c44edad29e23`) as its trace. This skill is the durable, deployable version of that near-lost process.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

7 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Mike Taylor — Concept / Headline Triage** — `skills/mike-taylor-synthetic-research/references/prompts-v2/concept-headline-triage.md`
- **Mike Taylor — Distribution & Calibration Check** — `skills/mike-taylor-synthetic-research/references/prompts-v2/distribution-calibration-check.md`
- **Mike Taylor — Latent Demand Mining** — `skills/mike-taylor-synthetic-research/references/prompts-v2/latent-demand-mining.md`
- **Mike Taylor — Persona Grounding From Transcripts** — `skills/mike-taylor-synthetic-research/references/prompts-v2/persona-grounding.md`
- **Mike Taylor — Persona Panel Triage** — `skills/mike-taylor-synthetic-research/references/prompts-v2/persona-panel-triage.md`
- **Mike Taylor — Personalized Message Cascade** — `skills/mike-taylor-synthetic-research/references/prompts-v2/personalized-message-cascade.md`
- **Mike Taylor — Synthetic vs. Real Research Decision** — `skills/mike-taylor-synthetic-research/references/prompts-v2/synthetic-vs-real-decision.md`

<!-- END:execution-prompts -->
