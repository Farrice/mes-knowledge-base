---
name: youtube-screen-share-to-existing-skill-expansion
problem_signature: "A screen-share YouTube source needed to become a connected skill-system expansion without duplicating an existing expert, trusting transcript-only evidence, or crossing external-write boundaries."
domain: system
tags: [youtube, extraction, source-to-skill, visual-evidence, routing, negative-control]
date: 2026-08-30
status: active
session: "Extraction: YouTube Source - Build Skill System"
---

## Problem

A new practitioner video contained both spoken methodology and UI-level evidence. The repository already had the correct expert owner, but that skill explicitly lacked product-page coverage. A transcript-only extraction or a new parallel skill would either miss implementation truth or split routing authority.

## Root Cause

The transferable mechanism was distributed across captions, visible prompts, theme-editor state, mutation summaries, and first-pass defects. The default video downloader also stalled on YouTube's PO-token path, while repository-wide pointer/index generators could refresh unrelated files if their output was not scoped and reviewed.

## Approach That Worked

1. Capture native captions and selected screen-share frames with a proven `web_embedded` fallback; preserve spoken, visual, inferred, source-reported, and untested claims separately.
2. Run existing-coverage discovery before building, expand the named owner, write a Skill System Contract and Agentic Engineering Packet, then implement one conductor plus two component workflows.
3. Prove the failure path with an incomplete synthetic product: missing fit/material/policy evidence must produce `BLOCKED BY FACTS`, a claims veto, and `NO PERMISSION` rather than a plausible page.
4. Validate source intake, prompt structure, skill tier checks, command routing, expert routing, and negative controls; revert unrelated generator refreshes immediately.

## Dead Ends

- The default watch downloader entered a PO-token retry loop; repeated retries were stopped and replaced with the configured embedded-player fallback.
- A repository-wide prompt-pointer refresh touched five unrelated skills; those generated changes were restored before continuing.
- Initial natural-language routing favored generic sales/product routes until the new command descriptions carried the actual Shopify/apparel/customer-evidence vocabulary and BitBranding received a bounded curated router entry.

## Verification

- Video package verifier: PASS with 1,100 caption segments, 16,042 clean words, and 1,100 spoken-ledger rows.
- BitBranding skill heartbeat: 7/7 PASS.
- Renaissance prompt audit: 3,929/3,929 PASS.
- Cold-start verifier: PASS; unsupported claims and connector writes rejected.
- Natural-language routing: BitBranding and `/bb-pdp-rebuild` rank first for the intended query.
- Human blind comparison and live Shopify behavior remain untested.

## Weaker-Model Trap

A weaker model will summarize the transcript into a large prompt, declare the upload successful, or create a new “AI Shopify” skill. The correct move is to inspect the screen, extend the existing owner, preserve the questions/approval/state boundaries, and make rejection behavior part of the proof.

## Pointers

- `extractions/video-context/fwv1l_kdW18/`
- `skills/bitbranding-fashion-shopify/references/pdp-rebuild-skill-system-contract.md`
- `skills/bitbranding-fashion-shopify/tests/verify_pdp_rebuild_system.py`
- `.agent/workflows/bb-pdp-rebuild.md`
