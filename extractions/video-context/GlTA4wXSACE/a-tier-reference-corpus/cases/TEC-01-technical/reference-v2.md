# Held-Out Reference V2 TEC-01

## Expected Behavior

- **Decision:** `NO STORY`.
- **Why:** This is an identity-sensitive engineering decision memo. Direct explanation keeps the failure, safeguard, repair, and acceptance criteria unmistakable.
- **Owner:** Direct engineering decision-memo owner.
- **Must preserve:** Exact collision, blast radius, current safeguard and recovery, preferred explicit-path repair, thread-identity behavior, acceptance criteria, and unbuilt status.
- **Must reject:** Dramatic chronology, blame, invented implementation details, passing-test claims, or a generalized systems essay.

## Reference Asset

**Decision memo: make handoff source identity explicit**

**Decision.** Make an explicit source path the preferred input for closeout persistence:

`handoff_store.py save --from <exact-path> --thread <thread-slug> ...`

This is a proposed repair, not current behavior. The identity guard and explicit `--from` mode have not been built.

**Failure mode and blast radius.** `handoff_store.py save --from-temp` selects the newest `handoff-*.md` file in a shared OS temp directory. Selection is based on recency, regardless of which session created the file. On 2026-07-25, the Jen Listings session wrote a handoff at 10:48. At 10:49, the `bc-arsenal-install` closeout consumed that file and saved Jen’s body beneath valid BC frontmatter. The command reported success; the only visible clue was the `from-temp:` source path. The resulting stored handoff was structurally credible but contextually wrong. The direct blast radius was that `/resume bc-arsenal-install` could have loaded a well-formed Jen Listings body as authoritative BC context.

**Current operating safeguard and recovery.** Until a code repair exists, inspect the `from-temp:` line after every `--from-temp` save and confirm that the selected source belongs to the active thread. Then inspect the persisted H1 and body; a successful exit and valid destination frontmatter are insufficient proof. If the source is wrong, make the correct handoff unambiguously newest and re-save it to the same thread. That recovery worked for this collision, but it remains an operator workaround and does not remove the cross-session race.

**Preferred repair and thread-identity behavior.** Closeout should pass the exact intended handoff with `--from <path>`. If `--from-temp` remains, it should filter candidates by the normalized active thread slug before applying recency. A missing identity match should refuse the save, or at minimum emit a loud mismatch warning that requires an explicit override. The confirmation should name the exact selected source, and persistence should verify body identity rather than trusting destination metadata. Recency may choose only among candidates already matched to the active thread; it must not stand in for identity.

**Acceptance criteria.**

- Two temp handoffs from different threads can coexist without cross-selection.
- A mismatched or unmatched thread identity fails closed or requires an explicit override.
- Every confirmation prominently names the exact source file.
- The persisted H1/body is checked against the intended thread identity.
- Re-saving one thread does not alter the sibling thread’s stored handoff.
- Explicit-path saves and ordinary single-session use continue to work.

**Status.** The workaround and successful recovery are known. The proposed explicit-path mode, identity guard, and regression coverage are unbuilt; no implementation or passing test is claimed.

## Reference Receipt

- **Narrative decision:** `NO STORY`.
- **Primary job:** Engineering decision support and identity-safe operating instruction.
- **Selected mechanic:** None; direct hierarchy and plain-language compression only.
- **Production owner:** Direct engineering decision-memo owner.
- **Truth boundary:** Current behavior, working workaround, recovery, proposed repair, and acceptance criteria remain separate.
- **Implementation status:** Unbuilt; no code or test result is claimed.
- **Reference Asset body word count:** 414 words.
