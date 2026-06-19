# Automation Engine

## Use When
Set up the create → schedule → auto-DM backbone for an account (TweetHunter-class tooling, or any compliant scheduler + DM automation). This is the "secret cheat code" layer that makes volume + autopilot possible.

## Load First
- `../genius.md`
- `../references/scaling-mechanics.md`
- `../references/compliance-gate.md` (mandatory — automation is the highest-risk surface)
- `../references/post-anatomy.md`
- `09-comment-dm-conversion-system.md`

## Pre-Flight Gate
The auto-DM may ONLY fire on an explicit opt-in (the user liked/commented to ask for it). If the plan would DM cold or unsolicited users, stop — that is spam and a ToS violation. Confirm the platform's current automation rules before scaling.

## Steps
1. **Create layer**: batch-generate posts with the AI-gen prompt pack (`post-anatomy.md`). Insert the mandatory **human claim-edit gate** — every post checked against `compliance-gate.md` before it enters the queue.
2. **Schedule layer**: set cadence (N posts/day), build the queue, define autopilot windows (incl. off-hours).
3. **Convert layer**: map the auto-DM — opt-in trigger (like/comment keyword) → free asset/link; separate value lane vs. purchase lane DM.
4. **Compliance block** (mandatory): opt-in only, no cold mass-DM, opt-out honored, rate/ToS note, per-platform automation rules.
5. **Human escalation**: define when a person steps in — ready buyers, objections, high-ticket conversations.
6. **Measurement**: track qualified comments, DM→sale rate, per-post revenue; set a kill/keep rule for posts and accounts.

## Content Type Adaptations
| Surface | Automation note |
|---|---|
| X / Twitter | Scheduler + auto-DM on like/comment; the home surface |
| Instagram | Comment-to-DM tool (ManyChat-class); Story/link-sticker paths |
| Cross-platform | Each platform has its own automation rules — verify per `platform-playbooks.md` |

## Output Format
```markdown
## Create Plan (batch-gen + human claim-edit gate)
## Schedule Plan (cadence, queue, autopilot windows)
## Auto-DM Map (opt-in trigger → value lane / purchase lane)
## Compliance Block (opt-in only, opt-out, rate/ToS, per-platform)
## Human-Escalation Rules
## Metrics + Kill/Keep Rule
```

## Quality Gate
- Opt-in trigger is required before any DM; cold mass-DM is explicitly excluded.
- The human claim-edit gate exists between generation and scheduling.
- Opt-out path present; no guaranteed-income content auto-posts.
- Metrics + kill/keep rule defined; escalation to a human is specified.
