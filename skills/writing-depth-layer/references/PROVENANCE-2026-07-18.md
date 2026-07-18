# PROVENANCE — writing-depth-layer repair (Wave 3 Lane 4 Batch 18)

Anchor → source file + location table. Every anchor was confirmed by direct file read or `grep` before use; none is asserted from memory. See `skills/writing-depth-layer/references/source-ledger.md` (in this output tree) for the claim-by-claim VERIFIED/LIKELY/UNCONFIRMED table — this file is the flat anchor index.

| Anchor used in genius.md | Source file | Location | Verified how |
|---|---|---|---|
| "writer is actually more interested in the sentence than the content" | `extractions/anne-lamott-neal-allen-really-real/source.clean.txt` | line 56, timestamp `[00:02:46.080]` | `grep -n` + direct read |
| "Literary showing-off is contrasted with story and care." | `extractions/anne-lamott-neal-allen-really-real/evidence-ledger.md` | row `00:30:54-00:31:25` | direct read |
| "Clarity is a courtesy. Compression can be care, not coldness." | `extractions/anne-lamott-neal-allen-really-real/evidence-ledger.md` | row `00:24:06-00:26:13` | direct read |
| "The goal is not dumping emotion." | `extractions/anne-lamott-neal-allen-really-real/mechanics.md` | section 2, "Realness Is Not Rawness" | direct read |
| "A sentence is alive when it earns the next sentence." | `extractions/anne-lamott-neal-allen-really-real/evidence-ledger.md` / `mechanics.md` | row `00:02:07-00:03:27` / section 1 | direct read |
| "'Comprehensive' output = system failure regardless of score." | `CLAUDE.md` | line 50 | `grep -n` |
| 2026-06-14 02:19 finalize, composite 7.25, "Needs Improvement" | `knowledge/log.md` | line 188 | `grep -n` + direct read |
| "36 rules module" / "36-rules module" (Lamott-Allen technical-craft expansion) | `knowledge/log.md` | lines 186, 188 | direct read |
| "Diagnose before treating. Never refine on a misdiagnosed draft..." | `skills/writing-depth-layer/references/depth-deficit-taxonomy.md` | line 246 | `grep -n` |
| 13 owner-skill paths (Hawley, Roth, Connelly, Cole, Lamott-Allen, Lamott-craft, Fareed, Sutherland, Lara Acosta, Diandra Escobar, Kallaway, Pressfield, ghostwriting-voice-engine) | `skills/<name>/genius.md` | file existence | `test -f` loop, all 13 present |

## Provenance notes

- **No fabricated absence.** This skill has no dedicated `extractions/` folder of its own (`ls extractions/ | grep -i "depth\|writing"` returns unrelated hits: `comedy-writing`, `nicolas-cole-ghostwriting-v1/v2`, `writing-masters`). It is a composition layer over the craft roster, not a named-expert extraction, so its one directly-quoted source is the `anne-lamott-neal-allen-really-real` extraction it already composes (`skills/lamott-allen-really-real-writing`) — used above. This was established by directly reading the extraction folder contents, not inferred.
- **No archive tarball scan needed.** Local sources (`git log`, `knowledge/log.md`, `extractions/`) were sufficient for every anchor added; per the envelope's search discipline, `_archive/claude-export-2026-07-01.tar.gz` is only opened when local search comes up empty, which did not happen here.
- **One pre-existing near-miss flagged, not silently fixed.** SKILL.md line 31 and the original genius.md §1 quote Lamott + Allen as saying a writer "cares more about the sentence than the content" — the verbatim transcript actually reads "is actually more interested in the sentence than the content." This predates this repair and was not a failing check, so it was left untouched (additive-first boundary), but it is called out in `references/source-ledger.md` claim #12 (labeled LIKELY, not VERIFIED) so no adversarial reviewer mistakes it for a checked anchor.
