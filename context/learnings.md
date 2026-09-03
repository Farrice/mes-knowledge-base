# Learnings (Scrapes Skill Systems self-improvement hook — LIVING)

> Every Scrapes skill except `00-social-content` reads and writes this file at
> `{decoupled_base}/context/learnings.md` (contract: `.claude/skills/meta-skill-creator/SKILL.md`
> "Self-improvement"). Until 2026-09-02 the file did not exist, so the hook was
> declared but dead. Our front-door workflows (`/social-carousel`, `/social-post`,
> `/social-repurpose`, `/deck-build`, `/video-to-shorts`, `/video-to-ebook`) append
> one entry per run under their skill's heading, and READ the last three entries
> before starting, so run N+1 begins where run N ended.
>
> Entry shape (one line, newest last): `- YYYY-MM-DD · <brand> · <slug> · <what to keep / what to change> · verdict: <Farrice's felt verdict or pending>`
> Brand-specific taste lives with the brand (calibration-log.md, voice-profile.md); this file holds
> pipeline lessons that transfer across brands.

# General
- 2026-09-02 · all · wiring · Scrapes pipelines own machinery; copy seams are ours (PRECEDENCE-MAP.md "Craft-room routing"). Scenario A ("finished text, just the images") is the supported hand-off point · verdict: ratified by Farrice
- 2026-09-02 · all · brand lock · every run resolves the brand through `execution/scrapes_brand.py` first and echoes the BRAND LOCK line into pipeline-log.md; ambiguity asks, never guesses · verdict: ratified by Farrice

## 00-social-content
- 2026-09-03 · farrice · editorial style (8 templates) · reference-led build worked cleanly: author the 4:5 frames as HTML first (`compositions/editorial/frames/`), render to `visual_refs/editorial/`, then one builder per frame. Builders found the source HTML and ported 1:1 (Check D 0% delta), all `solid-css`/`a-framed-image`, $0. They honored moves #8/#9 and refused AI in evidence/portrait zones on their own. Gate false positives recur on tight editorial grids (Check B raster-fill, ring-probe overflow) and are now a known class, not a defect. Photo slots are real-upload (`PHOTO_MAIN_PATH`); a preview with a placeholder is re-rendered with `--data` · verdict: frames approved with notes by Farrice; templates await his Studio Approve
- 2026-09-03 · farrice · template pool linkedin-carousel · 4 refs (Premium Minimal frames) → 4 templates, all `solid-css` pure HTML, $0 GPT Image. Builders fought Check D's absolute 8.0cqw display floor (the brand's restrained h1 is ~6.7cqw): headlines scaled up 40–60% vs refs; `compare_render_to_ref.py` ring probe throws false OVERFLOW on tight typographic layouts; Check B keyword heuristic trips on negated prose ("no AI image"). Keep: pure-HTML route for typographic brands. Change: expect the display-floor escalation and judge it by eye in the Studio · verdict: Farrice 2026-09-03 "typography, spacing, hierarchy done poorly on some" → craft pass back to the refs' 72px h1 and ref positions (pool REVIEW-NOTES.md). For typographic brands: treat the builder's Check D floor as a known distortion and plan the post-build craft pass as a standard step
- 2026-09-02 · jen · still-renting v1 · hook written from the Scrapes first-slide formulas alone read 6/10; v2 with Alyssa placement + Luke grip is the take to judge. Formulas = shape check, not the pen · verdict: v2 pending Farrice

## str-trending-research
- 2026-09-02 · all · replaced by `execution/research.py` (receipts, budgets). Our brief is written into `projects/str-trending-research/{date}/{brand}--{slug}.md` in their brief-template shape so the pipeline's cache check finds it · verdict: standing

## tool-humanizer
- 2026-09-02 · all · may run first in `deep` mode against the brand's voice-profile.md; `prose_classifier.py check` remains the gate. Blind bar #2 pending · verdict: pending

## tool-fact-checker
- 2026-09-02 · all · optional second pass; `claim_audit.py check --strict` is the veto · verdict: standing

## viz-image-gen
- 2026-09-03 · farrice · render_template.py autosize · the fit test requires the text's SINGLE-LINE width ≤ box, so a headline that wraps naturally is shrunk toward its floor (72→37px seen). Pass headlines with explicit `<br>` per line; `--no-autosize` exists for our own renders · verdict: standing
- 2026-09-02 · all · every AI slide prompt passes the craft-map master (nano-banana / gpt-image-2 director) before generation; `openai_budget_guard.py check` before every GPT Image call; $15/mo cap · verdict: standing

## mkt-content-repurposing
## 00-slides
## 00-longform-to-shortform
## 00-youtube-to-ebook
