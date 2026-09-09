import {
  Surface,
  Masthead,
  Display,
  Secondary,
  DecisionLine,
} from '@farrice/premium-minimal';

export const MasterBrand = () => (
  <Surface size="banner">
    <Masthead mode="master-brand" />
    <div style={{ flex: 1 }} />
    <Display level={3} as="p">
      Stronger arguments for honest products.
    </Display>
    <div style={{ height: 12 }} />
    <DecisionLine />
  </Surface>
);

export const Offer = () => (
  <Surface size="banner">
    <Masthead mode="offer" />
    <div style={{ flex: 1 }} />
    <Display level={3} as="p">
      Three campaign arguments. One recommendation.
    </Display>
    <div style={{ height: 12 }} />
    <DecisionLine weight="recommendation" />
  </Surface>
);

export const OnInk = () => (
  <Surface size="banner" tone="ink">
    <Masthead mode="offer" />
    <div style={{ flex: 1 }} />
    <Secondary onInk>
      The masthead is a functional label, never a logo — it holds identity
      without asking for attention.
    </Secondary>
  </Surface>
);
