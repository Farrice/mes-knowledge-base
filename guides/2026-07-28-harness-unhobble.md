---
date: 2026-07-28
session: harness-unhobble
tier: operator-guide
status: enriched
---

# Harness Unhobble — What We Built 2026-07-28 and How to Use It

> The session that applied Anthropic's Claude-5 context rules to the whole harness: CLAUDE.md dieted 56%, the enforcement ecology cut from 60 orphans to 9, the seating charter ratified, and the Gemini Ultra research path repaired and verified live. Companions: `docs/solutions/2026-07-28-claude5-context-rules-six-shifts.md` (the rubric), `knowledge/council-sessions/2026-07-28-seating-charter-harness-diet-ratification-contex.md` (the deliberation), `research_outputs/2026-07-28-graph-engineering-deep-research.md` (the same-day hype contrast case).

## ⚡ If you only read 10 lines

1. Primary source for everything here: claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models (Thariq Shihipar, 2026-07-24) — "removed over 80% of Claude Code's system prompt… no measurable loss."
2. CLAUDE.md is now 1,601 words (was 3,672). Restore point: commit `32965d24b`. Cut text: `directives/archive/claude-md-cut-2026-07-28.md`.
3. Constitution law: compress a marked block → remove its `<!-- BEGIN/END -->` markers or `platform_compiler.py compile` clobbers your edit. Bless with `python3 execution/platform_compiler.py sync` after any constitution change; `check` is the read-only drift probe.
4. The two-sided grounding test governs every rule/hook/tool: name a `consumer:` (code acts on it) or a `scar:` (dated wound it guards) — neither = archive to `execution/archive/` (delist, not delete; a doc-citation is a restock ticket).
5. Seating: Fable writes ONLY the closed hop-0 list (Parallax editions, cold offers, letters-to-JJ). Opus 5 = steady-state everything. No Fable seat → Opus 5 writes + Farrice's felt verdict arbitrates; park Fable-grade calls via `handoff_store.py save`, never stall.
6. Dialect cards now cover the live seat: `directives/model-dialects/claude-fable-5.md` (SEEDED — probe battery pending); verify injector anytime: `python3 execution/verify_dialect_injector.py` (26 checks).
7. Steering hook fires Next-Moves guidance on deliverable-classified prompts only; escalation counters are deleted. Miss logging stays observe-only in `.agent/sessions/steering-observe.jsonl`.
8. `wiring_audit.py` now proves via Python imports, skills/ prose, and docs/solutions — and excludes `execution/archive/`. Orphans 60 → 9; the 9 go to the next `/weekly-closeout` grounding pass.
9. Deep research is frontier-grade again: `python3 execution/research.py "<q>" --depth deep` → receipt must say `engine_used: gemini_deep`. If it says "prepayment credits depleted," the Studio key lost its Ultra plan link — fix at ai.studio/projects, never by rebuilding the engine.
10. Skills corpus: NOT dieted, on purpose — progressive disclosure means unfired skills cost zero. Diet a skill only when its output feels flat (rules→pointers, exemplars stay).

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/platform_compiler.py check` | constitution drift report (read-only) | after editing CLAUDE.md/GEMINI.md/AGENTS.md |
| `python3 execution/platform_compiler.py sync` | blessed baseline hashes | drift reviewed and intentional |
| `python3 execution/verify_dialect_injector.py` | 26-check injector health | new/edited dialect card |
| `python3 execution/wiring_audit.py status` | orphan count + sample (JSON) | pending-decisions nags about orphans |
| `python3 execution/research.py "<q>" --depth deep` | receipt-carrying research | any research; receipt engine line = billing health probe |
| `python3 execution/citation_integrity.py` | broken-pointer scan (325 sources) | after any archive/move; annotations `(deleted`/`(superseded`/`(planned`/`(not yet` skip honestly-absent files |
| `git mv <file> execution/archive/` + README line | deliberate delisting | grounding test fails; restock = `git mv` back |

## The mental model

**Always-loaded context is taxed every turn; invoked context is free until fired.** That single line decides everything: CLAUDE.md got the diet (always loaded), the 393-skill corpus did not (progressive disclosure). The next-largest resident item is now the skill *listing* (~13k est. tokens), not any file you wrote.

**On judgment models, the scar is the enforcement.** The council's stress-test caught the diet cutting dated wounds while keeping abstract rules — backwards. "Two rejected takes = stop" enforces nothing; "scar: 2026-07-27, eight headline rounds, 26k words unread" does.

**Maintenance that generates maintenance is hop-2+ and dies.** The 07-28 cleanup session deleted verifiers whose citations broke, which the next session had to clean. The grounding chain (human within two hops) is the exit from that loop — and the refusal clause matters most: no new trackers may be minted to govern the cleanup.

## Capability: the constitution diet (applied)

**What it is:** CLAUDE.md rewritten to the six shifts — rules→judgment, dedup vs hooks/cards, progressive disclosure — with the money/truth/loss gates (cost gate, factual veto, golden rule, Notion pin) kept verbatim. GEMINI.md's pre-compass "PHYSICAL gates" section replaced (it taught an extraction freeze Farrice killed in June).
**When to reach for it:** any always-loaded file that has accreted defensive prose for a model generation that no longer exists.
**When NOT to:** skills, genius.md files, exemplar bodies — they load on invocation and carry the product. Cheaper alternative: leave them; diet on felt-flatness only.
**How to invoke:** edit → `platform_compiler.py check` → review → `sync`. Marked blocks: strip markers before compressing (see line 3 above).
**Worked example:** this session — 2,071 words cut, two scars restored post-council, lint went from FAIL (GEMINI.md over 15,000 chars) to clean.
**Honest edges:** eval evidence is Anthropic's assertion, not published tables; HN carries first-day Opus 5 regression reports; the 5-session re-measure (baseline in the six-shifts card: 20% production share, composites 7.0–9.0) is the real verdict and hasn't happened yet.

## Capability: the grounding-chain archive (applied)

**What it is:** two-sided provenance (consumer/scar) applied wholesale — 3 steering-theater verifiers + 47 orphans archived, 4 restocked same-hour when doc-citations surfaced, 16 dead-session ledger debts cleared.
**When to reach for it:** pending-decisions lists orphans; a verifier is red for days with no shipped-artifact consequence.
**When NOT to:** anything with a live consumer (wiring_audit.py was 30 seconds from archiving itself — run the import/launchd cross-check first) or a dated scar.
**How to invoke:** the keep-test is one question — *has a finding from this thing ever changed a shipped artifact?* Mine handoffs/solutions for the receipt; absence = archive.
**Honest edges:** 9 orphans remain with ambiguous references — deferred to `/weekly-closeout`, not resolved. `verify_fleet.py` still calls two deleted scripts (known, uncorrected — grounding-grep territory).

## Capability: the seating charter (ratified, Fork-1B)

**What it is:** the hop ladder in `directives/orchestration-doctrine.md` § Seating Charter — who writes what, the Fable budget rule (name the consumer before the turn), the misseat log read only in `/weekly-closeout`, and the Fable-absent degradation clause.
**When to reach for it:** every session start on a non-Fable seat; any "should this run on Fable?" hesitation.
**When NOT to:** don't consult it for subagent seating — the dispatch seating law above it already covers that (`sonnet` grunt / `opus` heavy / conductor by exception).
**Honest edges:** the hop-0 closed list will face creep pressure ("voice-bearing" is an adjective); nothing enters without Farrice's explicit say. Fork 2's 7-day mute experiment was superseded by the calmed-hook middle path — conversion data never got collected.

## Composition (options, not pipeline)

| Stacks with | When it earns its cost |
|---|---|
| `/weekly-closeout` | owns the grounding grep, the 9 orphans, the misseat trend, the 5-session re-measure |
| `/wargame-run` | banking Fable-grade judgment as failure-maps before an Opus-only week |
| `/doctor` (in-session) | post-diet checkup ran 2026-07-28: healthy; stale 2.1.17 install at /usr/local awaits sudo removal; skill listing flagged as largest resident item |
| `handoff_store.py save` | parking Fable-grade calls when the seat is absent — charter behavior, not failure |
