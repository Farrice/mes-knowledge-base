# Tool Wiring — Customer Truth Map

The expert's original is **manual** (copy-paste, NotebookLM by hand). This is how we **surpass** it:
real tools wired into the gather/ground/verify steps, with budget gates and an honest fallback
chain. The honesty spine still rules — every tool here either returns *real* customer language or is
not used. **No tool is allowed to invent a quote.**

All commands run from the repo root (`/Users/farricecain/Google Antigravity`). Paid tools are
**cost-gated**: the PreToolUse hook hard-blocks until approved. Surface the projected cost, get an
explicit yes, then proceed. Never retry a denied call.

---

## Layer 0 — Ground before you scrape (free, always first)
Front-load what we already know so we don't re-gather. Run both:
```bash
python3 execution/memory_facade.py "<customer + problem>" --top 10
```
Unified recall across sovereign + automem + wiki + agents (degraded stores are reported, not
dropped). Plus **Recall** (3,000+ cards) via MCP:
```
mcp__recall__search   { "query": "<customer + problem>" }
mcp__recall__get_document_content   { "document_id": "<id>" }
```
Output feeds `/ctm-scope` P1 (tag each problem `[assumed]` vs `[evidenced: source]`).

---

## Layer 1 — Gather raw language (the wired core of /ctm-gather)
Try in this order; each step's failure falls through to the next. **Manual paste always works and is
the floor** — never block the map on a tool.

### 1a. Reddit / forums — Apify (primary, budget-gated)
```bash
python3 execution/apify_client.py budget-status            # MANDATORY pre-check
python3 execution/apify_client.py reddit "<keyword phrase>" --limit 50 --comments
python3 execution/apify_client.py reddit --subreddit FirstTimeHomeBuyer --limit 50 --comments
```
- Budget: **$29/mo**, soft-warn $20.30 (70%), hard-stop $26.10 (90%). Reddit ≈ **$0.001/result** →
  ~$0.05 for 50 posts+comments. Cheap, but still **cost-gated** — surface the number first.
- On exhaustion the client returns `{"status":"budget_exhausted","fallback":true}` — **check
  `.fallback`** and drop to 1b.
- Loop guards: max 5 calls/task, dedupe, keep the raw JSON. The text you keep is verbatim customer
  language with permalinks → ideal source tags for `/ctm-clean`.

### 1b. Reddit + other forums — NotebookLM (the expert's pick; grounded, cited)
```bash
python3 execution/notebooklm_client.py query <notebook-id> "<query>"   # ONLY subcommand that runs from CLI
```
- **CLI note:** the CLI guard requires 4+ argv, so only `query <notebook-id> "<query>"` runs from the
  command line. `list`, `budget`, and `search` trip the guard and exit 1 — to list notebooks or check
  budget, use the `/query-notebook` + `/add-notebook` skills or the NotebookLM MCP.
- Budget: **100 queries/mo**, soft-warn 80, hard-stop 100; per-task cap 5; 7-day cache. Collapse
  multi-part asks into one query (saves ~66%).
- Why it shines (per the expert): NotebookLM **reaches Reddit/forums better than most tools and cites
  the exact lines it pulled, so it won't invent a quote**. Limit: it only works from sources you hand
  it — add the specific threads/review pages first (as web links or pasted text). New notebook? use
  `/add-notebook`.

### 1c. Login-gated / JS-rendered communities & review sites — Playwright (read-only, Tier 1)
```
mcp__playwright__browser_navigate     { "url": "<thread or review page>" }
mcp__playwright__browser_snapshot     {}        # a11y tree → copy real text
mcp__playwright__browser_evaluate     { "function": "() => document.body.innerText" }
```
- Read-only navigation/snapshot/evaluate are **Tier 1 — no confirmation**. Never enter credentials;
  never take Tier-2 (state-changing) actions while gathering. Per `directives/browser-automation-
  safety.md`. Use only when WebFetch returns an empty SPA shell.

### 1d. Static review/blog/SEO pages — WebFetch (free, fast)
Use `WebFetch` for plain HTML pages (<1s). Falls back to Playwright for JS-heavy SPAs.

### 1e. Broad web signal / fallback synthesis — research engine (free→budgeted)
```bash
python3 execution/research.py "<voice-of-customer query>" --depth standard --json
```
Gemini-primary → Perplexity ($30/mo) fallback → Bedrock floor (WebSearch + Tavily + Recall). Carries
an honest receipt of what fired/failed/cost. Use to *find where they talk* and to triangulate — **not**
as a quote source unless it returns verbatim lines with citations.

### 1f. Own data (often the single best source — don't skip)
Sales/discovery-call transcripts, support tickets/emails, DMs, reviews of your product *and
competitors'.* Read from files the user provides (Read/Glob). These are the richest, free, and need
no scraping. Treat exactly like scraped text in `/ctm-clean`.

**Fallback chain (state it in the run):** Apify → NotebookLM → Playwright → WebFetch → research.py →
manual paste. Log which fired and why (honest receipt).

---

## Layer 2 — No-fabrication gates (what makes us trustworthy)
The map's entire value is that nothing is invented. Three gates:

1. **Verbatim-integrity check (in `/ctm-clean`).** Every extracted line must be a substring of the
   source chunk it came from. The deterministic backstop is a real script — run it, don't eyeball it:
   ```bash
   python3 execution/ctm_verbatim_check.py --source <raw_chunk> --quotes <extracted>
   ```
   It exits 1 and lists every non-verbatim offender (bracketed insertions + source tags are allowed).
   Any offender → discard it and re-issue the verbatim rule (P3). This is deterministic and checkable,
   not a vibe.
2. **Verification protocol (Step 5.5), before any fact-bearing output.** If an output asserts a
   real-world claim riding alongside the language (a statistic, a named competitor's pricing, an
   event), route it through the Step 5.5 Verification protocol
   (`directives/verification-agent-protocol.md`) for VERIFIED / LIKELY / UNCONFIRMED labels.
   Pure-language outputs (quotes, headlines drawn from quotes) don't need it; claims about the world do.
3. **Prose check on any drafted output:** `python3 execution/prose_classifier.py check <file>` — keep
   AI-slop out of the put-to-work deliverables (CLEAN/WARNING, never FLAGGED).

---

## Layer 3 — Compose the heavier research (don't reimplement)
- **`/buyer-sourcer`** (skills/luke-iha-avatar-machine) — scaled, source-traced VoC mining (Perplexity
  + Playwright + Apify, ≥15 source URLs, auto-fails on modeled claims). `/ctm-gather` can delegate the
  whole mine to it, then run `/ctm-clean` on the returns.
- **`/mcraney-deep-canvass`** — belief excavation + resistance hierarchy. `/ctm-deepen` hands the map
  over for identity-level depth.
- **`/consumer-posture-profile`** (consumer-posture-research skill) — `python3 execution/research.py`-grounded
  posture (occupation, activity, thought-process). The runnable command is `/consumer-posture-profile`.
  `/ctm-deepen` enriches the map with it.

---

## Layer 4 — Persist + refresh
- Save the map as a plain markdown file the user keeps open (e.g.,
  `references/worked-exemplar-<audience>.md` for shipped examples, or a project file for live maps).
- **Schedule the refresh:** `/ctm-refresh` can register a quarterly job via `/schedule` so "the
  freshness is the edge" becomes a real recurring task, not a good intention.
- Finalize quality on any shipped map/output: `python3 execution/chain_runner.py finalize …`.

## Budget cheat-sheet
| Tool | Budget | Unit cost | Gate |
|---|---|---|---|
| Apify reddit | $29/mo | ~$0.001/result (~$0.05 / 50) | cost-gate hook; budget-status pre-check |
| NotebookLM | 100 q/mo | free per query (within cap) | 5/task; collapse queries |
| Perplexity (via research.py) | $30/mo | per query | cost-gate hook |
| Gemini (via research.py) | free (Ultra) | — | primary |
| Playwright / WebFetch / Recall / memory_facade | free | — | none (read-only) |
