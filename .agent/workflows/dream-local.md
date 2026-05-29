---
description: Local file-memory consolidation — MANUAL FALLBACK for Anthropic's native /dream. Prunes/merges MEMORY.md + topic files. Non-destructive (proposes, then applies on approval). Defers to native auto-dream when active.
---

# /dream-local — File-Memory Consolidation (manual fallback)

> **Defers to native.** Anthropic's native `/dream` (Claude Code auto-dream) owns the
> `/dream` name and runs as a background consolidation when enabled for your account.
> **If native auto-dream is on, use it — do not run this.** Check: type `/dream` in the
> terminal, or look for `Auto-dream: on` in the `/memory` selector. This `/dream-local`
> exists only as the **manual fallback** for when the native feature is NOT yet active
> (it's a server-gated research preview). When native turns on, this becomes redundant
> and can be archived.

Local equivalent of the native auto-dream. A "dream" reads the **file** memory layer —
`MEMORY.md` + topic files — and produces a *cleaner* version: duplicates merged,
relative dates made absolute, stale entries flagged, the index rebuilt lean. Models the
native Dreams API contract: **the input is never mutated in place** — a proposal is
written for review, applied only on approval.

## Scope (read before running)

- **Targets the FILE memory layer only**: `~/.claude/projects/-Users-farricecain-Google-Antigravity/memory/`.
- **Does NOT touch the sovereign DB** (`.memory/sovereign.db`). That layer already
  has its own dream-equivalent: `memory_distill.py` (weekly cluster→propose→judge) +
  `memory_review.py` (human promote). Running this does not overlap or compete.
- **Does NOT touch** `knowledge/` (that's `/reflect` + `knowledge_compiler.py`).
- **Does NOT touch the native feature's state** — no lock files, no settings. If native
  auto-dream is mid-run, do not run this concurrently.

## Usage

```
/dream-local              # full pass: scan → propose → gated apply
/dream-local --scan       # detection only, no proposal (calls dream.py scan)
/dream-local --apply      # apply a proposal already reviewed in .tmp/dream/<date>/
```

## The 4 Phases (mirrors the native auto-dream system prompt)

### Phase 0 — DEFER CHECK
Before anything: is native auto-dream active? (`/memory` shows `Auto-dream: on`, or `/dream`
is a live command.) If yes → stop, let native handle it. If no → proceed.

### Phase 1 — ORIENT (deterministic)
Run the scanner. It is the always-on detection backstop — never skip it, never
hand-eyeball the directory instead.

```bash
python3 execution/dream.py scan
```

Read the findings: relative dates, oversized index lines, orphan pointers, unindexed
files, near-duplicate bullets, bloated MEMORY.md sections, stale candidates.

### Phase 2 — GATHER SIGNAL (judgment)
The scan flags *candidates*, not verdicts. For each finding decide REAL vs FALSE POSITIVE:
- **Relative dates**: a date inside a quoted *writing example* (e.g. `'right now'` in a
  banned-phrase list) is NOT a date to convert. Only convert dates describing when
  something actually happened.
- **Stale candidates**: `feedback_*`/`user_*` are never auto-pruned (load-bearing
  lessons + identity). For others, confirm the topic hasn't merged elsewhere.
- **Bloated sections**: a `## section` over the line budget = move its body to a topic
  file, leave a one-line pointer in MEMORY.md — UNLESS the body is itself a list of
  legitimate one-line pointers (then it's a false positive; keep it).

If recent sessions added decisions not yet in memory, this is where you fold them in
(read the relevant topic file before editing — never blind-append).

### Phase 3 — CONSOLIDATE (non-destructive write)
Build the proposed new state under `.tmp/dream/<YYYY-MM-DD>/`:
- `MEMORY.md` — the rebuilt index (leaner; one line per memory, < 200 chars).
- any rewritten/merged topic files (only the ones that change).
- `CHANGES.md` — a diff-style log: what merged, what's now absolute-dated, what's
  proposed for archive, with the **reason** for each. This is the review surface.

Rules: convert confirmed relative dates to absolute (today = the scan's `scanned_at`).
Merge near-duplicates into one entry. Move bloated-section bodies into topic files.
Do **not** delete `feedback_*`/`user_*`. Density > completeness — the rebuilt MEMORY.md
should be smaller than the input.

### Phase 4 — PRUNE & INDEX + GATED APPLY
Present `CHANGES.md` to the user. **Stop. Do not apply unsold.** On explicit approval:
1. Back up first: copy current `MEMORY.md` + any files being changed to
   `.tmp/dream/<date>/_backup/`.
2. Stale archive candidates move to `memory/_archive/` (created if absent) — archived,
   never deleted.
3. Copy the proposed files over the live ones.
4. Re-run `python3 execution/dream.py scan` and report the before/after finding count.

## Safety contract
- Detection is deterministic (`dream.py`) — observable without a model in the loop.
- Apply is human-gated + backed up + archive-not-delete. Mirrors the native Dreams API
  "review the output, keep or discard" guarantee.
- Reads only until the apply step — no contention with native consolidation during scan/propose.

## When to run
- Only while native auto-dream is NOT yet enabled for the account.
- When MEMORY.md crosses ~250 lines or the session-start "only partially loaded" warning fires.
- Monthly, paired with `/reflect` + `/calibrate`.
