# Provenance — mark-manson-values-psychology repair (2026-07-18)

Anchor → source file + location for every claim added or newly cited in this repair. Full claim table also lives in `references/source-ledger.md`; this file is the flat anchor index the adversarial verifier can walk quote-by-quote.

Ground-truth discovery: `ls extractions/ | grep -i manson` returned nothing — no `extractions/` directory exists for this expert. Real source material was traced via `agents/mark-manson/memory/context.md` (names the two Solved Podcast episodes) → `_active/claude-export/harvest/census-full.json` (contains an "expert": "Mark Manson" entry with 4 unique conversation IDs) → the 332MB `_archive/claude-export-2026-07-01.tar.gz`, opened with Python's `tarfile` module and the 4 specific conversation `.md` members extracted by exact tarball path (never assumed absent — recovered and read in full).

| Anchor location in genius.md | Source file (in `raw-sources/`) | Line range | Verbatim anchor |
|---|---|---|---|
| Model Calibration — gut/rider example | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 3075-3090 | "You know what I just did there — I just made all that up after the fact too... that was the writer justifying my elephant." |
| Desert Island Discrepancy — Source line | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 2919-2925 | "if there is a large discrepancy... that's a sign that a lot of what you're prioritizing in your life [is] not actually your values." |
| Frustration Forensics — Source line | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 3005-3013 | "I see incompetence in the world and it just... drives me insane... this goes back to my mastery." |
| Three-Layer Happiness Stack — Source line | `5c9b1db0-a6dc-401d-9ea9-dc2a2dc1f3a9.md` | 1112-1128 | "Affect is probably measurable on minutes to days... years to decades... we have that absolutely backwards." |
| Anti-pattern 1 (preference vs. value) | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 374 | "my preference is for steak over chicken. That's not a value." |
| Anti-pattern 2 (distrust of surveys) | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 792-794 | "I've been through value surveys before and they're always... different." |
| Anti-pattern 3 (rider/elephant, Haidt 2012) | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 2500-2517, 3075-3090 | "The Righteous Mind. It came out in like 2012" + gut/rider self-catch (same quote as Model Calibration) |
| Anti-pattern 4 (golf/Tiger Woods) | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 3197-3249 | "the hilarious part about this is that I hate golf" |
| Anti-pattern 5 (happiness stack backwards) | `5c9b1db0-a6dc-401d-9ea9-dc2a2dc1f3a9.md` | 1120-1135 | "we approach this backwards... I think we have that absolutely backwards." |
| Anti-pattern 6 (eulogy/validation) | `2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` | 2972-3005 | "nobody's going to stand up at your funeral and say he [bleep] like a wildebeest and had the best golf swing I've ever seen." |

## Pre-existing claims spot-checked (not modified, confirmed still grounded)

- Schwartz value theory / six markers: `2a2e8433...md` lines 230-244.
- Sacrifice Test: `2a2e8433...md` lines 636, 875-913.
- Self-Confrontation / Rokeach / civil-rights era: `2a2e8433...md` lines 4139-4172 (transcript renders the name "Milton Roich" — ASR artifact for Rokeach, noted in the ledger, not silently corrected in the raw quote).
- Post-traumatic growth / Dabrowski's positive disintegration: `2a2e8433...md` lines 3444-3477, 3630-3664 (transcript renders "Droski"/"Drowski").
- Volume-knob calibration (10→9, 4→6): `2a2e8433...md` lines 3130-3178.
- Aristotle / 17 virtues / Nicomachean Ethics: `2a2e8433...md` lines 1213-1235.

## No fabricated-absence claims

No claim in this repair asserts a source is missing or unrecoverable. Every quote cited above was located by direct text search inside the extracted conversation files (sizes recorded via `wc -c` in `references/source-ledger.md`: 298,555 / 260,414 / 59,064 / 37,873 bytes — none 0-byte, none truncated).
