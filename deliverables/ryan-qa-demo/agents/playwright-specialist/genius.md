# Playwright Specialist — Genius Patterns

> Deep knowledge from real-world Playwright at scale. Not docs — hard-won patterns.

## Pattern 1: The Auto-Retrying Assertion Principle

Playwright's killer feature is auto-retrying assertions — `expect(locator).toBeVisible()` retries until timeout. But most teams don't realize: **only `expect(locator)` auto-retries. `expect(await locator.textContent())` does NOT.** The `await` resolves immediately, snapshots the value, and the assertion checks a stale snapshot.

```typescript
// BROKEN — snapshots immediately, no retry
expect(await page.locator('.status').textContent()).toBe('Approved');

// CORRECT — auto-retries until match or timeout
await expect(page.locator('.status')).toHaveText('Approved');
```

This single misunderstanding causes 80% of flaky Playwright tests.

## Pattern 2: The Selector Hierarchy

Not all selectors are equal. In order of reliability:

1. `getByRole()` — accessible roles, survives refactors, enforces a11y
2. `getByTestId()` — explicit test hooks, immune to UI changes
3. `getByText()` / `getByLabel()` — readable but fragile to copy changes
4. `locator('[data-qa="..."]')` — custom attributes, team convention dependent
5. `locator('.css-class')` — breaks on ANY styling change
6. `locator('#id')` — seems stable, but IDs get reused/changed
7. `locator('div > span:nth-child(3)')` — breaks if someone adds a `<div>`

**Rule**: If your selector would break because a designer changed a CSS class, it's wrong.

## Pattern 3: The Wait Anti-Pattern Taxonomy

There are 4 types of waits. Only one is acceptable:

| Wait Type | Example | Verdict |
|-----------|---------|---------|
| **Hard wait** | `page.waitForTimeout(3000)` | NEVER — arbitrary, slow, still flaky |
| **Element wait** | `page.waitForSelector('.loaded')` | SOMETIMES — use `expect().toBeVisible()` instead |
| **Network wait** | `page.waitForResponse('**/api/claims')` | GOOD — waits for the actual trigger |
| **Auto-retry assertion** | `await expect(locator).toBeVisible()` | BEST — Playwright-native, retry-based |

Every `waitForTimeout` is a bug report waiting to happen. CI machines are 2-5x slower than dev machines. A 3-second wait that works locally will randomly fail in CI on heavy pipeline days.

## Pattern 4: The Network Interception Power Move

Most teams test through the full UI → API → Database stack. This makes tests slow and fragile. Playwright's `page.route()` lets you intercept API calls to:

- **Mock slow endpoints** — Don't wait 5 seconds for a real PDF generation
- **Test error states** — Return 500s, timeouts, malformed responses
- **Test empty states** — Return empty arrays without needing an empty database
- **Isolate the UI** — Test the frontend behavior independent of backend state

This isn't "cheating" — it's testing the UI layer properly. Integration tests cover the full stack. UI tests should test the UI.

## Pattern 5: The Parallel Execution Readiness Test

Before claiming tests are "ready for parallel," run this mental test:

1. Do any tests share a database user/account? → They'll collide in parallel
2. Do any tests write to the same record? → Last-write-wins in parallel
3. Do any tests depend on a specific database state? → Another worker may have changed it
4. Do any tests use the same port/file/resource? → Resource conflicts in parallel

The fix is always: **each test creates what it needs, uses what it creates, cleans up after itself.** Playwright's worker-scoped fixtures make this natural.

## Pattern 6: The Mobile Viewport Trap

Testing responsive design in Playwright requires more than `page.setViewportSize()`. Common mistakes:

- Setting viewport but not testing touch events (mobile users tap, not click)
- Not accounting for mobile browser chrome (address bar steals ~60px)
- Testing only two breakpoints (desktop, mobile) when the app has 4
- Not testing orientation changes mid-flow

**Application**: When reviewing mobile test code, check whether the test actually behaves like a mobile user or just renders in a small window.
