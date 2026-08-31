import type { ReactNode } from 'react';

export type SurfaceSize =
  | 'banner'
  | 'cover'
  | 'feed'
  | 'carousel'
  | 'field-guide'
  | 'free';

export type SurfaceTone = 'canvas' | 'paper' | 'ink';

export interface SurfaceProps {
  /** Native canvas from the design contract. `free` is an unsized block for web layout. */
  size?: SurfaceSize;
  /** Background field. `ink` is the dark interruption — one per sequence, maximum. */
  tone?: SurfaceTone;
  children?: ReactNode;
  className?: string;
}

/**
 * The root wrapper every Premium Minimal composition must sit inside.
 *
 * Surface carries the type family, the canvas colour, the contract's safe
 * margins, and the container context the type scale reads. A component placed
 * outside a Surface renders unstyled and at the wrong size.
 *
 * Sizes map to the contract's standard surfaces: banner 1584x396, cover
 * 1920x1080, feed and carousel 1080x1350, field-guide 16:9. Padding is a
 * percentage of width, so the declared safe margins hold at any render scale.
 */
export function Surface({
  size = 'free',
  tone = 'canvas',
  children,
  className,
}: SurfaceProps) {
  const classes = [
    'fc-surface',
    `fc-surface--${size}`,
    tone === 'canvas' ? null : `fc-surface--${tone}`,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <div className={classes}>
      <div className="fc-surface__body">{children}</div>
    </div>
  );
}
