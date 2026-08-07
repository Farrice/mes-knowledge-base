# The canonical stamp became an attractor — the living-vs-record rule replaced it

**Date**: 2026-08-07 · **Reported by**: Farrice · **Status**: shipped

## The problem, in his words

> "What ends up happening with the use of 'canonical' — it's too overpowering.
> Whatever has that title attached to it ends up superseding actual current
> files, current doctrine, or current research, and then it keeps getting
> referred back to... everything seems to refer back to that one document
> instead of it being collectively looked at as a whole."

He was right, and the proof was live in the repo the same day. `CANON.md` in
the LinkedIn project marked `2026-07-28-PROFILE-GO-LIVE-TONIGHT.md` as
canonical while the actual current profile work was the 2026-08-06 rebuild.
Every session reading CANON.md was being pointed at a nine-day-old snapshot
and told it was truth.

The stamp has three structural failures:

1. **It freezes.** A stamp records what was true when someone typed it. Nothing
   re-evaluates it, so it ages into a lie while still carrying authority.
2. **It outranks accumulation.** A stamped snapshot beats the sum of newer work
   because the newer work carries no stamp.
3. **It needs maintenance nobody does.** `CANON.md` ended with the line
   "Unmarked (279 docs)" — it only knew 19 of 298 files, because
   `artifact_frontmatter_guard.py` bans frontmatter in human-facing docs, so
   almost nothing carried the field the canon system depended on.

## The fix

> **A filename that LEADS with `YYYY-MM-DD-` is a RECORD** — a receipt of one
> session, never truth, never built on.
> **No leading date = LIVING** — one per slot, at the bucket root, updated in
> place.

Why this works where the stamp did not:

- **Positional, so it cannot lie.** The marker is the filename. There is no
  second place for it to disagree with.
- **Nothing frozen can be canonical.** The trap is structurally impossible:
  anything dated is by definition a record.
- **Zero maintenance.** No field to write, none to keep current.
- **"Current" comes from git**, never a stamp — and specifically from *last
  actually worked on*: a commit touching 40+ files in one initiative is
  housekeeping and does not count, and **a rename is not work at all**.

`status: canonical` is retired. `superseded_by:` survives only for a doc that
was *wrong*, not merely older.

## What enforces it

- `execution/front_door.py` — generates the one `START-HERE.md` +
  Premium Minimal HTML board per initiative. Its **Unabsorbed records** section
  is the standing detector: any record newer than its bucket's living doc is
  work that outran the truth. Its **Competing versions** section groups undated
  files by normalised slot, which is how fourteen parallel profile copies
  become one visible line.
- `execution/hooks/superseded_read_guard.py` — path-only RECORD branch. The
  moment any session opens a dated file it hears "this is a record from
  <date>, the living doc is X." Works with no frontmatter, which matters
  because 279 of 298 docs had none.
- `execution/hooks/artifact_placement_hook.py` — LIVING SLOT nudge at write
  time: creating a second undated file for an occupied slot says so, and offers
  the date prefix as the alternative. ~25ms, never blocks.

## The other half: four front doors

The same project had `CAMPAIGN.md`, `CANON.md`, `INDEX.md` and
`04-deliverables/00-CONTROL-TOWER.md` all claiming to be the entry point.
CONTROL-TOWER announced itself as *"The ONE index. Open this first"*, was dated
2026-06-30, and pointed at a $500 offer killed five weeks earlier. Eight
per-folder READMEs footered back to it. `CAMPAIGN.md`'s own 16 artifact links
were written `../02-offer/…` from a file at the project root, so they resolved
to `_active/02-offer/` — the file every session is told to read first could not
be clicked.

**Rule: exactly one front door per initiative, and it is generated.** Anything
else that starts claiming to be an index gets reported as drift.

## Do not re-derive

Full standard: `directives/artifact-placement.md`. The move-tooling traps found
while shipping this (blind verifier, silent grep failure, shortening-rename
rewrite returning 0, stub-corrupting rollback, snapshot projects, rename-loses-
history) are catalogued there under **Moving Things** — every one was found by
measurement, not by reading the code.
