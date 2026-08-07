# Skill Source Ledger

This is the hot, distilled routing ledger. The canonical readable ledger is `extractions/kyle-milligan-copywriting/source-ledger.md`; exact segment references and truth permissions live in `speaker-ledger.jsonl` under the same extraction directory.

## Truth Vocabulary

| Class | Permitted use | Forbidden use |
|---|---|---|
| `OBSERVED` | Method grounding, workflow instruction, diagnosis | Market result, voice imitation, unreviewed regulated claim |
| `SELF_REPORTED` | Source context with disclosure | Offer proof, role credential, market-performance claim |
| `ILLUSTRATIVE` | Technique example | Factual claim, testimonial, authority, regulated claim |
| `THIRD_PARTY` | Attribution context | Kyle-owned doctrine, offer proof, role credential |
| `INFERRED` | Operational synthesis with observed anchors | Source quote, new fact, performance claim |

## Workflow Anchor Rows

| Workflow | Machine rows | Human rows / time | Owner | Grounded mechanic |
|---|---|---|---|---|
| 5-3-1 | `SL-023` | `H-019`, 24:42–25:11 | Kyle | Five relevant reads, three claim/proof breakdowns, one primary swipe |
| Promise spine | `SL-009`, `SL-014`, `SL-015` | `H-007`, `H-011`, `H-012`, 10:03–17:25 | Kyle | Mechanism/durable-force/result or catalyst/pattern/exploitation above beats |
| Promise-level edit taxonomy | `SL-008` | `H-006`, 09:21–10:03 | Matthew | Separate idea, functional flow, and line language |
| Four Punches | `SL-022` | `H-018`, 22:30–23:43 | Kyle | Bounded language of known moves; not the four-beat opening |
| Four-beat opening | `SL-038`, `SL-047` | `H-030`, `H-037`, 51:35–52:13 and 66:41–67:04 | Kyle / co-authored recitation | Interrupt, consequential claim, credibility, demonstrated result |
| First-four gate | `SL-045` | `H-036`, 65:23–65:53 | Kyle | Early continuation questions; the adjacent contest count is self-reported in `SL-046` |
| Thumbtack continuity | `SL-051`, `SL-064` | `H-041`, `H-052`, 71:48–72:20 and 96:26–96:50 | Kyle / co-authored | One concept must carry through adjacent sentences |
| Proof texture | `SL-030`, `SL-037`, `SL-039`, `SL-057`, `SL-058` | `H-024`, `H-029`, `H-031`, `H-047`, `H-048` | Kyle | Replace prestige/adjectives with relevant comparative detail and evidence |
| Mumbo jumbo | `SL-048`, `SL-062` | `H-038`, `H-050`, 68:24–69:10 and 95:55–96:20 | Kyle / co-authored | Count and prune simultaneous undefined concepts |
| Negative space | `SL-003`, `SL-020`, `SL-068` | `H-002`, `H-016`, `H-055` | Kyle | Reject context-free rescue work; detect research breaks and absent moves |
| NESB restraint | `SL-013`, `SL-017` | `H-010`, `H-014`, 14:46–15:11 and 18:58–20:40 | Kyle | Emotional categories do not authorize adjective stuffing |
| Evidence-derived mechanism | `SL-018` | `H-013`, 17:36–18:41 | Matthew | Do not invent a mechanism backward from the desired claim |
| Compensation-copy label | `SL-050` | `H-040`, 71:32–71:47 | Matthew label; Kyle agrees with diagnosis | Do not attribute the label solely to Kyle |
| Claim/demo match | `SL-066` | `H-054`, 98:14–99:30 | Kyle-led, co-authored row | The next demonstration must prove the exact preceding claim |

## Self-Reported and Illustrative Locks

- `SL-002`, `SL-006`, `SL-029`, `SL-032`, `SL-036`, `SL-046`, `SL-069`, plus the self-reported half of `H-028`: context only.
- `SL-012`, `SL-027`, `SL-040`, `SL-059`, `SL-061`, `SL-067`: illustrative details only.
- `SL-026`: David Deutsch attribution context; not Kyle-owned doctrine.
- `SL-043`, `SL-053`, `SL-063`: visual confirmation only.

Run `verify_source_ledger.py` whenever this file, the canonical ledger, the schema, or captured source bytes change.
