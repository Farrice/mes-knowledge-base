# The Mailroom — Agent-to-Agent Communication Protocol

## Opt-in production companion (2026-09-08)

Recovered selectively from `worktree-mailroom`; existing council defaults below
remain intact. Production is explicitly requested, not automatically selected
because a task mentions experts. Extraction, original prompts and V2 stay fixed.

Compile a production assignment with:

```bash
python3 execution/persona_team.py production --packet <assignment.json> --platform codex
python3 execution/persona_team.py evaluate --record <pilot-record.json>
```

The packet contains `id`, `client`, `objective`, `output`, `preserve`, `constraints`,
`context` and `excluded_examples`. Each context entry names an exact `path`, `kind`
(skill, method, workflow, execution_prompt, source, approved_example, correction),
`client` (the named client or shared), and why it is relevant. Optional inclusive
`start_line`/`end_line` selects a complete relevant section. Full selections are
loaded without prefix truncation, with file/selection hashes in the receipt.
Missing files, absent required kinds, wrong declared client scope or excluded
examples in the positive packet yield `INPUT_GAP` and no dispatchable members.
These are input checks; the conductor still evaluates actual relevance and truth.

The generated common brief must be frozen before a paired comparison. All routes
receive identical evidence, expertise, constraints, approved examples and feedback
access. Keep source acquisition outside the paired production stage. If facts
change, refreeze and restart both variants rather than changing only one side.

Production responsibilities are source strategist, craft owner and independent
editor. The conductor supplies canonical peer task names after native dispatch.
In Codex use `collaboration.send_message`; an idle worker may require a conductor
`followup_task`. Peers return complete evidence, drafts, challenges and revised
positions. Root owns all file writes; there is no concurrent shared-file appending
exception in this Codex production run. No additional worker dispatches.

The source strategist and craft owner form independent initial positions. The
editor independently assesses the shared brief before reading the craft draft.
Then direct exchanges can revise specific choices. Collect every full contribution
with stable `id`, `role`, `status`, `body` and optional `revised_artifact`.
`expert_production.revision_handoff()` retains all of it. The craft owner returns
`final_artifact` plus a decision for every contribution id: accept/reject, reason,
and affected passage. `check_integration()` verifies coverage, never quality.
Failed/missing workers produce an incomplete handoff; the conductor may finish
useful work, but cannot label it a complete team comparison.

The craft owner writes the final artifact; the conductor must not replace it with
a summary. No fixed discussion word cap or top-three-changes limit constrains an
assigned finished artifact. Preserve the artifact's native format and creative
latitude. Source claims, marketing promises and old workshop rituals inside
loaded references do not override the current client assignment.

### Jen proof sequence and adoption

The first pilot lives in Jen's existing content studio under
`04-deliverables/social-content/2026-09-08-swarm-pilot/`. First one B-roll post,
then a second distinct B-roll post after acceptance, then a photographic carousel
after B-roll acceptance. Use a solo baseline from a fresh context and a separate
three-role team; inherited model settings, no cross-reading before draft lock.
Do not add paid generation, publishing or new account permissions.

Farrice compares anonymized work and supplies corrections. Jen keeps final client
approval. Record active human correction/preparation minutes separately from
experimental judging; no inference from chat delays, revision counts or AI time.
Use at most two feedback revision rounds per route and one bounded repair of a
failed case. Do not disguise extra failed samples as a new first attempt.

The evaluator requires all `broll-1`, `broll-2`, `carousel-1` records: matched
inputs verified; no regression; approved standard met; a recorded Farrice quality
preference for swarm; observed lower active human work; and demonstrated feedback
application on later cases. Missing observations mean `UNPROVEN`, a tie/failure
means `REVISE`, a second failed attempt means `RETAIN_CURRENT_METHOD`. Passing
means only `ADOPT_FOR_JEN_COMPARABLE_WORK`, never global superiority.

Report actual agent counts, elapsed time and tokens when available. Mark absent
telemetry `UNMEASURED`. This is a practical outcome comparison, not an equal-compute
experiment. A broader extraction evolution requires separate evidence identifying
an extraction-specific problem; never bundle it into this production repair.

### Storage and feedback

Use the existing client vault and posting-package surfaces. Preserve legacy
`shipped` text as historical wording, not proof of posting. New pilot records keep
`copy_approval`, `rendered_availability`, `client_approval`, `delivery`, and
`publishing` separate. Drafts are review-only until approved. Rejected examples
stay excluded from positive retrieval. Save human feedback alongside the affected
artifact and scope, then verify a later artifact applied it without reminders.
Do not auto-append creative verdicts to expert/global memory or rewrite skills.

All production tooling is advisory/read-only except the conductor's explicitly
authorized local writes. An input/coverage PASS never overrides missing human
judgment, source fitness, permissions or the client approval boundary.

> **Goal:** reply-to-reply deliberation — personas answer each other's challenges instead of
> shipping every disagreement upward frozen at exchange one.
> **Scar:** frozen-snapshot deliberation (2026-08-27, Grok Bot blueprint session — every council
> phase fired personas in parallel against a static snapshot; `/roundtable` Round 2 worked around
> it by ventriloquizing the exchange, reintroducing the anchoring bias Round 1 existed to kill).
> **Decision:** Farrice, 2026-08-27 — adopt the full Grok Bot interaction layer, adapted to this
> harness. Source: Mark Kashef, "Cursor Accidentally Exposed Grok Bot's Blueprint"
> (youtube.com/watch?v=mAWT1HCBgbQ) + b-nnett/grok-bot-0.18-reconstructed.

## Where this runs

Live deliberation is **conductor-executed with the Agent tool** (named teammates + SendMessage).
Workflow-engine `agent()` calls cannot message each other — so live mode is a runbook
(`.agent/workflows/roundtable-live.md`), never a `.workflow.js`. We build no app: the harness IS
the runtime (teams, messaging, worktree sandboxes, permission modes). This directive is only the
protocol those teammates follow. Briefs are generated by `execution/persona_team.py` — never
hand-write a teammate brief.

## The six mechanics (Grok Bot → here)

| Mechanic | Implementation |
|---|---|
| Per-agent identity + private notes | `genius.md` excerpt + `agents/<name>/memory/context.md`, loaded at seat time, appended at session close (`persona_team.py close-session`) |
| Async DMs | SendMessage between named teammates; non-blocking — send, then keep working |
| Priority tiers | `[NORMAL]` / `[PRIORITY]` / `[URGENT]` subject prefixes (semantics below) |
| Manager-run meetings | Conductor = manager; rounds with pass tokens; max 3 rounds; ends in `{crux, next_steps, dissent_log}` |
| Per-agent screen/sandbox | Existing worktree lanes + `isolation:'worktree'` — reuse, never rebuild |
| Progressive permissions | Harness-native permission modes — reuse, never rebuild |

## DM semantics

- Address peers by teammate slug (`SendMessage to: "cardinal-mason"`). Subject prefix is mandatory:
  - `[NORMAL]` — recipient reads after finishing its current beat. Default; when unsure, NORMAL.
  - `[PRIORITY]` — recipient reads at its next natural pause (tool-call boundary).
  - `[URGENT]` — recipient drops its current thread now. Legal ONLY for a factual error or a
    finding that invalidates a peer's in-flight work. Urgency inflation is a protocol violation —
    the conductor names it in the session digest.
- **Non-blocking always.** After sending, keep working. Never idle waiting on a reply.
- **Farrice outranks everything.** His input reaches the meeting via the conductor as `[URGENT]`;
  nothing interrupts his conversation.

## Meeting protocol (the anti-chatter mechanism)

1. Conductor opens a round with the question on the table and the Commons path.
2. Round-robin: every member either **contributes** — BUILD on a named peer, CHALLENGE with the
   real disagreement stated plainly (never smoothed), or CROSS-POLLINATE two ideas into something
   none said alone — or replies exactly **`PASS`**. Restating agreement is not a contribution.
3. **Max 3 rounds.** A round where every member passes ends the meeting immediately.
4. Every meeting ends with the conductor's `{crux, next_steps, dissent_log}` — a meeting without
   next steps didn't happen.
5. Dissent canon unchanged and binding inside teams: preserve real disagreement for the synthesis;
   consensus-blending is a failure of the meeting, not a simplification (EVAL-045).

## The Commons (shared reasoning file)

Per-session blackboard at `councils/commons/<date>-<slug>.md` — the "Reasoning Trace Linker" that
`skills/mark-kashef-ai-councils` specifies as its own top rubric tier, now real. Rules:
- Append-only. Each member writes under its own `### <Name>` heading; never edit another's entries.
- What goes in: evidence with sources, intermediate findings, named disagreements. Not chatter.
- Members read the Commons before each contribution. The conductor snapshots it into the session
  digest at close. This is the sanctioned exception to `parallelism-cheat-sheet.md` Rule 2
  ("no shared state") — one file, one session, conductor-owned lifecycle.

## The reader contract (binding — Farrice feedback 2026-08-27: "verbosity, not insight")

The machinery stays in the engine room. What Farrice reads per council (extended 2026-08-27 after
session 2 — "this is exactly what I wanted"): **the debate in the seats' own plain words** (who
pushed back, who conceded, why — quotes over summaries) **then the one-page decision: Do this /
Don't do / We're wrong if**, cost in one closing line. Seats are briefed that their words go to
him verbatim — plain first-person, ≤180 words, no framework names. Expansive on insight, zero on
process. Entry gate: the conductor attempts a one-paragraph answer first — a confident paragraph
replaces the council. Grounding: seats get his real report outputs (revenue_tracker, live offer
docs, open loops) verbatim, never memory paraphrase. This register is his DEFAULT for all
substantive system outputs, not just councils (memory: default-output-register-debate-then-memo).

## Cost discipline (binding — Farrice 2026-08-27: "no haphazard burning")

- **Frozen mode stays the default.** Live mode is invoked deliberately (`--live` / the
  roundtable-live runbook) for taste-bearing forks and real disagreements — never auto-routed.
- 4 seats default, 6 max. Sonnet bodies, Opus heads per the seating law (`orchestration-doctrine.md`);
  no unseated dispatches.
- Persona loads are capped excerpts (`persona_team.py`: genius ≤6k chars, memory ≤2k), sized to the
  question, not the library.
- Pass tokens exist to kill wasted turns: a dry meeting ends in one round.
- Every live session's digest records measured token/agent counts. Nothing about live mode becomes
  a default until Farrice confirms the measured number is worth it (3-run review).

## Session close (identity accumulates)

At close the conductor runs `python3 execution/persona_team.py close-session --members <slugs>
--question "<q>" --verdict "<one line>" --session <digest path> [--positions '<json>']` — one
entry per seated persona into `agents/<name>/memory/context.md` (Grok Bot's "private notes"),
so the next council that seats them starts from accumulated experience, not a cold genius file.
Standing-council sessions also append the verdict line to `councils/<name>/decisions.md` and close
any matching `councils/buyers/calibration.jsonl` rows whose outcome is now known.

## Grounding chain (Seating Charter compliance)

Farrice's 2026-08-27 decision grants the Mailroom its exception to the hop-2+ clause — and every
chain still grounds in him within two hops by design: DM → synthesis → Farrice; persona memory →
next council he convenes → Farrice; standing-council pulse → COS digest → Farrice. No agent-only
loops: anything that stops grounding in him gets archived per the charter, no ceremony.
