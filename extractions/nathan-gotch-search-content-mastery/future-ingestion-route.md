# Future Nathan Gotch Episode Ingestion Route

## Current state

`NO EVENT` — the seed source announces future episodes, but no uncaptured episode is treated as evidence. No finding, mechanic, contradiction, or result is invented in advance.

## Trigger

Use this route only when a public episode URL and publication date exist.

1. Check `corpus-manifest.json` and `extractions/video-context/<video-id>/` for an existing package.
2. If the source already exists, compare source hashes and reuse the canonical transcript instead of copying it.
3. Capture native captions first through the watch workflow. Whisper remains cost-gated fallback only.
4. Preserve metadata, caption provenance, raw timed captions, timestamped segments, uncertainty, source hashes, and a timestamped claims ledger.
5. Inspect visuals only at cues where the screen carries evidence the transcript cannot establish. Record the frame hash, observation, evidence value, and limitation.
6. Label each finding `OBSERVED`, `INFERRED`, `CORROBORATED`, or `UNCONFIRMED`. `OBSERVED` means the source said or showed it; it does not prove a market effect.
7. Compare the episode against `portfolio-forge.md`: duplicate mechanics merge into the evidence count; contradictions and temporal changes remain explicit.
8. Propose any workflow or rubric change in the append-only recommendation ledger. Do not mutate or promote the skill automatically.
9. Run `python3 execution/verify_search_content_mastery.py` before calling the updated system runtime-observed.

## Stop conditions

- Missing or unusable source evidence: remain `NO EVENT` or `UNCONFIRMED`.
- Paid transcript fallback denied: stop; do not synthesize from memory.
- Existing canonical source mismatch: preserve both hashes and investigate before integration.
- Market-effect claim without dated external evidence: keep `UNTESTED`.
- Publishing, outreach, connector write, sponsorship, payment, deployment, or paid generation: explicit approval required.
