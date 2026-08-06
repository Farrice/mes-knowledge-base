---
date: 2026-08-06
session: forsyth-enchantment-os
tier: operator-guide
status: enriched
---

# The Enchantment OS — What We Built 2026-08-06 and How to Use It

> This session forged Mark Forsyth from his brand-new second Perell interview (plus a re-extraction of the
> 2024 original), taking `skills/mark-forsyth-rhetoric` from 3 to 16 workflows and shipping `/enchant` — a
> single-author writing OS that composes whole pieces, not just repairs lines. Companion files: the method
> lives in `skills/mark-forsyth-rhetoric/genius.md`, the working cheat sheet in
> `references/figure-catalog.md`, and the boundaries against every other writing front door in
> `references/lane-contract.md` (binding). Sources are retained at `extractions/mark-forsyth/`.

## ⚡ If you only read 10 lines

1. **`/enchant compose`** writes a whole piece end-to-end in Forsyth's method. **`/enchant elevate`** treats
   an existing draft's line, sound and voice. One author throughout — no other expert co-writes.
2. **The misquote test is the diagnostic**: would someone who heard a flat paraphrase *correct it into* your
   line? If not, the line has no shape. That is falsifiable, and it is the whole method in one question.
3. **The announcer rule is the governor** and it *subtracts*: 2–4 ornamented moments per piece, plain prose
   between. Ornament spread evenly is ornament wasted.
4. **Classify the job first.** Dishwasher manual → be laconic and stop. Meant to be kept → full method.
   An INSTRUCTION verdict ends the run; that is a feature.
5. **The ornament ceiling is deliberately unresolved.** `/enchant` stages **two takes** (full-ornament vs
   gate-clean) and your verdict banks to `.agent/jam/taste-ledger.jsonl`. **No default until ~10 verdicts.**
6. Inside `/enchant` only: `prose_classifier` reports and never blocks; density and low-cognitive-load rules
   suspend. **Factual veto, cost gate and compliance language never suspend.**
7. **Never run `/enchant` and `/how-i-write` Layer 5 on the same passage.** Same for Forsyth and Farnsworth
   in `/writers-room`. Double-picked lane; the 2026-06-22 bake-off already priced it at 3/10.
8. **Farnsworth when the line must land as a punch. Forsyth when it must be repeated.**
9. Blind pass is **B+, not A** — it passed on retry after v1 failed the recognition test on an instructional
   close. Heartbeat 7/7. Merged to main at `fd6ebf817` and verified fireable.
10. **First thing to run:** `/enchant elevate` on the LinkedIn profile copy —
    `_active/linkedin-launch/03-launch/2026-07-30-LINKEDIN-PROFILE-COPY-PASTE-MASTER.md`.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/enchant compose` | A finished piece, single-author, end-to-end | You need the whole thing written and it must be *remembered* |
| `/enchant elevate` | An existing draft's line/sound/voice layer treated | The draft is clear, competent, and nobody will quote a line of it |
| `/mark-forsyth` | Expert front door — persona + full arsenal | You want the tier menu rather than a specific move |
| `/mark-forsyth-classify-the-job` | INSTRUCTION vs MEMORY verdict + ornament licence | Before anything else. Unrecoverable if wrong |
| `/mark-forsyth-enchantment-audit` | 7 falsifiable tests, ONE highest-leverage finding | Diagnosis only, before committing to a treatment pass |
| `/mark-forsyth-announcer-map` | Whole-piece ornament plan **and a cut list** | Deciding where the voice rises. This one subtracts |
| `/mark-forsyth-repetition-forge` | Sandwich · Drumbeat · Landing · Staircase · Shape-Shift | The idea turns on one word, a chain, or a build |
| `/mark-forsyth-symmetry-forge` | Mirror · Even Scales · Rule of Three · Full Sweep | One thing weighed against another, or the point is totality |
| `/mark-forsyth-sensory-transfer` | Sense-Jump · Dressed Abstraction · Overshoot · Impossible Thing | Something abstract or enormous will not land |
| `/mark-forsyth-paradox-forge` | Koan · Double Meaning · Counterintuitive Proof | A truth will be resisted or skimmed past |
| `/mark-forsyth-rhythm-and-sound` | Alliteration, metre, the Fist, the Long Hold | **The facts are locked** and only form can change |
| `/mark-forsyth-run-up-rewrite` | A dead passage deleted and rewritten whole | Prose is technically fine and rhythmically dead |
| `/mark-forsyth-pull-through-architecture` | Section units that offer the exit and make it unattractive | Readers stop mid-piece and don't come back |
| `/mark-forsyth-word-world-wedge` | Texture vocabulary + connotation date-check | Period work, niche voice, ICP language |

`write-to-enchant` and `figure-diagnostic` have no standalone shims — the minter judged both reachable
through `/enchant`, which is correct: they are its two halves.

## The mental model

**Three ideas make everything else obvious.**

**1. Memorable language is formula, and the proof is falsified memory.** "Fly, my pretties, fly!" is not in
*The Wizard of Oz*. Churchill said "blood, toil, tears and sweat," and the world corrected him to "blood,
sweat and tears." The figures are strong enough that **we change what we heard — and change history — to get
a nice memorable phrase.** That gives you a test instead of an opinion: the misquote test.

**2. The reason to write well is enchantment, not transmission.** *"Don't write just to be efficient and get
the meaning across. Write to enchant."* Writing for efficiency is like dressing for efficiency — everyone in
high-visibility waterproof trousers. And the etymology closes it: a *grammar* was something written down; a
*glamour* was a spell you cast to carry someone off. Same word. *Spelling*, *spell*.

**3. You cannot grip a reader continuously, so ornament must be rationed.** A compilation of the best bass
drops with none of the buildups is horrible to listen to. The flat prose is what makes the loud passages
audible. This is why the announcer map is a *subtracting* workflow and why "flat everywhere" and "loud
everywhere" are both diagnoses.

## The Enchantment OS (`/enchant`)

**What it is.** A single-author front door owning no craft of its own — it classifies, sequences and gates,
and every move belongs to a workflow inside the skill. `compose` runs occasion → prepare-aloud → establishing
shot → fast draft → announcer map → run-up edit → pull-through. `elevate` runs audit → announcer map →
figure diagnostic → forge → run-up rewrite.

**When to reach for it.** The piece must be *remembered*, not merely correct — and you want one voice
carrying the whole thing.

**When NOT to.** When the piece needs several specialists at different altitudes: that is `/how-i-write`,
and running both on one passage is forbidden. When the structure or thesis is what's broken: `/enchant
elevate` treats lines and will stop and say so — route to `/depth-audit` → `/depth-inject`. When the job is
INSTRUCTION: Step 0 ends the run and offers the plain rewrite instead.

**How to invoke.**
```
/enchant compose   [objective + format + raw material]
/enchant elevate   [path to draft]
```
Load `_active/farrice-brand/voice/VOICE-CARD.md` as a layer first when the piece is in Farrice's or a
client's voice. Forsyth supplies shapes; the voice card supplies the person.

**Worked example.** The blind-pass generation for this session — a ~600-word Substack-length essay judged
against two unseen real Forsyth pieces. **v1 failed the recognition test**, and the tell was precise: it
ended on *"Your reader is that man. Give them something to hold."* Real Forsyth ends on a joke, not a lesson;
"Cutthroat Compounds" closes on an invented word and *"I accept that this has not caught on."* v2 fixed the
close, cited the OED by name, stacked a seven-item idiom burst matching his enumeration rhythm, and passed.
Both drafts are on disk at `extractions/mark-forsyth-rhetoric/blind-pass/`.

**Honest edges.** The blind pass is **B+, not A** — it needed a retry, and the residual gap is logged: v2 is
still tidier than his real rambling. The two-take contract has **zero verdicts banked**; until roughly ten
accumulate, there is no default and the system genuinely does not know your ornament ceiling. The
pure-vs-composed bake-off has not run. Codex `AGENTS.md` parity for `/enchant` is not done.

## The calibration contradiction (read before you argue with a take)

The two source interviews disagree, and the disagreement is preserved rather than averaged.

- **2024**, asked whether people overuse the figures: *"No, no, no, I don't. I've never seen somebody
  overusing the figures of rhetoric."*
- **2026**, asked when figures turn baroque: *"There's always going to be a limit where that was too many
  chilies and now you're ill. But those first few flakes of chili are always going to be good."*

**Reconciliation:** the ceiling is real; almost nobody is near it. The operating consequence is that in this
harness the live failure mode is **under-ornamentation** — our anti-slop instruments were tuned against
AI-median writing and will flag 2,500-year-old devices that Lincoln and JFK used on purpose. Hence the
two-take contract: rather than guess whose ceiling wins, `/enchant` measures yours.

## Composition table (options, never pipeline steps)

| Stack with | When it earns its cost |
|---|---|
| `/writers-room` | Whole-draft multi-lens treatment. Forsyth fires there as a **card**, never alongside Ward |
| `/high-taste-writing-os` | Its adversarial pass now carries the enchantment check (read-aloud + misquote) |
| `/voice-os` | The voice problem spans a body of work, not one opening |
| `ward-farnsworth-rhetorical-mastery` | The line needs a **punch** (register, end-weight) rather than a **shape** |
| `fact-verifier` | **Mandatory** whenever a treated piece carries real-world claims |
| `/jam` | The two-take verdict loop this OS already borrows; same ledger, same schema |

## Two repairs this session made in passing

- **The founding source defect is closed.** The pre-forge ledger recorded *"no raw source material exists for
  this expert in `extractions/`"* — the skill had been built from a transcript read once and discarded. Both
  interviews are now retained (22,367 words), and all ten prior patterns were re-checked against real text.
  All ten hold; nothing was overturned.
- **The phantom-lock bug is root-caused and fixed.** `.agent/session.lock` was tracked in git, so every
  `git worktree add` was born holding a stale lock from whichever session last committed it — and
  `session_lock.py claim` BLOCKED in a brand-new worktree no session was writing to. Now gitignored.

**Still open, flagged not fixed:** `wire_prompt_pointers.py --write` duplicates its managed block in skills
where that block is not last in the file (hit `skills/grace-liu` and `skills/fashion-coupids`; both reverted).
