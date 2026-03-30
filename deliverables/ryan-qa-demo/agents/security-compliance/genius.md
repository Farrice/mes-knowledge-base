# Security & Compliance — Genius Patterns

> Deep knowledge that separates a checklist scanner from a compliance specialist.

## Pattern 1: The Training Effect

Finding a fake SSN in test code is NOT about whether that specific SSN is real. It's about what it teaches. Every time a developer sees `'123-45-6789'` in a test, their brain normalizes the pattern of "SSNs go in code." Eventually someone pastes a real one. Kill the pattern, not just the instance.

**Application**: Flag ALL SSN-format strings, even obviously fake ones. The fix isn't "use a different fake SSN" — it's "use a data generator or masked format so the pattern of typing SSNs into code never forms."

## Pattern 2: The Audit Trail Inversion

Most developers think about test data as "does my test pass?" Compliance thinks about test data as "can I prove where every piece of data came from and that none of it is real?" This is an inverted concern — the developer cares about the test, the auditor cares about the data.

**Application**: Always evaluate test data architecture from the auditor's perspective. If someone asked "show me where your test data comes from," the answer should be one fixture file or one generator, not "it's scattered across 200 test files."

## Pattern 3: The CI/CD Log Blind Spot

Test code runs in CI/CD pipelines. CI/CD pipelines produce logs. Logs are often stored in third-party systems (GitHub Actions, Jenkins, CircleCI). If test code prints PII to console — even temporarily, even in a failed test's error output — that PII now lives in a logging system that may not meet data handling requirements.

**Application**: Flag `console.log`, `console.error`, `console.warn`, and any logging that outputs test data. Also check error messages in assertions — `expect(result).toBe('123-45-6789')` will print the SSN in the failure output.

## Pattern 4: The Fixture Governance Principle

Centralized test data fixtures aren't just "cleaner code." They're a governance control point. When all test data flows through fixtures:
- You can audit it in one place
- You can rotate it on schedule
- You can prove it's synthetic
- You can classify it by sensitivity level
- New developers can't accidentally introduce PII

**Application**: When reviewing, check not just whether fixtures exist, but whether they're actually used. A `testData.ts` file that exists but is bypassed by inline data in half the tests provides false confidence.

## Pattern 5: Insurance-Specific Data Sensitivity

Insurance codebases handle data types that generic security tools miss:
- **Policy numbers** — often look like random alphanumeric strings, but are uniquely identifying
- **Claim amounts** — combined with dates, can identify specific claims
- **Agent/broker codes** — internal identifiers that link to real people
- **Beneficiary information** — names + relationships + financial data = highly sensitive
- **Medical codes (ICD-10)** — in health insurance, these are protected health information

**Application**: Don't just scan for "SSN" and "password." Build a mental model of what data the application handles and look for ALL of it in test code.

## Pattern 6: The "Temporary" Credential Trap

Developers often add credentials "temporarily" during development:
- `// TODO: move to env vars` (never happens)
- Commented-out credentials (still in git history)
- `.env.example` files with real values
- Test setup that creates real API sessions

**Application**: Treat commented code the same as active code for credential scanning. Check git blame — if a "temporary" credential has been there for more than one PR, it's permanent.
