import {
  Surface,
  Masthead,
  Display,
  Secondary,
  DecisionLine,
  FieldIndex,
} from '@farrice/premium-minimal';

export const FeedPage = () => (
  <div style={{ maxWidth: 420 }}>
    <Surface size="feed">
    <Masthead mode="master-brand" />
    <div style={{ flex: 1 }} />
    <FieldIndex label="FIELD" index="01" />
    <div style={{ height: 18 }} />
    <Display level={1}>
      A new hook is not a new campaign angle.
    </Display>
    <div style={{ height: 24 }} />
    <DecisionLine weight="structural" />
    <div style={{ height: 18 }} />
      <Secondary>
        More creative can become a socially safer substitute for choosing one
        message direction.
      </Secondary>
    </Surface>
  </div>
);

export const BannerCanvas = () => (
  <Surface size="banner">
    <Masthead mode="master-brand" />
    <div style={{ flex: 1 }} />
    <Display level={3} as="p">
      Stronger arguments for honest products.
    </Display>
  </Surface>
);

export const PaperTone = () => (
  <Surface size="field-guide" tone="paper">
    <Masthead mode="offer" />
    <div style={{ flex: 1 }} />
    <Display level={2}>The decision before the creative.</Display>
    <div style={{ height: 18 }} />
    <Secondary>
      Paper is the lifted field: an alternate page inside the same sequence.
    </Secondary>
  </Surface>
);

export const InkTone = () => (
  <Surface size="field-guide" tone="ink">
    <Masthead mode="offer" />
    <div style={{ flex: 1 }} />
    <Display level={2}>Lead with the reorder rate.</Display>
    <div style={{ height: 18 }} />
    <Secondary onInk>
      One dark interruption per sequence. It earns contrast by being rare.
    </Secondary>
  </Surface>
);
