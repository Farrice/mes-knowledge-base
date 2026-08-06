---
date: 2026-08-06
session: video-studio-edit-bay
tier: operator-guide
status: enriched
---

# The Edit Bay — What We Built 2026-08-06 and How to Use It

> This session turned a YouTube pipeline demo into a working in-house video studio. Brad Bonanno's agentic edit pipeline was watched with frames, decoded through MES 3.0, and rebuilt on the house stack — free-first, Higgsfield-free, verified end-to-end on real footage at $0. You can now say "edit this" or "turn this essay into an explainer" and get a captioned, three-format, publish-ready package. Companion files: `skills/video-studio/SKILL.md` (front door) · `directives/video-studio-policy.md` (the 10 binding rules) · `extractions/brad-bonanno-edit-bay/extraction-report.md` (the source decode) · handoff `.agent/handoffs/2026-08-06-video-studio-edit-bay.md`.

## ⚡ If you only read 10 lines

1. Front door: `skills/video-studio/SKILL.md`. Full production run: `workflows/produce-explainer.md`.
2. Transcribe first, always: `python3 execution/transcribe_local.py <media> --project <slug> --srt` — WhisperX, local, $0, word-level timestamps.
3. The agent writes `cutlist.json` (beats + shots); `python3 execution/edit_bay.py cutlist-apply --project <slug>` renders it. Use `--dry-run` to see the plan first.
4. Seven subcommands: `probe · cutlist-apply · overlay · captions-burn · audio-mix · transcode · qa-probe`.
5. Three export presets, every release: `yt-169` · `vert-916` · `linkedin` (LinkedIn always burns captions).
6. Audio law: −14 LUFS integrated. `qa-probe` fails the render if it drifts — it caught a real −17 LUFS defect on the first live run.
7. Graphics are the fails-by-default stage: load `skills/video-studio/style/graphics-taste.md` § named stack before ANY comp, and run its pre-render grep.
8. QA loop = `video_qa.py inspect --seams` → picky-editor reads `REVIEW.md` → `fixlist.json` → revise → re-render. Cap 3 iterations, then surface.
9. **ffmpeg trap:** Homebrew's build here has no libass (can't burn captions). The static build at `tools/bin/ffmpeg` is auto-preferred — never hardcode the Homebrew path for filter work.
10. His rulings, binding: no Higgsfield anywhere · his own VO always (no clone, no TTS) · free-first B-roll ladder · he posts, not the system.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/transcribe_local.py <media> --project <slug> --srt` | `transcript.json` (word-level) + `captions/auto.srt` | Any footage or VO enters the studio |
| `python3 execution/edit_bay.py probe --in <file>` | Normalized JSON: duration, w/h, fps, codecs | Checking an unknown source before planning cuts |
| `python3 execution/edit_bay.py cutlist-apply --project <slug> [--dry-run]` | `renders/vNN.mp4` at preset spec, manifest-indexed | The cutlist is written and you want the render |
| `python3 execution/edit_bay.py captions-burn --in <f> --srt <f> --style <preset>` | Captioned MP4 | Shorts, LinkedIn, or any burn-required export |
| `python3 execution/edit_bay.py audio-mix --in <f> [--music <f>] [--duck -10] --lufs -14` | Mixed, loudness-normalized MP4 | Music bed, SFX, or a loudness failure to fix |
| `python3 execution/edit_bay.py transcode --in <f> --preset <yt-169\|vert-916\|linkedin>` | Platform export in `exports/` | Final delivery, one call per format |
| `python3 execution/edit_bay.py qa-probe --project <slug> --render <path>` | Pass/fail report: resolution, fps, duration drift, LUFS, black frames, silences | Before any human or agent eyes look at a render |
| `python3 execution/video_qa.py inspect --project <slug> --render <p> --seams --graphics` | Seam-targeted frames + `inspection.json` | Feeding the picky-editor review |
| `python3 execution/video_qa.py fixlist-validate --file <p>` | Schema + citation check; downgrades uncited blockers | A reviewer just returned a fixlist |
| `python3 execution/broll_source.py search --query "..."` | Owned manifest hits FIRST, then Pexels/Pixabay results | A beat needs a visual you don't have |
| `python3 execution/broll_source.py fetch --id pexels:NNN --project <slug>` | Downloaded clip + manifest line with license/source_url | Taking a stock result into the project |

## The mental model

**Editing isn't a capability problem, it's a sensory one.** Claude can't hear, so it can't know where a cut lands — word-level timestamps are its ears. It can't see its own render, so overlays and captions fail silently — frame extraction is its eyes. Both gaps close with cheap local instrumentation, not a bigger model. Every stage of this studio exists at a boundary of what an agent can actually execute: read text, run a CLI, write code.

**Some stages are solved; some fail by default.** A rough cut is a pure transcript problem — it works every time, spot-check only. Anything visual (graphics, captions, overlays) fails by default and *requires* the review loop. Budget attention accordingly; don't frame-review a rough cut, don't ship a graphic unreviewed.

**Inspection is directed, not passive.** Defects concentrate at seams — cut boundaries, graphic edges, caption onsets. The QA layer extracts frames exactly there rather than sampling uniformly, which is why it finds things a video-understanding model would smooth over.

**Corrections compound or you pay for them forever.** Every note Farrice gives is a note he'd give again next week unless it's promoted into `_active/farrice-brand/voice/video-style.md` before the edit closes. That promotion step is the difference between a workflow and a system that gets better.

## Capability 1 — Transcript-driven cutting

**What it is.** WhisperX (faster-whisper + wav2vec2 forced alignment) running locally produces per-word start/end times. The agent reads the transcript, decides what goes — silences over 0.7s, filler, false starts, the weaker of two takes — and expresses those decisions as `shots[]` in `cutlist.json`. ffmpeg executes: each shot is trimmed and re-encoded to preset spec, then joined (normalize-then-concat, which kills the entire class of mixed-source concat bugs).

**When to reach for it.** Any raw recording. This is stage one of every production, in all three modes.

**When NOT to.** If the source already has clean captions you trust (a YouTube pull), `yt-dlp` VTT is cheaper — but its timings are segment-level, so you cannot cut on word boundaries with it. Word-accurate cutting requires WhisperX.

**How to invoke.**
```bash
python3 execution/transcribe_local.py _active/<slug>/05-assets/video/footage/take1.mp4 \
  --project <slug> --srt --model small
python3 execution/edit_bay.py cutlist-apply --project <slug> --dry-run   # inspect the plan
python3 execution/edit_bay.py cutlist-apply --project <slug>             # render vNN
```

**Worked example.** 90 seconds of source → 14 segments, 310 timed words → a hand-written 6-shot cutlist dropping two dead sections → 59.65s render at 1920×1080, duration drift 0.06s against the cutlist. Receipts in `_active/video-studio-shakedown/05-assets/video/`.

**Honest edges.** `--model small` is the default and is good; `large-v3` is slower on CPU and rarely changes cut decisions. The wrapper wires certifi itself because the venv python couldn't fetch the alignment model over SSL — if downloads fail, that's the first thing to check. xfade transitions add intermediate re-encodes; on long projects that costs time and disk.

## Capability 2 — The QA loop (the part that actually makes it work)

**What it is.** Two layers. `qa-probe` is deterministic: resolution, fps, duration-vs-cutlist, integrated LUFS, black frames, long silences — machine-checkable defects never reach an agent's eyes. Then `video_qa.py inspect` pulls frames at every cut ±0.2s, every graphic in/out edge, and caption onsets, writes `inspection.json` mapping each frame to a shot and a reason, and a reviewer reads them against `REVIEW.md` as a picky senior editor. Output is `fixlist.json`: timestamp, shot id, kind, severity, observed vs expected, and an executable action. Blockers must cite a style rule or they're auto-downgraded to nits.

**When to reach for it.** Every render that has anything visual on it. Mandatory by policy.

**When NOT to.** A rough cut with no overlays — run `qa-probe` only and move on. Reviewing a rough cut frame-by-frame wastes the loop's budget on a stage that doesn't fail.

**How to invoke.**
```bash
python3 execution/edit_bay.py qa-probe --project <slug> --render renders/v01.mp4
python3 execution/video_qa.py inspect --project <slug> --render renders/v01.mp4 --seams --graphics
# reviewer (sub-agent or Codex) reads REVIEW.md + inspection.json → writes renders/v01-fixlist.json
python3 execution/video_qa.py fixlist-validate --file renders/v01-fixlist.json
python3 execution/video_qa.py apply-log --project <slug> --fixlist renders/v01-fixlist.json
```

**Worked example.** First live probe returned `loudness: fail — got -17.09 LUFS`, everything else passing. One `audio-mix --lufs -14` call, re-probe: all six checks pass. The loop caught a defect a human would have shipped.

**Honest edges.** Reviewer judgment is nondeterministic — that's why blockers need citations and the loop caps at 3 iterations before surfacing to Farrice. The picky-editor persona has run once (this session); its calibration against his taste is unproven until a real pilot.

## Capability 3 — The taste layer

**What it is.** Motion graphics are HTML/TSX, so graphic quality *is* front-end design quality. `skills/video-studio/style/graphics-taste.md` holds ten numbered, citable rules (authored-not-defaulted, one idea per graphic, hierarchy through type not decoration, motivated motion, name what's in tension, squint test, brand type law, real data, the travel test) plus a slop-tell list that acts as automatic blockers and a deterministic pre-render grep over comp source for off-brand fonts, off-palette hex values, and shadow stacks. The named load — this file, the `frontend-design` skill, the three-level style merge, grace-liu on taste-fog — is gated into the workflow, the SKILL table, and the reviewer contract.

**When to reach for it.** Before the first comp of any session. No exceptions — "it looks fine" is exactly when the load gets skipped.

**When NOT to.** Pure cut-and-caption work with no graphics; the style files alone cover captions.

**How to invoke.** Read `skills/video-studio/style/graphics-taste.md`, follow its § "The named load", then build. Grep the comp source before rendering. Reviewers cite violations as `graphics-taste#<n>`.

**Honest edges.** Written this session, never exercised on a real comp. The first pilot will show whether the rules bite or need sharpening; the pre-render grep is manual and could become a small linter if it proves leaky.

## Capability 4 — B-roll ladder and sourcing

**What it is.** An ordered, mandatory ladder: own footage and screen recordings → free stock (Pexels primary, Pixabay secondary) → motion graphics as code → fal-generated last, quoted first. `broll_source.py search` enforces the first rung in code by grepping the asset manifest before touching any API. Downloads carry `license` and `source_url` into the manifest.

**When to reach for it.** A beat's annotation asks for a visual you don't have.

**When NOT to.** When the beat is data, a concept, or a diagram — a graphic beats found footage there, and it's rung 3 for a reason. Also never for lip-sync plates (the Decoupling Law: action B-roll cuts away from the speaker).

**How to invoke.**
```bash
python3 execution/broll_source.py search --query "server room" --orientation landscape --min-duration 5
python3 execution/broll_source.py fetch --id pexels:12345 --project <slug> --tags "tech,server"
```

**Honest edges.** No live API call has been made — `PEXELS_API_KEY` and `PIXABAY_API_KEY` are pending free signups. Until then the ladder runs on rungs 1, 3, and 4 only.

## Composition table (options, never pipeline steps)

| Stacks with | What it adds | When it earns its cost |
|---|---|---|
| `skills/remotion-video-creation/` (34 rules) | Full programmatic comps: charts, maps, caption pipelines; `rules/high-retention-editing.md` is the pacing law | Data-heavy or full-frame graphic beats |
| HyperFrames (`_active/hyperframes-studio/`, cloned) | HTML overlay graphics on real footage, no build step | Once inspected and wired — lower thirds and callouts |
| `skills/brad-bonanno-explainer-architecture` | What to *say* — explainer structure, demo discipline, trust anchors | Planning a video before annotating the script |
| `skills/jenny-hoyos-shorts` | Shorts grammar for `derive-shorts.md` | Cutting verticals from a finished long-form |
| `/generate` + craft-map masters | Generated B-roll with real direction (cinema-worldbuilder, Dave Clark flatness audit) | Rung 4 only, when nothing else can serve the beat |
| `/parallax`, `/voice-os` | Source material and voice fidelity for scripts | Essay-to-video conversions |

## Where things live

- Execution: `execution/{transcribe_local,edit_bay,video_qa,broll_source}.py` · static ffmpeg at `tools/bin/ffmpeg` (gitignored)
- Skill: `skills/video-studio/` — SKILL.md, 6 workflows, REVIEW.md, `schemas/`, `style/`, `caption-styles.json`
- Policy: `directives/video-studio-policy.md` · Extraction: `extractions/brad-bonanno-edit-bay/`
- Brand style (the compounding file): `_active/farrice-brand/voice/video-style.md`
- Proof: `_active/video-studio-shakedown/05-assets/video/` · Commits `7d43c4fb6`, `ea01feaa3`, `c8f605811`
