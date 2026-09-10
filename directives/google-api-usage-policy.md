# Google AI API Usage Policy

**Status:** Active, fail-closed for paid research
**Ledger:** `.agent/gemini-api-usage.json`
**Research owner:** `/deep-research-os`

## Billing truth

- A consumer Gemini or Google AI subscription does not, by itself, prove that Gemini API calls have zero incremental cost.
- Google currently describes typical Deep Research Agent costs, not a hard per-request maximum. Estimates are planning inputs, not permission.
- A local ledger can prevent our own retries and duplicate accounting. It cannot cap a provider invoice.
- `incremental API cost: $0` may be recorded only for an imported consumer-subscription report or when the provider billing record proves zero incremental API cost.

## Default route

Codex-native research through `/deep-research-os --mode auto|codex-native` is the permanent default. It uses host web search/page reads, claim-level evidence, counterevidence, verification, and authority resolution without a provider API call.

Gemini is an explicit calibration challenger only:

- standard model only;
- one interaction maximum;
- no paid retry or automatic fallback;
- no Gemini Max in the parity bakeoff;
- never activated by generic research routing;
- billing path and provider hard ceiling must be machine verified before the call.

If the provider hard ceiling is unknown, the request is `BLOCKED_BEFORE_START`. User authorization and a local `$10` preference do not override that factual gap.

## $10 bakeoff invariant

| Boundary | Amount | Meaning |
|---|---:|---|
| Application authorization ceiling | $8.00 | Recorded plus pending provider exposure stops here. |
| Reporting-lag reserve | $2.00 | Never intentionally authorized; protects the absolute invariant. |
| Absolute ceiling | $10.00 | Must never be exceeded. |

Before a Gemini standard call, `execution/research_bakeoff.py` must confirm all of:

1. Mission explicitly permits `gemini` mode.
2. No prior Gemini reservation or interaction exists for the mission.
3. A machine-readable billing check confirms a provider-side hard ceiling.
4. The conservative reservation fits below $8 recorded plus pending exposure.
5. The shared `execution/cost_gate.py` approves the request.

Any unknown cost, missing billing state, duplicate interaction ID, retry, fallback, or automatic escalation hard-fails. A failed/invalid report after interaction start retains its full reserved exposure.

## Usage ledger

Each interaction is keyed by provider interaction ID. Replays may normalize a result but must not create another charge or duplicate ledger row. Historical duplicate rows are ignored in available-budget arithmetic and should be reported, not silently deleted.

Required receipt fields:

- model and interaction ID;
- started/completed timestamps;
- estimated and actual cost when known;
- billing-verification state;
- report/citation validity;
- stop reason;
- whether interaction started.

## Environment variables

| Variable | Purpose | Billing interpretation |
|---|---|---|
| `GOOGLE_AI_STUDIO_KEY` | Gemini Deep Research agent client | API billing is separate unless proven otherwise. |
| `GEMINI_API_KEY` | Other legacy Gemini SDK paths | Outside this parity contract; do not infer zero cost. |
| `GOOGLE_CLOUD_PROJECT` | Vertex/Cloud routing | Separate billing surface. |

Keys are not interchangeable. No credential proves a spending ceiling.

## Cost estimates

The runtime currently reserves $3 for one standard interaction because Google documents standard runs as typically about $1-$3. This is deliberately conservative but is still only an estimate. Gemini Max is excluded from the bakeoff.

## No silent fallback

When Gemini is unavailable, blocked, invalid, rate-limited, or over budget:

1. record the stop reason;
2. do not retry;
3. do not activate Perplexity, another provider, or Max;
4. continue only with the Codex-native candidate or imported subscription artifacts;
5. label the comparison partial.

## Activation record

The historical usage file contains a prior interaction and duplicate accounting rows. It is evidence that the client has run, not evidence of current billing coverage. The parity bakeoff starts with no new provider call until the hard-ceiling check passes.

*Corrected: 2026-08-17. Supersedes the unverified Ultra-coverage and prepaid-balance assumptions.*
