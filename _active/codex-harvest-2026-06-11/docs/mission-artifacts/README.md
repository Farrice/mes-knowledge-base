# Mission Artifacts

Mission artifacts are durable outputs created by Mission OS when a mission needs more than transient chat context.

The engineering contract is inspired by Compound Engineering, but adapted to Antigravity:

- `strategy-anchor.md` keeps the mission tied to a guiding bet.
- `requirements.md` captures requirements with stable R/A/F/AE identifiers.
- `plan.md` breaks execution into stable U-IDs that must not be renumbered.
- `review.md` records scrutiny, user-outcome review, and residual work decisions.
- `solution-capture.md` preserves solved problems while context is fresh.
- `pulse.md` captures post-ship or post-delivery signals.

Use `execution/mission_control.py create --artifact-contract engineering` to generate the starter files for a mission.
