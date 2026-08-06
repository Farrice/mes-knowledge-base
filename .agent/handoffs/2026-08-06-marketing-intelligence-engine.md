---
thread: marketing-intelligence-engine
status: ready
resume_hint: Fill listening-creators.md (10-20 real creators via /creator-aperture) then first full scout run + Organic Engine v1 pen card
unfinished: Real creator list; Organic Engine v1; verify first unattended zeitgeist + angle-brief receipts; payment URL still blocks mission 2b
branch: main
pin: true
---

# Marketing Intelligence Engine — Overnight Build (Cody Forge + Signal Scout + Angle Brief)

## Purpose
- **Next session should do:** (1) get Farrice's real 10–20 listening creators into `_active/linkedin-launch/05-lead-gen/listening-creators.md` (Cody's aperture rule: creators his BUYER follows — supplement/performance-brand ICP lane is currently empty), then run the first full `signal_scout.py` pass on them; (2) build Organic Engine v1 — ONE hybrid Lara×Cole pen card under VOICE-CARD (his tap 2026-08-06; single authored pen, honors one-author-per-body), `DAILY-DRAFT-PROMPT.md`, `com.antigravity.organic-drafts` plist (~2h, no new Python — clone the angle-brief runner pattern); (3) verify first unattended receipts: `.agent/zeitgeist-run.log` (daily 06:20) and `.agent/angle-brief-run.log` (Mon/Thu 07:00).
- **Not in scope:** ANY outreach automation — sends/reputation/distribution stay HUMAN (binding, 2026-08-06; the DM-draft queue was killed, not disabled). Enrichment-stack purchases (Apollo/Prospeo/etc.) stay deferred. Never re-research the Isenberg×Schneider video — it's extracted.

## Load First
- `deliverables/research-briefs/night-shift-2026-08-06/` — the build report; "judgment calls" section carries the open decisions
- `_active/farrice-brand/04-deliverables/ANGLE-BRIEF-PROMPT.md` — the loop's synthesis contract (filed to 04-deliverables post-session; runner updated to match)
- `skills/cody-schneider-signal-outbound/SKILL.md` + `genius.md` — the extracted doctrine; `references/era-bound-2026-08-stack.md` for tool specifics
- `_active/linkedin-launch/05-lead-gen/engager-rosters/ROSTER-2026-08-06-test.md` — what scout output looks like (resonance + ICP verbatim + scored roster)
- `_active/linkedin-launch/CAMPAIGN.md` — mission 2b still send-ready; $750 payment URL still missing (the real blocker)

## Current State
- **Objective:** AI marketing leverage without automating his reputation — listening loops + visual briefs + deployable expert, extend-never-rebuild.
- **What is already done:** Cody Schneider forge (11 workflows, 3 tiers, blind-pass EVAL-062 PASS, auditor 0/7 failing, `/cody-schneider` front door + menu parity minted); Signal Scout (`execution/signal_scout.py` + `linkedin-post-reactions`/`linkedin-post-comments` actors in `apify_client.py`, live-tested: 4 posts → 229 engagers, $0.50, receipt `.agent/health/signal-scout-2026-08-06-test.json`); Angle Brief loop loaded (`com.antigravity.angle-brief`, Mon/Thu 07:00) with supervised edition 001 on the board; grounding brief `ai-marketing-agents-hype-vs-harness`; zeitgeist confirmed armed (stale "not loaded" warning was wrong); registries updated (apify-usage-policy, cli-reference, SLASH_COMMANDS); 3 commits pushed to main (through `371c0effc`); chain finalize logged.
- **What is uncertain or stale:** zeitgeist + angle-brief first UNATTENDED runs unproven (check logs); new actors have one pricing datapoint each; Cody skill is single-source (his solo channel = extension corpus, 2 transcripts already in `reference-corpus/`); the ~80% creator-coverage heuristic is UNCONFIRMED until two scout runs compare.
- **Latest proof/receipt:** blind-pass ledger `extractions/cody-schneider-signal-outbound/blind-pass-log.md` (EVAL-062); scout health receipt above; briefs board.

## Suggested Skills / Workflows
- `/resonance-to-angle` — turn the next scout roster into content angles (Cody T1)
- `/creator-aperture` — build the real 10–20 creator list with Farrice (Cody T1; emits the scout's creators file)
- `/cody-schneider` — expert front door
- `/briefing-room` — open the board with all three session briefs
- `/voice-os` — for the Lara×Cole hybrid pen card taste pass

## Exact Next Prompt
```text
Read .agent/handoffs/LATEST.md. Then: run /creator-aperture with me to build my real 10-20 listening creators (buyer-follows rule, both lanes: solopreneur/AI-consulting + supplement-brand ICP), write them to _active/linkedin-launch/05-lead-gen/listening-creators.md, run python3 execution/signal_scout.py, and read me the resonance report. Then build Organic Engine v1 per the deferred spec (hybrid Lara×Cole pen card — show me the pen card for a taste pass BEFORE wiring the plist).
```

## Acceptance Criteria
- listening-creators.md has 10–20 real, verified handles across both lanes
- A full scout run completes under budget with a receipt, and the resonance report references his actual niche
- Organic Engine: pen card approved by Farrice's felt verdict, first draft queue produced, plist loaded, zero send capability
- Both loop logs show one clean unattended run each

## Risk Notes
- Playwright MCP could technically drive a logged-in LinkedIn — ungated, unused; needs an explicit gate decision from Farrice
- Scout samples page 1 of engagement per post (≤100 reactions + ≤100 comments) — mega-posts are sampled, not exhausted
- Apify monthly budget $29 with ~$27 headroom; scout ≈ $0.50/run at test scope — cadence is the cost lever
- No secrets in this packet; APIFY_TOKEN lives in `.env` (loaded by the scout via dotenv for headless runs)

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
