# Provenance — andrew-dun-vibe-consulting repair

Anchor → source file + location. All source files were opened and read in full; sizes recorded via `wc -c` (bytes).

| Source | Path | Size (bytes) |
|---|---|---|
| Primary transcript | `extractions/andrew-dun/transcript.txt` | 87,837 |
| Internal amplification report (v2.0 origin) | `_active/codex-harvest-2026-06-11/brain/70d4034d-7603-456b-9b97-89bfe2613f97/artifacts/andrew-dun-amplification-report.md` | 14,691 |
| Internal v1 extraction (Revenue Architecture origin) | `_active/codex-harvest-2026-06-11/brain/70d4034d-7603-456b-9b97-89bfe2613f97/artifacts/andrew-dun-extraction.md` | 22,019 |

## genius.md — "How to Use This Skill (Model Calibration)" section (new)

Every craft claim in this section is anchored to a verbatim transcript quote already used elsewhere in genius.md (no new claims introduced):
- "no one cares" quote → `extractions/andrew-dun/transcript.txt` (verified substring match, see below)
- "I struggle to turn on my computer" → same file, opening minutes of the interview
- SDR ROI example ($166,400) → same file, matches genius.md's existing Hall of Fame Exemplar

## genius.md — Anti-Patterns section (7/7 now source-attributed)

| Bullet | Verbatim anchor | Confirmed via |
|---|---|---|
| Prescribe before diagnosis | "prescription uh without diagnosis is malpractice" | `python3` substring check against `transcript.txt` — True |
| Interview only executives | "operators know the road" / "executives show you know the destination" | substring check — True |
| Time savings without $ | "Time wasted times number of people times day per year times loaded hourly cost is the annual waste" | substring check — True |
| Lead with tool names | "people that say I build this really complex thing never make sales because no one cares, right? They just want to know what it's going to do for them" | substring check — True; cross-referenced against `workflows/05-diagnostic-presentation-architect.md`'s pre-existing "Non-Technical Language Rules" (unchanged, already in skill) |
| Skip change management gate | "a senior member who is what we would deem an AI champion" | substring check — True |
| Close before ROI proof | "these are what I like to call the springboard. This is how we jump up to those big swings" | substring check — True |
| Accept engagement w/o Champion | "position of power within the org" | substring check — True |

All 7 quotes were verified programmatically as exact substrings of `extractions/andrew-dun/transcript.txt` before being written — none were reconstructed from memory.

## references/source-ledger.md

Full claim inventory with VERIFIED (19 items, transcript-verbatim) / LIKELY (2 items, cross-artifact consistent but not a direct Dun quote) / UNCONFIRMED (5 items — the v2.0 "Research shows..." statistics: 65%/30% close rates, hourly-billing $50K cap, Success Fee Hybrid $40K figure, LinkedIn POC Teardown 45%/2-per-month stats, Readiness Scorecard 65-70%/$497 figures). The UNCONFIRMED items were traced to `andrew-dun-amplification-report.md`, which itself cites no external study — confirmed absent from the primary transcript by direct substring search (0 hits each for "65%", "30%", "$40K", "teardown", "497", "scorecard").

## Workflow Output Schema additions

Each Output Schema was derived directly from that workflow's own pre-existing "Produces" list and its numbered Steps (already-passing content) — no new deliverable structure was invented; each schema formalizes what the step-by-step templates already build toward. No external anchors needed beyond the workflow file itself, since these are structural/format requirements, not factual claims.

## genius.md epigraph consistency check

The skill's existing epigraph ("Prescription without diagnosis is malpractice") and SKILL.md's identical line were confirmed against the transcript's "prescription uh without diagnosis is malpractice" — the skill's phrasing quietly drops Dun's verbal filler ("uh"), which is standard cleanup, not an invented claim. Left unchanged (pre-existing, passing content).
