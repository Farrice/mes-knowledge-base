import type { ReactNode } from 'react';

export interface SecondaryProps {
  /** Set on an ink surface so the text stays readable against the dark field. */
  onInk?: boolean;
  children?: ReactNode;
  className?: string;
}

/**
 * Supporting body text in Graphite.
 *
 * Reduced emphasis, never reduced legibility — the contract forbids secondary
 * text so light it becomes unreadable. Measure is capped near 62 characters.
 */
export function Secondary({ onInk, children, className }: SecondaryProps) {
  const classes = [
    'fc-secondary',
    onInk ? 'fc-secondary--on-ink' : null,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return <p className={classes}>{children}</p>;
}
