export type FieldIndexScale = 'label' | 'large';

export interface FieldIndexProps {
  /** The field name, e.g. `FIELD`, `NOTE`. Omit for a bare page number. */
  label?: string;
  /** Two-digit index, e.g. `01`. */
  index: string;
  /** `label` renders in Graphite at label size; `large` renders in Stone at display size. */
  scale?: FieldIndexScale;
  className?: string;
}

/**
 * The numbering mark: `FIELD / 01`, `NOTE / 02`, or a bare two-digit page
 * number.
 *
 * At label scale it is Graphite and quiet. At large scale it is Stone and acts
 * as structure, never as a headline — it must not compete with the dominant
 * idea on the surface.
 */
export function FieldIndex({
  label,
  index,
  scale = 'label',
  className,
}: FieldIndexProps) {
  const classes = [`fc-field-index`, `fc-field-index--${scale}`, className]
    .filter(Boolean)
    .join(' ');

  return (
    <span className={classes}>{label ? `${label} / ${index}` : index}</span>
  );
}
