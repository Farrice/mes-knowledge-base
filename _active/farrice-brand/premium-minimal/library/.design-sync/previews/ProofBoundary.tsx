import {
  Surface,
  ProofBoundary,
  FunctionalLabel,
  Display,
} from '@farrice/premium-minimal';

export const ThreeFields = () => (
  <Surface size="field-guide">
    <FunctionalLabel>What the supplied proof carries</FunctionalLabel>
    <div style={{ height: 24 }} />
    <ProofBoundary
      fields={[
        {
          status: 'supported',
          claim: 'Repeat purchase rate of 38% across twelve months.',
        },
        {
          status: 'qualified',
          claim: 'Absorption advantage, pending the third-party panel.',
        },
        {
          status: 'outside',
          claim: 'Any claim about sleep quality.',
        },
      ]}
    />
  </Surface>
);

export const TwoFields = () => (
  <Surface size="field-guide">
    <Display level={3}>Before the next creative cycle is funded.</Display>
    <div style={{ height: 24 }} />
    <ProofBoundary
      fields={[
        {
          status: 'supported',
          claim: 'Third-party tested at the dose printed on the label.',
        },
        {
          status: 'outside',
          claim: 'Comparative performance against a named competitor.',
        },
      ]}
    />
  </Surface>
);
