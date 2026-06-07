export const RISK_REGIME_LABELS = {
  liquidity_defensive: "Cash and defensive FX",
  duration_credit: "Rates and credit",
  defensive_equity: "Defensive equity",
  broad_cyclical_equity: "Broad and cyclical equity",
  growth_technology: "Growth and technology",
  international_equity: "International equity",
  real_assets_inflation: "Real assets and inflation",
  crypto: "Crypto"
};

function finiteAverage(values) {
  const finite = values.filter((value) => typeof value === "number" && Number.isFinite(value));
  return finite.length ? finite.reduce((total, value) => total + value, 0) / finite.length : null;
}

function populationStandardDeviation(values) {
  const mean = finiteAverage(values);
  if (mean === null) return null;
  return Math.sqrt(values.reduce((total, value) => total + (value - mean) ** 2, 0) / values.length);
}

function allocationBps(allocation) {
  if (typeof allocation?.allocation_bps === "number") return allocation.allocation_bps;
  const allocationPct = Number(allocation?.allocation_pct ?? 0);
  return Number.isFinite(allocationPct) ? allocationPct * 100 : 0;
}

function definitionFor(optionId, definitions) {
  const definition = definitions?.[optionId];
  if (!definition) throw new Error(`Missing asset-risk definition for ${optionId}`);
  return definition;
}

export function historicalRiskLabel(score) {
  if (score === null || !Number.isFinite(score)) return "Not enough history";
  if (score < 2.15) return "Defensive";
  if (score < 3.15) return "Balanced";
  if (score < 4.15) return "Growth";
  return "Aggressive";
}

export function riskPulseLabel(score) {
  if (score === null || !Number.isFinite(score)) return "Not available";
  if (score < 20) return "Defensive";
  if (score < 40) return "Cautious";
  if (score < 60) return "Balanced";
  if (score < 80) return "Risk-seeking";
  return "Aggressive";
}

export function agreementLabel(standardDeviation) {
  if (standardDeviation === null || !Number.isFinite(standardDeviation)) return "Not available";
  if (standardDeviation < 5) return "Tight";
  if (standardDeviation <= 12) return "Mixed";
  return "Divided";
}

export function scorePortfolioRisk(allocations, definitions) {
  const normalized = (allocations ?? [])
    .map((allocation) => ({
      optionId: String(allocation.option_id ?? ""),
      allocationBps: allocationBps(allocation)
    }))
    .filter((allocation) => allocation.optionId && allocation.allocationBps > 0);
  const denominatorBps = normalized.reduce((total, allocation) => total + allocation.allocationBps, 0);
  if (denominatorBps <= 0) {
    return {
      score: null,
      riskScore1To5: null,
      riskOnLoading: null,
      regimeShares: {},
      assets: []
    };
  }

  let riskScore1To5 = 0;
  let riskOnLoading = 0;
  const regimeShares = {};
  const assets = [];
  for (const allocation of normalized) {
    const definition = definitionFor(allocation.optionId, definitions);
    const weight = allocation.allocationBps / denominatorBps;
    riskScore1To5 += weight * Number(definition.risk_score_1_5);
    riskOnLoading += weight * Number(definition.risk_on_loading);
    regimeShares[definition.regime_group] = (regimeShares[definition.regime_group] ?? 0) + weight * 100;
    assets.push({
      option_id: allocation.optionId,
      allocation_pct: weight * 100,
      risk_score_1_5: Number(definition.risk_score_1_5),
      risk_on_loading: Number(definition.risk_on_loading),
      regime_group: definition.regime_group
    });
  }

  return {
    score: 50 + 50 * riskOnLoading,
    riskScore1To5,
    riskOnLoading,
    regimeShares,
    assets
  };
}

function roundSortValue(round) {
  return `${round?.decision_deadline_utc ?? ""}:${round?.decision_date ?? ""}:${round?.round_id ?? ""}`;
}

function roundDecisionDate(round) {
  return String(round?.decision_date ?? round?.decision_deadline_utc ?? "").slice(0, 10);
}

function portfolioKey(portfolio) {
  return `${portfolio.round_id}:${portfolio.run_id}:${portfolio.model_id}`;
}

function scoredPortfolios(portfolios, definitions) {
  return portfolios
    .map((portfolio) => ({
      ...portfolio,
      portfolio_key: portfolioKey(portfolio),
      risk: scorePortfolioRisk(portfolio.allocations ?? [], definitions)
    }))
    .filter((portfolio) => typeof portfolio.risk.score === "number");
}

function averageObjectShares(rows, field) {
  const output = {};
  if (!rows.length) return output;
  for (const row of rows) {
    for (const [key, value] of Object.entries(row[field] ?? {})) {
      output[key] = (output[key] ?? 0) + Number(value) / rows.length;
    }
  }
  return output;
}

function trackRoundSnapshot(round, portfolios, definitions) {
  if (!round) return null;
  const rows = scoredPortfolios(
    portfolios.filter((portfolio) => portfolio.round_id === round.round_id),
    definitions
  );
  const byModel = new Map();
  for (const row of rows) {
    const modelRows = byModel.get(row.model_id) ?? [];
    modelRows.push(row);
    byModel.set(row.model_id, modelRows);
  }
  const models = Array.from(byModel.entries())
    .map(([modelId, modelRows]) => ({
      model_id: modelId,
      score: finiteAverage(modelRows.map((row) => row.risk.score)),
      risk_score_1_5: finiteAverage(modelRows.map((row) => row.risk.riskScore1To5))
    }))
    .filter((model) => typeof model.score === "number")
    .sort((left, right) => right.score - left.score || left.model_id.localeCompare(right.model_id));
  const regimeShares = averageObjectShares(
    rows.map((row) => ({ shares: row.risk.regimeShares })),
    "shares"
  );
  const assetShares = {};
  for (const row of rows) {
    for (const asset of row.risk.assets) {
      assetShares[asset.option_id] = (assetShares[asset.option_id] ?? 0) + asset.allocation_pct / rows.length;
    }
  }
  const score = finiteAverage(models.map((model) => model.score));
  return {
    round_id: round.round_id,
    decision_date: round.decision_date,
    decision_deadline_utc: round.decision_deadline_utc,
    track: round.track,
    score,
    label: riskPulseLabel(score),
    model_count: models.length,
    portfolio_count: rows.length,
    models,
    regime_shares: regimeShares,
    asset_shares: assetShares
  };
}

function combineTrackSnapshots(weekly, monthly) {
  const tracks = [weekly, monthly].filter(Boolean);
  if (!tracks.length) return null;
  const score = finiteAverage(tracks.map((track) => track.score));
  const modelIds = new Set(tracks.flatMap((track) => track.models.map((model) => model.model_id)));
  const models = Array.from(modelIds)
    .map((modelId) => {
      const scores = tracks
        .map((track) => track.models.find((model) => model.model_id === modelId)?.score)
        .filter((value) => typeof value === "number");
      return { model_id: modelId, score: finiteAverage(scores) };
    })
    .filter((model) => typeof model.score === "number")
    .sort((left, right) => right.score - left.score || left.model_id.localeCompare(right.model_id));
  const modelScores = models.map((model) => model.score);
  const standardDeviation = populationStandardDeviation(modelScores);
  const regimeShares = {};
  const assetShares = {};
  for (const track of tracks) {
    for (const [key, value] of Object.entries(track.regime_shares)) {
      regimeShares[key] = (regimeShares[key] ?? 0) + Number(value) / tracks.length;
    }
    for (const [key, value] of Object.entries(track.asset_shares)) {
      assetShares[key] = (assetShares[key] ?? 0) + Number(value) / tracks.length;
    }
  }
  return {
    score,
    label: riskPulseLabel(score),
    models,
    model_count: models.length,
    agreement: {
      label: agreementLabel(standardDeviation),
      standard_deviation: standardDeviation,
      range:
        modelScores.length > 0
          ? { minimum: Math.min(...modelScores), maximum: Math.max(...modelScores) }
          : { minimum: null, maximum: null }
    },
    regime_shares: regimeShares,
    asset_shares: assetShares
  };
}

function outstandingTrackSnapshot(track, portfolios, definitions) {
  const rows = scoredPortfolios(portfolios.filter((portfolio) => portfolio.track === track), definitions);
  const byModel = new Map();
  for (const row of rows) {
    const values = byModel.get(row.model_id) ?? [];
    values.push(row.risk.score);
    byModel.set(row.model_id, values);
  }
  const models = Array.from(byModel.entries()).map(([modelId, values]) => ({
    model_id: modelId,
    score: finiteAverage(values),
    portfolio_count: values.length
  }));
  const score = finiteAverage(models.map((model) => model.score));
  return {
    track,
    score,
    label: riskPulseLabel(score),
    model_count: models.length,
    portfolio_count: rows.length,
    round_count: new Set(rows.map((row) => row.round_id)).size,
    models
  };
}

function latestRoundAsOf(rounds, track, date) {
  return rounds
    .filter((round) => round.track === track && roundDecisionDate(round) <= date)
    .sort((left, right) => roundSortValue(right).localeCompare(roundSortValue(left)))[0];
}

function historyTopAssets(assetShares, assetsById, definitions, limit = 5) {
  return Object.entries(assetShares ?? {})
    .map(([optionId, allocationPct]) => ({
      option_id: optionId,
      label: assetsById.get(optionId)?.label ?? optionId,
      ticker: assetsById.get(optionId)?.ticker ?? "",
      allocation_pct: Number(allocationPct),
      risk_on_loading: Number(definitionFor(optionId, definitions).risk_on_loading),
      regime_group: definitionFor(optionId, definitions).regime_group
    }))
    .sort((left, right) => right.allocation_pct - left.allocation_pct || left.label.localeCompare(right.label))
    .slice(0, limit);
}

function historyRegimeExposure(regimeShares) {
  return Object.entries(regimeShares ?? {})
    .map(([key, allocationPct]) => ({
      key,
      label: RISK_REGIME_LABELS[key] ?? key,
      allocation_pct: Number(allocationPct)
    }))
    .sort((left, right) => right.allocation_pct - left.allocation_pct);
}

function buildDecisionPulseHistory(rounds, portfolios, assetsById, definitions) {
  const dates = Array.from(new Set(rounds.map(roundDecisionDate).filter(Boolean))).sort();
  return dates.map((date) => {
    const weeklyRound = latestRoundAsOf(rounds, "weekly", date);
    const monthlyRound = latestRoundAsOf(rounds, "monthly", date);
    const weekly = trackRoundSnapshot(weeklyRound, portfolios, definitions);
    const monthly = trackRoundSnapshot(monthlyRound, portfolios, definitions);
    const combined = combineTrackSnapshots(weekly, monthly);
    const regimeExposure = historyRegimeExposure(combined?.regime_shares ?? {});
    return {
      date,
      combined_score: combined?.score ?? null,
      label: combined?.label ?? "Not available",
      weekly_score: weekly?.score ?? null,
      monthly_score: monthly?.score ?? null,
      weekly_round_id: weekly?.round_id ?? null,
      monthly_round_id: monthly?.round_id ?? null,
      model_count: combined?.model_count ?? 0,
      agreement_label: combined?.agreement?.label ?? "Not available",
      agreement_standard_deviation: combined?.agreement?.standard_deviation ?? null,
      agreement_range: combined?.agreement?.range ?? { minimum: null, maximum: null },
      top_regime: regimeExposure[0] ?? null,
      top_assets: historyTopAssets(combined?.asset_shares ?? {}, assetsById, definitions),
      regime_exposure: regimeExposure
    };
  });
}

function roundWasOpenOn(round, date) {
  const decisionDate = roundDecisionDate(round);
  const exitDate = String(round?.exit_date ?? "").slice(0, 10);
  return Boolean(decisionDate && decisionDate <= date && (!exitDate || exitDate >= date));
}

function buildOutstandingHistory(rounds, portfolios, definitions) {
  const dates = Array.from(new Set(rounds.map(roundDecisionDate).filter(Boolean))).sort();
  return dates.map((date) => {
    const openRoundIds = new Set(rounds.filter((round) => roundWasOpenOn(round, date)).map((round) => round.round_id));
    const openPortfolios = portfolios.filter((portfolio) => openRoundIds.has(portfolio.round_id));
    const weekly = outstandingTrackSnapshot("weekly", openPortfolios, definitions);
    const monthly = outstandingTrackSnapshot("monthly", openPortfolios, definitions);
    const score = finiteAverage([weekly.score, monthly.score]);
    return {
      date,
      score,
      label: riskPulseLabel(score),
      weekly_score: weekly.score,
      monthly_score: monthly.score,
      portfolio_count: new Set(openPortfolios.map(portfolioKey)).size,
      round_count: openRoundIds.size,
      weekly_portfolio_count: weekly.portfolio_count,
      monthly_portfolio_count: monthly.portfolio_count,
      weekly_round_count: weekly.round_count,
      monthly_round_count: monthly.round_count
    };
  });
}

function regimeDescription(regimeShares, score) {
  const defensive =
    Number(regimeShares.liquidity_defensive ?? 0) +
    Number(regimeShares.duration_credit ?? 0) +
    Number(regimeShares.defensive_equity ?? 0);
  const realAssets = Number(regimeShares.real_assets_inflation ?? 0);
  const growth = Number(regimeShares.growth_technology ?? 0) + Number(regimeShares.crypto ?? 0);
  const broadRisk =
    growth +
    Number(regimeShares.broad_cyclical_equity ?? 0) +
    Number(regimeShares.international_equity ?? 0);

  if (defensive >= 40 && realAssets >= 20) return "Defensive and inflation-sensitive rotation";
  if (defensive >= 50) return "Defensive positioning";
  if (growth >= 50) return "Growth-led risk seeking";
  if (realAssets >= 30) return "Inflation-sensitive risk taking";
  if (broadRisk >= 70) return "Broad risk seeking";
  if (score !== null && score < 60) return "Selective and balanced positioning";
  return "Selective risk taking";
}

export function buildRiskAppetiteSnapshot({ rounds, portfolios, assets, definitions, version }) {
  const publishedRounds = rounds.filter(
    (round) =>
      (round.track === "weekly" || round.track === "monthly") &&
      portfolios.some((portfolio) => portfolio.round_id === round.round_id)
  );
  const activeRounds = rounds.filter(
    (round) =>
      round.status === "active" &&
      (round.track === "weekly" || round.track === "monthly") &&
      portfolios.some((portfolio) => portfolio.round_id === round.round_id)
  );
  const roundsByTrack = {
    weekly: activeRounds.filter((round) => round.track === "weekly").sort((left, right) => roundSortValue(right).localeCompare(roundSortValue(left))),
    monthly: activeRounds.filter((round) => round.track === "monthly").sort((left, right) => roundSortValue(right).localeCompare(roundSortValue(left)))
  };
  const currentWeekly = trackRoundSnapshot(roundsByTrack.weekly[0], portfolios, definitions);
  const currentMonthly = trackRoundSnapshot(roundsByTrack.monthly[0], portfolios, definitions);
  const current = combineTrackSnapshots(currentWeekly, currentMonthly);
  const priorWeekly = trackRoundSnapshot(roundsByTrack.weekly[1], portfolios, definitions);
  const priorMonthly = trackRoundSnapshot(roundsByTrack.monthly[1], portfolios, definitions);
  const prior = combineTrackSnapshots(priorWeekly, priorMonthly);
  const activePortfolios = portfolios.filter((portfolio) => portfolio.status === "active");
  const outstandingWeekly = outstandingTrackSnapshot("weekly", activePortfolios, definitions);
  const outstandingMonthly = outstandingTrackSnapshot("monthly", activePortfolios, definitions);
  const outstandingScore = finiteAverage([outstandingWeekly.score, outstandingMonthly.score]);
  const assetsById = new Map(assets.map((asset) => [asset.option_id, asset]));
  const topAssets = Object.entries(current?.asset_shares ?? {})
    .map(([optionId, allocationPct]) => ({
      option_id: optionId,
      label: assetsById.get(optionId)?.label ?? optionId,
      ticker: assetsById.get(optionId)?.ticker ?? "",
      allocation_pct: Number(allocationPct),
      risk_on_loading: Number(definitionFor(optionId, definitions).risk_on_loading),
      regime_group: definitionFor(optionId, definitions).regime_group
    }))
    .sort((left, right) => right.allocation_pct - left.allocation_pct || left.label.localeCompare(right.label));
  const regimeRows = Object.entries(current?.regime_shares ?? {})
    .map(([key, allocationPct]) => ({
      key,
      label: RISK_REGIME_LABELS[key] ?? key,
      allocation_pct: Number(allocationPct)
    }))
    .sort((left, right) => right.allocation_pct - left.allocation_pct);
  const decisionPulseHistory = buildDecisionPulseHistory(
    publishedRounds,
    portfolios,
    assetsById,
    definitions
  );
  const outstandingHistory = buildOutstandingHistory(publishedRounds, portfolios, definitions);

  return {
    methodology_version: version,
    status: "live_allocations_not_investment_advice",
    current_decision_pulse: {
      score: current?.score ?? null,
      label: current?.label ?? "Not available",
      regime: regimeDescription(current?.regime_shares ?? {}, current?.score ?? null),
      weekly: currentWeekly,
      monthly: currentMonthly,
      change_from_previous: current && prior ? current.score - prior.score : null,
      previous_score: prior?.score ?? null,
      previous_round_ids: {
        weekly: priorWeekly?.round_id ?? null,
        monthly: priorMonthly?.round_id ?? null
      },
      agreement: current?.agreement ?? {
        label: "Not available",
        standard_deviation: null,
        range: { minimum: null, maximum: null }
      },
      models: current?.models ?? [],
      top_assets: topAssets,
      regime_exposure: regimeRows
    },
    outstanding_live_book: {
      score: outstandingScore,
      label: riskPulseLabel(outstandingScore),
      weekly: outstandingWeekly,
      monthly: outstandingMonthly,
      portfolio_count: new Set(
        activePortfolios.map(portfolioKey)
      ).size,
      round_count: activeRounds.length
    },
    history: {
      decision_pulse: decisionPulseHistory,
      outstanding_live_book: outstandingHistory
    },
    scale: {
      minimum: 0,
      maximum: 100,
      bands: [
        { minimum: 0, maximum: 20, label: "Defensive" },
        { minimum: 20, maximum: 40, label: "Cautious" },
        { minimum: 40, maximum: 60, label: "Balanced" },
        { minimum: 60, maximum: 80, label: "Risk-seeking" },
        { minimum: 80, maximum: 100, label: "Aggressive" }
      ]
    }
  };
}
