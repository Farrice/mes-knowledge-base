---
category: Decision
---

# RouteSet

Three parallel strokes that compare real choices.

Routes are differentiated by **number, position, and stroke weight — never by colour**. The recommended route gets the 6px stroke; the others stay quiet at 1–2px.

Three is the grammar. Two reads as a false binary; four dilutes the decision.

Use this motif only when the content genuinely compares options. A route set with nothing to choose between is decoration, and the contract forbids it.

```jsx
<RouteSet
  recommended={1}
  routes={[
    { index: '01', label: 'Lead with the clinical dose', note: 'Slowest to land, hardest to argue with.' },
    { index: '02', label: 'Lead with the reorder rate', note: 'Proof they already own. Fastest route to trust.' },
    { index: '03', label: 'Lead with the founder', note: 'Cheapest to make, weakest at scale.' },
  ]}
/>
```
