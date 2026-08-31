---
date: 2026-07-29
session: harness-apex metabolism audit
name: orphan-sweep-severed-live-import
problem_class: harness / cleanup sweep / severed import
domain: harness
status: proven
problem_signature: "a cleanup or orphan sweep archives a file that IS imported; the import sits inside a bare try/except pass so nothing errors, and a downstream health or report artifact silently freezes with no alarm"
tags: [orphan-sweep, imports, health-metrics, classifier, archive, silent-failure]
---
# Solution Card — orphan sweep archived a live module because verdicts predated the scanner fix in the same commit

**Problem signature:** a cleanup/orphan sweep archives a file that IS imported; the import sits inside `try/except Exception: pass`, so nothing errors and a downstream artifact silently freezes. Symptom: a health/report artifact stops updating with no alarm.

**Instance (2026-07-28/29):** commit `10d0cdd54` archived `execution/session_ledger_report.py` as one of 47 orphans. It was the SOLE reader of the 4.7 MB `.agent/sessions/observe-log.jsonl`, imported at `health_metrics.py:165` inside a bare `except: pass`. `.agent/health/latest.json` lost its `session_ledger` key for a day; the ledger report froze at 07-28 06:24. Found by the harness-apex metabolism audit.

**Root cause (the interesting part):** the SAME commit both taught `wiring_audit.py` to see python imports AND executed the archive list. The orphan verdicts were computed by the old, import-blind scanner; the fix and the damage landed together. Not a scanner bug — a sequencing bug: **verdicts must be recomputed AFTER the scanner changes, before any action is taken on them.**

**Fix applied:**
1. `git mv` the module back; import + render verified; `session_ledger` key restored in latest.json.
2. `health_metrics.py` bare `pass` → records `session_ledger_error` in the metrics, so a severed consumer becomes a visible flag instead of silence.

**Rule going forward:** any batch action driven by a classifier (archive/demote/delete lists) re-runs the classifier in the SAME session after any classifier change, and acts on the fresh output only. Verdict lists are perishable.
