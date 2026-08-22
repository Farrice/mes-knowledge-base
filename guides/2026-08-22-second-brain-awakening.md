---
date: 2026-08-22
session: second-brain-awakening
tier: operator-guide
status: enriched
---

# Second-Brain Awakening — What We Built 2026-08-22 and How to Use It

> One session turned a write-only memory stack into a system that talks back: sovereign-memory recall injected into every prompt, a permanent Operator Lesson ledger (676 recovered), the Farrice Intelligence Layer page, a fixed distiller (15 topics/week instead of 1 blob), a hardened review gate, and a Monday nudge that reaches the Mac. Companions: plan+audit `~/.claude/plans/https-www-youtube-com-watch-v-teyaltxi-e-fluffy-cascade.md` · curation receipts `.agent/memory-curation-2026-08-21.md` · diagnostic card `docs/solutions/2026-08-21-documented-but-unwired-read-paths.md`.

## ⚡ If you only read 10 lines

- The brain is at **http://127.0.0.1:8765/intelligence** — 1,629 learnings, searchable, rebuilds nightly.
- Memory now injects itself into prompts (`MEMORY (…): …` lines). Wrong/stale line? Say so — that prunes it. Off switch: `MEMORY_RECALL_OFF=1` or touch `.agent/memory-recall.off`.
- Monday 09:00: Mac notification fires ONLY if rules await review. Respond by telling Claude: **"review the memory queue with me."** Silent = nothing pending.
- Never bulk-approve the queue — every approve/reject is now logged to `.memory/review-audit.jsonl`; >10 approvals/60s refuses without `--bulk-ok`.
- `python3 execution/memory_pulse.py` — one-line second-brain health (also auto-appears in the session brief).
- `python3 execution/operator_ledger.py stats` — lesson count/arenas (676 at ship).
- `python3 execution/intelligence_layer.py regen` — rebuild the brain page on demand (~0.1s).
- Distill runs weekly, ~15 topical proposals into `memory_review.py list`; the fix was mean-centering (raw cosine median 0.801 = one blob).
- Doctrine line: **hooks execute, instructions don't** — a store "feels dormant" when its readers are prose; diff fires-per-day hook-wired vs documented paths.
- Farrice-only unlocks still open: Recall auth (claude.ai → Connectors), optional `NTFY_TOPIC` in `.env` for phone nudges.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/memory_pulse.py` (`--full` for JSON) | one-line memory health: lessons this week, review queue, staleness | session brief flagged something, or a quick pulse check |
| `python3 execution/operator_ledger.py stats` / `backfill` / `daily` | lesson counts / full episodic re-scan / last-48h scan | verifying the nightly ran; recovering after downtime |
| `python3 execution/intelligence_layer.py regen` | fresh `_active/farrice-brand/intelligence/index.html` | after a big learning burst; before showing the page |
| `python3 execution/memory_review.py list` / `approve <id>` / `reject <id>` | the human gate over distilled rules | Monday nudge fired; or say "review the memory queue with me" |
| `python3 execution/memory_review_nudge.py --force` | test-fires the Mac/phone notification | verifying the nudge channel works |
| `ANTIGRAVITY_DISTILL_INCLUDE_EXPORT=1 python3 execution/memory_distill.py run --days 14 --min-cluster 2 --max-clusters 15 --judge-threshold 6.5` | fresh rule proposals → flagged_review (never auto-promotes) | deliberate distill outside the weekly cadence |
| `tail -5 .memory/backups/harvest-memory-daily.log` | nightly cycle receipt (embed · ledger · regen · distill) | morning-after verification of the unattended loop |

## The mental model

1. **Write side was always healthy; the session installed the read side.** Episodic capture → nightly harvest → ledger + mirror → distill proposals → YOUR gate → semantic tier → recall hook → your next prompt. One loop, every arrow now physical.
2. **Two speeds of memory.** Fast lane: Operator Lessons, captured nightly from chat, no review needed (they're already one-line distillations). Slow lane: distilled rules, ~15/week, always through your gate — because auto-evolution ≠ ground truth.
3. **Nudges come to you; rituals die.** The review queue sat 26 days behind a launchd log. Now the alarm is a Mac notification and a session-brief line. Anything recurring built for Farrice defaults to push-to-him.
4. **The gate is Farrice's alone.** Proven the hard way: a sibling Haiku session mass-approved 41 rules in a second. The audit trail + bulk guard make that impossible to repeat silently; the curation pattern (keep specific-and-lived, demote jargon/dupes/gate-proposals) is the recovery play.

## Capabilities

### Memory recall in prompts (`skill_router_hook.py::_memory_recall_lines`)
**What:** FTS match of your prompt against sovereign semantic+procedural tiers; max 2 one-liners injected; fires even when skill routing abstains. **When:** automatic — nothing to invoke. **When NOT:** noisy day or sensitive demo → `MEMORY_RECALL_OFF=1`. **Worked example:** "draft linkedin outreach dms for the supplement offer" surfaced the 2026-07-31 ALL-IN LOCK unprompted. **Honest edges:** floor tuned on today's corpus (≥3 word-boundary hits, ≥2 len≥5, bm25 ≤ −9.0); expect occasional near-miss/false-positive — verdicts on bad lines are how it tunes. Embeddings for the 676 new lesson rows backfill via nightly quota; until embedded they rank via FTS only.

### Operator Lesson ledger (`operator_ledger.py` → `knowledge/lessons/LEDGER.jsonl`)
**What:** line-anchored extraction of `Operator Lesson:` lines from episodic assistant turns; typed (insight/rule/win/loss) + arena-routed; sha-deduped; mirrored to sovereign (`metadata.source='operator-ledger'` — reversible with one DELETE). **When:** runs itself nightly; `backfill` only after harvest downtime. **When NOT:** don't hand-edit the JSONL — capture flows one way. **Honest edges:** arena heuristic is keyword-based; 411/676 landed "general" — acceptable for recall, imperfect for browsing.

### Intelligence Layer page (`intelligence_layer.py` → `/intelligence`)
**What:** one offline HTML file: learnings by arena + solved-problem table + themes + canon pointers; client-side search; Ink+Steel theme. **When:** thinking, prepping a call, showing another AI who you are. **When NOT:** it's INTERNAL — TACT LAW applies before any external share; Drive export deliberately deferred (~30-min add via repaired `export_to_drive.py`). **Honest edges:** homebase card renders from main's generated homebase.html — regenerates on the next homebase build; `surface_nav` doesn't list `/intelligence` in other pages' navs (kept diff minimal).

### Distiller (`memory_distill.py`)
**What:** mean-centered centroid clustering (no chaining), adaptive to the corpus; judge scores each cluster's proposed rule; everything lands in flagged_review pending. **When:** weekly cron; deliberate runs for the untouched `claude-export` corpus (thousands of rows — run in small `--days` batches). **When NOT:** never raise `--max-clusters` casually — 15 proposals is already a 5-minute review. **Honest edges:** threshold 0.45 calibrated on one corpus snapshot; if weekly runs return 1-2 clusters again, re-measure the centered distribution before touching code.

### Review gate + nudge (`memory_review.py`, `memory_review_nudge.py`)
**What:** approve/reject CLI with authorship audit + bulk-rate wall; Monday launchd notification when pending>0. **When:** the nudge fires, or `memory_pulse` shows a queue. **When NOT:** never from an agent without Farrice's explicit direction; never `--bulk-ok` to "tidy up." **Worked example:** the 41-item curation — keeps were specific+lived ("local-first for scheduled automation"), demotes were jargon ("Extract-Forge-Amplify pipeline"), dupes, and gate-proposals. **Honest edges:** audit trail starts today (empty history before); the guard is per-minute rate, not identity — a slow drip would pass (acceptable: the audit names it).

## Composition (options, not wiring)

| Stack with | When it earns its cost |
|---|---|
| `/resume second-brain-awakening` | continuing this thread — pinned handoff has the verification checklist |
| `memory_facade.py "<intent>" --top 10` | deep manual recall across all 8 stores (now also bumps access stats) |
| `/system-audit` | if recall lines feel systematically off — describe the symptom |
| Solution card `documented-but-unwired-read-paths` | ANY store that "feels dormant" — run the fires-per-day diff before building anything |
