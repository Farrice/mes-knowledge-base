---
name: Project Artifacts Loose While Router Scaffold Sits Empty
problem_signature: a project's deliverables sit loose at the folder root while the artifact router's empty numbered subfolders sit alongside; the user opens the subfolders, finds them empty, and concludes "nothing is here / it's not organized"
domain: system
tags: [artifact-organization, project-structure, artifact-router, file-hygiene, cross-links]
date: 2026-07-07
status: active
session: suzuki-os-embodiment-dwa-rebuild
---

## Problem

A built project (`_active/dwa-affiliate-battle-test/`) had all its deliverables committed and present — but loose at the folder root. The global artifact router had auto-created a full generic scaffold (`00-start-here` … `99-archive`) and, by its own policy (`active project file is governed but not automatically moved`), left every subfolder empty. The user opened the numbered subfolders, found them all empty, and reasonably concluded "all the folders are empty / this isn't organized," even though nothing was lost.

## Root Cause

Two half-states collided: (1) the router scaffolds lifecycle folders but does NOT file active-project artifacts into them, and (2) the builder left files flat. The result is the worst of both — misleading empty folders *plus* loose files. Empty folders read as "missing content" to a human, regardless of where the real files are.

## Approach That Worked

1. **Verify first, never argue.** `ls -R` + `git ls-files` proved the files existed and were committed — the issue was organization, not loss.
2. **Only-populated-subfolders rule.** Create canonical numbered subfolders (`00-start-here`, `01-source`, `02-research`, `04-deliverables`, `06-system`) and place files into them — but **only instantiate a folder if it has content.** No empty scaffold. (Empty `03-working-drafts/05-assets/90-exports/99-archive` were simply not created.)
3. **Fix cross-links on move.** The files referenced each other by bare filename (flat assumption). A Python pass rewrote every markdown link `](x)` and inline-code `` `x` `` to the correct relative path based on each file's new folder (same-folder refs left bare).
4. **Verify links.** A scan resolved all 38 intra-project references → 0 broken, 0 empty dirs.
5. **Durable convention:** every project is organized into populated canonical subfolders from the start; INDEX documents the structure; this card is the auto-resurfacing backstop.

## Dead Ends

- **"Flat + numbered is fine, don't move them."** True in isolation, but it ignored the standing user preference for subfolders and left the empty-scaffold confusion in place. The user's explicit spec ("subfolders, highly organized, every time") overrides the builder's convenience.
- **Filing into the FULL generic scaffold.** Would leave `research/drafts/assets/exports/archive` empty — recreating the exact empty-folder problem. Only-populated is the fix.
- **rmdir-ing the scaffold and staying flat.** Solves the empty-folder view but not the user's actual ask for organized subfolders.
