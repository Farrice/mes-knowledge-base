import {
  Surface,
  Secondary,
  Display,
  DecisionLine,
} from '@farrice/premium-minimal';

export const UnderADisplay = () => (
  <Surface size="field-guide">
    <Display level={2}>The decision before the creative.</Display>
    <div style={{ height: 24 }} />
    <DecisionLine />
    <div style={{ height: 18 }} />
    <Secondary>
      Show the recognizable scene in which a team keeps producing because
      choosing one direction feels harder than making one more asset.
    </Secondary>
  </Surface>
);

export const OnInk = () => (
  <Surface size="field-guide" tone="ink">
    <Display level={3}>Product truth a buyer can believe.</Display>
    <div style={{ height: 18 }} />
    <Secondary onInk>
      Reduced emphasis, never reduced legibility. Secondary text that stops
      being readable has stopped being secondary.
    </Secondary>
  </Surface>
);
