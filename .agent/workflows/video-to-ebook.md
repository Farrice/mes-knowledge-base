---
description: "/video-to-ebook — YouTube video → fact-checked magazine-style article → PDF for a named brand: BRAND LOCK → Scrapes 00-youtube-to-ebook (transcript, mkt-longform-article, tool-fact-checker, human review, humanizer, PDF) with OUR claim audit as the veto and prose classifier as the gate before the PDF."
---
<!-- thin front door for the vendored Scrapes Skill Systems (2026-09-02). Machinery = .claude/skills/00-youtube-to-ebook. Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md -->

# /video-to-ebook — long-form from a video, with a real veto

State the scale in one line: one video, one article (~N words), PDF.

## Steps
1. **BRAND LOCK** — `python3 execution/scrapes_brand.py resolve --from-prompt "<ask>" --cwd "$PWD"`; exit 3 → ask. Voice for the article = the locked brand's `voice-profile.md` (their `tool-humanizer deep` reads it) — pass `brand_context_path`. Output under BRAND.yaml `output_base`/00-youtube-to-ebook/.
2. **Scrapes machinery** — invoke `00-youtube-to-ebook` with the URL. Let its Step 4 `tool-fact-checker` run (their pass), and honor its Step 5 human review: that review is Farrice's; leave the run there if he is absent.
3. **Our veto** — before Step 6 (humanize) and again before Step 7 (PDF): `python3 execution/claim_audit.py check <article.md> --strict`. Every claim tagged; UNCONFIRMED density ≤30%; a real person's quote or title without a source is cut, not softened.
4. **Our gate** — `python3 execution/prose_classifier.py check <final-article.md>` after their humanizer. FLAGGED never renders.
5. **Compound** — learnings entry under `## 00-youtube-to-ebook`; `chain_runner.py finalize --skill vendor:00-youtube-to-ebook --workflow video-to-ebook --type Content --factual N`; handoff on `<brand>-longform`.

## Never
Ship their fact-check as the veto. Skip the human review. Edit inside `.claude/skills/*`.
