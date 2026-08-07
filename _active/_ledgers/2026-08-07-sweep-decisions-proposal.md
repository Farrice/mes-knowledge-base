# Sweep decisions — 66 projects under `_active/`

*Generated 2026-08-07 07:51 by `execution/sweep_triage.py`. Evidence is computed; the calls are yours.*

**How to answer:** everything is pre-filled with a recommendation. Only tell me the ones you want to CHANGE — say the project name and your call. Silence = the recommendation stands.

Columns: **last** = last time anyone actually worked on it (a 40+ file commit is housekeeping and does not count; a rename is not work). **refs** = files elsewhere pointing at it. **ctrl** = control-plane files citing it — those are wired into the harness.

## KEEP — stays live, gets the arena/initiative shape — 64

These get reorganised. Confirm the arena, or rename it — the arena is the folder name you will actually click.

| project | proposed arena | last | refs | ctrl | files | debt | why |
|---|---|---|---|---|---|---|---|
| `andrea-dj` | **andrea** | 2026-08-07 | 32 | 8 | 423 | 51 competing | cited by 8 control-plane file(s) — it is wired in |
| `chris-restaurants` | **chris** | 2026-07-28 | 1 | 0 | 5 | — | worked on 9d ago |
| `dwa-threads-engine-2026-07-05` | **client-trials** | 2026-07-28 | 9 | 1 | 92 | 2 competing | cited by 1 control-plane file(s) — it is wired in |
| `trendscale-trial` | **client-trials** | 2026-07-29 | 9 | 1 | 68 | 1 competing | cited by 1 control-plane file(s) — it is wired in |
| `dwa-affiliate-battle-test` | **client-trials** | 2026-07-15 | 7 | 1 | 17 | — | cited by 1 control-plane file(s) — it is wired in |
| `trendscale-brief-revision` | **client-trials** | 2026-07-01 | 2 | 1 | 86 | — | cited by 1 control-plane file(s) — it is wired in |
| `coach-cooz` | **coach-cooz** | 2026-07-28 | 15 | 3 | 324 | 10 competing | cited by 3 control-plane file(s) — it is wired in |
| `farrice-brand` | **farrice-brand** | 2026-08-07 | 583 | 58 | 322 | 8 competing · 2 unabsorbed | cited by 58 control-plane file(s) — it is wired in |
| `farrice-final-10` | **farrice-brand** | 2026-08-07 | 9 | 1 | 16 | — | cited by 1 control-plane file(s) — it is wired in |
| `parallax-icp-offer` | **farrice-brand** | 2026-06-30 | 7 | 1 | 43 | — | cited by 1 control-plane file(s) — it is wired in |
| `farrice-creative-strategist-portfolio` | **farrice-brand** | 2026-07-28 | 5 | 1 | 39 | — | cited by 1 control-plane file(s) — it is wired in |
| `farrice-master-context-2026-07-07` | **farrice-brand** | 2026-07-29 | 3 | 2 | 6 | — | cited by 2 control-plane file(s) — it is wired in |
| `farrice-teach-grow-rich` | **farrice-brand** | 2026-07-01 | 3 | 1 | 10 | — | cited by 1 control-plane file(s) — it is wired in |
| `content-system-audit` | **harness** | 2026-06-30 | 22 | 1 | 14 | — | cited by 1 control-plane file(s) — it is wired in |
| `swarm-apex-2026-07-07` | **harness** | 2026-07-29 | 17 | 3 | 10 | — | cited by 3 control-plane file(s) — it is wired in |
| `system-audit` | **harness** | 2026-07-28 | 15 | 8 | 24 | 1 competing | cited by 8 control-plane file(s) — it is wired in |
| `codex-repeatability` | **harness** | 2026-07-01 | 13 | 3 | 8 | — | cited by 3 control-plane file(s) — it is wired in |
| `elevation-track` | **harness** | 2026-07-28 | 10 | 4 | 20 | — | cited by 4 control-plane file(s) — it is wired in |
| `harness-apex-2026-07-07` | **harness** | 2026-07-29 | 8 | 1 | 7 | — | cited by 1 control-plane file(s) — it is wired in |
| `prompt-wiring-os-2026-07-13` | **harness** | 2026-07-29 | 7 | 1 | 15 | — | cited by 1 control-plane file(s) — it is wired in |
| `system-integration` | **harness** | 2026-06-30 | 7 | 6 | 12 | — | cited by 6 control-plane file(s) — it is wired in |
| `memory-bakeoff` | **harness** | 2026-07-29 | 6 | 2 | 5 | — | cited by 2 control-plane file(s) — it is wired in |
| `loop-engineering-integration` | **harness** | 2026-07-24 | 5 | 1 | 14 | — | cited by 1 control-plane file(s) — it is wired in |
| `frontier-elevation-2026-07-17` | **harness** | 2026-07-21 | 4 | 2 | 7 | — | cited by 2 control-plane file(s) — it is wired in |
| `prompt-renaissance` | **harness** | 2026-07-29 | 4 | 2 | 17 | — | cited by 2 control-plane file(s) — it is wired in |
| `codex-parity-2026-07-13` | **harness** | 2026-07-15 | 3 | 1 | 7 | — | cited by 1 control-plane file(s) — it is wired in |
| `context-engineering-os` | **harness** | 2026-07-29 | 3 | 1 | 5 | — | cited by 1 control-plane file(s) — it is wired in |
| `operator-cockpit-v2` | **harness** | 2026-07-29 | 3 | 1 | 4 | — | cited by 1 control-plane file(s) — it is wired in |
| `platform-bakeoff` | **harness** | 2026-07-29 | 3 | 1 | 13 | — | cited by 1 control-plane file(s) — it is wired in |
| `system-health-check-framework` | **harness** | 2026-07-29 | 3 | 1 | 7 | — | cited by 1 control-plane file(s) — it is wired in |
| `claude-code-harness-analysis` | **harness** | 2026-07-28 | 2 | 2 | 11 | — | cited by 2 control-plane file(s) — it is wired in |
| `operator-core-backport` | **harness** | 2026-07-29 | 2 | 1 | 7 | — | cited by 1 control-plane file(s) — it is wired in |
| `fork-harvest-2026-07-02` | **harness** | 2026-07-29 | 1 | 1 | 5 | — | cited by 1 control-plane file(s) — it is wired in |
| `second-brain-audits` | **harness** | 2026-07-29 | 1 | 1 | 8 | — | cited by 1 control-plane file(s) — it is wired in |
| `javier-human-values` | **javier** | 2026-07-28 | 6 | 1 | 25 | — | cited by 1 control-plane file(s) — it is wired in |
| `jen-listings` | **jen-listings** | 2026-08-05 | 51 | 10 | 29 | — | cited by 10 control-plane file(s) — it is wired in |
| `jen-santulan` | **jen-listings** | 2026-07-28 | 7 | 1 | 33 | — | cited by 1 control-plane file(s) — it is wired in |
| `josh-swing-nerd-shirts-v1` | **josh-katie** | 2026-07-28 | 16 | 2 | 78 | 1 competing | cited by 2 control-plane file(s) — it is wired in |
| `josh-katie-fitness` | **josh-katie** | 2026-07-15 | 8 | 1 | 67 | — | cited by 1 control-plane file(s) — it is wired in |
| `josh-dancewear-brand` | **josh-katie** | 2026-07-28 | 6 | 1 | 35 | — | cited by 1 control-plane file(s) — it is wired in |
| `kens-fasting` | **kens-fasting** | 2026-07-28 | 7 | 1 | 27 | 2 competing | cited by 1 control-plane file(s) — it is wired in |
| `health-performance-ip-library` | **knowledge** | 2026-08-07 | 96 | 6 | 106 | 21 unabsorbed | cited by 6 control-plane file(s) — it is wired in |
| `notion-intellectual-library` | **knowledge** | 2026-07-29 | 10 | 3 | 7 | — | cited by 3 control-plane file(s) — it is wired in |
| `search-content-mastery` | **knowledge** | 2026-08-07 | 8 | 1 | 98 | — | cited by 1 control-plane file(s) — it is wired in |
| `mastery-forge` | **knowledge** | 2026-08-06 | 7 | 2 | 10 | — | cited by 2 control-plane file(s) — it is wired in |
| `youtube-notion-replication` | **knowledge** | 2026-08-06 | 2 | 2 | 5 | — | cited by 2 control-plane file(s) — it is wired in |
| `linkedin` | **linkedin** | 2026-08-07 | 253 | 28 | 439 | 5 competing · 16 unabsorbed | cited by 28 control-plane file(s) — it is wired in |
| `_ledgers` | **misc** | 2026-06-30 | 13 | 9 | 26 | — | cited by 9 control-plane file(s) — it is wired in |
| `re-compliance` | **misc** | 2026-07-28 | 4 | 1 | 10 | — | cited by 1 control-plane file(s) — it is wired in |
| `digital-product-lane-2026-08-05` | **misc** | 2026-08-05 | 3 | 1 | 4 | — | cited by 1 control-plane file(s) — it is wired in |
| `mybpm-merch-os-run-1` | **mybpm** | 2026-07-29 | 13 | 2 | 29 | — | cited by 2 control-plane file(s) — it is wired in |
| `pmf-offer-shelf` | **offer-strategy** | 2026-08-07 | 13 | 1 | 16 | — | cited by 1 control-plane file(s) — it is wired in |
| `alignment-architect-2026-07-07` | **offer-strategy** | 2026-07-29 | 11 | 1 | 23 | — | cited by 1 control-plane file(s) — it is wired in |
| `path-decision-2026-07-01` | **offer-strategy** | 2026-08-07 | 9 | 3 | 12 | — | cited by 3 control-plane file(s) — it is wired in |
| `offer-rederivation-2026-07-25` | **offer-strategy** | 2026-07-26 | 6 | 1 | 11 | — | cited by 1 control-plane file(s) — it is wired in |
| `positioning-cowork-2026-07-25` | **offer-strategy** | 2026-07-28 | 2 | 1 | 12 | — | cited by 1 control-plane file(s) — it is wired in |
| `pmf-brief-2026-07-07` | **offer-strategy** | 2026-07-15 | 1 | 0 | 5 | — | worked on 22d ago |
| `pmf-offer-map-2026-07-07` | **offer-strategy** | 2026-07-15 | 0 | 0 | 5 | — | worked on 22d ago |
| `pmf-ofm-options-2026-07-07` | **offer-strategy** | 2026-07-15 | 0 | 0 | 5 | — | worked on 22d ago |
| `kdp-book-one-pilot` | **publishing** | 2026-08-06 | 9 | 1 | 11 | — | cited by 1 control-plane file(s) — it is wired in |
| `video-studio-shakedown` | **video-studio** | 2026-08-06 | 6 | 1 | 47 | — | cited by 1 control-plane file(s) — it is wired in |
| `disney-crowd-app` | **video-studio** | 2026-07-28 | 2 | 1 | 10 | — | cited by 1 control-plane file(s) — it is wired in |
| `remotion-studio` | **video-studio** | 2026-07-28 | 2 | 2 | 21 | — | cited by 2 control-plane file(s) — it is wired in |
| `prediction-market-arb` | **wagering** | 2026-07-28 | 7 | 2 | 31 | — | cited by 2 control-plane file(s) — it is wired in |

## ARCHIVE? — cold and unreferenced — 1

My read is these are done. Archiving moves them to `_active/_archive/2026-08-07-sweep/` with every referrer repointed — reversible, nothing deleted. Tell me any you intend to pick back up.

| project | proposed arena | last | refs | ctrl | files | debt | why |
|---|---|---|---|---|---|---|---|
| `strategic-clarity` | **offer-strategy** | 2026-06-30 | 1 | 0 | 5 | — | cold 37d, only 1 inbound ref(s) |

## FREEZE — repo snapshots, never touched — 1

These contain their own `_active/` tree. Rewriting inside them edits what the snapshot recorded. No decision needed.

| project | proposed arena | last | refs | ctrl | files | debt | why |
|---|---|---|---|---|---|---|---|
| `codex-harvest-2026-06-11` | **harness** | 2026-08-07 | 141 | 5 | 4363 | 86 competing | a copy of this repo — never restructure or rewrite inside it |

## Dupes needing a call

Byte-identical duplicates are decided by `diff` and never reach you. Non-identical ones are listed per project in that project's `START-HERE.md` under **Competing versions** — I will surface the specific pairs for whichever projects you keep, once the arenas are settled.

---

**SUPERSEDED 2026-08-07.** This is the proposal, not what shipped. Farrice folded the eight client arenas into one `clients/` (66 folders -> 10 arenas, not 18) and archived the cold folders. What actually ran is `.agent/organization/sweep-plan-2026-08-07.json`; what the tree looks like now is each arena's generated `START-HERE.md`.
