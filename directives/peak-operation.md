# Peak Operation Doctrine

> Written 2026-07-06 by Claude Fable 5 (last full-capability session) after a three-mission day: harness redesign, second-brain/evolution audit+repair, full queue execution. Purpose: any model driving this system — Sonnet, Opus, Codex — can replicate Fable-grade outcomes by following the *shape of the work*, not by being smarter. The system's intelligence lives in its loops, gates, and evidence discipline. Load this when orchestrating anything multi-step or when quality feels off.

## 1. The operating shape that produces top-grade outcomes

Every strong outcome today followed the same five-beat shape. Reproduce the shape:

1. **Scout thin, then decompose.** One cheap inventory pass (file listing, counts, log tails) before any deep work. Then split the task into 2-5 lanes with **disjoint file ownership** — name exactly which files each lane may touch, and which it must not.
2. **Evidence before judgment.** Auditor/explorer agents gather timestamps, row counts, log tails, run artifacts — never documentation claims. Every finding must carry its evidence line. Word-ceiling every agent report (500-900 words); density > completeness.
3. **Judgment at the top, execution at the bottom.** The orchestrator (whatever model) makes the architecture calls and writes them down BEFORE dispatching builders. Builders get: full context in the prompt (they inherit nothing), explicit do-not-touch lists, verification commands to run, and "report deviations honestly" instructions.
4. **Verify by execution, not by reading.** A change isn't done until a real command proved it: the hook smoke-tested with real JSON, the benchmark run with real numbers, the scan fired on a real risky file. If a builder reports success without run evidence, re-run it.
5. **Commit per unit, immediately.** Concurrent sessions are this repo's #1 corruption hazard (GOLDEN RULE violated live on 2026-07-06; recovered via stash). Small targeted `git add <files>` commits after each verified unit — never `git add -A`, never batch at the end.

## 2. Outcome → engine routing (the proven paths)

| Outcome envisioned | Run this — do not rebuild it |
|---|---|
| **A messy thought, any domain — "just make this happen"** | **`/go` (2026-07-06): silent DICE compile → written assumptions (max ONE question round) → run packet with taste refs → routes to the right conductor below → delivers + 3 Next-Prompts. The anti-bottleneck front door — the system sharpens intent, not Farrice** |
| **Any content, any purpose (education/value/AHA/personal/client)** | **`/create` — the universal conductor (2026-07-06): outcome contract (≥2 engineered outcomes) → context richness (memory facade + COS goals + thought-bank) → live zeitgeist (perplexity/recall/research.py, receipts required) → route to the specialist stack → proven recipe → gates. Composes the engines below; never replaces them** |
| Multi-deliverable marketing/creative mission | `/supercomputer` |
| Gate-suppressed end-to-end run (3 taste gates only) | `/autopilot` |
| Any-objective content engine | `/jw-engine` |
| LinkedIn (Farrice) | `/farrice-engine`, `/linkedin-daily` |
| Cold-start converting copy | `/copy-engine` (Ground Once, Refine Free) |
| Substack | `/parallax` — never writers-room |
| Refine an existing draft | `writers-room` (Layer 0 = today's zeitgeist brief / `/create` Stage 2 signals first) |
| Health-brand client work (Path A) | Load `/claim-safe` alongside the content engine; the finalize claim-risk scan fires automatically as backstop |
| Image/design | `/satori-design-think` decides the concept → `/satori-composition-brief` compiles the layout grammar → `/fantastic-studio` executes (never hand a bare prompt to a generator) |
| Deep research | `execution/research.py` (receipt-carrying), Gemini→Perplexity→floor |
| System repair | `/system-audit`; control-plane complaints route here before expert matching |

The benchmark recipe for content quality remains: scaffold × parallel-depth × expert-lens × voice-rules × dual-QA (`feedback_content-quality-pipeline-recipe.md`; exemplar `_active/linkedin/04-deliverables/content-os/ai-boom-content-package.md`). One author writes the body; hooks à la carte; more experts ≠ better voice.

## 3. Model economics post-Fable

- **Sonnet is the default executor and auditor.** Today's entire output — 20+ commits, three missions — was Sonnet-built under thin orchestration. Opus only for judgment-dense synthesis (doctrine, adversarial verdicts, taste calls). Never pin Opus; degrade a tier on unavailability, don't stall.
- **The orchestrator stays thin.** Its budget goes to: decomposition, architecture decisions, reading agent reports, catching contradictions between reports, and honest synthesis. If the orchestrator is reading many files itself, the shape is wrong.
- **Parallelize lanes, serialize shared files.** Two agents never edit the same file in the same wave. If a wave's lanes both need `evolution_orchestrator.py`, run them in sequence.

## 4. Weekly operating rhythm (the whole outer loop, ~30 min)

1. `.agent/router-report-card.md` — is the routing loop alive; weight movers sane; synonym candidates to approve.
2. `evolution_store/traces/daily_evolution_<latest>.md` — read ONE nightly report; the loop only improves if findings get read. Approve/reject synonym candidates.
3. `python3 execution/memory_review.py` — clear the flagged-review queue (alarm fires in the daily harvest log past 14 days).
4. `python3 execution/revenue_tracker.py due` + `/weekly-closeout` — the market feedback loop. **This is the system's weakest historical link: deliverables ship, outcomes never get logged, so nothing learns what actually sold.** Logging outcomes is the highest-leverage 20 minutes of the week.
5. Glance `launchctl list | grep antigravity` — any non-zero exit codes.

## 5. Drift detection — when to stop producing and repair

Signals, in order of severity: (a) felt-drift — output feels off even when gates pass: **felt verdict wins, always** (`feedback_auto-evolution-cant-substitute-for-ground-truth.md`); (b) finalize composites flatten to a narrow band across different work (grade compression — recalibrate against `rubric_v1.md` anchors, name the anchor or lower the score); (c) router report card shows loop-dark (zero decisions logged in 7d); (d) the same expert loads for everything (routing collapse — check `.agent/skill-weights.json` for runaway weights; clamp is [0.5,2.0] by design); (e) daily evolution log shows repeated identical errors. For (b)-(e): run `/system-audit`. Do not patch symptoms mid-production-session; finish the deliverable, then repair in a dedicated session.

## 6. Invariants — never trade these away

1. **GOLDEN RULE**: one driver per working tree. `active_tool_lock` warns now — treat its warning as a stop sign.
2. **Cost gate is a hard block**; extractions are never gated; MCP spend is observe-only until data says otherwise.
3. **Compass, never cage**: gates flag loudly, they do not deny Farrice his own system.
4. **No AI-memory-dependent observability**: anything that must happen gets a hook, a launchd job, or a deterministic script sink. If a new process depends on a model remembering, it is not shipped.
5. **Notion**: `execution/notion_api.py` only (2022-06-28 pin). Never convert property types — it silently wipes values (confirmed experimentally 2026-07-06). Additive schema changes only.
6. **Never rebuild what's already good.** Preserve the spine, make surgical passes, one engine per body. Rebuilding elevated content degrades it (proven 3/10 failure).
7. **Honest state files.** When reality changes, update the state file in the same session (`evolution-paused.json` drifted 4 days and misdirected planning). A stale state file is worse than none.
8. **Scores are earned, not asserted**: ≥8 requires naming the rubric anchor; hardcoded scores in workflows are a known past failure (E1) — if a workflow text contains a score, delete it.

## 7. First fortnight post-Fable — the validation checklist

The 2026-07-06 production audit found the engines healthy but several load-bearing paths *unproven in their current form*. Before trusting them in production, run each once and let the gates score honestly:

1. **`/linkedin-daily`** — rewritten to v2 on 07-01, zero runs since. Its Step 1 now force-loads the proven benchmark (`ai-boom-content-package.md`); the first run validates the rewrite.
2. **`/writers-room`** — rewritten 07-01, longest run-gap of all engines (18d). One refinement pass on any existing draft proves it.
3. **`/weekly-closeout`** — never executed as a ritual, ever. The revenue loop numbers (86 outcomes, $4,200 lifetime, all logged retroactively in one sitting) are the direct cost of that. The COS daily brief now shows the Outer Loop counts; the Sunday board is the moment to run it.
4. **Router**: glance `.agent/router-report-card.md` after a week; if the loop is alive and weights sane, set `SKILL_ROUTER_EMBED=1` (benchmarked +6pts top-3, p95 +600ms).
5. **Stashes**: `stash@{0}` (57 files) and `stash@{1}` (6 files) hold real dropped work (creative_router/workflow_router edits, jason-fladlien skill edits) — review and apply-or-drop deliberately; don't let them rot.
6. **Sunday 07-12 05:00**: verify `knowledge-compiler-weekly` produced its first log with clean exit.

## 8. What only Farrice can do (the system cannot self-supply these)

Taste verdicts on A-tier promotions · blind-rating bake-offs · memory review approvals · synonym candidate approvals · revenue/outcome data entry · the felt-drift call. The system is built to make each of these a ≤15-minute act. If any of them is being skipped repeatedly, the system is flying blind in that dimension — say so in the weekly COS board rather than silently continuing.
