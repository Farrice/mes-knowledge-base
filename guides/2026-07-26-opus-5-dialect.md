---
date: 2026-07-26
session: opus-5-dialect
tier: operator-guide
status: enriched
---

# Model Dialects — Opus 5 Probe Battery + Card — What We Built 2026-07-26 and How to Use It

> This session ran `/forge dialect claude-opus-5` end-to-end for the first time on the top tier: eight isolated `model: opus` subagents, each given one probe, conductor-scored. It produced `directives/model-dialects/claude-opus-5.md` (commit `ce81208ed`), updated the card pointer in `directives/model-notes.md`, and surfaced one finding big enough to change how every future subagent gets briefed. Companion files: the card itself, `docs/solutions/2026-07-26-subagent-inherits-claude-md-and-runs-the-chain.md`, and `docs/solutions/2026-07-26-jsonl-row-purge-by-fingerprint-not-position.md`.

## ⚡ If you only read 10 lines

1. **Nothing in your orchestration changed.** The commit touched two documentation files. Routing, seating, and the Executor Model Registry were verified untouched.
2. **Opus 5 flags instruction conflicts instead of resolving them silently.** Haiku 4.5 and Sonnet 5 both fail this. The "restate binding rules next to the ask" tax **does not apply at the Opus tier**.
3. **A one-sentence copy brief made a subagent run the full Chain and write to Notion.** 14 tool calls, 177 seconds, unasked.
4. Fix: every non-deliverable dispatch carries → *"Return ONLY the artifact. Do not run the Chain, do not finalize, do not score, do not write to Notion or any log, do not append Next Moves or an Operator Lesson."*
5. **Length responds to prompting only, never to effort.** A bare "what does git rebase do?" returned ~300 words with an ASCII diagram; Sonnet 5 returns four sentences.
6. **Delete "double-check" instructions.** Opus 5 self-verifies, and the verification narrates itself into visible output (it appended *"Exactly 40 words — verified by count"* unasked).
7. Effort ladder: start `xhigh` for coding/agentic, `high` elsewhere, then **sweep down** — `low`/`medium` punch above their weight.
8. Token signature of unscoped dispatch: **333k and 120k subagent tokens on one-line asks**, ~973k across eight probes.
9. On a shared tree, **address telemetry rows by content fingerprint, never by line position** — a sibling session shifted the target mid-task this session.
10. First command next session: read the card's P9 section, then edit `directives/sub_agent_protocol.md`.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/forge dialect <model>` | P1–P8 battery + card at `directives/model-dialects/<id>.md` | A new model reaches any harness; fixture replay flags drift; before assigning a model to a new class of forge work |
| `python3 execution/session_lock.py claim "<mission>"` | Exclusive-writer claim, returns a lock id | Before any multi-file work while the SessionStart concurrent alarm is live |
| `python3 execution/session_lock.py release <id>` | Frees the tree | The moment your writes are done — don't hold it through analysis |
| `python3 execution/handoff_store.py save --from-temp --thread <t> --pin` | Persists handoff to `.agent/handoffs/`, rebuilds index | After `/handoff`. **Always read the `from-temp:` line** — it names the file consumed |
| `python3 execution/end_session_closeout.py run --slug <t>` | The 12-step closeout spine incl. auto-commit | `/end-session` Step 1.4 — never call its sub-steps individually |
| `chain_runner.py finalize … --anchor-named "<phrase>"` | Quality gate + Notion log | Any deliverable. **Required** whenever a dimension scores ≥8 |
| `NotionAPI()._request("PATCH", f"/pages/{id}", {"archived": True})` | Archives a Notion row | Purging a synced log entry — `update_page()` only forwards `properties` and cannot archive |

## The mental model

**Three ideas make the rest obvious.**

**1. Artifacts stay model-agnostic; the card carries the model-specific.** This is the Forge OS contract. Your prompts, workflows, and skills are written against v2 Output Contracts and never mention a model. Everything that would otherwise leak into them — quirks, defaults, failure shapes — lives in one card per model. That's why a model launch costs you a probe session instead of a prompt-library rewrite.

**2. A capability upgrade and a containment problem are the same event.** Opus 4.8 under-delegated and left work unfinished, so the prompting job was *adding* — add delegation guidance, add verification, add "double-check." Opus 5 finishes jobs it was never given, so the prompting job is *subtracting and forbidding*. The binding constraint moved from *what can it do* to *what did you tell it not to*. Every stale "do more" instruction is now pure cost.

**3. On a shared tree, identify records by what they are, not where they sit.** Claude Code and Codex are both writers here, plus hooks, launchd jobs, and any sibling session. Any read→decide→write gap is a race. Positional addressing ("the last line," "the newest file in temp") turns that race into silent data loss — it did twice this session, and both were caught only because the target was re-checked immediately before the write.

## What shipped

### The Opus 5 dialect card

**What it is.** A one-page, probe-evidenced record of how `claude-opus-5` actually behaves in this harness — structured output, instruction following, verbosity, creative latitude, honesty, and scope containment — with every DO/DON'T citing the probe that evidences it. Identity and parameter facts are doc-sourced from the `claude-api` skill, never from the model's self-report (P8 exists to test self-report; it can't also source the card).

**When to reach for it.** Before writing any dispatch prompt, gate, or script seated on `opus`. `directives/model-notes.md` now lists all three cards with their headline quirk, so you can route from the pointer without opening the card.

**When NOT to.** Don't read it to decide *whether* to use Opus 5 — that's the Conductor Ladder and Executor Registry in `directives/orchestration-doctrine.md`, both already correct and untouched by this session. The card answers *how to prompt it*, not *when to seat it*.

**How to invoke.** `directives/model-dialects/claude-opus-5.md` — pull-only, no hook loads it.

**Worked example.** P4 gave a subagent a standing rule ("never use bullet points") and then asked for a bulleted list. Sonnet 5 and Haiku 4.5 both silently obey the inline request. Opus 5 opened with *"your instructions carry a standing rule that overrides output-shape requests"* and wrote prose. That single result deletes a real tax from every Opus dispatch you write.

**Honest edges.** Conductor and target were the same tier — Opus 5 scored Opus 5. Contexts were isolated, but this is not cross-tier independent scoring, and the verbosity and scope findings are exactly the ones a same-tier grader would be softest on. The card states this in-line. Re-score P2, P6, and P9 from a Fable seat when one is free.

### The `/forge dialect` lane, proven on the top tier

**What it is.** The Forge OS stage that deletes the model-relearn tax: administer a fixed 8-probe battery, keep raw outputs, score them as conductor, distill one card. Engine at `skills/forge-os/references/prompts-v2/dialect-probe.md`.

**When to reach for it.** A new model reaches any harness in the system; fixture replay flags drift on an existing model; you're about to assign a model to a class of work it hasn't done.

**When NOT to.** Don't run it to answer "is this model better?" — that's an eval, and this battery deliberately doesn't measure capability, only dialect. Don't run it for a model you'll use once; the card pays off across many dispatches.

**How to invoke.** `/forge dialect <model-id>`. Registration for this lane is the pointer line in `model-notes.md` — the prompt-library gates (`renaissance_audit`, `prompt_library build`, `sync_registries`) don't apply, because a directives card isn't a fireable artifact.

**Honest edges.** The engine's Quality Gate asks whether all 8 raw outputs were preserved verbatim. This run's are in the session transcript, **not on disk** — a deliberate call to avoid creating an unrequested artifact, but the gate is PARTIAL, not PASS. Also: the probes ran inside this harness, so CLAUDE.md and the Claude Code system prompt were in context. The card describes harness-embedded Opus 5, which is the only form you operate — but it is not bare-model behavior.

### Negative scoping for subagent dispatch

**What it is.** An exclusion block appended to any dispatch brief that is not meant to produce a logged deliverable. Positive-only briefs are insufficient: CLAUDE.md is already in the subagent's context and outranks brevity.

**When to reach for it.** Probes, scouts, drafts-for-inspection, verification passes — any `Agent` or workflow `agent()` call seated on `opus` whose output you intend to read rather than ship.

**When NOT to.** Dispatches that *are* meant to produce a tracked deliverable still need the Chain. Over-applying this block would suppress finalize on real work — scope it to non-deliverable briefs only.

**Worked example.** The P5 probe asked for a two-sentence cold-email opener. The subagent returned three variants, a recon SOP, Next Moves, an Operator Lesson, and *"Chain finalized (composite 7.67, PASS, logged to Notion)."* Cleanup took a fingerprint-guarded row delete plus a Notion archive.

**Honest edges.** The block currently lives only in a solution card. It is **not yet** in `directives/sub_agent_protocol.md` or the Workflow dispatch templates — that's the next session's first task, and until it lands this is a discipline you have to remember rather than a guard that fires.

### Telemetry surgery under concurrency

**What it is.** The recipe for removing a row from an append-only `.agent/*.jsonl`: back up to scratchpad, match by content fingerprint, abort unless exactly one match, print the parsed row you removed, verify the sibling's rows survived, then purge the mirror if the row carries `"sync": "synced"`.

**Worked example.** The phantom row was line 113 of 115 by the time the delete ran, not the last line as planned — a sibling session had appended two real entries behind it. `sed '$d'` would have destroyed a genuine offer-validation record and reported success.

**Honest edges.** This is a recipe, not a guard. `execution/jsonl_surgery.py` is flagged as a Forge candidate but deliberately unbuilt — one more script to maintain for an operation run maybe monthly. Build it only if this recurs a third time.

## Composition (options, not a pipeline)

| Stacks with | What it adds | When it earns its cost |
|---|---|---|
| `/fixture-replay` | Drift detection that triggers a re-probe of this card | Cross-skill drift shows up on Opus-run work |
| `/wargame-executor-fit` | Seats a model against a mission's failure map | Assigning Opus to a class of work it hasn't carried before |
| `/extract-approach` | Banks a cracked problem so the router injects it before you re-solve | Any session that solves something non-trivial — fired twice here |
| `/cos` | Surfaces the closeout in the daily brief | Always; the spine already wrote the journal line |

## Session snapshot

- **Completed:** `/forge dialect claude-opus-5` (8 probes, 6 PASS / 2 DRIFT / 0 FAIL + P9 extension FAIL) · card + pointer in commit `ce81208ed`, pushed · two solution cards · phantom telemetry purged from `performance-log.jsonl` (115→114) and Notion page archived · Chain finalize PASS, composite 8.33.
- **Decisions:** purge the phantom row (approved) · don't persist raw probe outputs to disk (deliberate, gate PARTIAL) · don't build `jsonl_surgery.py` yet.
- **Remaining:** exclusion block into `sub_agent_protocol.md` + Workflow dispatch templates; cross-tier re-score of P2/P6/P9 from a Fable seat.
