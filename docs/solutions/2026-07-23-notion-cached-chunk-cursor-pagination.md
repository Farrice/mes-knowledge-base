---
name: Notion loadCachedPageChunk Silently Paginates — Follow the Cursor or Lose 30%
problem_signature: a Notion public-api scrape (api/v3 loadCachedPageChunk) returns 200 with a plausible recordMap; content silently truncated ~100 blocks in — child refs missing from recordMap, tables/rows absent, no error anywhere
domain: scraping
tags: [notion, scraping, pagination, api-v3, verification]
date: 2026-07-23
status: active
session: fladlien-pattern-library-harvest
---

## Problem
Scraping Fladlien's 56-page pattern library via `POST /api/v3/loadCachedPageChunk` looked complete (200s, rich recordMaps, compiled to 27.7k words). It was 30% short: the response paginates via a `cursor` field; one call returns ~100 blocks per page and the tail is simply absent. 332 child block refs pointed at records not in the map, and ALL `table` blocks were among the losses. `syncRecordValues` as a patch-fetch is 403 on public sites — pagination is the only recovery path.

## Approach That Worked
1. **Completeness invariant, not vibes**: walk every `content` id recursively and count refs missing from the recordMap. >0 missing = the scrape is incomplete, period.
2. **Cursor-follow loop**: re-request with the returned `cursor` + incrementing `chunkNumber`, merging `recordMap.block` until `cursor.stack` is empty.
3. **Type coverage audit**: Counter over all block types BEFORE converting; any type not in the converter's map (here: `table`/`table_row`) is silent data loss — map it or fail loudly (`MISSING BLOCK` sentinel + assert), never skip.
4. Result: 27.7k → 39.6k words, +494 table rows, 0 missing refs.

## Dead Ends
- `syncRecordValues` for the missing ids → 403 unauthenticated on notion.site publics.
- Trusting "200 + big JSON" as done — the API gives zero signal that content remains.

## Deploy When
- Any api/v3 notion.site scrape (loadCachedPageChunk/loadPageChunk) — always cursor-loop + run the missing-ref invariant before compiling.
- Generally: any scrape feeding an extraction — a completeness invariant (refs resolve, types mapped) is part of the scrape, not optional QA.
