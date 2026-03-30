# Flakiness Hunter — Genius Patterns

> Deep knowledge for finding tests that will betray you on the worst possible day.

## Pattern 1: The Flakiness Taxonomy

Not all flaky tests are created equal. There are 5 root causes, each with different fixes:

| Root Cause | Signal | Fix |
|-----------|--------|-----|
| **Timing** | `waitForTimeout`, hardcoded delays | Auto-retrying assertions, network waits |
| **Shared State** | Test passes alone, fails in suite | Test isolation, fixture per-test data |
| **Environment** | Passes locally, fails in CI | Environment variables, config-based setup |
| **Resource Contention** | Fails under parallel execution | Worker isolation, unique data per worker |
| **External Dependency** | Fails when API/service is slow | Mock external services, circuit breakers |

Most teams treat all flakiness as "timing issues" and add more waits. This only fixes 1 of 5 causes and makes the other 4 worse (longer tests = more time for state collisions).

## Pattern 2: The CI Multiplication Factor

A test that has 1% failure rate sounds acceptable. Here's why it's not:

- 1% failure rate × 200 tests = **87% chance at least one fails per run**
- Formula: `1 - (0.99)^200 = 0.866`
- With 3 retries each, CI time bloats 5-15 minutes per flaky test
- With 5 flaky tests, pipeline adds 25-75 minutes of waste PER DAY

At scale, "rare" flakiness becomes "constant" pipeline failure. The math is brutal.

**Application**: When you spot a flakiness risk, calculate the multiplication factor for the team's test suite size. "This wait pattern has ~5% failure risk, and with 150 tests, that's a 99.95% chance of at least one failure per CI run."

## Pattern 3: The Race Condition Detector

Race conditions in tests happen when:

1. **Click then assert without waiting** — The click triggers an API call, the assertion runs before the response arrives
2. **Multiple tests modify the same record** — In parallel, last-write-wins is non-deterministic
3. **Animations or transitions** — Element exists but is mid-animation, click hits wrong position
4. **Debounced inputs** — Type a value, but the component debounces and the assertion fires before the debounce resolves

The fix pattern is always the same: **wait for the CONSEQUENCE, not the ACTION.** Don't wait for the button click. Wait for the table row that the click creates.

```typescript
// RACE CONDITION — click fires, assertion runs before API responds
await page.click('#submit');
await expect(page.locator('.success')).toBeVisible(); // might fail

// SAFE — wait for the network response, THEN assert
await Promise.all([
  page.waitForResponse('**/api/claims'),
  page.click('#submit'),
]);
await expect(page.locator('.success')).toBeVisible(); // response is back
```

## Pattern 4: The Time Zone & Date Trap

Date-dependent tests are a hidden flakiness source:

- **Tests that use `new Date()`** — Will produce different results at 11:59 PM vs. 12:01 AM
- **Tests that compare dates** — Daylight Saving Time shifts break date comparisons twice a year
- **Tests with "today" or "yesterday" logic** — Break on Jan 1, month boundaries, leap years
- **CI servers in different time zones** — Test passes in EST, fails when CI runs in UTC

**Application**: Flag any test that creates or compares dates without explicitly setting the time zone. Playwright's `page.clock` API exists specifically for this.

## Pattern 5: The Viewport & Responsive Flakiness

Tests that work at 1920×1080 but break at 1366×768 aren't flaky — they're untested at the wrong viewport:

- **Element hidden below fold** — `click()` succeeds on visible viewport, fails when element requires scroll
- **Overlay/modal covering target** — At smaller viewports, elements overlap
- **Responsive layout shifts** — Elements exist but are in different positions at different breakpoints

CI runners often use different default viewports than developer machines. If your tests don't explicitly set viewport, they're running at an unpredictable size.

## Pattern 6: The Flaky Test Quarantine Protocol

When a flaky test is found, the wrong response is "add a retry." The right protocol:

1. **Tag it** — `test.fixme('JIRA-1234: flaky due to timing')` or `test.skip`
2. **Track it** — File a ticket with failure rate data and CI logs
3. **Timebox it** — If not fixed in 2 sprints, delete the test (a flaky test is worse than no test)
4. **Root cause it** — Use the taxonomy above to identify which of the 5 causes applies
5. **Fix the cause, not the symptom** — Adding retries hides the bug. Fix the isolation, timing, or environment issue.

**Application**: When flagging flakiness risks, always suggest the quarantine step AND the root cause investigation. "Add a retry" is never the recommendation.
