---
thread: jen-engine-v2
status: active
resume_hint: Jen Engine v2: weeks 1-2 BUILT on placeholder photos (04-deliverables/2026-09-06-engine-v2-weeks-1-2/); next = swap her shoots in from Drive folder 01, re-run build_weeks.py, drop week folders into Drive 04
branch: worktree-jen-engine-v2-weeks (built on top of worktree-jen-carousel-reel-concepts @306efbde8)
pin: false
---

## Purpose
Jen Santulan content system, retooled after she rejected the September build (2026-09-02). Engine v2: place-plus-price identity ("Your Valley agent. $800K and up, buying or selling"), done-for-her production in her photo-over-serif look, her veto inside the loop, saved replies and the file behind every post.

## Current State
- Living spec: `_active/clients/jen-listings/06-system/ENGINE-V2.md` (identity, the deal, realism gate, districts, formats, look, Drive, cadence, reply layer, scoreboard, what beats Coffee & Contracts). Read this first.
- Records: `06-system/2026-09-02-reset-after-jen-said-no.md` (her perspective, the deal), `06-system/2026-08-26-coffee-and-contracts-open-house-notes.md` (the webinar she was sold on), `06-system/2026-09-02-deep-research-what-works-valley-agents.md` (Gemini pass, DONE, $0.50, 47 sources; folded into ENGINE-V2.md section 12).
- Six-seat round table (Enrico, Sherrard, Grace Andrews, Jun Yuh, Kallaway, Jen-as-herself) unanimous: niche is the place; local formats need a price/place qualifier in the hook or they're reach with nobody in it; photo-motion reels over her listing photos are format #1; condo and rail topics dead under her realism gate, insurance and rates pass.
- Builders in `04-deliverables/2026-09-01-september-carousels/`: `gen_photo.py` (photo-look cards PH1–3), `build_reel.py` + `reels/*.json` (photo-motion reels, proof: `video/insurance-before-offer.mp4`, gitignored), `build_video.py` + `tts_fal.py` (narrated deck), `new_set.py`, `gen_deck.py` (16-board presentation, superseded in spirit by v2), `gen_topics.py` (five FTHB memo cards, now off-thesis).
- Drive drop folder live: https://drive.google.com/drive/folders/1yMVTQdZ0TkfieKPckwidJJ3Ci9m0s2iZ (01 listings · 02 phone clips · 03 portraits · 04 ready to post · READ ME). Empty until Farrice drags her listing shoots in.
- Memory updated: `feedback_jen-hands-off-photo-look.md`, `feedback_jen-presentation-framing.md`, `project_jen-valley-native-system.md`. Calibration log has the 2026-09-02 rows.
- Uncertain: real comps for "what $X buys" posts (VERIFY); her listing photos (none on disk, placeholders only).

## Weeks 1-2 (built 2026-09-02, lane worktree-jen-engine-v2-weeks)
- `04-deliverables/2026-09-06-engine-v2-weeks-1-2/build_weeks.py` — one command, six finished posts (4 photo-motion reels + 2 three-slide cards), captions.txt, day-plan.txt, saved-replies.txt (four arrivals), MESSAGE-to-jen.txt per week; `--no-video` for the copy/QA loop. Imports gen_photo.py + build_reel.py (both extended: main guard, per-beat `size`, `out_dir`); auto-fit so a serif line never wraps.
- Week of 9/7: 01 attract "what $850K actually buys" (3 real comps, Redfin 9/2) · 02 position "6.66% is not the number that matters" (Freddie Mac 8/27) · 03 convert 5421 Bothwell ($5,695,000, Active 9/2, luxury register).
- Week of 9/14: 04 attract "$900K sherman oaks vs van nuys" · 05 position insurance-before-the-offer (FAIR Plan Oct 15) · 06 position seller-side "tarzana median −14.5% is still not your number".
- `FACTS.md` = every number, label, source, and the send-day re-check (rates refresh 9/3; listings still active; Bothwell price from her MLS). `PHOTO-SWAP.md` = every frame → the shot from folder 01/03 that replaces it. `COPY-weeks-1-2.md` = the words in one file for lint + classifier (fair-housing PASS; captions 1.5/10 and 0/10 clean).
- Rules encoded: other brokers' listings never named by address on a frame or caption (addresses go out only in her DM, the reason to write); no "first home"/buyer-type language; "buying or selling" in every ask.
- NOT in Drive folder 04 yet: photos are placeholders. Nothing goes to Jen on placeholders.

## Remaining Priority
1. Farrice drags her listing shoots into Drive folder 01 (and portraits into 03). 2. Swap per PHOTO-SWAP.md, `python3 build_weeks.py`, eyeball the six. 3. Refresh the three send-day facts in FACTS.md. 4. Drop `week-of-2026-09-07/` into Drive 04 with MESSAGE-to-jen.txt as the text. Show her the reel, not the spec. Week 3 candidates banked: 5200 Armida convert (status UNCONFIRMED, ask her), "just breathe" card (her words), a clean Van Nuys comps pull.

## Do-NOT-Rebuild
Weeks 1-2 builder + six posts (extend build_weeks.py WEEKS list for week 3; never a second generator). Valley Native line-drawing system (shelved, not deleted). The 16-board deck and narrated video (done). The five FTHB topic cards (off-thesis; mine them for lines only). Never a weekly ask on Jen; never name the machine to her.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
