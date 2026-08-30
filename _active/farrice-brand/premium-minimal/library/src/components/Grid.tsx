import type { ReactNode } from 'react';

export interface GridProps {
  /** Gap between columns and rows, in the 12px spacing scale. Defaults to 24px. */
  gap?: 12 | 18 | 24 | 36 | 48 | 72 | 84 | 96 | 120;
  children?: ReactNode;
  className?: string;
}

export interface ColumnProps {
  /** How many of the twelve columns this cell occupies. */
  span?: number;
  /** 1-indexed column this cell starts on. Omit to flow. */
  start?: number;
  children?: ReactNode;
  className?: string;
}

/**
 * The twelve-column grid the contract requires on every surface.
 *
 * Use alignment and whitespace before containers. Keep at least one third of
 * the composition open — that open space is the system, not leftover room.
 */
export function Grid({ gap = 24, children, className }: GridProps) {
  return (
    <div
      className={['fc-grid', className].filter(Boolean).join(' ')}
      style={{ gap: `${gap}px` }}
    >
      {children}
    </div>
  );
}

/** A cell inside {@link Grid}. */
export function Column({ span = 12, start, children, className }: ColumnProps) {
  return (
    <div
      className={['fc-grid__col', className].filter(Boolean).join(' ')}
      style={{
        gridColumn: start
          ? `${start} / span ${span}`
          : `span ${span} / span ${span}`,
      }}
    >
      {children}
    </div>
  );
}
