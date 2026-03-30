# Corporate Standards — Genius Patterns

> Deep knowledge for enforcing organizational consistency across QA automation.

## Pattern 1: The Standards Adoption Curve

Corporate coding standards fail when they're imposed as a 50-page PDF nobody reads. They succeed when they're embedded in tooling. The progression:

**Level 0 — Document**: Standards exist in a wiki. Nobody checks. Violations found in PR review (too late).
**Level 1 — Linting**: ESLint/Prettier catches formatting. But logic standards aren't lintable.
**Level 2 — Templates**: Test templates enforce structure. But developers modify templates.
**Level 3 — Agent Review**: AI reviews against full standard set including intent, naming, and patterns.
**Level 4 — Generation**: AI generates compliant test scaffolding. Standards are built in, not bolted on.

**Application**: This agent operates at Level 3. When suggesting fixes, always provide the compliant code — don't just cite a rule number.

## Pattern 2: The Naming Convention Multiplier

Consistent naming isn't cosmetic. It's a search multiplier. When every test follows `should [expected behavior] when [condition]`:

- `grep "should.*when.*invalid"` finds all negative test cases
- `grep "should.*when.*unauthorized"` finds all auth tests
- `grep "should display"` finds all UI rendering tests
- New developers can find relevant tests by guessing the name

When naming is inconsistent (`test claim`, `claim test`, `test_process_claim`, `verify claim works`), search is broken and discovery is manual.

**Application**: Naming violations are HIGH, not LOW. They compound across every test written after the violation.

## Pattern 3: The Description Tag Discipline

File-level and test-level descriptions serve different audiences:

- **File-level `@description`**: For the test runner, CI reports, and QA managers. "What area does this test suite cover?"
- **`describe` block descriptions**: For developers navigating the test structure. "What feature am I testing?"
- **`test` descriptions**: For failure investigation. "What exact behavior broke?"

When a test fails at 2 AM, the on-call engineer sees the test name first, then the file name. If both say `test('test 1')` in `test.spec.ts`, they have zero context.

**Application**: Check all three levels. Missing descriptions at any level creates an information gap for a specific audience.

## Pattern 4: The Forbidden Pattern Registry

Every organization has patterns that SEEM fine but cause problems at scale. These aren't in generic linters — they're organizational knowledge:

- **`test.only`** — Left in accidentally, silently skips all other tests in the file
- **`test.skip` without a ticket number** — Skipped tests without a tracking ticket become permanently skipped
- **`console.log` in committed code** — Clutters CI output, may leak data (see Security agent)
- **`any` type annotations** — Defeats TypeScript's value in test code
- **Commented-out test code** — Dead code that confuses readers; delete it or fix it
- **Import from `../../../../../../`** — Indicates missing path aliases or broken project structure

**Application**: These are more valuable than generic lint rules because they encode organizational experience. A generic linter doesn't know that `test.skip` without a Jira ticket is a problem at your company.

## Pattern 5: The PR Template Integration

Standards enforcement is most effective when it aligns with the PR process:

- **PR description template** should prompt: "What tests were added/modified?"
- **Required labels** should include test type (unit, integration, e2e)
- **Code review checklist** should include standards compliance
- **CI gates** should block merge on standards violations

This agent's output format is designed to integrate with PR comments. Each finding includes severity, location, and fix — ready to paste into a PR review.

**Application**: When producing the review output, format it so it can be directly used in a PR comment. Include line numbers, code snippets, and specific fixes.

## Pattern 6: The Living Standards Document

Standards that never change are either perfect (unlikely) or dead (common). Healthy standards evolve:

- New patterns discovered in PR reviews get codified into standards
- Patterns that produce false positives get refined or removed
- Framework upgrades (Playwright versions) may obsolete some standards
- Team retrospectives should feed back into standards updates

**Application**: When you find a pattern that isn't covered by current standards but should be, flag it as a "Standards Gap" — a finding for the team to discuss, not a violation to enforce.
