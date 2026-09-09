---
date: 2026-07-27
session: compass doctrine gate audit
name: compass-doctrine-blocking-gate-audit
problem_class: harness / gates / overcorrection
domain: harness
status: proven
problem_signature: "the system keeps interrupting shipping — a finalize refuses over a missing flag, a stale mirror halts a creative run, a routing trial blocks a prompt on one keyword — and it feels like the harness is overcorrecting and trapping the operator, with more gates scheduled to switch themselves on by date"
tags: [gates, compass-doctrine, enforcement, trials, chain-runner, directives]
---
# Solution Card — the enforcement layer was scheduled to cage itself

**Date:** 2026-07-27 · **Domain:** control plane / harness · **Trigger:** Farrice, mid-flow: *"the system is overcorrecting and trapping me"*

## The problem

Across one working session the system interrupted shipping four separate times:

1. `chain_runner finalize` **refused** — `ANCHOR REQUIRED`, because a dimension scored 8 without `--anchor-named`. Work was clean; the refusal was about a flag.
2. `chain_runner finalize` would also have halted on a **stale Notion mirror** (>72h). A memory-sync job's freshness gating a creative finalize.
3. The **routing binding trial** injected `MANDATORY BINDING matched ★ /ward-rhetorical-engine` on a prompt that described a *prose-classifier false positive*, because the word "anaphora" appeared in it. In enforce mode that returns `decision: block` and demands a `!route` token.
4. Prose gates and doc-level "BINDING / non-negotiable / hard stop" language produced hesitation three more times on the send-before-build rule.

## What the audit found

The live blocking surface, measured rather than assumed:

| Gate | State found | Verdict |
|---|---|---|
| `cost_gate_hook.py` | `sys.exit(2)` ×3, **LIVE** | **KEEP** — guards money, not quality |
| `.agent/routing-enforce-trial.json` | `active: true`, blocks prompts, `!route` to override | **DISARMED** |
| `chain_runner` anchor / blind-pass / learning-debt latches | refuse, `sys.exit(1)` | **→ nudge** |
| `chain_runner` notion_mirror staleness | `status: halted`, returns early | **→ nudge** |
| `chain_runner` factual veto (`--factual` < 6) | blocks delivery | **KEEP** — only fires on already-known-bad facts |
| `session_ledger_hook` :582 / :669 / :719 | `decision: block`, gated on `ENFORCE` | dormant, and the trial that would arm them is disarmed |
| `steering_loop_hook` :258 | `decision: block`, gated on trial | dormant, trial disarmed |
| `fleet_write_guard`, `active_tool_lock`, `menu_parity`, `offer_gate`, `forge_gate` | warn / auto-fix / advisory | already fine |

**The actual finding is the schedule.** `.agent/enforce-trials/` held three gates queued to flip `active: true` on their own, one per week: `blind_pass` (due 07-24, overdue), `ledger_debt` (07-31), `steering` (08-07). Each file carried the instruction *"ON THE DUE DATE flip active:true."* Left alone, the system would have become progressively more locked without anyone deciding to lock it.

A ratchet with no pawl on the release side isn't governance. It's drift with a calendar.

## The fix

**Code** — `chain_runner.py` gets a `COMPASS_MODE` constant (default on) and a `_compass(result, msg)` helper. Each latch site becomes `if err and _compass(result, err):` so the latch records a warning and execution continues. `print_result` surfaces them as `🧭 NUDGE (did not block)`. `COMPASS_MODE=0` restores old behaviour for a single run.

**State** — all four trial files set `active: false` with a `disarmed` stamp, a `compass_doctrine` field, and `activation` rewritten to *"Never auto-activate on a date."*

**Prose** — CLAUDE.md's "Deterministic Enforcement Layer (these gates are PHYSICAL)" became "Compass Layer (nudges, not cages)" with the doctrine at the top. "Non-negotiable" → "Expected, not enforced." "binding" → "expected." "hook-enforced" → "observe-only." `routing-bindings.md`'s offer row now says never hold a build or a send waiting on the red team.

## The rule

**Gate spend and gate known-falsehoods. Nudge everything else.**

Two failure modes to watch for, because both recur:
- **Process checks wearing correctness clothes.** "You didn't name the anchor" is not "your work is wrong." Anything that refuses should be able to point at the defect, not the paperwork.
- **Self-arming schedules.** Any file whose instructions include flipping its own enforcement on by date is drift. The only thing that should turn a block on is a person saying so.

A gate that cries wolf gets ignored, and an ignored gate is worse than no gate — the same lesson as [[2026-07-27-prose-gate-scaffolding-false-fail]], one layer up.

---

## Round 2 — the prose sweep and the Codex side (same day)

**Codex was already fixed, and that's the useful finding.** `.codex/tools/codex_hook_runner.py` is a pure subprocess pass-through to the same `execution/hooks/*.py` and reads the same trial files. Every compass change propagated with zero Codex-side work. Verified live: the exact `anaphora` prompt that blocked under the trial now returns exit 0 with an advisory line. **There is no separate Codex enforcement state to maintain** — do not go looking for one.

**One genuine Codex-only bug.** `codex_dangerous_git_guard.py` blocked `\bgit\s+push\b` — *all* pushes — while `feedback_all-work-on-main` says commit and push main every session. The Claude-side `.claude/hooks/block-dangerous-git.sh` never had that pattern, so this was a drifted copy, not a policy. Narrowed to `git push` + `--force`/`-f`. Verified: plain push allowed, force push blocked, `reset --hard` and `clean -fd` still blocked.

**Related false positive, not fixed:** the git guards substring-match the whole command line, so they also block commands that merely *contain* the text — a shell one-liner testing the guard gets blocked by the guard. Annoying, low stakes, and the safe direction to fail. Noted rather than loosened.

**Directives sweep: 83 cage-language lines → 55.** 27 lines across 20 files softened, by script, dry-run reviewed twice before applying. The dry run is what made it safe — the first pass would have rewritten `routing binding` → `routing standing` (mangling a term of art tied to `routing_enforcer.py BINDINGS`), rewritten historical rows in an evolution log, and — worst — softened `cost_gate ... HARD BLOCK` to `FIRM NUDGE` in `system-primitives.md`, because the immune-list pattern said `cost gate` and the line said `cost_gate`.

Deliberately untouched: spend policies (fal/apify/perplexity/notebooklm/google), `merge-discipline.md` (tree-corruption integrity), `browser-automation-safety.md`, historical logs, the factual-veto line in `verification-agent-protocol.md`, and every use of "binding" as a technical noun.

**Second-order rule learned:** when softening language at scale, the immune list is more important than the substitution list, and it will be wrong on the first try. Dry-run, read every diff, fix the immune list, dry-run again. A blanket sed over 90 directives would have silently disarmed the one gate that guards money.

Related: `feedback_compass-doctrine-no-blocking-gates` · `feedback_cos-compass-not-cage` · `project_deterministic-enforcement-rebuild`
