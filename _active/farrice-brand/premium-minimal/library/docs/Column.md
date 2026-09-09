---
category: Structure
---

# Column

A cell inside [Grid](./Grid.md). `span` is how many of the twelve columns it occupies; `start` is the 1-indexed column it begins on.

Leaving a column empty is a legitimate move here — it is how the one-third open-space rule gets met.

```jsx
<Grid gap={24}>
  <Column span={5}>
    <FunctionalLabel>Field note</FunctionalLabel>
  </Column>
  <Column span={6} start={7}>
    <Secondary>Position carries the hierarchy. Containers do not.</Secondary>
  </Column>
</Grid>
```
