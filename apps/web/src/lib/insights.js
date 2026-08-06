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
  if (insight?.href) return String(insight.href);
  return insight?.id ? `/insights#${encodeURIComponent(insight.id)}` : "/insights";
}

export function roundHref(roundId) {
  return `/rounds/${encodeURIComponent(String(roundId ?? ""))}`;
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
  if (unit === "score_100" || name.includes("risk_taking_score")) return `${value.toFixed(1)}/100`;
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

const ROUND_ID_PATTERN = /\bCB-\d{4}-\d{2}-\d{2}(?:-V\d+)?-(?:1W|1M)\b/g;

export function roundReferenceTokens(value) {
  const text = String(value ?? "");
  if (!text) return [];

  const tokens = [];
  let lastIndex = 0;
  for (const match of text.matchAll(ROUND_ID_PATTERN)) {
    const roundId = match[0];
    const index = match.index ?? 0;
    if (index > lastIndex) tokens.push({ type: "text", text: text.slice(lastIndex, index) });
    tokens.push({ type: "round", text: roundId, href: roundHref(roundId) });
    lastIndex = index + roundId.length;
  }
  if (lastIndex < text.length) tokens.push({ type: "text", text: text.slice(lastIndex) });
  return tokens.length > 0 ? tokens : [{ type: "text", text }];
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
      if (insight?.context?.insight_kind === "combined_recent_winner_tilt") {
        return "Recent-winner tilt measures how much weight a model placed in assets that had already risen before the portfolio was frozen. Higher does not mean better performance.";
      }
      return "Momentum exposure measures how much of the frozen portfolio went into assets that had already been recent winners before the model made its allocation.";
    case "live_performance":
      return "Live alpha is interim model return minus interim S&P 500 return. It is provisional until the round reaches its official score date.";
    case "model_similarity":
      return "Cosine similarity measures allocation overlap between model portfolios. A value near 1.00 means the weights are very similar.";
    case "market_environment":
      return "Market environments group resolved rounds by the S&P 500 return over the same weekly or monthly window. Models are compared only on shared rounds; high confidence requires at least six observations and stable leadership.";
    default:
      return "This insight is generated from CapitalBench public rounds, frozen portfolios, scored results, and linked evidence files.";
  }
}

function dateValue(value) {
  if (!value) return null;
  const text = String(value);
  const match = /^(\d{4})-(\d{2})-(\d{2})/.exec(text);
  const date = new Date(match ? `${match[1]}-${match[2]}-${match[3]}T00:00:00Z` : text);
  const time = date.getTime();
  return Number.isNaN(time) ? null : time;
}

function roundIdDateValue(roundId) {
  const match = /\bCB-(\d{4})-(\d{2})-(\d{2})(?:-V\d+)?-(?:1W|1M)\b/.exec(String(roundId ?? ""));
  return match ? dateValue(`${match[1]}-${match[2]}-${match[3]}`) : null;
}

function maxDateValue(values) {
  const dates = values
    .flatMap((value) => (Array.isArray(value) ? value : [value]))
    .map((value) => dateValue(value) ?? roundIdDateValue(value))
    .filter((value) => typeof value === "number" && Number.isFinite(value));
  return dates.length > 0 ? Math.max(...dates) : 0;
}

export function insightRecencyValue(insight) {
  const context = insight?.context ?? {};
  const dataDate = maxDateValue([insight?.data_as_of, context.data_as_of]);
  if (dataDate > 0) return dataDate;
  const contextDate = insightContextRecencyValue(insight);
  if (contextDate > 0) return contextDate;
  return maxDateValue([insight?.generated_at, insight?.date]);
}

export function insightContextRecencyValue(insight) {
  const context = insight?.context ?? {};
  return maxDateValue([
    context.decision_date,
    context.entry_date,
    context.decision_dates,
    context.round_id,
    context.round_ids,
    context.best?.round_id,
    context.worst?.round_id
  ]);
}

function generatedAtValue(insight) {
  return maxDateValue([insight?.generated_at, insight?.date]);
}

function publicationTierValue(insight) {
  return { global: 3, category: 2, detail: 1 }[insight?.publication_tier] ?? 2;
}

function confidenceValue(insight) {
  return { high: 3, medium: 2, low: 1 }[insight?.confidence] ?? 0;
}

function maturityValue(insight) {
  return { ready: 2, forming: 1 }[insight?.context?.maturity] ?? 2;
}

export function compareInsightsNewestFirst(left, right) {
  return (
    insightRecencyValue(right.insight) - insightRecencyValue(left.insight) ||
    publicationTierValue(right.insight) - publicationTierValue(left.insight) ||
    confidenceValue(right.insight) - confidenceValue(left.insight) ||
    maturityValue(right.insight) - maturityValue(left.insight) ||
    Number(right.insight.importance_score ?? 0) - Number(left.insight.importance_score ?? 0) ||
    insightContextRecencyValue(right.insight) - insightContextRecencyValue(left.insight) ||
    generatedAtValue(right.insight) - generatedAtValue(left.insight) ||
    left.index - right.index
  );
}

export function publishedInsightRows(rows) {
  return (Array.isArray(rows) ? rows : [])
    .map((insight, index) => ({ insight, index }))
    .filter((row) => row.insight?.status !== "draft")
    .sort(compareInsightsNewestFirst)
    .map((row) => row.insight);
}

export function publishedInsights(readModel) {
  const rows = Array.isArray(readModel?.insights?.insights) ? readModel.insights.insights : [];
  return publishedInsightRows(rows);
}

export function currentLiveRoundIds(readModel) {
  const pulse = readModel?.risk_appetite?.current_decision_pulse;
  return [pulse?.weekly?.round_id, pulse?.monthly?.round_id]
    .filter(Boolean)
    .map(String)
    .sort();
}

export function isCurrentLiveInsight(readModel, insight) {
  if (insight?.context?.scope !== "live_rounds") return true;
  const currentRoundIds = currentLiveRoundIds(readModel);
  const insightRoundIds = Array.isArray(insight?.context?.round_ids)
    ? insight.context.round_ids.filter(Boolean).map(String).sort()
    : [];
  return (
    currentRoundIds.length > 0 &&
    currentRoundIds.length === insightRoundIds.length &&
    currentRoundIds.every((roundId, index) => roundId === insightRoundIds[index])
  );
}

export function staleLiveInsights(readModel) {
  return publishedInsights(readModel).filter(
    (insight) => insight?.context?.scope === "live_rounds" && !isCurrentLiveInsight(readModel, insight)
  );
}

export function featuredInsightRows(rows, limit = 18, perCategory = 2) {
  const ranked = publishedInsightRows(rows).filter((insight) => insight?.publication_tier !== "detail");
  const selected = [];
  const selectedIds = new Set();
  const categoryCounts = new Map();
  for (const insight of ranked) {
    if (categoryCounts.has(insight.category)) continue;
    selected.push(insight);
    selectedIds.add(insight.id);
    categoryCounts.set(insight.category, 1);
    if (selected.length >= limit) return selected;
  }
  for (const insight of ranked) {
    if (selectedIds.has(insight.id)) continue;
    const count = categoryCounts.get(insight.category) ?? 0;
    if (count >= perCategory) continue;
    selected.push(insight);
    selectedIds.add(insight.id);
    categoryCounts.set(insight.category, count + 1);
    if (selected.length >= limit) break;
  }
  return selected;
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

function readyMarketEnvironmentInsight(insight) {
  return Boolean(
    insight?.category === "market_environment" &&
      insight?.confidence !== "low" &&
      insight?.publication_tier !== "detail" &&
      insight?.context?.maturity === "ready"
  );
}

function marketEnvironmentSynthesis(rows) {
  return rows.find(
    (insight) => readyMarketEnvironmentInsight(insight) && insight?.context?.insight_kind === "synthesis"
  );
}

function surfaceCategoryLeads(rows, categories) {
  return categories.map((category) => rows.find((insight) => insight.category === category)).filter(Boolean);
}

export function combinedRecentWinnerInsight(readModel) {
  const behavior = readModel?.model_behavior ?? {};
  const profiles = Array.isArray(behavior.profiles) ? behavior.profiles : [];
  const rows = profiles
    .filter((profile) => profile?.lifecycle_status !== "retired")
    .map((profile) => {
      const combined = profile?.recent_winner?.current_methodology?.combined;
      const score = combined?.average_tilt_score;
      if (combined?.combined_available !== true || typeof score !== "number" || !Number.isFinite(score)) return null;
      return {
        model_id: String(profile.model_id ?? ""),
        label: String(profile.label ?? profile.model_id ?? "Model"),
        score,
        observation_count: Number(combined.observation_count ?? profile?.recent_winner?.current_methodology?.observation_count ?? 0)
      };
    })
    .filter(Boolean);

  if (rows.length < 2) return null;

  const highestFirst = [...rows].sort((left, right) => right.score - left.score || left.label.localeCompare(right.label));
  const lowestFirst = [...rows].sort((left, right) => left.score - right.score || left.label.localeCompare(right.label));
  const leader = highestFirst[0];
  const lowest = lowestFirst[0];
  const dataAsOf = behavior.data_as_of ?? null;

  return {
    id: "combined-recent-winner-tilt",
    status: "published",
    category: "model_behavior",
    confidence: "medium",
    publication_tier: "category",
    importance_score: 80,
    source_type: "deterministic",
    generated_at: behavior.generated_at ?? readModel?.generated_at ?? null,
    data_as_of: dataAsOf,
    title: `${leader.label} follows recent winners most`,
    summary: `${lowest.label} has the lowest combined tilt at ${lowest.score.toFixed(1)}. Monthly and weekly behavior receive equal weight.`,
    why_it_matters: "This describes how models allocate, not whether following recent winners produced a better return.",
    calculations: [
      {
        name: "highest_combined_tilt",
        value: Number(leader.score.toFixed(4)),
        unit: "score_100",
        formula: "50% monthly recent-winner tilt plus 50% weekly recent-winner tilt"
      }
    ],
    evidence: [
      {
        label: "Recent-winner tilt benchmark",
        href: "/models/patterns/#recent-winner-title",
        source: "/api/v1/models/behavior"
      }
    ],
    related: [{ label: "Model behavior patterns", href: "/models/patterns/" }],
    href: "/models/patterns/#recent-winner-title",
    cta_label: "Compare every model",
    context: {
      scope: "model_behavior_history",
      insight_kind: "combined_recent_winner_tilt",
      maturity: "ready",
      data_as_of: dataAsOf,
      primary_label: "50% monthly / 50% weekly",
      model_count: rows.length,
      model_ids: rows.map((row) => row.model_id),
      best: { model_id: leader.model_id, label: leader.label, score: leader.score },
      worst: { model_id: lowest.model_id, label: lowest.label, score: lowest.score }
    }
  };
}

export function insightsForSurface(readModel, surface, limit = 3) {
  const rows = publishedInsights(readModel);
  const currentRows = rows.filter((insight) => isCurrentLiveInsight(readModel, insight));
  const market = marketEnvironmentSynthesis(currentRows);
  if (surface === "home") {
    const positioning = currentRows.find((insight) => insight.category === "current_positioning");
    const recentWinner = combinedRecentWinnerInsight(readModel);
    const fallback = surfaceCategoryLeads(currentRows, [
      "risk_regime",
      "horizon_agreement",
      "live_performance",
      "oracle_comparison"
    ]);
    return uniqueInsights([positioning, market, recentWinner, ...fallback]).slice(0, limit);
  }
  if (surface === "results") {
    const base = topInsightsByCategory(
      readModel,
      ["consensus_performance", "oracle_comparison", "benchmark_difficulty", "confidence_calibration"],
      limit
    );
    return uniqueInsights([market, ...base]).slice(0, limit);
  }
  if (surface === "ticker") {
    const candidates = [
      market,
      ...surfaceCategoryLeads(currentRows, [
        "current_positioning",
        "risk_regime",
        "horizon_agreement",
        "live_performance",
        "oracle_comparison"
      ])
    ]
      .filter(Boolean)
      .sort(
        (left, right) =>
          Number(right.importance_score ?? 0) - Number(left.importance_score ?? 0) ||
          insightRecencyValue(right) - insightRecencyValue(left)
      );
    return uniqueInsights(candidates).slice(0, limit);
  }
  return rows.slice(0, limit);
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
  const target = String(roundId).toLowerCase();
  const context = insight?.context ?? {};
  if (context.scope === "round") return String(context.round_id ?? "").toLowerCase() === target;
  if (context.scope === "live_rounds" || context.scope === "live_interim") {
    return (context.round_ids ?? []).some((value) => String(value).toLowerCase() === target);
  }
  if (context.scope) return false;
  return linkedText(insight).includes(target);
}

function matchesModel(insight, modelId, modelName) {
  const context = insight?.context ?? {};
  const structuredIds = uniqueStrings([
    ...(Array.isArray(context.model_ids) ? context.model_ids : []),
    context.model?.model_id,
    context.best?.model_id,
    context.worst?.model_id
  ]).map((value) => String(value).toLowerCase());
  if (structuredIds.length > 0) {
    return Boolean(modelId && structuredIds.includes(String(modelId).toLowerCase()));
  }
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
 * @param {{ modelId?: string; modelName?: string; limit?: number; includeFallback?: boolean }} [options]
 */
export function insightsForModel(readModel, { modelId, modelName, limit = 3, includeFallback = true } = {}) {
  const direct = publishedInsights(readModel).filter((insight) => matchesModel(insight, modelId, modelName));
  if (!includeFallback) return uniqueInsights(direct).slice(0, limit);
  const fallback = topInsightsByCategory(
    readModel,
    ["performance_attribution", "confidence_calibration", "model_behavior", "model_similarity"],
    limit
  );
  return uniqueInsights([...direct, ...fallback]).slice(0, limit);
}
