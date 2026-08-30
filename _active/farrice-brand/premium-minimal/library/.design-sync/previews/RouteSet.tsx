import {
  Surface,
  RouteSet,
  Masthead,
  FunctionalLabel,
} from '@farrice/premium-minimal';

export const ThreeRoutesOneRecommended = () => (
  <Surface size="field-guide">
    <Masthead mode="offer" />
    <div style={{ height: 36 }} />
    <RouteSet
      recommended={1}
      routes={[
        {
          index: '01',
          label: 'Lead with the clinical dose',
          note: 'Slowest to land. Hardest for a competitor to argue with.',
        },
        {
          index: '02',
          label: 'Lead with the reorder rate',
          note: 'Proof the brand already owns. Fastest route to trust.',
        },
        {
          index: '03',
          label: 'Lead with the founder',
          note: 'Cheapest to produce. Weakest once the spend scales.',
        },
      ]}
    />
  </Surface>
);

export const NoRecommendationYet = () => (
  <Surface size="field-guide">
    <FunctionalLabel>Arguments on the table</FunctionalLabel>
    <div style={{ height: 24 }} />
    <RouteSet
      routes={[
        { index: '01', label: 'Reformulation is the story' },
        { index: '02', label: 'Retail availability is the story' },
        { index: '03', label: 'The category is lying and we are not' },
      ]}
    />
  </Surface>
);
