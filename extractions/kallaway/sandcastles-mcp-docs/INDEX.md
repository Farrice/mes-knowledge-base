# Sandcastles MCP Tool Docs — INDEX — captured 2026-08-27

Source: help.sandcastles.ai (Notion knowledge base, Category: MCP, pages last updated 2026-08-09). All 10 pages captured successfully. Credit costs are NOT stated on any individual tool page; the only credit signal in the docs is `/channels-recap` ranking videos "by ROI on your credits" (deep video analysis consumes credits) and site-wide pricing FAQ language that analyzing a video or writing a script costs 1 credit each.

## analyze — `analyze.md`
- What: deep analysis of a single short-form video (YouTube Shorts, Instagram, TikTok) — transcript, hook breakdown, format, narrative beats with timestamps, topic/angle/substance, meta-pattern. Bulk analyze supported via pasted URL lists.
- Inputs: `/analyze <video URL>` plus optional refining prompt (e.g. "full details including transcript, format analysis, hook breakdown").
- Outputs/fields: performance metrics (views, likes, comments, outlier score, engagement rate, post date), transcript, hook (category/formula/effectiveness), format (category/type/flavor/visual layout), why-format-works, narrative structure beats, topic/angle/substance, meta-pattern, sources.

## channels-add — `channels-add.md`
- What: adds an Instagram, TikTok, or YouTube channel to your watchlist, either by URL or from channels mentioned in the current chat.
- Inputs: `/channels-add <channel URL>` (or bare `/channels-add` to pick from conversation).
- Outputs/fields: confirmation with channel name + platform, counts for Added / Submitted as new / Skipped, and updated watchlist total.

## channels-recap — `channels-recap.md`
- What: recap of a specific creator's recent content performance over a chosen window (30/90 days, up to a year), surfacing what's winning and patterns.
- Inputs: `/channels-recap <channel URL>` plus free-form questions (timeframe, synthesis of best topics/takes, flag un-analyzed videos).
- Outputs/fields: headline analysis (views, avg outlier score, followers), content focus, top performers, B-tier, un-analyzed videos, "Worth Analyzing (ranked by ROI on your credits)", pattern identification. Supports multi-channel and follow-up drill-downs (pillars, common hooks).

## channels-search — `channels-search.md`
- What: discovers channels from Sandcastles' curated database by criteria — topic/niche, similarity to a known channel, follower range, posting frequency. Aimed at brands/startups finding creators.
- Inputs: `/channels-search` + natural-language criteria (platform, follower band, min posts/month, vibe filters); refinable ("20 accounts similar to X, ranked, with profile links").
- Outputs/fields: ranked channel list with profile links for manual review.

## channels-suggest — `channels-suggest.md`
- What: suggests new creators based on your existing watchlist (similar audience demographics, content strategy, engagement patterns).
- Inputs: `/channels-suggest` + request (e.g. "best 5 channels 100K-250K on Instagram based on my marketing watchlist"); offers follow-up batches by follower band.
- Outputs/fields: username, follower count, total views, short content-strategy description per suggestion. Chains with `/channels-add` and `/video-suggest` for multi-step workflows in one prompt.

## topic — `topic.md`
- What: identifies highest-performing topics ("idea seeds," not broad categories) across your watchlist videos from the last 30 days, clustered into 3-5 working themes.
- Inputs: `/topics` + refining prompt (ranking basis, granularity, link videos per cluster).
- Outputs/fields: topic name, view counts, 2-3 example videos per theme, "Your fit" analysis (make-or-skip), actionable suggestions; can be turned into a refreshable live artifact.

## formats-watchlist — `formats-watchlist.md`
- What: distribution analysis of best-performing video formats across already-analyzed watchlist videos over a lookback window (e.g. 60 days), including sub-flavors within a format.
- Inputs: `/formats-watchlist` + request (window, visual report, per-format video links, sub-flavor breakout).
- Outputs/fields: data summary (video count, period), visualizations (Format Mix pie chart, Total Views by Format bars), ranked format breakdown (video count, total views, peak outliers), individual video links.

## hooks-watchlist — `hooks-watchlist.md`
- What: analyzes best-performing hooks from analyzed watchlist videos (default ~last 14 days), identifying named hook patterns and flagging un-analyzed outliers (e.g. >2x) for deeper analysis.
- Inputs: `/hooks-watchlist` + request (window, outlier threshold, format + link detail).
- Outputs/fields: top hook patterns (e.g. "Secret Reveal / Breakdown," "Scenario Hypothetical," "Receipts/Case Study") with examples, views + outlier scores, takeaways, un-analyzed outlier list (channel, title, views, outlier score). Caveats in doc: visual hook + text hook work together; hooks are platform-specific; 14-day default window.

## video-suggest — `video-suggest.md`
- What: ranked recommendations for what video to make next, based on top performers in your watchlist/niche and current trends.
- Inputs: `/video-suggest` + optional prompt ("What should I make today?", niche context for better tailoring).
- Outputs/fields: ranked idea list with supporting research/data points; doc suggests running it regularly or via automations to keep an idea pipeline.

## videos-watchlist — `videos-watchlist.md`
- What: pulls top-performing videos from your watchlist with custom filters (window, min engagement rate, exclude boosted entries).
- Inputs: `/videos-watchlist` + query (e.g. last 28 days, order by views, ER >2%, include link + creator).
- Outputs/fields: ranked list — creator handle, views, engagement rate, title, direct video link; flags videos not yet deep-analyzed for follow-up hook/format/narrative analysis.

## Capture notes
- All pages are JS-rendered Notion pages; two required a retry (channels-search rendered a 404 fallback on first load; formats-watchlist flashed the marketing homepage on first load — both captured cleanly on second navigation).
