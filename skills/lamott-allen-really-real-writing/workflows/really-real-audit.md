# /really-real-audit - False-Note Diagnosis

## Purpose
Diagnose where a draft feels false, shallow, performative, generic, confusing, or emotionally unearned.

## Inputs
- Draft
- Audience and medium
- Optional: the user's suspicion about what feels wrong

## Process
1. **Trust baseline:** describe what the piece is trying to make the reader believe or feel.
2. **False-note map:** flag lines under these labels:
   - Performative
   - Generic
   - Overproved
   - Abstract
   - Confusing
   - Emotionally unearned
   - Too heavy for medium
3. **Reader friction:** identify where the reader may stop, resist, or feel handled.
4. **Really real gap:** name the human truth the piece avoids.
5. **Music score:** score melody, rhythm, and harmony from 1-5.
6. **Repair order:** rank the top three changes by impact.

## Output
Return an audit table:

| Location | Weak Link | Source Mechanic | Fix Direction | Risk If Unfixed |
|---|---|---|---|---|

Then provide the highest-impact rewritten section.

## Quality Gate
The audit must be actionable. Do not diagnose with vague labels like "needs more emotion" unless you name the exact missing human pressure.
