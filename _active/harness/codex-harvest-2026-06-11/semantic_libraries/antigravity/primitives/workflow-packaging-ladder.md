# Workflow Packaging Ladder

## Purpose

Use this primitive when deciding whether repeated Antigravity work should stay as a prompt, become a workflow, become a skill, or be wrapped as a Codex plugin.

The goal is not to package everything. The goal is to stop rebuilding the same operating context in every thread.

## Ladder

| Level | Use When | Keep It Here Until |
|---|---|---|
| Prompt | One-off request or temporary instruction | The same wording is reused 3+ times |
| Workflow | Steps are repeatable inside this repo | The workflow needs trigger rules, references, or examples |
| Skill | Codex needs a reusable method and loading trigger | The method needs to travel, install, or bundle tools |
| Companion skill | Existing skill owns the domain but misses one method | The companion becomes a stable operating layer |
| Repo-local plugin | A stable workflow bundle should install from this repo | Fresh-thread tests pass and paths resolve |
| Home/global plugin | The bundle should be available outside this repo | It has no repo-only hidden dependencies |
| MCP/app connector | The work needs live external systems | Permissions and auth are approved |
| Deterministic hook/script | A step must be checked mechanically | The model should not judge that step manually |

## Plugin-Readiness Test

Score a workflow family before packaging it:

| Dimension | Max | Question |
|---|---:|---|
| Repetition | 20 | Does this get used often enough to justify a bundle? |
| Reconstruction cost | 20 | Does the user or agent keep re-explaining the setup? |
| Tool needs | 15 | Does it need scripts, apps, MCP, browser, or local checks? |
| Verification needs | 15 | Does it have a clear test loop and stop condition? |
| Portability | 15 | Can it install and trigger without hidden repo lore? |
| Failure history | 15 | Does packaging prevent known drift or misroutes? |

For broad restructuring, run `/system-efficiency-benchmark` before this scorecard. If router weighting, command metadata cleanup, or skill description tightening produces the same improvement as a plugin, use the simpler optimization first.

## Decision Bands

| Score | Decision |
|---:|---|
| 80-100 | Package now |
| 65-79 | Improve first, then package |
| 45-64 | Keep as workflow or skill |
| 0-44 | Keep as prompt, reference, or archive candidate |

## Rules

- Package proven workflows, not vague intent.
- Keep skills as the authoring format; use plugins as the installable distribution unit.
- Add app connectors or MCP only when live systems are necessary.
- Add scripts or hooks when a check should be deterministic.
- Do not archive a large library just because it is large; first measure what is surfaced, routed, and used.
- Do not package the whole system; package only workflow families that prove they reduce reconstruction burden or fresh-thread friction.

## Acceptance Tests

Any repo-local plugin candidate must pass:

1. Direct invocation by plugin or skill name.
2. Natural-language trigger without magic words.
3. Missing-info behavior: asks the right small question or states assumptions.
4. Path behavior: every local path resolves from a fresh install/cache.
5. Fresh-session behavior after restarting Codex.
