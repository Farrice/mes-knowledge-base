# PROVENANCE — re-compliance-pack repair (Wave 3 Lane 4 Batch 14)

Anchor → source file + location. Ground truth = verbatim content already inside `skills/re-compliance-pack/` plus live verification searches run 2026-07-18 (no matching `extractions/` folder exists for this domain — it's a regulation-derived method skill, not a person extraction; confirmed via `ls extractions/ | grep -i compliance` / `re-compli` → no hits).

| Anchor (in repaired `genius.md` / `workflows/01-fh-auditor.md`) | Source file + location |
|---|---|
| "$19,787" figure, "median" mislabel | `skills/re-compliance-pack/SKILL.md:28`, `README.md:14` (original claim) — corrected framing verified against live search, `references/source-ledger.md` VERIFIED table |
| 24 CFR §100.75 | `skills/re-compliance-pack/genius.md` (original, throughout), `SKILL.md:13,110`, `workflows/01-fh-auditor.md:74,91,146` — verified live at law.cornell.edu/cfr/text/24/100.75, 2026-07-18 |
| NAR Code of Ethics Article 12 | `skills/re-compliance-pack/SKILL.md:13,112`, `README.md:65` — verified live at nar.realtor, 2026-07-18 |
| *Fair Housing Council v. 1734 East 82nd Street* (9th Cir. 2019) | `skills/re-compliance-pack/genius.md` (original "Case Law Armory" §1), `workflows/01-fh-auditor.md:149`, `receipts/audit-test-listing-1.json:53,77,88,151` — searched, not located; UNCONFIRMED per `references/source-ledger.md` |
| *United States v. Newberry* (4th Cir. 1999) | `skills/re-compliance-pack/genius.md` (original "Case Law Armory" §4), `workflows/01-fh-auditor.md:103,151`, `receipts/audit-test-listing-1.json:23,33,153` — searched, not located; UNCONFIRMED |
| *Fair Housing Center v. Sears* (8th Cir. 2009) | `skills/re-compliance-pack/genius.md` (original "Case Law Armory" §2), `workflows/01-fh-auditor.md:150`, `receipts/audit-test-listing-1.json:43,152` — searched, not located; UNCONFIRMED |
| *Fair Housing Center of West Michigan v. Karwoski* (6th Cir. 2015) | `skills/re-compliance-pack/genius.md` (original "Case Law Armory" §5), `workflows/01-fh-auditor.md:152`, `receipts/audit-test-listing-1.json:63,154` — searched, not located; UNCONFIRMED |
| "No smokers" not a protected class | `skills/re-compliance-pack/genius.md` (original "Conditional Red Flags"), `references/test-listings.md:16` (Test Listing 1, dated 2026-07-14) |
| "Walking distance to schools" as familial-status pattern | `skills/re-compliance-pack/references/hud-standards/hud-word-phrase-list.md:120-122`, general HUD advertising guidance confirmed live 2026-07-18 |
| KW MREA 8x8/33-touch | `skills/re-compliance-pack/SKILL.md:29` — verified live against KW official instructor PDF, 2026-07-18 |
| 12 CFR §1026.19 (TRID) | `skills/re-compliance-pack/SKILL.md:115` — verified live at law.cornell.edu/cfr/text/12/1026.19, 2026-07-18 |

No quote was fabricated: every case-law name and CFR/NAR citation used as an anchor already existed verbatim inside the pre-repair skill files (genius.md, SKILL.md, README.md, the workflow, or the receipt JSONs) — this repair pass did not introduce new legal authorities, only verified the existing ones and labeled the four unverifiable case citations UNCONFIRMED instead of silently treating them as settled.
