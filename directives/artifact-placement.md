# Artifact Placement — Every Asset Into Its Populated Subfolder

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
then (only-populated). If the placement hook fires on you, do the move it names
before continuing. Moving anything by hand? Use `project_filer.py`, never bare
`mv` — bare moves orphan every inbound link.
