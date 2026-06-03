---
description: "Production weather market trading system extracted from alteregoeth-ai/weatherbot — airport station resolution matching eliminates 3-8F systematic error, multi-source forecast selection (HRRR/ECMWF/METAR) weighted by geography and time horizon, self-calibrating per-city sigma..."
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/prediction-market-weather-trading/SKILL.md`. Also load `skills/prediction-market-weather-trading/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/prediction-market-weather-trading/workflows/market-forecast-edge.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
