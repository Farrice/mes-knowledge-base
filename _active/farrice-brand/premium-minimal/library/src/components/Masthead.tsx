export type MastheadMode = 'master-brand' | 'offer';

export interface MastheadProps {
  /**
   * `master-brand` mastheads FARRICE CAIN over the category descriptor.
   * `offer` mastheads THE ANGLE MAP and credits FARRICE CAIN as author.
   */
  mode?: MastheadMode;
  /** Overrides the identity label. Use only for a genuinely different property. */
  identity?: string;
  /** Overrides the right-hand descriptor or author credit. */
  descriptor?: string;
  className?: string;
}

const DEFAULTS: Record<MastheadMode, { identity: string; descriptor: string }> =
  {
    'master-brand': {
      identity: 'FARRICE CAIN',
      descriptor: 'CREATIVE STRATEGY FOR SUPPLEMENT + PERFORMANCE BRANDS',
    },
    offer: {
      identity: 'THE ANGLE MAP',
      descriptor: 'FARRICE CAIN',
    },
  };

/**
 * The small uppercase identity label at the top of a surface.
 *
 * It is a functional label, not a decorative logo. It does not get a mark, a
 * badge, a seal, or a container. It sits top-left and stays quiet.
 */
export function Masthead({
  mode = 'master-brand',
  identity,
  descriptor,
  className,
}: MastheadProps) {
  const preset = DEFAULTS[mode];

  return (
    <div className={['fc-masthead', className].filter(Boolean).join(' ')}>
      <span className="fc-masthead__identity">
        {identity ?? preset.identity}
      </span>
      <span className="fc-masthead__descriptor">
        {descriptor ?? preset.descriptor}
      </span>
    </div>
  );
}
