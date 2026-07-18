# PROVENANCE — kallaway-social-commerce repair (Wave 3 Batch 2)

Anchor → source file + location. Full claim-by-claim table lives in
`references/source-ledger.md`; this file is the compact anchor index for the
adversarial verifier.

## Primary Source (located during this repair — not previously cited correctly)

- **File**: `_active/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/transcript.txt`
- **Metadata**: `_active/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/metadata.json`
- **Video**: Kallaway, *"The NEW Way to WIN on Social Media in 2026,"* YouTube,
  published 2026-04-29, https://www.youtube.com/watch?v=ImzoNTrgvFg, duration 24:14.
- **Read**: full 1,487-line timestamped transcript read start to finish for this repair.

## Files Confirmed NOT to Contain This Skill's Source Material (checked, not assumed)

Per envelope rule 2 ("a claim that sources are ABSENT is itself a provenance claim"),
these were opened and grepped, not skipped:

- `extractions/kallaway/transcript.txt` (34,072 bytes) — "illusion of novelty" storytelling content.
- `extractions/kallaway/internet-money-machine-transcript.txt` (24,657 bytes) — funnel/offer content.
- `extractions/kallaway/internet-money-machine-extraction.md` (12,864 bytes)
- `extractions/kallaway/word-mastery-extraction.md` (16,292 bytes)
- `extractions/kallaway/extraction-report.md` (6,971 bytes)
- `extractions/kallaway-content-system/transcript.txt` (43,221 bytes)
- `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` (398,725 bytes)
- `extractions/kallaway-content-system/extraction-report.md`, `integrity-patch.md`

All grepped for: `Manis|Instagram Shop[s]|TikTok Shop|peak taste|permissionless|64
billion|revenue per view|RPV|agentic commerce|dollar store` — zero matches in any file.

## Anchor Index (genius.md additions → source line/timestamp)

| Anchor in genius.md | Section | transcript.txt timestamp |
|---|---|---|
| Source citation block (top) | header blockquote | metadata.json (title/date/URL) |
| Model Calibration section | new H2, top of file | synthesized calibration guidance, cross-referenced against transcript quotes already cited elsewhere in this table (00:01:17, 00:05:33, 00:00:15) — not a new factual claim, a craft-texture description |
| Anti-pattern 1 (AI-as-automation) | new "Anti-Patterns" H2 | 00:01:17–00:01:30 |
| Anti-pattern 2 (AI doing the thinking) | new "Anti-Patterns" H2 | 00:05:33–00:05:38 |
| Anti-pattern 3 (brand-deal grind) | new "Anti-Patterns" H2 | 00:17:38–00:17:44 |
| Anti-pattern 4 (1.0-era assumptions) | new "Anti-Patterns" H2 | 00:08:51–00:09:00 |
| Anti-pattern 5 (hijacking attention) | new "Anti-Patterns" H2 | 00:19:20–00:19:25 |
| Anti-pattern 6 (fast cuts / Alex Garcia) | new "Anti-Patterns" H2 | 00:20:26–00:20:33 |

## Known Unresolved Item (flagged, not silently fixed)

`genius.md` (both the original and this repaired version, per additive-only repair
boundaries) still reads **"Manis"** for the Meta acquisition, in three places: Pattern 2
("Meta × Manis"), Hidden Knowledge #3 ("The Manis Signal"), and Signature Moves ("$2B
Manis acquisition"). The primary source names the company **"Manifold,"** not "Manis"
(transcript.txt @ 00:13:44–00:13:58). This error predates this repair — it also appears
in `_active/codex-harvest-2026-06-11/brain/e51c78e9-.../artifacts/kallaway-expansion-vision.md`,
the original extraction vision doc, meaning it was introduced at extraction time, not
during this pass. Recorded in `references/source-ledger.md` claim #12 as LIKELY (concept
and dollar figure verified, name incorrect). Not corrected in-place per the envelope's
"never delete or rewrite passing content" boundary — flagging for an explicit follow-up
pass rather than silently editing shipped content.
