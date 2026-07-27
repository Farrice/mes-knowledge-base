# Solution Card — A dated promise needs a tickler, not a note in a living doc

**Date:** 2026-07-27
**Domain:** system / COS
**Trigger phrase:** "note for [future date]", "be mindful when", "you might forget", "remind me on"

## The problem

Farrice promised JJ a spin top at the next dentist visit (2026-08-31) and said
in the same breath: *"You might forget."* The capture path available at the time
wrote it into `.agent/cos/life-context.md § JJ` as a prose note reading
"**Note for 08-31:** he expressed interest in a spin top; be mindful."

That note is only as good as a future model happening to read that section on
the right morning and noticing the date. It is AI-memory-dependent
observability — the exact pattern the standing rule
`feedback_ai-memory-dependent-observability` bans, applied to a promise made to
a two-year-old.

Root gap: the system had **no dated-reminder mechanism at all**. Grep across
`execution/`, `.agent/`, `directives/` for `remind|tickler|calendar|upcoming`
returned nothing, and none of the 17 antigravity launchd agents covered it.
Everything time-based in the system was *recurring* (daily prep, weekly distill,
nightly mirror); nothing was *one-shot on a future date*.

## The fix

`execution/cos_reminders.py` — stdlib-only dated tickler.

- Store: `.agent/cos/reminders.jsonl`, one object per line
  (`id`, `date`, `lead_days`, `text`, `source`, `done`).
- `render_reminders()` returns brief lines when a reminder's window is open:
  `date - lead_days  ..  date + 7`. Empty list otherwise, so the brief never
  pads with an empty header.
- The **grace tail is the important half**: a reminder you blew past keeps
  nagging for 7 days instead of vanishing the morning after, which is the
  failure mode that makes calendar reminders useless for things you actually
  need to do.
- Corrupt JSONL lines are skipped, never raised — a bad line must not break the
  morning brief.
- Wired into `execution/cos_prep.py` with one import and one
  `lines.extend(render_reminders())` above the world-pulse section.

CLI: `add --date --text [--lead-days] [--source]` · `list [--all]` · `due` ·
`done <id>`.

## Proof (in-session)

```
$ cos_reminders.py add --date 2026-08-31 --lead-days 3 --text "JJ's dentist ..."
added 93263c48325d — surfaces 3d before 2026-08-31
$ cos_reminders.py due
nothing in window                       # correct — today is 07-27
$ render_reminders(on=2026-08-29)  →    # fires, "(in 2d)"
$ render_reminders(on=2026-09-02)  →    # still fires, "(2d ago, still open)"
```

## The transferable rule

**A promise with a calendar date belongs in a tickler, not in prose.** When a
capture surfaces a specific future date — a follow-up, an appointment, a
renewal, a "check back in 30 days" — write the dated entry. The living-doc note
is the *context*; the tickler is the *trigger*. Keep both; never let the note be
the only one.

## Related

- [[feedback_ai-memory-dependent-observability]] — the rule this implements
- [[project_chief-of-staff-os]] — the brief this surfaces in
- [[project_system-health-loop]] — same principle, system-health flavor
