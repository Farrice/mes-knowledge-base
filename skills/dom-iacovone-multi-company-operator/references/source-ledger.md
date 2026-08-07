# Source Ledger — dom-iacovone-multi-company-operator

Every source consulted during this repair, claim-by-claim, labeled VERIFIED / LIKELY / UNCONFIRMED. This supplements (does not replace) the already-passing `references/source-map.md`.

## Sources Consulted

| Source | Location | Sizes (wc -c) | Status |
|---|---|---|---|
| Extraction package (found — original SKILL.md/genius.md claimed absent) | `_active/harness/codex-harvest-2026-06-11/extractions/dom-iacovone/multi-company-operator/` | README.md 1823; chapter-map.md 2711; operator-principles.md 3217; examples-bank.md 2672; failure-modes.md 1999; timestamped-insight-ledger.md 4725; harness-application-notes.md 2170; README.metadata.json 230 | VERIFIED (files exist, read in full, non-empty) |
| Raw video transcript/evidence package | `extractions/video-context/TUdTU1pwoZ4/` | not found anywhere in this repo (searched `extractions/`, `_active/harness/codex-harvest-2026-06-11/extractions/`, `_archive/claude-export-2026-07-01.tar.gz` file listing) | UNCONFIRMED-ABSENT — genuinely absent, not merely unread. The extraction package's own README (line 5) and SKILL.md already flag this; this repair confirms it rather than re-asserting it blind. |
| `_archive/claude-export-2026-07-01.tar.gz` | repo root `_archive/` | checked via `tar -tzf` listing for "iacovone"/"dom-iacovone" paths — no match | UNCONFIRMED-ABSENT for this expert |

## Claim-by-Claim Labels (new content added in this repair)

| Claim | Label | Basis |
|---|---|---|
| Four blockquotes in genius.md "Source Voice" section | LIKELY (3 of 4) / VERIFIED (1 of 4) | Each is a verbatim sentence copied from the named extraction file/line — verified as verbatim against the file's own text, but the extraction is itself a paraphrase of Dom's spoken words (transcript unavailable), so the LIKELY label reflects paraphrase-of-paraphrase distance, not doubt about the extraction file's existence. The harness-application-notes.md line 5 quote is the extraction author's own framing statement (not a claim about Dom's speech), so it is labeled VERIFIED. |
| 10 Anti-Patterns in genius.md | VERIFIED | Directly paraphrased (with citation) from `failure-modes.md`'s "Failure Mode" column, a file that exists and was read in full. Timestamp citations cross-checked against `timestamped-insight-ledger.md` rows, also read in full. |
| Timestamps used throughout (e.g., 04:47, 22:17, 64:40, 74:10, 86:17, 49:55, 128:15) | VERIFIED | Copied directly from `timestamped-insight-ledger.md` rows, not invented. |
| "10,300 observed spoken transcript rows... 20 sampled video frames... OCR unavailable (0 rows)" | VERIFIED | Copied directly from `_active/harness/codex-harvest-2026-06-11/extractions/dom-iacovone/multi-company-operator/README.md` "Evidence Status" section. |
| Workflow Quality Gate criteria (all 6 files) | VERIFIED as internally consistent with source, not new external claims | Derived from the same `operator-principles.md` / `failure-modes.md` content already governing the workflow's `## Steps`/`## Gates` sections — no new factual claims about Dom or the source were introduced; these are process-design criteria for the workflow's own deliverable shape. |

## Rule Applied

Per ENVELOPE hard rule 2: before writing "no source exists," this repair verified with actual file reads (all 8 extraction files opened and read in full) and recorded sizes above. The raw transcript absence is a re-confirmation of a gap already flagged in the pre-existing SKILL.md/README.md, not a fresh unverified claim.
