# Doc Format Research — How Operators Format Client-Facing Action Documents

Scope: format only. Every fact in the rebuilt Cooz package still traces to `06-market-truth/` — nothing new here. Question answered: what structural moves make a document readable-and-actionable in one pass, and what does that imply for 00-playbook + 5 action docs + Receipts.

## Structural Principles

**1. One document, one pause point.** Gawande's surgical checklists exist for a defined moment in real work, not a manual read beforehand — after 60-90 seconds at a pause point the checklist becomes a distraction. [LIKELY — secondary summary of *The Checklist Manifesto*, runn.io] **Implies:** each action doc = one sitting, one decision. Needs two pause points → two docs.

**2. Checklists cap at 5-9 items, killer steps only.** Gawande's rule: keep only steps "most dangerous to skip." Even the thorough WHO surgical checklist ran 19 checks split across three separate pause points, never one long list. [LIKELY] **Implies:** no card exceeds ~7 checkboxes; longer means it's really two cards.

**3. DO-CONFIRM vs. READ-DO — pick one, say which.** Gawande's two checklist types: read-do (read then act) vs. do-confirm (act from memory, then verify). [LIKELY] **Implies:** every Cooz card is read-do by default — new territory for him, so he reads then acts.

**4. Job aids lead with verbs and use one visual system, not decoration.** ID sources agree job aids exist for in-the-moment performance support (not training); steps open with strong verbs (identify, submit, review); the same icon/checkbox logic repeats across every aid. [LIKELY — corroborated across TechSmith, Venngage, 24/7 Teach, San Diego Online] **Implies:** every HOW line starts with an imperative verb; identical visual grammar across all 5 docs and the 00-playbook.

**5. The headline states the conclusion, not the topic.** McKinsey's "action title" convention (Minto's Pyramid Principle): the header is the takeaway — "Cut cost 20% by optimizing the supply chain," not "Supply Chain Optimization" — so header-only reading still gets the argument. [LIKELY — slideworks.io] **Implies:** WHAT lines are instructions, never category labels. "Booking page" banned; "Fix the /briefing link before you print flyers" is the header.

**6. Progressive disclosure: small core layer by default, rest on request.** Nielsen's 1995 concept, still NN/g doctrine: show the smallest control set needed by default; move lower-frequency, harder material to a layer opened on purpose. [LIKELY — concept corroborated via IxDF/UXPin; primary NN/g page not directly quoted] **Implies:** card face = core layer, capped at four fields. Receipts folder = the on-request layer, one link out, never inline.

**7. Job aids match the tool to real task friction, including real time.** ID sources define job aids as usable without prior training, meaning they must reflect actual time/skill gaps, not idealized ones. [LIKELY] **Implies:** honest effort labeling isn't a courtesy add-on — it's what separates a job aid from a training doc pretending to be one.

**8. Ramit Sethi's action-guide format — UNCONFIRMED.** Search surfaced reputation ("extremely detailed, sequenced") but no primary structural breakdown. Flagging rather than inventing one. If it matters later: pull an actual IWT workbook PDF and extract structure directly.

**9. "Champagne tower" architecture — UNCONFIRMED.** No established source under this name for document depth-layering. Appears to be informal shorthand for what #5 and #6 already verify. Not counted as a distinct, separately-sourced principle.

## Proposed Spec

**Card anatomy — Farrice's WHAT/WHY/HOW/DONE-WHEN, validated, one addition.** All four fields map directly to principles 5, 1, 4, and 3+1. One change: fold the effort tag into the HOW header instead of a fifth field — `HOW (15 min)` or `HOW (45 min — needs Squarespace login)` — keeping the card at four fields per principle 6.

```
### [Bold imperative WHAT — the conclusion, not a topic]
WHY: [one sentence — the stake if this doesn't happen]
HOW (time + who):
  [ ] step 1 (verb-led)
  [ ] step 2
  [ ] step 3  (max ~7; split into two cards past that)
DONE-WHEN: [visible, binary proof — not a feeling]
Go deeper: [link to one receipt section, not a whole doc]
```

**Doc skeleton.** `00-MASTER-PLAYBOOK.md` = the pyramid apex: one line stating the single highest-leverage move, then all 5 action docs listed as one-line WHAT entries linking down. Each action doc = one pause point, 1-3 cards max. `06-market-truth/` stays untouched as Receipts — expert layer, never inline in a card.

**Depth-layering mechanism.** Three layers per principle 6: Core (card face, always visible) → On-request (one "Go deeper" link per card to a specific receipt section) → Expert (the Receipts folder, for defending a decision to himself or a client — never required to finish a checklist). Receipts are ammunition, not a dependency.

**Honest effort labeling.** Every HOW header carries a real, scoped time/effort tag pulled from the actual task, naming anyone else involved. A 45-minute step says 45 minutes — rounding down to look easier breaks the trust the receipts exist to protect.
