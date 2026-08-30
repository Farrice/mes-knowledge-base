export interface Route {
  /** Two-digit index, e.g. `01`. */
  index: string;
  /** The argument this route makes, in sentence case. */
  label: string;
  /** One line of support. Optional. */
  note?: string;
}

export interface RouteSetProps {
  /** Three routes is the grammar. Two reads as a false binary; four dilutes the decision. */
  routes: Route[];
  /** 0-indexed route carrying the recommendation. Omit when no route is being recommended. */
  recommended?: number;
  className?: string;
}

/**
 * Three parallel strokes that compare real choices.
 *
 * Routes are differentiated by number, position, and stroke weight — never by
 * colour. The recommended route gets the 6px stroke; the others stay quiet at
 * 1-2px. Use this motif only when the content genuinely compares options. A
 * route set with nothing to choose between is decoration, and the contract
 * forbids it.
 */
export function RouteSet({ routes, recommended, className }: RouteSetProps) {
  return (
    <div className={['fc-route-set', className].filter(Boolean).join(' ')}>
      {routes.map((route, i) => {
        const isRecommended = recommended === i;
        const classes = [
          'fc-route',
          isRecommended ? 'fc-route--recommended' : 'fc-route--quiet',
        ].join(' ');

        return (
          <div className={classes} key={route.index}>
            <span className="fc-route__stroke" />
            <span className="fc-route__index">{route.index}</span>
            <span className="fc-route__label">{route.label}</span>
            {route.note ? <p className="fc-route__note">{route.note}</p> : null}
          </div>
        );
      })}
    </div>
  );
}
