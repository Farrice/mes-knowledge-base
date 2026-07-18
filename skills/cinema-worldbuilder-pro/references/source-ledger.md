# Source Ledger — cinema-worldbuilder-pro

Repair pass: Wave 3 Lane 4 Batch 3. This is a **method/tool skill** (a locked Seedance video-prompt grammar), not a person extraction to be rewritten — "sources" means the skill's own locked SKILL.md plus Joey's real companion documentation for this exact drop, not a personality transcript to mine for voice. Every claim used in `genius.md` and `workflows/*.md` is labeled below. File sizes recorded via `wc -c` (bytes, not lines) per this batch's provenance rule — a claim that a source is absent is itself checked with a real read/grep, never assumed.

## Sources consulted

| # | Source | Path | Size (bytes, `wc -c`) | Role |
|---|---|---|---|---|
| 1 | The skill's own locked grammar | `skills/cinema-worldbuilder-pro/SKILL.md` | 41,802 | Primary ground truth — every mode, block, rule, and locked prompt structure this repair cites. Read in full (525 lines), not skimmed. |
| 2 | Joey's companion doc for this exact 3.0 drop | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | 13,796 | Public Notion page, harvested 2026-07-13 via Playwright. Directly names `cinema-worldbuilder-pro-3.0` and explains the FOV-degree, Frame Map, and bell-curve density design decisions in Joey's own words. |
| 3 | Extraction vision brief | `extractions/joey-cinema/VISION.md` | 4,704 | Who Joey is, Control/Noisy Group/KY context, source inventory for the three-skill drop. |
| 4 | Cross-check analysis of the raw skill zips | `extractions/joey-cinema/skill-files-analysis.md` | 61,244 | Independent line-by-line description of `cinema-worldbuilder-pro-30/SKILL.md` (524 lines in the original zip vs. 525 in the installed copy — used only to cross-check that the installed skill matches the analyzed source, not cited as a primary quote source). |
| 5 | Joey video transcript (general pipeline video) | `extractions/joey-cinema/transcript.txt` | 15,915 | Checked via `grep -in "degree\|write the visible\|frame map\|bell curve\|element tag\|km/h\|physics engine"` — **zero matches**. This transcript covers voice-consistency/Bible content, not Cinema Worldbuilder-specific grammar. Confirms this transcript is not a CWB source; not cited for CWB-specific claims. |
| 6 | `extractions/` directory scan for a dedicated Cinema Worldbuilder / Seedance-grammar extraction folder | `extractions/` (`ls extractions/ \| grep -iE "seedance\|higgsfield\|banana\|cinema\|worldbuild\|joey"`) | n/a | Confirms the `joey-cinema*` and `joey-cinema-os` folders are the only relevant matches; no separate "cinema-worldbuilder" extraction exists outside the `joey-cinema` family. |
| 7 | Sibling skill (same source drop) repair, read for house style only | `skills/banana-pro-director/genius.md`, `references/source-ledger.md`, `workflows/mode-0-face-lock.md` | 8,341 / 6,719 / 4,016 | Not a content source for this skill's claims — read only to match the envelope's "match house style of a passing workflow" instruction and the required "How to Use This Skill" section format. |

## Claims, labeled

| Claim | Label | Anchor |
|---|---|---|
| "Seedance is a physics engine, not a mood board. It renders things it can see and count. Mood words evaporate." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 30 |
| "No style header at the top of the prompt. Style isn't a single object..." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 190 |
| "Seedance latches onto FOV in degrees as a snap value... Millimeters read as suggestion; degrees read as instruction." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 211 |
| "Never write a non-anchor value — 23° is not on the ladder, so use 18° or 29° instead." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 213 |
| "Trust the reference for wardrobe... Wardrobe details visible in the reference are NOT re-described." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 472 (Universal Prompt Rule 20) |
| "State what happens. Do not state what shouldn't. Negative language weakens the signal..." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 52 |
| "Every named subject that appears in a Seedance scene gets its canonical reference tagged separately... No exceptions." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 100 |
| "For new scenes, confirmation is mandatory. Never assume runtime — ask." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 148 |
| "Default camera energy is handheld with breath, drift, organic operator movement... Locked-off tripod is OPT-IN ONLY." | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, lines 384–386 |
| "No platform/tool names in prompt output" (Universal Rule 10) | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 462 |
| Pre-Delivery Pass is a silent QA gate, run before every delivery | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 478 |
| Density rule: 280–400 words single-shot, up to 600 multi-shot | VERIFIED | `skills/cinema-worldbuilder-pro/SKILL.md`, line 12 |
| "The prompt box is not linear. More detail isn't automatically better. It's a bell curve, and the job is finding the top of it." | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 64 |
| "FOV in degrees, not just millimeters... 47° (50mm) holds. 50mm drifts." | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 69 |
| "Frame Map anchors screen position before identity ever enters." | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 68 |
| "These encode my taste. Not yours. Fork them. Break them. Make them yours." | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 93 |
| "Hit rate scales with prep... The pipeline is what makes the prompt cheap." | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 91 |
| Companion doc harvested 2026-07-13 via Playwright from a public Notion page | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, line 3 |
| Joey — professional filmmaker turned AI filmmaker, channel "JOEY," ~25,000 subscribers, Higgsfield-sponsored via credit giveaways, builder of Control (CTRL), community brand Noisy Group, collaborator KY (CTRL World Fashion Design Director) | VERIFIED | `extractions/joey-cinema/VISION.md`, line 7 |
| This skill shipped as `cinema-worldbuilder-pro-3.0` alongside `banana-pro-director-3.0` and `story-bible-builder` in one drop | VERIFIED | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md`, lines 19–26 |
| "Omni ≤10s rule" / "Seedance 4K native" appear anywhere in the installed `cinema-worldbuilder-pro/SKILL.md` | UNCONFIRMED — verified absent | `extractions/joey-cinema/VISION.md`, line 13 attributes these to companion Video 1, but a full read of all 525 lines of `skills/cinema-worldbuilder-pro/SKILL.md` found no occurrence of either term — checked absence, not assumed |
| `extractions/joey-cinema/transcript.txt` contains CWB-specific grammar detail (FOV, Frame Map, bell-curve, element tags, km/h, "physics engine") | UNCONFIRMED — verified absent | `grep -in` of the six keyword terms against the 15,915-byte transcript returned zero matches |
| A dedicated `extractions/` folder exists specifically named "cinema-worldbuilder" (as opposed to the shared `joey-cinema` family) | UNCONFIRMED — verified absent | `ls extractions/ \| grep -iE "seedance\|higgsfield\|banana\|cinema\|worldbuild\|joey"` returned only `joey-cinema`, `joey-cinema-os`, `joey-cinema-v1/v2/v3`, `mark-kashef-banana-squad` — no separate CWB-only folder |

## What this ledger does NOT claim

This skill's locked prompt grammar (the five-mode framework, the FOV-degree ladder, the block order, the Capture Realism physics) is **not** asserted to be a verbatim transcript of Joey speaking — it is Joey's own authored production skill (downloaded as a `.zip` of Claude skill files per the companion doc), cross-checked against his public explanatory writing about that same skill version. Anywhere this ledger cites SKILL.md as the anchor, the claim is "this is what the skill's own locked rule says," which is itself Joey's shipped IP, not a third-party's summary of it.
