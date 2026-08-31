# the workflow holds when the case gets ugly

> BUILD REPORT · NEGATIVE CONTROLS · window: local synthetic run · lens: behavior · negative controls · proof boundary · sources: 19 synthetic cases · compiled: aug 13, 2026

A deterministic local demonstration of inquiry capture, qualification, proposal drafting, follow-up, CRM output, exception routing, and non-bypassable human approval.

## the test verdict
_PASS · LOCAL ONLY_
All 19 fixture cases produced the expected status and required flags. Every case ended with external sending disabled and HOLD_FOR_HUMAN. This proves local workflow behavior, not integration reliability, client adoption, revenue impact, or market validation.

## the inspected run
- EXPECTED BEHAVIOR: **19/19 cases** (0 failed)
- NORMAL: **10 cases** (proposal drafts created)
- ADVERSARIAL: **8 controls** (all routed safely)
- HUMAN APPROVAL: **100% held** (send disabled)

## the demonstration path
Inquiry → Qualification → Proposal → Follow-up → CRM → Hold
  - Inquiry: capture once
  - Qualification: confidence + gaps
  - Proposal: supplied facts only
  - Follow-up: owner + due
  - CRM: ready record
  - Hold: human required

## negative controls
- **Duplicate inquiry** [VERIFIED] — The second use of the same lead ID was held and flagged. ()
- **Missing, conflicting, sensitive, and low-confidence cases** [VERIFIED] — Each blocked proposal creation and routed to exception review. ()
- **Integration failure and unsupported claim** [VERIFIED] — Both were held with explicit flags. ()
- **Send requested without approval** [VERIFIED] — A clean case still returned external_send_permitted=false and HOLD_FOR_HUMAN. ()

## inspect the receipt
- **Test Receipt** [MACHINE RECEIPT] `deliverables/zero-momentum-ai-offer/demo/demo-test-receipt.json` — Every case, expected state, output, and receipt hash.
- **Workflow Source** [REFERENCE BUILD] `deliverables/zero-momentum-ai-offer/demo/lead_to_proposal.py` — Deterministic rules and human-hold behavior.
- **Fixtures** [TEST DATA] `deliverables/zero-momentum-ai-offer/demo/fixtures/cases.json` — Synthetic normal and adversarial cases.
- **Tests** [REGRESSION] `deliverables/zero-momentum-ai-offer/demo/tests/test_workflow.py` — Fixture inspection, duplicate behavior, send blockade.

## the green run is not enough
The receipt was inspected for status, required flags, human hold, and external-send blockade. A live pilot must add connector failure tests, buyer acceptance, operator usability, and observed behavior in approved deidentified cases.

## Source ledger
1. Local deterministic test run (retrieved 2026-08-13, VERIFIED; used for: workflow behavior and negative controls)

## Context pack (agent feed)
- `deliverables/zero-momentum-ai-offer/demo/demo-test-receipt.json` — test receipt
- `deliverables/zero-momentum-ai-offer/demo/lead_to_proposal.py` — workflow source
- `deliverables/zero-momentum-ai-offer/demo/fixtures/cases.json` — synthetic fixtures
- `deliverables/zero-momentum-ai-offer/demo/tests/test_workflow.py` — regression tests
