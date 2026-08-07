=== CASE TEC-01 ===

# Final Asset

## Decision Memo: Make Handoff Source Identity Explicit

**To:** Maintainer of `handoff_store.py`  
**Decision requested:** Implement and prefer explicit `--from <path>` selection. Retain `--from-temp` only if it filters by thread slug and refuses or loudly warns on an identity mismatch.

### Failure mode

`/end-session` instructed operators to place a handoff in the shared OS temp directory and run `handoff_store.py save --from-temp`. That option selects the newest `handoff-*.md` file by recency, regardless of which session created it.

On 2026-07-25, the Jen Listings session wrote a handoff at 10:48. At 10:49, the `bc-arsenal-install` closeout consumed that file and saved Jen’s body beneath valid BC frontmatter. The command reported success. The only visible clue was the `from-temp:` source path.

This creates a high-risk false-success condition: `/resume bc-arsenal-install` could load a well-formed handoff containing the wrong session context. Valid frontmatter and a successful exit status do not prove that the saved body belongs to the target thread.

### Immediate operating safeguard

Until the repair is implemented, inspect the reported `from-temp:` path for every save. Then inspect the saved handoff and verify that its H1 and body belong to the intended thread. Do not accept exit status alone as proof of a correct save.

Recovery in this incident worked by making the correct handoff unambiguously newest and re-saving it to the same thread. That is a manual recovery procedure, not a durable fix.

### Preferred repair

Add and prefer an explicit `--from <path>` option so the caller identifies the exact source file. If `--from-temp` remains available, constrain candidate selection by thread slug and refuse the save—or emit a prominent warning—when source identity does not match the target thread.

### Proposed acceptance criteria

- An explicit source path causes only that file to be consumed.
- A missing, invalid, or mismatched source fails closed rather than selecting another temp file.
- Retained `--from-temp` behavior considers only candidates matching the target thread slug.
- A thread-identity mismatch cannot report an unqualified success.
- Save output continues to expose the selected source path.
- A regression test recreates two cross-session handoffs ordered by recency and proves that the newer wrong-thread body cannot be saved beneath the target thread’s frontmatter.
- `/end-session` guidance prefers explicit source selection and retains the manual inspection safeguard until the repair is deployed.

### Current implementation status

The preferred repair is proposed but unbuilt. Neither `--from <path>` nor a thread-identity guard is claimed to exist. The current working safeguard remains manual inspection of the source path and saved H1/body.

# Story Deployment Receipt

**Narrative decision:** `NO STORY`

**Primary communication job:** Decision support for a technical and operational failure mode.

**Audience relationship:** Internal maintainer familiar with `/end-session` and handoff persistence; less than two minutes of attention.

**Evidence sufficiency:** The supplied brief contains the incident, mechanism, blast radius, workaround, recovery, proposed repair, and implementation status needed for a direct memo. It does not supply current code evidence or proof of an implemented repair.

**Why this dosage:** The task is an internal engineering decision memo about an incident, safeguard, specification change, acceptance criteria, and status. Narrative treatment would add attention cost without improving the decision.

**Rejected dosage alternatives:**

- `FULL STORY`: Rejected because transformation, identity, and a protagonist arc are not the communication job. A dramatic incident narrative would obscure the required technical distinctions.
- `STORY FRAGMENT`: Rejected because the incident facts already function as direct operational evidence. Recasting them as an anecdotal fragment could weaken the hierarchy or imply that one incident alone proves more than the supplied failure mechanism.

**Selected story mechanic:** `NONE`

**Permitted editorial treatment:** Hierarchy and plain-language compression.

**Production owner:** Direct engineering decision memo owner.

**Factual boundary:**

- All incident details are brief-supplied facts.
- The supplied source path is a traceability pointer; it was not opened.
- No code, test, filename, additional incident, affected session, or root cause was added as an existing fact.
- Proposed acceptance criteria describe required future behavior; they do not claim that behavior or its tests currently exist.

**Facts preserved:**

- Recency-only selection from a shared temp directory.
- Jen Listings handoff written at 10:48 on 2026-07-25.
- `bc-arsenal-install` consumed it at 10:49.
- Jen’s body was saved beneath valid BC frontmatter.
- The command reported success; `from-temp:` was the only visible clue.
- `/resume bc-arsenal-install` could have loaded a well-formed wrong-context handoff.
- The working safeguard is source-path and saved H1/body inspection.
- Recovery used an unambiguously newest correct handoff and re-saved the same thread.
- Explicit `--from <path>` is preferred but unbuilt.
- Any retained `--from-temp` should filter by thread slug and refuse or loudly warn on identity mismatch.

**Truth constraints applied:** No invented chronology, code, tests, outcomes, motives, or additional causes. Current workaround, proposed repair, acceptance criteria, and implementation status remain separate.

**Exit condition:** The maintainer can identify the failure, follow the current safeguard, decide on the preferred repair, and evaluate future implementation against explicit acceptance criteria without mistaking proposed behavior for deployed behavior.

## CONTEXT READ

1. `skills/shaan-puri-storytelling/SKILL.md`
2. `skills/shaan-puri-storytelling/references/story-deployment-map.md`
3. `skills/shaan-puri-storytelling/workflows/shaan-story-deploy.md`
4. `skills/shaan-puri-storytelling/references/prompts-v2/shaan-story-deploy.md`
5. `extractions/video-context/GlTA4wXSACE/a-tier-reference-corpus/cases/TEC-01-technical/brief.md`

=== END TEC-01 ===
