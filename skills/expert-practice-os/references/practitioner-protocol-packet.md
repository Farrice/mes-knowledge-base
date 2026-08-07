# Practitioner / Protocol Packet

Every path is required. Use `UNKNOWN`, `UNTESTED`, `NO_EVENT`, or `NO_PERMISSION` for an honest gap.

```json
{
  "schema_version": "1.0",
  "fixture_id": "...",
  "practitioner": {
    "identity": "...",
    "public_role": "...",
    "experience": ["..."],
    "credentials": ["..."],
    "scope": {"allowed": ["..."], "excluded": ["..."]},
    "repeated_results": ["..."],
    "evidence_provenance": "..."
  },
  "protocol": {
    "name": "...",
    "steps": ["..."],
    "dependencies": ["..."],
    "evidence": ["..."],
    "claims": {"allowed": ["..."], "restricted": ["..."], "unsupported": ["..."]}
  },
  "buyer": {
    "specific_buyer": "...",
    "observable_problem": "...",
    "present_state": "...",
    "desired_state": "...",
    "desired_feeling": "...",
    "outcome_limits": ["..."],
    "alternatives": ["..."],
    "failed_attempts": ["..."],
    "investment_conditions": ["..."],
    "disqualifiers": ["..."]
  },
  "offer": {
    "name": "...",
    "scope": ["..."],
    "format": "...",
    "price": "...",
    "price_status": "...",
    "terms_status": "...",
    "paid_event_gate": "..."
  },
  "proof": {
    "source": [],
    "practitioner": [],
    "demand": [],
    "delivery": [],
    "outcome": [],
    "repeatability": [],
    "permissions": {"measurement": "...", "quotation": "...", "anonymization": "...", "reuse": "..."}
  },
  "stage": {"proof_stage": "...", "requested_next_stage": "..."},
  "capacity": {
    "available_hours_per_week": 0,
    "working_weeks": 0,
    "delivery_hours_per_unit": 0,
    "support_hours_per_unit": 0,
    "concurrency": 0,
    "sales_call_limit": 0,
    "life_constraints": ["..."],
    "margin_floor": "..."
  },
  "acquisition": {"primary_path": "...", "secondary_paths": []},
  "actuals": {"sent": [], "held": [], "sold": [], "collected": [], "delivered_units": []},
  "economics": {
    "requested_model": "NONE",
    "revenue_target": "...",
    "owner_income_target": "...",
    "price": "...",
    "capacity": "...",
    "acquisition_actuals": "...",
    "retention": "...",
    "costs": "...",
    "margin": "...",
    "timeline": "..."
  },
  "authorization": {
    "requested_result": "...",
    "authorized_local_outputs": ["..."],
    "forbidden_external_actions": ["..."],
    "provenance": "ORCHESTRATOR_ATTESTED"
  }
}
```

Event arrays contain dated evidence objects. A count is derived from array length; it is never entered separately.
