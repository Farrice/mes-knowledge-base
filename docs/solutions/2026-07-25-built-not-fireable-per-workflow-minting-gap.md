---
date: 2026-07-25
session: arsenal loop build
name: built-not-fireable-per-workflow-minting-gap
problem_class: harness / arsenal / unreachable assets
domain: harness
status: proven
problem_signature: "hundreds of workflows and skills sit on disk with no way to invoke them and assets keep getting rebuilt because no surface can answer what do I already have for this — a checker correctly reports the drift every run and nothing ever mints the missing wrappers"
tags: [arsenal, wrappers, minting, index, reachability, generators]
---
# Solution Card — Built-but-not-fireable: a generator that mints per-SKILL does not mint per-WORKFLOW

**Date:** 2026-07-25 · **Domain:** system / harness · **Status:** SOLVED, physically enforced

## The problem

728 skill workflows, 225 command workflows, and 74 skills sat on disk with no way to invoke them.
Assets were being rebuilt because no surface could answer "what do I already have for this?"

This had already been "fixed" twice and came back both times:

| Date | Fix attempted | Why it came back |
|---|---|---|
| 2026-07-21 | Manual step added to `extract.md`: *"Mint BOTH wrapper layers per workflow… the generators do not mint per-workflow shims"* | A manual step is model compliance, not a gate. It lost to velocity. |
| 2026-07-25 (am) | Heartbeat check 7 `menu_parity` added to `skill_auditor.py` | A **detector** cannot fix a **minting** gap. It correctly reported drift that nothing then closed. |

## Root cause

Nothing indexed `skills/*/workflows/*.md`.

- `find_skill.py` indexes only `skills/*/SKILL.md` (371 entries)
- `sync_registries.py` mints one shim **per skill** — by design, and it says so
- Therefore per-workflow registration had **no owner**, only prose asking a human/model to do it

One missing index produced two symptoms that looked unrelated: unreachable commands (menu) and
forgotten assets (recall). They were the same hole.

## The fix

`.agent/arsenal-index.json` (`execution/arsenal_index.py`) — a workflow-granularity index, ~5,600
entries — becomes the spine. Everything else reads it:

- `execution/mint_menu_wrappers.py` closes reachability
- `execution/arsenal.py` (`/arsenal`) closes recall
- Four surfaces run it unattended: PostToolUse hook · end-session spine step · launchd 06:40 ·
  SessionStart injection

Result: 1,599 files minted, 911 commands, zero collisions, zero pre-existing files modified,
drift 0.

## The transferable lessons

1. **Detection ≠ correction.** If the missing action is *generation*, a checker will report the
   same failure forever. Ask: "when this fires, what closes it, and who runs that?"
2. **A manual step in workflow prose is not a gate.** Under velocity it will be skipped. Side
   effects belong in the deterministic spine, never in instructions to a model.
   (Repo binding: *AI-memory-dependent observability is BANNED without a deterministic backstop.*)
3. **Auto-fix beats nagging.** The 4 surfaces MINT rather than warn. A gate that blocks a closeout
   over housekeeping is a gate that gets disabled.
4. **Two symptoms, one index.** "Can't fire it" and "can't find it" were the same missing corpus.
   When two problems resist separate fixes, look for the shared missing data structure.
5. **A file stem is not a command name.** Numbered workflows fire under a prefixed name
   (`04-viral-idea-ladder` → `/jenny-idea-ladder`). Any consumer deriving invocation from the
   filename hands back commands that do not exist. Store the resolved command; read it back off
   the wrapper.
6. **Reachability must have exactly one definition.** `arsenal_index` imports check 7's primitives
   rather than re-implementing them — otherwise the minter mints what the auditor still counts as
   missing, forever.

## Re-solve guard

**Do NOT** re-add a manual "mint the wrappers" step to any extraction or forge workflow. **Do NOT**
build a second index, ranker, or minter. If a new asset type needs coverage, add a `kind` to
`arsenal_index.py` and let the existing surfaces pick it up.

Spec: `directives/arsenal-loop.md`. Related: `2026-07-21-wired-but-never-loaded-prompts.md`
(same family — an asset linked on disk is not an asset loaded at fire time).
