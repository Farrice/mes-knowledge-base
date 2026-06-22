---
description: Phase 1 Step 3 of the Customer Truth Map — the WIRED collection step. Pulls raw, unedited verbatim customer language down the full fallback chain (Apify Reddit → NotebookLM → Playwright → WebFetch → research.py → manual paste) plus own-data ingest, keeps every source tag and permalink, honors the cost gate, and outputs one raw corpus ready for /ctm-clean.
---

# /ctm-gather — Collect the Raw Language (Wired)

Phase 1, Step 3. This is where words become gold. It takes the source map from `/ctm-scope` and **collects raw, unedited customer language** — typos and all — from where people already talk, down a real, budgeted fallback chain. It collects only; it does not clean, sort, or paraphrase (those are `/ctm-clean` and `/ctm-map`). The output is one raw corpus with source tags + permalinks, ready to hand to `/ctm-clean`. Full wiring: [../references/tool-wiring.md](../references/tool-wiring.md).

## Pre-Flight Gate

Load `../genius.md` if not hot. Answer before collecting (Decision Framework, genius.md):

1. **Real sources named?** `/ctm-scope` produced specific communities/threads/own-data with capture tools — not "the internet." If the source map is missing, run `/ctm-scope` first.
2. **Do we already hold this language?** Confirm Layer-0 grounding (memory + Recall) ran in `/ctm-scope` — don't pay to re-scrape what we already have.
3. **Verbatim discipline armed?** We capture word-for-word. No tool here is allowed to summarize or invent a quote; collection and organization are two different jobs and this is collection only (genius.md, Pattern 1).
4. **Own data weighted first?** *"Your past conversations are often the single best source"* (genius.md) — sales calls, support, DMs, reviews of your product *and* competitors'. Ingest these before spending a cent on scraping.
5. **Honest about the tools?** Most chat tools can't reliably bulk-scrape Reddit; manual paste always works and is the floor. State the real limit; never pretend a tool returned more than it did (genius.md, Pattern 12).

## Skill Acquisition

- **Always:** `../genius.md` (words-as-gold/AI-as-sorter, keep-the-typos, honest-about-the-tools) + [../references/tool-wiring.md](../references/tool-wiring.md) Layers 0–1 (the gather core, fallback chain, budgets) + the verbatim rule from P3 ([../references/prompt-library.md](../references/prompt-library.md)).
- **Scale:** `/buyer-sourcer` (skills/luke-iha-avatar-machine) — delegate the whole mine for source-traced VoC at scale, then run `/ctm-clean` on the returns.
- **Browser safety:** `directives/browser-automation-safety.md` (read-only Tier-1 Playwright only).
- **Hands off to:** `./ctm-clean.md` (verbatim extraction on the corpus this produces).

## Execution

Collect down the fallback chain. **Each step's failure falls through to the next; manual paste is the floor — never block the map on a tool.** Keep the raw text exactly as written (typos, slang, ALL CAPS — the ungrammatical phrasing carries the selling power, genius.md Pattern 3), and tag every captured block `> "raw text" — [source, date/permalink]`.

> **Honesty note:** every quote shown below is `[illustrative]` to show the *capture shape* only. **Real runs keep only the actual harvested text** — word-for-word from the source, with a working permalink. Nothing here is invented; if a real run can't find a line, it isn't written.

### Step 0 — Own-data ingest FIRST (free, richest, often best)
Before any paid call, pull what you already own. Read sales/discovery-call transcripts, support tickets/emails, DMs, and reviews of your product *and competitors'* from files the user provides (Read/Glob). Treat exactly like scraped text in `/ctm-clean`. This is free, the person was talking directly about your space, and most people skip it.
- Worked: `> "I just kept hoping they'd send the next project so I never had to go looking for anyone new."` — [discovery-call transcript, 2026-05-12] `[illustrative]`

### Step 1 — Reddit / forums via Apify (primary, budget-gated)
**Mandatory pre-check, then the pull:**
```bash
python3 execution/apify_client.py budget-status
python3 execution/apify_client.py reddit "<keyword phrase>" --limit 50 --comments
python3 execution/apify_client.py reddit --subreddit Bookkeeping --limit 50 --comments
```
- **Cost-gate honesty (non-negotiable):** Apify is $29/mo, ~$0.001/result (~$0.05 for 50 posts+comments — cheap, but still cost-gated). The PreToolUse hook hard-blocks until approved. **Surface the projected number first, get an explicit yes, then run. Never retry a denied call** — surface it to Farrice instead.
- **Check `.fallback`:** on exhaustion the client returns `{"status":"budget_exhausted","fallback":true}` → drop to Step 2.
- Loop guards: max 5 calls/task, dedupe, keep the raw JSON. Each comment is verbatim customer language with a permalink → ideal source tag.

### Step 2 — Reddit + forums via NotebookLM (the expert's pick; grounded, cited)
```bash
python3 execution/notebooklm_client.py query <notebook-id> "<query>"   # ONLY subcommand that runs from CLI
```
- **CLI note:** the CLI guard requires 4+ argv, so only `query <notebook-id> "<query>"` runs from the command line. `list`, `budget`, and `search` trip the guard and exit 1 — to list notebooks or check budget, use the `/query-notebook` + `/add-notebook` skills or the NotebookLM MCP.
- Budget: 100 queries/mo (soft-warn 80, hard-stop 100); per-task cap 5; 7-day cache. Collapse multi-part asks into one query (~66% saving).
- Why it shines: NotebookLM reaches forums better than most tools and **cites the exact lines it pulled, so it won't invent a quote** — but only from sources you hand it. Add the specific threads/review pages first (web links or pasted text); new notebook → `/add-notebook`.

### Step 3 — Login-gated / JS-rendered communities via Playwright (read-only, Tier 1)
```
mcp__playwright__browser_navigate  { "url": "<thread or review page>" }
mcp__playwright__browser_snapshot  {}
mcp__playwright__browser_evaluate  { "function": "() => document.body.innerText" }
```
Read-only navigate/snapshot/evaluate are Tier-1 (no confirmation). **Never enter credentials; never take state-changing actions while gathering** (`directives/browser-automation-safety.md`). Use only when WebFetch returns an empty SPA shell.

### Step 4 — Static review/blog/SEO pages via WebFetch (free, fast)
`WebFetch` plain HTML review/blog pages (<1s). Falls through to Playwright (Step 3) for JS-heavy SPAs.

### Step 5 — Broad signal / triangulation via research engine (free→budgeted)
```bash
python3 execution/research.py "<voice-of-customer query>" --depth standard --json
```
Gemini-primary → Perplexity ($30/mo, cost-gated) → Bedrock floor. Carries an honest receipt of what fired/failed/cost. Use to *find where they talk* and to triangulate — **not** as a quote source unless it returns verbatim lines with citations.

### Step 6 — Manual paste (the floor — always works)
When every tool above stalls or a community is closed, the user pastes raw blocks directly. State this honestly rather than pretending a scraper covered it. Tag each pasted block with its source.

### Optional — delegate the whole mine at scale
For heavy, source-traced VoC across many communities, hand the source map to **`/buyer-sourcer`** (Perplexity + Playwright + Apify, ≥15 source URLs, auto-fails on modeled claims), then run `/ctm-clean` on what it returns. Don't reimplement scaled mining here.

**State the chain in the run:** Apify → NotebookLM → Playwright → WebFetch → research.py → manual paste. Log which fired, why, and what it cost (honest receipt). A step that returned nothing is reported as nothing, not padded.

## Content-Type Adaptations

The capture tool follows the *source type*, not the deliverable (full key: [../references/cross-domain-adaptations.md](../references/cross-domain-adaptations.md)):

| Source type | Primary tool | Fallback |
|---|---|---|
| **Public subreddit / forum** | Apify reddit actor (budget-gated) | NotebookLM → manual paste |
| **Login-gated FB group / Discord / Slack** | Playwright (read-only) | manual paste |
| **Review sites (G2/Capterra/Amazon/Yelp)** | WebFetch | Playwright (if SPA) → manual paste |
| **YouTube comments** | manual paste / `fetch-video-context.py` | — |
| **Own data (calls, support, DMs, reviews)** | Read/Glob on user files | manual paste |
| **"Where do they even talk?" still unclear** | research.py (find sources) | then re-run `/ctm-scope` |

## Output Requirements

Return:
1. **The raw corpus** — one collection of unedited, verbatim customer language, typos preserved, each block tagged `> "raw text" — [source, date/permalink]`. No cleaning, sorting, or paraphrase — that is `/ctm-clean`'s job.
2. **The gather receipt** — the fallback chain as run: which tools fired, which fell through (and why), source counts per tool, and the total spend (with any cost-gate pause surfaced for approval). A denied paid call is reported as denied, never retried.
3. **A coverage note** — which scoped sources were captured vs still pending, and which are own-data vs scraped.

Hand the corpus to `./ctm-clean.md`.

## Quality Gate

Score against the `../genius.md` rubric (1–10; name the anchor for ≥8). The criteria this phase owns:
- **Verbatim Integrity** — every captured block is the source's *actual* words with a working permalink/tag; nothing summarized at capture.
- **Unprompted Sourcing** — the corpus is mostly unsolicited talk (reviews/threads/DMs/own-data), not survey answers.
- **Honest tooling** — the receipt states the real fallback chain truthfully; no tool's output is exaggerated, no denied call retried.

**Verbatim-Integrity veto (non-negotiable).** This is the step most tempted to "fill gaps" with plausible-sounding language. Do not. A single invented or paraphrased line entering the corpus is an **automatic fail** — the customer's words are the gold; the tools only fetch them. If a source returned nothing, the corpus shows nothing for it. Real language in, or it doesn't go in.

**Self-check:** *Could a skeptic open every permalink and find each quote verbatim, and is the spend receipt honest about what fired?* If yes, hand to `/ctm-clean`. If no, the offending block is pulled before anything moves downstream.
