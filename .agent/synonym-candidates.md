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
