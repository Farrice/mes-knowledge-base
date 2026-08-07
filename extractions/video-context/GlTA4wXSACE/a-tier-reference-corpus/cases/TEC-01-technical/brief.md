# Blind Brief TEC-01

## Communication Job

Create a 350-500 word internal engineering decision memo for the maintainer of `handoff_store.py`. The memo must make the failure mode, immediate operating safeguard, preferred repair, acceptance criteria, and current implementation status unmistakable.

Run the complete `/shaan-story-deploy` workflow. Return the finished asset followed by its Story Deployment Receipt.

## Audience and Attention

- Internal maintainer already familiar with `/end-session` and handoff persistence.
- Less than two minutes of attention.
- Domain/truth risk: technical and operational; wrong-context risk is high.
- Destination: internal decision memo.
- Voice owner: none; direct engineering prose.

## Incident Facts

- `/end-session` instructed operators to write a handoff into the shared OS temp directory and run `handoff_store.py save --from-temp`.
- `--from-temp` selected the newest `handoff-*.md` file by recency, regardless of which session created it.
- On 2026-07-25, the Jen Listings session wrote a handoff at 10:48. At 10:49, the `bc-arsenal-install` closeout consumed that file and saved Jen's body beneath valid BC frontmatter.
- The command reported success. The only visible clue was the `from-temp:` source path.
- Blast radius: `/resume bc-arsenal-install` could have loaded a well-formed but wrong-context handoff.
- Working safeguard: inspect `from-temp:` and verify the saved H1/body, not only exit status.
- Recovery worked by making the correct handoff unambiguously newest and re-saving to the same thread.
- Proposed repair was not built: prefer an explicit `--from <path>`; if `--from-temp` remains, filter by thread slug and refuse or loudly warn when identity does not match.

## Source Path

- `docs/solutions/2026-07-25-handoff-from-temp-cross-session-collision.md`.

## Truth Constraints

- Do not claim the guard or `--from` flag is implemented.
- Do not invent code, tests, filenames, affected sessions, additional incidents, or root causes beyond recency-only selection in a shared directory.
- Separate current workaround, proposed repair, and acceptance criteria.
- The memo should drive a decision; it is not an incident story or postmortem narrative.
