# Verification Receipt

## Artifact scope

- Source package: `extractions/video-context/1ilMGCxJBQY/`
- Primary judgment surface: `JUDGMENT-PACK.md`
- Live skill changes: none
- Global changes: none
- Subagents: none

## PASS evidence

| Check | Instrument | Result |
|---|---|---|
| Source-package completeness | `verify_video_context_source_package.py` | PASS |
| Transcript structure | Package verifier + JSON assertions | 989 timestamped segments; 13,856 clean words |
| Visual coverage | Frame count + manual inspection | 100 scene-aware frames present; all inspected |
| Evidence ledger | Package verifier + JSON assertions | 21 rows; 14 spoken rows; non-empty and valid JSON |
| Required extraction depth | Heading and section checks | 14 patterns, seven hidden mechanics, four-level 30-day method, 24-hour/7-day/30-day pathways, failure modes, transcendence |
| System packaging | File and contract inspection | Skill System Contract, candidate workflow, four born-v2 prompts, behavior proof, negative control, judgment card |
| Export boundary | `export_format_guard.py` | PASS; no unrequested HTML, DOCX, or PDF |
| Artifact metadata | `artifact_frontmatter_guard.py` | PASS; no visible metadata above H1 |
| Artifact surface | `artifact_surface_guard.py` | PASS |
| Prose review | `prose_classifier.py` | WARNING only: 2/10 primary pack, 3.5/10 mastery report; structural parallelism from the extraction format, no delivery block |
| Canonical skill-system contract | `verify_skill_system_contract.py` | PASS |

## Claim accounting

- Direct or recipe-level source evidence: 12 ledger rows.
- Visually verified source evidence: 5 ledger rows.
- Self-reported and externally unconfirmed claims: 2 ledger rows.
- Bounded inferences: 2 ledger rows.

## Negative controls

- The behavior proof rejects “make seven viral posts” as an authority strategy when category, audience, proof, and trust evidence are absent.
- The prompt tests refuse to call high reach with poor audience fit an authority win.
- Low-reach, high-buyer-signal content is not automatically killed.
- Unsupported high-stakes claims trigger a factual/claim-risk hold while safe positioning work continues.

## Broader verifier failures not caused by this package

1. `verify_operator_core_source_to_skill_system.py` fails because the global AGENTS surface lacks the exact sentence “real Codex subagents require explicit authorization.” The current task used zero subagents and made no global edits.
2. The archived `verify_behavior_changing_extraction_contract.py` resolves the repository root as `execution/`, so it reports canonical files as missing even though they exist at repository root.

These failures are recorded as harness drift. They were not repaired because the request authorized a source extraction and judgment package, not global or control-plane repair.

## Final proof state

**PACKAGE: PASS**  
**LIVE PROMOTION: NOT RUN; HUMAN JUDGMENT PENDING**  
**EXTERNAL CLAIM VALIDATION: NOT RUN**
