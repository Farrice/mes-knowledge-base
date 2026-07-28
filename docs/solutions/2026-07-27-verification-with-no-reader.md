---
name: verification-with-no-reader
problem_signature: "verification machinery that reports to a log file nobody reads is indistinguishable from no verification"
domain: system
tags: [hooks, verification, false-green, negative-control, observability, opus-5]
date: 2026-07-27
status: active
session: "a919a6cd"
---

## Problem

Farrice: *"There are so many times where I've been fooled into confidently
believing that things are being done and they're not."* The felt shape was:
deep in flow, using commands and workflows, then at the finish line intuition
alarms — something is off — and the session flips into backtrace-and-repair
instead of ship-and-move-on.

The obvious hypothesis (files silently don't get written) was **wrong**.
Measured across 400 transcripts / 9.5 days: 45 repo paths were asserted as
created/wired; **44 existed on disk.** Writing was never the failure.

## Root Cause

**Proof with no reader.** Every signal already existed and every one of them
reported into a dead channel:

| Signal | Where it went | Who read it |
|---|---|---|
| `verify_fleet.py` — 73 verifiers, **12 failing** | `.agent/health/fleet.log` | nobody |
| `citation_integrity.py` — 2 broken pointers | `.agent/citation-integrity.log` | nobody |
| session ledger — every skill load | `.agent/sessions/ledger-*.json` | nobody |
| `content_creation_gate` floor (>= 2 skill files) | `directives/*.md` prose | never checked |
| Opus 5 dialect rules | `CLAUDE.md` prose | may or may not be read |

Same class as the PARTNER dial firing zero times for eleven days: **a rule in
a channel that doesn't execute is not a rule.** Measured cost of the unchecked
gate: 43 sessions wrote a deliverable, **29 read fewer than 2 skill files, 13
read zero.**

Opus 5 makes this *feel* worse without making it worse: it self-verifies and
narrates the verification into visible output (dialect probe P2 — appended
"verified by count" unasked). Confidence in the prose went up; the proof
channel stayed dark. That gap is the "fooled" sensation.

## Approach That Worked

1. **Read before building.** `skill_grepped` — half the intended mechanism —
   had shipped the previous day. The build became an extension, not a rebuild.
2. **Extend the channel that already fires.** Manifest capture went into
   `session_ledger_hook.py` (PostToolUse, already firing ~2,800×/9 days at
   31 ms). No new subsystem, no new command to remember.
3. **Separate observation from debt.** The manifest never accrues debt and
   never blocks — compass doctrine. `execution_receipt.py` is a pure renderer.
4. **Withhold, never infer.** Ledgers written before the manifest have no
   depth data. They are marked `legacy` and manifest-derived flags are
   suppressed. Absent data is reported as absent.
5. **Negative-control every check** (see Verification). A test that has never
   failed has not been tested.

## Dead Ends

- **A "translator skill" for Opus 5 intent.** Farrice's opening frame. Wrong
  layer: the dialect card is explicit that length responds only to prompting,
  and a skill you must remember to invoke is the same dead channel as prose
  you must remember to read.
- **A claim-vs-disk regex auditor.** Built it, ran it, results were noise
  ('both', 'their', 'day-one' as skill names). Discarded rather than quoted.
- **Migrating skills to agents/plugins.** Agent definitions are resident
  *always*: 12 agents = ~4.3k tokens, so 378 would be ~134k before typing.
  Skills are lazy. The real axis is resident vs lazy, not skill vs agent.

## Verification

Four negative controls — the check must fail when broken, in both directions:

| Control | Sabotage | Result |
|---|---|---|
| 1 | manifest capture disabled | 5 FAIL ✓ |
| 2 | UNDER FLOOR silenced (**false green**) | 1 FAIL ✓ |
| 3 | UNDER FLOOR always fires (**false red**) | 1 FAIL ✓ |
| 4 | original short `DELIVERABLE_ROOTS` restored | 2 FAIL ✓ |

`python3 execution/verify_execution_receipt.py` → 34 pass / 0 fail. Joins the
Sunday fleet automatically via `execution/verify_*.py` glob.

**The bug the receipt found in itself, and the wrong diagnosis of it.**
First real run: `_deliverables()` returned `[]` for every session, silently
killing UNDER FLOOR — a false green produced by the anti-false-green check.
First stated root cause: "absolute-path substring matching." **That was
wrong** — `guides/` is a substring of the absolute path too. Proven by
reverting and watching the regression test still pass. Actual cause:
`DELIVERABLE_ROOTS` shipped without `guides/ docs/ skills/ execution/`. The
test now exercises *every* declared root, because an unexercised root is an
untested root.

Earlier the same session, a launchd health check reported **16 scripts
MISSING**. Also false — the grep broke on the space in "Google Antigravity".

## Weaker-Model Trap

Three traps, all of which produce a confident-and-wrong result:

1. **Declaring victory on a first-run green.** 24/24 passed immediately. A
   suite that has never failed proves nothing. Sabotage it and watch it fail
   *before* trusting it.
2. **Reporting the first plausible root cause.** "Absolute paths" explained
   the symptom and was false. Re-introduce the alleged cause; if the test
   still passes, the diagnosis is wrong.
3. **Inferring from absent data.** Legacy ledgers have no `genius_read` field.
   Flagging TIER 1 ONLY there is a false RED, which destroys trust in a
   reporter exactly as fast as a false green.

Also: **never assume a shell one-liner is right because it ran.** Paths in
this repo contain a space. `grep -oE '[^ ]+\.py'` and bare `$var` both break.

## Pointers

- `execution/execution_receipt.py` — renderer + CLI (`--all`, `--json`)
- `execution/hooks/session_ledger_hook.py` — `_empty_manifest`, `_mf_add`, `_emit_receipt`
- `execution/verify_execution_receipt.py` — 34 checks, 4 negative controls
- `.claude/settings.json` — PostToolUse matcher widened with `mcp__recall__.*`
- `directives/model-dialects/claude-opus-5.md` — P2 self-verification narration
- Related: `docs/solutions/2026-07-13-divergent-branch-work-silently-lost.md`
