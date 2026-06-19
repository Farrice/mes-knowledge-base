# PRD — External skill visibility in the Antigravity registry

Status: ready-for-agent
Category: enhancement
Created: 2026-06-15 (via /to-prd)
Tracker: local-markdown (see docs/agents/issue-tracker.md)

> Seams to confirm with maintainer before implementation (see "Testing Decisions"): (1) the registry-sync module is the highest seam — extend it rather than the router hook; (2) external skills are read from the canonical global skills dir, not per-agent symlink dirs. Flag if either is wrong.

## Problem Statement

I install third-party skills (Matt Pocock's 29, and more to come) globally, and my agents can invoke them — but my own system can't *see* them. The auto-generated skill registry only knows about skills inside the project `skills/` directory. So globally-installed external skills never appear in the registry the router and discovery layer consult, they don't surface as routing suggestions, and the only record that they exist is a directive I have to maintain by hand. As I import more external skills, this blind spot grows: I can invoke a skill only if I already remember it exists, which defeats the point of a discovery system.

## Solution

The registry becomes aware of globally-installed external skills without me hand-maintaining a list. When the registry is synced, external skills are discovered from the global skills location, normalized into the same shape as native skills (slug, description, source, invocation), and surfaced through the same discovery/routing surfaces native skills use — clearly marked as external and read-only so they're never confused with native expert skills or accidentally edited. The hand-written registry directive stops being the source of truth and becomes (at most) human-readable narrative; the machine record regenerates itself.

## User Stories

1. As the operator, I want globally-installed external skills to appear in the skill registry after a sync, so that discovery reflects everything I can actually invoke.
2. As the operator, I want each external skill labeled with its source (e.g. `mattpocock/skills`) and an `external` marker, so that I can tell at a glance it isn't a native expert skill.
3. As the operator, I want external skills excluded from native-only operations (extraction enrichment, genius.md expectations, finalize routing), so that they don't pollute expert-specific tooling.
4. As the operator, I want the router/discovery layer to be able to *suggest* a relevant external skill, so that I don't have to remember it exists to use it.
5. As the operator, I want the sync to be idempotent, so that re-running it doesn't create duplicates or churn.
6. As the operator, I want external skills that were uninstalled to drop out of the registry on the next sync, so that the registry never lists skills I can't invoke.
7. As the operator, I want the external-skill section visibly separated from native skills in any generated index, so that the two populations stay legible.
8. As the operator, I want a skill that exists both natively and externally (name collision) to be disambiguated rather than silently merged, so that I know which one resolves.
9. As the operator, I want the sync to read from the canonical global skills directory (not each per-agent symlink copy), so that the same skill isn't counted once per agent.
10. As the operator, I want the discovery record to capture each external skill's description verbatim, so that trigger matching uses the creator's intended wording.
11. As the operator, I want the existing hand-written external-skills directive to remain valid as narrative, so that the migration doesn't break references already pointing at it.
12. As a future maintainer, I want a single command to refresh external-skill visibility, so that onboarding a new external source is one step.
13. As the operator, I want external skills with no parseable description to be reported, not silently dropped, so that a malformed import is visible.
14. As the operator, I want the count of external skills surfaced after a sync, so that I can confirm an import landed.

## Implementation Decisions

- Extend the existing registry-sync responsibility to additionally enumerate external skills from the canonical global skills location, rather than building a parallel system. One sync, two populations (native + external).
- External skills are read-only in the registry: discovered, never written back to. The global install stays the source of truth so the upstream updater (the skills CLI) keeps them current; the registry only mirrors metadata.
- A skill's identity for the registry is (slug, description, source-repo, scope=external). Description is captured verbatim from the skill's own frontmatter so trigger matching matches the creator's wording.
- Name collisions between a native skill and an external skill are disambiguated (native wins for the bare slug; external is namespaced or flagged), never silently merged.
- Enumerate from the canonical global directory, not the per-agent symlink directories, so a skill installed for five agents counts once.
- External skills are excluded from native-only expectations: no genius.md requirement, no expert-extraction tooling, no finalize/expert routing. They are tagged as utilities that bypass The Chain.
- The generated index keeps native and external skills in clearly separated sections; the hand-written directive is demoted to narrative and is no longer the machine source of truth.
- Removal is handled by regeneration: each sync rebuilds the external section from what's currently installed, so uninstalled skills disappear and re-runs are idempotent.
- Skills that fail to parse (no description) are reported in the sync output rather than dropped.

## Testing Decisions

- Good tests here assert *external behavior of the sync*, not its internals: given a known set of installed external skills, the regenerated registry contains exactly those, correctly labeled — independent of how enumeration is implemented.
- Cover: (a) a fresh external skill appears after sync; (b) an uninstalled skill disappears after sync; (c) re-running sync is idempotent (no duplicates, no diff); (d) a native/external name collision is disambiguated, not merged; (e) a malformed (description-less) skill is reported, not silently dropped; (f) a skill installed for multiple agents is counted once.
- Highest seam: drive the sync end-to-end against a temporary fixture skills directory and assert on the regenerated registry output — prefer this over unit-testing the enumerator. Prior art: existing registry-generation behavior is the closest analog; mirror its test style if one exists, otherwise establish this as the seam.
- Verify the router/discovery layer can return an external skill as a suggestion given a matching prompt (behavioral, through the same surface a native suggestion uses).

## Out of Scope

- Auto-installing or auto-updating external skills (the skills CLI owns that).
- Editing or forking external skill content into the project tree (explicitly forbidden — breaks the updater).
- Routing *bindings* / mandatory-load rules for external skills (they remain explicit-invoke utilities that bypass The Chain).
- Per-agent symlink management or multi-tool sync (the CLI handles fan-out).
- Modifying the constitution files (CLAUDE.md / AGENTS.md / GEMINI.md).

## Further Notes

- Today's blind spot: the sync module's skills scope is the project `skills/` dir only; the global external skills (`~/.agents/skills/`) are unseen. The current stopgap is the hand-written `directives/external-skills-registry.md`.
- This PRD was generated as a live demo of the newly-wired `/to-prd` against the local-markdown tracker. Treat the seams note at the top as the open question before building.
- Natural follow-ups: `/to-issues` to slice this into `.scratch/external-skill-visibility/issues/`, then `/tdd` to build it test-first.
