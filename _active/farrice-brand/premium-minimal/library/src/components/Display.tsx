import type { ReactNode } from 'react';

export interface DisplayProps {
  /** 1 is the dominant idea on the surface. Never place two level-1 displays together. */
  level?: 1 | 2 | 3;
  /** Renders as this element. Defaults to `h1` at level 1, `h2` otherwise. */
  as?: 'h1' | 'h2' | 'h3' | 'p' | 'div';
  children?: ReactNode;
  className?: string;
}

/**
 * The headline voice: sentence case, tight tracking, close optical leading.
 *
 * Sentence case is a rule, not a preference — title case and all-caps
 * headlines read as advertising and break the system. One dominant idea per
 * surface means one level-1 Display per surface.
 */
export function Display({ level = 1, as, children, className }: DisplayProps) {
  const Tag = as ?? (level === 1 ? 'h1' : 'h2');
  const classes = ['fc-display', `fc-display--${level}`, className]
    .filter(Boolean)
    .join(' ');

  return <Tag className={classes}>{children}</Tag>;
}
