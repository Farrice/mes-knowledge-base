export type DecisionLineWeight = 'hairline' | 'structural' | 'recommendation';

export interface DecisionLineProps {
  /**
   * `hairline` (1px) is quiet structure. `structural` (2px) separates real
   * sections. `recommendation` (6px) is reserved for the line that carries a
   * decision — using it decoratively spends the system's only emphasis.
   */
  weight?: DecisionLineWeight;
  className?: string;
}

/**
 * A horizontal rule that establishes structure, and gets heavier only when it
 * is making a recommendation.
 *
 * This is the system's primary separator. Reach for it before a container, a
 * card, or a background change.
 */
export function DecisionLine({
  weight = 'hairline',
  className,
}: DecisionLineProps) {
  const classes = [
    'fc-decision-line',
    weight === 'hairline' ? null : `fc-decision-line--${weight}`,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return <hr className={classes} />;
}
