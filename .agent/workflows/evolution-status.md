---
description: Dashboard of all active and completed evolution loops
---

# Evolution Status

> This is a status/dashboard command. No skill loading required.

## When to Use
- Check the status of active evolution loops
- Review historical evolution results across components
- Identify which components have been evolved and which haven't
- Periodic system health check on self-evolution capability

## Execution

### Step 1 — Scan Evolution Store
1. Check for `evolution_store/` directory in the project
2. List all subdirectories (one per evolved component)
3. For each, read the latest iteration's `result.json`

### Step 2 — Build Dashboard

```
╔══════════════════════════════════════════════════════╗
║              EVOLUTION STATUS DASHBOARD              ║
╠══════════════════════════════════════════════════════╣
║ Component         │ Iterations │ Baseline → Best │ Δ ║
╠═══════════════════╪════════════╪═════════════════╪═══╣
║ [workflow name]   │ 12/20      │ 6.2 → 8.1      │+1.9║
║ [skill name]      │ 5/5 ✓     │ 7.0 → 7.8      │+0.8║
║ [prompt section]  │ 3/10       │ 5.5 → 6.9      │+1.4║
╚══════════════════════════════════════════════════════╝
```

### Step 3 — Assessment
1. **Active loops**: List components currently mid-evolution
2. **Completed loops**: List components that finished evolution
3. **Never evolved**: List high-value components that haven't been evolved yet
4. **Recommendation**: Which component should be evolved next (based on quality gate history)?

## Output
1. **Dashboard table** — all evolved components with scores
2. **Active loops** — in-progress evolutions with current iteration
3. **Recommendations** — next evolution priorities based on system data
