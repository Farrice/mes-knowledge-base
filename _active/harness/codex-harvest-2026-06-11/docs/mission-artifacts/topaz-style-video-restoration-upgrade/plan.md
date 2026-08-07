# Unit Plan: Topaz-Style Video Restoration Upgrade

Created: 2026-05-11
Mission: topaz-style-video-restoration-upgrade

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **Compatibility Guard**
  - Covers: R1, R6, AE1
  - Scope: `execution/video_enhance.py`, `execution/test_video_enhance.py`
  - Decision: Keep existing defaults and filenames stable.
  - Tests or verification: py_compile and existing smoke tests pass.
  - Dependencies: none
- U2. **Premium Restoration Tier**
  - Covers: R2, R5, R6, AE2
  - Scope: premium FFmpeg filter profiles, premium outputs, manifest entries, summaries.
  - Decision: Use local deterministic restoration views; label them as approximations, not Topaz/proof.
  - Tests or verification: premium synthetic test verifies files, probes, manifest labels, and disclaimer.
  - Dependencies: U1
- U3. **Capability Transparency**
  - Covers: R3, AE4
  - Scope: optional tool detection and processing logs.
  - Decision: Detect Real-ESRGAN and Topaz Video AI availability but do not fail if missing.
  - Tests or verification: skipped capability rows appear when tools are unavailable.
  - Dependencies: U1
- U4. **Bounded Focus Search**
  - Covers: R4, AE3
  - Scope: audio focus detection and parser options.
  - Decision: Add explicit search start/end bounds instead of relying on manual external scans.
  - Tests or verification: synthetic bounded-spike case lands inside the requested window.
  - Dependencies: U1

## Sequencing
1. U1
2. U2
3. U3
4. U4

## Risks
- Over-sharpening creates false-looking edges: keep multiple variants, name outputs as viewing treatments, and retain original comparisons.
- Premium filters are slower: keep the standard tier as default and make premium opt-in.
- Topaz expectations exceed local tools: log local capability limits and do not imply proprietary model restoration.

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| Existing CLI remains stable | U1 | scrutiny | Existing tests pass |
| Premium mode produces richer artifacts | U2 | scrutiny/user-outcome | Premium outputs and manifest entries exist |
| Optional AI/tool availability is transparent | U3 | scrutiny | Capability log rows show found/skipped status |
| Known event windows can constrain audio focus | U4 | scrutiny/user-outcome | Focus time respects search bounds |
