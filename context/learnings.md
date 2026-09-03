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
- 2026-09-02 · jen · still-renting v1 · hook written from the Scrapes first-slide formulas alone read 6/10; v2 with Alyssa placement + Luke grip is the take to judge. Formulas = shape check, not the pen · verdict: v2 pending Farrice

## str-trending-research
- 2026-09-02 · all · replaced by `execution/research.py` (receipts, budgets). Our brief is written into `projects/str-trending-research/{date}/{brand}--{slug}.md` in their brief-template shape so the pipeline's cache check finds it · verdict: standing

## tool-humanizer
- 2026-09-02 · all · may run first in `deep` mode against the brand's voice-profile.md; `prose_classifier.py check` remains the gate. Blind bar #2 pending · verdict: pending

## tool-fact-checker
- 2026-09-02 · all · optional second pass; `claim_audit.py check --strict` is the veto · verdict: standing

## viz-image-gen
- 2026-09-02 · all · every AI slide prompt passes the craft-map master (nano-banana / gpt-image-2 director) before generation; `openai_budget_guard.py check` before every GPT Image call; $15/mo cap · verdict: standing

## mkt-content-repurposing
## 00-slides
## 00-longform-to-shortform
## 00-youtube-to-ebook
