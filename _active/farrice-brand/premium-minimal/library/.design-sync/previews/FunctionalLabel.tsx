import {
  Surface,
  FunctionalLabel,
  DecisionLine,
} from '@farrice/premium-minimal';

export const Tones = () => (
  <Surface size="field-guide">
    <FunctionalLabel tone="ink">Ink — a named section</FunctionalLabel>
    <div style={{ height: 18 }} />
    <FunctionalLabel>Graphite — the default label</FunctionalLabel>
    <div style={{ height: 18 }} />
    <FunctionalLabel tone="stone">
      Stone — non-essential labels only
    </FunctionalLabel>
    <div style={{ height: 24 }} />
    <DecisionLine />
  </Surface>
);

export const OnInk = () => (
  <Surface size="field-guide" tone="ink">
    <FunctionalLabel tone="on-ink">Recommendation</FunctionalLabel>
    <div style={{ height: 24 }} />
    <DecisionLine weight="recommendation" />
  </Surface>
);
