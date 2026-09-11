---
job: decision-packet
name: Decision packet (a choice that is his, on the board)
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Take a DECISION-shaped ask ("should I…", "which…", "allocate…") to one packet he can answer in a sentence: the options researched with receipts, one recommendation with the why, what happens if he does not answer. It lives on the board as a one-lane job so the packet shows on Homebase and in the session brief instead of vanishing in a chat reply. No build, no lanes beyond the one.

## Sub-jobs / lanes
- L1 Packet — research every option named (prices, limits, what he already pays for on disk: `.agent/*.json` trackers, `directives/<service>-usage-policy.md`, `MEMORY.md` cost rules); write ONE decision packet (`job_board.py packet add`); mark this lane blocked on his answer [parallel]

## Ask me first
- Q: none before the packet — the packet IS the question · look first: the ask itself names the options; budgets live in `.agent/*.json` and the usage policies

## Handles alone
Reading trackers and policies, web-checking prices and plan limits, the math, the recommendation.

## Comes back when
- The packet is written (that is the only come-back)
- A named option cannot be priced from any source — say so inside the packet, never guess

## Needs approval
Nothing — a decision packet spends nothing and sends nothing. Acting on his answer is a NEW job if it is job-shaped.

## Needs
The ask verbatim · `.agent/*.json` spend trackers · usage-policy directives · web access for current prices.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| a price or limit is unverifiable | label it UNCONFIRMED in the packet | never — the packet carries the label |
| the ask is really a job (several deliverables, sequence) | close this and `/job` it with a real recipe | in one line |
| his answer needs work done | open the follow-on job; this one closes as answered | never |

## Done means
One packet on the board (Choice · Irreversible? · Options + recommendation · If no answer) · every figure labelled VERIFIED / LIKELY / UNCONFIRMED · lane L1 blocked on his answer · after his answer: lane complete with the answer as evidence, job closed.

## Ratchet log
- none yet
