# PROVENANCE — april-dunford-positioning repair

Anchor → source file + location, for the adversarial verifier. Every quote below was confirmed present verbatim in the cited file via direct `grep -c` / string search before being written into genius.md (not assumed, not paraphrased-then-cited).

| Anchor (genius.md location) | Source file | Verification method |
|---|---|---|
| AP-1: "brand positioning" / tagline pet peeve | `extractions/april-dunford/transcript-1-positioning.txt` | `grep -c "my personal pet peeve is when people talk about brand positioning"` → 1 match |
| AP-2: "biggest mistake is not deliberately positioning" | `extractions/april-dunford/transcript-1-positioning.txt` | `grep -c "biggest mistake is not deliberately positioning"` → 1 match |
| AP-3: premature category creation = "a disaster" | `extractions/april-dunford/transcript-1-positioning.txt` | `grep -c "companies that love the idea of category creation are attempting to create a category"` → 1 match |
| AP-4: hero's-journey arc rejected (no competitor slot) | `extractions/april-dunford/transcript-1-positioning.txt` | `grep -c "the problem with that storytelling arc is there's kind of no competitor in there"` → 1 match |
| AP-5: generic trend ≠ insight | `extractions/april-dunford/transcript-2-sales-pitch.txt` | `grep -c "look your missing out like the competitors"` for locating region + direct substring match on the trend quote → confirmed present |
| AP-6: investor-pitch/future framing misapplied to sales | `extractions/april-dunford/transcript-2-sales-pitch.txt` | Direct substring match on "sales pitch is all about right now" confirmed present |
| AP-7: FOMO backfires on indecisive buyers (Jolt Effect/Gong) | `extractions/april-dunford/transcript-2-sales-pitch.txt` | `grep -c "look your missing out like the competitors are all doing it"` → 1 match; Matt Dixon/Jolt Effect/Gong context confirmed in same passage |
| "How to Use This Skill" quote: "first 40% of your pitch should contain zero product mentions" | Pre-existing genius.md, Pattern 1 ("The Context-Before-Product Pattern") | Not re-derived from transcript this pass — carried forward from the existing (pre-repair) genius.md text, cited internally rather than re-anchored to a new transcript location |
| Video titles/URLs (vM_1G1LCotU, -VqmFI9vY7w) | `extractions/april-dunford/transcript-1-positioning.txt` line 2, `transcript-2-sales-pitch.txt` line 2 | Direct file header read (both files carry a `SOURCE:` line with the YouTube URL) |

## File sizes recorded (per envelope rule 2 — verify absence, don't assume it)

```
14683  extractions/april-dunford/extraction-report.md
70691  extractions/april-dunford/transcript.txt
70905  extractions/april-dunford/transcript-1-positioning.txt
98005  extractions/april-dunford/transcript-2-sales-pitch.txt
```
(via `find extractions/april-dunford -type f -exec wc -c {} \;`, run before any claim was made about source availability.)

## UNCONFIRMED items (named honestly, not fabricated)

- The three "Hall of Fame Exemplars" already in genius.md (Unseen Cost Pitch, Champion's Internal Sell, Feature Dump anti-exemplar) are constructed teaching illustrations from the prior extraction pass, not verbatim April Dunford quotes. No source file contains them. Left untouched (pre-existing, passing `verbatim_exemplars` on other grounds — the file has 35 separately-verified long inline quotes plus 1 blockquote) but flagged UNCONFIRMED in `references/source-ledger.md` rather than silently treated as sourced.
- No timestamp/timecode data exists in either transcript (checked, zero matches for `[HH:MM]` pattern) — anchors above cite file + search string, never a fabricated timecode.
