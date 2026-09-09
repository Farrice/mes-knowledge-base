---
name: jen-content-intelligence-archive
problem_signature: "Build a budget-capped, resumable Instagram archive that separates private evidence from curated story intelligence and survives provider gaps."
domain: system
tags: [instagram, monid, archive, content-intelligence, privacy, budget]
date: 2026-09-03
status: active
session: "Content: Jen Intelligence Bank - Archive and Story System"
---

## Problem

A 2,780-post Instagram history needed to become a reusable, source-traced story
bank without exposing client details, double-charging on resume, or calling an
incomplete scrape complete.

## Root Cause

The original Monid budget policy had drifted, provider error envelopes could be
misread as billable success, and a naive content classifier promoted keyword
matches into story truth. Media preservation also needed a terminal-with-gaps
state distinct from perfect download completeness.

## Approach That Worked

1. Put every paid page behind a quote, pending receipt, immutable raw envelope,
   query-bound cache key, checksum, cursor ledger, project cap, tranche cap, and
   process lock. Reconstruct spend from provider-reported cost.
2. Separate private source evidence from curated records; require stable IDs,
   exact evidence spans, privacy states, proof ceilings, and independent archive,
   story-truth, attention, and commercial-proof states.
3. Preserve all accessible thumbnails plus the selected top-200 source media,
   while recording operator waivers and coverage gaps explicitly.

## Dead Ends

- The v1 comment endpoint returned HTTP 400 with zero provider cost; a v2 canary
  worked, but the operator removed comments from scope before bulk extraction.
- Recursively collecting every Highlight URL also captured alternate renditions,
  music, and sticker assets. Highlights were later waived and those local media
  files were removed.
- Drive rejected large media archives over 100 MB; deterministic 95 MB parts plus
  a checksum manifest preserved recoverability.

## Verification

- `JEN CONTENT ARCHIVE: PASS (28 checks)`
- `MONID BUDGET GUARD: PASS (23 checks)`
- Cost hook self-test: `18 negatives, 10 positives`
- 2,779 unique accessible posts versus 2,780 profile-reported; one explicit gap
- 2,979 required media files preserved with zero unavailable
- Final bank: 200 entries, 50 deep packets, six candidate pillars, acceptance PASS
- Google Drive permission metadata verified both raw and curated folders as not shared

## Weaker-Model Trap

Do not equate a raw checksum with story truth, an engagement outlier with a lead,
a keyword with a Jen action, a 200-row bank with 200 publish-ready stories, or an
exhausted accessible cursor with exact equality to Instagram's profile count.

## Pointers

- `execution/jen_content_archive.py`
- `execution/verify_jen_content_archive.py`
- `execution/verify_monid_budget_guard.py`
- `_active/clients/jen-listings/06-system/content-intelligence/`
- Private archive folder: `1Bx5eVp8AOCq6eTaW9nbMyCzrMaYErNIc`
- Curated folder: `16n35G9_-FRRr46fUEj98LHoFjv6NvT9J`
