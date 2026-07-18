# AFK Overnight Mission-Runner (T1-only)

> Built 2026-07-18, Wave 7 Frontier Elevation Program. Lets `/go` Mission Cards
> execute unattended overnight without loosening any autonomy-tier gate from
> `directives/orchestration-doctrine.md`. Mechanism: `execution/mission_runner.py`.
> Fixture gate: `execution/verify_mission_runner.py` (5/5 PASS required before trusting a change).

## What runs

- `queue <card.md>` — copies a Mission Card into `.agent/mission-queue/pending/`.
- `run` — the nightly entry point. Claims `execution/session_lock.py` (abort loudly,
  touch nothing, if a fresh foreign lock is held). For each pending card: parses its
  declared `Tier:` line. **Only Tier T1 cards execute** — headless
  `claude -p "<card body>" --permission-mode acceptEdits`, stdout captured to
  `.agent/mission-queue/done/<card>-transcript.md`, card moved alongside it. Lock is
  released in a `finally` block — a crash never leaves the tree bricked.
- `status` — lists pending/parked/done with parsed tier per card.
- `receipt` — writes `.agent/cos/overnight-receipt-<date>.md`: outcomes, transcript
  paths, parked cards + reasons, a token/cost line (honest "not available" today —
  see Phase 2), and the drafts-only disclaimer.

## What NEVER runs

- **Tier T2 or T3 cards.** Moved to `.agent/mission-queue/parked/` with the card body
  UNTOUCHED, plus a `<card>.reason.txt` explaining the tier. They wait for Farrice's
  nod like any other T2/T3 work per the doctrine's Blast-Radius Autonomy Tiers.
- **Anything that publishes, sends, posts, pays, or deploys** — a regex refusal net
  (`publish|send|post to|payment|purchase|deploy`, case-insensitive) parks the card
  with a matched-pattern reason regardless of its declared tier. A mis-tiered T1 card
  is not an excuse to take an outward or financial action while nobody is watching.
- Anything outside `.agent/mission-queue/` and whatever the T1 card's own scope
  touches — the runner does not decide WHAT a T1 mission does, only whether it's safe
  to run headless. Bad mission content is still the conductor's problem, not this
  gate's.

## Where drafts land

- Executed cards + transcripts: `.agent/mission-queue/done/`.
- Parked cards + reasons: `.agent/mission-queue/parked/` (card untouched, reason in
  a sibling `.reason.txt`).
- Any files the T1 mission itself created/edited land wherever that mission's own
  intent pointed — the transcript is the pointer; there is no separate manifest.

## Morning receipt

`.agent/cos/overnight-receipt-<date>.md`, written by `mission_runner.py receipt`
(run it manually, or wire it as the first step of the morning COS brief). Lists every
executed and parked card with its outcome/reason, and closes with the drafts-only
disclaimer: nothing in an overnight run publishes, sends, deploys, or spends —
those actions are always parked for a human.

## Install (documented, not executed — Farrice's call)

```bash
cp "launchd/com.antigravity.mission-runner.plist" ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.antigravity.mission-runner.plist
```

Matches the `com.antigravity.evolution-auto` pattern (same `.venv/bin/python3`
invocation, `StartCalendarInterval`, repo-root `WorkingDirectory`) — scheduled
nightly at 02:30. Uninstall: `launchctl unload ~/Library/LaunchAgents/com.antigravity.mission-runner.plist`.

## Phase 2 — NOT built yet

- **Google Drive sync of overnight drafts.** Next step is wiring `gws` CLI
  (`directives/` has the auth pattern already used by other jobs) to mirror
  `.agent/mission-queue/done/` into a Drive folder each morning so drafts are
  reachable off-machine. Documented as the obvious next step; no code for it exists.
- **Cost/token metadata** — today's transcripts are plain stdout text. Getting a real
  cost line into the receipt means switching the `claude -p` invocation to
  `--output-format json` and parsing usage out of it; deferred until cost visibility
  is worth that plumbing change.
