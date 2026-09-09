import { Surface, Display, Secondary } from '@farrice/premium-minimal';

export const LevelOne = () => (
  <Surface size="field-guide">
    <div style={{ flex: 1 }} />
    <Display level={1}>I don't make weak products louder.</Display>
  </Surface>
);

export const LevelTwo = () => (
  <Surface size="field-guide">
    <div style={{ flex: 1 }} />
    <Display level={2}>
      A fairy-dust dose does not get a heroic headline.
    </Display>
  </Surface>
);

export const LevelThree = () => (
  <Surface size="field-guide">
    <div style={{ flex: 1 }} />
    <Display level={3} as="p">
      Honest products with real proof deserve an argument strong enough to earn
      attention.
    </Display>
    <div style={{ height: 18 }} />
    <Secondary>
      Level three steps down without becoming body copy.
    </Secondary>
  </Surface>
);
