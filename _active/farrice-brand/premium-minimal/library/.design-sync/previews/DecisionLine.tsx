import {
  Surface,
  DecisionLine,
  FunctionalLabel,
} from '@farrice/premium-minimal';

export const ThreeWeights = () => (
  <Surface size="field-guide">
    <FunctionalLabel>Hairline — quiet structure</FunctionalLabel>
    <div style={{ height: 12 }} />
    <DecisionLine />
    <div style={{ height: 48 }} />
    <FunctionalLabel>Structural — separating real sections</FunctionalLabel>
    <div style={{ height: 12 }} />
    <DecisionLine weight="structural" />
    <div style={{ height: 48 }} />
    <FunctionalLabel tone="ink">
      Recommendation — the line carrying a decision
    </FunctionalLabel>
    <div style={{ height: 12 }} />
    <DecisionLine weight="recommendation" />
  </Surface>
);

export const OnInk = () => (
  <Surface size="field-guide" tone="ink">
    <FunctionalLabel tone="on-ink">Hairline on ink</FunctionalLabel>
    <div style={{ height: 12 }} />
    <DecisionLine />
    <div style={{ height: 48 }} />
    <FunctionalLabel tone="on-ink">Recommendation on ink</FunctionalLabel>
    <div style={{ height: 12 }} />
    <DecisionLine weight="recommendation" />
  </Surface>
);
