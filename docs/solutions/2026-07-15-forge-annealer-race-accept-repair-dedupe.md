# Concurrent Annealer Racing a Live Forge: Accept → Repair → Dedupe, Never Revert

**Date**: 2026-07-15 · **Domain**: system / extraction forging · **Origin**: jeremy-haynes-cold-offer forge session

## Problem

During a live `/extract-forge` build, the harness's annealing machinery (see
[[2026-07-14-cold-start-probe-anneals-new-engine-prompts]]) rewrote prompt files mid-session AND
forged additional assets the conductor never authored: two extra prompts-v2 files, two extra skill
workflows, two extra slash wrappers, an AGENT.md expansion, and a SKILL_INDEX row. Three failure
shapes resulted: (1) annealed rewrites dropped audit-required sections (`## Output Skeleton`),
(2) new wrappers pointed at skill workflows that didn't exist yet at wrapper-creation time,
(3) two prompts covered ONE deliverable (author's + annealer's) — a duplicate the spec forbids.
A conductor that reverts the annealer's files fights its own harness; one that blindly trusts them
ships audit failures and dangling pointers.

## Solution

Treat the annealer as a co-author whose work merges on the conductor's terms:

1. **Accept** — never revert annealed/added files; they often carry harness-native improvements
   (the annealer's articulation-brief prompt had VERIFIED/LIKELY/UNCONFIRMED labeling and a
   proof-to-hook map the hand-written version lacked — it won the dedupe).
2. **Repair to spec** — run `renaissance_audit.py` immediately after any anneal wave; add missing
   required sections (Output Skeleton was the repeat offender), and fix H1→H2 section headers
   (the audit only recognizes `## `-level section names).
3. **Resolve dangling pointers** — `ls` the wrapper dir vs. the skill workflows dir; any wrapper
   without a workflow gets the workflow written (if the deliverable is real) rather than the
   wrapper deleted.
4. **Dedupe per deliverable** — one prompt per distinct deliverable; compare both candidates,
   keep the stronger, `rm` the loser, update workflow pointer lines, re-run
   `prompt_library.py build` + `wire_prompt_pointers.py --write` + audit to 0 fail.
5. **Fidelity-check annealer inventions** — annealed content can smuggle in numbers the corpus
   never stated (numeric show-rate bands); label them "operator heuristic" rather than expert claim.

## Why it works

The annealer optimizes files locally without the session's full context; the conductor holds the
corpus and spec. Merging (accept+repair) captures both: harness-native structure wins where it's
better, extraction fidelity wins where the annealer guessed. The deterministic gates
(renaissance_audit 0-fail, heartbeat 6/6) are the arbitration layer — not opinions.

## Deploy when

Any `/extract` or `/extract-forge` session where files change that you didn't write, extra
prompts/wrappers appear, or the audit fails on files that passed at write time.
