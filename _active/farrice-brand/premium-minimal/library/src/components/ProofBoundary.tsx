export type ProofStatus = 'supported' | 'qualified' | 'outside';

export interface ProofField {
  /** Where this claim sits against the supplied proof. */
  status: ProofStatus;
  /** The claim itself, stated plainly. */
  claim: string;
}

export interface ProofBoundaryProps {
  /** Two or three fields. More than three stops being a boundary and becomes a table. */
  fields: ProofField[];
  className?: string;
}

const STATUS_TEXT: Record<ProofStatus, string> = {
  supported: 'Supported',
  qualified: 'Qualified review',
  outside: 'Outside supplied proof',
};

/**
 * Aligned fields separated by rules, stating what the supplied proof supports.
 *
 * Status is carried by wording and by weight — never by warning colour, shield,
 * check mark, badge, or any other compliance theatre. The honest boundary is
 * the point: it says what is supported, what is under qualified review, and
 * what sits outside the proof entirely.
 */
export function ProofBoundary({ fields, className }: ProofBoundaryProps) {
  return (
    <div className={['fc-proof-boundary', className].filter(Boolean).join(' ')}>
      {fields.map((field) => (
        <div
          className={`fc-proof-field fc-proof-field--${field.status}`}
          key={field.claim}
        >
          <span className="fc-proof-field__status">
            {STATUS_TEXT[field.status]}
          </span>
          <p className="fc-proof-field__claim">{field.claim}</p>
        </div>
      ))}
    </div>
  );
}
