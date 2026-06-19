export function categoryLabel(value) {
  return String(value ?? "unknown")
    .split("_")
    .filter(Boolean)
    .map((part) => {
      const lower = part.toLowerCase();
      if (lower === "ai") return "AI";
      if (lower === "sp500") return "S&P 500";
      return part.charAt(0).toUpperCase() + part.slice(1);
    })
    .join(" ");
}

export function confidenceLabel(value) {
  const label = String(value ?? "unknown");
  return `${label.charAt(0).toUpperCase()}${label.slice(1)}`;
}

export function insightHref(insight) {
  return insight?.id ? `/insights#${encodeURIComponent(insight.id)}` : "/insights";
}

export function dateLabel(value) {
  if (!value) return "n/a";
  const match = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(value));
  if (!match) return String(value);
  const date = new Date(`${match[1]}-${match[2]}-${match[3]}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", year: "numeric", timeZone: "UTC" }).format(date);
}

export function shortDateLabel(value) {
  if (!value) return "n/a";
  const match = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(value));
  if (!match) return String(value);
  const date = new Date(`${match[1]}-${match[2]}-${match[3]}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

export function calculationLabel(value) {
  return String(value ?? "")
    .split("_")
    .filter(Boolean)
    .map((part) => {
      const lower = part.toLowerCase();
      if (lower === "sp500") return "S&P 500";
      if (lower === "ai") return "AI";
      return part.charAt(0).toUpperCase() + part.slice(1);
    })
    .join(" ");
}

export function calculationValue(calculation) {
  const value = calculation?.value;
  if (typeof value !== "number" || !Number.isFinite(value)) return value ?? "n/a";
  const unit = String(calculation.unit ?? "").toLowerCase();
  const name = String(calculation.name ?? "").toLowerCase();
  if (name.includes("risk_taking_score")) return `${value.toFixed(1)}/100`;
  if (unit === "percent" || unit === "percentage_points") {
    return `${value > 0 ? "+" : ""}${value.toFixed(Math.abs(value) >= 10 ? 1 : 2)}%`;
  }
  if (unit === "points") return value.toFixed(1);
  if (unit === "count" || unit === "models") return String(Math.round(value));
  return value.toFixed(Math.abs(value) >= 10 ? 1 : 2);
}

function roundWindowLabel(context) {
  if (context?.decision_date && context?.exit_date && context.decision_date !== context.exit_date) {
    return `${shortDateLabel(context.decision_date)}-${shortDateLabel(context.exit_date)}`;
  }
  if (context?.decision_date) return shortDateLabel(context.decision_date);
  if (context?.data_as_of) return `Data through ${shortDateLabel(context.data_as_of)}`;
  return null;
}

export function insightTimeframeLabel(insight) {
  const context = insight?.context ?? {};
  const window = roundWindowLabel(context);
  if (window) return window.replace("Data through ", "As of ");
  const dataAsOf = context.data_as_of ?? insight?.data_as_of;
  if (dataAsOf) return `As of ${shortDateLabel(dataAsOf)}`;
  return context.primary_label ?? `${confidenceLabel(insight?.confidence)} confidence`;
}

function uniqueStrings(values) {
  return Array.from(new Set(values.filter(Boolean)));
}

export function contextPills(insight) {
  const context = insight?.context ?? {};
  const pills = [];
  if (context.primary_label) pills.push(context.primary_label);
  if (context.scope === "round" && context.round_id) pills.push(context.round_id);
  if (context.scope === "live_rounds" && context.round_count) pills.push(`${context.round_count} live rounds`);
  if (context.scope === "live_interim" && context.round_count) pills.push(`${context.round_count} open rounds`);
  if (context.scope === "resolved_history" && context.round_count) pills.push(`${context.round_count} resolved rounds`);
  if (context.model_count) pills.push(`${context.model_count} model${context.model_count === 1 ? "" : "s"}`);
  if (context.result_count && context.scope !== "round") pills.push(`${context.result_count} scored results`);
  if (context.oracle_asset?.display) {
    const oracleReturn =
      typeof context.oracle_asset.return_pct === "number"
        ? `, ${context.oracle_asset.return_pct > 0 ? "+" : ""}${context.oracle_asset.return_pct.toFixed(2)}%`
        : "";
    pills.push(`Oracle: ${context.oracle_asset.display}${oracleReturn}`);
  }
  if (context.model?.label) pills.push(`Model: ${context.model.label}`);
  if (typeof context.median_confidence === "number") pills.push(`Median confidence ${context.median_confidence.toFixed(2)}`);
  if (context.status_label) pills.push(context.status_label);
  return uniqueStrings(pills).slice(0, 6);
}

export function sourcePills(insight) {
  const pills = [`${confidenceLabel(insight?.confidence)} confidence`, "Math: deterministic"];
  if (insight?.source_type === "llm_assisted") pills.push("Wording: LLM-assisted");
  pills.push(`Data through ${dateLabel(insight?.data_as_of)}`);
  return pills;
}

export function insightDefinition(insight) {
  switch (insight?.category) {
    case "consensus_performance":
      return "Consensus means the average of model allocations in the same round. CapitalBench Score compares that return with the hindsight-best eligible asset for that exact scoring window.";
    case "benchmark_difficulty":
      return "Asset dispersion is the gap between the best and worst eligible assets in the same round. Wider dispersion makes missed allocation choices more costly.";
    case "oracle_comparison":
      return "Oracle means the best eligible asset in hindsight for that round. Models do not know it when portfolios are frozen.";
    case "current_positioning":
      return "Aggregate allocation averages the newest live model portfolios before final scores are known.";
    case "risk_regime":
      return "Risk-taking score is allocation-based, not performance-based: higher means more weight in growth, momentum, cyclical, and higher-risk assets.";
    case "confidence_calibration":
      return "Confidence is the model's own 0-1 self-reported confidence at submission time, compared with later realized returns.";
    case "horizon_agreement":
      return "Horizon agreement compares the newest weekly and monthly live portfolios to see whether short- and longer-window model stances line up.";
    case "performance_attribution":
      return "Attribution multiplies each frozen holding's weight by its asset return to show what helped or hurt the model portfolio.";
    case "model_behavior":
      return "Momentum exposure measures how much of the frozen portfolio went into assets that had already been recent winners before the model made its allocation.";
    case "live_performance":
      return "Live alpha is interim model return minus interim S&P 500 return. It is provisional until the round reaches its official score date.";
    case "model_similarity":
      return "Cosine similarity measures allocation overlap between model portfolios. A value near 1.00 means the weights are very similar.";
    default:
      return "This insight is generated from CapitalBench public rounds, frozen portfolios, scored results, and linked evidence files.";
  }
}

export function publishedInsights(readModel) {
  const rows = Array.isArray(readModel?.insights?.insights) ? readModel.insights.insights : [];
  return rows
    .map((insight, index) => ({ insight, index }))
    .filter((row) => row.insight?.status !== "draft")
    .sort(
      (left, right) =>
        Number(right.insight.importance_score ?? 0) - Number(left.insight.importance_score ?? 0) ||
        String(right.insight.generated_at ?? "").localeCompare(String(left.insight.generated_at ?? "")) ||
        left.index - right.index
    )
    .map((row) => row.insight);
}

export function topInsightsByCategory(readModel, categories, limit = 3) {
  const categorySet = new Set(categories);
  return publishedInsights(readModel)
    .filter((insight) => categorySet.has(insight.category))
    .slice(0, limit);
}

export function leadInsightsByCategory(readModel, categories, limit = categories.length) {
  const rows = publishedInsights(readModel);
  return categories
    .map((category) => rows.find((insight) => insight.category === category))
    .filter(Boolean)
    .slice(0, limit);
}

function linkedText(insight) {
  return JSON.stringify({
    id: insight.id,
    title: insight.title,
    summary: insight.summary,
    why_it_matters: insight.why_it_matters,
    evidence: insight.evidence,
    related: insight.related
  }).toLowerCase();
}

function matchesRound(insight, roundId) {
  if (!roundId) return false;
  return linkedText(insight).includes(String(roundId).toLowerCase());
}

function matchesModel(insight, modelId, modelName) {
  const text = linkedText(insight);
  return Boolean(
    (modelId && text.includes(String(modelId).toLowerCase())) ||
      (modelName && text.includes(String(modelName).toLowerCase()))
  );
}

function uniqueInsights(rows) {
  const seen = new Set();
  return rows.filter((row) => {
    if (!row?.id || seen.has(row.id)) return false;
    seen.add(row.id);
    return true;
  });
}

export function insightsForRound(readModel, roundId, limit = 3) {
  return uniqueInsights(publishedInsights(readModel).filter((insight) => matchesRound(insight, roundId))).slice(0, limit);
}

/**
 * @param {any} readModel
 * @param {{ modelId?: string; modelName?: string; limit?: number }} [options]
 */
export function insightsForModel(readModel, { modelId, modelName, limit = 3 } = {}) {
  const direct = publishedInsights(readModel).filter((insight) => matchesModel(insight, modelId, modelName));
  const fallback = topInsightsByCategory(
    readModel,
    ["performance_attribution", "confidence_calibration", "model_behavior", "model_similarity"],
    limit
  );
  return uniqueInsights([...direct, ...fallback]).slice(0, limit);
}
