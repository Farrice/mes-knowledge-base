---
name: Divergent-Branch Work Silently Lost
problem_signature: session work committed on a divergent branch line never reached main; weeks later the working tree silently lacks files that memory, CLAUDE.md, and other docs still cite as live
domain: system
tags: [git, coexistence, codex, restoration, audit, working-tree, golden-rule]
date: 2026-07-13
status: active
session: novelty-standards-audit
---

## Problem

A June session built a full skill package (kallaway-illusion-of-novelty: engine workflow, 8 references, enriched genius.md/SKILL.md, prose_classifier detectors, ai-slop-ban-bank directive) and it was committed — but the commit (`40da44cda`) sat on a divergent branch line that never merged into main. Weeks later the working tree silently lacked those files while MEMORY.md, CLAUDE.md's slop-ban section, and downstream workflows still cited them as live. Nothing errored; the system just quietly ran without its own enforcement layer.

## Root Cause

Two-driver tree corruption window (the CLAUDE.md GOLDEN RULE failure, root-caused 2026-06-30): Claude Code and Codex both operated on the directory; one line of history won, the other became unreachable-from-main. `git log --all` still showed the commit, so casual inspection looked healthy. No commit ever DELETED the files — main simply never contained them — so `git log --diff-filter=D` found nothing and `git status` was clean. The loss was invisible to every per-file history check.

## Approach That Worked

1. A standards audit (comparing the skill against current A-tier markers) surfaced "missing" files that context said existed — treat doc/memory pointers to nonexistent files as a LOSS SIGNAL, not doc rot.
2. `git log --all -- <path>` found the orphaned commit; `git merge-base --is-ancestor <sha> HEAD` proved it was never in main (the diagnostic that distinguishes "reverted" from "never merged").
3. `git checkout <orphan-sha> -- <paths>` restored every committed file into the current tree (safe: no later main commits touched those paths).
4. Pieces never committed anywhere (classifier detectors, ban-bank directive) were re-applied verbatim from the session transcript still in context — the conversation itself is a recovery source when git isn't.
5. Generator-owned blocks (SKILL.md prompt menu) were regenerated via their tool (`wire_prompt_pointers.py --write` after updating `.agent/prompt-index.json`), never hand-grafted.
6. Full verification after restore: renaissance gate, broken-ref scan, classifier regression (tells FLAG / clean prose stays CLEAN), registry sync.

## Dead Ends

- `git log --diff-filter=D` and ancestor-range queries (`sha..HEAD -- path`) — both return empty when the commit was never an ancestor; they answer "was it deleted," not "was it ever here."
- Assuming `git status` clean + files cited in docs means files exist.

## Verification

Post-restore: 14 workflows + 14 v2 prompts + 10 references on disk; renaissance_audit 3519/3519 pass; zero broken sibling/reference links; classifier flags tell-stuffed samples and passes clean human prose; SKILL_INDEX shows 14 workflows.

## Weaker-Model Trap

Trusts the audit surface ("file missing → the doc must be stale → fix the doc") and repoints citations at substitutes, silently accepting the loss. The right move is the opposite: a live doc pointing at a missing file means GO FIND THE FILE — check `git log --all` for orphaned commits before rewriting a single pointer.

## Pointers

- Orphaned commit: `40da44cda` (feat(kallaway): expand illusion-of-novelty into a full novelty engine)
- CLAUDE.md GOLDEN RULE (one tool per working tree) — the prevention rule this loss validates
- `docs/OPERATING-CODEX-AND-CLAUDE.md` — safe-handoff protocol
- Restored package: `skills/kallaway-illusion-of-novelty/` · `execution/prose_classifier.py` · `directives/ai-slop-ban-bank.md`
