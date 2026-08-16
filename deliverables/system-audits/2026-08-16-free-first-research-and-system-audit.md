# Free-First Research Activation and System Audit

**Date:** August 16, 2026

**Owner:** System Audit

**Status:** Research repair `PASS`; wider system audit `ACTION REQUIRED`
**Scope:** Google Antigravity main checkout, Codex automations, Antigravity launch agents, Apify shutdown status, research routing, and read-only system health.

## Executive verdict

The Free-First Research Mission is integrated into the live dirty `main` checkout and passes its routing, policy, parity, and control-plane verification. Current-world research now defaults to native web research and primary sources, with bounded Tavily Search/Extract available only after a native-web attempt and a confirmed zero-dollar boundary. Apify, paid accelerators, schedules, Tavily Research, and real subagents are excluded from this lane.

Apify containment is also intact: all six known Apify launch agents are unloaded and disabled, no matching scraper process is running, there is no user crontab, and the Codex Health Performance GEO daily automation is paused.

The wider workspace is usable, but it is not maintenance-clean. One likely orphaned Codex heartbeat remains active every 10 minutes, and four local launch jobs are failing. Those issues did not block the research repair, and they were deliberately not mutated during this audit so the evidence remains reviewable.

## Decision surface

### LOCKED

1. Free-First is the default for current-market, current-world, social-listening, and deep-research requests.
2. The runtime routes those requests to `/deep-research-os`; nonexistent routes or verifiers fail closed instead of presenting a false “Running now” state.
3. Native web is the first live source. Local workspace context can shape questions and synthesis but cannot prove current-world claims.
4. Search snippets cannot be promoted to `VERIFIED`; evidence must resolve to inspectable sources.
5. Tavily is limited to Search/Extract, only when native web is insufficient and the request remains within a confirmed zero-dollar boundary.
6. Apify, paid accelerators, Tavily Research, schedules, and real subagents are barred from this mission.
7. The 131 pre-existing dirty-main path entries were preserved. Their working-tree, index, and untracked-name fingerprints were unchanged immediately after integration.

### PARKED

1. **Likely orphaned Codex heartbeat (high priority).** `finish-notion-second-brain-merge` is active every 10 minutes. Its target task `019ff40f-2068-7c33-8009-80edf28cd99b` no longer resolves. The automation’s own instructions say it should disable itself after the merge. This is the first item to pause or retire after confirming the branch outcome.
2. **Fleet verifier launch job (high priority).** `com.antigravity.verify-fleet` calls `execution/verify_fleet.py run`. The current command no longer accepts `run`. The weekly background verifier is broken even though today’s manual all-up verifiers passed.
3. **Health metrics launch job (medium priority).** `com.antigravity.health-metrics` failed when a deep scan encountered a worktree path that disappeared during traversal. The scanner needs to tolerate transient worktree removal.
4. **Notion mirror launch job (medium priority).** `com.antigravity.mirror-nightly` failed on DNS resolution for `api.notion.com`. The local mirror is about 109 hours stale. Current research must not depend on this mirror for live-world truth.
5. **Citation integrity launch job (medium priority).** `com.antigravity.citation-integrity` reports 470 missing pointers spread across active material, history, handoffs, and temporary worktrees. This needs a scoped classification pass, not a blind mass rewrite.
6. **System-health false negative (medium priority).** The quick status surface reports zero Performance Log entries because it depends on Notion. The local performance log contains 191 entries. The status readout should degrade to local truth when Notion is unavailable.
7. **Temporary worktree storage (low priority).** `.tmp` occupies roughly 44 GB, about 43 GB of it in Codex worktrees. Cleanup could reclaim substantial disk space, but it is destructive and should be reviewed lane by lane.
8. **Control-plane residue (low priority).** The active mission/intent status still points to an old completed Eightward mission. Routing feedback is sparse, 10 protocols are overdue, and the canonical system-audit workflow still names three archived verifiers. These are governance and observability debt, not blockers to using Free-First research now.

### NEXT ACTION

Use Free-First research immediately. On the next maintenance pass, first pause the orphaned 10-minute heartbeat, then repair the fleet verifier argument and the health-metrics worktree race. After those deterministic fixes, decide whether to retry/decouple the Notion mirror and scope citation-integrity findings.

## What changed

The activation commit is `c474575a9` (`fix: make current research free-first and fail closed`). It adds the Free-First mission compiler and verifier, establishes the canonical research contract, repairs stale Autopilot routing, strengthens worktree/runtime parity, and changes current-research routing to fail closed.

The integration also repaired a verifier timeout: the Savant Control Room verifier previously rebuilt the same output twice and exceeded its parent’s 90-second limit. It now executes the real command once and renders both views from that one payload.

## Verification receipt

**Free-First mission verifier: `PASS`.** Policy, route ownership, spend exclusions, and the evidence contract are wired.

**Autopilot runtime preflight: `PASS`.** Current-market research routes correctly, and missing runtime targets are blocked.

**Deep Research OS verifier: `PASS`.** The research owner is reachable.

**Control-intent suite: `PASS`, 31/31 + 7/7.** Natural-language research and repair intents route as designed.

**Google Operator Core, Codex/Claude parity, and Codex authority: `PASS`.** Operator alignment, the active workspace contract, and canonical authority pointers remain intact.

**Skill-system and subagent-language checks: `PASS`.** The contract and no-subagent boundary remain valid.

**Savant Control Room: `PASS`.** The repaired verifier completes under the parent budget.

**System control plane: `PASS`.** The live `main` checkout passed 85 golden queries, 40 helper checks, and its active contracts.

**Codex workspace check: `PASS`.** Commands, skills, agents, workflows, and execution scripts are structurally healthy.

**System verifier: `ALL CLEAR`.** It reported no structural error or warning.

**Native-web smoke test: `PASS`.** The lane reached an official NIST page updated April 8, 2026, without Apify or a paid accelerator.

**Dirty-main preservation: `PASS`.** All 131 pre-existing path entries and their fingerprints remained unchanged after integration.

Current-world smoke source: [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

## Apify containment and value audit

### Containment proof

All six launch agents are unloaded and disabled: `com.antigravity.zeitgeist-daily`, `com.antigravity.angle-map-listening`, `com.antigravity.social-pulse-farrice`, `com.antigravity.social-pulse-jen`, `com.antigravity.angle-brief`, and `com.antigravity.social-pulse-mybpm`.

No live process matched Apify, Signal Scout, social pulse, Angle Brief, Angle Map listening, Zeitgeist, Brand Radar, or the hybrid morning radar. No user crontab exists. The Codex automation `health-performance-geo-daily-brief` is paused, and no other Codex automation configuration references Apify, Angle Map, or Zeitgeist.

### Did Apify return value?

**Some data returned, but the value loop was weak.** A Signal Scout live test produced four posts and 229 engagers at an estimated local cost of about $0.50, and Angle/zeitgeist briefs were generated. That proves the actors were not uniformly empty.

However, several receipts show low decision value: repeated Reddit searches returned zero, one Twitter lane emitted identical `mock_tweet` placeholder rows, one Jen run used the wrong geography, and an August 12 Angle Map brief scored 5.33 (`Needs Improvement`). The data was not consistently surfaced as a clear decision, reusable context asset, or measurable commercial result.

The local spend ledger is not a trustworthy budget truth source. It records $9.3393 against a $29 plan and documents an earlier 3.32x under-reporting correction plus a calendar-month versus billing-cycle mismatch. The Apify dashboard’s reported 75% usage therefore outranks the local ledger for containment decisions.

**Verdict:** keeping Apify stopped is the correct default. Re-enable a paid scraper only for a named decision, a bounded spend ceiling, a visible evidence receipt, and a stop condition that proves the data changed something valuable.

## Automation inventory

**Paused:** `health-performance-geo-daily-brief`. This is the correct shutdown state.

**Active and suspect:** `finish-notion-second-brain-merge`. Its target task is unresolved, and it wakes every 10 minutes.

**Active with no Apify reference:** `monthly-sidebar-cleanup`, `daily-brief`, `weekly-review`, and `follow-up-monitor`.

Antigravity has 28 launch-agent definitions: six intentionally disabled Apify jobs and 22 loaded jobs. Of the loaded jobs, 18 are currently running or last exited successfully; four are failing as listed in `PARKED`.

## How to use Free-First now

Paste this into the current Codex task:

> Research the current market for [topic]. Use the Free-First Research Mission: native web first, official/primary sources where possible, bounded Tavily Search/Extract only if needed and confirmed zero-dollar, RSS where useful, no Apify, no paid accelerators, no schedules, no subagents. Label VERIFIED/LIKELY/UNCONFIRMED and give me the decision-changing synthesis plus source ledger.

Expected behavior:

1. Codex identifies the decision the research must support.
2. It searches the live web, prioritizing current primary sources.
3. It uses local context only to make the research more relevant, never as proof of present-world facts.
4. It resolves evidence into a source ledger and labels confidence honestly.
5. It stops when the evidence changes the decision or the remaining gap is explicit.

## Repair order for the next session

1. Pause and retire `finish-notion-second-brain-merge` after checking whether its branch outcome already landed.
2. Replace the obsolete `run` argument in `com.antigravity.verify-fleet` and live-fire the launch job.
3. Make health-metrics traversal resilient to disappearing worktrees and add a regression test.
4. Give system-health a local Performance Log fallback when Notion is stale or unreachable.
5. Retry or deliberately decouple the Notion mirror; do not let it gate current-world research.
6. Classify citation-integrity misses into active, historical, handoff, and disposable-temp buckets before repair.
7. Review dormant worktrees and reclaim disk space only after ownership checks.

## Boundaries observed

1. No Apify or paid research service was called.
2. No new schedule or automation was created.
3. No real subagent was used.
4. No force push, destructive cleanup, archive sweep, or unrelated main-tree edit was performed.
5. Audit findings beyond the approved research repair remain evidence-first recommendations for Farrice’s return.
