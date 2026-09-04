import assert from "node:assert/strict";
import { evaluateDiagnostic } from "./decision-logic.js";

const base = {
  primary: "coordination",
  secondary: "none",
  region: "west",
  timeline: "3_6",
  stage: "preparing",
  note: "",
  wantsHelp: "yes",
  representation: "no",
  consent: "yes"
};

const journeys = [
  ["two W-2 buyers aligning payment and commutes", {}, "coordination", "active_conversation", []],
  ["unsure sibling buyers with variable income", { primary: "unsure", secondary: "coordination", note: "We need to understand what the lender can use to qualify." }, "coordination", "active_conversation", ["lender_boundary"]],
  ["one partner engaged, more than a year away", { timeline: "12_plus", stage: "exploring" }, "coordination", "nurture", []],
  ["solo buyer seeking decision support", { primary: "solo", timeline: "6_12" }, "solo", "active_conversation", []],
  ["solo transition with a title question", { primary: "solo", note: "I may need legal help with title after a divorce." }, "solo", "active_conversation", ["legal_or_title_boundary"]],
  ["buyer asks which neighborhood is safest", { primary: "solo", note: "Which area is safest and has the best schools?" }, "solo", "active_conversation", ["objective_criteria_redirect"]],
  ["freelancer preparing a lender question", { primary: "creative", timeline: "3_6", note: "I am wondering what I qualify for." }, "creative", "active_conversation", ["lender_boundary"]],
  ["self-employed buyer with W-2 partner", { primary: "creative", secondary: "coordination" }, "creative", "active_conversation", []],
  ["out-of-area buyer", { primary: "creative", region: "outside" }, "creative", "route_out", []],
  ["buyer already represented", { primary: "solo", representation: "yes", consent: "no" }, "solo", "route_out", []],
  ["buyer wants the result but no conversation", { primary: "unsure", wantsHelp: "no", consent: "no" }, "unsure", "nurture", []],
  ["buyer shares sensitive numbers and asks for eligibility", { primary: "creative", note: "My credit score is 720 and income is $150000. What do I qualify for?" }, "creative", "active_conversation", ["sensitive_data", "lender_boundary"]]
];

for (const [name, changes, route, state, flags] of journeys) {
  const result = evaluateDiagnostic({ ...base, ...changes });
  assert.equal(result.route, route, `${name}: route`);
  assert.equal(result.serviceState, state, `${name}: service state`);
  assert.deepEqual(result.manualFlags, flags, `${name}: manual flags`);
}

console.log(`PASS ${journeys.length}/${journeys.length} diagnostic journeys`);
