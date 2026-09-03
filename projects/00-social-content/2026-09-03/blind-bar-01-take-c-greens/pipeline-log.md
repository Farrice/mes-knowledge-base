# pipeline-log · blind-bar-01-take-c-greens · 2026-09-03

BRAND LOCK: farrice (Farrice Cain, owner) — brand_context=/Users/farricecain/Google Antigravity/.claude/worktrees/scrapes-routing/brand_context output_base=projects/00-social-content pens=luke-iha-vicious-hooks+farrice-voice-card-blend veto=farrice-as-himself voice_dial=BLEND

Scenario A: finished text, just the images. Copy source: _active/farrice-brand/content/blind-bar-01/2026-09-03-take-C-greens-composite.md (claim audit PASS strict, classifier CLEAN). Style: editorial. Pool: brand_context/templates/linkedin-carousel. Cost so far: research $0.50 (shared across takes), templates $0, AI slides 0.


## Phase 5.0.5 — VISUAL INVENTORY [done] — ssc-designer (Scenario A)
- Logos: 0 · Photos: 0 · Screenshots: 0 · User assets: 9 (huel-greens evidence crops, tier 5) · Video frames: 0
- Scope: only `evidence/huel-greens/` globbed for candidates — that is the source the locked slide script references. `evidence/ag1-adlibrary*`, `evidence/ag1-classaction/`, `evidence/im8-vs-ag1/` exist on disk but belong to sibling blind-bar takes, out of scope for this composite.
- Used in slide_plan: crop-numbers.png (n2), crop-scoop.png (n3, n5), crop-bubbles.png (n4, n5), crop-subscribe.png (n6)
- Unused (present but not called by script): crop-bottle.png, crop-claim.png, crop-column.png, crop-hero.png, screenshot.png (uncropped source, brand visible — correctly excluded)
- Elapsed: ~15s (glob + read only, no search/fetch — all sources pre-resolved by the script)

## Phase 5.3 — SLIDE PLAN [done] — ssc-designer (Scenario A, copy LOCKED)
- Arc (as observed in the finished copy, lead_gen shape): category sameness (pain) → shared-claim pattern → why the count claim is dead/wallpaper (cost of inaction) → three-angle framework (solution teaser) → format churn without argument change (reinforcement) → the miss: subscription-first skips the ritual argument (proof) → DM ANGLE (CTA)
- 7 slides, template_pool=linkedin-carousel, all template_id values verbatim from the script, all copy verbatim (headlines keep literal `<br>`)
- No rewrites performed anywhere — Hard Rule 1 (copy/template_id final)

| # | Role | template_id | Render mode | Visual weight | Source tier |
|---|------|-------------|-------------|----------------|-------------|
| 1 | hook | signature-cover | TEMPLATE | template | — (typographic, brand-locked cover) |
| 2 | context | word-photo-band-body | HYBRID_REAL | anchor | 5 (crop-numbers.png) |
| 3 | build | photo-right-columns-body | HYBRID_REAL | supporting | 5 (crop-scoop.png) |
| 4 | build | photo-left-list-body | HYBRID_REAL | anchor | 5 (crop-bubbles.png) |
| 5 | build | two-photo-list-body | HYBRID_REAL | supporting | 5 (crop-scoop.png + crop-bubbles.png) |
| 6 | proof | evidence-crop-body | HYBRID_REAL | anchor | 5 (crop-subscribe.png) |
| 7 | cta | signature-close-cta | TEMPLATE | template | — (typographic close + signature) |

## Phase 5.3b.0 — AUDITS [done] — Scenario A deviations logged, nothing rebalanced (copy/template_id locked per Hard Rule 1)
- 7.0 Slide-1 cover check: generic rule rejects TEMPLATE-mode/no-image on slide 1. OVERRIDDEN by orchestrator Hard Rule 2 ("TEMPLATE for signature-cover"). signature-cover is this brand's own locked hook device (giant lowercase word + red script signature, full-bleed typographic) — not escalated to HYBRID_AI/HYBRID_REAL since Rule 2 forbids introducing any new image (no stock, no AI, no unlisted photo) on this run. Deviation documented, not fixed.
- 7.1 Per-slide real check: PASS — every HYBRID_REAL slide resolved to an absolute USER_ASSET path under brand_context/visual-identity/compositions/editorial/evidence/huel-greens/; no search-pending, no alternatives_rejected needed.
- 7.2 Visual floor: N=7 → floor_required=5 (ceil(14/3)). visual_slides_count=5 (n2-n6, anchor+supporting). PASS (5/5).
- 7.3 Icon-anchor: N/A — no icon assets used this run.
- 7.4 White-space: PASS — n1/n7 are dense typographic covers (masthead, giant word, footer strip, hairlines); n2-n6 all carry a real evidence photo + text.
- 7.5 Diversity: PASS — render_modes {TEMPLATE, HYBRID_REAL}, 7 distinct template_ids, no consecutive (template_id, render_mode) repeat, ≥1 pure-typographic slide (n1, n7), ≥1 real-image slide (n2-n6).
- 7.6 FULL_AI eligibility: N/A — available_providers=[] this run (HTML-only); no slide uses HYBRID_AI/FULL_AI (all locked to TEMPLATE or HYBRID_REAL already). 0 eligible, 0 downgraded.
- 7.7 Scenario F mandate: N/A — scenario is A.
- 7.9.1 Headline word cap: all headline/HEADLINE_WORD values ≤4 words — PASS, no rewrite needed (n1 "greens"=1, n2 "the same three lines"=4, n3 "the count"=2, n4 "three angles"=2, n5 "what changed"=2, n7 "dm angle"=2).
- 7.9.2 Body line cap (≤25 words, ≤4 for tension/proof exception): n2 SUBTITLE=27 words (VIOLATION, minor over on a context slide, not in the exception role list) · n3 BODY=34 words (VIOLATION) · n6 ANALYSIS_BODY≈45 words (VIOLATION, role=proof so eligible for the 4-line exception but still runs long even against that ceiling) · n4 SUBHEAD=14w PASS · n5 BODY=14w PASS. All left untouched per Hard Rule 1 — copy is final, script was pre-approved (claim audit PASS strict, classifier CLEAN per log header). Flagging for the record only.
- 7.9.3 Standalone-in-Explore: PASS all — no slide opens with a dangling reference ("and the answer is...") or depends on a sibling slide to parse.
- 7.9.4 Energy curve: target [HIGH,LOW,MED,MED,HIGH,MED,LOW] (7-slide canonical). Actual, mapped from visual_weight (anchor=HIGH, supporting=MED, template=LOW): [LOW, HIGH, MED, HIGH, MED, HIGH, LOW]. Mismatches at position 1 (template cover vs HIGH-photo expectation) and position 2 (photo band reads HIGH not LOW). Not rebalanced — both are direct consequences of the locked template_id sequence (Hard Rule 1/3), and the brand's own "editorial" style family opens on a typographic cover by design, not a photographic one. Position 6 (penultimate) hits HIGH as required; position 7 (CTA) hits LOW as required.
- 7.9.5 Build tonal alternation: N/A — every template_id in the locked "editorial" style subset (signature-cover, word-photo-band-body, photo-right-columns-body, photo-left-list-body, two-photo-list-body, evidence-crop-body, portrait-statement-cta, signature-close-cta) carries `tone: light` in the pool manifest. There is no dark-toned entry inside this style's allowed subset to alternate against — uniform light tone is an inherent property of the "editorial" style family (the dark frame belongs to the separate "typographic" style's statement-close-cta, not in scope here). Logged as N/A, not a violation.
- 7.9.6 CTA image-less: PASS — n7 signature-close-cta is TEMPLATE, image_zone none, no image_source.
- 7.9.7 Verbatim check: N/A by construction for this run — inspiration_pool passed in IS the locked slide-script table itself (Scenario A finished text), so every slide trivially "matches" its own source. This audit's purpose (catching un-humanized scrape copy) does not apply; the copy was already claim-audited and classifier-clean per the source file's own header.
- Gallery sweep (Step 7.8): N/A — render_mode set is {TEMPLATE, HYBRID_REAL} only; no ai_style assignment needed on any slide (no HYBRID_AI/FULL_AI slides this run).
- Elapsed: ~20s (all audits are read/count checks against pre-locked copy, no rewrites performed)

## Phase 7 — RENDER [done] — ssc-image-generator (Scenario A, no AI, available_providers=[])

| Slide | template_id | Render mode | Result | Notes |
|---|---|---|---|---|
| 1 | signature-cover | TEMPLATE | OK | clean render, no clamps |
| 2 | word-photo-band-body | HYBRID_REAL | OK | autosize CLAMPED at floor (SUBTITLE, SOURCE_LABEL @ 22px) — copy is locked/final, not rewritten |
| 3 | photo-right-columns-body | HYBRID_REAL | OK | autosize CLAMPED at floor (MASTHEAD, BODY, ITEM_1_TEXT, ITEM_2_TEXT, ITEM_3_TEXT @ 22px) — copy locked |
| 4 | photo-left-list-body | HYBRID_REAL | OK | autosize CLAMPED at floor (SUBHEAD, LIST_1/2/3 label+body @ 22px) — copy locked |
| 5 | two-photo-list-body | HYBRID_REAL | OK | autosize CLAMPED at floor (HEADER, BODY, ITEM_2_BODY @ 22px) — copy locked |
| 6 | evidence-crop-body | HYBRID_REAL | OK | autosize CLAMPED at floor (MASTHEAD, EVIDENCE_LABEL, ANALYSIS_BODY @ 22px) — copy locked |
| 7 | signature-close-cta | TEMPLATE | OK | autosize CLAMPED at floor (MASTHEAD @ 22px) — copy locked |

7/7 slides OK, 0 FAIL. All renders `--no-ai-bg --use-sample-text`, no AI generation invoked (available_providers=[]). Total render cost: $0.00.

Clamp notes are cosmetic autosize warnings (`needs-user-decision` tag from the renderer's autosize floor logic) surfaced for visibility only — slot copy is FINAL per orchestrator instruction and was not altered. `manifest.json` written. `CONTACT-SHEET.png` built (4x2 grid, 35% scale, white background).

## Orchestrator correction (2026-09-03)
Re-rendered slides [2, 6] with the same renderer command after shortening labels to one line and single-lining the band headline. Copy meaning unchanged; take file and slide_plan.yaml updated to match. Cost $0.
