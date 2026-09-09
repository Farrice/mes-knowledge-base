# Validation receipt

Run: September 6, 2026. Lane: `codex/dan-koe-video-system`. Source: MqjmPknAvuw. No paid API calls, subscriptions, dependencies, external sending or subagents.

| Boundary | Evidence | State |
|---|---|---|
| Original watch setup | Binaries present, keyless setup complete | PASS |
| Original watch URL | DNS failure; unrestricted retry entered token-generation failures | FAIL, recovered by alternative |
| Original watch local visual extraction | 14 scene frames from full media | PASS, sampled |
| Free adapter public URL | Captions and download exit 0; `acquisition.json` | PASS |
| Full source transcript | Native captions span 1.829–1881.474 sec; interval coverage 99.45%; no gap >30 sec; full text read | PASS, not an accuracy score |
| Visual review | 40 uniform + 14 scene images inspected; `frame-review.json` and ledger | PASS, sampled not frame-by-frame |
| Offline transcription | Integrated `watch_free.py` local-file path on 20.02-second source clip; ASR exit 0 and 3 frames | PASS on clip; full-length offline path untested |
| Free tool controls | `python3 execution/test_watch_free.py`: 9 tests pass including timeout, missing dependency, output preservation and missing-evidence rejection | PASS |
| Source integrity and connections | `python3 execution/verify_dan_koe_linkedin.py`: source ID, media checksum, coverage, frame records, links, prompts and bridges | PASS |
| Prompt format | New prompts 3/3 pass; full renaissance audit 4007/4007 pass | PASS, structural |
| Existing skill audit | `skill_auditor.py check --skill dan-koe-multipassionate-mastery`: 0/7 failures | PASS, structural |
| System contract | `verify_skill_system_contract.py` | PASS |
| Routing | Workflow search ranks new route first; command menu finds `/dan-koe-linkedin-system`, cold-bridge | PASS in lane |
| Prompt discovery | Canonical index builder 7576 entries; canonical pointer renderer applied only to Dan's skill, 29 v2 prompts | PASS, no other skill rewrites |
| Registries | Canonical indexes regenerated: Dan workflow count 6→9; command family lists new route | PASS |
| Behavior | Same factual input transformed with angle choice and additive card/caption; `behavior-proof.md` | PASS for applied demonstration |
| Anti-slop | Pre-draft source anchored; final caption classifier CLEAN, 0/10, no signals; judgment review found no invented personal story or result | PASS for draft review |
| Copy review | Model assessments: hook 7, punch 7, voice 7, tension 7, reader language 7, anchor 8, belief 7, proof 8, ending/action 7, prose 8, platform fit 7 | Draft judgment only; not independent scoring or buyer proof |
| Export guard | No unrequested written export formats | PASS |
| Blind comparison | `blind_pass.py prepare` found zero valid unseen corpus pieces; no invented PASS recorded | NOT READY |
| Independent cold start | Replay prompt prepared; no second agent/run used | UNTESTED |
| Chain finalize | Local receipt logged with blind-pass override and no Notion; conservative 7/10 yields MARGINAL under existing scoring logic | MARGINAL, not human acceptance |
| Publication / market | No posting, followers, qualified conversations or attributable revenue produced | UNTESTED / NO EVENT |

Structural audits are not a claim that the skill produces superior writing. The stronger proof here is the applied draft, and its next evaluator is Farrice. A future market test must measure qualified attention and operator time as well as raw impressions.

## Retrieval

Start with `.agent/workflows/dan-koe-linkedin-system.md` in this lane. Read the source-method reference and only the component needed. The downloaded full video is retained locally under `raw/video.mp4` and deliberately Git-ignored; captions, frame evidence and metadata are durable source files. Acquisition state stays CAPTURED_REVIEW_REQUIRED; separate review evidence records what the model actually inspected.

## Integration

Main had unrelated tracked changes before this run. Integration is subject to the standard clean-main lane guard. No global watch replacement or hot skill promotion is part of this build. See `integration-receipt.txt` for the actual merge/park result.
