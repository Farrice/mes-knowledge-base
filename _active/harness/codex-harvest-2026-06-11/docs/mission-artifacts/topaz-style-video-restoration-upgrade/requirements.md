# Requirements: Topaz-Style Video Restoration Upgrade

Created: 2026-05-11
Mission: topaz-style-video-restoration-upgrade

## Problem Frame
Upgrade execution/video_enhance.py from a basic inspection enhancer toward a Topaz-like local restoration pack with explicit capability boundaries, stronger FFmpeg restoration profiles, optional AI detection, focused ROI outputs, and verification.

## Requirements
- R1. Existing single-output and standard variant-pack behavior must remain compatible.
- R2. Add a higher-quality local restoration tier that uses stronger FFmpeg restoration passes without claiming proprietary Topaz Video AI parity.
- R3. Detect and log optional restoration accelerators such as Real-ESRGAN and Topaz Video AI availability; skip cleanly when unavailable.
- R4. Support bounded audio focus search so the user can constrain spike detection to a known time range such as the first 8 seconds.
- R5. Improve ROI-centered review artifacts, including a focused ROI contact sheet when a crop is supplied.
- R6. Every output and summary must preserve the interpretation boundary: viewing aid only, not proof of contact, fault, causation, or responsibility.

## Actors
- A1. User inspecting home-security video for clearer viewing.
- A2. `execution/video_enhance.py` CLI user.
- A3. Future Codex operator rerunning or extending the tool.

## Key Flows
- F1. User runs the existing CLI -> standard outputs are produced unchanged.
- F2. User runs premium mode with ROI and focus search bounds -> premium variants, ROI zooms, ROI contact sheet, comparisons, logs, and manifest are produced.
- F3. Optional AI tools are absent -> the run logs skipped capability checks and continues locally.

## Acceptance Examples
- AE1. Given a synthetic video, when standard tests run, then prior expected outputs and logs still pass.
- AE2. Given `--quality-tier premium --roi x,y,w,h`, when the variant pack runs, then premium outputs and ROI contact sheet exist and are listed in the manifest.
- AE3. Given audio with a spike outside a bounded search window and one inside it, when `--focus-search-end` is set, then focus detection lands inside the bounded window.
- AE4. Given unavailable Real-ESRGAN or Topaz Video AI, when premium mode runs, then skipped capability checks are logged instead of failing.

## Scope Boundaries
- In scope: `execution/video_enhance.py`, its tests, mission artifacts, and one rerun of the provided clip when practical.
- Out of scope: installing paid/proprietary Topaz software, claiming forensic proof, or modifying the original Google Antigravity workspace.

## Open Questions
- Blocking: none.
- Deferred: actual Topaz Video AI adapter if the user installs Topaz Video AI and wants that software invoked directly.
