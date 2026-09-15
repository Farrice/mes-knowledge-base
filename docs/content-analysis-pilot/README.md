# Content analyst: tested source extraction and optional Gemini perception

**Current result:** the complete 02:45:08 Paddy Galloway interview was sent to
Gemini 3.8 Flash. Google completed the request; its response was recovered from
AI Studio after a local timeout. Independent checks found wrong timestamps and
unsupported rules. Keep captions and selective frame verification as the evidence
base. This test does not justify replacing the existing watch workflow.

One paid request; usage-derived estimate about $0.81; invoice unverified because
Google's token counters conflict. A $1.25 reservation remains against this job's
$10 cap. No retry, second inference, agentic navigation or recurring job ran.

[Full test and costs](../../extractions/paddy-galloway/youtube-masterclass/gemini-quality-review.md) ·
[Extraction](../../extractions/paddy-galloway/youtube-masterclass/youtube-masterclass-extraction.md) ·
[Worked production packet](../../extractions/paddy-galloway/youtube-masterclass/applied-production-packet.md)

## Use from Codex or Claude Code

Use `/video-creative-reference` in content analyst mode to discover references,
analyze taste, extract a lesson or create an original adaptation from available
evidence. It separates performance, taste, observed evidence and inference.
Unsupported URLs require an accessible source file or platform-specific retrieval;
there is no universal private-video access. A Gemini key is not permission to spend.

Use `/pg-creative-sprint` for a connected production packet. Focused decisions use
`/pg-title-lab`, `/pg-thumbnail-concepts`, `/pg-intro-rewrite` or the other commands
in the Paddy skill. These workflows reason over supplied evidence and never start
paid perception automatically. The original watch skill is preserved.

## Spending controls

The general `content_analysis_pilot.py` is still offline-only. Its preview and
simulation approval do not permit real API calls. The separate
`content_analysis_live_trial.py` is fixed to the approved Z2uoA3bhJT0 job and model.
Its current unresolved usage hold prevents additional dispatch. Neither tool
creates a recurring allowance or changes Google billing settings.

Both preserve liability on interrupted or uncertain attempts. Requests are hashed,
state is shared across lanes, locks prevent concurrent dispatch, and completed
requests reuse receipts. The fixed trial caps attempts and output, with no implicit
retry or model fallback. Tests prove local controls, not a universal provider-side
billing ceiling. Other programs using the same key are outside these controls.

## Offline example

```sh
python3 execution/content_analysis_pilot.py preview docs/content-analysis-pilot/example-request.json
python3 execution/content_analysis_pilot.py approve-simulation BATCH_HASH --hash BATCH_HASH --budget-usd 1.00 --note 'Offline simulation approved; no paid calls'
python3 execution/content_analysis_pilot.py simulate BATCH_HASH
python3 execution/content_analysis_pilot.py status BATCH_HASH
```

Use the actual preview hash. Shared simulation state lives in the main checkout at
`.agent/content-analysis-pilot/simulation.sqlite3`. Test stores are isolated; they
must never be used to evade real liability.

## Recovery and remaining limits

Do not treat a local timeout as remote cancellation. Preserve the original
request, inspect its existing provider log and recover completed work before
considering another request. Our full-video trial demonstrates that recovery path.
Its counters require independent billing reconciliation; the ledger remains on
hold. Do not delete it, release the reservation or change identifiers to retry.

Agentic video navigation remains untested because a defensible total internal
processing cap was not verified. No global plugin, autonomous watch replacement,
background discovery, posting or image-generation integration was installed.

[Original offline contract](CONTRACT.md) · [Approved trial contract](FULL-VIDEO-TRIAL-CONTRACT.md) ·
[Analyst behavior](../../skills/youtube-video-context-analysis/references/content-analyst-pilot.md)
