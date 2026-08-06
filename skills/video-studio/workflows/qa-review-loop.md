# QA Review Loop — render → picky editor → fixlist → revise (max 3 passes)

No editor edits with their eyes closed. Visual stages fail by default; this loop is where
they get fixed. Two layers: deterministic probe first (never waste agent eyes on
machine-checkable defects), judgment review second.

## Per iteration (N starts at 1)

1. **Deterministic probe** — `python3 execution/edit_bay.py qa-probe --project <slug> --render renders/vNN.mp4`
   Fails here (resolution/fps/duration-drift/loudness/black frames/silences) are fixed
   directly — they never reach the reviewer.
2. **Seam-targeted frames** — `python3 execution/video_qa.py inspect --project <slug> --render renders/vNN.mp4 --seams --graphics`
   → `renders/vNN-frames/` + `inspection.json` (frame → shot_id, timestamp, why-extracted).
   Controllable inspection: cuts ±0.2s, graphic in/out edges, caption onsets — NOT uniform sampling.
3. **Picky-editor review** — dispatch a sub-agent (or run inline in Codex) with `REVIEW.md`
   as its full contract + the style files + `inspection.json`. Brief negatively per house
   rule: *no Chain, no finalize, no Notion, no Next Moves — return only fixlist.json.*
4. **Validate + apply** — `python3 execution/video_qa.py fixlist-validate --file renders/vNN-fixlist.json`.
   Apply blockers to `cutlist.json` / comps / SRT; nits only if free.
   `python3 execution/video_qa.py apply-log --project <slug> --fixlist renders/vNN-fixlist.json`
   (appends to `cutlist.revisions[]`). Re-render → v(N+1).
5. **Exit**: verdict `pass` → done. N=3 without pass → STOP, surface remaining blockers to
   Farrice with frames (a stuck loop is a decision point, not a grind — compass, not cage).

## Farrice review (after loop passes)
His notes arrive as a fixlist with `"reviewer":"farrice"`. Apply, then **promote every one
into `_active/farrice-brand/voice/video-style.md` § Correction Log before close-out** — a note
given twice is a system failure.

## Reviewer variance guards
- Blockers REQUIRE a style-rule citation; no citation → auto-downgrade to nit.
- Fix actions must be executable verbatim ("move s014 out to 36.42"), never aesthetic vibes.
- The reviewer sees the previous fixlist — re-raising a fixed item needs the frame that proves the regression.
