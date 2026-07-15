---
name: Ours-Merge Absorbs Silently Drop Branch Content
problem_signature: a divergence alarm answered with `git merge -s ours` (or a "content recovered file-wise" absorb that missed files) silences the alarm while discarding branch content; ancestry-based checks then report 0-ahead and the loss becomes invisible
domain: system
tags: [git, divergence, merge-ours, data-loss, empty-absorb, health-loop, all-work-on-main]
date: 2026-07-15
status: active
session: system-health-debt-control-loop
---

## Problem

The SessionStart divergence alarm flagged `origin/brief/2026-07-14 (+1)` and `origin/brief/2026-07-15 (+1)`. The same morning both were "absorbed" with `git merge -s ours` (commits `ad7978724`, `39840843d`) — which records the merge and discards ALL branch content. Counts went to 0, alarm went silent, and the 07-14 health-performance GEO brief (360 lines) plus 20 ledger lines were gone from main. Auditing the previous 14 days of absorb merges found SIX more with the same defect: 9 files dropped despite commit messages claiming "content recovered where main lacked it," and 96 append-only ledger lines (43 researched insights) that file-wise recovery had missed.

## Root Cause

Ancestry counting (`git rev-list --count main..ref`) measures SHA reachability, not content. After ANY merge — including `-s ours` — the branch tip is an ancestor of main, so the count reads 0 whether or not the content arrived. The alarm therefore cannot distinguish "absorbed" from "silenced." The `merge -s ours` recipe in the all-work-on-main playbook was only safe with a completed file-wise recovery first; nothing verified that precondition, and partial recoveries passed silently for weeks.

## Approach That Worked

1. **Ground truth is trees, not ancestry.** Per branch: files its own commits ADDED (`git diff --diff-filter=A --name-only $(git merge-base main ref) ref`) that are absent from current main (`git cat-file -e main:path`) = real loss. Modified append-only ledgers need a line-level pass: `comm -23 <(git show ref:file | sort) <(sort file)`.
2. Restore whole files with `git show <ref>:<path> > <path>`; merge lost ledger lines with sort-union, then validate every line as JSON before committing.
3. **Empty-absorb detector** added to `divergence_alarm_hook.py` (`_detect_empty_absorbs`): for merges into main (last 14d), flag any whose branch-created files are missing from CURRENT main — checked against current main so completed recoveries self-clear the alarm. Batched existence check via `git cat-file --batch-check` keeps it ~1s at session open.
4. Only after recovery is committed AND pushed do branches get pruned.
5. Same-day filename collisions (two different 07-15 briefs from parallel local + cloud runs) get suffixed (`-cloud.md`), never overwritten — both were real content.

## Dead Ends

- `git rev-list --cherry-pick --right-only --count main...ref` — better than plain ancestry pre-merge (kills rebased-content false positives) but still reads 0 after any merge; it cannot catch this loss class alone.
- Trusting absorb commit messages ("content recovered") — 6 of ~27 were wrong. Verify content, not intent.
- `git diff --name-status ref main | grep '^D'` on old branches over-alarms: it flags files main deliberately moved/deleted after the branch. Scope to files the branch itself ADDED.

## Verification

Detector run against pre-recovery main listed all 7 defective merges with exact lost paths; post-recovery-commit run is clean (self-clearing confirmed). 27 remote branches then passed the branch-added-files audit and were pruned; `git branch -r` shows only origin/main. Recovered ledgers: 234-line content-finish-log + 116-line insights.jsonl, all valid JSON.

## Weaker-Model Trap

Sees the divergence alarm, runs `git merge -s ours` because a memory card says "diverged branches = recover files + merge -s ours" — executing the second half of the recipe without the first, then treating the now-silent alarm as success. The silence IS the failure: never use an ours-merge to clear a divergence alarm until a tree-level content audit proves main holds every file and ledger line the branch created.
