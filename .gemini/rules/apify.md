# Apify Scraping & Social Listening — Tool Available

You have access to **Apify** for scraping, social listening, and structured data extraction. Use it when a task needs raw data from sites that generic web search can't reach (Reddit threads, Instagram posts, TikTok hashtags, YouTube transcripts, Amazon products, Google Maps places).

Apify is exposed via a Python CLI wrapper. There is no MCP server for you (Gemini Antigravity doesn't support MCP) — you call it via Bash:

```bash
python execution/apify_client.py <command> [args]
```

## Decision: When to Use Apify vs Other Tools

| Task type | Tool |
|---|---|
| Reddit threads, comments, sentiment | `apify_client.py reddit` |
| Instagram profile audits, hashtag analysis | `apify_client.py instagram` |
| TikTok hashtag scans, trend mining | `apify_client.py tiktok` |
| YouTube videos + transcripts (vlogs, day-in-life) | `apify_client.py youtube` |
| Amazon products, reviews, Best Sellers | `apify_client.py amazon` |
| Google Maps places, local businesses | `apify_client.py maps` |
| JS-rendered page that `read_url_content` chokes on | `apify_client.py web <url>` |
| **Synthesis, Q&A, citations from web** | **Perplexity** (`perplexity_client.py`) — NOT Apify |
| **Quick factual lookups** | Tavily / web search — NOT Apify |
| **Extracting from already-known good URLs** | `read_url_content` — NOT Apify |

**Rule of thumb**: Apify pulls raw structured data. Perplexity synthesizes meaning. Use Apify → Perplexity as a pipeline, not as competitors.

## The 7 Approved Actors

Only these 7 actors are wired up. Anything else requires editing `execution/apify_client.py`:

- `reddit` (cheap) — Reddit posts/comments
- `instagram` (cheap) — IG profiles and posts
- `tiktok` (medium) — TikTok hashtags
- `youtube` (medium) — YouTube + transcripts
- `amazon` (cheap-medium) — Amazon products
- `maps` (medium) — Google Maps places
- `web` (cheap) — JS-rendered page fetch

## Examples

```bash
# Reddit deep dive on first-time home buyers
python execution/apify_client.py reddit "first time home buyer california" --limit 50 --comments

# Pull a specific subreddit
python execution/apify_client.py reddit --subreddit FirstTimeHomeBuyer --limit 30

# Instagram profile audit
python execution/apify_client.py instagram realestatewithjing --limit 20

# YouTube vlog transcripts
python execution/apify_client.py youtube "pilates day in the life" --limit 5 --transcript

# Amazon Best Sellers in a category
python execution/apify_client.py amazon --best-sellers --limit 30

# Google Maps local businesses
python execution/apify_client.py maps "yoga studio" --location "Sherman Oaks CA" --limit 30

# Generic JS-rendered web fetch
python execution/apify_client.py web "https://example.com"
```

## Budget Awareness — Critical

Every Apify call costs money against the user's $29/month plan. Before any **expensive** run (>0.5 CU = >$0.15), check budget:

```bash
python execution/apify_client.py budget-status
```

The wrapper enforces a hard 90% cap automatically. **You do not need to enforce it yourself.** But you do need to handle the response:

## Fallback Contract (READ THIS)

Every Apify call returns JSON. If the response contains:

```json
{"status": "budget_exhausted", "fallback": true, ...}
```

…then **do not retry the Apify call**. Instead, route the same research need to:

1. **First fallback**: Perplexity (`perplexity_client.py` or via the `perplexity-ask` MCP)
2. **Second fallback**: Tavily search (`tavily-search` skill)
3. **Third fallback**: Generic `read_url_content` / web search

The wrapper will NEVER raise an exception on budget exhaustion. It always returns a structured response. Workflows must check `.fallback` and reroute. This is what keeps workflows from breaking when the cap is hit.

## Cost Reference (so you can budget intelligently)

- Reddit deep dive (50 posts): ~$0.05
- Instagram audit (20 posts): ~$0.01
- TikTok scan (50 posts): ~$0.20
- YouTube transcript (5 videos): ~$0.025
- Amazon scrape (30 products): ~$0.045
- Google Maps (30 places): ~$0.21
- Web fetch (1 page): ~$0.003

**Monthly budget**: $29.00. Soft warn at $20.30 (70%). Hard stop at $26.10 (90%).

**Tracking file**: `.agent/apify-usage.json`

**Full policy**: `directives/apify-usage-policy.md`
