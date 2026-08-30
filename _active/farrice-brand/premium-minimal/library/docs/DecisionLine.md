---
category: Structure
---

# DecisionLine

A horizontal rule that establishes structure, and gets heavier only when it is making a recommendation.

This is the system's primary separator. Reach for it before a container, a card, or a background change.

| `weight` | Width | Use |
|---|---|---|
| `hairline` | 1px | Quiet structure — the default |
| `structural` | 2px | Separating real sections |
| `recommendation` | 6px | The line carrying a decision |

The 6px weight is the system's only emphasis move. Spend it on a decision or not at all.

```jsx
<DecisionLine />
<DecisionLine weight="recommendation" />
```
