---
name: teardown-carousel-copy-lock-evidence-crops
problem_signature: "a high-taste social carousel (brand teardown, authority piece) has to come out production-usable and repeatable, not slop; earlier attempts at the same pipeline produced flat copy, AI-looking visuals, or both"
domain: content
tags: [carousel, linkedin, scrapes, blind-bar, evidence, copy-lock, editorial, farrice-brand]
date: 2026-09-03
status: active
session: scrapes-routing (blind bar 01)
---

## Problem
Farrice's own social pipeline attempts "worked a lot worse" than the reference product, and generic carousel generators rewrite the copy, invent visuals, and land in the middle. Blind bar 01 (three AG1/greens teardown carousels, 2026-09-03) came out above his expectation: take 1 "10 out of 10, or even 11 out of 10... this needs to be the floor." This card is the shape that produced it, so it repeats.

## Root Cause
Three things had been mixed in one pass before: writing the argument, verifying the facts, and planning visuals. When one model does all three, the copy drifts toward what the templates can hold, the facts soften into adjectives, and the photos become stock or AI. Separating them, and locking each before the next starts, is what made the difference.

## Approach That Worked
1. **BRAND LOCK first.** `scrapes_brand.py resolve` line opens every log and dispatch; the pool, voice canon, and output base are explicit paths. Nothing is inferred from the working directory.
2. **Research with receipts into their cache.** `research.py run --depth standard` (Gemini Deep Research, $0.50), then a brief in the Scrapes shape at `projects/str-trending-research/<date>/<brand>--<slug>.md`, every finding tagged VERIFIED / LIKELY / UNCONFIRMED. Single-source numbers stay out of copy.
3. **Real evidence captures, not stock, not AI.** `tool-web-screenshot` on the primary surfaces (Meta Ad Library filtered to the brand's page id, product pages, the court-filing page). Crop to the slot's shape (portrait crops for portrait slots, wide for band/evidence). When a site blocks bots, use the Ad Library and third-party record pages instead. The captures then upgraded the ledger: a LIKELY count from a competitive-intel blog became a VERIFIED count read off the page.
4. **Claims ledger before copy.** One table: claim as used, tag, source. Anything not on it does not ship. Copy quotes the ledger; the ledger never chases the copy.
4b. **Concept Room, his review beat (added 2026-09-03 after his note; blind bar 01 skipped it because he was asleep).** Before any copy: one page with the tagged findings and captures, three angle candidates (the fight each picks), two or three hooks for the recommended one, the photo plan, and the named-vs-composite call. He taps or edits; copy is written only after. He arrives with a concept, references, and any images he has, never with the angle or the copy. Their draft and humanizer phases stay off.
5. **Our pens write, one integrator, copy is FINAL.** Caption in the brand's voice dial (BLEND) plus a seven-slide script mapped to template ids with every slot filled. Headlines carry their `<br>` breaks. Three takes on purpose: named brand with the fight picked (A), named brand on a symptom-to-decision arc (B), anonymized composite (C). Farrice's verdict: the fight-picking named take is the floor; the composite is a 9 because "safe gets buried"; keep it for client-privacy moments.
6. **Machine floor, free.** `claim_audit.py check --strict` on the take file (operator scaffolding dates and arrows tagged or removed so the audit reads the copy), `prose_classifier.py check` on the caption alone. Both must pass before any machinery runs.
7. **Scrapes designer with copy locked.** Dispatch `ssc-designer` with the slide script as `inspiration_pool`, `allowed_template_ids` = the style's templates, `available_providers = []`, and the hard rule "headlines, bodies, template ids are FINAL; photo slots resolve to these evidence paths as USER_ASSET tier 5". It returned every slot verbatim on both runs. Unescape `&lt;br&gt;` in its YAML. Its story-framework audit (25-word caps, no typographic cover, energy curve) is noise for the editorial pool.
8. **Render with the slot rules.** `uv run --with playwright python render_template.py --template-pool … --template-id … --brand-context … --use-sample-text --no-ai-bg --data <slide-NN.data.json>`. Data as a FILE. Labels ≤ ~50 chars, one-line verdict word and band headline, short FOOTER_TOPIC, portrait vs wide crops. Direct render (take B) and the Scrapes image generator (A, C) give identical output when the plan is the same; the machinery's value is the plan discipline, not the pixels.
9. **Contact sheet read before he sees it.** Render a 4x2 sheet, read it, fix label clipping and crop cut-offs, re-render only the affected slides, log the correction in the pipeline log.
10. **Blind judging surface.** Three takes as 1/2/3 in a shuffled order with the approved frames as the bar at the bottom; the key in a sidecar file he opens after tapping. His verdicts go to `voice_ratchet.py add` verbatim.

## Dead Ends
- Openverse / stock photos for a named-brand teardown: unusable, off-subject. Real captures only.
- Inline JSON in `--data`: crashes the renderer (Errno 63) once the copy is real.
- Letting labels run long: they render uppercase letterspaced and clip on the second line.
- A two-line VERDICT_WORD or band HEADLINE: collides with the body under it.
- Scoring the composite as the safe default: "In the middle, content gets killed and buried."

## Verification
Farrice, 2026-09-03: take 1 (A) "11 out of 10... this needs to be the floor"; take 3 (B) "really hard to go between 1 and 3, I would close both"; take 2 (C) "9 out of 10... safe... not the floor". Cost: $0.50 research, $0 images. `claim_audit --strict` PASS x3, `prose_classifier` CLEAN x3. Open critiques he named (not yet applied): composition and proportion still busy on some slides, hierarchy uneven, some screenshots cut off at points that matter, and he wants an operator-only verification hub per run (claims, sources, crops in one place; never on the slides).

## Weaker-Model Trap
A mid-tier model "improves" the locked copy to satisfy the designer's word caps, swaps a real capture for a cleaner stock image, or scores the safe composite highest because it is the least risky. Tell it: copy is final, photos are receipts, and the floor is the take that picks the fight.

## Pointers
- `.agent/workflows/social-carousel.md` (the door; carries the slot rules and this run shape)
- `_active/farrice-brand/content/blind-bar-01/` (takes A/B/C, claims ledger, JUDGING-SURFACE.html, JUDGING-KEY.json)
- `projects/00-social-content/2026-09-03/blind-bar-01-*/` (slide plans, data files, renders, pipeline logs)
- `projects/str-trending-research/2026-09-03/farrice--ag1-greens-creative-strategy.md` (research brief)
- `context/learnings.md` §00-social-content, §viz-image-gen
- `brand_context/visual_refs/editorial/` (the bar), `brand_context/templates/linkedin-carousel/` (the pool)
