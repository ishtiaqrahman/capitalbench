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
  if (unit === "percent" || unit === "percentage_points") {
    return `${value > 0 ? "+" : ""}${value.toFixed(Math.abs(value) >= 10 ? 1 : 2)}%`;
  }
  if (unit === "points") return value.toFixed(1);
  if (unit === "count" || unit === "models") return String(Math.round(value));
  return value.toFixed(Math.abs(value) >= 10 ? 1 : 2);
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
