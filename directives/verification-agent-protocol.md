# Verification Agent Protocol

> **Purpose**: Adversarial verification that tries to _break_ deliverables before finalization. Adapted from Claude Code's verification agent architecture.
> **When**: Fires between Step 5 (PRODUCE) and Step 6 (FINALIZE) for implementation work.
> **Principle**: The verifier's job is NOT to confirm the implementation works — it's to try to break it.

---

## When to Activate

| Task Type | Verification Required |
|-----------|----------------------|
| Code / scripts / execution files | ✅ Always |
| System changes (directives, workflows, prompts) | ✅ Always — dry-run on an example |
| Content / copy / strategy | ⚠️ Only via quality gate (Step 6) |
| Quick answers / conversations | ❌ Never |

---

## Two Documented Failure Modes

You have two failure patterns to guard against:

1. **Verification avoidance**: When faced with a check, you find reasons not to run it — you read code, narrate what you would test, write "PASS," and move on. **Reading is not verification. Run it.**

2. **Seduction by the first 80%**: You see a polished output and feel inclined to pass it, not noticing half the functions do nothing, the state vanishes on edge cases, or the script crashes on bad input. **Your entire value is in finding the last 20%.**

---

## Verification Strategy (by change type)

**Scripts / execution files:**
- Run with representative inputs → verify stdout/stderr/exit codes
- Test edge inputs (empty, malformed, boundary values)
- Verify --help / usage output is accurate

**Workflow / directive changes:**
- Dry-run the workflow on a simple example
- Check that all referenced files/paths exist
- Verify the workflow produces output that matches its claimed format

**System prompt changes:**
- Run a test query that exercises the changed instruction
- Verify the chain still fires correctly
- Check that no existing behavior is broken

**Integration / API changes:**
- Hit the endpoint or run the API call → verify response shape
- Test error handling with bad inputs
- Check idempotency: same request twice → correct behavior?

---

## Required Steps (Universal)

1. **Read the spec**: What was the deliverable supposed to do? What's the success criteria?
2. **Build check**: If applicable, does it run without errors?
3. **Functional check**: Run it with intended inputs → expected outputs?
4. **Adversarial probe**: Run at least one attempt to break it:
   - Boundary values: 0, -1, empty string, very long strings, unicode
   - Idempotency: same mutating action twice
   - Missing references: IDs/paths that don't exist
   - Concurrency: if applicable, parallel requests

---

## Recognize Your Own Rationalizations

These are the exact excuses you reach for — recognize them and do the opposite:

- "The code looks correct based on my reading" — **reading is not verification. Run it.**
- "This is probably fine" — **probably is not verified. Run it.**
- "This would take too long" — **not your call.**
- "I don't have a way to test this" — **did you actually try? Write a test script to /tmp/ if needed.**

If you catch yourself writing an explanation instead of a command, **stop. Run the command.**

---

## Output Format

Every check MUST follow this structure:

```
### Check: [what you're verifying]
**Command run:**
  [exact command you executed]
**Output observed:**
  [actual output — copy-paste, not paraphrased]
**Result: PASS** (or FAIL — with Expected vs Actual)
```

End with exactly one of:
```
VERDICT: PASS
VERDICT: FAIL
VERDICT: PARTIAL
```

- **PASS**: All checks passed, including at least one adversarial probe
- **FAIL**: A check failed that should block deployment
- **PARTIAL**: Environmental limitation prevented full verification (not for uncertainty)

---

## Chain Integration

### Before Finalize (Step 5.5)

For implementation tasks, run verification between produce and finalize:

```
Step 5: PRODUCE → output generated
Step 5.5: VERIFY → adversarial checks
  If VERDICT: PASS → proceed to Step 6
  If VERDICT: FAIL → fix, re-produce, re-verify
  If VERDICT: PARTIAL → note limitations, proceed to Step 6 with caveat
Step 6: FINALIZE → quality gate + log
```

### Finalize Integration

When running `chain_runner.py finalize`, include verification result in notes:
```bash
python3 execution/chain_runner.py finalize "[summary]" \
    --expert [name] --skill [dir] --workflow [name] \
    --type System \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "VERDICT: PASS | [verification summary]"
```

The adversarial resilience score in Step 6 should reflect the verification verdict:
- VERDICT: PASS → adversarial score ≥ 7
- VERDICT: PARTIAL → adversarial score 5-6
- VERDICT: FAIL → do not finalize until fixed

---

## Anti-Pattern: Self-Grading

The implementer and verifier should apply different mental models:
- **Implementer mindset**: "Does this do what was asked?"
- **Verifier mindset**: "What would make this fail?"

The same agent can hold both, but you must _switch modes_ between Step 5 and Step 5.5. If your verification step finds zero issues, you probably didn't try hard enough.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | — |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-05-01 |

*Created: 2026-04-01 | Adapted from Claude Code verification agent architecture*
