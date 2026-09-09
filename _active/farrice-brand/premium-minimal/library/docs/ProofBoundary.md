---
category: Decision
---

# ProofBoundary

Aligned fields separated by rules, stating what the supplied proof actually supports.

Status is carried by wording and by weight — **never by warning colour, shield, check mark, badge, or any other compliance theatre**. The honest boundary is the point.

Three statuses: `supported`, `qualified` (renders "Qualified review"), `outside` (renders "Outside supplied proof").

Two or three fields. More than three stops being a boundary and becomes a table.

```jsx
<ProofBoundary
  fields={[
    { status: 'supported', claim: 'Repeat purchase rate of 38% across twelve months.' },
    { status: 'qualified', claim: 'Absorption advantage, pending the third-party panel.' },
    { status: 'outside', claim: 'Any claim about sleep quality.' },
  ]}
/>
```
