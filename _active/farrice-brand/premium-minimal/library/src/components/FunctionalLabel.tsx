import type { ReactNode } from 'react';

export type FunctionalLabelTone = 'graphite' | 'ink' | 'stone' | 'on-ink';

export interface FunctionalLabelProps {
  /** `stone` is for non-essential labels only. `on-ink` is for dark surfaces. */
  tone?: FunctionalLabelTone;
  children?: ReactNode;
  className?: string;
}

/**
 * Uppercase label type at +0.16em tracking — the system's only uppercase move.
 *
 * Use it to name a field, a section, or a state. Content is uppercased by the
 * stylesheet, so pass normal text. Do not use it for headlines: a headline in
 * uppercase is the luxury theatre this system rejects.
 */
export function FunctionalLabel({
  tone = 'graphite',
  children,
  className,
}: FunctionalLabelProps) {
  const classes = [
    'fc-functional-label',
    tone === 'graphite' ? null : `fc-functional-label--${tone}`,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return <span className={classes}>{children}</span>;
}
