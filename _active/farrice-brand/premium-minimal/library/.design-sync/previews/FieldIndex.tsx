import {
  Surface,
  FieldIndex,
  Display,
  DecisionLine,
} from '@farrice/premium-minimal';

export const LabelScale = () => (
  <Surface size="field-guide">
    <FieldIndex label="FIELD" index="01" />
    <div style={{ height: 12 }} />
    <DecisionLine />
    <div style={{ height: 36 }} />
    <FieldIndex label="NOTE" index="02" />
    <div style={{ height: 12 }} />
    <DecisionLine />
  </Surface>
);

export const LargeScale = () => (
  <Surface size="field-guide">
    <FieldIndex index="02" scale="large" />
    <div style={{ height: 24 }} />
    <Display level={2}>Proof is not the same as promise.</Display>
  </Surface>
);
