# Source Ledger — oren-taste-development

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 13). Ground truth = files under
`extractions/` matching Oren, checked by direct read/grep, plus verbatim
quotes already inside the skill files. Every claim below is labeled
VERIFIED (quote found verbatim in a source file), LIKELY (a real source
file exists and closely supports the claim, but it's an interpretive
synthesis rather than a word-for-word quote), or UNCONFIRMED (no locatable
source file after active search — never presented as fact, never anchored
as a citation).

## Sources consulted (file + size, `wc -c`)

| File | Bytes | Notes |
|---|---:|---|
| `extractions/oren-1person-ai-marketing/transcript.txt` | 33,026 | Raw source recording — "last summer to lock in" video. Primary source for the 4 new VERIFIED anti-pattern quotes. |
| `extractions/oren-1person-ai-marketing/mastery-extraction.md` | 56,878 | MES extraction report over the same transcript; corroborates and re-cites the same verbatim lines. |
| `extractions/oren/extraction-report-repositioning.md` | 21,509 | Repositioning-focused extraction report. Source of the "Hunt for Vision" synthesis (LIKELY item). |
| `extractions/oren/extraction-report.md` | 23,343 | Read in full; no taste-development-specific verbatim quotes found beyond what's already cited elsewhere in genius.md. |
| `extractions/oren/oren-systems-extraction-report.md` | 14,668 | Read in full; operational-systems focus, not taste-judgment. No new anti-pattern material used from here. |
| `extractions/oren/transcript.txt` | 29,376 | Read/grepped for "taste", "CEV", "composition/effectivity/vibes", "thrift" — zero hits. Not the taste-development source video. |
| `extractions/oren-identity-brand-os/blind-pass-candidate-driver-diagnostic.md` | 8,605 | Read for overlap check; belongs to `oren-identity`'s Five Identity Drivers system, not this skill. Not cited. |
| `extractions/oren-identity-brand-os/blind-pass-log.md` | 973 | Read for overlap check. Not cited. |
| `extractions/oren-john-identity-marketing/mastery-extraction.md` | 28,424 | Grepped for anti-pattern language; content belongs to the Five Identity Drivers skill (binding ruling in file line 5 explicitly reserves "archetypes" terminology for `oren-brand-archetypes`). Not cited here to avoid cross-skill content bleed. |
| `extractions/oren-john-identity-marketing/companion-stussy-art-direction.md` + `-transcript.md` | 10,968 / 27,863 | Grepped for "one thing," "displacement," "parasite," "vignette," "bell curve," "washed/torched" — zero hits. Does not back the existing "Patterns from claude.ai export" section (see below). |
| `extractions/oren-john-identity-marketing/companion-brand-archetypes.md` + `-transcript.md` | 12,104 / 31,331 | Same negative-search result as above. |
| `extractions/oren-john-identity-marketing/source-transcript.md`, `source-digest.md`, `vision.md`, `visual-context.md`, `enrichment-research.md`, `arsenal-map.md` | 27,062 / 16,169 / 6,970 / 10,053 / 16,208 / 11,170 | Skimmed for taste/CEV/art-direction-mechanics overlap; all belong to the Five Identity Drivers extraction, not this skill's source material. |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 | Listed (`tar -tzf`) and grepped by filename for "art direction," "moodboard," "creative director," "creative strategy" — zero matching entry names. Does not confirm the claimed source of the "Patterns from claude.ai export" section. |

## Claims and labels

### New Anti-Patterns section (added this pass)

1. **"Midbaseline" / anti-slop guardrail** — VERIFIED. Quote found verbatim
   in `extractions/oren-1person-ai-marketing/transcript.txt` (~char 8,480):
   *"We've seen this flood now of these AI creators all sound alike... it
   performs at this like midbaseline standard where it doesn't ever break
   out, but it fills up. It clutters everything with noise."*
2. **AI No-Go Zone for personal-brand voice** — VERIFIED. Quote found
   verbatim in the same transcript (~char 8,690): *"I don't think you
   should be using a lot of those tools for your personal brand."*
3. **Paste-and-pray vs. strategic framework** — VERIFIED. Quote found
   verbatim in the same transcript (~char 20,600): *"They need to do it
   with a strategic framework versus just pasting the idea in and asking
   for a version."*
4. **"Not looking foolish" review gate** — VERIFIED. Quote found verbatim
   in the same transcript (~char 21,300): *"tips and tricks for reviewing
   this and deploying this and not looking foolish."*
5. **Vision-decision deficit ("Hunt for Vision")** — LIKELY. The exact
   sentence *"Most brands fail not because of bad taste but because nobody
   decided that vision matters"* is present verbatim in
   `extractions/oren/extraction-report-repositioning.md` line 86, but that
   file is itself an interpretive extraction report synthesizing Oren's
   Charli XCX/Brat creative-team story — not a direct transcript quote from
   Oren. Labeled LIKELY, not VERIFIED, for that reason.

### Pre-existing genius.md content (audited, not modified this pass)

6. **Patterns 1–14 (Demystification Frame, CEV Critique Matrix, Thrift
   Store Taste Test, etc.), Hidden Knowledge (Four-Domain Canon,
   Label-Stripping Test), Hall of Fame Exemplars, Signature Moves, Quality
   Rubric** — UNCONFIRMED as to a locatable raw source file. Actively
   searched: every `extractions/oren*` directory (`grep -in` for "CEV",
   "composition.*effectivity", "thrift store", "demystif", "taste is") and
   a repo-wide `grep -rli` for the same terms outside the oren folders —
   no matching source transcript or report was found. This does not mean
   the content is false; it means no extraction file in the current repo
   backs it verbatim, so it cannot be cited as VERIFIED or LIKELY. Left
   in place (additive-first, no deletion of passing content) but flagged
   here honestly per the envelope's hard rule: an absence-of-source claim
   must itself be checked before being asserted, which is what the file
   list above documents.
7. **"Patterns from claude.ai export — Oren art-direction & creative-
   direction conversations (2026-07-01)"** (The One-Thing Rule, Six-
   Technique Toolkit, Displacement + Parasite Marketing, Customer Bell
   Curve, Vignette Formula, World Building, sensory/brand-object/archive
   insights) — UNCONFIRMED. The section cites "five unmined extraction
   conversations (Art Direction 101/201, 'A Creative's Guide to Great Art
   Direction,' 'Creative Director 101: Briefs & Techniques,' 'Mastering
   Moodboards,' Creative Strategy Playbook)." None of those titles, nor
   the specific terminology used in the patterns (checked: "one thing,"
   "displacement," "parasite," "vignette," "bell curve," "washed,"
   "torched"), appear in any file under `extractions/` or in a filename
   listing of `_archive/claude-export-2026-07-01.tar.gz`. Left in place
   (additive-first) but not usable as a citation source for any new claim
   until the raw conversations are located or re-extracted.
8. **Evolution Log entry (2026-04-09, Decision Pressure Architecture)** —
   LIKELY. This is a standard chain-finalize evolution-cycle record (score
   deltas, KEPT verdict), not an extraction claim about Oren himself; the
   format matches the system's own evolution-log convention used across
   skills. Not independently re-verified against `evolution_store/` this
   pass (out of scope for the two failing checks being repaired).

## What this repair pass did NOT do

- Did not delete or rewrite any passing content (additive-first).
- Did not import content from any other oren-* skill's reserved
  terminology (e.g., "archetypes," "Five Identity Drivers" stay with
  `oren-brand-archetypes` / `oren-identity`).
- Did not attempt to re-verify claims 6–8 beyond the search documented
  above — that is a larger project than the two failing heartbeat checks
  (`anti_patterns_sourced`, `source_ledger`) this pass targets.
