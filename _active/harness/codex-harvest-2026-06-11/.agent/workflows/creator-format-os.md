---
description: Turn source material, raw thoughts, founder interviews, or brand problems into creator-to-brand format cards, content directions, and campaign briefs
---

# /creator-format-os - Creator-To-Brand Format OS

Use this command when a source, idea, client conversation, product, or brand problem should become reusable creator-native formats rather than a generic content plan.

This workflow extends `/farrice-content-os`, `/source-to-skill-system`, and `/extraction-governor-agent`. It uses the local playbook at `_active/farrice-content-os/04-deliverables/creator-to-brand-format-os.md` as the operating reference.

## Source Authority

Read only what is needed:

1. `_active/farrice-content-os/04-deliverables/creator-to-brand-format-os.md`
2. `extractions/video-context/flvU6sb9sg0/uncertainty-report.md` when referencing the Sweat Equity source
3. `extractions/video-context/flvU6sb9sg0/video-context-ledger.md` when timestamp proof is needed
4. `_active/farrice-content-os/context-index.md` and `FARRICE.md` when translating into Farrice voice
5. Existing relevant skills on demand only:
   - `skills/kallaway-content-system/SKILL.md`
   - `skills/kallaway-content-psychology/SKILL.md`
   - `/Users/farricecain/.codex/skills/tim-danilov-niche-bending/SKILL.md`
   - `/Users/farricecain/.codex/skills/jun-yuh-creator-vision/SKILL.md`
   - `/Users/farricecain/.codex/skills/grace-andrews-media-company/SKILL.md`
   - `/Users/farricecain/.codex/skills/alex-copper-creative-strategy/SKILL.md`

Do not load all expert files by default. Use the card library first, then pull the specific expert reference only if the output needs that lens.

## Modes

```text
/creator-format-os use [raw thought, source, draft, product, or problem]
/creator-format-os sprint --source [founder interview, client notes, or source package] --count 12
/creator-format-os brief --brand [brand/product] --audience [buyer] --format [card name]
/creator-format-os audit [draft, campaign, or content system]
```

## Operating Flow

1. **Ground the input.** Identify source evidence, user context, and uncertainty. If the input is the Sweat Equity video, use `extractions/video-context/flvU6sb9sg0/`.
2. **Pick the trust job.** Choose one: risk transfer, identification, insider reveal, trust transfer, guilt relief, proof contrast, routine, or format-market transplant.
3. **Select format cards.** Use one primary card and at most one modifier card from the 12-card library.
4. **Translate the domain.** Adapt for personal brand, consultant, SaaS, ecommerce, local service, education, AI content, or saturated market.
5. **Produce the artifact.** Return one of:
   - 3 content directions
   - 12-card content sprint
   - brand/creator brief
   - audit with revise/reject/ready verdict
6. **Gate the output.** Apply source fidelity, buyer relevance, Farrice voice, format fit, specificity, trust, AI ethics, and reuse gates.
7. **State the reuse hook.** Name what should be saved as a phrase, card, workflow, brief, offer asset, or content pack.

## Output Shapes

### Use Mode

```markdown
# Creator Format Directions

## Source Lock
- Input:
- Evidence or uncertainty:
- Audience:
- Business use:

## Directions
| Direction | Format card | Hook | Body spine | CTA | Quality gate |
|---|---|---|---|---|---|

## Best Move
- Use now:
- Reuse hook:
```

### Sprint Mode

```markdown
# Creator Format Sprint

## Source Lock
- Source:
- Offer/audience:
- Proof available:
- Limits:

## 12-Card Sprint
| # | Card | Trust job | Hook | Proof needed | CTA | Reuse |
|---|---|---|---|---|---|---|

## Batch Logic
- Format mix:
- First 3 to draft:
- Feedback metric:
```

### Brief Mode

```markdown
# Creator Brand Brief

## Brand Lock
- Brand/product:
- Audience:
- Desired action:
- Claims limits:

## Format Brief
- Card:
- Creator setup:
- Proof event:
- Script spine:
- Visual/action notes:
- Variants:
- Acceptance criteria:
```

## Quality Gate

Reject or revise before final if:

- source claims are not timestamped or labeled as unverified
- the format is decorative instead of creating a trust effect
- competitor callouts are unfair, defamatory, or unsupported
- AI-generated examples are passed off as observed reality
- the output could belong to any creator, founder, or brand
- no reusable phrase, card, brief, or offer asset is produced

## Bridge Notes

This is a lightweight command surface. It should not become a standalone mega-skill unless repeated use proves the card system needs its own deeper implementation package.

