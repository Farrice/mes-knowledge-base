# Memory Capture Bake-off — Protocol & Pre-Committed Decision Rule

Purpose: choose the canonical **L1 episodic-capture layer** with scored evidence, not vibes. Mirrors `_active/platform-bakeoff/04-deliverables/PROTOCOL.md` — the decision rule is locked BEFORE any session is scored; post-hoc rationalization is the failure mode this file exists to prevent.

## Contestants
- **A — episodic-memory** (superpowers plugin, v1.0.15). **INSTALLED & LIVE.** Mechanical `SessionStart` hook → indexes every CC/Codex exchange into `~/.config/superpowers/conversation-index/db.sqlite`. Local embeddings (sqlite-vec + bundled transformers) → **$0/session**. Already holds **133,216 exchanges (22,939 for this project)** as of 2026-06-23.
- **B — claude-mem** (github.com/thedotmack/claude-mem). **NOT installed.** Plugin: `SessionStart`/`PostToolUse`/`SessionEnd` hooks → AI-compress (~$0.05/session) → SQLite/FTS5 (+ optional Chroma) → auto-inject last-N sessions. Starts cold (0 history).

**Install B only in an isolated git worktree profile** so its hooks never touch the committed `.claude/settings.json`. Fully reversible.

## How to run
1. Test window: **10 real working sessions OR 7 calendar days**, whichever comes first. Same machine, same repo.
2. claude-mem's cold start (0 history vs 22.9k) is a **recorded handicap, not corrected** — "what you actually get day-to-day" is the thing being measured (same rule as platform-bakeoff).
3. Append one JSON line per `(session, contestant)` to `scores.jsonl` (schema below). Score blind where possible.
4. Run a scorecard (clone `_active/platform-bakeoff/04-deliverables/scorecard.py`) to aggregate the weighted composite and apply the rule mechanically.

```
{"session": 1, "contestant": "episodic-memory", "relevance": 8, "token_savings": 7, "completeness": 8, "latency_cost": 10, "stability": 10, "queryability": 10, "notes": "..."}
```

## Metrics (weighted; 0-10 against named anchors)
| # | Metric | Weight | Measurement |
|---|--------|:--:|---|
| 1 | Retrieval relevance | 30% | 10 fixed recall queries from past work; blind-score top-5 hits vs `evolution_store/ground_truth/rubric_v1.md` anchors |
| 2 | Context-token savings | 20% | tokens auto-injected at SessionStart that were *actually used* ÷ total injected (precision), from transcript |
| 3 | Capture completeness | 15% | sample 5 sessions; % of consequential decisions/files present in the store |
| 4 | Latency + cost / session | 15% | SessionStart added wall-clock (ms) + $/session. **Ungated paid calls → automatic −3 on this metric** |
| 5 | Stability / hook-safety | 10% | any double-PostToolUse, gate bypass, or Stop-hook interference over the window (binary: 0 or 10) |
| 6 | Facade queryability | 10% | can `memory_facade.py` read it read-only via SQL with no node/extension dependency? (episodic: yes via `exchanges`; claude-mem: yes via FTS5) |

## Pre-committed decision rule (LOCKED 2026-06-23, before any session scored)
- **Daily driver** = higher weighted composite, **minimum 7.0**, **AND zero hook-safety failures**.
- **HARD DISQUALIFIER**: any contestant that makes **ungated paid API calls** cannot be daily driver regardless of composite — the repo's cost-gate principle (CLAUDE.md "PHYSICAL, not advisory") is non-negotiable. (This is the standing strike against claude-mem's ungated `SessionEnd` compression.)
- **Tie-break**: retrieval relevance (metric 1) — that is the entire point of the layer.
- **If neither clears 7.0**: episodic-memory remains canonical **by data, not inertia** (incumbent + already-indexed history + $0 + local).
- The rule may not be edited after the first session is recorded.

## Retire the loser
Uninstall it, remove its hooks/data, and record the outcome in the consolidation map (CLAUDE.md / `project_*` memory). If episodic-memory wins, `.claude/settings.json` must be byte-identical to its pre-bakeoff baseline.

## Fast-path (recommended, on file as the alternative)
Given the install-state asymmetry — incumbent already holds 22.9k exchanges, $0, no hook conflicts, while the challenger is disqualifier-prone on metric 4 — **adopting episodic-memory directly and keeping this protocol as the on-demand validation** is the lower-cost path. Default is the safe isolated bake-off above unless the fast-path is greenlit; either way the locked rule governs.
