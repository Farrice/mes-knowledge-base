---
name: anchor-named-discipline
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: "--intent 8|--intent 9|--intent 10|--expert-score 8|--expert-score 9|--expert-score 10|--adversarial 8|--adversarial 9|--adversarial 10|expert_standard.*[89]\\.\\d|composite_score.*[89]\\.\\d"
  - field: transcript
    operator: not_contains
    pattern: "--anchor-named|anchor_named=True|anchor_named.*true|Anchor 9|Anchor 8|matches the Anchor"
---

**Anchor-Named Discipline**: A finalize call self-scored ≥8 on one or more dimensions but `--anchor-named` was not set AND no rubric anchor was named in the notes. Per the Bimodal Taste Profile in `evolution_store/ground_truth/rubric_v1.md`, any dimension ≥8 must cite the specific rubric anchor (Anchor 8 or Anchor 9) it matches.

The 8-must-be-earned rule (`execution/taste_signature.py` Rule 2) caps any 8+ dimension at 7.5 when `anchor_named=False`. This is intentional — if you can't name the anchor, the score reflects an aspiration, not a measurement.

Before ending this turn, EITHER:

1. **Re-finalize with anchor naming** if you can cite the anchor:
   ```bash
   python3 execution/chain_runner.py finalize "..." \
       --intent 8 --expert-score 9 --adversarial 8 \
       --anchor-named \
       --notes "Anchor 9 match on Expert Standard: <one-line reasoning>"
   ```

2. **Accept the cap silently** — the taste filter already enforced 7.5; no re-finalize needed. The hook is a reminder, not a block.

3. **Lower the self-scores** to honest 6-7 range and re-finalize.

The 2026-04-24 audit found 94-99% of finalize traces scored 8+. Wave 1+2 caps prevent that statistically — but only if `--anchor-named` is set honestly when claimed. Dishonesty here re-clusters the distribution above 8 and grade inflation creeps back in.

Background: `directives/quality_gate.md`, `evolution_store/ground_truth/rubric_v1.md` Bimodal Taste section, `execution/taste_signature.py`.
