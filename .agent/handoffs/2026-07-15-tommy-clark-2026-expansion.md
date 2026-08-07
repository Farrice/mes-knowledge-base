---
thread: tommy-clark-2026
status: ready
resume_hint: Farrice judges blind-pass side-by-side for A-tier, then run /tc-uncopyable-filter on linkedin-launch drafts
unfinished: A-tier verdict pending; first real-post moat audit not yet run
branch: main
pin: true
---

# Tommy Clark LinkedIn OS — 2026 Three-Moat Expansion (forge+amplify)

## Purpose
- **Next session should do:** (1) Farrice judges the blind-pass side-by-side for A-tier promotion; (2) deploy `/tc-uncopyable-filter` on Farrice's own LinkedIn launch content and Jen's client posts; (3) optionally build the first data-moat chart or TLA boost plan when a post proves ICP pull.
- **Not in scope:** Re-extracting Tommy Clark (v3.0 is complete — extend, never rebuild); re-running the prompt wiring backfill; touching the pre-existing dirty files (directives/*, knowledge/*, ethan-smith-aeo) that other tooling owns.

## Load First
- `skills/tommy-clark-linkedin-growth/SKILL.md` — v3.0 workflow table (6 workflows, 2 tiers) + stacking guide
- `skills/tommy-clark-linkedin-growth/genius.md` — 7 patterns, 5 hidden knowledge, 7 sourced anti-patterns, recognition test
- `extractions/tommy-clark/amplification-report-2026-07-15.md` — coverage map: what the 2026 video added and why
- `extractions/tommy-clark-linkedin-growth/blind-pass-sample-uncopyable-filter.md` — the side-by-side awaiting Farrice's A-tier verdict
- `skills/tommy-clark-linkedin-growth/references/source-ledger.md` — VERIFIED/LIKELY/UNCONFIRMED claim labels (note: "LinkedIn suppresses AI content" is UNCONFIRMED — never repeat as fact in client work)

## Current State
- **Objective:** Deploy Tommy Clark's 2026 LinkedIn strategy (Three-Moat System, TLA engine) for Farrice's own LinkedIn + clients.
- **What is already done:** Skill v2.0 → v3.0 shipped and pushed (commit `1595c6fff`): 4 new workflows (`uncopyable-post-filter`, `thought-leader-ad-engine`, `data-moat-visualization`, `physical-moat-library`), 4 born-v2 prompts wired (renaissance audit 0 fail), `/tc-*` slash wrappers, SKILL_INDEX + SLASH_COMMANDS registered, genius.md expanded, source ledger created, reference corpus (2 verbatim Social Files editions) collected, blind-pass PASS recorded (EVAL-038), heartbeat 5/6, finalize composite 8.3, forge_gate recorded.
- **What is uncertain or stale:** Blind-pass is model-judged only → skill sits at B-tier until Farrice's side-by-side verdict. `named_entity_floor` heartbeat check is marginal (0.24 vs 0.20, non-blocking). TLA edit-post CTA behavior is practitioner-reported (LIKELY) — re-verify in Campaign Manager before real client spend. `extractions/tommy-clark/visual-context.md` is deliberately gitignored (repo policy) — exists on disk only.
- **Latest proof/receipt:** Commit `1595c6fff` on main (pushed); blind-pass log `extractions/tommy-clark-linkedin-growth/blind-pass-log.md`; EVAL-038 in `evolution_store/ground_truth/eval_set_v1.jsonl`.

## Suggested Skills / Workflows
- `/tc-uncopyable-filter` — the deployment front door: audit any post for narrative/data/physical moats
- `/tc-tla-engine` — once a post proves ICP pull, build the $30/day boost plan (Apollo list + edit-post CTA)
- `/tc-data-moat` + `dataviz` skill — first Carta-pattern chart from proprietary data
- `/farrice-engine` or `/ghostwrite` × `/tc-uncopyable-filter` — moat-gate any LinkedIn deliverable before shipping
- `/jen-santulan` × `/tc-physical-moat` — listings are born-physical; upgrade her content framing

## Exact Next Prompt
```text
Read extractions/tommy-clark-linkedin-growth/blind-pass-sample-uncopyable-filter.md and the two reference-corpus pieces next to it. I'll give my gut verdict on whether the sample passes as Tommy Clark's method (A-tier) or not. Then run /tc-uncopyable-filter on my 5 most recent LinkedIn drafts from _active/linkedin/ and give me the moat audit table for each.
```

## Acceptance Criteria
- Farrice has rendered a PASS/FAIL felt verdict on the blind-pass sample (recorded via `blind_pass.py record` if it changes tier)
- At least one real post (Farrice's or Jen's) has been through the Three-Moat filter with a named moat declaration
- No UNCONFIRMED ledger claim appears as fact in any delivered content

## Risk Notes
- Source is a single 3,614-word video — fidelity-sized to 4 workflows deliberately; don't inflate beyond source
- TLA mechanics (PS-line survives boost; no-CTA-button objectives) are platform behaviors subject to change — re-verify before spending client budget
- Concurrent-tool caution: working tree had pre-existing modifications from other tooling (ethan-smith-aeo, directives) — left uncommitted on purpose; GOLDEN RULE applies
