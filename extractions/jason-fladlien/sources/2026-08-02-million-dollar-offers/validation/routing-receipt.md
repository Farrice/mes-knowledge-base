# Offer TERMS — Routing Receipt

## Direct Command Resolution

`python3 execution/command_menu.py show fladlien-terms` resolved:

- Workflow: `.agent/workflows/fladlien-terms.md`
- Source command: `.claude/commands/fladlien-terms.md`
- Execution status: `workflow-with-source`
- Domain: offers

## Natural-Language Routing

`python3 execution/workflow_router.py search "diagnose the time effort routine money and status burden in this offer before writing copy"`

- Rank 1: `/fladlien-terms`

`python3 execution/workflow_router.py search "this offer is valuable but buyers have too much work and do not adopt it"`

- Rank 1: `/fladlien-terms`

## Explicit Preflight

`python3 execution/codex_operator_preflight.py "use Jason Fladlien TERMS to rebuild this offer before copy or acquisition" --plain`

- Chosen entry point: `/fladlien-terms`.
- Runtime function owner loaded by that wrapper: `/revenue-offer-agent`.

The routing enforcer returned `valid: true`, but also returned `binding_matched: null` and `mandatory_workflow: null`. The same request can validate against an alternative workflow, so this result is permissive compatibility evidence, not ownership or exclusivity proof. No enforcement claim is made from it.

## Ownership Boundary

`/revenue-offer-agent` remains the function owner. `/fladlien-terms` is the one public TERMS front door and now loads the Revenue Offer Agent before delegation. Diagnostic and internal-component outputs are recommendations; the Revenue Offer Agent performs the separate accept, offset, reject, or hold reassembly. `offer-adoption-and-proof-loop` is an internal, named menu exemption and has no public command.

## Proof Boundary

- Direct command resolution proves the public command is installed.
- Natural-language ranking proves the intended query surfaces the public entry point first for the tested wording.
- Wrapper inspection proves the declared owner is present in the call path.
- No mandatory routing binding exists; exclusivity is not claimed.
