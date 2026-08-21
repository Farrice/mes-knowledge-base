# Solution Card — Reddit thread data via Playwright in-page JSON fetch

**Date**: 2026-08-21 · **Context**: live verification of the Vosler language-bank quotes (supplement-founder mining run)

## Problem
Reddit is unreachable by the light tools: `WebFetch` returns "unable to fetch" on all reddit.com URLs (datacenter-IP block), the Claude in-app browser pane blocks reddit.com **by policy**, `curl` gets 403 on old.reddit.com, and search engines don't index comment-level text (exact-phrase WebSearch on a 138-upvote comment returned nothing). Sessions were burning turns rediscovering this wall and doubting whether Reddit mining is possible at all.

## Solution (verified live 2026-08-21, $0)
The authenticated Playwright MCP (the user's own logged-in browser) reaches Reddit cleanly — and the JSON API is same-origin once a page is open:

1. `mcp__playwright__browser_navigate` → `https://www.reddit.com/r/<sub>/comments/<id>/` (the HTML page; loads fine).
2. `mcp__playwright__browser_evaluate` with an **async in-page fetch** — same-origin, so no CORS, and it rides the browser's real session:
   ```js
   async () => { const r = await fetch('/r/<sub>/comments/<id>/.json?limit=500',
     {headers:{accept:'application/json'}});
     const j = await r.json(); /* walk j[0] post + j[1] comment tree:
     node.data.body, node.data.ups, node.data.created_utc, node.data.replies */ }
   ```
3. Walk `data.children` + `data.replies.data.children` recursively for comments; `j[0].data.children[0].data` for the post (title, score, created_utc).

Proof: two mined quotes re-verified word-for-word this way, with live scores and dates (one had gained 5 upvotes since capture — drift confirming live data both times).

## Gotchas
- Do **not** navigate directly to the `.json` URL — a concurrent process or viewer reset can blank the page between navigate and evaluate; navigate to the HTML thread, then fetch JSON from inside it (one round-trip, atomic enough).
- The shared Playwright browser is a contended resource: another session can navigate it away mid-run (observed twice). Keep navigate→evaluate adjacent; retry once on `about:blank`.
- Sort discipline for mining: append `?sort=top` to HTML URLs / use ranked search — never `new` (Vosler ranking-lens rule).
- Respect read-only Tier 1 (browser-automation-safety.md): navigate/evaluate only, never posting.

## Where this is wired
- `execution/surface_router.py` → `route "reddit thread comments"` prints this chain.
- `directives/browser-automation-routing.md` § Known Walls.
- Consumed by: sean-vosler workflow 02 (research-arbitrage miners), any community-mining dispatch.
