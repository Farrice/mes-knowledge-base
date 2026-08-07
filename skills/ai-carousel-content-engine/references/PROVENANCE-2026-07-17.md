# PROVENANCE — ai-carousel-content-engine repair (Wave 3 Lane 4 Batch 1, 2026-07-17)

Anchor → source file + exact location. Full claim-by-claim ledger with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md` (this output dir).

| Anchor used in repaired file | Where it lands | Source file + location |
|---|---|---|
| "I specifically didn't want to make this fully autonomous..." | genius.md — How to Use / Operating Principles / Anti-Patterns | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/_3SEUgRCXX0/video-context-ledger.md` rows 00:01:55.600–00:01:59.680 |
| "we say we want you to match the style exactly..." | genius.md — Operating Principles / Anti-Patterns / Verbatim Source Material | same file, rows 00:04:24.400–00:04:39.280 |
| "this whole process end to end can be automated..." | genius.md — How to Use / Anti-Patterns / Verbatim Source Material | same file, rows 00:06:26.479–00:06:40.400 |
| "What are the problems they're struggling with on a daily basis?..." | genius.md — Anti-Patterns / Verbatim Source Material | same file, rows 00:07:06.319–00:07:16.080 |
| "creating SEO optimized, go optimized articles is incredibly important..." | genius.md — Anti-Patterns | same file, rows 00:07:45.360–00:07:51.440 |
| "you are now an orchestrator of an entire marketing operation" | genius.md — Core Thesis | same file, rows 00:08:41.599–00:08:43.919 |
| "I'm going to try and get two to three references..." | genius.md — Operating Principles | same file, rows 00:03:19.599–00:03:44.400 |
| "check out the link in the description. We've got an entire school community" | genius.md — Anti-Patterns | same file, rows 00:08:31.840–00:08:37.680 |
| "it's reading our entire article, and it's going to turn it into a carousel..." | genius.md — Verbatim Source Material | same file, rows 00:01:45.680–00:01:51.600 |
| Video metadata (title, channel, publish date, URL, duration) | genius.md — multiple sections | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/_3SEUgRCXX0/analysis.md` lines 5-9 |
| "Long copy that cannot fit on a slide" failure condition | genius.md — Anti-Patterns (paragraph-text item) | `skills/ai-carousel-content-engine/references/quality-rubric.md` Failure Conditions section |
| "Do not claim a hidden prompt was recovered" | genius.md — Anti-Patterns (hidden-prompt item) | `skills/ai-carousel-content-engine/references/source-map.md` Evidence Rules section |
| Live-path discrepancy (`extractions/video-context/_3SEUgRCXX0/` referenced but absent at repo root) | references/source-ledger.md | Verified absent via `find . -iname "*3SEUgRCXX0*"` (repo root scope) — zero hits under `extractions/`; present under `_active/harness/codex-harvest-2026-06-11/extractions/...` (byte sizes recorded via `wc -c`) |
| Output Schema / Quality Gate content in all 7 workflow files | workflows/01-07 | Derived from the skill's own pre-existing `references/prompts-v2/*.md` files (already-passing house style: Output Contract / Output Skeleton / Quality Gate), condensed and made file-specific — no external source needed, these were already inside the skill |

## Absence Verification (per envelope rule 2)

- `extractions/` at repo root has zero entries matching `carousel`, `luke`, or `_3SEUgRCXX0` (checked via `grep -rl` and `find`) — confirmed absence is real, not unread.
- The video-context package the skill's own note points to is NOT absent overall — it exists at a different path (`_active/harness/codex-harvest-2026-06-11/...`), fully read, byte sizes recorded above. This distinction matters: the source is real and was used, only the note's stated path is stale.
