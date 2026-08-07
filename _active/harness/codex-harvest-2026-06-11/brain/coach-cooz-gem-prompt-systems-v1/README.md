# Coach Cooz Gemini Gem Prompt Systems V1

Purpose: A complete Gemini Custom Gem operating system for Coach Cooz so he can create content, execute LinkedIn distribution, package marketing assets, protect proof claims, and run client-service workflows without needing Farrice to rebuild the creative strategy from scratch every time.

## Why This Exists

Cooz can execute well when the steps, rationale, and quality bar are clear.

The risk is not effort.

The risk is that when creative strategy gets handed off loosely, the work turns into generic trainer content, weak packaging, vague DMs, or over-polished AI copy that does not match the premium service.

This package gives him specialized Gemini Gems with exact roles, source files, behavior rules, output formats, and quality gates.

## Gemini Fit

Google describes Gems as customized versions of Gemini for repetitive tasks or deep expertise. Google also documents that custom Gems work better with clear instructions and can use uploaded files for extra context.

Sources:

- Google Gems overview: https://support.google.com/gemini/answer/15236321?hl=en
- Custom Gem instructions and knowledge files: https://support.google.com/gemini/answer/15235603?hl=en
- Gem sharing and file visibility notes: https://support.google.com/gemini/answer/16504957?hl=en

## Files

- `GEM-SETUP-GUIDE.md` - How to create the Gems in Gemini, what to upload, and how to share safely.
- `COOZ-MASTER-BRAND-BRAIN-GEM.md` - The master guardrail Gem for positioning, voice, offer, claims, and north star.
- `COOZ-CONTENT-FLYWHEEL-GEM.md` - Voice memo or rough idea into LinkedIn, Instagram, YouTube, blog, and story prompts.
- `COOZ-LINKEDIN-DISTRIBUTION-GEM.md` - Commenting, connecting, warm DMs, referral asks, and daily LinkedIn routine.
- `COOZ-DESIGN-MARKETING-ASSET-GEM.md` - Carousels, profile assets, landing sections, simple campaign assets, and creative briefs.
- `COOZ-SERVICE-OPS-GEM.md` - Triage Audit prep, follow-up, onboarding, weekly check-ins, client notes, miss recovery, and proof capture.
- `COOZ-PROOF-CLAIMS-GEM.md` - Claim safety, permission, measurement checks, proof-safe rewrites, and public-use rules.
- `COOZ-DAILY-AI-RUNBOOK.md` - Simple daily and weekly usage cadence.
- `COOZ-GEM-TESTING-PROTOCOL.md` - Stress tests and pass/fail gates for each Gem.

## Source Stack

Primary source truth:

- `brain/coach-cooz-avatar-content-v3/AVATAR-ICP-BELIEF-PROFILE.md`
- `brain/coach-cooz-avatar-content-v3/CONTENT-STRATEGY-V3.md`
- `brain/coach-cooz-avatar-content-v3/LINKEDIN-POSTS-V3.md`
- `brain/coach-cooz-avatar-content-v3/INSTAGRAM-YOUTUBE-BLOG-CASCADE-V3.md`
- `brain/coach-cooz-avatar-content-v3/VOICE-MEMO-INTAKE-PROMPTS.md`
- `brain/coach-cooz-offer-positioning-north-star-v3/NORTH-STAR-MISSION-VISION.md`
- `brain/coach-cooz-offer-positioning-north-star-v3/POSITIONING-CLARITY-LOCK.md`
- `brain/coach-cooz-offer-positioning-north-star-v3/OFFER-ARCHITECTURE-V3.md`
- `brain/coach-cooz-offer-positioning-north-star-v3/SERVICE-DESIGN-DELIVERY-MAP.md`
- `brain/coach-cooz-offer-positioning-north-star-v3/TRIAGE-TO-CLIENT-CONVERSION-SYSTEM.md`
- `brain/coach-cooz-offer-positioning-north-star-v3/PROOF-CLAIMS-VALIDATION-MAP.md`

Workflow source:

- `.agent/workflows/avatar-content-elevation.md`
- `.agent/workflows/cooz-flywheel.md`
- `.agent/workflows/offer-positioning-north-star.md`
- `skills/futurepedia-prompt-engineering/workflows/custom-ai-solution-architect.md`

## Recommended Gem Order

Create the Gems in this order:

1. Cooz Master Brand Brain
2. Cooz Proof And Claims Guard
3. Cooz Content Flywheel
4. Cooz LinkedIn Distribution
5. Cooz Design And Marketing Asset Builder
6. Cooz Service Ops

The Master Brand Brain and Proof Gem should be used as the guardrail layer before anything public ships.

## Operating Rule

Do not ask Gemini to "make content."

Give it:

- the source moment
- the buyer lane
- the intended platform
- the reader value
- the proof status
- the CTA intent

Then make it pass the quality gate.

## Boundary

This package does not edit any Google Antigravity files or prior V3 files. It is a standalone handoff system for Cooz.
