# Fetch Notes — Persuasive Patterns (full 55-pattern library)
- Source: https://jumpy-oregano-409.notion.site/Persuasive-Patterns-Jason-Fladlien-38abc67d4986803b93c8d8dc22ddf656 (public share given by Fladlien via Instagram DM to Farrice)
- Fetched 2026-07-23 via Notion public api/v3 (loadCachedPageChunk + queryCollection + per-row loadCachedPageChunk), after Playwright confirmed the page renders publicly.
- Actual contents: 56 database rows across 10 categories (page intro says "55 patterns"; video said 8 categories — actual taxonomy is 10: Building Block, Commitment, Constraints, Contrast, Elicitation, Future Pacing, Identity, Linking, Reframe, Resource).
- Each pattern page: Structure template, Examples list, multi-section "Why It Works" mechanics. ~28k words of body documentation.
- Raw per-page JSON was fetched to scratchpad only (re-fetchable); rows.json here carries all row properties + block ids.

## Correction (same day, verification pass)
First fetch ignored loadCachedPageChunk's `cursor` pagination → 332 block refs missing (~12k words, all 54 tables) while LOOKING complete. Re-fetched with full cursor-follow: 0 missing refs; body corpus = 39,608 words + 494 table rows. Notion rebuild v1 archived; v2 migrated complete with native table blocks. Deployed Notion copy: Knowledge Vault → "Persuasive Patterns | Jason Fladlien — Full 56-Pattern Library" (child DB 3a649875-a897-81e7-a1d1-f5ebe5675c2f).
