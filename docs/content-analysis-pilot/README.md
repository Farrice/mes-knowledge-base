# Your content analyst — local pilot

**Built:** a shared analyst workflow and tested offline spending controls.
**Not enabled:** Gemini video calls, paid uploads or automatic discovery.
Your confirmed build did not authorize API spending. Live allowance remains $0.

## Use it in Codex or Claude Code

“Use `/video-creative-reference` in content analyst mode. Help me [discover
references / understand my taste / extract lessons / create an original
adaptation]. Reuse available evidence; show a preview before any paid work.”

The same reference guides both harnesses. Existing evidence packages, transcripts,
screenshots and explicit taste notes can be analyzed now. Fresh Gemini video
perception remains a separate trial. No global plugin or watch install was changed.

The result is a short brief: source evidence, performance versus a relevant
baseline (or unknown), taste fit, the useful mechanism, one application and limits.
It will not label content a proven winner from a polished video alone.

## What the pilot proves

- Exact sources, question, model, processing and limits are bound to a batch hash.
- Even a small call requires an explicit simulation approval record.
- The shared ledger reserves simulated cost before a child starts.
- Duplicate/repeated requests reuse completed receipts; they don't dispatch again.
- Expiry, source changes and altered previews stop execution.
- A timeout, crash, missing usage or overrun stops the batch. Unknown charges stay
  reserved across restarts; completed results remain available.
- Calls and elapsed time are bounded; no automatic retries or provider fallback.
- A key or an enable-live environment variable cannot turn this into a paid run.

These tests establish local control behavior only. They do not establish real
video quality, API billing entitlement or a hard provider-side cost ceiling.
Other tools with the same API key are outside this pilot's boundary.

## Offline example (Codex handles these commands)

From the owning workspace checkout:

```sh
python3 execution/content_analysis_pilot.py preview docs/content-analysis-pilot/example-request.json
python3 execution/content_analysis_pilot.py approve-simulation BATCH_HASH --hash BATCH_HASH --budget-usd 1.00 --note 'Offline simulation approved; no paid calls'
python3 execution/content_analysis_pilot.py simulate BATCH_HASH
python3 execution/content_analysis_pilot.py status BATCH_HASH
```

`BATCH_HASH` is the actual preview's full hash. The simulated dollar allowance
is not API permission. Default simulation state is shared at the main checkout's
`.agent/content-analysis-pilot/simulation.sqlite3`; tests use isolated temp stores.
`--state-dir` is for isolated simulation tests only, never a way around liability.
The pilot has no live transport, reads no API keys and makes no network requests.

A preview uses operator-declared video duration and a dated static token estimate;
these are not probed or guaranteed costs. Agentic estimates explicitly carry
UNVERIFIED cost bounds. Unknown platforms return a retrieval/native-reader gap.

## Failure recovery

Run `status` and keep the receipt. A stopped batch cannot be reapproved or silently
retried. Unresolved reservations block new dispatches in that simulation store.
There is intentionally no automatic reset or refund path: reconciliation needs
independent usage evidence. A future live adapter must implement and test that
reviewed recovery path before running paid work. Never assume killing a local
process cancelled a remote request or its bill.

## Next quality gate

Separately approve one public-video trial and its maximum budget. Before calling
Google, verify billing, current API limits and enforceable usage bounds, then add
the live transport under those constraints. Test visual facts absent from the
captions, timestamp accuracy, and recorded input/output/thinking/tool usage.
If agentic execution lacks a defensible cap, keep it disabled and bring back the
tradeoff. Do not silently spend on a supposedly safe estimate.

[Contract](CONTRACT.md) ·
[Analyst workflow](../../skills/youtube-video-context-analysis/references/content-analyst-pilot.md)
