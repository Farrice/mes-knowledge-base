# Pulse: Topaz-Style Video Restoration Upgrade

Created: 2026-05-11
Mission: topaz-style-video-restoration-upgrade

Use after a release, delivery, experiment, or meaningful mission milestone. Keep it single-page.

## Headlines
- Added `--quality-tier premium` and `--topaz-like` to `execution/video_enhance.py`.
- Produced a new premium pack for the provided clip at `deliverables/video-enhancement/1000010463-20260511-111152/`.
- Kept all outputs as viewing aids only, with no forensic proof claim.

## Usage Or Adoption
- User explicitly asked for Topaz-like quality after reviewing the initial ROI pack.
- The tool now supports bounded focus search with `--focus-search-start` and `--focus-search-end`; the real run constrained search to the first 8 seconds and detected focus at `3.63s`.

## System Or Delivery Performance
- Premium run completed successfully but is slower than standard mode.
- Local checks found Real-ESRGAN unavailable and Topaz Video AI unavailable; Topaz Photo AI is installed but not useful for video restoration.

## Quality Sample
- `restore-clean.mp4`: 2560x1440, 15 fps, full clip.
- `roi-premium.mp4`: 1240x600, 15 fps, full clip.
- `focus-premium-comparison.mp4`: 1280x720, 4 seconds around the detected early event window.
- `contact-sheet-roi.jpg`: ROI-centered still sequence from `1.63s` to `5.63s`.

## Followups
- F1. Add a true external backend adapter if the user installs Topaz Video AI or Real-ESRGAN.
- F2. Add optional frame-by-frame export at 0.1s intervals around the focus window for manual inspection.

## Report Decision
- Save or mirror to `docs/pulse-reports/`: no; mission-local pulse is enough.
