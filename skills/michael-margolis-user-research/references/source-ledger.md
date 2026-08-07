# Source Ledger — michael-margolis-user-research

Wave 3 Lane 4 Batch 11 repair (2026-07-17/18). Every claim added or already present in
`genius.md` labeled VERIFIED / LIKELY / UNCONFIRMED against what was actually found on
disk. Search performed per envelope rule 2 — absence verified, not assumed.

## Search performed

```
$ ls extractions/ | grep -i margolis    → 0 results
$ find extractions -iname "*margolis*"  → 0 results
$ find . -iname "*margolis*" -not -path "./.claude/worktrees/*"
  ./agents/michael-margolis
  ./.tmp/wave3-lane4-b11/audit-michael-margolis-user-research.txt
  ./.claude/commands/michael-margolis.md
  ./.claude/commands/michael-margolis-user-research.md
```

No `extractions/` directory exists for Michael Margolis. `SKILL.md` frontmatter states
`source: claude.ai export 2026-07-01` — this points at the git-ignored web-export corpus
described in `docs/claude-export-import.md`, whose raw conversation files are staged only
inside `_archive/claude-export-2026-07-01.tar.gz` (a 332,779,255-byte archive; `wc -c`
confirmed) and are NOT present in the working tree (`.tmp/claude-export/` does not exist
on disk; only `_active/harness/claude-export/` metadata/index does). This repair opened the
archive directly rather than declaring the source unrecoverable.

## Locating the source (name fragments, no punctuation, per-member tarfile scan)

```python
import tarfile
t = tarfile.open('_archive/claude-export-2026-07-01.tar.gz', 'r:gz')
for m in t:
    if 'margolis' in m.name.lower() or 'bullseye' in m.name.lower():
        print(m.name, m.size)
```
→ 0 filename matches (conversation files are named by UUID, not by title).

Cross-referenced `_active/harness/claude-export/index.json` (present on disk, not git-ignored) by
grepping the `title` field for "margolis" — found 3 conversation records with `md_path`
pointers into the archive's `claude-export/normalized/conversations/<uuid>.md` layout.
Re-scanned the tarball for those exact UUIDs (still no punctuation in the match string)
and extracted each member with `tarfile.extractfile()`, recording real sizes via `wc -c`
after extraction (not assumed from the tar header):

| # | Conversation UUID | Title | `wc -c` (extracted) | Label |
|---|---|---|---|---|
| 1 | `81526288-a470-4353-b247-20ebab6da854` | "[💎📈 BULLSEYE CUSTOMER DEFINITION 10/10/25]…Identify your bullseye customer in one day" | 126,943 bytes | VERIFIED — primary source |
| 2 | `8f994738-1c58-451a-8435-6f475c739237` | "[Research & ICP Prompts]Identify your bullseye customer in one day \| Michael Margolis" | 142,497 bytes | VERIFIED — independent capture of the same raw transcript (see below) |
| 3 | `779c66a8-5c0b-4fa4-9c57-f84fe91841f0` | "…pt.2" (Crown Jewel prompt-generation follow-up) | 20,156 bytes | UNCONFIRMED as Margolis-original — see below |

**What #1 and #2 actually are**: both are Claude-web conversations whose first human
message pastes a raw YouTube auto-transcript (credited "by Merlin AI") of *Lenny's
Podcast* episode "Identify your bullseye customer in one day | Michael Margolis (UX
Research Partner at GV)" (`youtube.com/watch?v=B6Dt1sgGmLI`), then asks Claude to run an
MES 3.0 extraction on it. `diff` between the two files (after stripping headers) shows
they are the same transcript pasted on two separate dates (2025-09-05 and 2025-10-09) —
independent confirmation the transcript text is stable, not two different sources. All
quotes cited in `genius.md`'s new Anti-Patterns section are read directly from the raw
transcript lines (timestamped `mm:ss - <words>`), not from either assistant's derivative
extraction output.

**What #3 is**: a follow-up conversation asking Claude to generate 7 net-new "Crown
Jewel" AI-research prompts *inspired by* Margolis's method but explicitly designed to
*replace* his interview-based method with AI web-scraping — i.e., Claude-generated
derivative content, not Margolis's own words. Not cited as a Margolis quote anywhere in
this repair. Any framework name that appears only in this file (e.g. "Assumption Map")
and not in the primary transcript (#1/#2) is UNCONFIRMED as an authentic Margolis term.

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| "we didn't recruit specifically enough and weren't picky enough about Bullseye customers... it just feels mushy" | VERIFIED | Verbatim, transcript #1 lines 2277–2286 (timestamp 79:42–80:19), cross-present in #2 |
| "we have people manually taking notes and not using AI to take notes... lean out a little bit or maybe you checked your slack" | VERIFIED | Verbatim, transcript #1 lines 1989–1999 (timestamp 69:50–70:22) |
| "I will pay $125 to anybody who... listens to Lenny's podcast... I'm going to get a bazillion people" / open-ended alternative | VERIFIED | Verbatim, transcript #1 lines 1268–1284 (timestamp 43:52–44:56) |
| "you get overcommitted to one idea you're polishing... pushes teams to think of new different possibilities" | VERIFIED | Verbatim, transcript #1 lines 543–551 (timestamp 17:59–18:31) |
| "it should feel comically narrow" (attributed by Margolis to Andy Johns) / "oh for God's sakes Margolis... this is too much" | VERIFIED | Verbatim, transcript #1 lines 774–784 (timestamp 26:09–27:10) |
| "put more weight on past experiences than on people's predictions of what they would do" | VERIFIED | Verbatim, transcript #1 lines 2344–2354 (timestamp 82:27–82:49) |
| Michael Margolis = first UX Research Partner at GV since 2010, 300+ sprints, author of *Learn More Faster* | LIKELY | Stated in the podcast host's intro (transcript #1 lines 67–79); not independently re-verified against an external bio in this repair pass (out of scope — this repair repairs provenance labeling, not fresh biographical research) |
| "Margolis looked at published 'narrow' ICPs from Gong and Linear and said he'd go deeper" (existing `genius.md` Pattern: Comically Narrow) | UNCONFIRMED | Grepped for "Gong" across all three source files — zero matches. "Linear" appears 4 times in transcript #1/#2 but only in the waitlist-as-screener example (timestamp 81:51, already correctly captured in "Pattern: The Sprint Ends With One or Two True Attributes"), never paired with Gong or with "narrow ICP." This claim predates this repair and is left in place (additive-first — not deleting passing content the auditor did not flag), but is flagged here honestly rather than silently re-certified. |
| All 5 remaining "Genius Patterns" bullets (Five and Three in One, Inclusion/Exclusion/Triggers, Non-Telegraphing Screener body text, Humble Inquiry, Two-Part Arc, Three Recipes, Watch Party, Predict Before/Compare After, Past Behavior) | LIKELY | Content and phrasing are directly traceable to transcript #1/#2 on spot-check (e.g. "five and three in one," "humble inquiry," Edgar Schein, the couch-shopping analogy, the cold-chain refrigerated-meds example, the Linear waitlist example all appear verbatim in the transcript); not every sentence was individually re-quoted line-by-line in this pass since named_entity_floor and workflow_contracts already PASS and this repair's scope is the 3 failing checks |
| The 3 workflow files' Output Schema + Quality Gate content | VERIFIED (unchanged) | `execution/skill_auditor.py` heartbeat already reports `workflow_contracts: PASS`; not modified by this repair |

## What this repair did NOT do

- Did not fabricate a YouTube publish date for the underlying podcast episode — every
  date cited is the claude.ai export's own capture timestamp (2025-09-05 / 2025-10-09),
  which is independently verifiable in this repo's `_active/harness/claude-export/index.json`.
- Did not cite conversation #3 (the AI-research-prompt follow-up) as a source of any
  Margolis quote — it is Claude-generated derivative content and is labeled as such.
- Did not delete or silently "fix" the pre-existing Gong/Linear claim in the Comically
  Narrow pattern (it wasn't a failing check and additive-first boundaries apply); flagged
  it UNCONFIRMED here instead so the gap is auditable rather than hidden.
- Did not claim the raw transcript is "unrecoverable" — it was located, extracted, and
  read directly from the archive, with real byte sizes recorded at every step.
