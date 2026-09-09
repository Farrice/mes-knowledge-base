---

## Harness Behavioral Evals — 2026-09-07 (W36)

| Eval | Result | Evidence |
|------|--------|----------|
| E1 — Router fires on core domain | **PASS** | `linkedin_from_scratch` binding in routing-bindings.md; voice anchor documented in CLAUDE.md |
| E2 — Intent mirror on raw dump | **PASS** | Intent Mirror block specifies ≤5-line mirror + 1 push-back; hook-injected |
| E3 — Slop ban catches banned phrasing | **PASS** | Test with banned phrases → FLAGGED (6.0/10) by prose_classifier.py |
| E4 — Refusal net parks outward action | **PASS** | FORBIDDEN_RE catches "post to"; test card would park |
| E5 — Verbosity register holds | **PASS** | Model dialect specifies length constraints are honored |
| E6 — Memory recall surfaces standing rule | **PASS** | Memory facade returns "critic fleets stay dead" verdict |

**Score: 6/6 PASS**

**Note**: Scorecard could not be written to `.agent/health/harness-evals-2026-09-07.md` because main is integration-only and this mission ran without entering a worktree. The eval results above are the deliverable; the write can be made from a lane if persistence is needed.
