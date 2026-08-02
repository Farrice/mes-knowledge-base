# Workflow 01 — Flat-to-Cinematic Audit

**Produces:** a shot-level diagnosis of why a piece of AI video (or a board, or a single frame) reads flat,
with the specific fix for each defect and an explicit call on which defects are worth fixing.

**Use when:** something generated "looks AI," a client says "make it more cinematic," a reel is technically
clean but dead, or before committing a look to a whole piece.

**Load first:** `genius.md` — the flat-vs-cinematic axis section is the spine of this workflow.

> **Model-independent by design.** Nothing in this audit names a generator, and no finding here is fixed by
> switching models. Six of the eight causes are decided before or after generation. If the diagnosis you
> produce could be answered with "use a better model," you have diagnosed the wrong thing.
>
> **Provenance.** Clark never published a flat-vs-cinematic framework. The eight causes are assembled from his
> stated practice plus the observed signature of his own 2025 director reel. Every check carries a source tag.
> See `references/source-notes.md`. Do not present this as his named framework.

---

## Step 1 — Establish the intent before you judge the execution

You cannot diagnose flatness without knowing what the piece was trying to be. Get, or infer and state:

- **The one-sentence idea.** What is this about? If it can't be said, stop — that *is* the diagnosis
  (cause #8, and no lighting fix touches it). *"You still need to actually have an idea."* [FWAI 2023 @ 06:45]
- **The genre container.** Which grammar is it operating in, and does that grammar forgive or expose the
  artifacts present? (Pattern 15 — found footage makes artifact into texture.)
- **The delivery target.** Phone feed, pitch sizzle, broadcast, or platform QC. This sets how far down the
  chain the audit runs — edit survivability is irrelevant for a Reddit post and decisive for a Netflix deliverable.

## Step 2 — Run the eight-cause diagnostic, in order

Order matters: sorted by how often each is the *actual* cause. Stop escalating once you've found defects that
explain the flatness. A list of fourteen problems is not a diagnosis.

| # | Check | Ask | Fix (principle, not tool) |
|---|---|---|---|
| 1 | **Selection depth** | Does this look like a first take? Is there any evidence of choosing? | Rule of Five, then composite the take — mask the best element out of each generation into one plate. [EVERY 2024 @ 52:13, 54:08] |
| 2 | **Cut rhythm** | Time the clips. Are they all the same length? | Make duration an editorial variable: generate to be retimed, alternate long beats against quick cuts. [EVERY 2024 @ 17:22, 19:23] |
| 3 | **Light motivation** | Point at where the light is coming from. Can you? Is the face the brightest thing for no reason? Is there a real black point, or are the shadows lifted grey? | Respecify: one named source, its direction, whether it's behind or beside. Crush the blacks; allow the source to clip. [REEL-obs 2025]; [EVERY 2024 @ 27:43] |
| 4 | **Atmosphere** | Is there anything physically between camera and subject? | Put something in the air — mist, dust, smoke, rain, spray, embers. Depth is planes, not blur. [REEL-obs 2025] |
| 5 | **Capture layer** | Is it too clean to have been photographed? | One global grain/gate/handheld layer across the whole timeline, not per-shot. [FWAI 2023 @ 16:13]; [REEL-obs 2025] t=00:19 |
| 6 | **Coverage** | Do any two shots read as the same place? | Generate coverage pairs — the medium close-up *and* its wide, from one setup. [FWAI 2023 @ 15:57] |
| 7 | **Reference discipline** | Read the prompt back. Could it describe a thousand different images? | Replace adjectives with a named film **plus the mechanism underneath it** (Pattern 8). [EVERY 2024 @ 27:29] |
| 8 | **Stake** | Why does this exist? What is anyone supposed to feel? | Not a craft fix. Back to Step 1, or back to the script. [FWAI 2023 @ 06:45] |

Then, only if the delivery target requires it:

| | Check | Ask | Fix |
|---|---|---|---|
| 9 | **Drift** | Does the look or identity hold across the length? | Move whatever must persist outside the model: trained model, 3D scene, layer separation, locked plate. [FORBES26 2026] |
| 10 | **Edit survivability** | Will this sit beside live-action plates and clear QC? Bit depth, colour space, frame rate, resolution, gamma. | Match to the live-action spec — and note that none of these are recoverable after generation. [NFS 2025] |
| 11 | **Provenance** | Can you say where every frame came from? | Log prompts, settings and approvals as you go. *"A convincing image is not enough."* [FORBES26 2026] |

## Step 3 — Read it back the way he reads a take

Never render a verdict as a vibe. For each defect, name the **specific mechanical thing**, the way he does live:
*"I don't like that the light is kind of going out as we're going in"* [EVERY 2024 @ 57:36]. One named defect,
one mechanism, one fix. If you catch yourself writing "feels generic," you haven't finished diagnosing.

Do the same for what's working — *"I like this little leak back here going on, it's kind of cool cinematic"*
[EVERY 2024 @ 62:15]. An audit that only lists faults will get the good parts regenerated away.

## Step 4 — Triage: what to fix, and what to leave

Rank the defects by **cost of fix × effect on the read**. Be explicit that some are not worth fixing. The genre
container often makes a "defect" free (Pattern 15) — artifact inside found footage is texture, not damage.

State the **single highest-leverage fix** at the top. One thing, not seven.

**Execution prompt:** `references/prompts-v2/flat-to-cinematic-audit.md` — honor its Output Contract.

---

## Output shape

1. **Verdict** — one line. Flat / uneven / reads as film. Plus the single highest-leverage fix.
2. **Intent read** — idea, genre container, delivery target.
3. **Diagnostic table** — only the causes that actually fired, each with observed evidence and the fix.
4. **What's already working** — named as specifically as the faults, so it survives the next pass.
5. **Triage** — fix now / fix if budget / leave alone, with reasons.

## Quality gate

- [ ] Every defect names a specific observable, not a feeling
- [ ] Causes ordered by likelihood; the audit stopped once the flatness was explained
- [ ] At least one thing that's working is named as specifically as the faults
- [ ] The single highest-leverage fix is stated first and is genuinely single
- [ ] Delivery-target checks (9–11) run only when the target warrants them
- [ ] **No finding is answerable with "switch models."** If one is, it was mis-diagnosed
- [ ] No fabricated lighting ratios, f-stops, colour temperatures, LUTs or grading values — the corpus contains
      none, and inventing them is a fidelity failure
- [ ] No dependency on any mechanic from `genius.md` Appendix A (era-bound 2023–24 tool state)
