# Test Architecture — Genius Patterns

> Deep knowledge that separates a linter from a test architect.

## Pattern 1: The Page Object Maturity Model

Not all POM implementations are equal. There's a progression:

**Level 0 — No POM**: Selectors inline in every test
**Level 1 — Selector Constants**: Selectors extracted to a file, but actions still inline
**Level 2 — Action Methods**: Page objects with methods like `fillClaimForm()`, `submitClaim()`
**Level 3 — Business Operations**: Page objects that express business language: `claimsPage.fileNewClaim(claimData)` — the test reads like a user story
**Level 4 — Composable Flows**: Page objects compose into workflows: `await claimFlow.createAndSubmit(data)` with built-in waits, assertions, and error handling

Most teams plateau at Level 1-2. Level 3 is where tests become documentation. Level 4 is where tests become reusable building blocks.

**Application**: Don't just check "does a POM exist?" — evaluate its maturity level and recommend the next step, not the final destination.

## Pattern 2: The Fixture Hierarchy

Playwright fixtures have a natural hierarchy that mirrors test needs:

```
Global Setup          → Database seeding, service health checks
Worker Fixtures       → Shared browser context, authenticated session
Test Fixtures         → Per-test data, fresh page state
Inline Setup          → Test-specific overrides
```

Each level has different lifecycle, isolation, and performance characteristics. The mistake most teams make is putting everything at the test level (slow) or the global level (shared state = flaky).

**Application**: Evaluate whether the fixture hierarchy matches the data lifecycle. Auth tokens should be worker-level (shared, refreshed per worker). Test data should be test-level (isolated, cleaned up). Database state should be global setup (once).

## Pattern 3: The Isolation Spectrum

True isolation is a spectrum, not binary:

**Full isolation**: Each test creates all data, runs independently, cleans up after itself. Slowest, most reliable.
**Shared read-only**: Tests share reference data they only read. Fast, reliable if discipline holds.
**Shared mutable**: Tests share data they can modify. Fast, extremely fragile.
**Sequential dependency**: Test B needs Test A's output. Not really separate tests.

The right level depends on execution speed requirements, team discipline, and data setup cost. But you should always know WHERE on the spectrum you are and WHY.

**Application**: Don't just flag "shared state." Identify what KIND of sharing is happening and whether it's deliberate (shared read-only for speed) or accidental (leftover data from a previous test).

## Pattern 4: The Abstraction Goldilocks Zone

Over-abstraction in tests is as dangerous as under-abstraction:

**Under-abstracted**: 30 files with copy-pasted login flows. One auth change = 30 fixes.
**Just right**: Shared `loginAsAdmin()` helper. One auth change = one fix. Tests still readable.
**Over-abstracted**: `TestFramework.execute(TestConfig.fromYAML('claim-test.yml'))`. Nobody can read the tests. Debugging requires understanding 4 abstraction layers.

The test: Can a new developer read a test file and understand what it's testing within 30 seconds? If yes, abstraction is appropriate. If they need to trace through 3+ files to understand a single test, you've over-abstracted.

**Application**: When recommending abstractions, always show the "before and after" readability. If the abstraction makes the test LESS readable, it's wrong regardless of DRY principles.

## Pattern 5: The CI Pipeline Compatibility Checklist

Tests that work locally but fail in CI usually fail for one of these reasons:

1. **Timing**: Local machine is fast, CI runner is shared/slow → hardcoded waits fail
2. **State**: Local runs sequentially, CI runs in parallel → shared state collisions
3. **Environment**: Local has .env, CI has different config → hardcoded URLs break
4. **Resources**: Local has one browser, CI has 4 workers → memory/port conflicts
5. **Network**: Local hits real services, CI hits stubs → different response shapes

**Application**: When reviewing, mentally simulate "what happens if 4 copies of this test run simultaneously on a machine with 2 CPU cores?" That's your CI reality.

## Pattern 6: The Test Naming Contract

Test names are a contract with future developers. They should answer three questions:
1. **What component** is being tested?
2. **Under what conditions?**
3. **What is the expected outcome?**

`test('claim test')` answers none. `test('should show validation error when claim amount exceeds policy limit')` answers all three. The name IS the documentation.

**Application**: Bad test names are a HIGH finding, not a LOW one. When tests fail in CI, the name is the first thing a developer sees. If it says `test('test 1')`, they have to read the entire test to understand what broke.
