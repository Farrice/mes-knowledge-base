# Verification Agent Protocol

> **Purpose**: Adversarial verification that tries to _break_ deliverables before finalization. Adapted from Claude Code's verification agent architecture.
> **When**: Fires between Step 5 (PRODUCE) and Step 6 (FINALIZE) for ALL deliverables — implementation AND content/research with real-world claims.
> **Principle**: The verifier's job is NOT to confirm the implementation works — it's to try to break it. For factual deliverables: the verifier's job is to find what's wrong before the user does.

---

## When to Activate

| Task Type | Verification Required |
|-----------|----------------------|
| Code / scripts / execution files | ✅ Always — run it |
| System changes (directives, workflows, prompts) | ✅ Always — dry-run on an example |
| **Research / factual deliverables** | **✅ Always — verify claims against sources (see Factual Verification below)** |
| **Content / copy with real-world claims** | **✅ Always — verify every proper noun, policy, date, price, spec, API detail** |
| Pure creative / strategic (no verifiable facts) | ⚠️ Only via quality gate (Step 6) |
| Quick answers / conversations | ❌ Never |

**The old rule that content "only fires via quality gate" is revoked.** That gap allowed factually wrong deliverables to pass because the quality gate didn't check facts. Now: if a deliverable makes claims about the real world, verification fires.

---

## Three Documented Failure Modes

You have three failure patterns to guard against:

1. **Verification avoidance**: When faced with a check, you find reasons not to run it — you read code, narrate what you would test, write "PASS," and move on. **Reading is not verification. Run it.**

2. **Seduction by the first 80%**: You see a polished output and feel inclined to pass it, not noticing half the functions do nothing, the state vanishes on edge cases, or the script crashes on bad input. **Your entire value is in finding the last 20%.**

3. **False confidence in factual claims (added 2026-04-15)**: You research a topic, get results from one or two sources, and compile them into a polished document. The polish — tables, frameworks, confident tone — makes unverified claims look as solid as verified ones. You present a banned item as recommended gear, mislabel a major artist, cite a feature that doesn't exist where you said it does, and hand it over like it's done. **The user becomes the fact-checker on their own deliverable. This is the most dangerous failure mode because it erodes trust in the entire system.** Origin: Coachella 2026 family plan — 6+ factual errors delivered with full confidence, caught only because the user pushed back.

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

**Research / factual deliverables (added 2026-04-15):**
- **Claim inventory**: Before writing, list every factual claim the deliverable will make. Policies, names, dates, prices, locations, specs, schedules, rules.
- **Source verification**: Each claim must be checked against primary sources (official sites, documentation, authoritative reporting). Single-source claims get flagged. Multi-source (3+) claims are grounded.
- **Verify BEFORE writing**: Research → verify → THEN compile. Not: research → compile → verify after pushback. The verification pass must happen before the user sees anything.
- **Confidence labeling**: Every factual claim in the deliverable must be one of:
  - **VERIFIED** — confirmed across 2+ independent sources. No flag needed in output.
  - **LIKELY** — from one credible source or strong inference. Flag in output: *"[Based on single source / inferred from X]"*
  - **UNCONFIRMED** — could not verify. Flag in output: *"[Unconfirmed — verify directly with X]"*
  - Presenting UNCONFIRMED info with VERIFIED confidence = automatic Factual Grounding score ≤4.
- **Proper noun check**: Every person, company, product, artist, or named entity — verify it exists and is described correctly. "Nine Inch Noize is a heavy electronic act" when it's actually NIN + Boys Noize = the kind of error that destroys trust.
- **Policy/rule check**: Any claim about what's allowed, banned, required, or costs money — verify against the official source, not a third-party summary. Third-party summaries paraphrase and introduce errors.
- **Contradiction scan**: If two sources disagree, flag the contradiction and present both — don't pick the one that sounds better.
- **Internal consistency scan (added 2026-04-23)**: Before delivery, check whether two of your own outputs in this session contradict each other. If file A says "Gemini 3.1 Pro-backed" and file B says "Gemini 2.5 Pro," one of them is wrong. Origin: Gemini 2.5 vs 3.1 naming error where both claims coexisted in session context but no mechanism forced a cross-check.

### Freshness Tax (added 2026-04-23 — mechanical enforcement via hookify)

**Any of these claim categories MUST fire verification before delivery.** Non-optional. Not willpower-gated. The `.claude/hookify.freshness-tax.local.md` hook mechanically blocks session end when these patterns appear without verification evidence.

| Category | Examples | Must verify against |
|---|---|---|
| **Model names + versions** | `Gemini 3.1 Pro`, `Claude Opus 4.7`, `GPT-5`, `Sonnet 4.6` | Primary source fetched THIS SESSION (not memory). Model lineups change monthly. |
| **Pricing** | `$20/mo`, `$249.99/month`, `$0.05 per query`, `$100 Cloud credits` | Official pricing page with date stamp. |
| **Dates / "as of" claims** | `as of April 2026`, `launched Dec 2025`, `released last week` | Primary source + confirm the date is actually current. |
| **Status claims** | `beta`, `GA`, `preview`, `deprecated`, `early access`, `public API`, `trusted testers only` | Official announcement or changelog. |
| **Benchmark numbers** | `93.3% on DeepSearchQA`, `top quartile`, `outperforms X` | Original benchmark source, not a summary article. |
| **Superlatives** | `latest`, `newest`, `state-of-the-art`, `most advanced`, `current` | Force yourself to name the primary source. If you can't, remove the superlative. |

**How to satisfy the Freshness Tax** (any ONE of these closes the hook):

1. **Verified live this session** — ran `/deep-research-gemini`, `/grounding-pass`, or `WebFetch` against a primary source dated within 30 days. Cite the URL.
2. **Confidence labels applied** — every freshness-sensitive claim in the deliverable is tagged `[VERIFIED]`, `[LIKELY]`, or `[UNCONFIRMED]` with explicit reasoning for the label.
3. **No factual claims** — the deliverable is purely creative/strategic with no version/price/date assertions.
4. **Explicitly flagged to user** — you told the user these claims are unverified and why (matches the `Say I don't know` memory rule).

**Why this exists**: The system has failed this exact class of check repeatedly — Coachella 2026 family plan (6+ factual errors), Gemini 2.5 vs 3.1 naming (today), Parallax Edition 02 fabrications. Every failure had the same shape: research → compile → polish → deliver → user catches. Verification was willpower-gated. The hook moves it into the harness layer where it runs regardless of my state. State + mechanical enforcement beats discipline every time.

### Source Hierarchy for Factual Verification

When checking a claim, prefer sources in this order — each has different strengths:

1. **Primary source** (official website, documentation, authoritative org). Always highest priority. No API needed, use WebFetch.
2. **Recall** (3,038 saved cards — extractions, transcripts, prior research). Free, zero-latency. Use `mcp__recall__search` to check if claim is grounded in your own knowledge base. Often catches claims that external search misses because Recall indexes long-form expert content.
3. **Deep Research / Deep Research Max** (Gemini Interactions API). Highest-accuracy external research (93.3% DeepSearchQA for Max). Use `/deep-research-gemini` or `execution/deep_research_client.py` for foundation-level verification. Budget-safe: Ultra-covered with $10 prepaid ceiling. See `directives/google-api-usage-policy.md`.
4. **Perplexity sonar-deep-research** (via `perplexity_client.py`). Proven track record, $30/mo budget, fast. Preferred when Deep Research budget is low or rate-limited.
5. **Perplexity sonar-pro** (via `perplexity_client.py`). Tier 2 validation, fact-check, trend verification.
6. **Web search** (search_web + read_url_content). Fallback when budgeted tools exhausted. Only as last resort because raw search results can be wrong/paraphrased.

**Fallback chain**: Deep Research → Perplexity sonar-deep-research → Perplexity sonar-pro → web search. Tag the output with which source actually ran if a fallback fired.

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
- "I found it in a search result, so it's true" — **search results paraphrase, hallucinate, and conflate. Check the primary source.**
- "The document looks comprehensive" — **polish is not accuracy. Comprehensive-looking with wrong facts is worse than rough with right facts.**
- "I'll flag it for the user to verify" — **only acceptable AFTER you've genuinely tried to verify it yourself. Delegation ≠ diligence.**
- "It's a minor detail" — **minor details are where trust erodes. You recommended a banned item as essential gear. That's not minor.**

If you catch yourself writing an explanation instead of a command, **stop. Run the command.**
If you catch yourself compiling research into a document without a verification pass, **stop. Verify first.**

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

For ALL deliverables with verifiable claims (implementation AND content/research):

```
Step 5: PRODUCE → output generated
Step 5.5: VERIFY
  Implementation: adversarial checks (run it, break it)
  Factual: claim inventory → source verification → confidence labeling → contradiction scan
  If VERDICT: PASS → proceed to Step 6
  If VERDICT: FAIL → fix, re-research if factual, re-produce, re-verify
  If VERDICT: PARTIAL → note limitations, proceed to Step 6 with caveat
Step 6: FINALIZE → quality gate (now 4 dimensions) + log
```

**For factual deliverables, the verification step MUST happen before the user sees the document.** If you compile first and verify after pushback, Step 5.5 has failed even if the corrections are right. The sequence matters: research → verify → compile → deliver. Not: research → compile → deliver → get caught → verify → fix.

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

For factual deliverables, the Factual Grounding score (Dimension 4) should reflect:
- All claims verified, confidence labels applied → Factual Grounding ≥ 8
- Core claims verified, some flagged as LIKELY/UNCONFIRMED → Factual Grounding 6-7
- Unverified claims presented as fact → Factual Grounding <6 → blocks delivery

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

---

## Cross-Reference: /parallax Phase 2.5

For Parallax Substack editions, verification is front-loaded into Phase 2.5 GROUND + ZEITGEIST CHECK (`.agent/workflows/parallax.md`) — claim extraction + Recall/Perplexity routing + zeitgeist scan runs BEFORE drafting, not between production and finalize. This prevents fabrications from entering the draft in the first place rather than catching them at Step 5.5. Phase 2.5 uses the same claim-category taxonomy (PERSON/BRAND/EVENT/STAT/QUOTE/CULTURAL/TECHNICAL/PERSONAL) documented here, with an added PERSONAL category for inner-circle facts that bypass external verification.
