---
name: Blind-Pass Corpus From Login-Walled Platforms (X 402 → Playwright Public Snapshot → Own-Site Fallback)
problem_signature: extraction blind-pass corpus gate needs ≥2 verbatim published pieces, but the expert publishes on X/LinkedIn where WebFetch returns 402/login walls — the gate fails and the skill ships B-tier with an avoidable gap
domain: extraction
tags: [extraction, blind-pass, corpus, playwright, x-twitter, provenance]
date: 2026-07-21
status: active
session: paolo-trivellato-forge
---

## Problem

`blind_pass.py prepare` requires ≥2 provenance-verified verbatim published pieces in `extractions/<skill-dir>/reference-corpus/`. Modern LinkedIn-economy experts publish on X and LinkedIn: WebFetch on `x.com/<user>/status/<id>` returns **HTTP 402**; LinkedIn posts and the X profile timeline are login-walled. Naive path: give up, ship B-tier "A-tier awaits blind pass."

## Approach That Worked (~5 min, $0)

1. **WebSearch first** — `"<expert name> <brand> <topic>"` surfaces direct status URLs (search snippets even preview the opening text, confirming which posts are long-form text, not video).
2. **Playwright on the STATUS URL, not the profile** — single public tweet pages render logged-out; `browser_navigate` + snapshot → the full tweet text sits in the accessibility-tree YAML (`.playwright-mcp/page-*.yml`), extract with a 5-line Python slice. The **profile timeline** does NOT render logged-out (infinite loading spinner) — don't waste time there.
3. **Expert's own website as piece #2** — sales-page copy is verbatim published writing by the expert, fetchable with plain WebFetch, and often corroborates case-study claims from video sources (here: Kyle Hunt listed as Starborn Case Study 04). Add a provenance line noting any marketing-copy tensions (e.g. "last decade" bio vs stated age) so the corpus stays honest.
4. Corpus files: provenance line on top (URL + post date + capture date + capture method + engagement stats), then verbatim text → `blind_pass.py prepare` passes.

## Key Detail

The corpus dir must be named after the **skill dir**, not the expert slug: `extractions/paolo-trivellato-lead-magnet-engine/reference-corpus/`, even when the extraction report lives at `extractions/paolo-trivellato/`.

## Dead Ends

- WebFetch on any `x.com` URL → 402 Payment Required, always.
- Playwright on the X **profile** page → login-gated skeleton, loading spinner, no posts.
- Video-frame screenshots of posts (JPEGs) → gate requires non-empty .md/.txt verbatim text, not images.
