# Audit: watch → extract-forge → source-to-skill-system

## Verdict

Keep the workflow. Improve its acquisition reliability, reduce duplicate handoffs, and make applied proof plus outcome feedback the finish line. The existing system already has strong source, voice and behavior-proof standards. Its weakness is inconsistent execution across the connections, not a lack of more expertise documents.

Audit scope: this actual run plus the invoked canonical files and relevant existing Dan skills. This is not a whole-repository health certification.

## Findings ranked by consequence

| Priority | Evidence from this run | Consequence | Action/status |
|---|---|---|---|
| 1 | `watch/scripts/download.py` inherits global yt-dlp config/plugins; subprocess calls have no overall timeout. DNS failure retried, then token provider repeatedly failed in an unrestricted run. | A recoverable source task can stall before extraction, and repeated diagnosis costs attention. | FIXED IN LOCAL FALLBACK: isolated downloader configuration, bounded retries/deadlines, child-group termination, stage logs. Global watch itself unchanged. |
| 2 | The watch skill offers paid Whisper API fallback; keyless mode has no built-in offline ASR. Installed local whisper.cpp/model were available but unused. Default GPU run crashed; CPU run passed. | A free-use requirement can end in frames-only or a paid suggestion despite an available local path. | FIXED IN LOCAL FALLBACK: native captions first, CPU offline transcription second, explicit failure if dependencies are absent. Full URL path passed; offline path passed on a 20-second source clip. |
| 3 | `fetch-video-context.py` has a default 600-second skip threshold. This source is 1,882 seconds. Original watch scene pass selected only 14 frames and none after 24:39. | A forge can skip a relevant visual demonstration or leave the conclusion uncovered while the transcript continues. | THIS RUN RESOLVED: no duration skip; 40 full-range frames plus 14 scene frames reviewed. Uniform/cue options and review state in the fallback. Long-video coverage is still sampled. |
| 4 | `source-to-skill-extraction.md` still forbids writing Google and assigns ownership to retired Codex Antigravity. `skill-system-contract.md` contains a stale workspace exception. | Correct active-workspace execution competes with historical authority text. | DIAGNOSED: followed current AGENTS.md and isolated worktree. Broader authority cleanup remains a separate reviewable patch; no indiscriminate rewrites. |
| 5 | Forge asks for 8–15 workflows and its comparison table still says ordinary extraction produces 3–5, while its own current opening says ordinary extraction can match forge scale. Dan already has two skill packages. | Padding and duplicate architecture can substitute for a useful source delta. | RESOLVED IN THIS BUILD: three new components inside existing owner; no new Dan persona, no arbitrary quota, no hot skill promotion. |
| 6 | Forge and source-to-system repeat acquisition, routing, architecture and verification. Existing prompt-library and pointer tools have broad default write scopes. | Repeated ceremony increases context and creates unrelated churn. | BOUNDED: one captured source package, one build contract, explicit component loading and targeted wiring. Global/broad repair deferred. |
| 7 | This source selects winners, includes an established account, proposes creator amplification, and does not show a zero-to-10K experiment. | Faithful imitation can inherit exposure advantages and be mistaken for expected beginner performance. | BUILT INTO ADAPTATION: ordinary-post comparisons, same-age measurement, audience fit, attribution and explicit untested outcomes. |
| 8 | Source-system contract already demands behavior-changing proof; a new command by itself is insufficient. The visible demo itself produces an oversized breakdown at 18:09. | “System built” can mean documents exist, with no better output or easier reuse. | APPLIED: same-input draft transformation and callable bounded workflow. Human preference and independent cold-start remain pending. |
| 9 | Existing `execution/video_context/transcript.py` imports `.common`, absent in this checkout; importing it failed. | Reuse by filename alone can conceal a broken dependency boundary. | AVOIDED: fallback has a small stdlib parser with overlap and failure tests. Existing unrelated package left untouched. |
| 10 | No live posts, audience baseline, qualified replies or revenue event were provided or created in this run. | Model scoring cannot show whether the strategy works commercially. | OPEN: six-post matched pilot and outcome table prepared. Use existing content/outcome trackers when real observations arrive; do not create another dashboard. |

## Better recurring sequence

1. **Acquire once.** URL-keyed source package: metadata, raw captions, clean transcript, segments, frames, coverage and limits. Fall back based on the actual failed stage. Retain full video locally; avoid putting large media into Git.
2. **Extract the useful delta.** Compare existing owner, preserve explicit method and observed examples, label inferences. A source can justify a reference addition instead of a whole skill.
3. **Apply before expanding.** Run one realistic input through the new method. Preserve what changed and whether the author accepts it. Do not confuse an applied example with a blinded comparison.
4. **Wire only the smallest usable surface.** One entry route and focused components. Keep source evidence cold. Consolidate approval around concrete outputs when local work is already authorized.
5. **Measure use and outcomes separately.** First prove future execution works; then record audience/qualified actions after actual publication. Alter only a supported weak link. Stop building when a real test would teach more.

## What stays

Timestamp grounding; viewing visuals where they matter; extending existing owners; factual veto; author voice; worktree isolation; no paid calls or external sending without approval; the existing behavior-proof contract. Do not add a new universal score or permanent enforcement layer to prove this audit ran.

## What this run cannot certify

Future YouTube availability, continuous visual comprehension, full-length offline transcription accuracy, independent cold-start behavior, human taste acceptance, beginner growth, qualified pipeline or revenue. The tool is free in the sense of no new subscription or per-call service charges; local compute, disk use and the existing Codex plan still apply.
