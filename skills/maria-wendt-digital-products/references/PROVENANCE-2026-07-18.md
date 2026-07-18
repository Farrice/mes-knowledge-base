# Provenance — Maria Wendt: Digital Product Mastery (repair pass)

Anchor → source file + location. Full claim-by-claim reasoning in
`references/source-ledger.md`; this table is the quick-index.

| Anchor (genius.md section) | Source file | Location |
|---|---|---|
| "How to Use This Skill (Model Calibration)" — "boring and super clear" quote | `extractions/maria-wendt-2/transcript.txt` | Lesson 4 ("Clarity converts more than creativity... the stuff that actually sells is boring and super clear") |
| "How to Use This Skill" — "if someone lands on your page and has to think for more than 3 seconds" | `extractions/maria-wendt-2/transcript.txt` | Lesson 5 |
| Genius Pattern 1 (Research-First Kill Switch) formula | `extractions/maria-wendt/transcript.txt` | "Who struggles with what when trying to do something?" — problem-formula paragraph |
| Genius Pattern 4 (MVP in 60 minutes, "good enough is good enough") | `extractions/maria-wendt/transcript.txt` | "create your product in 60 minutes" section |
| Genius Pattern 8 (Find-One-Help-One script) | `extractions/maria-wendt/transcript.txt` | verbatim outreach script paragraph near end |
| Genius Pattern 9 (Identity Shift, $5-$10 pricing) | `extractions/maria-wendt/transcript.txt` | "$5 to $10... it's still a big identity shift that happens" |
| Genius Patterns 3, 6, 10 + most Hidden Knowledge bullets | `extractions/maria-wendt-2/transcript.txt` | Numbered lessons 1-36 (pre-selling = lesson 2; pricing-as-positioning = lesson 6; product ladder = lesson 29; embarrassment threshold = lesson 35, etc.) |
| Genius Patterns 11-16 + "Hidden Knowledge (export layer)" | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/838c2c5d-e657-42a6-a4e2-a9bebc878923.md` (and `5fb4d480-...md`) | "17-Second Strategic Pause" listed explicitly as a Claude-generated "Hidden Virtuoso Pattern," not a Wendt quote — **UNCONFIRMED**, caveat added in genius.md above that section |
| "student Brooke... a million dollars" / "$13 million" | `_archive/claude-export-2026-07-01.tar.gz` → `838c2c5d-...md` | Merlin AI transcript attachment, opening lines — **LIKELY** (real transcript, not re-verified against a second source) |

## Method note (per ENVELOPE source-search discipline)
- Searched `extractions/` for the name fragment `wendt` (no punctuation) via `ls | grep -i`.
- Read both matching transcript files in full (11,751 + 12,443 bytes, confirmed with `wc -c`).
- Because genius.md cited a "claude.ai export — Maria $600K/month System" not present in
  `extractions/`, searched the repo for a matching archive (`_archive/claude-export-2026-07-01.tar.gz`)
  and scanned it with `python3 tarfile` (never `tar -x` on 7,720 members) for the fragment
  `wendt`, then narrowed by distinctive co-occurring keywords before opening candidate
  files directly to check exact wording.
- The "no source found" conclusion for the export-layer figures is not a blind assertion —
  the source *was* found, read, and shown to be a prior AI's own generated content, which
  is why the label is UNCONFIRMED (fabricated-adjacent precision) rather than "absent."
