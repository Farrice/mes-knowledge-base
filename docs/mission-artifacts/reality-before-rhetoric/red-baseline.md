# Reality Before Rhetoric: Red Baseline

> **SUPERSEDED V1 TEST EVIDENCE.** This is the red baseline for the retired
> blanket-integration experiment, not a current implementation target. The
> active regression target is
> `execution/fixtures/reality_before_rhetoric/anti-shackle-regression-set.json`.

## Result

`EXPECTED FAIL — TESTS PRECEDE INTEGRATION`

Command:

```bash
python3 execution/verify_reality_before_rhetoric.py
```

The verifier failed before any live workflow was changed. It detected:

- the missing central primitive;
- missing Co-Creative Launchpad contract and runtime wiring;
- missing High-Taste Writing OS workflow and primitive wiring;
- missing Farrice Content OS handoff fields;
- missing Dhar source-acquisition route;
- the missing deterministic helper;
- the intentionally unfrozen accepted-behavior hash.

The fixture schema itself produced no failure: five required domains were present, each domain had exactly two fixtures, and both mechanical bypass controls were valid. Candidate accepted-behavior hash:

`20fd35a3dfb99c088d481649a71a73eecfef8afaec73cffb11e288d263ce6077`

This is the required red proof. A green result must close these exact gaps without changing the accepted behavior merely to satisfy the implementation.
