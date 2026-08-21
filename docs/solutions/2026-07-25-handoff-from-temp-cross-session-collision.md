---
date: 2026-07-25
session: bc-arsenal-install closeout
name: handoff-from-temp-cross-session-collision
problem_class: harness / handoff / recency collision
domain: harness
status: proven
problem_signature: "the closeout saved the handoff with from-temp and it silently picked up a sibling session's body, so resume hands the next session a confident, well-formed, completely wrong context filed under the right title"
tags: [handoff, end-session, concurrency, temp-dir, resume, collision]
---
# Solution Card — `handoff_store.py --from-temp` grabs a sibling session's handoff

**Date**: 2026-07-25 · **Domain**: system fix (handoff/resume loop) · **Status**: SOLVED (workaround; guard not built)

## Problem

`/end-session` Step 1 says to write the handoff to the OS temp dir, then persist with
`handoff_store.py save --from-temp`, which "auto-discovers the newest `handoff-*.md`" — described
in the workflow as removing "the main silent-failure mode."

It has its own silent-failure mode: **`--from-temp` picks the newest file in the shared OS temp
dir regardless of which session wrote it.** Two sessions closed out on 2026-07-25. The
`jen-listings` session wrote `handoff-jen-listings-moonseed-20260725.md` at 10:48. At 10:49 the
`bc-arsenal-install` close-out ran `--from-temp` and stapled **correct bc frontmatter onto the
jen-listings body**, writing it to `.agent/handoffs/2026-07-25-bc-arsenal-install.md` — and
overwriting the good bc handoff the finalize had already pinned there.

The output looked like success: `saved: .agent/handoffs/2026-07-25-bc-arsenal-install.md
[thread=bc-arsenal-install status=ready]`. Nothing in the confirmation reveals whose body it took.
Only the `from-temp:` line names the source file, and it's easy to skim past.

**Blast radius**: `/resume bc-arsenal-install` would have handed the next session Jen's Moonseed
shoot sheet under a Briar Cochran title. The wrong-context handoff is worse than a missing one,
because it reads as authoritative.

## Solution (what worked)

1. **Read the `from-temp:` line every time** — it names the file consumed. If the basename doesn't
   match this session's work, the save is wrong.
2. **Verify the body, not just the exit status**: `sed -n '9,12p' .agent/handoffs/<date>-<slug>.md`
   should show your session's H1.
3. **Recovery**: place the correct handoff in the OS temp dir so it is unambiguously newest, then
   re-save:
   ```bash
   cp <your-handoff>.md /var/folders/.../T/handoff-<slug>-<date>.md
   touch /var/folders/.../T/handoff-<slug>-<date>.md   # make it newest
   python execution/handoff_store.py save --from-temp --thread "<slug>" ... --pin
   ```
   Re-saving to the same thread overwrites cleanly; the sibling thread's own row is untouched
   (verified: `2026-07-25-jen-listings.md` still had its correct body).

## Prevention / next build (Forge Radar — not built)

`--from-temp` should filter by slug before falling back to newest: prefer
`handoff-*<thread-slug>*.md`, and refuse (or warn loudly) when the newest file's basename shares
no token with `--thread`. A `--from <path>` explicit flag would remove the guesswork entirely.
Tradeoff: one more argument to pass, against silently inheriting another session's context.
Not built this session (touching the handoff spine mid-closeout is the wrong time).

## Reusable lesson

**Auto-discovery by recency is unsafe in any directory more than one writer can reach.** The
convenience flag that "removes the silent-failure mode" introduced a worse one, because its
failure produces a confident, well-formed, wrong artifact. Any `--from-temp`-style affordance
needs an identity check (slug match), not just an ordering check (newest).

Related: `2026-07-25-social-intel-date-normalization-and-watch-url-parse.md` — same session, same
shape of bug (a convenience shortcut that silently produced wrong data instead of failing).
