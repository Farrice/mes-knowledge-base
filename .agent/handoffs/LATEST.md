# Latest Handoff

**Thread:** about-rebuild-ship  
**Full path:** .agent/handoffs/2026-07-28-about-rebuild-ship.md  
**Date:** 2026-07-28 (today)  
**Status:** ready  
**Title:** LinkedIn Launch — About Rebuild v2 (Three Takes + Co-Creation Layer)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume about-rebuild-ship` for this one.

---

---
thread: about-rebuild-ship
status: ready
resume_hint: Gut-pick one of three About takes, /voice-compile, headline, ship profile, send teardown #1
unfinished: About pick · headline · featured · booking link · teardown sends · first content
branch: main
pin: true
---

# LinkedIn Launch — About Rebuild v2 (Three Takes + Co-Creation Layer)

## Purpose
- **Next session should do:** Gut-pick one of three About takes → /voice-compile (12 pending) → resolve headline against the picked About → ship profile top-to-bottom → send teardown #1 (Transparent Labs). One Pen Protocol pass max on the winner; iteration brake is now hook-enforced.
- **Not in scope:** New About variants beyond the pick+one-pass; re-litigating the reader-first architecture ruling; rebuilding the writers-room (Pen Protocol shipped, binding).

## Load First
- `.agent/handoffs/2026-07-28-about-rebuild-ship.md` — the full ship checklist + binding critiques distilled (THE working doc)
- `_active/linkedin-launch/03-launch/2026-07-28-about-rebuild-three-takes.md` — the three takes (Mirror / Aisle / Decision), all classifier-CLEAN ≤2,600
- `_active/farrice-brand/voice/VOICE-CARD.md` v1.2 — named-place principle, payoff punch, heat-in-nouns now in §6
- `.agent/handoffs/2026-07-27-positioning-before-headline.md` — headline is STILL the open positioning decision
- `_active/linkedin-launch/03-launch/2026-07-27-profile-top-to-bottom.md` — §7 featured section, §1-2 banner/photo, rest of profile copy

## Current State
- **Objective:** LinkedIn profile live + first teardown sent = inbound for the Proof-to-Market offer ($2,500 sprint, supplement/performance brands).
- **What is already done:** Three reader-first About takes ICP-grounded and CLEAN; Pen Protocol binding in writers-room; Co-Creation Enforcement Layer live in steering_loop_hook.py (spiral brake, feedback-turn protocol, work-mode front door); VOICE-CARD 1.2; 12 verdicts ratcheted; teardowns #1-3 built (NOTHING sent); all committed and pushed (f7b372d2b).
- **What is uncertain or stale:** Headline unresolved since 2026-07-27; sprint/retainer tier wording vs frozen Signal Pilot prices unreconciled; Cal.com booking link identified but unbuilt; About v9-v14 lineage superseded by the three takes — do not resume from v14.
- **Latest proof/receipt:** prose_classifier CLEAN 0/10 on all three takes; expert-load truth 15/15 loaded, 0 grepped; co-creation layer live-fired correctly on its first real prompt.

## Suggested Skills / Workflows
- `/resume about-rebuild-ship` — surfaces this thread pinned
- `/voice-compile` — fold 12 pending verdicts → VOICE-CARD 1.3 BEFORE judging takes
- `/writers-room` (Pen Protocol path) — the single allowed refinement pass on the picked take
- `/prose-check` on any edited line before paste-to-LinkedIn

## Exact Next Prompt
```text
Read .agent/handoffs/2026-07-28-about-rebuild-ship.md, run /voice-compile, then show me the three About takes side by side with a 2-line case for each. I'll gut-pick. After the pick: one Pen Protocol pass max, then headline resolved against the picked About, then the ship checklist top to bottom.
```

## Acceptance Criteria
- One take picked and live on LinkedIn (≤2,600, classifier CLEAN at paste time)
- Headline chosen and live; featured section's 3 slots populated; booking link exists
- Teardown #1 DM'd to Transparent Labs (send-before-build verb finally closed)
- VOICE-CARD at 1.3 with 0 pending verdicts

## Risk Notes
- Sibling-session concurrency on this tree (golden rule: one live writer; claim session_lock before multi-file work)
- Offer-tier wording may drift from CANONICAL-OFFER-BRIEF frozen prices — verify before promising specifics in DMs
- The spiral brake will fire if the new session produces About variants without a pick — that is by design, not a malfunction

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

