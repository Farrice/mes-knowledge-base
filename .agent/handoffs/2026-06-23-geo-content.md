---
thread: geo-content
status: mid-build
resume_hint: content-os post-body anti-slop fix — real skill + deterministic gate, one pillar at a time
unfinished: content-os slop fix (primary); git push origin main; merge daily-brief PRs; [VERIFY LIVE] newsjacks
branch: main
pin: true
---

# HANDOFF — geo-content (GEO/SEO LinkedIn business, health/wellness/performance)
_2026-07-01 · thread: `geo-content` · Resume: `/resume geo-content`_

**Front door:** `_active/linkedin-launch/99-archive/2026-08-07-dead-front-doors/00-CONTROL-TOWER.md` (the one index — read first)
**Detailed open-job handoff:** `.agent/handoffs/2026-06-23-content-os-slop-fix.md`

## STATE AT CLOSE (all committed on `main` = single source of truth)
- **`main` is unified** — merged everything (LinkedIn Business OS + Content OS + Codex control-plane), verified: 0 commits stranded on any other branch. Backup tags `backup/pre-merge-*` exist. **`origin/main` is NOT synced** — the agent git-push hook blocks it; run `git push origin main` from a terminal (clean fast-forward, no --force).
- **Folder reorg DONE** (by a parallel process): the hub is now numbered — `00-start-here/ 01-research/ 02-offer/ 03-launch/ 04-content-os/ 05-lead-gen/ 06-automation/`. The control tower + `/geo-content` paths were updated to match. Use these paths, not old flat ones.
- **Offer ENHANCED 2026-07-01** — `02-offer/CANONICAL-OFFER-BRIEF.md` now 5 rungs (incl. Trust-Layer Install), market-calibrated + red-teamed; receipts in `01-research/MARKET-OFFER-INTEL-2026-07-01.md`.
- **Daily market brief SCHEDULED** — cloud routine `trig_01LPK9dSCmABXfq1g3pRWGsq`, 7am PT daily, opens a PR. Merge it each morning (manage: https://claude.ai/code/routines/trig_01LPK9dSCmABXfq1g3pRWGsq).
- **Launch package** — DONE, shippable today (START-HERE + LAUNCH-DECK + $500 audit + lead-gen). Drive mirror: folder `1rSrzr8jYYlwbICfvcNRshhNAo5FhlLOz` (docs 00–15).

## PRIMARY OPEN JOB (next session) — Content OS post-body anti-slop fix
The `04-content-os/exemplars/_p1..p5` + `04-content-os/starter-content-batch.md` post BODIES still carry **structural sameness** (nearly every post uses the identical "I used to think X. Then Y. Now I Z." turn) + residual AI tropes. Word-level gate passes; the cross-post repetition is the tell. **Fix it as surgery, one pillar at a time** — a REAL skill (`/anti-slop-audit` or `/slop-check` + `prose-doctor`), VARY the structures, then verify with `python3 execution/prose_classifier.py check <file>` on the actual prose (last run's "Signals: 1 / parallel_structure" was a FALSE pass — it flagged label tables). Rewrite weak ones via `writers-room`/`/really-real-social`. Re-collate the batch. **Do NOT rebuild; no big multi-agent fan-outs — over-orchestration is what degraded quality.** Full detail: `.agent/handoffs/2026-06-23-content-os-slop-fix.md`.

## OTHER OPEN ITEMS
- `git push origin main` (manual, terminal) to sync the remote.
- Merge the daily-brief PR each morning; if it flags CONTEXT GAPS, push the missing `_active/` files.
- The 5 newsjack posts are `[VERIFY LIVE]` scaffolds — swap a real screenshotted moment before posting.
- `P3-3` (GLP-1 gaming "patch notes") — weakest; likely cut.
- Old branches `repair/codex-harness-restore` + `session/session-pin-formula` are now fully contained in `main` — safe to delete for tidiness.

## DISCIPLINE (why quality degraded — apply next time)
One engine, careful passes, the deterministic gate between each. Never accept an agent's self-reported "QA passed." Felt verdict > system scores. Strategy is LOCKED (edu-FIRST adjudication spine, value-first, `--cta` ~1-in-5) — don't relitigate; fix the prose. **The launch is READY — the bottleneck is publishing, not building.**

## SUGGESTED SKILLS
`/anti-slop-audit` · `/slop-check` · `prose-doctor` · `prose_classifier.py check` · `writers-room` · `/really-real-social` · `/resume geo-content` · `/geo-content` (daily driver). Avoid `/jarvis-command-center:deploy` and big Workflow fan-outs for this — it's surgery.
