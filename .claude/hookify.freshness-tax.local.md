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

**Freshness Tax**: time/version-sensitive claims detected with no verification marker. Verify against a primary source or label VERIFIED/LIKELY/UNCONFIRMED before delivering — these claim classes are the system's #1 confident-hallucination source (scar: Parallax Ed. 02). Full protocol: `directives/verification-agent-protocol.md` § Freshness Tax.
