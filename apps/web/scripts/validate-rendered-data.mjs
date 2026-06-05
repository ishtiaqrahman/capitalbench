import { readFileSync } from "node:fs";
import { join } from "node:path";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildCumulativeLeaderboardData } from "../src/lib/dataApi.js";

const failures = [];
const distRoot = join(process.cwd(), "dist");

function readHtml(path) {
  return readFileSync(join(distRoot, path), "utf8");
}

function includes(html, expected, context) {
  if (!html.includes(expected)) failures.push(`${context} missing rendered text: ${expected}`);
}

function includesAny(html, expectedValues, context) {
  if (!expectedValues.some((expected) => html.includes(expected))) {
    failures.push(`${context} missing rendered text; expected one of: ${expectedValues.join(" | ")}`);
  }
}

function excludes(html, unexpected, context) {
  if (html.includes(unexpected)) failures.push(`${context} contains stale rendered text: ${unexpected}`);
}

function scoreLabel(value) {
  return Number(value).toFixed(1);
}

function percentPointLabel(value) {
  return `${Number(value).toFixed(2)}%`;
}

function signedPercentPointLabel(value) {
  const numeric = Number(value);
  const formatted = `${numeric.toFixed(2)}%`;
  return numeric > 0 ? `+${formatted}` : formatted;
}

function signedPpLabel(value) {
  const numeric = Number(value);
  const formatted = `${numeric.toFixed(2)} pp`;
  return numeric > 0 ? `+${formatted}` : formatted;
}

function htmlText(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function compactExposurePct(value) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return "0%";
  if (numeric >= 1) return `${numeric.toFixed(1)}%`;
  if (numeric > 0) return `${numeric.toFixed(2)}%`;
  return "0%";
}

function allocationLabels(value) {
  const numeric = Number(value);
  return Number.isInteger(numeric) ? [`${numeric}%`, `${numeric.toFixed(1)}%`] : [`${numeric.toFixed(1)}%`];
}

function resolvedLabel(count) {
  return `${count} resolved test${count === 1 ? "" : "s"}`;
}

function modelLabel(modelId) {
  return apiReadModel.models.find((model) => model.model_id === modelId)?.label ?? modelId;
}

function uniquePortfolioKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}`;
}

function assetDisplay(row) {
  if (!row) return "";
  return row.ticker ? `${row.label} (${row.ticker})` : row.label;
}

function optionDisplay(row) {
  if (!row) return "";
  if (row.is_cash || row.option_id === "CASH") return row.label || row.option_id;
  return assetDisplay(row);
}

function optionShortDisplay(row) {
  if (!row) return "";
  if (row.is_cash || row.option_id === "CASH") return row.label || row.option_id;
  return row.ticker || row.label || row.option_id;
}

function allocationPctLabel(value) {
  const numeric = Number(value);
  return Number.isInteger(numeric) ? `${numeric}%` : `${numeric.toFixed(1)}%`;
}

function average(values) {
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : 0;
}

function averageOrNull(values) {
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : null;
}

function shortDate(value) {
  if (!value) return "n/a";
  const [year, month, day] = value.slice(0, 10).split("-").map(Number);
  if (!year || !month || !day) return value.slice(0, 10);
  return new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", timeZone: "UTC" }).format(
    new Date(Date.UTC(year, month - 1, day))
  );
}

function buildActiveExposureSummary() {
  const activeAllocations = apiReadModel.allocations.filter(
    (row) => row.status === "active" && ["weekly", "monthly"].includes(row.track)
  );
  const portfolioKeys = new Set(activeAllocations.map(uniquePortfolioKey));
  const trackPortfolioKeys = {
    weekly: new Set(activeAllocations.filter((row) => row.track === "weekly").map(uniquePortfolioKey)),
    monthly: new Set(activeAllocations.filter((row) => row.track === "monthly").map(uniquePortfolioKey))
  };
  const assets = new Map();

  for (const row of activeAllocations) {
    const existing =
      assets.get(row.option_id) ??
      {
        option_id: row.option_id,
        label: row.label,
        ticker: row.ticker,
        total_bps: 0,
        portfolios: new Set(),
        track_bps: { weekly: 0, monthly: 0 }
      };
    existing.total_bps += row.allocation_bps;
    existing.portfolios.add(uniquePortfolioKey(row));
    existing.track_bps[row.track] += row.allocation_bps;
    assets.set(row.option_id, existing);
  }

  const denominator = portfolioKeys.size * 10_000;
  const rows = Array.from(assets.values())
    .map((row) => ({
      ...row,
      exposure_pct: denominator > 0 ? (row.total_bps / denominator) * 100 : 0,
      weekly_share_pct:
        trackPortfolioKeys.weekly.size > 0 ? (row.track_bps.weekly / (trackPortfolioKeys.weekly.size * 10_000)) * 100 : 0,
      monthly_share_pct:
        trackPortfolioKeys.monthly.size > 0 ? (row.track_bps.monthly / (trackPortfolioKeys.monthly.size * 10_000)) * 100 : 0
    }))
    .sort((left, right) => right.exposure_pct - left.exposure_pct);

  return {
    portfolio_count: portfolioKeys.size,
    active_round_count: new Set(activeAllocations.map((row) => row.round_id)).size,
    rows
  };
}

function latestLiveRows() {
  const latestByPortfolio = new Map();
  for (const row of apiReadModel.interim_performance ?? []) {
    if (row.status !== "active") continue;
    if (row.published === false) continue;
    if (typeof row.model_return_pct !== "number" || typeof row.sp500_return_pct !== "number" || typeof row.alpha_pp !== "number") continue;
    if (row.days_elapsed <= 0 || row.target_date <= row.entry_date || row.target_date >= row.exit_date) continue;
    const key = uniquePortfolioKey(row);
    const existing = latestByPortfolio.get(key);
    if (!existing || row.target_date > existing.target_date || (row.target_date === existing.target_date && row.price_date > existing.price_date)) {
      latestByPortfolio.set(key, row);
    }
  }
  return Array.from(latestByPortfolio.values());
}

function buildLivePerformanceSummary() {
  const rows = latestLiveRows();
  const byModel = new Map();
  const benchmarkByRound = new Map();

  for (const row of rows) {
    const existing =
      byModel.get(row.model_id) ??
      {
        model_id: row.model_id,
        provider: row.provider,
        returns: [],
        benchmark_returns: [],
        alphas: [],
        round_ids: new Set(),
        latest_price_date: ""
      };
    existing.returns.push(row.model_return_pct);
    existing.benchmark_returns.push(row.sp500_return_pct);
    existing.alphas.push(row.alpha_pp);
    existing.round_ids.add(row.round_id);
    existing.latest_price_date = row.price_date > existing.latest_price_date ? row.price_date : existing.latest_price_date;
    byModel.set(row.model_id, existing);

    const roundKey = `${row.round_id}:${row.run_id}`;
    const benchmark = benchmarkByRound.get(roundKey);
    if (!benchmark || row.target_date > benchmark.target_date) benchmarkByRound.set(roundKey, row);
  }

  const modelRows = Array.from(byModel.values())
    .map((row) => ({
      model_id: row.model_id,
      label: modelLabel(row.model_id),
      return_pct: average(row.returns),
      benchmark_return_pct: average(row.benchmark_returns),
      alpha_pp: average(row.alphas),
      open_round_count: row.round_ids.size,
      latest_price_date: row.latest_price_date
    }))
    .sort(
      (left, right) =>
        right.return_pct - left.return_pct ||
        right.alpha_pp - left.alpha_pp ||
        left.label.localeCompare(right.label)
    );

  const benchmarkRows = Array.from(benchmarkByRound.values());

  return {
    modelRows,
    benchmark_return_pct: average(benchmarkRows.map((row) => row.sp500_return_pct)),
    benchmark_round_count: benchmarkRows.length,
    latest_price_date: rows.reduce((latest, row) => (row.price_date > latest ? row.price_date : latest), ""),
    open_round_count: new Set(rows.map((row) => row.round_id)).size,
    next_final_date: rows.map((row) => row.exit_date).filter(Boolean).sort()[0] ?? ""
  };
}

function roundSortKey(round) {
  return `${round.exit_date ?? ""}:${round.decision_deadline_utc ?? ""}:${round.round_id ?? ""}`;
}

function latestRound(track, status) {
  return apiReadModel.rounds
    .filter((round) => round.track === track && round.status === status)
    .sort((left, right) => roundSortKey(right).localeCompare(roundSortKey(left)))[0];
}

function latestRoundByTrack(track) {
  return apiReadModel.rounds.find((round) => round.track === track);
}

function trackStatusLabel(round) {
  if (!round) return "Not started";
  if (round.status === "resolved") return "Scored";
  if (round.status === "archived") return "Archived";
  return "Waiting for result";
}

function pctValue(value) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return "n/a";
  if (Math.abs(numeric) >= 1) return `${numeric.toFixed(1)}%`;
  return `${numeric.toFixed(2)}%`;
}

function modelLiveExposure(modelId) {
  const allocations = apiReadModel.allocations.filter((row) => row.model_id === modelId && row.status === "active");
  const portfolioKeys = new Set(allocations.map(uniquePortfolioKey));
  const byAsset = new Map();
  for (const row of allocations) {
    const existing =
      byAsset.get(row.option_id) ??
      {
        option_id: row.option_id,
        label: row.label,
        ticker: row.ticker,
        total_bps: 0,
        portfolio_keys: new Set()
      };
    existing.total_bps += row.allocation_bps;
    existing.portfolio_keys.add(uniquePortfolioKey(row));
    byAsset.set(row.option_id, existing);
  }
  const denominator = portfolioKeys.size * 10_000;
  const holdings = Array.from(byAsset.values())
    .map((row) => ({
      ...row,
      exposure_pct: denominator > 0 ? (row.total_bps / denominator) * 100 : 0
    }))
    .sort((left, right) => right.exposure_pct - left.exposure_pct || assetDisplay(left).localeCompare(assetDisplay(right)));

  return {
    portfolio_count: portfolioKeys.size,
    holdings,
    top_holding: holdings[0]
  };
}

function modelAverageAlpha(modelId, track) {
  return averageOrNull(
    apiReadModel.results
      .filter((row) => row.model_id === modelId && row.track === track && typeof row.alpha_pp === "number")
      .map((row) => row.alpha_pp)
  );
}

function modelTrackSummary(modelId, track) {
  const rows = apiReadModel.results.filter((row) => row.model_id === modelId && row.track === track);
  return {
    rows,
    averageReturn: averageOrNull(rows.map((row) => row.portfolio_return_pct).filter((value) => typeof value === "number")),
    averageSp500: averageOrNull(rows.map((row) => row.benchmark_return_pct).filter((value) => typeof value === "number")),
    averageAlpha: averageOrNull(rows.map((row) => row.alpha_pp).filter((value) => typeof value === "number")),
    hitRate: rows.length ? (rows.filter((row) => typeof row.alpha_pp === "number" && row.alpha_pp > 0).length / rows.length) * 100 : null,
    averageRank: averageOrNull(rows.map((row) => row.rank).filter((value) => typeof value === "number")),
    bestRound: [...rows].sort((left, right) => Number(right.alpha_pp ?? -Infinity) - Number(left.alpha_pp ?? -Infinity))[0]
  };
}

function buildHomepageTrackState(track) {
  const round = latestRoundByTrack(track);
  if (!round) return null;
  const portfolios = apiReadModel.portfolios.filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
  const allocations = apiReadModel.allocations.filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
  const modelCount = portfolios.length;
  const byAsset = new Map();
  for (const allocation of allocations) {
    const existing =
      byAsset.get(allocation.option_id) ??
      {
        option_id: allocation.option_id,
        label: allocation.label,
        ticker: allocation.ticker,
        is_cash: allocation.option_id === "CASH",
        total_bps: 0
      };
    existing.total_bps += allocation.allocation_bps;
    byAsset.set(allocation.option_id, existing);
  }
  const assets = Array.from(byAsset.values())
    .map((row) => ({
      ...row,
      average_pct: modelCount > 0 ? row.total_bps / modelCount / 100 : 0
    }))
    .sort((left, right) => right.average_pct - left.average_pct || left.option_id.localeCompare(right.option_id));
  const concentrationScore = assets.reduce((total, asset) => total + (asset.average_pct / 100) ** 2, 0);
  return {
    round,
    portfolios,
    assets,
    top_asset: assets[0],
    top_three_share_pct: assets.slice(0, 3).reduce((total, asset) => total + asset.average_pct, 0),
    effective_asset_count: concentrationScore > 0 ? 1 / concentrationScore : 0
  };
}

function portfolioHoldingLine(portfolio) {
  return [...(portfolio.allocations ?? [])]
    .sort((left, right) => right.allocation_bps - left.allocation_bps)
    .map((allocation) => `${optionShortDisplay(allocation)} ${allocationPctLabel(allocation.allocation_pct)}`)
    .join(", ");
}

const indexHtml = readHtml("index.html");
const leaderboardsHtml = readHtml("leaderboards/index.html");
const modelsIndexHtml = readHtml("models/index.html");
const roundsIndexHtml = readHtml("rounds/index.html");
const universeHtml = readHtml("universe/index.html");
const apiHtml = readHtml("api/index.html");

for (const track of ["weekly", "monthly"]) {
  const cumulative = buildCumulativeLeaderboardData(apiReadModel, track);
  if (cumulative.comparison.comparison_round_count === 0 || cumulative.data.length === 0) continue;

  const eligibleRows = cumulative.data.filter((row) => row.is_rank_eligible);
  const leader = eligibleRows[0];
  if (!leader) failures.push(`${track} cumulative leaderboard has no rank-eligible leader`);

  const score = leader ? scoreLabel(leader.capitalbench_score) : "";
  const countLabel = resolvedLabel(cumulative.comparison.comparison_round_count);
  const pagePath = `leaderboards/cumulative-${track}/index.html`;
  const cumulativeHtml = readHtml(pagePath);
  const context = `${track} cumulative page`;

  includes(cumulativeHtml, `${cumulative.comparison.comparison_round_count} resolved`, context);
  includes(cumulativeHtml, score, context);
  includes(cumulativeHtml, "Scores combine every resolved", context);
  for (const roundId of cumulative.comparison.comparison_round_ids) {
    includes(cumulativeHtml, roundId, context);
  }
  for (const row of cumulative.data) {
    includes(cumulativeHtml, row.label, `${context} ${row.model_id}`);
    if (typeof row.capitalbench_score === "number") {
      includes(cumulativeHtml, scoreLabel(row.capitalbench_score), `${context} ${row.model_id} CapitalBench Score`);
    }
    includes(cumulativeHtml, `${row.tests_included}/${row.tests_required}`, `${context} ${row.model_id} scored tests`);
  }

  const provisionalRows = cumulative.data.filter((row) => !row.is_rank_eligible);
  for (const row of provisionalRows) {
    includes(cumulativeHtml, `${row.tests_included}/${row.tests_required}`, `${context} provisional marker`);
    includes(cumulativeHtml, "short history", `${context} provisional marker`);
  }

  if (track === "weekly") {
    includes(indexHtml, "Full-history leader", "homepage weekly lane");
    includes(indexHtml, `${score} score · ${countLabel}`, "homepage weekly lane");
    includes(indexHtml, leader.label, "homepage weekly lane");
  }
  includes(leaderboardsHtml, leader.label, `leaderboards index ${track} leader`);
  includes(leaderboardsHtml, score, `leaderboards index ${track} leader score`);
  includes(leaderboardsHtml, `${cumulative.comparison.comparison_round_count} resolved`, `leaderboards index ${track} resolved count`);
}

for (const [context, html] of [
  ["homepage", indexHtml],
  ["leaderboards index", leaderboardsHtml],
  ["API docs", apiHtml],
  ["weekly cumulative page", readHtml("leaderboards/cumulative-weekly/index.html")]
]) {
  excludes(html, "1 comparable", context);
  excludes(html, "same-roster", context);
  excludes(html, "latest comparable model cohort", context);
  excludes(html, "Comparable leader", context);
  excludes(html, "CB-2026-05-28-W1", context);
}

const resolvedRoundCount = apiReadModel.rounds.filter((round) => round.status === "resolved").length;
const activeRoundCount = apiReadModel.rounds.filter((round) => round.status === "active").length;
const currentUniverseOptionCount = apiReadModel.assets.filter((asset) => asset.in_current_universe).length;
const latestResolvedRound = apiReadModel.rounds
  .filter((round) => round.status === "resolved")
  .sort((left, right) => roundSortKey(right).localeCompare(roundSortKey(left)))[0];
const latestActiveWeekly = latestRound("weekly", "active");
const latestActiveMonthly = latestRound("monthly", "active");
includes(leaderboardsHtml, `<strong>${resolvedRoundCount}</strong>`, "leaderboards index completed count");
includes(leaderboardsHtml, `<strong>${activeRoundCount}</strong>`, "leaderboards index live count");
includes(leaderboardsHtml, `<strong>${apiReadModel.models.length}</strong>`, "leaderboards index model count");
includes(leaderboardsHtml, `<strong>${currentUniverseOptionCount} options</strong>`, "leaderboards index universe count");
if (latestResolvedRound) includes(leaderboardsHtml, latestResolvedRound.round_id, "leaderboards index latest scored round");
if (latestActiveWeekly) includes(leaderboardsHtml, latestActiveWeekly.round_id, "leaderboards index latest active weekly round");
if (latestActiveMonthly) includes(leaderboardsHtml, latestActiveMonthly.round_id, "leaderboards index latest active monthly round");

for (const round of apiReadModel.rounds) {
  includes(roundsIndexHtml, round.round_id, "rounds index");
}

if (apiReadModel.current_universe_round_id) {
  includes(universeHtml, apiReadModel.current_universe_round_id, "universe page current round");
}
for (const asset of apiReadModel.assets.filter((row) => row.in_current_universe)) {
  includes(universeHtml, asset.option_id, `universe page asset ${asset.option_id}`);
  if (asset.ticker) includes(universeHtml, asset.ticker, `universe page asset ${asset.option_id}`);
}

const latestActiveWeeklyRound = latestRound("weekly", "active");
if (latestActiveWeeklyRound) includes(apiHtml, `/v1/rounds/${latestActiveWeeklyRound.round_id}/concentration`, "API docs concentration example");

const latestResolvedScoredRound = apiReadModel.rounds
  .filter(
    (round) =>
      round.status === "resolved" &&
      apiReadModel.results.some((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
  )
  .sort((left, right) => roundSortKey(right).localeCompare(roundSortKey(left)))[0];

if (latestResolvedScoredRound) {
  const context = "homepage latest scored chart";
  const resultRows = apiReadModel.results
    .filter((row) => row.round_id === latestResolvedScoredRound.round_id && row.run_id === latestResolvedScoredRound.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  const returnRows = apiReadModel.returns.filter(
    (row) => row.round_id === latestResolvedScoredRound.round_id && row.run_id === latestResolvedScoredRound.official_run_id
  );
  const benchmarkReturn = returnRows.find((row) => row.is_benchmark)?.return_pct;
  const maxReturnRow = [...returnRows]
    .filter((row) => typeof row.return_pct === "number")
    .sort((left, right) => right.return_pct - left.return_pct)[0];
  const allocationRows = apiReadModel.allocations.filter(
    (row) => row.round_id === latestResolvedScoredRound.round_id && row.run_id === latestResolvedScoredRound.official_run_id
  );

  includes(indexHtml, "Most Recent Finished Test", context);
  includes(indexHtml, "Portfolio Return And S&amp;P 500", context);
  includes(indexHtml, latestResolvedScoredRound.round_id, context);
  includes(indexHtml, latestResolvedScoredRound.entry_date, `${context} entry date`);
  includes(indexHtml, latestResolvedScoredRound.exit_date, `${context} exit date`);
  includes(indexHtml, `<span><strong>Models</strong>${resultRows.length}</span>`, `${context} model count`);
  includes(indexHtml, `<span><strong>Asset choices</strong>${returnRows.length}</span>`, `${context} asset count`);
  includes(indexHtml, `<span><strong>Test length</strong>${latestResolvedScoredRound.track === "weekly" ? "Weekly" : "Monthly"}</span>`, `${context} track label`);

  if (typeof benchmarkReturn === "number") {
    includes(indexHtml, percentPointLabel(benchmarkReturn), `${context} S&P 500 return`);
    includes(indexHtml, "Benchmark return over the same scoring window", `${context} S&P 500 reference`);
  } else {
    failures.push(`${context} missing benchmark return in generated data`);
  }

  if (maxReturnRow) {
    includes(indexHtml, "Maximum possible return", `${context} max possible legend`);
    includes(indexHtml, "Max possible", `${context} max possible row`);
    includes(indexHtml, percentPointLabel(maxReturnRow.return_pct), `${context} max possible return`);
    includes(indexHtml, `100% ${htmlText(assetDisplay(maxReturnRow))} hindsight ceiling`, `${context} max possible label`);
    if (typeof benchmarkReturn === "number") {
      includes(indexHtml, signedPpLabel(maxReturnRow.return_pct - benchmarkReturn), `${context} max possible minus S&P`);
    }
  } else {
    failures.push(`${context} missing max-return row in generated data`);
  }

  for (const row of resultRows) {
    const modelContext = `${context} ${row.model_id}`;
    includes(indexHtml, modelLabel(row.model_id), modelContext);
    includes(indexHtml, percentPointLabel(row.portfolio_return_pct), `${modelContext} portfolio return`);
    includes(indexHtml, signedPpLabel(row.alpha_pp), `${modelContext} alpha`);
    includes(indexHtml, htmlText(`${modelLabel(row.model_id)}: ${percentPointLabel(row.portfolio_return_pct)}.`), `${modelContext} chart tooltip`);

    const modelAllocations = allocationRows
      .filter((allocation) => allocation.model_id === row.model_id)
      .sort((left, right) => left.allocation_rank - right.allocation_rank || right.allocation_bps - left.allocation_bps);
    if (modelAllocations.length === 0) {
      failures.push(`${modelContext} has no allocation rows`);
    }
    for (const allocation of modelAllocations) {
      const allocationContext = `${modelContext} allocation ${allocation.option_id}`;
      const shortLabel = allocation.ticker || allocation.label || allocation.option_id;
      includes(indexHtml, htmlText(assetDisplay(allocation)), `${allocationContext} full label`);
      includes(indexHtml, htmlText(shortLabel), `${allocationContext} short label`);
      includes(indexHtml, allocationPctLabel(allocation.allocation_pct), `${allocationContext} allocation pct`);
    }
  }
}

for (const track of ["weekly", "monthly"]) {
  const state = buildHomepageTrackState(track);
  if (!state) continue;
  const label = track === "weekly" ? "Weekly" : "Monthly";
  const context = `homepage latest ${track} picks`;
  const { round, portfolios, assets, top_asset: topAsset } = state;

  includes(indexHtml, `${label} picks`, context);
  includes(indexHtml, round.round_id, `${context} round id`);
  includes(indexHtml, `${round.entry_date} to ${round.exit_date}`, `${context} score window`);
  includes(indexHtml, trackStatusLabel(round), `${context} status`);

  if (portfolios.length > 0) {
    for (const portfolio of portfolios) {
      const portfolioContext = `${context} ${portfolio.model_id}`;
      includes(indexHtml, modelLabel(portfolio.model_id), portfolioContext);
      const holdingLine = portfolioHoldingLine(portfolio);
      if (holdingLine) includes(indexHtml, htmlText(holdingLine), `${portfolioContext} holdings`);
      for (const allocation of portfolio.allocations ?? []) {
        includes(indexHtml, allocationPctLabel(allocation.allocation_pct), `${portfolioContext} allocation ${allocation.option_id}`);
      }
    }

    if (topAsset) {
      includes(indexHtml, optionDisplay(topAsset), `${context} shared top pick`);
      includes(indexHtml, `Average across ${portfolios.length} model portfolios.`, `${context} model count`);
    } else {
      failures.push(`${context} has portfolios but no concentration top asset`);
    }
    includes(indexHtml, `Top 3 <strong>${allocationPctLabel(state.top_three_share_pct)}</strong>`, `${context} top-three concentration`);
    includes(indexHtml, `Spread <strong>${state.effective_asset_count.toFixed(1)} assets</strong>`, `${context} effective asset count`);

    for (const asset of assets.slice(0, 4)) {
      includes(indexHtml, optionDisplay(asset), `${context} exposure ${asset.option_id}`);
      includes(indexHtml, allocationPctLabel(asset.average_pct), `${context} exposure ${asset.option_id} average allocation`);
    }
  } else {
    includes(indexHtml, `No model picks yet.`, context);
  }
}

const activeExposure = buildActiveExposureSummary();
const largestActiveExposure = activeExposure.rows[0];
if (largestActiveExposure) {
  includes(indexHtml, "Open picks map", "homepage active exposure");
  includes(indexHtml, `${assetDisplay(largestActiveExposure)} is the largest open pick.`, "homepage active exposure top asset");
  includes(indexHtml, compactExposurePct(largestActiveExposure.exposure_pct), "homepage active exposure top percentage");
  includesAny(
    indexHtml,
    [
      `${largestActiveExposure.portfolios.size} of ${activeExposure.portfolio_count}`,
      `${largestActiveExposure.portfolios.size}<!-- --> of <!-- -->${activeExposure.portfolio_count}`
    ],
    "homepage active exposure holder count"
  );
  includes(indexHtml, compactExposurePct(largestActiveExposure.weekly_share_pct), "homepage active exposure weekly share");
  includes(indexHtml, compactExposurePct(largestActiveExposure.monthly_share_pct), "homepage active exposure monthly share");
  includes(indexHtml, "Finished tests are excluded", "homepage active exposure scope");
}

const livePerformance = buildLivePerformanceSummary();
if (livePerformance.modelRows.length > 0) {
  const liveLeader = livePerformance.modelRows[0];
  includes(indexHtml, "Live Portfolio Returns", "homepage live performance");
  includes(indexHtml, String(livePerformance.open_round_count), "homepage live performance open round count");
  includes(indexHtml, shortDate(livePerformance.latest_price_date), "homepage live performance latest close");
  includes(indexHtml, shortDate(livePerformance.next_final_date), "homepage live performance next final date");
  includes(indexHtml, liveLeader.label, "homepage live performance leader");
  includes(indexHtml, signedPercentPointLabel(liveLeader.return_pct), "homepage live performance leader return");
  includes(indexHtml, signedPercentPointLabel(liveLeader.benchmark_return_pct), "homepage live performance leader benchmark return");
  includes(indexHtml, signedPercentPointLabel(liveLeader.alpha_pp), "homepage live performance leader alpha");
  includes(indexHtml, signedPercentPointLabel(livePerformance.benchmark_return_pct), "homepage live performance S&P 500 return");
  includes(indexHtml, "Interim returns use open tests only", "homepage live performance scope");
}

const latestResolvedWeeklyRound = latestRound("weekly", "resolved");
if (latestResolvedWeeklyRound) {
  const latestWeeklyHtml = readHtml("leaderboards/latest-weekly/index.html");
  const latestWeeklyRows = apiReadModel.results
    .filter((row) => row.round_id === latestResolvedWeeklyRound.round_id && row.run_id === latestResolvedWeeklyRound.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  const latestWeeklyWinner = latestWeeklyRows[0];
  includes(latestWeeklyHtml, latestResolvedWeeklyRound.entry_date, "latest weekly page entry date");
  includes(latestWeeklyHtml, latestResolvedWeeklyRound.exit_date, "latest weekly page exit date");
  includes(latestWeeklyHtml, latestResolvedWeeklyRound.round_id, "latest weekly page resolved round id");
  if (latestWeeklyWinner) {
    includes(latestWeeklyHtml, modelLabel(latestWeeklyWinner.model_id), "latest weekly page winner");
    includes(latestWeeklyHtml, percentPointLabel(latestWeeklyWinner.portfolio_return_pct), "latest weekly page winner return");
    includes(latestWeeklyHtml, percentPointLabel(latestWeeklyWinner.benchmark_return_pct), "latest weekly page benchmark return");
  }
  for (const row of latestWeeklyRows) {
    includes(latestWeeklyHtml, modelLabel(row.model_id), `latest weekly page result ${row.model_id}`);
    includes(latestWeeklyHtml, row.selected_option_id, `latest weekly page primary pick ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.portfolio_return_pct), `latest weekly page portfolio return ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.benchmark_return_pct), `latest weekly page benchmark return ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.alpha_pp), `latest weekly page alpha ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.regret_vs_best_option_pct), `latest weekly page regret ${row.model_id}`);
  }
  if (latestActiveWeeklyRound && latestActiveWeeklyRound.round_id !== latestResolvedWeeklyRound.round_id) {
    includes(latestWeeklyHtml, latestActiveWeeklyRound.round_id, "latest weekly page current active round");
  }
}

for (const round of apiReadModel.rounds) {
  const context = `round page ${round.round_id}`;
  const html = readHtml(`rounds/${round.round_id}/index.html`);
  includes(html, round.round_id, context);
  includes(html, round.official_run_id, context);
  includes(html, round.entry_date, context);
  includes(html, round.exit_date, context);
  includes(html, round.status === "resolved" ? "scored" : "pending", context);

  const portfolios = apiReadModel.portfolios.filter(
    (portfolio) => portfolio.round_id === round.round_id && portfolio.run_id === round.official_run_id
  );
  if (portfolios.length !== round.model_count) {
    failures.push(`${context} model_count ${round.model_count} does not match generated portfolio count ${portfolios.length}`);
  }
  for (const portfolio of portfolios) {
    includes(html, modelLabel(portfolio.model_id), `${context} portfolio ${portfolio.model_id}`);
    includes(html, portfolio.selected_option_id, `${context} portfolio ${portfolio.model_id}`);
    for (const allocation of portfolio.allocations) {
      includes(html, allocation.option_id, `${context} allocation ${portfolio.model_id}/${allocation.option_id}`);
      includesAny(html, allocationLabels(allocation.allocation_pct), `${context} allocation ${portfolio.model_id}/${allocation.option_id}`);
    }
  }

  const resultRows = apiReadModel.results
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  if (round.status === "resolved") {
    if (resultRows.length === 0) failures.push(`${context} is resolved but has no generated result rows`);
    const returns = apiReadModel.returns.filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
    const benchmark = returns.find((row) => row.is_benchmark);
    const maxReturn = returns.reduce(
      (best, row) => (typeof row.return_pct === "number" && row.return_pct > best ? row.return_pct : best),
      -Infinity
    );
    if (benchmark) includes(html, percentPointLabel(benchmark.return_pct), `${context} S&P 500 result`);
    if (Number.isFinite(maxReturn)) includes(html, percentPointLabel(maxReturn), `${context} max possible result`);
    for (const row of resultRows) {
      includes(html, modelLabel(row.model_id), `${context} result ${row.model_id}`);
      includes(html, percentPointLabel(row.portfolio_return_pct), `${context} result ${row.model_id}`);
      includes(html, percentPointLabel(row.benchmark_return_pct), `${context} result ${row.model_id} benchmark`);
      includes(html, percentPointLabel(row.alpha_pp), `${context} result ${row.model_id} alpha`);
      includes(html, percentPointLabel(row.regret_vs_best_option_pct), `${context} result ${row.model_id} regret`);
    }
  } else if (resultRows.length > 0) {
    failures.push(`${context} is not resolved but has generated result rows`);
  }
}

for (const model of apiReadModel.models) {
  const directoryContext = `models index ${model.model_id}`;
  includes(modelsIndexHtml, model.label, directoryContext);
  includes(modelsIndexHtml, model.model_id, directoryContext);
  includes(modelsIndexHtml, model.provider_label, directoryContext);

  const directoryLive = modelLiveExposure(model.model_id);
  const directoryCompletedCount = apiReadModel.results.filter((row) => row.model_id === model.model_id).length;
  includes(modelsIndexHtml, `<strong>${directoryLive.portfolio_count}</strong>`, `${directoryContext} live portfolio count`);
  includes(modelsIndexHtml, `<strong>${directoryCompletedCount}</strong>`, `${directoryContext} completed count`);
  if (directoryLive.top_holding) {
    includes(
      modelsIndexHtml,
      `${assetDisplay(directoryLive.top_holding)} ${pctValue(directoryLive.top_holding.exposure_pct)}`,
      `${directoryContext} top live holding`
    );
  }

  const directoryStyle = apiReadModel.model_styles.find((row) => row.model_id === model.model_id);
  if (directoryStyle) {
    includes(modelsIndexHtml, directoryStyle.risk_appetite_label, `${directoryContext} risk label`);
    if (typeof directoryStyle.risk_appetite_score === "number") {
      includes(modelsIndexHtml, `${directoryStyle.risk_appetite_score.toFixed(2)} / 5`, `${directoryContext} risk score`);
    }
  }

  const weeklyAlpha = modelAverageAlpha(model.model_id, "weekly");
  const monthlyAlpha = modelAverageAlpha(model.model_id, "monthly");
  if (weeklyAlpha !== null) includes(modelsIndexHtml, signedPercentPointLabel(weeklyAlpha), `${directoryContext} weekly alpha`);
  if (monthlyAlpha !== null) includes(modelsIndexHtml, signedPercentPointLabel(monthlyAlpha), `${directoryContext} monthly alpha`);

  const context = `model page ${model.model_id}`;
  const html = readHtml(`models/${model.model_id}/index.html`);
  includes(html, model.label, context);
  includes(html, model.model_id, context);
  includes(html, model.provider_label, context);

  const portfolios = apiReadModel.portfolios.filter((row) => row.model_id === model.model_id);
  const activePortfolios = portfolios.filter((row) => row.status === "active");
  const resolvedResults = apiReadModel.results.filter((row) => row.model_id === model.model_id);
  const activePortfolioCount = new Set(activePortfolios.map(uniquePortfolioKey)).size;
  const completedCount = new Set(resolvedResults.map((row) => row.round_id)).size;
  includes(html, `<strong>${activePortfolioCount}</strong>`, `${context} live portfolio count`);
  includes(html, `<strong>${completedCount}</strong>`, `${context} completed test count`);
  if (activePortfolioCount > 0) includes(html, "Live portfolios", context);

  const liveExposure = modelLiveExposure(model.model_id);
  if (liveExposure.portfolio_count > 0) {
    includes(html, `${liveExposure.portfolio_count} open portfolios`, `${context} live holdings open portfolio label`);
    for (const holding of liveExposure.holdings.slice(0, 5)) {
      includesAny(
        html,
        [assetDisplay(holding), htmlText(assetDisplay(holding))],
        `${context} live holding ${holding.option_id} label`
      );
      includes(html, String(holding.exposure_pct), `${context} live holding ${holding.option_id} exposure prop`);
      includes(html, String(holding.portfolio_keys.size), `${context} live holding ${holding.option_id} portfolio count`);
    }
  }

  const modelLiveRows = latestLiveRows().filter((row) => row.model_id === model.model_id);
  if (modelLiveRows.length > 0) {
    includes(html, "Current Return Before Final Scores", `${context} live mark-to-market section`);
    for (const row of modelLiveRows) {
      includes(html, row.round_id, `${context} live return round ${row.round_id}`);
      includes(html, row.price_date, `${context} live return price date ${row.round_id}`);
      includes(html, signedPercentPointLabel(row.model_return_pct), `${context} live portfolio return ${row.round_id}`);
      includes(html, signedPercentPointLabel(row.sp500_return_pct), `${context} live S&P 500 return ${row.round_id}`);
      includes(html, signedPpLabel(row.alpha_pp), `${context} live alpha ${row.round_id}`);
    }
    for (const track of ["weekly", "monthly"]) {
      const trackRows = modelLiveRows.filter((row) => row.track === track);
      if (trackRows.length === 0) continue;
      includes(html, signedPercentPointLabel(average(trackRows.map((row) => row.model_return_pct))), `${context} ${track} live average return`);
      includes(html, signedPercentPointLabel(average(trackRows.map((row) => row.sp500_return_pct))), `${context} ${track} live average S&P return`);
      includes(html, signedPpLabel(average(trackRows.map((row) => row.alpha_pp))), `${context} ${track} live average alpha`);
    }
  }

  for (const track of ["weekly", "monthly"]) {
    const summary = modelTrackSummary(model.model_id, track);
    if (summary.rows.length === 0) continue;
    includes(html, signedPercentPointLabel(summary.averageReturn), `${context} ${track} average return`);
    includes(html, signedPercentPointLabel(summary.averageSp500), `${context} ${track} average S&P return`);
    includes(html, signedPpLabel(summary.averageAlpha), `${context} ${track} average alpha`);
    if (summary.hitRate !== null) includes(html, pctValue(summary.hitRate), `${context} ${track} hit rate`);
    if (summary.averageRank !== null) includes(html, summary.averageRank.toFixed(1), `${context} ${track} average rank`);
    if (summary.bestRound) includes(html, summary.bestRound.round_id, `${context} ${track} best round`);
  }

  const style = apiReadModel.model_styles.find((row) => row.model_id === model.model_id);
  if (style) {
    includes(html, style.risk_appetite_label, `${context} risk label`);
    if (typeof style.risk_appetite_score === "number") {
      includes(html, `${style.risk_appetite_score.toFixed(2)} / 5`, `${context} risk score`);
    }
  }

  for (const portfolio of portfolios.slice(0, 3)) {
    includes(html, portfolio.round_id, `${context} recent portfolio ${portfolio.round_id}`);
  }
}

if (failures.length > 0) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log(JSON.stringify({ ok: true, rendered_data_checks: true }));
