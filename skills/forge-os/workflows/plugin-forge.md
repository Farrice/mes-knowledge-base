---
description: "/forge plugin <skill / prompt-set / workflow family> — Plugin Forge lane: a proven asset family → an installable Claude Code plugin. HARD-GATED: builds nothing without a verbatim operator lift token + 4/4 lift-plan fixtures passing in one run."
---

# Plugin Forge — Proven Asset Family → Installable Plugin

Dispatches `skills/forge-os/references/prompts-v2/plugin-forge.md` (the engine) plus the standing
decision document `skills/forge-os/references/plugin-forge-lift-plan.md`. Status: **ENGINE READY
— packaging gated (Wave 3)**.

## Invocation

`/forge plugin <asset family>`. This lane will NOT fire packaging on request alone — see the Gate
below.

## Stages

1. **Gate check (first, always)** — confirm a verbatim operator lift token exists naming scope
   (local-only, never marketplace) AND all four `plugin-forge-lift-plan.md` fixtures
   (F-REV / F-CRE / F-SYS / F-REG) passed in one run. Missing either → output the fixture
   checklist and the gap; build nothing.
2. **Anatomy mapping** — plugin surface sourced from the `plugin-dev:plugin-structure` skill
   (official plugin-dev cache), not improvised: `.claude-plugin/plugin.json` + `commands/*.md` +
   `skills/<name>/SKILL.md` + optional `hooks/hooks.json`, all intra-plugin paths on
   `${CLAUDE_PLUGIN_ROOT}`.
3. **Provenance manifest** — every packaged file matches its repo original byte-for-byte; the
   manifest records source paths.
4. **Validate through the installed plugin** — `plugin-dev:plugin-validator` (0 errors), local
   install, run the artifact's golden fixtures through the INSTALLED copy, uninstall, confirm
   clean teardown (`git status` clean, no shadowing of repo-native `/command` routing).
5. **Marketplace line** — out of scope entirely regardless of gate outcome; a separate explicit
   decision, never implied by a passing gate.

## Output Schema

Two possible shapes, per `plugin-forge.md`'s own Output Contract: (a) **gate-pass shape** — the
plugin package under a repo-local `plugins/` directory (manifest + `commands/` + `skills/` +
provenance block) + a Gate Record (lift token verbatim, F-REV/F-CRE/F-SYS/F-REG results table,
scope) + a validation block (validator / install / fixture-replay / uninstall / audit results); or
(b) **gate-fail shape** — the fixture checklist only, explicitly naming which of the four fixtures
is missing or failed, with nothing built. Shape (b) is a correct, complete deliverable for this
lane — it is not an incomplete run.

## Quality Gate

- Is the lift token verbatim operator language (not paraphrase or inference), with scope stated?
- Did all four fixtures pass in a SINGLE run before packaging began — partial passes across
  separate sessions do not accumulate, per `plugin-forge-lift-plan.md`'s own gate rule?
- Does every packaged file match its repo original byte-for-byte (no silent forks)?
- Was validation run through the INSTALLED plugin (not the source skill directly), and was
  uninstall proven clean?
- Was the "no marketplace edits" boundary respected regardless of gate outcome?
