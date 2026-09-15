# Artifact Placement — Every Asset Into Its Populated Subfolder

## Current Authority and Revision History (2026-09-15 reconciliation)

The latest explicit user decisions, interpreted within the whole accumulated
intent, determine authority. Resolve the decision-backed current project index
and its exact supporting documents. Filenames, dates, modification times,
canonical labels and search rank are discovery hints, never approval or truth.

Maintain one coherent living view per purpose. Regenerate it after a revision;
do not prepend a new CURRENT block over contradictory prior instructions.
Preserve accepted components, distinguish candidates from approved outputs, and
retire rejected direction from ordinary retrieval. A local correction must not
become an unwanted global rule. Keep useful research for its evidenced role.

Use the every-turn protocol in `directives/working-context-reconciliation.md`.
The session model performs semantic reconciliation; `execution/working_context.py`
checks receipt coverage, preservation, hashes and handoff freshness. Existing
project CANON/START-HERE documents and the document-history helper remain their
owners; the conversation view is not a competing project index.

Use Git or the existing document-history journal for ordinary edits. New files
need a distinct purpose, meaningful review checkpoint or evidence change.
When a replacement is authorized, preserve the previous bytes, archive through
the existing filing/history tools, leave a short redirect, and reconcile known
active pointers. Do not delete code or source material because copy was rejected.
Never restore an older candidate merely because the newest candidate failed.

The former date-led-record/undated-truth heuristic is superseded by the user's
newer decision-led filing contract in `/Users/farricecain/Work/ASSET-FILING.md`.
Dated files can contain authoritative decisions; undated files can be stale.
A new user decision can replace prior approval or explicitly restore a candidate.

## The Shape

```
_active/<arena>/<initiative>/<NN-bucket>/[<sub-bucket>/]<file>
```

- **Arena** — the surface (`linkedin`, `jen-listings`, `farrice-brand`). Plain
  English. Holds initiatives and nothing of its own but pinned files.
- **Initiative** — the thing being worked (`angle-map`, `profile`, `teardowns`).
  Plain English. **This is the unit the front door indexes.** A directory whose
  children are numbered buckets is an initiative, not an arena.
- **Bucket** — the numbered set below, instantiated only when populated.
  Project-internal numbered topic folders remain fine. Free naming is allowed
  for **sub-buckets** under `05-assets/` (`video/`, `graphics/`, `carousels/`).

Every project gets exactly ONE front door: a generated `START-HERE.md` +
`START-HERE.html`, written by `execution/front_door.py`. Nothing else may claim
to be an index. If a second file starts announcing itself as the place to
begin, the front door reports it as drift.

```bash
python3 execution/front_door.py build <path>    # md + Premium Minimal board
python3 execution/front_door.py build --all     # every initiative, ~4s
python3 execution/front_door.py check <path>    # drift only, never blocks
```

It reads only the tree, git history and frontmatter — every value is derived at
build time, so it cannot go stale. Dates mean *last actually worked on*: a
commit touching 40+ files in one initiative is housekeeping and does not count,
and a rename is not work at all.

**Status**: STANDING DECISION (Farrice 2026-07-08). Deterministic enforcement, not advisory prose.
**Origin**: 14 projects accumulated 4-43 loose root files while the router's empty
scaffolds sat alongside — retrieval broke. Root cause: prevention was never wired,
only cleanup. Solution cards: `docs/solutions/2026-07-07-project-artifacts-loose-plus-empty-scaffold.md`.

## The Standard

Every project under `_active/` and `projects/` organizes into the canonical set,
**instantiated only when populated** (an empty subfolder is a lie about content):

| Folder | Holds |
|---|---|
| `00-start-here` | orientation docs beyond INDEX.md |
| `01-source` | raw inputs, transcripts, captures |
| `02-research` | research, analysis, investigations |
| `03-working-drafts` | unfinished work |
| `04-deliverables` | finished outputs |
| `05-assets` | images, media |
| `06-system` | receipts, configs, scripts, gate reports |
| `90-exports` | pdf / docx / html renders |
| `99-archive` | superseded versions |

Root-level files allowed: `INDEX.md`, `README.md`, `CLAUDE.md`, `RISKS.md`, dotfiles.
`INDEX.md` documents the project's map. Numbered topic folders (e.g. coach-cooz's
`16-war-on-fitness-industry/`) are fine as project-internal structure — the rule
applies at whatever level files actually accumulate.

## The Machinery (all deterministic)

1. **Write-time advisory** — `execution/hooks/artifact_placement_hook.py`
   (PostToolUse/Write, wired in `.claude/settings.json`): a file written loose at a
   project root triggers an in-session correction with the exact fix. Fix it then,
   while context is hot.
   The same hook is wired through `.codex/hooks.json`, so Claude and Codex apply
   the living-slot rule consistently.
2. **Session-close sweep** — `execution/end_session_closeout.py` runs
   `project_filer.py sweep`: unambiguous strays get auto-filed with a receipt;
   ambiguous ones are listed for judgment. Never blocks closeout.
3. **Filing engine** — `execution/project_filer.py`:
   - `plan --project <dir>` → reviewable move plan with inbound-reference scan
   - `apply --plan <json>` → moves + rewrites every referrer (repo AND user-memory
     dir) + prunes empty scaffold + receipt + revert script
   - `verify --project <dir>` → 0 broken links, 0 old-path residue, 0 empty dirs
4. **Router** — `execution/artifact_router.py` remains the classifier/ledger owner;
   `ensure_project_shapes` no longer pre-creates empty scaffolds (fixed 2026-07-08).

## Pin Rules (what never moves)

A file referenced from `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`, `CODEX.md`,
`.claude/`, `.agent/workflows/`, `directives/`, `execution/`, or `skills/` is
PINNED in place — control-plane referrers are never rewritten by the filer.
Everything else moves WITH its referrers rewritten (including
`~/.claude/projects/…/memory/*.md`).

## Safety Contract

Every apply writes a receipt (`.agent/organization/receipts/`) and appends inverse
commands to `.agent/organization/REVERT-<date>.sh`. No git commands are run by the
tooling; commits are Farrice's call. Verify must PASS after every apply — a FAIL
stops the run, never gets papered over.

## For Agents (the one-paragraph version)

Creating a file in a project? Put it in the canonical subfolder at creation time —
never at project root. Creating the first file of its kind? mkdir the subfolder
then (only-populated). **Name it by the rule: no date = living (and there is only
one living doc per slot, so update the existing one instead of adding a rival);
leading `YYYY-MM-DD-` = a record of this session.** Reading? `START-HERE.md`
first, then the living docs it lists — a dated file is history, not truth. If the
placement hook fires on you, do what it names before continuing. Moving anything
by hand? Use `project_filer.py` for loose files and `project_relocate.py` for
directories, never bare `mv` — bare moves orphan every inbound link.

## Moving Things — the traps, all found the hard way (2026-08-07)

`project_filer.py` files LOOSE files at a project root; it cannot move a
directory. `project_relocate.py` moves directories. Both now:

- **verify absolute references.** `_is_pathlike` used to reject every target
  starting with `/`, and `scan_broken_refs` shares that gate, so ~26k absolute
  refs were rewritten but never checked — a move that shattered all of them
  still printed `RESULT: PASS`. (The repo path also contains a space, which
  rejected them a second time.)
- **abort on a failed referrer scan.** Both greps swallowed timeouts and
  returned `[]`, which is indistinguishable from "no referrers" — a slow grep
  silently became a move with zero rewrites. Now raises `GrepFailure`.
- **scan gitignored trees.** `git grep --untracked` skips *ignored* files;
  five real referrers survived a 439-file move because of it.
- **survive a shortening rename.** `<x>-launch` → `<x>`: the anti-double-write
  masking destroyed the source string and rewrote nothing. A 439-file move
  reported `total_rewrites: 0` and orphaned 308 referrers. `apply` now warns
  loudly when a plan found referrers and rewrote none.
- **recompute links INSIDE moved files.** Moving a tree to a different depth
  used to break its own outbound `../` links; archiving two files ADDED 16
  broken links.
- **leave append-only ledgers alone.** `.agent/assets/manifest.jsonl` is
  regenerated after a move, never rewritten — its tombstones are supposed to
  remember the old path.

**Rehearse the rollback before you trust it.** `--stub` used to leave a
`MOVED.md` at the source, so the source directory still existed and the inverse
`mv -n` moved the tree *inside* it — reporting exit 0 while corrupting the tree.
Run the REVERT script once on a small move and confirm `git status` is clean
before relying on it.
