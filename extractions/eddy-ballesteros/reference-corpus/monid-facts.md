# Monid AI — facts captured from the video + site (2026-08-05)

All items frame-cited from PmvqIaLC6AY unless marked WEB (from monid.ai search results, 2026-08-05).

## What it is
- "The OpenRouter for AI agents" (Eddy's framing, t=01:52) — universal API key: one connection, one wallet, agent discovers tools, checks price, executes, pays per call (t=02:04, 08:50).
- Scale claims on-screen/in-script: "Live · 1500+ tools" (homepage, t=01:54); script doc says "a single balance and one registry of over a thousand tools across thirteen-plus providers… pays per call. from about a tenth of a cent each" (t=02:02 doc).
- Connected to **Apify** under the hood for scraping endpoints (t=04:19 "because there's connected to ampify" [caption garble for Apify]).
- Data sources demonstrated: Semrush keyword metrics, Reddit (posts + community sizes, time-windowed), X/Twitter, YouTube, web search (t=06:09–06:24). WEB: catalog also lists TikTok, LinkedIn, Instagram, Amazon, Google Reviews, blockchain.

## Setup (three surfaces)
- **claude.ai** (t=03:37–04:06 + step cards t=13:54): Settings → Connectors → Add custom connector → name "Monid" → paste MCP URL **`https://mcp.monid.ai/v1`** → Add → log in/authorize (opens Monid login; Allow). New accounts get **$1 free credit — "hundreds of calls"**.
- **Agent-native/skill** (homepage, t=01:54): give the agent `set up https://monid.ai/SKILL.md` and "let it take it from there". WEB: docs at docs.monid.ai, quickstart-skill guide; install.sh exists.
- Dashboard: app.monid.ai (t=02:59).

## Costs (receipts)
- Eddy's full AI SEO research report: **$0.03** (t=06:04).
- Per-call floor: ~$0.001 ("about a tenth of a cent each", script doc).
- Signup credit: $1 free (t=13:54 step 3).
- Implication for our caps: $5/run default ≈ 150+ full reports of Eddy's size — the cap is a runaway-guard, not a constraint.

## Test prompt he recommends (t=13:12)
"Find the latest posts about [your topic] using Monid MCP" — Claude discovers tools, runs, returns live results.

## Not sponsored
Eddy states not sponsored, not an affiliate (t=02:25–02:30).
