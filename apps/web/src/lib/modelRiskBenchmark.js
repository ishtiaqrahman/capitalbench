import { riskPulseLabel } from "./riskAppetiteCore.js";

export const MODEL_RISK_BENCHMARK_VIEWS = [
  {
    key: "overall",
    label: "Overall",
    scoreField: "average_risk_pulse",
    countField: "portfolio_count"
  },
  {
    key: "monthly",
    label: "Monthly",
    scoreField: "monthly_risk_pulse",
    countField: "monthly_portfolio_count"
  },
  {
    key: "weekly",
    label: "Weekly",
    scoreField: "weekly_risk_pulse",
    countField: "weekly_portfolio_count"
  }
];

function finiteNumber(value) {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function clampScore(value) {
  return Math.min(100, Math.max(0, value));
}

function benchmarkRow(profile, view) {
  const score = finiteNumber(profile?.metrics?.[view.scoreField]);
  if (score === null) return null;

  const portfolioCount = finiteNumber(profile?.sample?.[view.countField]) ?? 0;
  const averageTopAllocation = finiteNumber(profile?.metrics?.average_top_allocation_pct);
  const defensiveAllocation = finiteNumber(profile?.metrics?.defensive_pct);

  return {
    modelId: String(profile?.model_id ?? ""),
    label: String(profile?.label ?? profile?.model_id ?? "Unknown model"),
    provider: String(profile?.provider ?? ""),
    providerLabel: String(profile?.provider_label ?? profile?.provider ?? ""),
    score,
    position: clampScore(score),
    riskLabel: riskPulseLabel(score),
    portfolioCount,
    earlySample: portfolioCount < 8,
    averageTopAllocation,
    defensiveAllocation,
    href: `/models/${profile?.model_id ?? ""}/#model-fingerprint`
  };
}

export function buildModelRiskBenchmark(modelBehavior) {
  const profiles = Array.isArray(modelBehavior?.profiles) ? modelBehavior.profiles : [];
  const views = MODEL_RISK_BENCHMARK_VIEWS.map((view) => ({
    ...view,
    rows: profiles
      .map((profile) => benchmarkRow(profile, view))
      .filter(Boolean)
      .sort((left, right) => right.score - left.score || left.label.localeCompare(right.label))
  }));

  return {
    dataAsOf: String(modelBehavior?.data_as_of ?? ""),
    methodologyHref: String(modelBehavior?.methodology_href ?? "/risk-appetite/#model-behavior-methodology"),
    views
  };
}
