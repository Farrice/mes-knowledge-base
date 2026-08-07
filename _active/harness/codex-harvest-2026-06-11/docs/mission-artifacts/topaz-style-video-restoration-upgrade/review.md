# Review Ledger: Topaz-Style Video Restoration Upgrade

Created: 2026-05-11
Mission: topaz-style-video-restoration-upgrade

## Scrutiny Review
- Scope reviewed: `execution/video_enhance.py`, `execution/test_video_enhance.py`, premium real-clip output pack.
- Checks run:
  - `python3 -m py_compile execution/video_enhance.py execution/test_video_enhance.py`
  - `python3 execution/test_video_enhance.py`
  - `python3 execution/mission_control.py validate topaz-style-video-restoration-upgrade`
  - `ffprobe` on `restore-clean.mp4`, `roi-premium.mp4`, `premium-comparison.mp4`, and `focus-premium-comparison.mp4`
- Findings: Premium mode works locally, but Real-ESRGAN and Topaz Video AI are not available on this machine; Topaz Photo AI exists but is not the video restoration app.
- Fixes applied: Added transparent capability logging, premium restoration profiles, bounded audio focus search, ROI-premium output, ROI contact sheet, and premium comparisons.

## User-Outcome Review
- Intended user/client experience: one command produces a richer inspection pack closer to a professional restoration workflow while keeping original comparisons and disclaimers.
- Evidence inspected: synthetic premium test outputs and real clip pack at `deliverables/video-enhancement/1000010463-20260511-111152/`.
- Gaps: This is still a deterministic local approximation, not proprietary Topaz Video AI or forensic analysis.
- Decision: Accepted as a materially stronger local pack; future upgrade requires installing an actual video AI backend or adding a dedicated adapter.

## Residual Work
| ID | Severity | Finding | Decision | Durable sink |
|---|---|---|---|---|
| RW1 | P2 | Actual Topaz Video AI adapter is not implemented because the video app is unavailable locally. | Defer until user installs/approves that tool. | `docs/mission-artifacts/topaz-style-video-restoration-upgrade/solution-capture.md` |
| RW2 | P3 | Premium full-clip processing is slower than standard mode. | Accept; premium is opt-in and standard remains default. | `execution/video_enhance.py` |
