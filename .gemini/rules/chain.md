# The Chain — 6 Steps, Every Deliverable

> THE CHAIN RUNS ON EVERY DELIVERABLE. "Trivial" is NOT a skip condition.

## Step 1: SCORE (1-5)
+1 Deliverable | +1 Audience | +1 Context | +1 End state | +1 Specific language.
**Print:** `CHAIN Step 1 — Score: [X]/5 | [reasoning]`

## Step 2: SHARPEN (if ≤ 3)
Ask missing dimensions. One round max. Skip if ≥ 4.

## Step 3: ROUTE
Name the expert. For known domains, route in-head (see `routing.md`).
Ambiguous? Read `DOMAIN_REGISTRY.md`. Check `FARRICE.md` for auto-deploy signals.
**Print:** `CHAIN Step 3 — Routing to: [Expert] | [reason]`

## Step 4: LOAD — ⛔ Last Chance to Read Files

Step 5 allows ZERO tool calls. Read everything you need NOW.

1. Check if expert is hot (already loaded this conversation) — skip if yes
2. Read `skills/[name]/SKILL.md` + relevant `workflows/*.md`
3. Add `genius.md` only if creative/complex or first pass was weak
4. **Pre-check:** "Do I have everything to produce the full output?" If no, read now.

For content: minimum 2 skill files per `directives/content_creation_gate.md`.
**Print:** `CHAIN Step 4 — Loaded: [Expert] Tier [X] | Files: [list]`
Then write `.agent/session-state.md`.

## Step 5: PRODUCE — Use Tools, Then Write (Never Both at Once)

⛔ **Each response is EITHER tool calls OR text. Never both in the same response.**

If the workflow requires research or data gathering:
1. **First response(s):** Make tool calls — run Perplexity searches, read data files, execute scripts. Output ONLY tool calls, no prose.
2. **Final response:** Generate your deliverable text using the results. ZERO tool calls in this response.

**You MUST actually use tools when the workflow requires it.** Do NOT substitute training data for real research. If a workflow says "search for X" or "analyze Y" — make the tool call.

## Step 5.5: VERIFY — Adversarial Check (Implementation Tasks)

For code, scripts, system changes, and workflow modifications:
1. Switch from implementer mindset to verifier mindset: "What would make this fail?"
2. Run actual commands — reading is not verification
3. Execute at least one adversarial probe (boundary values, idempotency, missing refs)
4. Issue VERDICT: PASS / FAIL / PARTIAL

FAIL → fix and re-verify before proceeding. Full protocol: `directives/verification-agent-protocol.md`.

Skip for content/copy/strategy tasks — those use the quality gate in Step 6.

## Step 6: FINALIZE — Separate Call After Text

Present output first. Then run as a separate tool call:
```bash
python3 execution/chain_runner.py finalize "[1-sentence summary]" \
    --expert [name] --skill [dir] --workflow [name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[1-2 lines]"
```
⛔ Pass only a SHORT summary. Large payloads crash the JSON parser.
If composite < 7 or any dimension < 6: retry weakest section, re-finalize.
**Print:** `CHAIN Step 6 — Finalized | Intent [X], Expert [X], Adversarial [X] | Composite: [X]`

---

## Narrowing (Never Skipping)

| Condition | Shortened | Required |
|-----------|-----------|----------|
| Score 4-5 | Skip Step 2 | 1,3,4,5,6 |
| "Just do it" | Skip Step 2, route silently | 1,3,4,5,6 |
| Follow-up, same plan | Reuse Step 3 | 1,4,5,6 |
| System command | Chain doesn't apply | — |

## Workflow Override
`/command` or `@command` → read `.agent/workflows/[command].md`. Workflow = Step 5. Chain still wraps it (Steps 1,3,4,6).
