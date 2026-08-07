# Strategy Anchor: Topaz-Style Video Restoration Upgrade

Created: 2026-05-11
Mission: topaz-style-video-restoration-upgrade

## Target Problem
The current enhancement pack is useful but still feels like a filter stack. The user expected something closer to a professional restoration workflow: multiple intelligent-looking views, better event isolation, better ROI review, and an honest explanation of which AI capabilities are actually available locally.

## Guiding Bet
Do not pretend local FFmpeg equals proprietary Topaz Video AI. Instead, build the most transparent local approximation: premium restoration profiles, optional accelerator detection, focus-window control, ROI-specific artifacts, and original-vs-enhanced comparisons.

## Audience
The user and friend reviewing the glass/window incident video for easier viewing.

## Key Metrics Or Proof Signals
- Existing smoke tests still pass.
- Premium mode writes richer outputs and logs skipped unavailable AI tools.
- Event focus can be constrained to the known first-8-second window.
- Every summary preserves the viewing-aid-only boundary.

## Active Tracks
- Compatibility-preserving CLI upgrade.
- Premium restoration and ROI-focused artifact generation.
- Verification on synthetic video and the provided clip when practical.

## Source Strategy
- Root `STRATEGY.md` checked: not applicable.
- Library Decision: adapt `docs/solutions/mission-engineering-artifact-contract.md`; no existing Topaz-style video enhancement solution was found.
- Mission-local strategy decision: Upgrade `execution/video_enhance.py` from a basic inspection enhancer toward a Topaz-like local restoration pack with explicit capability boundaries, stronger FFmpeg restoration profiles, optional AI detection, focused ROI outputs, and verification.
