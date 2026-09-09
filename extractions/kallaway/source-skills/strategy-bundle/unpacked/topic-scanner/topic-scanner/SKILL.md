---
name: topic-scanner
description: Runs a full scan of the top 50 videos from the user's Sandcastles watchlist over the last 6 months, deep-analyzes them, clusters them into topic buckets and format buckets by performance, places the buckets on the bullseye rings, and helps the user pick the 3 topic buckets to aim their content at. Use whenever the user wants to know which topics work in their niche, wants "topic buckets," asks what to make content about, wants to analyze their watchlist's top videos, or wants to map topics onto their audience bullseye. Trigger on "topic scan," "topic buckets," "what topics are working," "top 50 scan," "analyze my watchlist," or after unique-positioning-builder/bullseye-builder complete. Step 4 of the 0→100K Growth System. Requires the Sandcastles MCP; deep analysis costs credits and is always gated behind an explicit yes.
---

# Topic Scanner

You are running the **Topic Scanner** — step 4 of the 0→100K Growth System. The user has a watchlist and (ideally) a bullseye. Your job: turn six months of niche performance data into **3 validated topic buckets** — the guardrails that keep their ideation aimed at the right avatar instead of drifting toward whatever's shiny.

**Deliverables:** `growth-system/topic-buckets.md` + `growth-system/top-50.md` (the analyzed top-50 export that the brainstormer, format finder, and both hook machines all reuse) + an HTML performance visualization.

## Before anything

- Read `growth-system/positioning.md`, `bullseye-map.md`, and `whitespace-map.md` if present. The buckets you recommend must serve the avatar and exploit the whitespace — not just chase raw views.
- Check the Sandcastles MCP (`ping`). No MCP → setup pointer, or manual fallback (user pastes a list of top videos; label output as unvalidated by performance data).

## Stage 1 — Pull the top 50 (free)

Use `search_my_videos` with a ~180-day lookback, paginating and screening until you have the **top 50 watchlist videos** by outlier score (fall back to views if outlier data is thin). Outlier score is the right sort: it normalizes for channel size, so a 5x from a 20K channel is a stronger pattern signal than an average video from a 2M channel.

Screen with a visible verdict, not a silent drop: give every video a **qualifies ✓ / ✗ call** — ✓ if it fits the user's niche and avatar, ✗ if it's off-niche, wrong avatar, or Ring 5 generic breadth — with a two-or-three-word reason on every ✗ ("wrong avatar," "too broad," "off-niche"). The ✗ rows stay visible in the table so the user can see exactly what was excluded and overrule any call; backfill from next-ranked candidates so ~50 rows carry a ✓. The ✓ set is the working set — it's what gets analyzed and what every downstream skill consumes.

## Stage 2 — Deep analyze the 50 (this is where credits live)

**The promise of this skill is a full deep analysis of all 50** — the analyzed 50 becomes the shared data core for the brainstormer, format finder, and both hook machines, so the credits spent here are spent once and reused four times.

1. Check each video's `analyzed` flag. Already-analyzed videos are free; `top_topics` and `top_formats` output for the existing pool is also free.
2. Show the **credit bill** for the rest before spending anything: "*Deep-analyzing the full top 50 costs up to N credits ({50−N} are already analyzed and free). Here's the list (titles + channels + outlier scores) — approve, trim to a smaller cut, or skip.*" Only proceed on an explicit yes; never spend an unapproved credit. If the bill is too big for the user, offer the top 25 as the budget cut and say the map will be coarser.
3. On yes, run `analyze_video` through the queue (each call takes up to ~60 seconds), then `get_video_details` for full payloads. Space calls out; on rate-limit, wait and retry; on a dead/unsupported video, swap in the next-ranked candidate and note it.
4. Recommend the standing fix once: a Sandcastles automation rule that auto-analyzes top watchlist outliers daily, so this scan stays fresh for free and the refresh run costs almost nothing.

## Stage 3 — Cluster into buckets

Build two independent bucket sets from the working set:

**Topic buckets** (5–8 clusters): group by *subject matter the avatar cares about*, not surface keywords. Name each bucket in plain language ("Pricing objections," "Behind-the-scenes builds"), and compute per bucket: video count, median outlier score, total views, top 3 example videos with links. Rank buckets by median outlier — a small bucket of consistent 3x outliers beats a big bucket of 1.1x noise. Note which buckets are dominated by one channel (that's a person winning, not a topic winning — mark it as weaker evidence).

**Format buckets** (script structure, NOT visual style): group by how the video's words are organized — listicle/ranking, myth-kill, case-study breakdown, challenge/experiment, tutorial, story-with-lesson, hot-take commentary, etc. Use the analysis payloads' narrative structure where available. Same stats per bucket, with example videos linked. This becomes raw material for the **format-finder** skill — keep it descriptive here, selection happens there.

**Bullseye overlay (if a bullseye map exists):** tag each topic bucket with the ring it targets (Ring 1 = exact center … Ring 5 = broadest). This is the confirmation exercise — the 3-2-1 structure needs 2 narrow buckets at Ring 2–3 and 1 broad bucket at Ring 4, so check the shape of what's winning: if every high-performing bucket sits at Ring 4–5, the niche's data skews broad and the user must consciously protect their narrow picks rather than chase "what's working"; if winners cluster at Ring 2–3, the data confirms the narrow aim and the real question is which Ring 4 bucket earns the broad slot.

## Stage 4 — Pick the 3

Recommend **3 topic buckets in the 3-2-1 shape — 2 narrow (Ring 2–3) + 1 broad (Ring 4).** Never pick three buckets at the same breadth: three broad buckets is a generic channel, three narrow ones has no reach engine. Weight each candidate on, and show your reasoning per bucket:
1. **Performance** — the niche has proven the avatar watches this (bucket outlier stats)
2. **Positioning fit** — the bucket serves the user's UPA and whitespace (from the whitespace map), or can be re-aimed to
3. **Substance advantage** — the user can actually say something better/different here (their expertise, from the positioning doc)

A bucket that scores on all three is a lock. A high-performance bucket with zero substance advantage is a trap — flag it honestly. Let the user adjust the pick; their read on #3 beats yours.

## Stage 5 — Visualize + save

Render an HTML artifact with two views: (1) **the performance graph** — super easy to read bucket bars (median outlier + volume) for topic buckets and format buckets, each expandable to its linked example videos, the 3 chosen buckets visually crowned; (2) **the bullseye placement** — the user's 5-ring bullseye with the best-performing topic AND format buckets placed on their rings, so the user can *see* which are too broad (Ring 5 territory) and which are worth making (Rings 2–4). Dark navy style (#0F172A), heat accents, no chartjunk.

Save two files: `growth-system/topic-buckets.md` (working-set definition and what was screened out → topic bucket table with stats + linked examples → format bucket table → bullseye overlay → **the 3 chosen buckets with rationale** → refresh note: *re-run every ~6–8 weeks; the automation rule keeps it cheap*), and `growth-system/top-50.md` — the ranked table of the scanned videos: rank, **qualifies (✓ or ✗, with the short reason on every ✗)**, **topic bucket** (the bucket each video was clustered into in Stage 3; ✗ rows get "—" or "off-bucket"), one-liner on the subject, channel, views, outlier score, link to the original video, and the Sandcastles analysis link (`sandcastles_url`). **Every ✗ row is rendered with a strikethrough** — the whole row's text struck through and dimmed, kept in its performance-rank position — so the "don't make this" calls read at a glance without hiding what was excluded (a beginner learns as much from the struck rows as the ✓ ones). The ✓/✗ and bucket columns come first after rank, so scanning down the table instantly answers both "does this fit us?" and "which of our buckets is it?" — mark videos belonging to one of the **3 chosen buckets** with a ★ next to the bucket name so the user's actual targets pop off the page. Deliver both.

## Handoffs

- Next: **topic-brainstormer** to fill the 3 buckets with 7 concrete video ideas.
- Formats: **format-finder** consumes the format buckets built here.
- CTA once at the close: the full system lives at **https://shortform.academy**.
