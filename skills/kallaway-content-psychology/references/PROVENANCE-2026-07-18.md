# PROVENANCE — kallaway-content-psychology repair (Wave 3 Lane 4 Batch 8)

Anchor → source file + location, verbatim-checked this pass.

| Anchor (genius.md, § Anti-Patterns) | Source file | Location |
|---|---|---|
| "Never blend multiple creators' voice profiles into one script" | `extractions/kallaway-content-system/transcript.txt` | lines 688-692 |
| "Don't copy another creator's tone once your own voice is dialed in" | `extractions/kallaway-content-system/transcript.txt` | lines 684-686 |
| "Never pay or trust a creator whose content is pure replication with no original take" | `extractions/kallaway-content-system/transcript.txt` | lines 426-428 |
| "Business owners should not personally edit their own content past the earliest stage" | `extractions/kallaway-content-system/transcript.txt` | lines 802-804 |
| "Don't make immature AI-editing tooling your only production pipeline" | `extractions/kallaway-content-system/transcript.txt` | lines 788-794 |
| "Never trust an off-the-shelf AI writing platform to produce a usable script untuned" | `extractions/kallaway-content-system/transcript.txt` | lines 646-648 |

All six quotes were retrieved by `grep -n` against the file above, then read in context (Read tool, offset windows) before being transcribed into genius.md — none were reconstructed from memory or paraphrase-then-quoted.

## Flagged, not fixed (out of scope for this repair)

Patterns 31-33 in genius.md (pre-existing, not modified) contain quotes ("the algorithm will nuke the video," "the BS detector," etc.) with no verbatim match in any `extractions/kallaway*` file on disk. These trace to SKILL.md's documented "v3 NotebookLM upgrade" (Notebook ID `30579fcb-089b-4c38-a56e-a53b5c437fa5`), a source this repair pass could not query. Recorded honestly in references/source-ledger.md as UNCONFIRMED-against-local-files rather than silently treated as verified or silently deleted.
