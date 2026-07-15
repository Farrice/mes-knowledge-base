# Concurrent Session Racing a Live Forge: Accept → Repair → Dedupe, Never Revert

**Date**: 2026-07-15 (attribution corrected same day) · **Domain**: system / extraction forging · **Origin**: jeremy-haynes-cold-offer forge session

## Problem

During a live `/extract-forge` build, files changed that the conducting session never wrote: prompt
files rewritten mid-session, plus net-new assets (two prompts-v2 files, two skill workflows, two
slash wrappers, an AGENT.md expansion, a SKILL_INDEX row). Three failure shapes resulted:
(1) rewrites dropped audit-required sections (`## Output Skeleton`), (2) new wrappers pointed at
skill workflows that didn't exist yet, (3) two prompts covered ONE deliverable — a duplicate the
prompt-forging spec forbids.

**Root cause (verified, not guessed)**: a SECOND live Claude Code session on the same working tree
— three same-project session transcripts had concurrent writes; no annealing daemon or file-writing
hook exists (launchd + `.claude/settings.json` checked); Codex was idle. This is the CLAUDE.md
GOLDEN RULE scenario (one tool per working tree) and a sibling of
[[2026-07-07-parallel-builders-stale-contracts]] — same disease, but between whole sessions instead
of dispatched sub-agents. First attribution ("the harness's annealer") was wrong: an intelligent
co-writer producing context-aware content means another SESSION, not a linter — daemons don't write
300-line practitioner prompts.

## Solution

Two layers — merge discipline for when it happens, prevention so it stops happening:

**Merge discipline (in the moment):**
1. **Accept** — never revert the foreign session's files mid-race; reverting fights a live writer
   and its work often carries real improvements (its articulation-brief prompt had
   VERIFIED/LIKELY/UNCONFIRMED labeling the hand-written version lacked — it won the dedupe).
2. **Repair to spec** — run `renaissance_audit.py` after any unexplained file change; add missing
   required sections; fix H1→H2 headers (the audit only recognizes `## `-level section names).
3. **Resolve dangling pointers** — diff wrappers vs. skill workflows; write the missing workflow
   if the deliverable is real, rather than deleting the wrapper.
4. **Dedupe per deliverable** — one prompt per deliverable; keep the stronger candidate, update
   pointer lines, re-run library build + pointer wiring + audit to 0 fail.
5. **Fidelity-check foreign inventions** — merged content can smuggle in numbers the corpus never
   stated; label them "operator heuristic," not expert claim.

**Prevention (the actual fix):**
- **One driver per tree** — the Golden Rule. A second concurrent session belongs in its own
  `git worktree`.
- **Claim the lock** — `python3 execution/session_lock.py claim "<mission>"` at the start of any
  build/forge session; `check` before wave-building. The tool existed and neither session used it —
  opt-in locks don't fire; make claiming part of the forge/kickoff ritual.
- **Diagnostic tell**: unexplained context-aware file changes + fresh sibling transcripts in
  `~/.claude/projects/<project>/` with same-minute mtimes = concurrent session, not a linter.

## Why the merge discipline works

Deterministic gates (renaissance_audit 0-fail, heartbeat 6/6) arbitrate the merge instead of
opinions: harness-spec structure wins where the foreign writer was better, extraction fidelity wins
where it guessed. But note the luck involved — both sessions happened to be building the SAME
artifact compatibly. Two sessions pulling different directions is the 2026-06-30 "apply one fix,
another breaks" corruption; merge discipline is the seatbelt, the lock is the brake.

## Deploy when

Files change that you didn't write mid-build; extra prompts/wrappers appear; the audit fails on
files that passed at write time; system notes report modifications "by the user or a linter" on
content no linter could author.
