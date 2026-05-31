---
name: freshness-tax-enforcement
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: "Gemini \\d+\\.\\d+|Claude \\d(\\.\\d+)?|GPT-\\d|Opus \\d|Sonnet \\d|Haiku \\d|\\$\\d+(\\.\\d+)?/mo|\\$\\d+/month|\\$\\d+(\\.\\d+)? per (query|month|day)|as of [A-Z][a-z]+ 20\\d\\d|as of 20\\d\\d|released (last|this) (week|month|year)|(launched|released|shipped|rolled out)[^.]{0,40}20\\d\\d|(launched|released|shipped) (in )?[A-Z][a-z]+ 20\\d\\d|latest|newest|state-of-the-art|most advanced|current version|deprecated|early access|trusted testers"
  - field: transcript
    operator: not_contains
    pattern: "VERIFIED|grounding-pass|deep-research-gemini|WebFetch|WebSearch.*20\\d\\d|primary source|Sources:|verify.*before delivery|verify_proof_ledger|proof-claims|PROOF-LEDGER GATE: PASS|\\[VOC\\]|avatar_manifold_runner"
---

**Freshness Tax Triggered**: This session contains claims that are time/version-sensitive (model names, pricing, dates, or status words like "latest"/"current"/"state-of-the-art") but no verification evidence was detected. These are the EXACT claim categories that fail under the "confident hallucination" pattern (see feedback_factual-grounding-standard.md).

**Before ending this session, confirm one of:**

1. **Verified against primary source this session** — ran `/deep-research-gemini`, `/grounding-pass`, or fetched the official docs via WebFetch/WebSearch with a 2026 date. Name the source.
2. **Claims are tagged with confidence labels** — VERIFIED / LIKELY / UNCONFIRMED per `directives/verification-agent-protocol.md`.
3. **No factual claims made** — the session was pure creative/strategic output with no version/price/date assertions.
4. **Explicit acknowledgment to user** — you told the user these claims are unverified and why.

**If none of the above apply:** Do NOT deliver. Run verification now. Freshness-sensitive claims are the #1 source of confident hallucination failures in this system (Coachella 2026 fabrications, Gemini 2.5 vs 3.1 naming, Parallax Edition 02). Hook exists because protocols requiring memory keep failing. Full rationale: `directives/verification-agent-protocol.md` § Freshness Tax.

**To mark verified without re-running**: include the phrase "Sources:" followed by dated URLs in your final message, OR tag each factual claim with VERIFIED/LIKELY/UNCONFIRMED labels. Hook scans for these markers.
