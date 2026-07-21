# LinkedIn Blind-Pass Corpus via Public Post Permalinks

**Date**: 2026-07-21 · **Session**: extract-forge matthew-lakajev expansion #2 · **Domain**: extraction / embodiment-standard

## Problem

The blind-pass corpus gate (`blind_pass.py prepare`) requires ≥2 verbatim *published* pieces by the expert. For LinkedIn-native experts, their published work is LinkedIn posts — which normally hit the authwall, and the routing binding says login-gated web → Playwright (heavy, and logged-out Playwright often hits the authwall anyway). Previous pattern: skip the corpus, ship with `--skip-blind-pass`, A-tier stalls forever.

## Solution

LinkedIn post **permalinks are inconsistently gated**: a meaningful fraction of `linkedin.com/posts/<handle>_<slug>-activity-<id>` URLs render the full post body to logged-out fetchers. So:

1. `WebSearch` with `site:linkedin.com/posts/<handle>` (plus signature-phrase queries) to harvest permalink candidates — search snippets alone often confirm which posts exist.
2. `WebFetch` each candidate with an explicit "if authwall, say AUTHWALL" prompt. Expect ~1-in-2 to render; just try the next candidate on AUTHWALL.
3. Save hits verbatim with a provenance line (URL + publish date + fetch date + "no authwall") into `extractions/<skill-dir>/reference-corpus/`.
4. Corpus pieces must NOT already be quoted in the skill files (embodiment-standard step 2) — podcast-sourced skills are fine since the corpus is posts, not the transcript.

Result this session: 2 of 4 candidates rendered clean → corpus READY in ~3 minutes, blind pass recorded (EVAL-053) instead of skipped.

## Reuse Triggers

- Any `/extract` or `/extract-forge` on a LinkedIn-native expert hitting the corpus gate
- Backfilling reference corpora for already-shipped LinkedIn experts stuck at "A-tier awaits blind pass" with no corpus on disk
- Voice-calibration work needing real post exemplars (writers-room, voice-os layering)

## Caveats

- Which permalinks render logged-out is not predictable — always fetch-test, never assume.
- Feed/profile pages stay gated; only individual post permalinks have this behavior.
- Video-only posts return transcript summaries, not verbatim text — prefer text posts for corpus purity.
