export const ROUTES = {
  coordination: {
    label: "coordinating with another buyer",
    result: "Start by getting aligned before you look at more listings. Each buyer should separately write down the payment range a lender has confirmed or still needs to confirm, two non-negotiables, one tradeoff, and the commute or weekly destination that cannot break.",
    next: "Compare the gaps. Those gaps are the beginning of the plan. A lender handles qualification. An attorney or title professional handles ownership or contribution agreements."
  },
  solo: {
    label: "making the decision mostly on my own",
    result: "Start by choosing the next decision that needs proof: payment, area, property type, or condition risk.",
    next: "Give that decision to the right person. A lender handles payment. Jen handles the search and transaction sequence. An inspector or other specialist handles property risk. Buying on your own does not mean carrying every unknown alone."
  },
  creative: {
    label: "organizing nontraditional income",
    result: "Start with a lender question packet. Write down the types of income you receive, about how long each has existed, what records are available, and what may change this year. Do not upload documents here.",
    next: "A qualified lender decides what can be used. Jen can coordinate the search timing and property conversation around the lender's verified answer."
  },
  unsure: {
    label: "not sure yet",
    result: "You are not behind. Find the decision that is creating the pause.",
    next: "Is it mostly money, timing, location, the house itself, or not knowing who should help next?"
  }
};

export const SECONDARY_LABELS = {
  none: "no second issue",
  coordination: "coordinating with another buyer",
  solo: "making the decision mostly on my own",
  creative: "organizing nontraditional income",
  tradeoff: "choosing between payment, property, area, or commute",
  unsure: "still not sure"
};

export function manualReviewFlags(note = "") {
  const text = String(note).toLowerCase();
  const flags = [];

  if (/\b(ssn|social security|account number|routing number|tax return|bank statement|credit score)\b|\$\s?\d/.test(text)) {
    flags.push("sensitive_data");
  }
  if (/\b(safe|safety|crime|school|schools|demographic|family[- ]friendly)\b/.test(text)) {
    flags.push("objective_criteria_redirect");
  }
  if (/\b(qualif\w*|approv\w*|interest rate|credit score|dti|debt.to.income|tax return|bank statement)\b/.test(text)) {
    flags.push("lender_boundary");
  }
  if (/\b(title|co.?own|ownership agreement|legal|divorce|inherit|trust)\b/.test(text)) {
    flags.push("legal_or_title_boundary");
  }

  return flags;
}

export function evaluateDiagnostic(input) {
  let route = ROUTES[input.primary] ? input.primary : "unsure";
  const provisionalFromSecondary = route === "unsure" && ["coordination", "solo", "creative"].includes(input.secondary);
  if (provisionalFromSecondary) route = input.secondary;
  const secondary = input.secondary && input.secondary !== route ? input.secondary : "none";
  const wantsHelp = input.wantsHelp === "yes";
  const consent = input.consent === "yes";
  const represented = input.representation === "yes";
  const outsideArea = input.region === "outside";
  const early = input.timeline === "12_plus" || input.timeline === "not_sure" || input.stage === "exploring";
  const representationUnclear = input.representation === "not_sure" || input.representation === "prefer_not";
  const resourceOnly = input.consent === "resource";

  let serviceState = "active_conversation";
  let serviceReason = "The buyer asked for help, has a relevant market anchor, and is on a plausible 0–12 month path.";

  if (represented) {
    serviceState = "route_out";
    serviceReason = "The buyer says they are already represented. Deliver value, then keep their agent in the loop.";
  } else if (outsideArea) {
    serviceState = "route_out";
    serviceReason = "The stated search is outside Jen's service area. Offer a general resource or a referral only with permission.";
  } else if (!wantsHelp || resourceOnly || !consent || early || representationUnclear) {
    serviceState = "nurture";
    serviceReason = resourceOnly
        ? "The buyer asked for one relevant resource, not an ongoing conversation."
      : !consent
        ? "The buyer did not consent to personal follow-up. Keep this content-only."
      : !wantsHelp
        ? "The buyer wants the result, not a conversation right now."
        : representationUnclear
          ? "Clarify representation before offering services."
          : "The buyer has a real decision, but the timing or stage is still early.";
  }

  return {
    route,
    secondary,
    provisionalFromSecondary,
    result: ROUTES[route],
    serviceState,
    serviceReason,
    contactAllowed: wantsHelp && (consent || resourceOnly) && !represented && !outsideArea,
    contactMode: resourceOnly ? "one_resource" : consent ? "personal_reply" : "none",
    manualFlags: manualReviewFlags(input.note)
  };
}
