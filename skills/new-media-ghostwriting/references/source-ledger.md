# Source Ledger — New Media Ghostwriting (Compound: Nicolas Cole × a16z × Grace Andrews × Lara Acosta)

Every source consulted for this repair pass, plus a claim-by-claim status for every
pattern/quote added to `genius.md` and referenced from `SKILL.md`. Labels: **VERIFIED**
(verbatim quote or unambiguous paraphrase located directly in a primary-source transcript,
confirmed by direct file read this pass) / **LIKELY** (consistent with the expert's
documented framework per a synthesis document, but no verbatim primary-source transcript
exists in this repo to independently confirm) / **UNCONFIRMED** (no supporting text found
anywhere in this repo; flagged, not silently dropped).

## Sources Consulted (all confirmed non-empty by direct read or `wc -c` this pass)

| Source | Bytes | Type | Status |
|---|---|---|---|
| `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` | 30,638 | Raw YouTube transcript, single continuous line — "30-day plan to land writing clients" | VERIFIED present, read in full |
| `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | 21,487 | Raw YouTube transcript, single continuous line — "5 ways to land clients without a portfolio" | VERIFIED present, read in full |
| `extractions/nicolas-cole/transcript.txt` | 18,152 | Raw YouTube transcript, single continuous line — offer-stacking/digital-products talk | VERIFIED present, read in full (tangential to ghostwriting voice-capture; used for Cole's general "sales is education" voice texture only, not cited as a ghostwriting-specific claim) |
| `extractions/marc-andreessen-ben-horowitz/transcript.txt` | 55,427 | Raw ~45-min a16z internal video transcript | VERIFIED present, grep-confirmed for specific quotes this pass |
| `extractions/marc-andreessen-ben-horowitz/extraction-report.md` | 21,552 | Synthesis document built from the above transcript | Used only to locate WHERE to grep in the raw transcript; claims re-verified against `transcript.txt` directly, not taken on the report's word alone |
| `extractions/grace-andrews/extraction-report.md` | ~13,700 (227 lines) | Synthesis document — **no underlying raw transcript file exists in this repo** | Confirmed via `find extractions -iname "*grace*"` this pass: only this one file exists under `extractions/grace-andrews/`. All content sourced from it is LIKELY, never VERIFIED. |
| `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` | 31,860 | Raw YouTube transcript, single continuous line — "4321 LinkedIn playbook" | VERIFIED present, read in full |
| `extractions/lara-acosta/transcript.txt` | 64,332 | Raw YouTube transcript | VERIFIED present (not re-read in full this pass; already independently verified in the sibling repair `skills/lara-acosta-linkedin-growth/references/source-ledger.md`, dated earlier this Wave 3 batch) |

**Note on `wc -l` returning 0**: several of these transcripts report `0` lines via `wc -l`
because they are single unbroken paragraphs with no embedded newlines — this is a
transcription-format artifact, not evidence of an empty or corrupted file. Verified via
`wc -c` (byte count) and direct `Read` before drawing any conclusion, per the envelope's
rule against false "unrecoverable/0-byte" claims.

## Claim-by-Claim Ledger

| Claim (as it appears in `genius.md` / `SKILL.md`) | Status | Evidence |
|---|---|---|
| "As a ghost writer... confidential. So I'm not at liberty to share who I work with" | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v2/transcript.txt` |
| "we worked with over 300 different industry leaders... 300 plus clients... Zero. actually zero." | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v2/transcript.txt` |
| "we wrote 800word thought leadership articles... more... per month than Inc. Magazine and Forbes combined" + "23 plus full-time employees" | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v1/transcript.txt` |
| "You should never be charging less than $3,000 for a project or per month" | **VERIFIED** | Verbatim (near-exact, minor transcription artifacts) in `nicolas-cole-ghostwriting-v1/transcript.txt` |
| Quora / "$800 a month studio apartment" / "8,000 followers" | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v2/transcript.txt` |
| "your credibility is irrelevant... articulating your problem in detail" | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v2/transcript.txt` at char offset ~19,193 (confirmed via direct string search this pass) |
| "You can't be half and half... the whole motion of the old world will kill you in the new world and vice versa" | **VERIFIED** | Verbatim (transcription artifacts: "you can't be half and half the because...") in `marc-andreessen-ben-horowitz/transcript.txt`, grep-confirmed this pass |
| "we can go on... 30 podcast[s]... When in doubt, flood the zone" | **VERIFIED** | Verbatim, two adjacent passages in `marc-andreessen-ben-horowitz/transcript.txt`, grep-confirmed this pass |
| "Jordy from TBPN has this concept of a Joe Rogan CEO... someone like an Alex Karp, someone like a Palmer Lucky" | **VERIFIED** | Verbatim (transcription renders "Luckey" as "Lucky") in `marc-andreessen-ben-horowitz/transcript.txt`, grep-confirmed this pass |
| "would come off stage having deliberately said absolutely nothing and would have been thrilled" | **UNCONFIRMED** | This specific phrasing (carried into this skill's genius.md only as an explicit paraphrase, flagged as such) was NOT located verbatim in `transcript.txt` via targeted grep this pass. It appears in the sibling skill `skills/andreessen-horowitz-new-media/genius.md` line 12 as a direct quote — that skill's own provenance was not re-audited here. Treated as LIKELY-via-sibling-skill, not independently re-verified against the raw transcript in this pass. |
| "80-year aberration" / "80-Year Plastic Reign" framing | **LIKELY** | The underlying idea (corporate branding as a mid-20th-century communications artifact) is present in `extraction-report.md`; the specific "80-year" phrasing was not located verbatim in `transcript.txt` via this pass's grep (only found in the extraction-report synthesis). |
| Grace Andrews — "media company that happens to sell a product" | **LIKELY** | No raw transcript exists; sourced from `extractions/grace-andrews/extraction-report.md` Executive Summary, itself a third-party synthesis of a YouTube interview, not Grace Andrews's own written words |
| Grace Andrews — City Map (Grand Central/Destinations/Lines/Passengers) | **LIKELY** | Same source; consistent with the DOAC exemplar in the same report but not verbatim-confirmable |
| Grace Andrews — DOAC "10M views... 500K... podcast" production-split example | **LIKELY** | Same source, presented in the report as an illustrative example, not a direct quote |
| Grace Andrews — hypothetical "You're speaking at everyone and reaching no one" line | **UNCONFIRMED as a direct quote** | The extraction-report itself frames this as "Grace would say" — i.e., the report's own author is speculating/paraphrasing, not quoting. Deliberately excluded from `genius.md` as a blockquote to avoid presenting a fabricated line as verbatim. |
| "70 to 80% of my own revenue comes from email, not LinkedIn directly" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "I've got 300,000 followers... three six and seven figure businesses" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "4321 LinkedIn content playbook" (four posts/week, three content types, two audiences, one revenue mechanism) | **VERIFIED** | Verbatim structure and naming in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "Yasmin Alec... 1 + three rule... 4x more profile views" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` (transcript renders the name "Yasmin Alec" — the system's existing skill for this person is filed as `jasmin-alic`; this is a transcription-spelling variant of the same name, not a different person — flagged so a future pass doesn't treat it as a new entity) |
| "$10,000 passively... from comments... Gum Road" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "you can't just post and let the algorithm do its thing... don't post at all" | **VERIFIED** | Verbatim (close paraphrase of adjacent sentences) in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "Cross-posting identical content across platforms" (anti-pattern) | **VERIFIED (via sibling skill)** | Directly sourced from the already-audited `skills/andreessen-horowitz-new-media/genius.md`, "Platform-Native Obsession" pattern — that skill's own genius.md cites this against the same `marc-andreessen-ben-horowitz` transcript set |
| "Luke Iha methodology" (referenced in `workflows/01-voice-to-media-empire.md` Step 7, pre-existing content, not authored this pass) | **UNCONFIRMED** | No Luke Iha source file exists under `extractions/` matching this skill's compound expert set; this is pre-existing workflow content carried forward, named as a gap in `genius.md` Known Gaps rather than silently left unlabeled |

## Known Gaps (Named, Not Hidden)

1. **Grace Andrews has zero raw-transcript coverage in this repo.** Every Grace Andrews
   claim in this skill (and inherited by `SKILL.md`'s framework table, which lists
   "City Map Architecture — `grace-andrews-media-company` — Content strategy backbone") is
   LIKELY, not VERIFIED. A future pass should locate and add the source YouTube video
   ("Marketing GENIUS: If You Want To Grow An Audience In 2026, I'd Do This," *Anatomy of a
   Dream* podcast, Tiffany K. Guillen) as a raw transcript.
2. **One a16z direct quote already live in the sibling skill's genius.md** ("would come off
   stage having deliberately said absolutely nothing") was not independently re-verified
   against the raw transcript in this pass — flagged UNCONFIRMED-in-this-pass rather than
   silently inherited as VERIFIED.
3. **"Luke Iha methodology"** referenced in the pre-existing workflow file has no matching
   extraction source in this skill's compound set — carried forward as pre-existing content,
   labeled UNCONFIRMED, not re-authored or removed (additive-first boundary).
