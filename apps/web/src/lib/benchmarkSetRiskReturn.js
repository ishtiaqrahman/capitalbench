import { riskPulseLabel, scorePortfolioRisk } from "./riskAppetiteCore.js";

function finiteNumber(value) {
  return typeof value === "number" && Number.isFinite(value);
}

function average(values) {
  const finite = values.filter(finiteNumber);
  return finite.length ? finite.reduce((total, value) => total + value, 0) / finite.length : null;
}

function riskDefinitions(readModel) {
  return Object.fromEntries(
    (readModel?.assets ?? []).map((asset) => [
      asset.option_id,
      {
        risk_score_1_5: Number(asset.risk_score_1_5),
        risk_on_loading: Number(asset.risk_on_loading),
        regime_group: asset.risk_regime_group,
        defensive: Boolean(asset.defensive),
        technology: Boolean(asset.technology)
      }
    ])
  );
}

function portfolioKey(roundId, runId, modelId) {
  return `${roundId}:${runId}:${modelId}`;
}

export function focusedRiskDomain(values) {
  const finite = values.filter(finiteNumber);
  if (!finite.length) return { minimum: 0, maximum: 100 };

  let minimum = Math.max(0, Math.floor((Math.min(...finite) - 10) / 10) * 10);
  let maximum = Math.min(100, Math.ceil((Math.max(...finite) + 10) / 10) * 10);

  if (maximum - minimum < 40) {
    const center = (minimum + maximum) / 2;
    minimum = Math.max(0, Math.floor((center - 20) / 10) * 10);
    maximum = minimum + 40;
    if (maximum > 100) {
      maximum = 100;
      minimum = 60;
    }
  }

  return { minimum, maximum };
}

export function buildBenchmarkSetRiskReturn(readModel, benchmarkSet) {
  const includedRoundIds = benchmarkSet?.comparison?.comparison_round_ids ?? [];
  if (!includedRoundIds.length) return null;

  const definitions = riskDefinitions(readModel);
  const roundById = new Map((readModel?.rounds ?? []).map((round) => [round.round_id, round]));
  const portfolioByKey = new Map(
    (readModel?.portfolios ?? []).map((portfolio) => [
      portfolioKey(portfolio.round_id, portfolio.run_id, portfolio.model_id),
      portfolio
    ])
  );

  const models = (benchmarkSet?.data ?? [])
    .filter((row) => row.is_rank_eligible && finiteNumber(row.portfolio_return_pct))
    .map((row) => {
      const riskScores = includedRoundIds
        .map((roundId) => {
          const round = roundById.get(roundId);
          if (!round?.official_run_id) return null;
          const portfolio = portfolioByKey.get(portfolioKey(roundId, round.official_run_id, row.model_id));
          if (!portfolio) return null;
          return scorePortfolioRisk(portfolio.allocations ?? [], definitions).score;
        })
        .filter(finiteNumber);

      if (riskScores.length !== includedRoundIds.length) return null;
      const riskScore = average(riskScores);
      if (!finiteNumber(riskScore)) return null;

      return {
        modelId: row.model_id,
        label: row.label,
        provider: row.provider,
        providerLabel: row.provider_label,
        logoSrc: row.logo_src,
        returnPct: row.portfolio_return_pct,
        riskScore,
        riskLabel: riskPulseLabel(riskScore),
        riskMinimum: Math.min(...riskScores),
        riskMaximum: Math.max(...riskScores),
        roundCount: riskScores.length,
        href: `/models/${row.model_id}/`
      };
    })
    .filter(Boolean)
    .sort((left, right) => right.returnPct - left.returnPct || left.riskScore - right.riskScore || left.label.localeCompare(right.label))
    .map((row, index) => ({ ...row, returnRank: index + 1 }));

  if (!models.length) return null;

  const benchmarkReturn = benchmarkSet?.benchmark?.return_pct;
  const benchmarkRisk = scorePortfolioRisk(
    [{ option_id: "SP500", allocation_pct: 100 }],
    definitions
  ).score;
  const benchmark = finiteNumber(benchmarkReturn) && finiteNumber(benchmarkRisk)
    ? {
        label: "S&P 500",
        returnPct: benchmarkReturn,
        riskScore: Number(benchmarkRisk),
        roundCount: includedRoundIds.length
      }
    : null;

  const rows = models.map((model) => ({
    ...model,
    alphaVsBenchmarkPct:
      benchmark && finiteNumber(model.returnPct) ? model.returnPct - benchmark.returnPct : null,
    beatsBenchmarkWithNoMoreRisk:
      Boolean(benchmark) && model.returnPct > benchmark.returnPct && model.riskScore <= benchmark.riskScore
  }));
  const strongTradeoffModels = rows.filter((row) => row.beatsBenchmarkWithNoMoreRisk);

  return {
    setId: benchmarkSet.set_id,
    track: benchmarkSet.track,
    roundCount: includedRoundIds.length,
    methodologyVersion: readModel?.risk_appetite?.methodology_version ?? null,
    riskDomain: focusedRiskDomain([
      ...rows.map((row) => row.riskScore),
      ...(benchmark ? [benchmark.riskScore] : [])
    ]),
    benchmark,
    models: rows,
    returnLeader: rows[0] ?? null,
    strongTradeoffModels
  };
}
