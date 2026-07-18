# New Media Ghostwriting — Provenance Table (Wave 3 Batch 4 Lane 3 repair)

Anchor → source file + approximate character offset, for every quote/entity added to
`genius.md` in this repair pass. Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED labeling
lives in `references/source-ledger.md`; this table is the narrower "where exactly did this
text come from" index the envelope asks for.

Source files (all confirmed non-empty by direct `Read` or `wc -c` this session):
- `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` — 30,638 bytes → **NC1**
- `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` — 21,487 bytes → **NC2**
- `extractions/nicolas-cole/transcript.txt` — 18,152 bytes → **NC3**
- `extractions/marc-andreessen-ben-horowitz/transcript.txt` — 55,427 bytes → **A16Z**
- `extractions/grace-andrews/extraction-report.md` — 227 lines, no raw transcript exists → **GA** (synthesis only)
- `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` — 31,860 bytes → **LA1**

| Anchor text added to `genius.md` | Source | Offset / locator (approx.) |
|---|---|---|
| "As a ghost writer... confidential... worked with people just like you" | NC2 | ~char 2,200 (early in the "5 ways" transcript, after the case-study framing) |
| "we worked with over 300 different industry leaders... Zero. actually zero." | NC2 | ~char 1,050 |
| "we wrote 800word thought leadership articles... Inc. Magazine and Forbes combined" | NC1 | ~char 3,400 |
| "23 plus full-time employees" | NC1 | same passage as above, ~char 3,500 |
| "You should never be charging less than $3,000 for a project or per month" | NC1 | ~char 550 (opening minutes) |
| "$800 a month studio apartment... 8,000 followers" | NC2 | ~char 10,169 |
| "your credibility is irrelevant... articulating your problem in detail" | NC2 | ~char 19,193 |
| "You can't be half and half... will kill you in the new world and vice versa" | A16Z | ~char 3,950 (confirmed via direct string search) |
| "we can go on... 30 podcast[s]" | A16Z | ~char 3,375 |
| "When in doubt, flood the zone" | A16Z | ~char 745 (earlier in the transcript than the "30 podcast" passage — same overall crisis-doctrine discussion, non-contiguous) |
| "Jordy from TBPN has this concept of a Joe Rogan CEO... Palmer Lucky" | A16Z | ~char 15,010 |
| DOAC "10M views... 500K... podcast episode" production-split example | GA | `extraction-report.md`, "Exemplar 2: The Forgettable/Memorable Split at DOAC" section |
| City Map (Grand Central/Destinations/Lines/Passengers) | GA | `extraction-report.md`, GP-6 "City Architecture Thinking" and "Exemplar 1: The DOAC City Map in Action" |
| "media company that happens to sell a product" | GA | `extraction-report.md`, Executive Summary, first bullet |
| "70 to 80% of my own revenue comes from email, not LinkedIn directly" | LA1 | ~char 27,433 |
| "I've got 300,000 followers... three six and seven figure businesses" | LA1 | ~char 1,088 (opening) |
| "4321 LinkedIn content playbook" (four/three/two/one structure) | LA1 | ~char 13,601 |
| "Yasmin Alec... 1 + three rule... 4x more profile views" | LA1 | ~char 21,743 |
| "$10,000 passively... Gum Road" | LA1 | ~char 25,320 |
| "you can't just post and let the algorithm do its thing... don't post at all" | LA1 | ~char 20,471 (the "posting and ghosting" passage) |
| "Cross-posting identical content across platforms" anti-pattern | *(carried from sibling skill)* | `skills/andreessen-horowitz-new-media/genius.md`, "Platform-Native Obsession" pattern, itself anchored to A16Z |

## Checks fixed and how

1. **anti_patterns_sourced** — new `## Anti-Patterns — Sourced` section in `genius.md`, 8
   items, each carrying a file-path anchor (transcript.txt / genius.md) and, for 6 of the 8,
   a verbatim quote. Was 0/0 (no `genius.md` existed).
2. **verbatim_exemplars** — 3 multi-line blockquote blocks under `## Hall of Fame
   Exemplars` (Cole/Quora, a16z/NYT, Lara/commenting economics) plus several standalone
   inline blockquoted verbatim lines in the per-expert sections. Was 0/0.
3. **recognition_test** — `## How to Use This Skill (Model Calibration)` in `genius.md`
   contains the literal phrase "The recognition test: would Nicolas Cole recognize this
   as..." plus "using her vocabulary" — written fresh for this compound skill's specific
   four-voice-blending failure mode, not copied from `ben-watkins-storytelling`.
4. **source_ledger** — new `references/source-ledger.md` with full VERIFIED/LIKELY/
   UNCONFIRMED claim-by-claim table, including the honest Grace Andrews gap.
5. **named_entity_floor** — every `##` section in the new `genius.md` carries at least one
   verbatim quote, dollar figure, or multi-digit number pulled from the sources above.
6. **workflow_contracts** — added `## Output Schema` to
   `workflows/01-voice-to-media-empire.md`, specific to this workflow's deliverable set
   (the four-phase engagement's concrete artifacts); the pre-existing `## Quality Gates`
   section already satisfied the Quality Gate half of the check (confirmed by the audit
   text itself, which only flagged the Output Schema half as missing).
