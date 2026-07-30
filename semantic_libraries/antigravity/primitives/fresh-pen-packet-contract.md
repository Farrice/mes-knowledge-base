# Fresh-Pen Packet Contract — session-as-pen primitive (born 2026-07-29)

**Source evidence (live-session harvest, not video):** the 2026-07-29 apex session. Four profile-copy renditions rejected (v3 ban-list brief · v4 expert-less · v5 single-workflow · v6 un-wargamed) from a session that had already run two system programs; the 9/10 About (Take A, locked) came from a CLEAN session running the five-move recipe. Verdict trail: `_active/farrice-brand/voice/calibration-log.md` rows 2026-07-29; packet instance: `.agent/missions/profile-copy-fresh-0730/portable.md`. Uncertainty limit: n=1 contrast (one bloated session vs one clean session) — the mechanism is doctrine-consistent (compromised-producing-context, CLAUDE.md Step 5.5) but not yet replicated; the 0730 run is the replication test.

## The principle
**A session is a pen.** Long system-heavy contexts write degraded taste-work: they optimize against the last complaint, skip routing, and lose the reader. The fix is never a fifth rendition — it is moving the mission to a clean context through a packet that carries everything EXCEPT the fatigue.

## Trigger (either, on a taste-bearing artifact)
1. Spiral brake fires: 2 rejected takes or 3+ renditions.
2. Operator says **"fresh pen"** (his vocabulary, OPERATOR-ROUTINE.md) on any heavy session.

## Packet REQUIRED fields (a thin packet reproduces the failure in a cleaner room)
| Field | Content |
|---|---|
| Mission sentence | one line, the artifact + the bar (name the felt exemplar, e.g. "to the Take A standard") |
| Recipe shape | the five-move recipe steps as they apply (inventory → receipts state → isolated wargame → felt standard → decisions-not-homework) |
| ROUTE order | exact skill/workflow paths to load BEFORE drafting — the #1 prior-session failure class |
| Verdict wall | every logged FAIL/RULE relevant to this artifact, verbatim-sourced from the calibration log |
| Proof inventory | verified facts/numbers/logos only; placeholders for private facts (asked as fill-ins at verdict time) |
| Locked list | what must not be touched or cannibalized |
| Negative reference | prior rejected versions by path, marked harvest-bones vs do-not-build-on |
| Ship steps | exact on-PASS actions (files, uploads, queue flips, verdict logging w/ mission slug) |

## Invocation
Compile: `/fresh-pen "<artifact>"` (workflow) → writes `.agent/missions/<slug>/portable.md` + mission `compiled` line.
Run: **new session** → `/go run the packet at .agent/missions/<slug>/portable.md`.

## Context policy (the agentic-engineering packet, condensed)
The packet is the ONLY context bridge — the fresh session must not inherit the parent transcript. Parent session stays integration owner of everything non-taste; the fresh session owns exactly one mission and closes it with the operator's felt verdict. Keep this primitive cold (loaded by /fresh-pen and /go, never hooked hot).

## Quality gate
Reject a packet missing the verdict wall or ROUTE order — those two fields are why the pattern exists. Reject invocation inside the same session ("fresh pen" in the same context is a rendition with extra steps).

## Behavior-changing proof
Instance `profile-copy-fresh-0730` compiled at the live brake (before this primitive existed — the primitive is its generalization). Proof completes when that mission closes with a felt verdict ≥ good; log the outcome here. PENDING as of 2026-07-29.

## Reuse hook
Any taste-bearing artifact class: profile copy, editions, offers, naming, client creative. Composes with `/raw-intent-bridge` (intent→packet for NEW work) — /fresh-pen is specifically the REJECTION-driven pen swap carrying accumulated verdicts.
