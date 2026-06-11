# Platform Fit Gate

## Role

Audit whether a selected hook survives the first visible platform window.

## Inputs

1. Selected hook.
2. Platform: LinkedIn, X/Threads, newsletter, short script, ad, carousel, landing page, or other.
3. Target topical terms.
4. Voice constraints.

## Deterministic Check

Use the local auditor when possible:

```bash
python3 execution/attention_hijack_hooks.py --hook "[hook]" --platform linkedin --terms "term1,term2,term3"
```

## Review Checks

| Check | Pass/Revise | Notes |
|---|---|---|
| First 40 to 50 words carry topic signal | | |
| Curiosity gap is explicit | | |
| Format matches payload | | |
| Mobile/fold estimate is acceptable | | |
| No throat clearing | | |
| Specific name, number, image, consequence, or claim appears | | |
| Voice does not sound templated | | |

## Output Schema

```markdown
## Platform Fit Gate

- **Verdict**: PASS / REVISE
- **Platform**:
- **Format**:
- **Best hook**:
- **Mechanical audit**:
- **Human judgment note**:
- **Revision if needed**:
```

## Quality Gate

If the hook fails mechanical fit but the idea is strong, revise the package. If the hook passes mechanics but has no payload, reject it.
