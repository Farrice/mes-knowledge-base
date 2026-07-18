# PROVENANCE — strength-conditioning-os repair (Wave 3 Batch 2)

Anchor → source file + line, for every quote added in this repair. All line numbers
verified with `grep -n` against the live source files on 2026-07-17.

| Anchor (in my genius.md) | Source file | Line | Exact match confirmed |
|---|---|---|---|
| `Volume past MRV is "junk volume" — cost without return.` | `skills/michael-israetel-hypertrophy/genius.md` | 43 | Yes — `grep -F` exact hit |
| `even a little high-intensity training overflows it and the system fights back` | `skills/andy-galpin-training-intelligence/genius.md` | 88 | Yes — `grep -F` exact hit |
| `trained individuals who "knew" 100kg was a hard 10-rep set hit 20 reps` | `skills/eugene-teo-training/genius.md` | 17 | Yes — `grep -F` exact hit |
| `A plateau is "the body doing its job" — homeostasis` | `skills/alan-aragon-nutrition/genius.md` | 38 | Yes — `grep -F` exact hit |
| `Never prescribe a plan you couldn't imagine the client following for a year.` | `skills/alan-aragon-nutrition/genius.md` | 24 | Yes — `grep -F` exact hit |
| `Distribute ~70% of training volume at moderate intensity... and ~30% at high intensity` | `skills/andy-galpin-training-intelligence/genius.md` | 25 | Yes — `grep -F` exact hit |
| `you can't burn fat while insulin keeps you burning glucose` | `skills/strength-conditioning-os/references/field-guide.md` | 75 | Yes — `grep -F` exact hit (corrected mid-repair; see REPAIR-NOTES) |
| `the same 4×4 done identically forever stops adapting` | `skills/strength-conditioning-os/references/field-guide.md` | 59 | Yes — `grep -F` exact hit |
| `we evolved to be physically active when it was necessary or rewarding, and to rest whenever possible` | `skills/strength-conditioning-os/references/field-guide.md` | 67 | Yes — `grep -F` exact hit |
| `"Comprehensive" output = system failure regardless of score.` (Model Calibration section) | `/Users/farricecain/Google Antigravity/CLAUDE.md` | The Chain header line | Yes — verbatim from CLAUDE.md's opening line, read at task start |

## Ground-truth search performed

`ls extractions/ | grep -iE "galpin|israetel|teo|aragon"` and individual `find
extractions -iname "*<surname>*"` for all four lane experts returned **zero results**
on 2026-07-17. No dedicated raw-transcript extraction folder exists for Galpin,
Israetel, Teo, Aragon, Ethier, Magness, Lieberman, or Bikman anywhere in `extractions/`,
`extractions/transcripts/`, or `extractions/_archive/`. This is reported as a
provenance fact, not assumed — confirmed by actual `grep -l` / `find` runs against
`extractions/transcripts/*.txt` for expert surnames (no hits).

Ground truth for this repair is therefore the two sources the assignment explicitly
sanctions as fallback: (1) the four lane skills' own `genius.md` files (each already
carrying verbatim-quoted material, each stamped `source: "claude.ai export 2026-07-01"`
in its SKILL.md frontmatter), and (2) this hub's own `references/field-guide.md`,
which independently labels each of its 11 entries `[from source]` or `[referenced]`.
No new quote was invented; every quote above traces to one of these two already-vetted
locations, confirmed with `grep -F` exact-string search before being written.

## Anomaly discovered and worked around

`skills/strength-conditioning-os/SKILL.md`, `skills/strength-conditioning-os/genius.md`,
and `skills/strength-conditioning-os/references/source-ledger.md` were **already
modified in the live working tree** when this task began — uncommitted, not made by
this worker (confirmed via `git diff` timestamps and the file's own revision log,
which reads "2026-07-17 | Source ledger created | Wave 3 Batch 3 repair"). That prior
draft used `### Anti-Pattern:` H3 sub-headings instead of markdown list bullets, which
the auditor's `anti_patterns_sourced` check does not count (it only counts `-`/`*`/`N.`
list items) — so despite good sourcing, it still failed the check. That draft also
misnamed two experts ("Ron Bikman" for Benjamin Bikman, "Martin Henselmans" for Menno
Henselmans) and slightly misquoted the Bikman line. Per this task's GIT READ-ONLY
boundary, `skills/` was never touched — this repair was built independently into
`.tmp/wave3-batch2/strength-conditioning-os/`, reusing only the parts of that prior
draft's research that verified correctly, and fixing the rest. See REPAIR-NOTES.md.
