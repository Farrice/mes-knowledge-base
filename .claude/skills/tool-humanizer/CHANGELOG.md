# Changelog — tool-humanizer

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [1.1.0] — 2026-07-28

- New `detect` mode: audit only — names each pattern, quotes the line,
  suggests the fix. No rewrite, no score.
- New Step 3 "Identify Voice to Preserve" + minimum-effective-edit rule:
  distinctive sentences without AI patterns are left alone.
- New pattern category 9 "Rhetorical & structural slop": binary contrasts,
  faux-insight setups, colon reveals, fake-profound kickers, synonym
  cycling, negative listing, dramatic fragmentation, weak verb phrases,
  formatting slop. Matching replacement-guide entries added.
- New `references/quality-gate.md` + Step 8 final self-check against it
  (voice preservation, meaning & specificity, residual patterns).
- Em dash rule now scales with text length instead of a flat count.

## [1.0.1] — 2026-05-09

- Adapted from the agentic-os baseline for inclusion in
  @scrapes/skill-systems. See the parent system CHANGELOG for context.

## [1.0.0] — agentic-os baseline

- Originally shipped as part of agentic-os.
