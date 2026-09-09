---
description: "/deck-build — Slide deck from a topic, outline, or transcript for a named brand: BRAND LOCK → Scrapes 00-slides (research → outline approval → viz-frontend-slides on the brand's tokens.json → PDF) with our claim audit as the veto on the outline. Readouts and research briefs stay on /briefs."
---
<!-- thin front door for the vendored Scrapes Skill Systems (2026-09-02). Machinery = .claude/skills/00-slides + viz-frontend-slides. Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md -->

# /deck-build — a rendered deck, on the brand's tokens

State the scale in one line: one deck, ~N slides, one brand, PDF yes/no.

## Steps
1. **BRAND LOCK** — `python3 execution/scrapes_brand.py resolve --from-prompt "<ask>" --cwd "$PWD"`; exit 3 → ask which brand. Then `check <brand>` for `tokens.json` (00-slides renders on it). Not a readout or research brief — those go to `/briefs` (Ink + Steel Blue readout OS); if the ask is one, say so and hand off.
2. **Research seam** — when 00-slides would call `str-trending-research`, run `python3 execution/research.py run "<topic>" --depth standard` instead and write the brief into `projects/str-trending-research/<date>/<brand>--<slug>.md` (their cache shape) so the skill picks it up.
3. **Scrapes machinery** — invoke `00-slides` with the input and `brand_context_path` from BRAND.yaml. Its Phase 4 outline approval is Farrice's. Before he sees it, run `python3 execution/claim_audit.py check <outline.md> --strict`; tag every fact on the slides (VERIFIED / LIKELY / UNCONFIRMED). UNCONFIRMED claims never render as facts.
4. **Classifier** — `python3 execution/prose_classifier.py check <outline.md>` on the speaker-facing text.
5. **Compound** — append under `## 00-slides` in `context/learnings.md`; `chain_runner.py finalize --skill vendor:00-slides --workflow deck-build`; handoff on `<brand>-decks`.

## Never
Render a readout as a deck. Regenerate a brand's positioning inside a deck. Edit inside `.claude/skills/*`.
