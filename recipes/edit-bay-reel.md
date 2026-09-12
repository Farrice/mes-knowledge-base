---
job: edit-bay-reel
name: Edit bay / video studio reel
family: client-content
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Raw footage plus script to a finished, captioned, publish-ready reel through the Edit Bay pipeline — solved cuts spot-checked, anything visual QA'd, nothing sent without him.

## Sub-jobs / lanes
- L1 Script annotation — `skills/video-studio/workflows/script-annotation.md`; never start assembly unannotated [parallel]
- L2 Transcribe — `python3 execution/transcribe_local.py <media> --project <slug> --srt` [after: L1]
- L3 Rough cut — cutlist.json from the transcript, `python3 execution/edit_bay.py cutlist-apply --project <slug>` [after: L2]
- L4 Broll — `skills/video-studio/workflows/broll-ladder.md`: own footage, manifest search, free stock, graphics, then `/generate` [after: L3]
- L5 Graphics — HyperFrames or Remotion; taste gate `skills/video-studio/style/graphics-taste.md` plus `frontend-design` skill before any comp [after: L4]
- L6 Audio — `python3 execution/edit_bay.py audio-mix`, music bed, VO sidechain, minus 14 LUFS [after: L5]
- L7 Export and QA — `python3 execution/edit_bay.py transcode` x3 presets, `qa-probe`, `skills/video-studio/workflows/qa-review-loop.md` [after: L6]

## Ask me first
- Q: Which mode — talking head, VO only, or zero camera? · look first: `skills/video-studio/SKILL.md` modes section (his standing rule: no voice clone, no TTS narration)
- Q: Style overrides for this project? · look first: `_active/farrice-brand/voice/video-style.md`, the project's `style-overrides.md`

## Handles alone
Transcription, rough cut, broll ladder, graphics render, audio mix, transcode, QA loop.

## Comes back when
- A QA-loop correction repeats (promote it into the style file's Correction Log)
- A graphic needs a taste call the style files do not answer
- The publish or send decision

## Needs approval
Publishing or sending the finished reel · any paid `/generate` (fal) spend beyond the free-first default.

## Needs
`execution/transcribe_local.py` · `execution/edit_bay.py` · `skills/video-studio` style files · `_active/<slug>/05-assets/video/` workspace.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| own footage or stock has no broll match | escalate the ladder rung, log which rung closed it | it reaches the paid `/generate` rung |
| a Farrice correction repeats | promote into the style file Correction Log immediately | never — that is the rule, not a question |
| QA probe fails | fix and re-probe | never ship over a failed probe |

## Done means
Exported x3 presets, QA probe pass, workspace indexed to `/assets-board`, nothing sent.

## Ratchet log
- none yet
