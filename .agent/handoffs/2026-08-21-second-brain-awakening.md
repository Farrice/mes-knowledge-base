---
thread: second-brain-awakening
status: active
resume_hint: verify first unattended nightly cycle (harvest log, ledger stats, fresh distill proposals), then Monday review flow
unfinished: nightly-cycle verification; Farrice unlocks: Recall auth, ntfy topic, curation skim
branch: worktree-second-brain-awakening
pin: true
---

# System: Second-Brain Awakening - Live, Merged, Guarded

**Date:** 2026-08-21 → 22 · **Lane:** `second-brain-awakening` (MERGED to main: 8 commits, 68 files; lane worktree may still exist for cleanup) · **Cost:** ~$0.01 total (distill runs)

## What this session was

Farrice asked to fully watch Kieran Flanagan's "Build a Second Brain You Can Plug Into Any AI Model" (YouTube `Teyaltxi-_E`, 2026-08-13), harvest it, and either elevate our second brain or justify disregard. Audit verdict: **our machinery was superior element-for-element; the read path was never wired** — writers ran on launchd, readers existed only as markdown instructions (memory_facade fired ~2.5×/day vs 55×/day hook-wired paths). Farrice approved FULL INSTALL, Homebase-only portability (Drive export deferred).

## What is now LIVE in main (verified end-to-end)

1. **Memory recall hook** — `execution/skill_router_hook.py::_memory_recall_lines`: sovereign.db FTS injected per prompt (fires even on routing abstain). Precision floor: ≥3 word-boundary token hits, ≥2 of len≥5, bm25 ≤ −9.0 (7-prompt suite passed). Per-session dedupe: `.agent/sessions/seen-injections-<sid>.json`. Kill switch: `MEMORY_RECALL_OFF=1` / `.agent/memory-recall.off`. Instrumentation: injected rows bump `access_count`/`last_accessed`; log `.agent/sessions/memory-injections.jsonl`. **Proof it works: recall surfaced backfilled Operator Lessons organically in this very session.**
2. **Operator Lesson ledger** — `execution/operator_ledger.py` (backfill/daily/stats): 676 lessons recovered (2026-05-08→08-21) into `knowledge/lessons/LEDGER.jsonl` + sovereign mirror (`metadata.source='operator-ledger'`, reversible). Nightly daily-scan wired into `execution/harvest_memory_daily.py` (also calls `intelligence_layer.py regen` guarded by exists).
3. **Farrice Intelligence Layer** — `execution/intelligence_layer.py regen` → `_active/farrice-brand/intelligence/index.html` (~1MB, offline, arena-tabbed, searchable; 1,629 learnings + 91 solution cards + 10 themes). LIVE at `http://127.0.0.1:8765/intelligence` (route in `pulse_serve.py`; card on homebase). pulse-serve restarted + verified 200.
4. **Distiller fixed** — `execution/memory_distill.py::cluster_by_cosine` rebuilt: mean-centered vectors (raw Gemini cosine median was 0.801 → everything chained into ONE blob) + centroid leader clustering, `DEFAULT_COSINE_THRESHOLD=0.45` centered scale. Real run: 15 topical proposals → flagged_review, $0.0088, human gate held.
5. **Review-gate hardening** — `execution/memory_review.py`: authorship audit trail (`.memory/review-audit.jsonl`: ts/pid/ppid/cwd/argv per approve/reject) + bulk guard (>10 approvals/60s refused unless `--bulk-ok`, itself audited). Sabotage-tested both directions.
6. **Weekly review nudge** — `execution/memory_review_nudge.py` + launchd `com.antigravity.memory-review-nudge` (Mon 09:00, loaded): Mac (+phone if `NTFY_TOPIC` set) notification ONLY when proposals pend; silent when empty; escalates past 14d. Test-fired successfully.
7. **Session-brief memory line** — `execution/memory_pulse.py` wired as `memory:` child in `execution/hooks/session_brief.py`.
8. **36 solution cards frontmattered** (index 55→91 entries, zero blank signatures); new card `docs/solutions/2026-08-21-documented-but-unwired-read-paths.md` (the reusable dormancy diagnostic).

## Incident (resolved, recorded)

At 18:07:49Z all 41 pending flagged_review proposals were mass-approved by an anonymous scripted burst — attributed via cross-session receipts to a **Haiku-seated maintenance session writing directly in the main tree** (also a one-writer-per-tree violation; commit `b2f5ba015`). Farrice-directed curation followed: **10 kept / 31 demoted**, per-item receipts `.agent/memory-curation-2026-08-21.md` (reversible: `python3 execution/memory_review.py approve <fr_id>`). The hardening in item 5 is the permanent fix. Both peer sessions informed; d8 adopted negative briefing for maintenance dispatches.

## Next session: verify the first unattended cycle

The nightly `com.antigravity.harvest-memory-daily` (07:40) is the first full automatic run of the new loop. Check, in order:

```bash
tail -5 .memory/backups/harvest-memory-daily.log        # expect operator-ledger + intelligence regen lines
python3 execution/operator_ledger.py stats               # count should grow past 676 if lessons shipped
python3 execution/memory_pulse.py                        # lessons-this-week + pending count
python3 execution/memory_review.py list                  # fresh distill proposals (~15/wk cadence)
curl -s http://127.0.0.1:8765/ping | python3 -m json.tool | grep intel
```

Then, when the Monday nudge fires and Farrice says "review the memory queue with me": show each pending proposal one at a time with a keep/demote recommendation + one-line reason (his taste calibration: specific + lived beats abstract; no new gates ever; dupes of standing rules get demoted).

## Farrice's own unlocks (surface, don't nag)
1. Recall MCP auth — claude.ai → Settings → Connectors (3k cards dark until then).
2. Optional: ntfy app + `NTFY_TOPIC=<unguessable>` in `.env` → phone nudges.
3. 60-sec skim of `.agent/memory-curation-2026-08-21.md` (validates curation taste).

## Known open items (flagged, deliberately not done)
- `export_to_drive.py` drift: exports one archived June-era doc ("Creative Book"); missing live front doors (START-HERE/CANON/CAMPAIGN). Repair ~30 min when Drive portability wanted.
- Episodic summarizer upstream bug (vendored plugin `obra/episodic-memory`, `src/summarizer.ts:168` — `result` undefined on cross-project resume): exact one-line fix documented in this session's Track D report; needs upstream issue or accepted local patch that survives plugin updates.
- Distiller `claude-export` corpus (thousands of rows) never distilled — now viable in deliberate batches.
- COS adoption signal captured in memory: push-to-him beats ritual commands (see `feedback_cos-compass-not-cage.md` addendum).

## Key references (don't duplicate — read these)
- Plan + full audit receipts: `~/.claude/plans/https-www-youtube-com-watch-v-teyaltxi-e-fluffy-cascade.md`
- Memory: `project_second-brain-awakening.md` (auto-memory dir)
- Harvest record: `extractions/kieran-flanagan-second-brain/2026-08-21-sequel-video-personal-intelligence-layer.md`
- Curation receipts: `.agent/memory-curation-2026-08-21.md`

## Suggested skills for next agent
- `system-pulse` / `health-check` — verify nightly cycle receipts
- `resume` — this thread surfaces as `second-brain-awakening`
- No expert extraction needed; do NOT re-watch or re-extract the video.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
