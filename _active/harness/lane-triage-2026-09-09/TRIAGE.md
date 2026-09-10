# Lane triage — 2026-09-09 (record of one pass; the living count is `git for-each-ref` ahead-of-main)

Rule (Farrice, 2026-09-09): anything that merges clean lands with a one-line receipt; conflicts and dead lanes come back as a table with my call per row. No ref is deleted without his tap. Inventory basis: 64 refs ahead of main `6da8f9ded` (the session brief's "34" was low).

## LAND — landing now, receipts appended below as each merges

| Branch | ahead | what it holds | receipt |
|---|---|---|---|
| worktree-gigi-engine-run | 13 | Gigi nine-stage listing engine (demand report → carousel specs → render → judging page), 110-claim audit, BRAIN/VOICE | MERGED 15 commits / 369 files |
| codex/gigi-character-rebuild | 24 | The Calm Closer character system, property dossier launch system, editorial study, Unit 124 photography | PARKED by Law-3 (it deleted main's .agent state files) → merged into lane jen-launch-0909 with main as base, dropped files restored; lands with the lane |
| codex/rello-proof-pack | 6 | public-source creative proof pack, gatedrop spec | PARKED by Law-3 (deleted 4 recurring reports) → merged into lane with main as base; lands with the lane |
| codex/upwork-fiverr-cash-offers | 9 | marketplace cash sprint package, storefront + free channel kit, AI Council sample | MERGED 11 commits / 20 files |
| worktree-deep-research-ledger-fix | 4 | deep-research ledger fix, `main_drift_absorb.py`, `lane_reconciler.py` probe | PARKED (conflicts in a scratchpad handoff + .gitignore) → merged into lane, .gitignore union, main as base; lands with the lane. `main_drift_absorb.py` now exists |
| codex/solo-performance-creative-offer | 1 | solo performance creative test pack | MERGED 3 commits / 37 files |
| codex/oren-norton-arsenal | 3 | artifact-forge workflow + decision-table artifact pack | MERGED 4 commits / 62 files |
| codex/layout-composition-intelligence | 3 | satori composition brief owner + blind bakeoff | MERGED 5 commits / 70 files |
| codex/personal-brand-direction-diagnostic | 3 | 90-day creative direction + blind direction board | MERGED 6 commits / 21 files |
| codex/linkedin-800k-os | 5 | LinkedIn growth OS + first ten posts | MERGED 9 commits / 247 files |
| codex/pmf-health-linkedin-research | 1 | PMF verdict + source ledger | PARKED → merged into lane; main as base except `cost_gate_hook.py` (took the branch's research.py gemini patterns; self-test OK 13/9); lands with the lane |
| codex/systems-thinking-global-shadow | 2 | `verify_global_adaptive_judgment_floor.py` canary | MERGED 6 commits / 29 files |
| codex/nicolas-cole-first-dollar | 1 | first-dollar workflow + agent | MERGED 4 commits / 51 files |
| codex/signal-fidelity-shadow | 6 | six adversarial fixtures for the shadow fidelity layer | PARKED → merged into lane; main's primitives kept with the branch's two SHADOW sections appended (advisory, optional); fixtures land with the lane |

## REVIEW — my call per row (his tap to proceed)

| Branch | ahead | holds | overlap | my call |
|---|---|---|---|---|
| claude/sweet-chatterjee-785901 | 10 | today's Jen content session (hook room 11, code-words Sat 9/12) | 27/40 incl. jen.md, ENGINE-V2, WINNERS | **wait**: live session; it auto-merges at its end; if it parks, reconcile the three living docs by hand (main is base) |
| worktree-jen-reset-one-spine | 2 | the Sept 2 reset | 36/36 | **dead after today**: landed on main this morning by path checkout; delete ref |
| codex/jen-revenue-recovery | 7 | demo-to-offer path, First Home Valley handoff, roundtable scope | 28/92 (.dc.html canvases) | **cherry-pick files**: take `_active/clients/jen-santulan/deliverables/first-home-valley-ready/*` records; skip canvases |
| codex/jen-valley-tradeoff-30day | 3 | Valley Tradeoff 30-day test pack; condo-vs-house map | 2 | **land** (condo topic is dead on the grid; the test pack is a record, harmless) |
| worktree-gigi-concept | 12 | creative brief + SB 326 finding + 21-board rewrite | 9/75 (realtor-editorial DESIGN.md) | **merge after gigi-engine-run**; resolve DESIGN.md with main as base |
| worktree-vosler-7fig-extract | 8 | Vosler skill + 5 workflows + surface_router registry + 206-verbatim language bank | 19/89 (indexes) | **land**: overlaps are generated indexes; regenerate after |
| worktree-style-vault | 16 | style vault + brand-image pipeline + realism-floor linter | 8/41 | **land**: memory says Style Vault is LIVE; main lacks it → real gap |
| worktree-mailroom | 7 | agent-to-agent council layer, Mailroom protocol, live roundtable | 86/100 | **cherry-pick**: `directives/agent-mailroom.md` and `roundtable-live.md` are already on main; diff the rest and take only new files |
| worktree-farrice-character-sheets | 4 | photoreal Soul canon + 22-image calibration | 3/61 | **land** |
| codex/parallel-lanes-reliability-closeout | 10 | serialized closeout + lane sealing; non-mutating self-heal | 85/92 (AGENTS.md, CODEX.md, end-session.md) | **review in Phase 3**: high value, high conflict; port `end-session.md` logic by hand |
| codex/gtm-ezpoq8 | 3 | Jordan Crawford GTM OS | 89/94 | **park**: near-total overlap; check whether main already has it |
| codex/joanna-brand-voice-moat | 7 | voice-moat pipeline + client discovery demo | 12/70 | **land** |
| codex/marketing-engineering-service-recovery | 3 | marketing-engineering capability + health creative pilot | 8/33 | **land** |
| codex/multipassionate-focus-system | 7 | Breadth-to-Leverage coaching OS | 5/58 | **land** |
| codex/pej-preservation-closeout · codex/pej-final-closeout · codex/health-performance-evidence-journal | 8 · 9 · 10 | three PEJ closeouts | 3 · 1 · 70/74 | **collapse to one**: land `pej-final-closeout` (lowest overlap), then diff the other two for files it lacks; delete the rest |
| codex/health-performance-method-card | 5 | claim-bounded creative-test method card | 11/40 | **land** |
| codex/control-beater-buyer-test | 4 | smallest buyer test, warm send pack | 4/4 | **cherry-pick** the send pack files |
| codex/nicolas-cole-20m-course-lessons | 5 | scaling decision system | 6/34 | **land** |
| codex/fitness-business-copilot | 3 | fitness copilot package | 6/75 | **land** |
| codex/mybpm-product-image-standard | 6 | MyBPM image standard, wordmark lock | 9/16 | **land** |
| codex/portable-brief-export | 5 | portable brief bundles + client delivery room | 3/26 | **land** (supersedes the two briefing-room lanes) |
| codex/kallaway-frozen-client-proof | 2 | Kallaway fixture through growth blueprint | 17/17 | **park**: 100% overlap; likely already on main |
| codex/linkedin-creator-forge-0908 | 1 | tommy-linkedin-post-system skill + command | 3 | **land** |

## DEAD — delete on his tap (auto-generated churn or superseded)

seal-only / state-file churn: codex/kallaway-proof-integration · worktree-broke-agent-2026-playbook-forge · codex/paolo-linkedin-2026 · codex/creative-strategy-demand-20260811 · worktree-jen-tonight
superseded by portable-brief-export: codex/briefing-room-card-integrity · codex/briefing-room-gtm-preview
closeout bookkeeping only: codex/expert-practice-os-closeout · codex/linkedin-pmf-closeout · codex/priestley-universal-closeout · worktree-second-brain-awakening · worktree-apify-decommission · claude/nostalgic-lalande-e1ce93 · claude/vigilant-leakey-5f6293
dirty-main snapshots (100% overlap): codex/main-dirty-preserve-20260828-reader-bridge · codex/main-dirty-preserve-20260907-niche-closeout · worktree-main-dirty-preserve-20260905-closeout-integration-blocker · worktree-main-dirty-preserve-20260909-fladlien-integration
single pulse snapshots (remote-only): origin/worktree-market-pulse-2026-08-31 · -0903 · -2026-09-07 · origin/worktree-platform-pulse
rewritten on main since: codex/zero-momentum-offer · codex/operator-card-packaging · claude/dazzling-cannon-6ed186

Delete command (his tap, one line each): `git branch -D <branch>` for local refs; `git push origin --delete <branch>` for remote-only.

## Capabilities that were lying dormant (now landing or queued)

`main_drift_absorb.py` + `lane_reconciler.py` probe · serialized Codex closeout · six signal-fidelity fixtures · satori composition-brief owner · artifact-forge · joanna voice-moat pipeline · nicolas-cole first-dollar agent · tommy LinkedIn post system · five Vosler workflows + surface_router · the Gigi nine-stage engine · global adaptive-judgment canary.
