---
name: "Meg Heckman Buyer-Trigger OS"
description: "Apparel buyer psychology. Print-on-demand trigger audits. Identity-led product design. Cross-vertical purchase intent."
version: "1.1"
format: "completion-engine"
expert: "Meg Heckman"
aliases: "Meg Hackman"
domain: "print-on-demand, apparel buyer psychology, product design, purchase intent, identity-led creative, social currency"
source: "Meg Heckman, I Made $1.19M in 30 Days. Here’s What ACTUALLY Made People Buy, YouTube, 2026-06-07"
workflows: 5
---

# Meg Heckman Buyer-Trigger OS

This cold skill turns Meg Heckman's print-on-demand buyer psychology video into a reusable operating system for apparel, POD products, client creative, offer surfaces, landing pages, and identity-led product design. It can now run a research-backed lane that gathers current public evidence before applying the Meg model.

Use the source-canonical spelling `Meg Heckman`; preserve `Meg Hackman` as an alias because the user introduced that spelling.

## Source Grounding

- Source package: `extractions/video-context/7MNa2YTPGs4/`
- Primary ledger: `extractions/video-context/7MNa2YTPGs4/video-context-ledger.md`
- Clean transcript: `extractions/video-context/7MNa2YTPGs4/transcript.txt`
- Timestamped transcript segments: `extractions/video-context/7MNa2YTPGs4/transcript_segments.json`
- Metadata: `extractions/video-context/7MNa2YTPGs4/metadata.json`
- Uncertainty: `extractions/video-context/7MNa2YTPGs4/uncertainty-report.md`
- Visual limit: frames were sampled, but automated OCR was unavailable. Do not make visual claims unless a frame is reviewed by a human or vision adapter.
- Claim boundary: Meg's revenue and margin numbers are source claims from the video, not independently verified proof.

## Source-Trace Default

Every meaningful use of this OS must be source-traced. Do not generate from vibes, memory, or a rigid template.

Before output:

1. Load `references/source-ledger.md`.
2. Load `references/genius-patterns.md`.
3. Load only the workflow needed for the requested mode.
4. Name the source timestamp anchors used from the source ledger or video-context ledger.
5. Separate `Source Mechanics` from `Domain Extrapolation`.
6. Mark visual/OCR evidence unavailable unless reviewed evidence exists.
7. Mark revenue/margin numbers as source claims only.

## Research-Trace Default

Use this default when the user asks for current buyer insights, trends, live buyer language, social listening, purchase intent research, market evidence, competitor signals, or passes `--research`.

Research-backed runs must:

1. Keep Meg source mechanics separate from live market evidence.
2. Run or consume `execution/buyer_trigger_research.py` before producing a meaningful recommendation.
3. Use the public/free native research floor by default.
4. Never use `execution/research_router.py --provider auto` as the default buyer-trigger lane because it can trigger paid providers.
5. Include public social listening by default through URL-backed public sources.
6. Treat Apify as preview-only unless explicitly enabled with `--apify execute` or a clear user instruction to use Apify.
7. Preserve Apify budget guard output, estimated cost, monthly state, per-run cap, execution/fallback status, and item count in the receipt.
8. Refuse to fabricate current trends, quotes, buyer language, competitor facts, pricing, or marketplace claims.
9. If evidence is thin, mark the run `DEGRADED` and label outputs as research-informed hypotheses.
10. If evidence fails, mark the run `FAILED` and output only evidence gaps, source needs, and next gates.

The research package is the handoff object:

- `buyer_trigger_research_report.md`
- `source_ledger.md`
- `insight_ledger.md`
- `evidence.json`
- `buyer_trigger_research_report.metadata.json`

Every downstream mode must cite evidence IDs or source URLs for current-world claims.

Use this compact source-anchor set unless a task needs deeper citation:

| Mechanic | Source Anchor |
|---|---|
| Buyer psychology over hacks | 00:00-00:41 |
| Identity beats utility | 00:41-01:20 |
| Recognition creates emotion | 01:23-02:18 |
| Specificity beats broad appeal | 02:20-04:07 |
| Social currency | 04:16-05:50 |
| Familiar plus unexpected | 05:55-07:58 |
| Emotion before logic | 08:00-09:16 |

## Core Rule

Do not evaluate a product by asking only whether it is pretty, clever, or original. Evaluate whether the right buyer instantly recognizes themselves, imagines a social moment, feels something first, and only then justifies the purchase.

## Six Buyer Triggers

| Trigger | Operating Question | Failure Mode |
|---|---|---|
| Identity Signal | What does this let the buyer say about themselves? | The product is attractive but not self-expressive. |
| Instant Recognition | Does the right person get it before the scroll moment is gone? | The joke or value takes too much decoding. |
| Specific Person | Does it paint a person, not just name a market? | It targets a broad category and feels bland. |
| Social Currency | What reaction does the buyer imagine getting? | It sits on a page instead of moving through people. |
| Familiar Twist | Is it familiar enough to understand and unexpected enough to care? | It is boring, or it is too strange to decode. |
| Emotion First | What feeling arrives before the buyer gives themselves a reason? | The sale depends on price, specs, or utility alone. |

## Trigger Fit Table

Use this shape as the default output:

| Candidate | Target Buyer | Identity Signal | Recognition Speed | Specificity | Social Currency Moment | Familiar/Twist Pair | Emotion-First Reason | Risk | Revision |
|---|---|---|---|---|---|---|---|---|---|

## Available Workflows

| Workflow | Produces | Use When |
|---|---|---|
| [Research-Backed Trigger Run](workflows/research-backed-trigger-run.md) | Trigger Research Trace, Research Receipt, Source Ledger, Insight Ledger, source-backed Trigger Fit Table | Researching current buyer insights, trends, public social listening, purchase intent, or market evidence before using the OS. |
| [Buyer Trigger Audit](workflows/buyer-trigger-audit.md) | Trigger Fit Table, weak-link diagnosis, priority revisions | Auditing existing apparel, offers, pages, product ideas, ads, or creative concepts. |
| [Apparel Concept Generator](workflows/apparel-concept-generator.md) | Identity-led shirt/product concepts with proof notes and print constraints | Creating T-shirt, hoodie, mug, poster, merch, or POD concepts from a niche. |
| [Product Design Scoring](workflows/product-design-scoring.md) | Scorecard and pass/revise/kill verdict | Choosing which product/design concepts deserve testing. |
| [Cross-Vertical Transfer](workflows/cross-vertical-transfer.md) | Adaptation map for offers, landing pages, client work, content, and non-apparel products | Applying the trigger model beyond apparel without losing the original mechanics. |

## Cold-Start Routing Phrases

Route here for `buyer-trigger-os`, `Meg Heckman buyer psychology`, `apparel buyer psychology`, `print on demand trigger audit`, `POD buyer triggers`, `T-shirt purchase intent`, `shirt design psychology`, `EDM streetwear purchase intent`, `identity-led product design`, `social currency product design`, `product purchase intent`, `offer purchase intent`, `landing page purchase psychology`, `cross-vertical purchase intent`, `current buyer insights`, `purchase intent research`, `trend-backed shirt ideas`, `social listening product design`, `research-backed trigger audit`, and `find buyer trends`.

## Proof Examples, Not Templates

Josh and MyBPM are proof lanes from the original deployment request. They are not default templates and must not narrow generic use.

- Load `_active/josh-swing-nerd-shirts-v1/MEG_HECKMAN_TRIGGER_PASS.md` only when the query explicitly mentions Josh, swing-nerd shirts, or asks for Josh examples.
- Load `deliverables/designs/20260414_181005_mybpm_edm_streetwear_tee_with_prompt.json` and the MyBPM proof section in `extractions/video-context/7MNa2YTPGs4/meg-heckman-buyer-trigger-os-harvest.md` only when the query explicitly mentions MyBPM, EDM streetwear, or asks for MyBPM examples.
- For generic apparel, POD, offer, product, landing-page, or client work, start from the user's actual buyer, product, and use context.

## Load Order

1. `references/source-ledger.md`
2. `references/genius-patterns.md`
3. `workflows/research-backed-trigger-run.md` when current evidence, trends, social listening, or `--research` is requested
4. The one workflow needed for the task
5. Relevant proof example only when explicitly requested
6. `semantic_libraries/antigravity/primitives/buyer-trigger-design-psychology.md` for cross-vertical use
7. `references/quality-rubric.md` before client-facing, revenue-critical, or publishable output

## Stacking Guide

- Pair with `creative-direction` when the output needs streetwear/art direction, placement, typography, or image prompts.
- Pair with `kallaway-content-psychology` when the product needs hook testing, attention architecture, or buyer-content packaging.
- Pair with `kallaway-audience-obsession` when the product must move from signal to belief to action through indirect suggestion.
- Pair with `rafa-conde-memorable-product-design` when a non-apparel product needs emotional residue and remembered moments.
- Pair with `/source-to-skill-system` when new source material should become a durable skill system.
- Pair with `/extraction-governor-agent` when deciding whether new material is a skill, reference, workflow, or productized asset.

## Boundaries

- This skill remains the deep cold OS. `/buyer-trigger-os` is the approved workspace-local hot launcher and must load this full skill rather than duplicating it.
- Do not create additional hot slash commands, global mirrors, or external deployment surfaces without explicit approval.
- Do not claim Meg's business outcomes as independently verified.
- Do not use visual evidence from the video unless frames or OCR have actually been reviewed.
- Do not present current buyer insights, trends, social-listening claims, competitor claims, or marketplace claims without source URLs from a research package.
- Do not let Apify, Gemini, Perplexity, browser automation, authenticated scraping, or other paid/quota tools run silently; require the relevant preview, budget guard, and approval boundary.
- Do not create designs that rely on protected logos, lyrics, team names, event names, existing shirt designs, or copied meme layouts.
- Real Codex subagents, external publishing, connector writes, paid tools, and global mirrors require explicit approval.
