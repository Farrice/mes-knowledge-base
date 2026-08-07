# Phases 4-7 — Routing Bindings, Inheritance Contract, First Deliverable, Register & Ledger

**Duration**: the closing ~20-30 minutes of the 1-2 hour target. Phase 6 is optional (default ON; skip with `--no-deliverable`).

## Required inputs

A registered domain with 5 approved ground-truth samples (Phase 3 complete).

## Steps

### Phase 4 — Routing bindings (propose-only)

Read the existing `BINDINGS` structure (`grep -A 5 "^BINDINGS" execution/routing_enforcer.py | head -20`), propose 1-3 new entries (signal phrases → mandatory workflow → anti-patterns for when NOT to use), and surface the diff. Do NOT auto-edit `execution/routing_enforcer.py` — it is shared infrastructure every other calibrated vertical also routes through, so an unreviewed edit here risks misrouting domains that have nothing to do with this bootstrap.

### Phase 5 — Per-project CLAUDE.md (inheritance contract)

Generate `projects/<slug>/CLAUDE.md` against the fixed 6-section template already proven at `_active/clients/andrea-dj/CLAUDE.md`, `_active/clients/jen-listings/CLAUDE.md`, and `_active/farrice-brand/CLAUDE.md`: inheritance declaration, one-paragraph brand identity (a pointer, never a duplicate of the brand bible), voice test, when-to-load-context table, override list, vertical-specific anti-patterns. Append a row to root CLAUDE.md's "Per-Client / Per-Project CLAUDE.md Inheritance" table.

### Phase 6 — First deliverable (optional, default ON)

Pick one output type from the domain's registered `output_types`, invoke the matching single-deliverable workflow with the fresh voice doc + ICP as anchored context, and run `chain_runner.finalize`. Expert Standard should land 8+; if not, the calibration package (not the deliverable) needs revision. Save to `projects/<slug>/deliverables/first/<output-type>-<date>.md`. Skip with `--no-deliverable` for infrastructure-only setups.

### Phase 7 — Register & ledger

Verify all artifacts exist (ICP, voice doc, CLAUDE.md, ≥5 samples, routing proposal, optional first deliverable), anchor everything via `anchor_memory.py anchor`, and emit the ledger:
```bash
python3 execution/orchestration_ledger.py emit \
    --session-id "verticalize-<slug>-$(date +%Y%m%d)" \
    --project "<slug>" --since "<verticalize_start_time>"
```

## Output Schema

- **Phase 4** — a diff/proposal (not a file write) of 1-3 `BINDINGS` entries, presented for manual user application.
- **Phase 5** — `projects/<slug>/CLAUDE.md` with all 6 required sections present, plus one appended row in root `CLAUDE.md`.
- **Phase 6 (if run)** — `projects/<slug>/deliverables/first/<output-type>-<date>.md` with a `chain_runner.finalize` score attached.
- **Phase 7** — anchor entries for every artifact above, plus a printed ledger with a "SUGGESTED NEXT MOVES" section.

## Quality Gate

Before declaring the vertical bootstrapped:
- [ ] Phase 4's routing proposal was surfaced as a diff, never auto-applied to `execution/routing_enforcer.py`
- [ ] The per-project `CLAUDE.md` points to `00-foundation/02-icp-master.md` and `03-voice-document.md` rather than pasting their content — per SKILL.md's Anti-pattern #4 ("Don't duplicate brand bibles in the per-project CLAUDE.md")
- [ ] If Phase 6 ran, the first deliverable's Expert Standard score is 8+ before the vertical is called calibrated; a sub-8 score means the ICP/voice package needs revision, not that Phase 6 gets re-run on the same inputs
- [ ] All artifacts from Phases 1-6 are anchored via `anchor_memory.py anchor <slug>` so a later autopilot session in this vertical picks up the calibration package automatically
- [ ] The ledger emit actually ran and printed a "SUGGESTED NEXT MOVES" section — a bootstrap that ends without the ledger leaves no record for future sessions to inherit from
