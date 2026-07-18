# Source Ledger — skills/deliberate

`/deliberate` is a METHOD skill (a mechanism the system built, per `docs/solutions/`-style provenance, not a person extraction). There is no `extractions/` folder to ground against — confirmed by direct command, not assumed (see row below). Ground truth is the skill's own build artifacts plus the deterministic scripts it wires to. Every file below was opened and read in full during this repair pass (2026-07-17); byte sizes were captured with `wc -c` at read time so no "0-byte" or "unrecoverable" claim goes unverified per the envelope's provenance rules.

## Claim-by-claim

| # | Claim | Source | Label |
|---|---|---|---|
| 1 | Skill built 2026-05-25, commit `30a0d6345` ("feat(deliberate+anchor-memory): multi-model deliberation + mission templates + visual board") | `git log --follow -- skills/deliberate/SKILL.md` (and `genius.md`, same commit) | VERIFIED |
| 2 | Skill reissued as a structure-pure v2 prompt 2026-07-13, commit `8ae51279c` ("feat(wiring): forge wave 3 — 161 born-v2 prompts across 25 skills (0 fidelity-low)") | `git log --follow -- skills/deliberate/SKILL.md` | VERIFIED |
| 3 | `skills/deliberate/SKILL.md` is 9,005 bytes and contains the Anti-Patterns section quoted in genius.md (lines 129-136 at read time) | Direct `Read` of file + `wc -c` | VERIFIED |
| 4 | `skills/deliberate/genius.md` was 6,626 bytes before this repair (baseline, pre-edit) | `wc -c` at start of repair | VERIFIED |
| 5 | `.agent/workflows/deliberate.md` is 8,188 bytes and contains the Anti-Patterns (workflow FAIL) section quoted in genius.md (lines 195-202 at read time) | Direct `Read` of file + `wc -c` | VERIFIED |
| 6 | `skills/deliberate/references/prompts-v2/deliberation-synthesis.md` is 11,397 bytes, frontmatter records `forged: born-v2`, `refactored: 2026-07-13` | Direct `Read` of file + `wc -c` | VERIFIED |
| 7 | `execution/deliberate.py` exists (5,774 bytes) and is the Gemini voice executor referenced by SKILL.md Step 3 | `ls -la` + file present | VERIFIED (existence + size); interior logic not fully re-audited this pass — file was located and confirmed present, not opened line-by-line beyond confirming it's the referenced script |
| 8 | `execution/anchor_memory.py` exists (23,314 bytes) and implements the `anchor` subcommand referenced by SKILL.md Step 5 | `ls -la` | VERIFIED (existence + size only, same caveat as row 7) |
| 9 | `execution/gemini_client.py` (18,566 bytes, last modified 2026-03-08 — predates the skill by ~2.5 months) is "the underlying Gemini API client" per SKILL.md's See Also | `ls -la` timestamp + size | LIKELY — file exists, name and age are consistent with the claim, but this repair pass did not trace the import chain inside `execution/deliberate.py` to confirm it actually calls into this file rather than duplicating logic |
| 10 | Perplexity ships a "model council" feature that auto-synthesizes multiple models into one opaque answer | `skills/deliberate/SKILL.md` line 19 and `skills/deliberate/genius.md` line 20, both self-hedge with "(as best we can infer)" | UNCONFIRMED — the skill's own authors flag this as inference, not a verified read of Perplexity's product docs; this repair pass did not check Perplexity's actual feature set (out of scope: it's the original author's framing, not a new claim introduced here) |
| 11 | `evolution_store/v2_traces/trace_20260525_081832_deliberate.json` (1,067 bytes) is evidence of a real production `/deliberate` run | Direct `Read` of the trace file | UNCONFIRMED as usage proof — the trace's own `notes` field reads "Backward compat smoke test", `expert` is literally `"test-expert"`, and `factual_grounding` is `0.0`; this is a schema-compatibility test artifact, not a real deliberation. Recorded here so a future pass doesn't cite it as usage evidence. |
| 12 | No `docs/solutions/` card documents a `/deliberate`-specific solved problem | `grep -rl "deliberate" docs/solutions/` returned 2 files; both hits read and confirmed incidental (the word "deliberately" in one, an unrelated `/assemble` system's "Deliberate" phase name in the other) | VERIFIED absence — grep executed and both hits manually inspected, not assumed |
| 13 | No `extractions/` entry matches "deliberate" (this is a method skill, not a person extraction) | `ls extractions/ \| grep -i deliberate` returned zero rows | VERIFIED absence — command executed directly |
| 14 | `skills/deliberate/workflows/` did not exist before this repair (zero workflow files, per the audit) | `find skills/deliberate -type f` at repair start returned only `SKILL.md`, `genius.md`, `references/prompts-v2/deliberation-synthesis.md` | VERIFIED |

## Notes on the two new/changed files this pass produced

- `genius.md` — two new sections added (`## How to Use This Skill (Model Calibration)`, `## Anti-Patterns (Sourced)`). All quoted material in both sections is copy-pasted verbatim from rows 3 and 5 above, not paraphrased or invented.
- `workflows/deliberate.md` — new file, additive port of `.agent/workflows/deliberate.md` (row 5) with `## Output Contract` and `## Quality Gate` sections appended, written specific to the Deliberation Block deliverable (not boilerplate — every bullet maps to a named failure mode already documented in the skill).
