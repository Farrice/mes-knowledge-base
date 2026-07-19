# Mission Card — Source re-acquisition filing pass (archive → extractions/)
Tier: T1
Produced: 2026-07-18 (queued by Fable conductor, Farrice-directed maiden run)

## Objective
Repo-local recovery work, DRAFTS ONLY. Two items from the source re-acquisition queue:
1. tess-barclay: the REAL primary transcript for her 2025-11-28 video lives at
   `claude-export/normalized/conversations/6c48787f-c4f5-4654-9625-e93a6ee8a882.md`
   inside `_archive/claude-export-2026-07-01.tar.gz` (python tarfile extract). File it to
   `extractions/tess-barclay/transcript-2025-11-28-casual-content.txt` with a
   PROVENANCE header (member name, byte size via wc -c). Do NOT delete or overwrite the
   existing mismatched `transcript.txt` — add a README note explaining both files.
2. tom-noske: file the two masterclass transcripts (members 934a03af-…, e423b3d3-…, both
   ~90KB) to `extractions/tom-noske/` with the same provenance-header pattern.
Log both recoveries at the END of `.agent/mission-queue/done/source-reacq-log.md` with
byte sizes. Every quote/size claim must come from files you actually read.

## Constraints
- Additive only: never delete, overwrite, or rewrite any existing file.
- Three-location rule applies to any absence claim (directives/worker-envelope-standard.md).
- No web access needed; no external calls.
