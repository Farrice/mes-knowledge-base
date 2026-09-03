---
thread: scrapes-integration
status: ready
resume_hint: Blind bar 01 built at $0; his taps: approve 8 templates (:59172), verdict on JUDGING-SURFACE.html 1/2/3, named vs composite, handwriting signature
branch: worktree-scrapes-routing
pin: false
---

# Handoff · scrapes-integration · 2026-09-03 · status: draft (his taps pending)

## Shipped this sitting ($0 in images, $0.50 research)
- Blind bar 01: three 7-slide supplement-teardown carousels on the editorial pool, Farrice's brand.
  - A · AG1 named · our pens → Scrapes ssc-designer → ssc-image-generator (Scenario A) → `projects/00-social-content/2026-09-03/blind-bar-01-take-a-ag1/`
  - B · AG1 named · our pens → direct `render_template.py` → `.../blind-bar-01-take-b-ag1/`
  - C · unnamed greens composite · Scrapes path → `.../blind-bar-01-take-c-greens/`
  - Copy + ledger: `_active/farrice-brand/content/blind-bar-01/` (takes A/B/C, claims ledger, JUDGING-SURFACE.html, JUDGING-KEY.json)
  - Research brief in their cache: `projects/str-trending-research/2026-09-03/farrice--ag1-greens-creative-strategy.md`
- Machine floor: claim_audit --strict PASS ×3, prose_classifier CLEAN ×3 (captions). Evidence = real captures (Meta Ad Library AG1 page ~410 active ads, Huel page, classaction.org Hoke v. AG1).
- Learnings written: `context/learnings.md` (00-social-content, viz-image-gen); `social-carousel.md` door carries the `--data` file rule + slot ergonomics.

## His taps, in order
1. Template Studio :59172 — Approve the 8 editorial templates (status ready → approved).
2. JUDGING-SURFACE.html — verdict on 1/2/3 (which clears the bar, which is the exemplar, one change each). Key in JUDGING-KEY.json.
3. Named brand (AG1) vs anonymized composite for publishing. Sends stay human.
4. Real handwriting signature → `brand_context/visual-identity/logos/`, replacing Snell Roundhand.

## Named gap (blind bar, 1 round)
Composition/typography sit next to his frames without a seam. Photo zones carry evidence screenshots, not product photography: AG1's site is bot-blocked, stock and AI were refused. His call whether receipts-as-photos is the editorial move or a floor defect.

## Harness notes
- chain_runner finalize flagged a routing "violation": the word "Scrapes" in the description trips `scrapes_umbrella` even when the chosen door is `social-carousel`. Nudge only; the umbrella signal is too broad for notes text.
- ssc-designer HTML-escapes `<br>` in its YAML; unescape before render. Its story-framework audit is style-noise for the editorial pool.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-09-02-scrapes-integration.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
