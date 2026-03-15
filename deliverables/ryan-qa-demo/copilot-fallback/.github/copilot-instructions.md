# QA Code Review Instructions for Copilot

When reviewing Playwright test code, apply these 5 review lenses IN ORDER:

## 1. Playwright Best Practices
- Prefer `getByRole()` > `getByText()` > `getByTestId()` > CSS selectors
- Flag any `page.waitForTimeout()` — replace with auto-retrying assertions
- Every action (click, fill) must have a corresponding assertion
- Flag raw CSS/XPath selectors as warnings

## 2. Corporate Standards (JDM)
- Test files: `[feature]-[scenario].spec.ts`
- Test descriptions: "should [verb] when [condition]"
- Page objects: `[Page]Page.ts`
- No `console.log` in committed code
- No `test.only()` in PR code
- Skipped tests require Jira ticket in `.skip()` reason

## 3. Test Architecture
- Every test must be independent — no shared state
- Page Object Model for all page interactions
- Fixtures for test data, not inline hardcoding
- Setup/teardown must clean up after itself

## 4. Flakiness Detection
- Flag ALL time-dependent patterns (timeouts, Date.now(), animations)
- Flag shared state between tests
- Flag environment-specific assumptions (timezone, locale, viewport)
- Ask: "Would this pass 1,000 times on a cold CI machine at 3am?"

## 5. Security & Compliance
- No real PII in test data (SSNs, policy numbers, real names)
- No hardcoded credentials
- Auth tokens must use environment variables
- Test data for insurance claims must use masked/synthetic data

## Output Format
For each finding use:
- 🔴 Critical (must fix before merge)
- 🟡 Warning (should fix)
- 🟢 Suggestion (nice to have)

Include the line number and provide fixed code, not just a description.
