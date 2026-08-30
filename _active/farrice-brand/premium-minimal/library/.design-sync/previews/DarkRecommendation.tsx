import {
  Surface,
  DarkRecommendation,
  Masthead,
} from '@farrice/premium-minimal';

export const TheDecision = () => (
  <Surface size="field-guide">
    <Masthead mode="offer" />
    <div style={{ flex: 1 }} />
    <DarkRecommendation
      statement="Lead with the reorder rate."
      support="It is the only claim the supplied proof fully carries, and the only one a competitor cannot copy by Friday."
    />
  </Surface>
);

export const StatementOnly = () => (
  <Surface size="field-guide">
    <div style={{ flex: 1 }} />
    <DarkRecommendation
      eyebrow="The call"
      statement="Stop funding creative until the argument is chosen."
    />
  </Surface>
);
