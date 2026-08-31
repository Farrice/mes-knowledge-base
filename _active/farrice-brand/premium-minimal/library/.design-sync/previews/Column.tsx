import {
  Surface,
  Grid,
  Column,
  FunctionalLabel,
  Secondary,
} from '@farrice/premium-minimal';

export const SpanAndStart = () => (
  <Surface size="field-guide">
    <Grid gap={24}>
      <Column span={4}>
        <FunctionalLabel>Span 4</FunctionalLabel>
        <div style={{ height: 12 }} />
        <Secondary>Product truth a buyer can believe.</Secondary>
      </Column>
      <Column span={5} start={7}>
        <FunctionalLabel>Span 5, starting at 7</FunctionalLabel>
        <div style={{ height: 12 }} />
        <Secondary>
          The gap between them is deliberate, not leftover.
        </Secondary>
      </Column>
    </Grid>
  </Surface>
);

export const FullWidth = () => (
  <Surface size="field-guide">
    <Grid>
      <Column span={12}>
        <FunctionalLabel>Span 12</FunctionalLabel>
        <div style={{ height: 12 }} />
        <Secondary>
          One dominant idea per surface. A full-width column is the whole
          statement, not a container for three of them.
        </Secondary>
      </Column>
    </Grid>
  </Surface>
);
