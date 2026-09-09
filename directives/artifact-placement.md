# Artifact Placement — Every Asset Into Its Populated Subfolder

## The Living-vs-Record Rule (Farrice 2026-08-07 — read this first)

> **A filename that LEADS with `YYYY-MM-DD-` is a RECORD.**
> It is a receipt of one session. It is never truth and is never built on.
>
> **A filename with no leading date is LIVING.**
> One per slot, it sits at the bucket root, and it is UPDATED IN PLACE.

That is the whole rule. It is positional and machine-checkable, so nothing has
to be maintained and nothing can lie about itself.

**What it replaces, and why.** `status: canonical` became an over-powerful
attractor: once a doc was stamped, every later session cited that frozen
snapshot instead of the accumulated whole, so an old file outranked newer
cumulative work. Farrice named this precisely — *"everything seems to refer
back to that one document instead of it being collectively looked at as a
whole."* The proof was live in the repo the day he said it: `CANON.md` marked a
2026-07-28 profile doc canonical while the real work was the 2026-08-06
rebuild. **`status: canonical` is retired.** `superseded_by:` survives for one
narrow case — a doc that was *wrong*, not merely older. Older is the date rule's
job now.

**How an agent decides what to read:** open `START-HERE.md`, then read the
living docs it lists. Open a dated file only when you need the history of a
decision, never as the thing to build on.

**How work gets absorbed:** write the dated record, then edit the living doc in
place. The front door reports any record newer than its bucket's living doc as
*unabsorbed* — that is the standing detector for the trap above. Absorption is
judgment and is never automated.

**A new file must earn its existence.** Purpose, audience, approval state, or
evidence changed materially: create a date-led milestone record, then absorb
the decision into the living document. Editing passes, cleanup, formatting, and
minor wording: update the living document in place. Git and Google Docs already
hold revision history; do not create `v2`, `v3`, `final`, or `latest` as a
substitute. Google Doc exporters keep one ignored source-to-Doc-ID registry and
update that Doc unless `--new-milestone` is explicitly chosen.

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
