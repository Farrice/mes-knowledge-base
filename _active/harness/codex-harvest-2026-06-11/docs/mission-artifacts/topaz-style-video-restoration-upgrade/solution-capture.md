# Solution Capture: Topaz-Style Video Restoration Upgrade

Created: 2026-05-11
Mission: topaz-style-video-restoration-upgrade

Use this while context is fresh. If the learning is generalizable, copy or convert it into `docs/solutions/`.

## Track
- Type: workflow

## Symptoms Or Context
- The first implementation behaved like a useful FFmpeg inspection filter pack, but the user's quality target was closer to Topaz-style video restoration: restoration profiles, model/accelerator awareness, event-window control, and ROI-focused review.

## What Did Not Work
- Treating "enhance" as brightness, denoise, sharpen, and scale alone under-served the user's expectation.
- Claiming Topaz-level quality without installed video AI tooling would be misleading.
- Unbounded audio auto-focus can choose the wrong spike when the user knows the event happens inside a smaller time range.

## Working Solution Or Durable Guidance
- Keep standard mode stable, then add an opt-in premium tier with stronger local restoration filters and explicit capability checks.
- Add bounded focus search options so known event windows become part of the tool, not a manual pre-scan.
- Add ROI-specific premium outputs and contact sheets because the user's actual review target is a region, not the whole frame.

## Why This Works
- The premium tier uses available local FFmpeg filters for deblocking, temporal/spatial denoise, normalization, upscaling, sharpening, edge maps, and motion interpolation.
- Logs and manifest keep the capability boundary explicit: Real-ESRGAN and Topaz Video AI are checked, skipped when absent, and never implied.
- Synthetic and real-clip checks verify that the richer outputs are generated without modifying the source file.

## Prevention Or Reuse
- For future "make it like X premium software" requests: first detect whether the real backend is installed, then build a local approximation with explicit naming and proof boundaries.
- For video inspection tools: include time-window focus constraints and ROI artifacts as first-class controls.

## Generalization Decision
- Keep mission-local: yes for now.
- Promote to `docs/solutions/`: no; wait until another similar restoration/inspection request confirms reuse value.
