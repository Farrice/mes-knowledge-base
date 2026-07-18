# Source Ledger — New Media Kingmaker (Compound: a16z × Grace Andrews × Luke Iha × Nicolas Cole × Lara Acosta × Cardinal Mason)

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 12). Every source consulted for this pass, plus
a claim-by-claim status for every pattern/quote added to `genius.md` and referenced from
`SKILL.md`. Labels: **VERIFIED** (verbatim quote or unambiguous paraphrase located directly
in a primary-source transcript, confirmed by direct file read this pass) / **LIKELY**
(consistent with the expert's documented framework per a synthesis document or AI-run chat
extraction, but no raw primary-source transcript of the expert's own live words exists in
this repo to independently confirm) / **UNCONFIRMED** (no supporting text found anywhere in
this repo; flagged, not silently dropped).

## Sources Consulted (all confirmed non-empty by `wc -c` and/or direct `Read` this pass)

| Source | Bytes | Type | Status |
|---|---|---|---|
| `extractions/marc-andreessen-ben-horowitz/transcript.txt` | 55,427 | Raw ~45-min a16z internal video transcript | VERIFIED present, grep-confirmed for specific quotes this pass |
| `extractions/grace-andrews/extraction-report.md` | 25,439 | Synthesis document — **no underlying raw transcript file exists in this repo** | Confirmed via `find extractions -iname "*grace*"`: only this one file exists. All content sourced from it is LIKELY, never VERIFIED |
| `extractions/luke-iha/transcript.txt` | 32,648 | Raw YouTube transcript, single continuous line — "number one thing" client-getting video, contains the Proof Ladder segment | VERIFIED present, read in full this pass |
| `extractions/luke-iha-hooks/transcript.txt` | 25,569 | Raw YouTube transcript, single continuous line — "vicious hooks, eight principles" video | VERIFIED present, read in full this pass |
| `extractions/luke-iha/video-8-proof-ladder/extraction-report.md` | 17,119 | Synthesis document built from a Proof Ladder video | Used only as a cross-check pointer; the Proof Ladder quote actually used in `genius.md` was independently located in `luke-iha/transcript.txt` directly, not taken on the report's word alone |
| `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` | 30,638 | Raw YouTube transcript — "30-day plan to land writing clients" | VERIFIED present; quote reused from prior sibling-skill verification (`skills/new-media-ghostwriting/references/source-ledger.md`), spot-checked again this pass |
| `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | 21,487 | Raw YouTube transcript — "5 ways to land clients without a portfolio" | VERIFIED present; quote reused from prior sibling-skill verification, spot-checked again this pass |
| `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` | 31,860 | Raw YouTube transcript — "4321 LinkedIn playbook" | VERIFIED present; quote reused from prior sibling-skill verification, spot-checked again this pass |
| `knowledge/extractions/inbox/Claude-✍️ 💎💰 Cardinal Mason ! FREE AI Copywriting Course ! How to make $500k!year in 2026.md` | 391,128 | Claude.ai chat export, Part 1 — AI-run MES 3.0 extraction pass over Cardinal Mason's course material, not his own raw words | Confirmed non-empty via `wc -c`. No `extractions/cardinal-mason*` folder exists in this repo (confirmed via `find extractions -iname "*cardinal*"`, zero matches) |
| `...pt.2.md` (same series) | 355,727 | Part 2 — deployable prompt specs, incl. "Email Sequence Executioner" (#3) and "Master Conversion Sequencer" (#30) | Confirmed non-empty via `wc -c`; grep-located both named prompts this pass |
| `...pt.3.md` (same series) | 59,118 | Part 3 — course-content and authority-PR prompt specs | Confirmed non-empty via `wc -c`; not directly quoted in `genius.md` this pass, listed for completeness |

**Note on `wc -l` returning 0 for several transcripts**: several `.txt` files above report
`0` via `wc -l` because they are single unbroken paragraphs with no embedded newlines — a
transcription-format artifact, not evidence of an empty or corrupted file. Verified via
`wc -c` (byte count) and direct `Read`/`grep` before drawing any conclusion, per the
envelope's rule against false "unrecoverable/0-byte" claims.

## Claim-by-Claim Ledger

| Claim (as it appears in `genius.md`) | Status | Evidence |
|---|---|---|
| "You can't be half and half... the whole motion of the old world will kill you in the new world and vice versa" | **VERIFIED** | Verbatim in `marc-andreessen-ben-horowitz/transcript.txt` |
| "We can go on... 30 podcast[s]... When in doubt, flood the zone" | **VERIFIED** | Verbatim, two adjacent passages in `marc-andreessen-ben-horowitz/transcript.txt` |
| "Jordy from TBPN has this concept of a Joe Rogan CEO... someone like an Alex Karp, someone like a Palmer Lucky" | **VERIFIED** | Verbatim (transcript renders "Luckey" as "Lucky") in `marc-andreessen-ben-horowitz/transcript.txt` |
| Grace Andrews — City Map (Grand Central/Destinations/Lines/Passengers) | **LIKELY** | `extractions/grace-andrews/extraction-report.md`, GP-6 — no raw transcript exists |
| Grace Andrews — DOAC "10M views... 500K... podcast" production-split example | **LIKELY** | Same source, Exemplar 2 — presented as an illustrative example, not a direct quote |
| "A vicious hook goes right for the gut, right? It's something that sounds unreasonable... transgressive or dangerous" | **VERIFIED** | Verbatim in `luke-iha-hooks/transcript.txt` |
| "the vicious version is always the most specific, most embodied, most uncomfortable, and most charred version" | **VERIFIED** | Verbatim in `luke-iha-hooks/transcript.txt` |
| "My husband came out as gay after 26 years of marriage and it nearly killed me" (Iha's own hook example) | **VERIFIED** | Verbatim in `luke-iha-hooks/transcript.txt`, presented in-transcript as his own teaching example |
| "I've personally done over 100 million in sales, uh at least one VSL doing 100 million" | **VERIFIED** | Verbatim (transcript renders "VSSL" for "VSL", a transcription artifact) in `luke-iha-hooks/transcript.txt` |
| "There is a proof ladder, right? And there's seven different types of proof... The first one is a resume" | **VERIFIED** | Verbatim in `extractions/luke-iha/transcript.txt`, located via direct `Read` at the "seven different types of proof" passage |
| "As a ghost writer... confidential. So I'm not at liberty to share who I work with" | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v2/transcript.txt` |
| "we worked with over 300 different industry leaders... 300 plus clients... Zero. actually zero." | **VERIFIED** | Verbatim in `nicolas-cole-ghostwriting-v2/transcript.txt` |
| "70 to 80% of my own revenue comes from email, not LinkedIn directly" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "I've got 300,000 followers... three six and seven figure businesses" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "4321 LinkedIn content playbook" | **VERIFIED** | Verbatim structure and naming in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| "top creators like myself are doing over a thousand comments per week. Not posts, comments" | **VERIFIED** | Verbatim in `lara-acosta/2026-linkedin-playbook-transcript.txt` |
| Cardinal Mason — "Email Sequence Executioner" (prompt #3, Welcome/nurture/webinar sequences) | **LIKELY** | Named and indexed in `knowledge/extractions/inbox/...pt.2.md` prompt table — this is an AI-run extraction of his course, not his own primary-source words |
| Cardinal Mason — "Master Conversion Sequencer" combining his methodology with Gary Halbert's "pile of proof" and Frank Kern's "intent-based branding" | **LIKELY** | Verbatim prompt text located in `...pt.2.md`, APEX Prompt #30 — same LIKELY caveat applies |
| "Luke Iha proof-copy" / `skills/luke-iha-proof-copy` skill reference in `SKILL.md` and workflow files | **UNCONFIRMED as a real skill path** | No `skills/luke-iha-proof-copy/` directory exists — closest matches are `skills/luke-iha-proof-ladder` and `skills/luke-iha-vicious-hooks`. Pre-existing naming drift, not introduced this pass, flagged in `genius.md` Known Gaps rather than silently corrected |
| `skills/cardinal-mason/SKILL.md` reference in workflow files | **UNCONFIRMED as a real skill path** | Actual directory is `skills/cardinal-mason-ai-copywriting/`. Same pre-existing drift, flagged not silently corrected |

## Known Gaps (Named, Not Hidden)

1. **Grace Andrews has zero raw-transcript coverage in this repo.** Every Grace Andrews claim
   in this skill is LIKELY, not VERIFIED, until a raw transcript is located and added.
2. **Cardinal Mason has zero raw-transcript coverage in this repo.** The only source is a
   three-part AI-run Claude.ai chat extraction of his course material — LIKELY, never
   VERIFIED, matching the same standard already applied to this identical source in
   `skills/cardinal-mason-ai-copywriting/references/source-ledger.md`.
3. **Two skill-path references inside this skill's own `SKILL.md` and workflow files are
   stale** (`luke-iha-proof-copy`, `cardinal-mason`) — neither directory exists under the
   exact name referenced. This repair pass did not rename these paths (out of scope: the
   heartbeat checks being repaired are content-provenance checks, not link-integrity checks),
   but both are now named explicitly in `genius.md` Known Gaps so a future pass can fix the
   routing rather than rediscover the drift.
