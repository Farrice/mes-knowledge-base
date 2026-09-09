import type { ReactNode } from 'react';

export interface DarkRecommendationProps {
  /** Short uppercase label naming what this is, e.g. `Recommendation`. */
  eyebrow?: string;
  /** The decision itself, in sentence case. One sentence is usually right. */
  statement: string;
  /** One or two lines of reasoning. Optional. */
  support?: ReactNode;
  className?: string;
}

/**
 * The ink block: Paper text on an Ink field, reserved for the consequential
 * decision.
 *
 * One dark interruption per sequence, maximum. It earns its contrast by being
 * rare — a deck where three panels go dark has taught the reader that dark
 * means nothing. If the content is not a decision someone has to live with,
 * this is the wrong component.
 */
export function DarkRecommendation({
  eyebrow = 'Recommendation',
  statement,
  support,
  className,
}: DarkRecommendationProps) {
  return (
    <div
      className={['fc-dark-recommendation', className].filter(Boolean).join(' ')}
    >
      {eyebrow ? (
        <span className="fc-dark-recommendation__eyebrow">{eyebrow}</span>
      ) : null}
      <p className="fc-dark-recommendation__statement">{statement}</p>
      {support ? (
        <p className="fc-dark-recommendation__support">{support}</p>
      ) : null}
    </div>
  );
}
