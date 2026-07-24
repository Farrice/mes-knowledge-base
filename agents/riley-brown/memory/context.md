# Riley Brown — Agent Memory

## Provenance
- Extracted 2026-07-24 from 3 verified Riley Brown videos + 100-frame visual layer (`extractions/riley-brown/`). Deep-tier MES 3.0. Fidelity: full.
- This build **corrected** an earlier same-day draft (Codex-side, b492479ad) written from only the first half of the transcript. Fabrications killed: invented API pricing ($10-50/creator, $175-458/mo Foreplay, $0.10/page Firecrawl), invented endpoints (`api.foreplay.co`, `api.scrapecreators.com`), a fabricated engagement formula (likes+2×comments+5×shares), and placeholder timestamps. See `references/source-quotes.md` § "What the Source Does NOT Establish."

## Load-Bearing Truths (never re-litigate)
- **Content-verification gap** is the master key: code is verifiable, content isn't → retrieve exemplars, don't prompt harder.
- **Taste is non-delegable**: only delegate what you can judge.
- **Never auto-send**: every action ends in an editable draft/link behind approval.
- **The durable asset is a named skill**, born from a successful run — and it may be real code; open and read it.
- **Ad duration = inference proxy, never ROAS proof.** Meta Ad Library exposes no likes/spend/ROI for commercial ads — leave blank, never fabricate.
- **Never carry a real byline/person into a template-steal** (the "Dr. Fahim Hussain" failure Riley missed).

## Our-Stack Binding (critical)
- Riley's tools are all *paid third-party*; **we hold none of those keys.** Every workflow routes through our own infra at $0 + Apify cents: `/scrape-creator`, `/ad-spy`, `/creative-from-winners`, `/brand-asset-scrape`, `/inbox-drafts`, `/post-scheduler`, `/scheduling-links`. Social Intelligence Notion DB `3a749875-a897-8104-a867-fc9aeb53f52c` via `notion_api.py`.
- The only dollar figures Riley states: "$250 for nine [frontier] prompts", "$20/month plan". Both about model spend, not scrapers.

## Open Threads
- No structure-pure v2 prompts forged yet — prompt-forging backfill covers it (`directives/prompt-forging-spec.md`); do not invent ad hoc.
- A-tier pass awaits Farrice blind test against real Riley scripts.
- Front door + registry wiring run by main (sync_registries) — not this build.
