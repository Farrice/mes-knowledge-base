# Source Ledger — YouTube Video Context Analysis

This skill is a system pipeline (the `/watch` + `execution/fetch-video-context.py` video-vision stack), not a named-expert extraction. Ground truth is the pipeline's own code, directives, and archive conversations that used it — no external "expert transcript" exists to extract from. Every claim added or upgraded during this repair is labeled below.

## Sources Consulted

| # | Source | Type | Status |
|---|---|---|---|
| 1 | `execution/fetch-video-context.py` (module docstring, `KNOWN_VIDEO_HOSTS`, `DEFAULT_MAX_DURATION_SEC`) | Code, read directly | VERIFIED |
| 2 | `execution/video_context_ledger.py` | Code (file existence + mtime only, not read line-by-line) | VERIFIED |
| 3 | `execution/verify_video_context_source_package.py` | Code (file existence + mtime only) | VERIFIED |
| 4 | `directives/video-vision-protocol.md` | Directive, read in full | VERIFIED |
| 5 | `directives/routing-bindings.md` (video source binding row) | Directive, grepped + read in context | VERIFIED |
| 6 | `directives/cli-reference.md` (fetch-video-context.py invocation line) | Directive, grepped + read in context | VERIFIED |
| 7 | `skills/youtube-video-context-analysis/references/prompts-v2/*.md` (all 8 files) | In-skill born-v2 prompts, read in full | VERIFIED |
| 8 | `_active/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md` | Archive conversation deliverable, read in full | VERIFIED |
| 9 | `_active/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/may-june-extraction-integrity-ledger.md` | Archive conversation deliverable, read (header + relevant rows) | VERIFIED |
| 10 | `_active/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/INDEX.md` | Archive conversation index, read in full | VERIFIED |
| 11 | `_active/codex-harvest-2026-06-11/skills/youtube-video-context-analysis/SKILL.md` (prior fork copy) | Archive copy, grepped for the row-shaped-ledger line | VERIFIED |
| 12 | `execution/skill_auditor.py` (heartbeat check implementations) | Code, read to confirm exact pass conditions before writing fixes | VERIFIED |

## Claim-by-Claim

| Claim (as used in genius.md / workflows) | Source | Label |
|---|---|---|
| "~30-50% of meaning in modern video ... lives in the visual channel" | `directives/video-vision-protocol.md`, "Purpose" section, line 7 | VERIFIED — verbatim, minor markdown-bold stripped |
| `DEFAULT_MAX_DURATION_SEC = 600` / 10-minute skip cap | `execution/fetch-video-context.py`, line 49 | VERIFIED — verbatim constant |
| "Gives every extraction workflow access to visual frames + Whisper-grade transcripts without depending on the AI assistant remembering to invoke the `/watch` slash command" | `execution/fetch-video-context.py`, docstring lines 3-7 | VERIFIED — verbatim, line-unwrapped |
| Banned pattern dated 2026-05-03 (manual-invocation dependency) | `execution/fetch-video-context.py` docstring cites `feedback_ai-memory-dependent-observability.md`; corroborated in `directives/video-vision-protocol.md` line 9 | VERIFIED — the memory file itself was not opened this session; the citation is corroborated by two independent files that both name the same date and reason |
| 18 entries in `KNOWN_VIDEO_HOSTS` | `execution/fetch-video-context.py`, lines 61-70 | VERIFIED — hand-counted from the tuple literal |
| "collapsing 'the speaker probably showed X' into an observed visual row" | `references/prompts-v2/full-visual-context-ledger.md`, line 43 | VERIFIED — verbatim |
| "treating thumbnails, titles, or video descriptions as proof of in-video evidence" | `references/prompts-v2/frame-ledger.md`, line 29 | VERIFIED — verbatim |
| "YouTube captions were preserved as row-shaped ledger evidence but not reconstructed into a clean transcript surface" | `_active/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md`, line 7 | VERIFIED — verbatim |
| Repair landed ~2026-06-30 | `execution/video_context_ledger.py` and `execution/verify_video_context_source_package.py` filesystem mtimes (`Jun 30`) | LIKELY — inferred from mtime, not an explicit changelog entry; the causal link to "the Meg repair" is corroborated by `INDEX.md` naming the Meg Heckman deployment as the trigger, but no commit message was found tying the exact date |
| `extractions/video-context/Zc4E_K48v48` (attention-hijack-hooks) quarantined "quarantine from arsenal" | `may-june-extraction-integrity-ledger.md`, row for `Zc4E_K48v48`, audit window 2026-05-01 to 2026-06-11 | VERIFIED — verbatim row content |
| Governor over-triage risk (video source → conceptual template instead of preserving source mechanics) | `EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md`, "Audit Goals" section | VERIFIED as an audit *question posed*, not a confirmed incident — genius.md phrases it as "named as an open audit risk," never as a settled failure, to avoid overclaiming |
| "Claims that the system saw visuals" (Failure Conditions) | `skills/youtube-video-context-analysis/references/quality-rubric.md`, "Failure Conditions" | VERIFIED — verbatim (quoted fragment of the first bullet) |
| `git log` history for `skills/youtube-video-context-analysis` (2 commits, both bulk-wiring commits, no per-skill narrative) | `git log --oneline --all -- skills/youtube-video-context-analysis` | VERIFIED — checked, contains no additional per-incident detail beyond what's cited above |

## Explicitly Not Claimed

- No named human expert, interview, or transcript exists for this skill — it is a deterministic tooling pipeline. Any anti-pattern framed as "X's approach" would be UNCONFIRMED and was avoided entirely.
- The exact commit or PR that fixed the "row-shaped ledger" failure was not located in `git log` (the two commits touching this skill's path are both later bulk-wiring commits unrelated to that specific fix); the 2026-06-30 date is an mtime inference, labeled LIKELY above, not asserted as VERIFIED fact.
- `execution/video_context_ledger.py` and `execution/verify_video_context_source_package.py` were confirmed to exist and were spot-checked for their role (via `directives/video-vision-protocol.md` cross-references and `EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md`'s "Primary verifier" line) but were not read end-to-end this session — no line-specific quote is attributed to them.
