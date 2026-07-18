# Source Ledger — taylor-welch-wealthy-consultant

Repair pass 2026-07-17/18 (Wave 3 Lane 4 Batch 17). Every anchor added to
`genius.md` traced to a real, on-disk source and labeled VERIFIED / LIKELY /
UNCONFIRMED. No quote or figure below was invented to satisfy the auditor.

## Search performed (absence verified, not assumed)

- `ls extractions/ | grep -i welch` → 0 results. `find extractions -iname
  "*welch*" -o -iname "*wealthy*"` → 0 results. No `extractions/` folder
  exists for Taylor Welch — confirmed by directory listing, not inferred.
- `grep -rli "taylor welch" extractions/` → 0 hits (exact-phrase, case
  insensitive, whole corpus).
- Per rule 2 of the envelope, absence claims require verification before
  being written down — so the search widened to
  `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, `wc -c`,
  not `wc -l`), per the envelope's mandated fallback.
- Wrote a Python `tarfile` script that opened every member (7,720 files
  total) and searched member *content* — not filenames — for `Taylor
  Welch`, `Wealthy Consultant`, `Traffic and Funnels`, `Traffic & Funnels`,
  `Quantum Growth`, `The Deep End`. 22 matches found, all inside
  `claude-export/normalized/conversations/*.md` (individual archived
  Claude.ai chat exports) plus the raw `conversations.json`.
- Four of the highest-signal matches were extracted to a scratchpad and
  read in full:

| Archive member | Title | Size (`wc -c`) |
|---|---|---|
| `claude-export/normalized/conversations/76d8b6c8-b309-417d-96a6-f1de26519ba4.md` | "Taylor Welch: Quantum Growth Framework pt.1" | 11,213 bytes |
| `claude-export/normalized/conversations/e8e1c310-8784-457e-adb7-62baf0342646.md` | "Taylor Welch: Quantum Growth Framework pt.2" | 91,211 bytes |
| `claude-export/normalized/conversations/92b287b2-6402-46ee-b21a-1c6849e106ed.md` | "Taylor Welch: The Cycle of Trauma (spiritual scars, psychosomatics, & healing)" | 141,192 bytes |
| `claude-export/normalized/conversations/b076aae8-00f0-4aee-9935-fddca63897e3.md` | "Farrice Cain: Ghostwriting Niche & Positioning & Offer Discovery" | 100,582 bytes |

## What each source actually is

- **76d8b6c8** and **e8e1c310** (Quantum Growth Framework pt.1/pt.2): a
  Claude.ai MES-3.0 extraction session where Farrice fed Claude the
  *"Quantum Workbook.pdf"* (Welch's Quantum Growth Track companion
  workbook) and had Claude generate derivative "virtuoso mastery"
  analysis and prompt artifacts. This is **Claude's paraphrase and
  extraction commentary on Welch's material, not Welch's own words** —
  useful as corroborating structure (values-before-goals, Morning
  Formula, ceiling-to-floor, reverse teleology all appear here,
  matching the existing `genius.md` patterns) but every specific
  "quote" inside it is Claude's synthesis, not verbatim Welch. Labeled
  LIKELY, not VERIFIED, and NOT used as an anti-pattern anchor for that
  reason.
- **92b287b2** (The Cycle of Trauma): contains a **full verbatim,
  auto-generated (Merlin AI) YouTube transcript** of Taylor Welch's
  "The Deep End" podcast episode, pasted in by Farrice as a human-turn
  attachment (lines 24–2851 of the normalized `.md`). Source video:
  https://www.youtube.com/watch?v=_4060bW0p1Y. This is genuine primary
  material — Welch and his co-host ("Jake") speaking, transcribed with
  timestamps, no editorializing. **This is the source for all 6
  anti-pattern anchors in `genius.md`.** Every quote used was checked
  against this file's actual text (see `PROVENANCE.md` for line
  numbers) before being written down.
- **b076aae8** (Farrice's ghostwriting niche session): incidental
  name-drop of Taylor Welch as a reference point in an unrelated
  strategy conversation. Not used as a source for any claim.

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| Taylor Welch built Traffic & Funnels / The Wealthy Consultant | LIKELY | Public-figure biographical claim, consistent across both extraction sessions and the skill's pre-existing frontmatter; not independently re-verified via live web search in this repair (out of scope — this is a heartbeat-check repair, not a fresh extraction). |
| Values-Before-Goals, Reverse Teleology, Weed-Root Protocol, Five-Dimensional Wealth Hierarchy, Value-Scarcity Positioning, Ceiling-to-Floor (existing `genius.md` patterns, untouched by this repair) | LIKELY | Corroborated structurally by the Quantum Growth Framework pt.1/pt.2 extraction sessions (Claude's derivative synthesis of the actual Quantum Workbook PDF) — consistent terminology across two independent extraction passes, but no verbatim page-image of the workbook itself was located to VERIFY word-for-word. |
| "Trauma is not just what you use to justify being rude... reasoning device to justify them doing the wrong thing" | VERIFIED | Verbatim in `92b287b2...md`, transcript lines 227–237 (timestamps 7:31–7:58). Read directly, quote checked word-for-word against the file. |
| "This guilt will wrap around your neck and it will slowly suffocate you unless you get free" | VERIFIED | Verbatim in `92b287b2...md`, transcript lines 704–707 (timestamps 26:59–27:11). |
| "I got to audit all the trauma that came from when I was 17 and why I believed what I believed about myself" | VERIFIED | Verbatim in `92b287b2...md`, transcript lines 448–451 (timestamps 16:19–16:32); "the FTC" reference at line 448 (16:23) is Welch's own case, not fabricated. |
| "Constantly getting up to the edge and then it's breaking down right before you cross over the threshold" | VERIFIED | Verbatim in `92b287b2...md`, transcript lines 2603–2606 (timestamps 101:43–101:49). |
| "No man it's not Satan he doesn't care enough" | VERIFIED | Verbatim in `92b287b2...md`, transcript lines 1659–1661 (timestamps 64:37–64:42). |
| "Discipline is a form of love it's a form of hey you're actually in the family and I love you enough to do that" | VERIFIED | Verbatim in `92b287b2...md`, transcript lines 1671–1673 (timestamps 65:05–65:12); Welch attributes the idea's origin to "Jeremy Riddle" in the same breath (line 1669–1670), not claimed here as originally his — the quote anchor is his articulation of it on the show, which is what the anti-pattern cites. |
| workflow files (`01-rewire-wealth-identity.md`, `02-architect-quantum-growth-plan.md`, `03-navigate-wealth-thresholds.md`) carry Output Schema + Quality Gate | VERIFIED | Confirmed by `execution/skill_auditor.py` heartbeat check (workflow_contracts: PASS, pre-existing, unchanged by this repair). |

## What this repair did NOT do

- Did not invent a Welch quote, date, or episode citation to force the
  anti-pattern check to pass — all 6 anchors trace to a real,
  verbatim, timestamped transcript recovered from the archive, with
  line numbers recorded in `PROVENANCE.md`.
- Did not upgrade the Quantum Growth Framework pt.1/pt.2 material from
  LIKELY to VERIFIED — it is Claude's derivative extraction of a PDF
  workbook, not Welch's own words, and is labeled accordingly even
  though it corroborates the pre-existing `genius.md` patterns.
- Did not touch `SKILL.md`, the workflow files, or `references/prompts-v2/`
  — those checks (`verbatim_exemplars`, `named_entity_floor`,
  `workflow_contracts`) were already passing per the audit and are
  preserved untouched.
- Did not create a formal `extractions/taylor-welch-wealthy-consultant/`
  folder — the primary source lives inside the general claude-export
  archive, not as a dedicated extraction directory. Flagged here as a
  gap: a future `/extract-forge taylor-welch` pass against the full
  "Cycle of Trauma" transcript (and the other four Deep End episodes
  named in `genius.md`'s intro) would formalize this into a proper
  extraction with a reference corpus, closing the LIKELY→VERIFIED gap
  on the pre-existing Genius Patterns.
