# Perplexity Comet / Labs / Deep Research — Mechanics Brief (2026-07-07, Sonnet deep-research)

## The Single Truth
All three products run the same trick — decompose one prompt into a tool-call loop and paper over an unreliable execution layer with a visible trace (accessibility trees, tool logs, citations) — and the trace is more trustworthy than the execution. Labs and Deep Research trace-and-cite well; Comet's live-page execution is the weak link in every independent report.

## Comet Mechanics
- [VERIFIED — Zenity Labs reverse-engineering, labs.zenity.io] Four layers: backend LLM planner, Sidecar UI, three Chrome extensions, Chromium. Dual-channel: SSE stream carries reasoning/citations; WebSocket carries RPC automation. **The model never sees raw DOM** — `comet-agent` calls Chrome's `Accessibility.getFullAXTree` via `chrome.debugger`, hands back a YAML accessibility tree with reference IDs only for interactable elements (token-budget workaround). Action primitives: `ComputerBatch` (pixel clicks/drags/scrolls), `FormInput` (node-reference), `Navigate`, `ReadPage`, `GetPageText`, `CreateSubagent` (nested subagents for parallel tab work). Deterministic security boundaries in CODE: `isInternalPage`/`isUrlBlocked` hard-block chrome://, file://, blacklisted domains.
- [VERIFIED — Perplexity Help Center] Comet Assistant (sidecar, page-context Q&A) vs Comet Agent (main-window multi-step). Background Assistants + Scheduled Tasks (cloud cron, laptop closed) gated to $200/mo Max tier.
- Reliability [VERIFIED — eesel.ai 30-day review + PCMag]: solid at page/video summarization, cross-tab comparison, in-context Gmail drafting. FAILS multi-step transactions — fabricated hotel booking dates, navigation loops, slower than doing it by hand; ~20% CPU and 4GB+ memory with a few tabs.

## Labs Pipeline
- [VERIFIED — DataCamp + Department of Product hands-on] Single prompt → live research → code execution (Python/SQL) → chart/asset generation → compiled package. Runtime 5–10 min. Output three-part: one-page report + deployed interactive mini-app (persistent shareable URL outside the chat) + downloadable assets (CSV/PNG/scripts). A "Tasks pane" shows the literal ordered tool trace.
- Weaknesses [VERIFIED — review roundups]: coding/math edge cases, app inconsistencies; creative/marketing copy reads flat vs native ChatGPT/Claude.

## Deep Research Pipeline
- [VERIFIED — convergent] Iterative retrieve→read→reason→refine, not single-pass: decomposes into subtopics, fans out 20–50 targeted searches, clusters by topic/recency, deepens promising clusters, flags conflicts, iterates to one cited narrative. Runtime 2–4 min, hundreds of sources read.
- Best at [VERIFIED — Second Talent 9-test review]: market/competitor research, regulatory summaries, legal citations to government portals, academic deep-dives. Weak: niche VC/investment intelligence, non-headline financial commentary.
- **Citation accuracy is contested and load-bearing**: vendor-adjacent ~92–94% (largely self-reported) vs Columbia Journalism Review/Tow Center (Mar 2025, 1,600 queries, 8 engines): Perplexity BEST of cohort at **37% error rate** — mostly misattribution (right fact, wrong source), not fabrication; Grok 3 worst at 94%. [Caveat, UNCONFIRMED]: CJR tested standard search, not confirmed Deep Research mode — treat as a floor on the retrieval stack.

## Transferable Patterns
1. Accessibility-tree perception over raw DOM/screenshots — replicate via Playwright MCP accessibility snapshot as the default page-read mode.
2. Deterministic URL/domain gating in code, not prompt instructions — align `directives/browser-automation-safety.md`.
3. Subagent-per-source/tab spawning for multi-source research instead of serial page burn-through.
4. User-facing tool-trace as a first-class artifact — make the manifest (sources hit, scripts run, files produced) a visible companion to every research deliverable, not a buried receipt.
5. Never equate "has citations" with "citations are correct" — best-in-class still carries ~37% independently-measured misattribution. Validates Step 5.5 as a genuine structural advantage over a $200/mo product.

## Sources
Primary technical: Zenity reverse-engineering. Product: Perplexity Help Center/blog. Reviews: eesel.ai 30-day, DataCamp, Department of Product, Second Talent, Applied AI Tools/G2. Ground truth: CJR/Tow Center citation study. Internal: 13 Recall YouTube-transcript cards (LIKELY-tier corroboration).
