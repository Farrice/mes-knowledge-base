---
job: replace-paid-tool-local
name: Replace a paid AI tool with a local build
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Turn a subscription he is paying for (Poppy.ai, a $200/mo tool, anything with a UI he likes) into a local surface on the harness that does the part he actually uses, on his existing plans and seats, with the cancel decision backed by a side-by-side proof — not a clone of the whole product.

## Sub-jobs / lanes
- L1 What he actually uses — the three moves he does in the tool weekly, in his words; the feel he wants kept; the price he pays [parallel]
- L2 Product teardown — web-check what the tool really is under the hood (team, engine, what is pass-through model cost vs real IP; e.g. Poppy = transcript fetch + graph walk + pass-through model), pricing today, what is rented (scrapers, APIs) [parallel]
- L3 Arsenal — `python3 execution/arsenal.py "<the three moves>"`; what the repo already has (2026-09-10 scar: Poppy was 65% built before the job opened — pulse_serve, ingest, brain_graph, `claude -p` seat) [parallel]
- L4 Seat + cost plan — which model seats run it (Claude via `claude -p` on the plan, never the API from Python; Gemini metered; GPT via `codex exec` if the CLI allows) with the running cost shown in the UI [after: L1, L2, L3]
- L5 Build v1 on the existing surface — extend `pulse_serve.py` / Homebase, one page, no build step, boards as gitignored user data; the one feature that earns the cancel [after: L4]
- L6 Side by side proof — the same task in the paid tool and in v1, screenshots, time, cost; his felt verdict [after: L5]
- L7 Cancel packet + v1.5 list — the cancel decision as a packet with the proof; the next two features ranked by what he'd miss most [after: L6]

## Ask me first
- Q: What are the three things you actually do in the tool each week? · look first: memory (`project_canvas-poppy-local`, `project_homebase-command-center`), `.agent/handoffs/` threads naming the tool
- Q: What feel must survive (the node board, the chat-reads-everything, the speed)? · look first: the same memory; his verbatim in thought-bank
- Q: Which seat may it run on — Claude plan only, or Gemini/GPT metered too? · look first: `directives/model-notes.md`, `directives/*-usage-policy.md`

## Handles alone
Teardown research, arsenal check, seat wiring on existing plans, the page, ingestion, caching, cost display, the side-by-side run, screenshots, the ranked v1.5 list.

## Comes back when
- The tool's core is a rented service we cannot replace for free (scraper, proprietary data) — packet: pay for that piece / drop the feature / accept a weaker version
- v1 needs a metered seat to feel right (cost packet before wiring)
- The felt verdict on the side-by-side (his, always)
- The cancel itself

## Needs approval
Any paid API or subscription · upgrading a CLI he pins (e.g. codex) · cancelling the paid tool · publishing anything.

## Needs
The tool's name and what he pays · Homebase running (`pulse_serve.py`) · the seats' auth (claude login, gemini key) · a lane worktree.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| a seat's CLI rejects the model (scar: codex 0.144.3 rejects gpt-6-astra) | ship v1 with the seats that work; list the blocked seat in the packet | he wants that seat on day one |
| ingestion blocked (login-gated source) | Playwright per `directives/browser-automation-safety.md`, cache what works | all routes fail |
| `claude -p --bare` breaks keychain login | never `--bare`; scratch cwd `~/.cache/antigravity-canvas` | never |
| the feel isn't there on the side-by-side | one iteration on the named gap, then packet | second miss |
| the repo already has a surface for it | extend it (`/canvas`, Homebase), never a parallel board | never |

## Done means
v1 reachable at a local URL · the three moves work end-to-end with cost shown · side-by-side proof file with his verdict · cancel packet answered · memory note with seats, gotchas, and the v1.5 list.

## Ratchet log
- none yet
