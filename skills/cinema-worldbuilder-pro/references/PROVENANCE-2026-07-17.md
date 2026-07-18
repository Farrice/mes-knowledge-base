# Provenance — cinema-worldbuilder-pro repair

Anchor → source file + location, for everything added in `genius.md`, `references/source-ledger.md`, and `workflows/*.md`.

| Anchor / claim | Source file | Location |
|---|---|---|
| "Seedance is a physics engine, not a mood board. It renders things it can see and count. Mood words evaporate." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 30 |
| Write-the-visible examples (mood→muscle, "fast"→km/h, "hazy"→%/meters, "massive"→stacked humans) | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 32–35 |
| "No style header at the top of the prompt. Style isn't a single object..." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 190 |
| "Seedance latches onto FOV in degrees as a snap value... Millimeters read as suggestion; degrees read as instruction." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 211 |
| "Never write a non-anchor value — 23° is not on the ladder, so use 18° or 29° instead." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 213 |
| FOV degree table (9 anchor steps, 180° through 8°) | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 215–225 |
| "Trust the reference for wardrobe... Wardrobe details visible in the reference are NOT re-described." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 472 (Universal Prompt Rule 20) |
| "State what happens. Do not state what shouldn't..." (Positive Phrasing, LOCKED) | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 50–52 |
| "Every named subject that appears in a Seedance scene gets its canonical reference tagged separately... No exceptions." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 100 |
| Session-opener character-gate question | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 106–108 |
| "For new scenes, confirmation is mandatory. Never assume runtime — ask." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 148 |
| Ten-block code-block order (Scene & Mood → ... → Camera Capture) | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 162–184 |
| Distributed-style aspect→home-block table | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 192–203 |
| Mode-Select Table (M1–M5 capture/lens/movement/diffusion/grade) | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 277–283 |
| M1/M2/M3/M4/M5 Camera Capture template lines | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 289–316 |
| Capture Realism four mechanics + no-humans/M2-gloss tuning notes | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 361–379 |
| "Default camera energy is handheld... Locked-off tripod is OPT-IN ONLY." | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 384–386 |
| Extreme-FOV multishot four-lock protocol | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 412–417 |
| Pressure fracture / impactless breaks protocol | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 419–423 |
| Universal Prompt Rules 1–22 (no platform names, age-blind, one Camera Capture line, etc.) | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 451–474 |
| Pre-Delivery Pass silent QA checklist | `skills/cinema-worldbuilder-pro/SKILL.md` | lines 478–501 |
| "Never blend speed inside a single continuous shot — one speed per beat, cut cleanly at the transition." | `skills/cinema-worldbuilder-pro/SKILL.md` | line 271 |
| Whip-pan 0.8s minimum-motion rule | `skills/cinema-worldbuilder-pro/SKILL.md` | line 264 |
| "The prompt box is not linear... It's a bell curve, and the job is finding the top of it." | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | line 64 |
| "Frame Map anchors screen position before identity ever enters." | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | line 68 |
| "FOV in degrees, not just millimeters... 47° (50mm) holds. 50mm drifts." | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | line 69 |
| "These encode my taste. Not yours. Fork them. Break them. Make them yours." | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | line 93 |
| "Hit rate scales with prep... The pipeline is what makes the prompt cheap." | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | line 91 |
| Companion doc harvested 2026-07-13 via Playwright, public Notion page | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | line 3 |
| Joey bio (filmmaker, "JOEY" channel, ~25k subs, Control/CTRL, Noisy Group, KY) | `extractions/joey-cinema/VISION.md` | line 7 |
| This skill shipped as `cinema-worldbuilder-pro-3.0` alongside `banana-pro-director-3.0` and `story-bible-builder` | `extractions/joey-cinema/notion-cinema-claude-skills-v3.md` | lines 19–26 |
| "Omni ≤10s rule" / "Seedance 4K native" — UNCONFIRMED as applying to this skill | `extractions/joey-cinema/VISION.md` (attribution) vs. `skills/cinema-worldbuilder-pro/SKILL.md` (absence) | VISION.md line 13; confirmed absent by full 525-line read of SKILL.md, 2026-07-17, this session |
| Transcript checked, zero CWB-specific matches | `extractions/joey-cinema/transcript.txt` | `grep -in "degree\|write the visible\|frame map\|bell curve\|element tag\|km/h\|physics engine"` → 0 results, run 2026-07-17, this session |
| No dedicated "cinema-worldbuilder"-only extraction folder exists | `extractions/` directory listing | `ls extractions/ \| grep -iE "seedance\|higgsfield\|banana\|cinema\|worldbuild\|joey"` → only `joey-cinema*` family, run 2026-07-17 |

All byte sizes for presence/absence and cross-reference claims recorded via `wc -c` — see `references/source-ledger.md` for the full byte-count table.
