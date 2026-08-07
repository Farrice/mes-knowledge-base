# Source Ledger — Semantic Document Library OS

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 15). Ground truth for this skill is
NOT under `extractions/` at repo root — `ls extractions/ | grep -iE
"semantic|document|library"` returns nothing there. The real extraction
survives only inside the historical harvest copy:
`_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/`.
Confirmed present with `wc -c` before use (not assumed absent, not assumed
present).

## Primary Sources

| Source | Path | Size | Status | Basis |
|---|---|---:|---|---|
| Source video | "The Work Primitive: What Every AI Product Leader Gets Wrong" — Nate B. Jones, *AI News & Strategy Daily* channel, YouTube, 2026-05. `https://www.youtube.com/watch?v=b1fxYGPbHeo` | n/a | LIKELY | Title, channel, URL, and date confirmed via `extraction-brief.md` metadata (below). Video itself was not re-fetched/re-watched during this repair pass — the transcript file is the working proxy. |
| Transcript | `_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/transcript.txt` | 26,202 bytes | VERIFIED | Read in full during this repair. Every quote added to `genius.md` was checked character-for-character against this file. Caveat: the transcript reads as machine-generated (artifacts such as "llinters" for "linters" and "get history" for "git history" appear in it) — treat it as a faithful-but-imperfect capture of Jones's spoken words, not a publisher-certified transcript. |
| Extraction brief | `_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/extraction-brief.md` | 987 bytes | VERIFIED | Read in full. Confirms source video, URL, channel, and that this extraction deployed as `skills/semantic-document-library-os` plus `semantic_libraries/`. |

## Claim-by-Claim (genius.md additions)

| Claim / quote | Where it lands | Status | Basis |
|---|---|---|---|
| "But access only gets the agent into the work space. It doesn't make the work understandable." | Pattern 1 | VERIFIED | Verbatim in transcript.txt |
| "The future is software where the button is no longer the primitive. The primitive is the action behind it." | Pattern 2 | VERIFIED | Verbatim in transcript.txt |
| "Trust is not a switch." | Pattern 3, Anti-Pattern 1 | VERIFIED | Verbatim in transcript.txt |
| "We're talking about semantic meaning artifacts. They tell the agent what world it's operating in." | Pattern 4 | VERIFIED | Verbatim in transcript.txt |
| "can it build a durable work graph above the underlying apps?" | Pattern 5 | VERIFIED | Verbatim in transcript.txt |
| "one of those classic problem shapes is make a semantic meaning of work legible to agents today." | Pattern 6 | VERIFIED | Verbatim in transcript.txt |
| "Humans need clear interfaces. Agents need clear semantics. The best software will provide both." | Pattern 7 | VERIFIED | Verbatim in transcript.txt |
| "If you expose too little, generic agents will operate clumsily through the UI. If you expose too much, the product risks becoming back-end infrastructure for someone else's agentic interface." | Pattern 8 | VERIFIED | Verbatim in transcript.txt |
| "But the action is not really click save." | Anti-Pattern 2 | VERIFIED | Verbatim in transcript.txt |
| "guessing is not a strategy for high-consequence work." | Anti-Pattern 3 | VERIFIED | Verbatim in transcript.txt |
| "there were real production systems deleted as a result of exactly that issue" | Anti-Pattern 4 | VERIFIED | Verbatim in transcript.txt |
| "If it cannot tell the difference between issuing a refund from your chosen Shopify shop versus issuing a refund from your Stripe, you're going to have problems as well." | Anti-Pattern 5 | VERIFIED | Verbatim in transcript.txt |
| "SAP is locking off agents right now. They don't want agents to use their products." | Anti-Pattern 6 | VERIFIED | Verbatim in transcript.txt |
| "Do not sell this as documentation, better prompts, or an automation project." | Anti-Pattern 7 | VERIFIED | Verbatim in `skills/semantic-document-library-os/references/productized-service-blueprint.md` — internal delivery guidance, not a Jones quote |
| "The best libraries are organized by work primitives, not departments or file types." | Anti-Pattern 8 | VERIFIED | Verbatim in `skills/semantic-document-library-os/references/hidden-knowledge.md` — internal build guidance, not a Jones quote |
| "The human sees a calendar event and brings all of that context with them. The software seeds fields in a database, right?" | In His Own Words | VERIFIED | Verbatim in transcript.txt |
| "If there's a connector, use the connector. If there's a proper protocol, use the protocol. If the system exposes a typed object and a permissioned action, use that." | In His Own Words | VERIFIED | Verbatim in transcript.txt |
| "Do not ask only whether the agent can act. Ask whether the product knows what that action means. That is your key takeaway." | In His Own Words | VERIFIED | Verbatim in transcript.txt, final line of the video |
| "A refund, a reschedule, a payment authorization, a compliance exception, a meeting brief." | The Work Primitive section | VERIFIED | Verbatim in transcript.txt |
| "the loop is powerful because the work environment itself gives the agent semantic feedback." | Why Coding Agents Arrived First | VERIFIED | Verbatim in transcript.txt |
| "Agents should use the richest semantic interface available." | The Hierarchy Of Meaning | VERIFIED | Verbatim in transcript.txt |
| "does the system understand what kind of work is being done, who's allowed to do it, what could go wrong, and how the result is checked" | Source Thesis | VERIFIED | Verbatim in transcript.txt |

## Pre-Existing Skill Claims Reviewed (not newly added, flagged for the record)

| Claim | Location | Status | Basis |
|---|---|---|---|
| Commercial pricing tiers ($750-$1,500 / $3,000-$7,500 / $10,000-$25,000) | `references/productized-service-blueprint.md` | UNCONFIRMED | Internally authored pricing hypothesis. Not benchmarked against a specific closed client deal — no client-outcome evidence found in `extractions/` or the harvest copy. |
| "AI Operating Partner" positioning, offer ladder, sales-call narrative | `references/ai-operating-partner-story.md` | LIKELY | Internal productization synthesis consistent with the source thesis, not a Jones quote. Reasonable extrapolation, not verified against a real sale. |
| Proof-demo file reference `extractions/semantic-document-library-os/proof-demos/codex-session-kickoff-first-proof-demo.md` | `references/productized-service-blueprint.md` | UNCONFIRMED (broken path at repo root) | Confirmed present only under `_active/harness/codex-harvest-2026-06-11/extractions/semantic-document-library-os/proof-demos/codex-session-kickoff-first-proof-demo.md` (16,252 bytes). The path as written in the live skill file does not resolve from repo root. Flagged, not silently fixed — out of scope for this repair (additive-first boundary; the referencing file was already passing and untouched). |
| `semantic_libraries/antigravity/primitives/high-floor-operator-os.md`, `collaborative-steering-compass.md`, `references/no-lazy-path-gate.md`, `primitive-map.md` (Required Load Order in SKILL.md, Load section in `workflows/steering-compass.md`) | SKILL.md, steering-compass.md | VERIFIED | All four files confirmed present on disk at the cited paths. |

## Legend

VERIFIED = checked directly against a primary file during this repair pass. LIKELY = reasonably inferred from adjacent verified metadata but not independently re-fetched. UNCONFIRMED = claim exists in the skill but no corroborating source was found; treat as an open gap, not as fact.
