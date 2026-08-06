function finiteNumber(value) {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function clampScore(value) {
  return Math.min(100, Math.max(0, value));
}

export const PORTFOLIO_DIFFERENCE_BENCHMARK_VIEWS = [
  { key: "overall", label: "Overall", summaryKey: "combined" },
  { key: "monthly", label: "Monthly", summaryKey: "monthly" },
  { key: "weekly", label: "Weekly", summaryKey: "weekly" }
];

function viewSummary(profile, view) {
  const currentMethodology = profile?.portfolio_difference?.current_methodology;
  return view.summaryKey === "combined"
    ? currentMethodology?.combined
    : currentMethodology?.tracks?.[view.summaryKey];
}

function benchmarkRow(profile, view) {
  if (profile?.lifecycle_status === "retired") return null;

  const currentMethodology = profile?.portfolio_difference?.current_methodology;
  const summary = viewSummary(profile, view);
  const score = finiteNumber(summary?.average_difference_score);
  const observationCount = finiteNumber(summary?.observation_count) ?? 0;
  if (score === null || observationCount <= 0) return null;
  if (view.summaryKey === "combined" && summary?.combined_available !== true) return null;

  const decisionDateCount = finiteNumber(summary?.decision_date_count) ?? 0;
  const evidenceLabel = view.summaryKey === "combined"
    ? currentMethodology?.evidence?.label
    : observationCount >= 8 && decisionDateCount >= 6
      ? "Established sample"
      : "Early sample";

  return {
    modelId: String(profile?.model_id ?? ""),
    label: String(profile?.label ?? profile?.model_id ?? "Unknown model"),
    provider: String(profile?.provider ?? ""),
    providerLabel: String(profile?.provider_label ?? profile?.provider ?? ""),
    score,
    position: clampScore(score),
    observationCount,
    evidenceLabel: String(evidenceLabel ?? (observationCount >= 8 ? "Established sample" : "Early sample")),
    href: `/models/${profile?.model_id ?? ""}/#model-fingerprint`
  };
}

function benchmarkView(profiles, view) {
  const rows = profiles
    .map((profile) => benchmarkRow(profile, view))
    .filter(Boolean)
    .sort((left, right) => right.score - left.score || left.label.localeCompare(right.label));

  return {
    ...view,
    scoreLabel: `${view.label} score`,
    rows: rows.map((row, index) => ({
      ...row,
      distinction:
        index === 0
          ? "Most different"
          : index === rows.length - 1
            ? "Most like the group"
            : null
    }))
  };
}

export function buildPortfolioDifferenceBenchmark(modelBehavior) {
  const profiles = Array.isArray(modelBehavior?.profiles) ? modelBehavior.profiles : [];

  return {
    dataAsOf: String(modelBehavior?.data_as_of ?? ""),
    methodologyHref: "/models/patterns/#portfolio-difference-title",
    views: PORTFOLIO_DIFFERENCE_BENCHMARK_VIEWS.map((view) => benchmarkView(profiles, view))
  };
}
