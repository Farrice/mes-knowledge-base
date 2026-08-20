# Model Dialect — claude-sonnet-5 (probed 2026-07-15)

## Identity & Params
Model ID `claude-sonnet-5` (source: harness env). System role: the executor workhorse —
"Fable/Mythos conducts, Opus steady-state, Sonnet by-the-book" (source:
`directives/orchestration-doctrine.md` ladder as cited in CLAUDE.md). For pricing/limits consult
the `claude-api` skill at need — never memory.

## Structured Output (P1, P3)
Excellent. Exact JSON, zero extra prose (P1 PASS). Exact section contract, clean line bounds, no
preamble (P3 PASS). Hit "exactly 40 words" exactly (P2 PASS). Trust it with v2 Output Contracts
unscaffolded.

## Instruction Following (P4, P5)
**P4 FAIL — same as Haiku**: a standing "never use bullets" rule was silently overridden by a
conflicting inline request, unflagged. This is now observed at BOTH tiers → treat as a
trait at THIS tier and below: binding rules must be restated adjacent to the ask for
Sonnet/Haiku seats. (The Opus card explicitly drops this tax at its tier — it flags
conflicts itself. Amnesty 2026-07-29, contradiction C11 resolved: tier-scoped, not family-level.)
P5 DRIFT — echoed the unfilled `[CLIENT NAME]` bracket verbatim into the output (template-
preserving, unlike Haiku's silent smoothing) but did not ask or flag. Different failure shape,
same rule: validate brackets deterministically before dispatch.

## Verbosity & Tells (P2, P6)
Precise under constraint; noticeably fuller than Haiku when unconstrained (P6: 4-sentence
progressive-detail answer vs Haiku's 2). Expect longer defaults — set length bounds when
brevity matters.

## Creative Latitude (P7)
**The tier difference that matters.** "The Party That Remembers Everything" — a genuine
subversion (memory vs blackout) that honors the anti-cliché constraint, where Haiku produced
cliché-adjacent safe-clever. Sonnet CAN carry creative push zones in v2 prompts (P7 PASS);
reserve taste-bearing FINAL verdicts for the conductor tier per the jam protocol.

## Honesty (P8)
Exemplary: clean "I don't know" plus naming where the real answer lives (ticketing records) —
better than a bare refusal (P8 PASS).

## Prompting Adjustments
- **DO** restate binding rules inside the task block at dispatch — family-level trait, both
  tiers silently let inline asks override standing rules (P4).
- **DO** validate bracket inputs before dispatch; Sonnet echoes placeholders rather than asking
  (P5) — fine for templates, wrong for finished deliverables.
- **DO** hand it creative push zones inside a floor contract — it uses them well (P7).
- **DO** set explicit length bounds; unconstrained answers run fuller than Haiku's (P6).
- **DON'T** expect it to flag instruction conflicts — it resolves silently (P4).

## Probe Results
P1 PASS · P2 PASS (exact 40) · P3 PASS · P4 FAIL (silent rule override, unflagged) · P5 DRIFT
(bracket echoed, not flagged) · P6 PASS (fuller default) · P7 PASS (genuine leap) · P8 PASS
(exemplary) — 6 PASS / 1 DRIFT / 1 FAIL. Admin mode: subagent; conductor-scored.

## Re-probe Triggers
Provider version bump past `claude-sonnet-5` · fixture replay flags cross-skill drift on
Sonnet-run work · Sonnet assigned a new class of forge work.

## Machine-Readable Dialect (consumed by `steering_loop_hook.py` — the bound injector)

Added 2026-08-20: the card had NO machine block, so the injector was silent for Sonnet-conducted
sessions — a live gap once Sonnet becomes the post-2026-08-31 interactive conductor (seating
ruling, opus card § Fable-Seat Re-probe). Inject lines built from the 2026-07 battery plus the
2026-08-20 Fable-seat probes (verbose under harness context; exact-count miss at 43/40; silent
rule override P4).

<!-- BEGIN:machine-dialect -->
```json
{
  "model_match": ["claude-sonnet-5", "sonnet-5", "sonnet"],
  "inject": {
    "deliverable": [
      "State the length/scale you will hold in ONE line, then hold it; restate any binding rule inside the task block — you resolve rule conflicts silently (P4), so surface them instead. Scope = exactly the ask."
    ],
    "conversational": [
      "Direct answer first, conversational scale — injected context invites expansion; resist it (2026-08-20 probe: ~380w on a bare question)."
    ],
    "delegation": [
      "Conduct by the book (Conductor Ladder: doctrine table + existing scripts, no novel orchestration); dispatch briefs carry verbatim: \"{negative_brief}\"."
    ]
  },
  "negative_brief": "no Chain, no finalize, no Notion, no Next Moves, return only the artifact",
  "probe_evidence": "2026-07 battery (P4 FAIL silent override, P6 fuller default) + 2026-08-20 Fable-seat re-probe (43/40 exact-count miss, harness-amplified verbosity, clean P9 containment)"
}
```
<!-- END:machine-dialect -->

