---
category: Structure
---

# Grid

The twelve-column grid the contract requires on every surface.

Use alignment, rules, and whitespace before containers. Keep at least one third of the composition open — the open space is the system, not room left over.

```jsx
<Grid gap={36}>
  <Column span={7}>
    <Display level={2}>Three ways to open the category.</Display>
  </Column>
  <Column span={4} start={9}>
    <Secondary>Each route trades reach against proof.</Secondary>
  </Column>
</Grid>
```

`gap` takes values from the 12px spacing scale. `Column` takes `span` (of twelve) and an optional 1-indexed `start`.
