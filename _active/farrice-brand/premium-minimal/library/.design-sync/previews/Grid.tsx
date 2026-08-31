import {
  Surface,
  Grid,
  Column,
  Display,
  Secondary,
  FunctionalLabel,
  DecisionLine,
} from '@farrice/premium-minimal';

export const TwelveColumns = () => (
  <Surface size="field-guide">
    <Grid gap={24}>
      <Column span={7}>
        <Display level={2}>
          Three ways to open the category.
        </Display>
      </Column>
      <Column span={4} start={9}>
        <Secondary>
          Each route trades reach against the proof you can actually stand
          behind.
        </Secondary>
      </Column>
    </Grid>
  </Surface>
);

export const OpenSpaceHeld = () => (
  <Surface size="field-guide">
    <Grid gap={36}>
      <Column span={5}>
        <FunctionalLabel>Field note</FunctionalLabel>
        <div style={{ height: 12 }} />
        <Secondary>
          The empty columns are the system. Position carries hierarchy;
          containers do not.
        </Secondary>
      </Column>
    </Grid>
    <div style={{ flex: 1 }} />
    <DecisionLine />
  </Surface>
);
