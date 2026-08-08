---
date: 2026-08-08
session: loss-alarm-repair
tier: session-brief
status: enriched
---

# Loss-Alarm False Positives — What We Found 2026-08-08 and What To Do About It

> A diagnostic session, not a build. Two session-open alarms — 565 broken citations and 104 EMPTY-ABSORB files — were audited flag by flag against git history. **Verdict: zero confirmed content losses out of 669 flags.** Both alarms measure against the wrong baseline. The repair is specced in `.agent/handoffs/2026-08-08-loss-alarm-repair.md`; nothing was patched this session.
>
> *Tier correction: the spine detected `operator-guide` and listed 6 changed operator assets (`.agent/workflows/briefs.md`, `mission-control.md`, `sweep.md`, `directives/feedback-ratchet.md`, `quality_gate.md`, `session-state-protocol.md`). **None were touched by this session** — they were dirtied by concurrent sessions sharing the main tree. Filed as `session-brief`, which is what this actually was.*

## ⚡ If you only read 10 lines

1. **Nothing is lost.** 104 EMPTY-ABSORB files → 60 moved byte-identical, 43 moved content-evolved, 1 renamed. 565 citations → 413 moved, 106 phantom, 27 runtime, 19 deleted-by-intent.
2. Compared against the **merge commits** directly, all four flagged merges absorbed **0 dropped files**. The alarm compares against *current* main HEAD instead.
3. That's the bug: the 2026-08-07 arena sweep (`43ebc4014`, 66 folders → 10 arenas) legitimately moved paths, so every prior merge in the 14-day window re-flagged. **Any future reorg re-triggers this.**
4. `citation_integrity.py` mangles `~/` — reports `~/.agents/.skill-lock.json` (17KB, exists) as missing. This is the **only BINDING-tier finding, and it is false.**
5. 61 of 106 phantoms are **illustrative example paths inside extracted expert prompts** (`ROSTER-YYYY-MM-DD.md`, `products/catalog.md`, `deliverables/carousel_scripts/YOUR_FILE.md`) — not pointers.
6. 28 more sit in `skills/*/references/_legacy-prompts/` — an exact duplicate mirror of the adjacent `prompts/` dir, double-counting every finding.
7. All 19 DELETED verified as intentional restructures — 12 are `riley-brown-marketing-automation` workflow renames from tier-prefixes to slash-command names in the v2 forge rebuild.
8. **65 of 565 pointers live in dated RECORD files.** Per LIVING-vs-RECORD these are session receipts, never truth — **do not repoint them.** Only the 500 in LIVING docs are candidates.
9. Fixing `~` expansion + template exclusion + the legacy mirror drops 565 → **~420**, of which ~383 are one mechanical repoint pass.
10. First thing to run next session: patch the two scanners, then `python3 execution/citation_integrity.py` and confirm ~420 with zero BINDING findings.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/citation_integrity.py` | 565 broken pointers, tiered BINDING/MEMORY/WIRING | Checking pointer health — **currently ~180 false** |
| `python3 execution/citation_integrity.py --json` | Same, machine-readable (`scanned`/`missing`/`report`) | Any programmatic classification pass |
| `git diff --diff-filter=A --name-only <merge>^1...<merge>^2` | Files a branch created | Auditing what a merge *should* have absorbed |
| `git ls-tree -r --name-only <merge>` | The merge commit's actual tree | The correct EMPTY-ABSORB baseline — **this is the fix** |
| `python3 execution/worktree_lane.py merge --lane <branch>` | Lane merge with Law-3 audit | Lane closeout; refuses while another session writes main |
| `python3 execution/session_lock.py claim "<mission>"` | Session lock token | **Before** multi-file work — the lane gate checks it |

## Snapshot

**Completed**
- Working tree cleared: 28 files committed + pushed (`origin/main` = `f980c2fd1`, clean at close) — content vault drafts, health-performance daily cuts + ledgers, LinkedIn context-OS maps, recurring reports archived.
- Full forensic audit of both loss alarms, every flag classified against git history rather than trusted.
- Diagnosed Fable 5's absence from the VS Code extension: it ships its **own** pinned `claude` binary (`resources/native-binary/claude`, v2.1.156, **0** hits for `claude-fable-5`) while the PATH CLI is v2.1.220 (**32** hits). Not plan/entitlement, not ZDR. No `executablePath` override exists — fix is updating the extension.
- Committed the `codex/expert-practice-os-closeout` lane's loose work inside its own worktree.

**Decisions**
- Do not force lane merges past the fresh-writer gate. `worktree-farrice-character-sheets` (4 commits) stays unmerged — blocked by live session `ca6d17f0`, watched `.agent/perplexity-usage.json` tick 266→268 mid-audit. The interlock was working, not stuck.
- Left `codex/expert-practice-os-v2-architecture` (43 uncommitted files) untouched — Codex is live in it.
- Do not weaken either alarm's sensitivity. The 2026-07-13 loss class is real; fix the baselines, not the threshold.

**Genuine findings, separate from the false positives**
- **`skills/patrick-debois-cdlc/` is non-operational** — four workflows cite ten execution scripts that were never built (`skill_security_scan.py`, `skill_versions.py`, `skill_dependencies.py`, `observability_scanner.py`, `context_filter.py`, plus `evolution_store/observability/*.jsonl`). Build the layer or mark the workflows non-operational.
- Small dangling refs: `skills/nba-betting-edge/genius.md` → `execution/perplexity.py` (real path `research.py`); `guides/2026-07-26-opus-5-dialect.md` → `execution/jsonl_surgery.py`; `.agent/workflows/roth-content.md` → two missing `eric-roth-writing-mastery` workflows.
- **Filing bug:** `guides/2026-07-24-.md` has an empty slug and blank `session:` frontmatter — something wrote a guide with no title. It's also the noisiest stale citer (12 of the 19 DELETED).

**Where things live**
- Handoff + full repair spec: `.agent/handoffs/2026-08-08-loss-alarm-repair.md` (thread `loss-alarm-repair`, pinned)
- Scanners to patch: `execution/citation_integrity.py`, `execution/hooks/divergence_alarm_hook.py` (`_detect_empty_absorbs`, ~line 54)
- Why the moves happened: `_active/_archive/MOVED.md`
- The real loss class both alarms exist for: `docs/solutions/2026-07-13-divergent-branch-work-silently-lost.md`

**Honest edges**
- The ~420 residual count is projected from the classification, not measured — the patch hasn't run. Verify before trusting it.
- I did not test whether excluding `references/prompts*/` suppresses any *real* pointer in those dirs. Spot-check before shipping the exclusion.
- Cost: $0. Entire audit was local git + `strings`.
