# Attention Hijack Hook System

## Purpose

Use this primitive when a draft, source, trend, brand move, news item, named person, or market signal needs to become a stronger hook and then flow into end-to-end content production.

The goal is not to copy an attention source. The goal is to borrow existing attention, extract the useful tension, package it above the platform fold, and carry the reader into a real payload.

## Source Evidence

Primary source package:

- `extractions/video-context/Zc4E_K48v48/`
- Video: "I Studied 131 Viral LinkedIn Hooks, These 5 Will Make You Go Viral"
- Uploader: Diandra Escobar
- Evidence type: transcript-backed spoken evidence; no frame or OCR evidence in the current package

Key source-backed claims to preserve:

- Diandra studied 131 hooks from 21 creators and found five hook formats.
- LinkedIn judges the first 40 to 50 words before distribution.
- Hooks serve both the human reader and the platform model.
- Hook advice based only on character count is weak because mobile rendering depends on pixel width.
- Dense hooks fill roughly three mobile lines when the context needs to land before the click.
- Punchy plus context has the highest hit rate in her analysis.
- Single-line bombs are high variance and need blank lines to preserve the above-fold effect.
- Stacked hooks use repetition, contrast, and rhythm; random lines break the structure.
- The curiosity gap is the engine; format is only packaging.
- The best AI hook tool still needs creator judgment, audience knowledge, and full draft context.

## Operating Definition

Attention hijacking means redirecting attention from an already-recognized signal into your own argument.

Valid signal anchors:

| Anchor | Use When | Risk |
|---|---|---|
| Brandjack | A recognizable brand, product, campaign, or decision carries audience gravity | Summary trap or lazy brand name drop |
| Newsjack | Timely market, platform, industry, or company news has not saturated the target channel | Reporting instead of interpretation |
| Namejack | A public person, quote, move, or POV attracts the target audience | Parasitic commentary or weak audience fit |
| Trendjack | A repeated market behavior or meme is visible across sources | Trend chasing without a point of view |
| Claimjack | A common belief or consensus can be reversed with substance | Forced controversy |
| Draftjack | A strong body paragraph can be moved to the top as the hook | Manufactured hook disconnected from payload |

## Universal Hook Mechanics

Every output must define:

| Mechanic | Question | Output |
|---|---|---|
| Signal | What already has attention? | Entity, event, trend, belief, number, quote, or draft insight |
| Audience | Who already cares? | ICP or reader state |
| Payload | What expertise are we steering toward? | Argument, lesson, proof, offer, or story |
| Gap | What does the reader expect, and what will we claim instead? | Curiosity gap sentence |
| Format | Which packaging pattern carries the gap above the fold? | Dense, Punchy plus Context, Single-Line Bomb, Stacked, or Hybrid |
| Fit | Does it survive the platform fold? | Width, line break, first-50, or first-screen check |
| Judgment | What should a human keep, cut, or rewrite? | Selected hook and rejected-hook notes |

## Format Selection

| Format | Use When | Must Prove |
|---|---|---|
| Dense | Context is needed for the hook to make sense | One continuous block, high tension, no wasted setup |
| Punchy plus Context | A hard claim needs one support line to earn the click | First line provokes; second line creates or deepens the gap |
| Single-Line Bomb | One line is strong enough to stand alone | It is worth spending all above-fold real estate on one sentence |
| Stacked | A series, contrast, before/after, regrets, doubts, or escalation creates rhythm | Every line belongs to the same pattern |
| Hybrid | The creator has mastered the four core formats and needs a custom surface | It thinks in tension, not template novelty |

## System Placement

This primitive is a companion OS layer, not a replacement for existing content systems.

- `/attention-hijack-hooks` owns universal hook extraction, attention-anchor scanning, format selection, platform fit, and rehooking.
- `/farrice-content-os` owns full Farrice content production and should call this primitive during Hook Room.
- `/diandra-linkedin-system` owns the whole LinkedIn operating plan and should call this primitive when hook writing or rehooking is the bottleneck.
- `/publishable-copy-gate`, `/anti-slop-audit`, and `/high-taste-writing-os` remain final public-copy gates.
- `/plugin-readiness-audit` owns plugin packaging decisions; this primitive is not itself proof that a plugin should be built.

## Validation

Minimum local proof for a deployment:

```bash
python3 execution/attention_hijack_hooks.py --hook "Most LinkedIn hooks fail because creators count characters, but the real cutoff is pixel width. That tiny mistake kills both reader curiosity and algorithmic reach." --platform linkedin --terms "LinkedIn,algorithm,pixel"
python3 execution/verify_attention_hijack_hooks.py
python3 execution/command_menu.py search "brand tracking newsjacking hook hijack universal content"
python3 execution/workflow_router.py search "rehook draft Diandra hook formats attention hijack"
```

## Quality Bar

Reject the run if:

- The output only summarizes a brand, news item, or trend.
- The hook does not open a real gap.
- The format is chosen before the payload is understood.
- The first 40 to 50 words waste attention on throat clearing.
- The system claims visual proof from the video without frame or OCR evidence.
- The workflow jumps to publishing, scraping, posting, or external action without approval.
- The result depends on hidden chat context rather than local source paths, route names, and validation commands.
