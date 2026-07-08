---
name: Transcript-Only Extraction Produces Generic, Unusable Output
problem_signature: an expert extraction built from transcripts alone is mechanically correct but generic and low-grip (5/10) — it captures WHAT the expert does, not HOW; no real voice, no verbatim exemplars, no specificity; user says "I couldn't use any of this to see results"
domain: extraction
tags: [extraction, embodiment, watch, voice, specificity, heartbeat, mes]
date: 2026-07-07
status: active
session: suzuki-os-embodiment-dwa-rebuild
---

## Problem

The Alex Suzuki Revenue OS was extracted from video **transcripts only** (the source videos were >10 min, so `/watch` visual context auto-skipped). It produced correct mechanics — "specific hook, proof body, opt-in CTA" — but the applied output (a DWA affiliate campaign) read generic and tame. The user's verdict: *"very straightforward and to the point… didn't capture the style and essence… I wouldn't be able to use any of this to see results."* This is the "structure without heartbeat = 5/10" failure.

## Root Cause

A transcript gives you the *claims and the sequence*. The **essence lives in the artifacts the expert shows on screen** — the actual winning tweets — and in the texture of how they're written. Those are visual (screenshots on his mirrorboard), invisible to a transcript. Extracting from transcript alone abstracts the real, hyper-specific, mechanism-named posts into bland principles. Compounding it: for a compliance-constrained niche, the first rebuild stripped the *grip* (specificity, mechanism, payload) along with the banned income claims — leaving only tameness.

## Approach That Worked

1. **Watch the video for the real artifacts.** `/watch` with frame extraction (override the >10-min skip; `--no-whisper`, native captions). `Read` the frames to transcribe the actual winning tweet.
2. **Capture a verbatim exemplar + the signature moves.** The real post = transformation headline w/ two hard numbers → enemy line → **invented proprietary mechanism** ("Drag Map") → before/strip/after → a **payload freebie of 3–5 richly-spec'd named deliverables** → mechanical CTA (comment + follow + RT). Wrote `references/real-post-teardowns.md` (the exemplar) + `references/voice-and-texture.md` (the 9 moves + a specificity gate).
3. **Install an embodiment gate in the workflows.** Post workflows now fail any draft that's a topic-headline, has no invented mechanism, offers a vague "guide" instead of a spec'd stack, or uses "a lot/quickly/results" where a number belongs.
4. **Compliant-grip rule.** Keep every move; move specificity off *money* onto *skills/outputs/time*. ("$493K→$1.8M" → "blank page → live storefront in 9 days.") Never strip the grip with the claims.
5. **Rewrite the applied output** (DWA posts/LP/lead-magnet) against the exemplar — invented mechanism ("the Faceless Skill Stack"), a 4-part spec'd Starter Kit, transformation-in-outputs.

## Dead Ends

- **Abstracting to "3 invariants."** Correct but toothless. Rules ≠ voice.
- **Transcript-only forge for a visual creator.** The whole point (his real posts) is on screen, not in the words. For any on-camera / screen-recording expert, watching is mandatory, not optional.
- **Compliance-by-blandness.** Stripping income claims is required; stripping specificity, mechanism, and payload is what actually killed the grip. Those are independent.
