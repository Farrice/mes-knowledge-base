# Provenance — sky-tan-format-engine repair (Wave 3 Lane 4 Batch 16)

All anchors below verified with `grep -qF` against the exact source file — byte-for-byte
substring match confirmed for every quote (see repair session log). Ground truth =
`extractions/Sky Tan/` (transcript.txt, mastery-extraction.md, verification-record.md,
video1-Q984AzK0nlo.txt, video2-GNAZIHf6YiQ.txt, video3-siCsb23nuZM.txt).

## genius.md — "How to Use This Skill (Model Calibration)" (new section)

| Anchor | Source |
|---|---|
| "Oh, hey, that's the stop start guy" | `extractions/Sky Tan/video3-siCsb23nuZM.txt` |
| "polished now reads as fake" reference | genius.md's own pre-existing Hidden Knowledge insight (unchanged, cross-referenced) |

## genius.md — Pattern entity fixes (named_entity_floor)

| Pattern | Quote added | Source file |
|---|---|---|
| The One Idea | "Formats gets you views, but it's the expertise that gets people to pay you" | video2-GNAZIHf6YiQ.txt |
| 3. Cross-Niche Format Theft + Twist | "You find a format that's already proven somewhere else. You bring it to your niche before anyone does and you go" | video3-siCsb23nuZM.txt |
| 4. The 20-Minute Strategy Spine | "a $1 million content strategy in less than 20 minutes" + "8 million followers" | video1-Q984AzK0nlo.txt |
| 8. Format-From-Your-Own-Process Engine | "script out five, 10, 15 videos in the span of like an hour, whereas it would take someone an hour to script out one script" | video3-siCsb23nuZM.txt |
| 10. Saturation Blitz as Copy-Proof Moat | "I spent the next couple days and recorded, scripted, edited six videos a day of the same format" | video3-siCsb23nuZM.txt |
| 12. Volume → Feedback → Evolution | "the more volume I did, the more feedback I would get" | video3-siCsb23nuZM.txt |

## genius.md — Anti-Patterns section (anti_patterns_sourced)

All 7 bullets now carry an anchor on the list-item line itself (date/quote/source), per the
batch's additional format rule. Anchors added:

| # | Item (abbreviated) | Anchor added |
|---|---|---|
| 1 | "30 content ideas" list | quote "average business owner hires a junior strategist..." — video3-siCsb23nuZM.txt |
| 2 | Format fails Conversion Gate | "50M views in 2 weeks" Adam figure (already-established in Pattern 2 above) + video2-GNAZIHf6YiQ.txt citation |
| 3 | Copying inside niche | quote "once you're copying someone inside your own niche, you're already too late" — video3-siCsb23nuZM.txt |
| 4 | Scripts before Purpose | quote "before I touch the formats, before I touch the scripts, before I touch the edits, is the purpose" — video1-Q984AzK0nlo.txt |
| 5 | Scaling before 2x test | quote "post four videos in the same format" — video3-siCsb23nuZM.txt |
| 6 | Over-polishing | quote "the shooting is like not the best. The editing isn't anything crazy" — video2-GNAZIHf6YiQ.txt |
| 7 | Inventing case studies | citation `extractions/Sky Tan/verification-record.md` (dated 2026-05-30 in-file) |

## Checks left untouched (already PASS — preserved, not re-verified beyond confirming pass persists)

- `verbatim_exemplars` — was already 9/min-3, now 22 (side-effect of added quotes).
- `source_ledger` — already passing via `references/prompts-v2/counter-position.md` carrying
  literal VERIFIED/LIKELY labels; no references/source-ledger.md was added since the check
  was not failing (additive-only, minimal-touch per envelope).
- `workflow_contracts` — all 12 workflow files already carried Output Schema + Quality Gate;
  untouched.

## Local re-run of execution/skill_auditor.py heartbeat_checks() against the repaired file

```
PASS anti_patterns_sourced - 7 source-attributed anti-pattern item(s) (of 7 found; need ≥5)
PASS verbatim_exemplars    - 1 blockquote + 21 long inline quotes = 22 (need ≥3)
PASS recognition_test      - found: "recognize this as"
PASS source_ledger         - found: counter-position.md (VERIFIED/LIKELY/UNCONFIRMED labels)
PASS named_entity_floor    - 24 pattern section(s), zero-entity ratio 0.00 (max 0.2)
PASS workflow_contracts    - all 12 workflow file(s) carry Output Schema + Quality Gate
```
(Run against a scratch copy at /tmp/sky-tan-check, not inside skills/ — deleted after verification.)
