# Synonym Candidates

Human-review queue only. `evolution_orchestrator.run_routing_learning()`
(execution/evolution_orchestrator.py, Wave 3 2026-07) appends candidate
query-term -> skill pairs here, sourced from workflows that ran with zero
measured sub-agent spawns (`evolution_store/sub_agent_misses.jsonl`) — a
deterministic signal that a manual skill load happened without the router
having suggested it.

NEVER auto-applied to `execution/find_skill.py`'s `SYNONYMS` map. A human
reads the candidates below, decides whether the phrasing actually
generalizes (vs. being a one-off), and hand-adds it to `SYNONYMS` if so.

## 2026-07-08

- `extract-forge` -> `dara-denney-meta-ads` (manual load, 2026-07-07T20:36:03.973103)

## 2026-07-09

- `deep-research` -> `deep-research` (manual load, 2026-07-08T19:11:36.489154)

## 2026-07-16

- `extract-forge` -> `jeremy-haynes-cold-offer` (manual load, 2026-07-15T08:42:53.906934)
- `extract-forge` -> `tommy-clark-linkedin-growth` (manual load, 2026-07-15T09:24:55.413606)

## 2026-07-17

- `extract-forge` -> `jenny-hoyos-shorts` (manual load, 2026-07-16T11:24:56.930175)

## 2026-07-19

- `extract-forge` -> `creative-campaign-strategy` (manual load, 2026-07-19T00:26:44.944982)
- `extract-forge` -> `creative-campaign-strategy` (manual load, 2026-07-19T00:26:47.393078)

## 2026-07-21

- `extract-forge` -> `paolo-trivellato-lead-magnet-engine` (manual load, 2026-07-21T06:39:04.364096)

## 2026-07-26

- `extract-forge` -> `briar-cochran-content-science` (manual load, 2026-07-25T09:14:09.512247)
- `extract-forge` -> `dara-denney-meta-ads` (manual load, 2026-07-25T14:49:41.158504)
