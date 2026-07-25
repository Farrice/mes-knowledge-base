---
thread: jen-listings
status: ready
resume_hint: Film/post the Moonseed reels; then update SKILL.md + genius.md to @_jiing + jen-real-voice-profile.md
unfinished: Skill entry points still say @realestatewithjing and encode the retired hype register; 3 MLS facts need eyes-on confirm before filming
branch: main
pin: true
---

# Jen Listings — 1654 Moonseed Shoot Sheet + Voice Lock (@_jiing)

## Purpose
- **Next session should do:** get the Moonseed reels filmed/posted, and propagate the corrected voice reference into the skill's own entry points (SKILL.md + genius.md still say @realestatewithjing and encode the retired hype register).
- **Not in scope:** rewriting the hook set (Farrice-calibrated, delivered), re-scraping her IG (profile is current as of 2026-07-25), building a scraper tool (flagged on Forge Radar, not approved).

## Load First
- `_active/jen-listings/1654-moonseed-simi-valley/1654-moonseed-SHOOT-SHEET.md` — the deliverable: 6 hooks (hook separated from body script), IG caption, 3 team variations, pre-filming verify footer.
- `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` — NEW canonical voice source, built from her actual IG (bio + 20 posts/reels + 3 reels watched frame-by-frame). Wins over genius.md on any energy/register conflict.
- `~/.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback-jen-reel-hook-style.md` — updated format contract (hook-separated structure + calm-warm register).

## Current State
- **Objective:** listing-Reel hooks for 1654 Moonseed Ln, Simi Valley (Jen's own co-listing, MLS SR26157642, $700K, open house Sat/Sun 1-4).
- **What is already done:** v1 shoot sheet (finalized 8.3) → Farrice flagged the register as too hype → scraped @_jiing → wrote voice profile → v2 rewrite in her real voice with hooks separated → watched 3 reels frame-by-frame (spoken == caption confirmed, on-camera formula documented) → lead IG caption written → text-message-format package delivered in chat.
- **What is uncertain or stale:** Zillow engagement stats (3 days/807 views/33 saves) drift daily — re-pull morning of shoot. Two MLS contradictions unresolved: indoor laundry (description says yes, facts field says none) and whether HOA truly covers sewer (call Parklane 818-707-0200). "Zero shared walls" needs an eyes-on confirm before the wall-tap films.
- **Latest proof/receipt:** 3 chain finalizes on thread `listing-hook-set-v2` (composites 8.3, 8.7, 8.7); prose gate run 3x with golden-ref comparison documented.

## Suggested Skills / Workflows
- `/listing-content` — if another SFV/Ventura listing needs the same treatment (load the voice profile FIRST).
- `/voice-calibrate` — to run any non-Jen-authored copy through her register.
- `/watch` — needs a Groq key in `~/.config/watch/.env` to transcribe audio; IG blocks yt-dlp anonymously, so the working method is Playwright canvas seek-capture + reading burned-in captions.

## Exact Next Prompt
```text
Update skills/jen-santulan-listing-content/SKILL.md and genius.md to make jen-real-voice-profile.md the canonical voice source: fix the handle to @_jiing throughout, retire #realestatewithjing from the hashtag guidance, replace the high-energy register examples with her actual calm-warm exemplars, and add the hook-separated output shape (HOOK / Visual / Rest of script) to the workflow contract.
```

## Acceptance Criteria
- SKILL.md + genius.md reference @_jiing and jen-real-voice-profile.md; no surviving instruction to append #realestatewithjing.
- prompts-v2/listing-hook-set.md Output Skeleton carries the separated-hook shape.
- A fresh session loading only the skill produces calm-warm hooks without needing the correction re-explained.

## Risk Notes
- Voice regression: genius.md's §4 signature patterns still read hype-adjacent ("This shouldn't exist at $799K"); a future session loading Tier 2 without the profile could revert.
- Client-facing: anything Jen posts carries her license; keep the verify footer attached to every shoot sheet.
- Stats staleness: never let a spoken number ship without a same-day re-pull.
