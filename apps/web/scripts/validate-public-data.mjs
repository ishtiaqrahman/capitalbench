import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildCumulativeLeaderboardData } from "../src/lib/dataApi.js";

const repoRoot = resolve(process.cwd(), "../..");
const failures = [];
const EPSILON = 1e-7;
const BASIS_POINT_EPSILON = 1e-5;
const TECH_OPTION_IDS = new Set(["NASDAQ100", "LARGE_GROWTH", "TECHNOLOGY", "SEMICONDUCTORS", "SOFTWARE", "BROAD_AI_TECH", "CYBERSECURITY"]);
const DEFENSIVE_OPTION_IDS = new Set([
  "CASH",
  "SHORT_TREASURY",
  "INTERMEDIATE_TREASURY",
  "TIPS",
  "INVESTMENT_GRADE_CREDIT",
  "AGGREGATE_BONDS",
  "GOLD",
  "DIVIDEND",
  "LOW_VOL",
  "CONSUMER_STAPLES",
  "UTILITIES"
]);

function resultPath(round, filename) {
  return join(repoRoot, "rounds", round.round_id, "runs", round.official_run_id, "results", filename);
}

function roundPath(round) {
  return join(repoRoot, "rounds", round.round_id);
}

function readTextFile(path) {
  if (!existsSync(path)) return "";
  return readFileSync(path, "utf8").trim();
}

function parseCsvLine(line) {
  const cells = [];
  let cell = "";
  let inQuotes = false;
  for (let index = 0; index < line.length; index += 1) {
    const char = line[index];
    const next = line[index + 1];
    if (char === '"' && inQuotes && next === '"') {
      cell += '"';
      index += 1;
    } else if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === "," && !inQuotes) {
      cells.push(cell);
      cell = "";
    } else {
      cell += char;
    }
  }
  cells.push(cell);
  return cells;
}

function parseCsv(text) {
  if (!text) return [];
  const lines = text.split(/\r?\n/).filter(Boolean);
  if (lines.length === 0) return [];
  const headers = parseCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]));
  });
}

function readCsv(path) {
  return parseCsv(readTextFile(path));
}

function readJson(path) {
  if (!existsSync(path)) return null;
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch {
    return null;
  }
}

function numberValue(value) {
  if (value === undefined || value === null || value === "") return null;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function priceValue(row) {
  return numberValue(row?.adj_close) ?? numberValue(row?.close) ?? numberValue(row?.price);
}

function priceRowsByOption(round, side) {
  const rows = readCsv(join(roundPath(round), "prices", `${side}_prices.csv`));
  return new Map(rows.map((row) => [row.option_id || row.symbol, row]).filter(([key]) => key));
}

function optionReturnFromPriceRows(entryRow, exitRow) {
  const entry = priceValue(entryRow);
  const exit = priceValue(exitRow);
  if (!isFiniteNumber(entry) || !isFiniteNumber(exit)) return null;
  if (Math.abs(entry) < EPSILON) return null;
  return ((exit / entry) - 1) * 100;
}

function weeklyPriceRowsByTarget(round) {
  const rows = readCsv(join(roundPath(round), "prices", "weekly_prices.csv"));
  const byTarget = new Map();
  for (const row of rows) {
    if (!row.target_date || !row.option_id) continue;
    const targetRows = byTarget.get(row.target_date) ?? new Map();
    targetRows.set(row.option_id, row);
    byTarget.set(row.target_date, targetRows);
  }
  return byTarget;
}

function optionReturnFromWeeklyPrices(entryRows, targetRows, optionId) {
  return optionReturnFromPriceRows(entryRows?.get(optionId), targetRows?.get(optionId));
}

function canonicalDecisionAllocations(payload) {
  if (!payload || typeof payload !== "object") return [];
  if (Array.isArray(payload.portfolio)) {
    return payload.portfolio
      .map((allocation, index) => {
        const allocationPct = numberValue(allocation.allocation_pct);
        return {
          option_id: String(allocation.option_id ?? ""),
          allocation_pct: allocationPct,
          allocation_bps: allocationPct === null ? null : allocationPct * 100,
          allocation_rank: index + 1
        };
      })
      .filter((allocation) => allocation.option_id);
  }
  const optionId = String(payload.selected_option_id ?? "");
  return optionId ? [{ option_id: optionId, allocation_pct: 100, allocation_bps: 10_000, allocation_rank: 1 }] : [];
}

function decimalField(row, ...fields) {
  for (const field of fields) {
    const value = numberValue(row[field]);
    if (value !== null) return value;
  }
  return null;
}

function rowsForRound(rows, roundId) {
  return rows.filter((row) => row.round_id === roundId);
}

function approxEqual(left, right, epsilon = EPSILON) {
  return typeof left === "number" && typeof right === "number" && Number.isFinite(left) && Number.isFinite(right) && Math.abs(left - right) <= epsilon;
}

function isFiniteNumber(value) {
  return typeof value === "number" && Number.isFinite(value);
}

function percentInRange(value, label, context, min = 0, max = 100) {
  if (!isFiniteNumber(value) || value < min - EPSILON || value > max + EPSILON) {
    failures.push(`${context} ${label} ${value} is outside ${min}-${max}`);
  }
}

function dayDiff(startDate, endDate) {
  const start = Date.parse(`${startDate}T00:00:00Z`);
  const end = Date.parse(`${endDate}T00:00:00Z`);
  if (!Number.isFinite(start) || !Number.isFinite(end)) return null;
  return Math.round((end - start) / 86_400_000);
}

function expectedCapitalBenchScore(portfolioReturnPct, maxReturnPct) {
  if (typeof portfolioReturnPct !== "number" || typeof maxReturnPct !== "number") return null;
  if (Math.abs(maxReturnPct) < EPSILON) return Math.abs(portfolioReturnPct - maxReturnPct) < EPSILON ? 100 : 0;
  return (portfolioReturnPct / maxReturnPct) * 100;
}

function average(values) {
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : null;
}

function roundSortValue(round) {
  return `${round?.exit_date ?? ""}:${round?.decision_deadline_utc ?? ""}:${round?.round_id ?? ""}`;
}

function independentCumulativeLeaderboard(track) {
  const rows = apiReadModel.results.filter((row) => row.track === track);
  const roundById = new Map(apiReadModel.rounds.map((round) => [round.round_id, round]));
  const completedRoundIds = Array.from(new Set(rows.map((row) => row.round_id))).sort((left, right) =>
    roundSortValue(roundById.get(left)).localeCompare(roundSortValue(roundById.get(right)))
  );
  const testsRequired = completedRoundIds.length;
  const byModel = new Map();

  for (const row of rows) {
    const existing =
      byModel.get(row.model_id) ??
      {
        model_id: row.model_id,
        portfolio_return_values: [],
        benchmark_return_values: [],
        alpha_values: [],
        max_possible_return_values: [],
        capitalbench_score_values: [],
        wins: 0,
        positive_alpha: 0,
        round_count: 0
      };
    if (isFiniteNumber(row.portfolio_return_pct)) existing.portfolio_return_values.push(row.portfolio_return_pct);
    if (isFiniteNumber(row.benchmark_return_pct)) existing.benchmark_return_values.push(row.benchmark_return_pct);
    if (isFiniteNumber(row.alpha_pp)) {
      existing.alpha_values.push(row.alpha_pp);
      if (row.alpha_pp > 0) existing.positive_alpha += 1;
    }
    if (isFiniteNumber(row.max_possible_return_pct)) existing.max_possible_return_values.push(row.max_possible_return_pct);
    if (isFiniteNumber(row.capitalbench_score)) existing.capitalbench_score_values.push(row.capitalbench_score);
    if (row.rank === 1) existing.wins += 1;
    existing.round_count += 1;
    byModel.set(row.model_id, existing);
  }

  const data = Array.from(byModel.values())
    .map((row) => {
      const isRankEligible = testsRequired > 0 && row.round_count === testsRequired;
      return {
        model_id: row.model_id,
        portfolio_return_pct: average(row.portfolio_return_values),
        benchmark_return_pct: average(row.benchmark_return_values),
        alpha_pp: average(row.alpha_values),
        max_possible_return_pct: average(row.max_possible_return_values),
        capitalbench_score: average(row.capitalbench_score_values),
        round_count: row.round_count,
        tests_required: testsRequired,
        tests_included: row.round_count,
        is_rank_eligible: isRankEligible,
        sample_status: isRankEligible ? "eligible" : "provisional",
        wins: row.wins,
        win_rate_pct: row.round_count ? (row.wins / row.round_count) * 100 : null,
        positive_alpha_rate_pct: row.round_count ? (row.positive_alpha / row.round_count) * 100 : null
      };
    })
    .sort((left, right) =>
      Number(right.is_rank_eligible) - Number(left.is_rank_eligible) ||
      Number(right.capitalbench_score ?? -Infinity) - Number(left.capitalbench_score ?? -Infinity) ||
      Number(right.alpha_pp ?? -Infinity) - Number(left.alpha_pp ?? -Infinity)
    )
    .map((row, index) => ({ rank: index + 1, ...row }));

  return {
    comparison: {
      mode: "all_resolved_rounds",
      completed_round_count: completedRoundIds.length,
      completed_round_ids: completedRoundIds,
      comparison_round_count: testsRequired,
      comparison_round_ids: completedRoundIds,
      excluded_round_ids: [],
      comparison_model_count: new Set(rows.map((row) => row.model_id).filter(Boolean)).size,
      is_early_cohort: testsRequired === 1
    },
    data
  };
}

function sameNullableNumber(actual, expected) {
  if (actual === null || expected === null || actual === undefined || expected === undefined) {
    return actual === expected;
  }
  return approxEqual(actual, expected);
}

function rowKey(row) {
  return `${row.round_id}/${row.run_id}/${row.model_id}`;
}

function portfolioKey(row) {
  return `${row.round_id}/${row.run_id}/${row.model_id}`;
}

function riskScore(asset) {
  if (!asset) return 3;
  if (asset.is_cash) return 1;
  if (String(asset.asset_class).toLowerCase() === "crypto") return 5;
  switch (String(asset.risk_bucket).toLowerCase()) {
    case "cash":
      return 1;
    case "low":
      return 2;
    case "medium":
      return 3;
    case "high":
      return 4;
    case "very_high":
    case "very-high":
    case "speculative":
      return 5;
    default:
      return 3;
  }
}

function riskLabel(score) {
  if (score === null) return "Not enough history";
  if (score < 2.15) return "Defensive";
  if (score < 3.15) return "Balanced";
  if (score < 4.15) return "Growth";
  return "Aggressive";
}

function isDefensive(optionId, asset) {
  if (DEFENSIVE_OPTION_IDS.has(optionId)) return true;
  const category = String(asset?.category ?? "").toLowerCase();
  return category.includes("cash") || category.includes("bond") || category.includes("credit");
}

function isTechnology(optionId, asset) {
  if (TECH_OPTION_IDS.has(optionId)) return true;
  const category = String(asset?.category ?? "").toLowerCase();
  const label = String(asset?.label ?? "").toLowerCase();
  return category.includes("technology") || category.includes("ai") || label.includes("technology") || label.includes("software");
}

const roundById = new Map(apiReadModel.rounds.map((round) => [round.round_id, round]));
const assetById = new Map(apiReadModel.assets.map((asset) => [asset.option_id, asset]));
const modelById = new Map(apiReadModel.models.map((model) => [model.model_id, model]));
const portfoliosByKey = new Map(apiReadModel.portfolios.map((portfolio) => [portfolioKey(portfolio), portfolio]));

for (const round of apiReadModel.rounds) {
  const roundPortfolios = apiReadModel.portfolios.filter((portfolio) => portfolio.round_id === round.round_id && portfolio.run_id === round.official_run_id);
  const modelCount = new Set(roundPortfolios.map((portfolio) => portfolio.model_id)).size;
  if (round.model_count !== modelCount) {
    failures.push(`${round.round_id} model_count ${round.model_count} does not match portfolio model count ${modelCount}`);
  }
}

for (const portfolio of apiReadModel.portfolios) {
  const context = portfolioKey(portfolio);
  const round = roundById.get(portfolio.round_id);
  if (!round) failures.push(`${context} references missing round`);
  if (!modelById.has(portfolio.model_id)) failures.push(`${context} references missing model`);
  if (round && portfolio.run_id !== round.official_run_id) failures.push(`${context} run_id does not match round official_run_id ${round.official_run_id}`);
  if (round && portfolio.track !== round.track) failures.push(`${context} track ${portfolio.track} does not match round track ${round.track}`);
  if (round && portfolio.status !== round.status) failures.push(`${context} status ${portfolio.status} does not match round status ${round.status}`);
  if (!Array.isArray(portfolio.allocations) || portfolio.allocations.length === 0) {
    failures.push(`${context} has no allocations`);
    continue;
  }
  if (portfolio.holding_count !== portfolio.allocations.length) {
    failures.push(`${context} holding_count ${portfolio.holding_count} does not match allocation count ${portfolio.allocations.length}`);
  }
  const allocationTotalPct = portfolio.allocations.reduce((total, allocation) => total + allocation.allocation_pct, 0);
  const allocationTotalBps = portfolio.allocations.reduce((total, allocation) => total + allocation.allocation_bps, 0);
  if (!approxEqual(allocationTotalPct, 100, BASIS_POINT_EPSILON)) failures.push(`${context} allocation_pct total ${allocationTotalPct} does not equal 100`);
  if (!approxEqual(allocationTotalBps, 10_000, BASIS_POINT_EPSILON)) failures.push(`${context} allocation_bps total ${allocationTotalBps} does not equal 10000`);
  if (!portfolio.allocations.some((allocation) => allocation.option_id === portfolio.selected_option_id)) {
    failures.push(`${context} selected_option_id ${portfolio.selected_option_id} is not present in allocations`);
  }

  const seenRanks = new Set();
  for (const allocation of portfolio.allocations) {
    if (!assetById.has(allocation.option_id)) failures.push(`${context} allocation ${allocation.option_id} is not in public asset list`);
    percentInRange(allocation.allocation_pct, `allocation_pct for ${allocation.option_id}`, context);
    if (!approxEqual(allocation.allocation_bps, allocation.allocation_pct * 100, BASIS_POINT_EPSILON)) {
      failures.push(`${context} allocation ${allocation.option_id} bps ${allocation.allocation_bps} does not match pct ${allocation.allocation_pct}`);
    }
    seenRanks.add(allocation.allocation_rank);
  }
  for (let rank = 1; rank <= portfolio.allocations.length; rank += 1) {
    if (!seenRanks.has(rank)) failures.push(`${context} missing allocation_rank ${rank}`);
  }

  if (portfolio.parsed_file_path) {
    const parsedPayload = readJson(join(repoRoot, portfolio.parsed_file_path));
    if (!parsedPayload) {
      failures.push(`${context} parsed submission file ${portfolio.parsed_file_path} is missing or invalid JSON`);
    } else {
      if (parsedPayload.model_id !== portfolio.model_id) failures.push(`${context} model_id does not match parsed submission`);
      if (parsedPayload.provider !== portfolio.provider) failures.push(`${context} provider does not match parsed submission`);
      if (parsedPayload.round_id !== portfolio.round_id) failures.push(`${context} round_id does not match parsed submission`);
      const parsedAllocations = canonicalDecisionAllocations(parsedPayload);
      if (parsedAllocations.length !== portfolio.allocations.length) {
        failures.push(`${context} allocation count ${portfolio.allocations.length} does not match parsed submission ${parsedAllocations.length}`);
      }
      for (const parsedAllocation of parsedAllocations) {
        const generated = portfolio.allocations.find((allocation) => allocation.option_id === parsedAllocation.option_id);
        if (!generated) {
          failures.push(`${context} parsed allocation ${parsedAllocation.option_id} missing from generated portfolio`);
          continue;
        }
        if (!approxEqual(generated.allocation_pct, parsedAllocation.allocation_pct, BASIS_POINT_EPSILON)) {
          failures.push(
            `${context} generated allocation ${generated.option_id} pct ${generated.allocation_pct} does not match parsed ${parsedAllocation.allocation_pct}`
          );
        }
        if (!approxEqual(generated.allocation_bps, parsedAllocation.allocation_bps, BASIS_POINT_EPSILON)) {
          failures.push(
            `${context} generated allocation ${generated.option_id} bps ${generated.allocation_bps} does not match parsed ${parsedAllocation.allocation_bps}`
          );
        }
      }
    }
  }
}

for (const allocation of apiReadModel.allocations) {
  const portfolio = portfoliosByKey.get(portfolioKey(allocation));
  if (!portfolio) {
    failures.push(`${portfolioKey(allocation)} flat allocation has no matching portfolio`);
    continue;
  }
  const nested = portfolio.allocations.find((item) => item.option_id === allocation.option_id && item.allocation_rank === allocation.allocation_rank);
  if (!nested) {
    failures.push(`${portfolioKey(allocation)} flat allocation ${allocation.option_id}/${allocation.allocation_rank} missing from nested portfolio`);
    continue;
  }
  for (const field of ["track", "status", "entry_date", "exit_date", "provider"]) {
    if (allocation[field] !== portfolio[field]) {
      failures.push(`${portfolioKey(allocation)} flat allocation ${allocation.option_id} ${field} ${allocation[field]} does not match portfolio ${portfolio[field]}`);
    }
  }
  for (const field of ["allocation_pct", "allocation_bps"]) {
    if (!approxEqual(allocation[field], nested[field], BASIS_POINT_EPSILON)) {
      failures.push(`${portfolioKey(allocation)} flat allocation ${allocation.option_id} ${field} ${allocation[field]} does not match nested ${nested[field]}`);
    }
  }
}

for (const round of apiReadModel.rounds) {
  if (!round.official_run_id) continue;

  const leaderboardExists = existsSync(resultPath(round, "leaderboard.csv"));
  const returnsExists = existsSync(resultPath(round, "returns.csv"));
  const resultRows = rowsForRound(apiReadModel.results, round.round_id);
  const returnRows = rowsForRound(apiReadModel.returns, round.round_id);

  if (round.status === "resolved" && !leaderboardExists) {
    failures.push(`${round.round_id} is resolved but missing leaderboard.csv`);
  }
  if (round.status === "resolved" && !returnsExists) {
    failures.push(`${round.round_id} is resolved but missing returns.csv`);
  }
  if (round.status === "resolved" && resultRows.length === 0) {
    failures.push(`${round.round_id} is resolved but has no generated result rows`);
  }
  if (round.status === "resolved" && returnRows.length === 0) {
    failures.push(`${round.round_id} is resolved but has no generated asset-return rows`);
  }
  if (round.status === "active" && resultRows.length > 0) {
    failures.push(`${round.round_id} is active but has generated final result rows`);
  }
  if (resultRows.length > 0 && (!leaderboardExists || !returnsExists)) {
    failures.push(`${round.round_id} has generated result rows without complete canonical result files`);
  }

  if (resultRows.length > 0) {
    const canonicalLeaderboardRows = readCsv(resultPath(round, "leaderboard.csv"));
    const canonicalReturnRows = readCsv(resultPath(round, "returns.csv"));
    const canonicalAllocationRows = readCsv(resultPath(round, "allocations.csv"));
    const entryPriceRows = priceRowsByOption(round, "entry");
    const exitPriceRows = priceRowsByOption(round, "exit");
    const canonicalReturnByOption = new Map();
    const canonicalLeaderboardByModel = new Map();
    const canonicalAllocationsByModel = new Map();

    if (canonicalLeaderboardRows.length !== resultRows.length) {
      failures.push(`${round.round_id} canonical leaderboard row count ${canonicalLeaderboardRows.length} does not match generated result rows ${resultRows.length}`);
    }
    if (canonicalReturnRows.length !== returnRows.length) {
      failures.push(`${round.round_id} canonical returns row count ${canonicalReturnRows.length} does not match generated return rows ${returnRows.length}`);
    }

    for (const canonicalRow of canonicalLeaderboardRows) {
      if (canonicalRow.model_id) canonicalLeaderboardByModel.set(canonicalRow.model_id, canonicalRow);
    }
    for (const allocation of canonicalAllocationRows) {
      if (!allocation.model_id) continue;
      const existing = canonicalAllocationsByModel.get(allocation.model_id) ?? [];
      existing.push(allocation);
      canonicalAllocationsByModel.set(allocation.model_id, existing);
    }

    for (const canonicalRow of canonicalReturnRows) {
      const optionId = canonicalRow.option_id;
      const context = `${round.round_id}/${optionId} canonical return`;
      const entryPrice = numberValue(canonicalRow.entry_price);
      const exitPrice = numberValue(canonicalRow.exit_price);
      const canonicalReturnPct = decimalField(canonicalRow, "return");
      const expectedReturnPct =
        isFiniteNumber(entryPrice) && isFiniteNumber(exitPrice) && Math.abs(entryPrice) > EPSILON
          ? ((exitPrice / entryPrice) - 1) * 100
          : null;
      if (expectedReturnPct !== null && !approxEqual(canonicalReturnPct * 100, expectedReturnPct)) {
        failures.push(`${context} ${canonicalReturnPct * 100} does not match exit/entry return ${expectedReturnPct}`);
      }

      const entryRow = entryPriceRows.get(optionId);
      const exitRow = exitPriceRows.get(optionId);
      if (entryRow && !approxEqual(entryPrice, priceValue(entryRow))) {
        failures.push(`${context} entry price ${entryPrice} does not match price file ${priceValue(entryRow)}`);
      }
      if (exitRow && !approxEqual(exitPrice, priceValue(exitRow))) {
        failures.push(`${context} exit price ${exitPrice} does not match price file ${priceValue(exitRow)}`);
      }

      const priceFileReturnPct = optionReturnFromPriceRows(entryRow, exitRow);
      if (priceFileReturnPct !== null && !approxEqual(canonicalReturnPct * 100, priceFileReturnPct)) {
        failures.push(`${context} ${canonicalReturnPct * 100} does not match entry/exit price-file return ${priceFileReturnPct}`);
      }
      canonicalReturnByOption.set(optionId, canonicalReturnPct);
    }

    for (const [modelId, allocations] of canonicalAllocationsByModel.entries()) {
      const allocationTotal = allocations.reduce((total, allocation) => total + (numberValue(allocation.allocation_bps) ?? 0), 0);
      if (!approxEqual(allocationTotal, 10_000, BASIS_POINT_EPSILON)) {
        failures.push(`${round.round_id}/${modelId} canonical allocation bps total ${allocationTotal} does not equal 10000`);
      }
      for (const allocation of allocations) {
        const optionReturn = canonicalReturnByOption.get(allocation.option_id);
        const allocationBps = numberValue(allocation.allocation_bps);
        const canonicalOptionReturn = decimalField(allocation, "option_return");
        const canonicalContribution = decimalField(allocation, "return_contribution");
        if (!approxEqual(canonicalOptionReturn, optionReturn)) {
          failures.push(`${round.round_id}/${modelId}/${allocation.option_id} allocation option_return ${canonicalOptionReturn} does not match returns.csv ${optionReturn}`);
        }
        const expectedContribution = isFiniteNumber(allocationBps) && isFiniteNumber(optionReturn) ? (allocationBps / 10_000) * optionReturn : null;
        if (expectedContribution !== null && !approxEqual(canonicalContribution, expectedContribution)) {
          failures.push(
            `${round.round_id}/${modelId}/${allocation.option_id} return_contribution ${canonicalContribution} does not match weighted contribution ${expectedContribution}`
          );
        }
      }
    }

    const maxReturnPct = Math.max(...returnRows.map((row) => row.return_pct).filter((value) => typeof value === "number"));
    const benchmarkReturn = returnRows.find((row) => row.is_benchmark)?.return_pct;
    const returnByOption = new Map(returnRows.map((row) => [row.option_id, row.return_pct]));

    for (const row of resultRows) {
      const canonicalLeaderboardRow = canonicalLeaderboardByModel.get(row.model_id);
      if (!canonicalLeaderboardRow) {
        failures.push(`${rowKey(row)} generated result has no canonical leaderboard row`);
        continue;
      }
      const canonicalPortfolioReturnPct = decimalField(canonicalLeaderboardRow, "portfolio_return", "selected_asset_return") * 100;
      const canonicalSelectedReturnPct = decimalField(canonicalLeaderboardRow, "selected_asset_return") * 100;
      const canonicalBenchmarkReturnPct = decimalField(canonicalLeaderboardRow, "sp500_return") * 100;
      const canonicalAlphaPct = decimalField(canonicalLeaderboardRow, "alpha_vs_sp500") * 100;
      const canonicalRegretPct = decimalField(canonicalLeaderboardRow, "regret_vs_best_option") * 100;
      if (!approxEqual(row.portfolio_return_pct, canonicalPortfolioReturnPct)) {
        failures.push(`${rowKey(row)} portfolio_return_pct ${row.portfolio_return_pct} does not match canonical leaderboard ${canonicalPortfolioReturnPct}`);
      }
      if (!approxEqual(row.selected_asset_return_pct, canonicalSelectedReturnPct)) {
        failures.push(`${rowKey(row)} selected_asset_return_pct ${row.selected_asset_return_pct} does not match canonical leaderboard ${canonicalSelectedReturnPct}`);
      }
      if (!approxEqual(row.benchmark_return_pct, canonicalBenchmarkReturnPct)) {
        failures.push(`${rowKey(row)} benchmark_return_pct ${row.benchmark_return_pct} does not match canonical leaderboard ${canonicalBenchmarkReturnPct}`);
      }
      if (!approxEqual(row.alpha_pp, canonicalAlphaPct)) {
        failures.push(`${rowKey(row)} alpha_pp ${row.alpha_pp} does not match canonical leaderboard ${canonicalAlphaPct}`);
      }
      if (!approxEqual(row.regret_vs_best_option_pct, canonicalRegretPct)) {
        failures.push(`${rowKey(row)} regret_vs_best_option_pct ${row.regret_vs_best_option_pct} does not match canonical leaderboard ${canonicalRegretPct}`);
      }

      if (!approxEqual(row.max_possible_return_pct, maxReturnPct)) {
        failures.push(`${rowKey(row)} max_possible_return_pct ${row.max_possible_return_pct} does not match max universe return ${maxReturnPct}`);
      }
      if (!approxEqual(row.benchmark_return_pct, benchmarkReturn)) {
        failures.push(`${rowKey(row)} benchmark_return_pct ${row.benchmark_return_pct} does not match benchmark return ${benchmarkReturn}`);
      }
      const expectedAlpha = row.portfolio_return_pct - benchmarkReturn;
      if (!approxEqual(row.alpha_pp, expectedAlpha)) {
        failures.push(`${rowKey(row)} alpha_pp ${row.alpha_pp} does not match portfolio minus benchmark ${expectedAlpha}`);
      }
      const expectedRegret = maxReturnPct - row.portfolio_return_pct;
      if (!approxEqual(row.regret_vs_best_option_pct, expectedRegret)) {
        failures.push(`${rowKey(row)} regret_vs_best_option_pct ${row.regret_vs_best_option_pct} does not match max minus portfolio ${expectedRegret}`);
      }
      const expectedScore = expectedCapitalBenchScore(row.portfolio_return_pct, maxReturnPct);
      if (!approxEqual(row.capitalbench_score, expectedScore)) {
        failures.push(`${rowKey(row)} capitalbench_score ${row.capitalbench_score} does not match expected score ${expectedScore}`);
      }

      const allocations = apiReadModel.allocations.filter(
        (allocation) =>
          allocation.round_id === row.round_id &&
          allocation.run_id === row.run_id &&
          allocation.model_id === row.model_id
      );
      if (allocations.length > 0) {
        const allocationTotal = allocations.reduce((total, allocation) => total + allocation.allocation_pct, 0);
        if (!approxEqual(allocationTotal, 100, 1e-5)) {
          failures.push(`${rowKey(row)} allocation total ${allocationTotal} does not equal 100`);
        }
        const weightedReturn = allocations.reduce((total, allocation) => {
          const optionReturn = returnByOption.get(allocation.option_id);
          return total + (typeof optionReturn === "number" ? (allocation.allocation_pct / 100) * optionReturn : 0);
        }, 0);
        if (!approxEqual(row.portfolio_return_pct, weightedReturn, 1e-5)) {
          failures.push(`${rowKey(row)} portfolio_return_pct ${row.portfolio_return_pct} does not match allocation-weighted return ${weightedReturn}`);
        }
      }

      const canonicalAllocations = canonicalAllocationsByModel.get(row.model_id) ?? [];
      if (canonicalAllocations.length > 0) {
        const weightedReturnPct = canonicalAllocations.reduce((total, allocation) => {
          const optionReturn = canonicalReturnByOption.get(allocation.option_id);
          const allocationBps = numberValue(allocation.allocation_bps);
          return total + (isFiniteNumber(optionReturn) && isFiniteNumber(allocationBps) ? (allocationBps / 10_000) * optionReturn * 100 : 0);
        }, 0);
        if (!approxEqual(row.portfolio_return_pct, weightedReturnPct, 1e-5)) {
          failures.push(`${rowKey(row)} portfolio_return_pct ${row.portfolio_return_pct} does not match canonical allocation-weighted return ${weightedReturnPct}`);
        }
      }
    }

    const sortedByRank = [...resultRows].sort((left, right) => left.rank - right.rank);
    for (let index = 0; index < sortedByRank.length; index += 1) {
      const expectedRank = index + 1;
      if (sortedByRank[index].rank !== expectedRank) {
        failures.push(`${round.round_id} result ranks are not consecutive at rank ${expectedRank}`);
      }
      if (index > 0 && sortedByRank[index - 1].alpha_pp < sortedByRank[index].alpha_pp - EPSILON) {
        failures.push(`${round.round_id} result rank order does not sort by alpha descending`);
      }
    }
  }
}

for (const row of apiReadModel.interim_performance ?? []) {
  const context = rowKey(row);
  const round = roundById.get(row.round_id);
  const portfolio = portfoliosByKey.get(portfolioKey(row));
  if (!round) failures.push(`${context} interim row references missing round`);
  if (!portfolio) failures.push(`${context} interim row has no matching portfolio`);
  if (round && row.run_id !== round.official_run_id) failures.push(`${context} interim run_id does not match official run ${round.official_run_id}`);
  if (round && row.track !== round.track) failures.push(`${context} interim track ${row.track} does not match round track ${round.track}`);
  if (round && row.status !== round.status) failures.push(`${context} interim status ${row.status} does not match round status ${round.status}`);
  if (portfolio && row.holding_count !== portfolio.allocations.length) {
    failures.push(`${context} interim holding_count ${row.holding_count} does not match portfolio allocation count ${portfolio.allocations.length}`);
  }
  if (!approxEqual(row.alpha_pp, row.model_return_pct - row.sp500_return_pct)) {
    failures.push(`${context} interim alpha_pp ${row.alpha_pp} does not match model minus S&P ${row.model_return_pct - row.sp500_return_pct}`);
  }
  if (round) {
    const weeklyPrices = weeklyPriceRowsByTarget(round);
    const entryRows = weeklyPrices.get(round.entry_date);
    const targetRows = weeklyPrices.get(row.target_date);
    if (!entryRows) {
      failures.push(`${context} interim weekly_prices.csv has no entry-date snapshot for ${round.entry_date}`);
    }
    if (!targetRows) {
      failures.push(`${context} interim weekly_prices.csv has no target-date snapshot for ${row.target_date}`);
    }

    const sp500Return = optionReturnFromWeeklyPrices(entryRows, targetRows, round.benchmark_option_id ?? "SP500");
    if (sp500Return !== null && !approxEqual(row.sp500_return_pct, sp500Return, 1e-5)) {
      failures.push(`${context} interim sp500_return_pct ${row.sp500_return_pct} does not match weekly price return ${sp500Return}`);
    }
    const sp500TargetRow = targetRows?.get(round.benchmark_option_id ?? "SP500");
    if (sp500TargetRow && row.price_date !== (sp500TargetRow.price_date || row.target_date)) {
      failures.push(`${context} interim price_date ${row.price_date} does not match S&P weekly price date ${sp500TargetRow.price_date}`);
    }

    if (portfolio && entryRows && targetRows) {
      let expectedModelReturn = 0;
      let hasAllPrices = true;
      for (const allocation of portfolio.allocations) {
        const optionReturn = optionReturnFromWeeklyPrices(entryRows, targetRows, allocation.option_id);
        if (optionReturn === null) {
          failures.push(`${context} interim missing weekly price return for allocation ${allocation.option_id}`);
          hasAllPrices = false;
          continue;
        }
        expectedModelReturn += (allocation.allocation_pct / 100) * optionReturn;
      }
      if (hasAllPrices && !approxEqual(row.model_return_pct, expectedModelReturn, 1e-5)) {
        failures.push(`${context} interim model_return_pct ${row.model_return_pct} does not match weekly price weighted return ${expectedModelReturn}`);
      }
    }

    const entryPriceFileRows = priceRowsByOption(round, "entry");
    for (const [optionId, weeklyEntryRow] of entryRows ?? []) {
      const entryPriceRow = entryPriceFileRows.get(optionId);
      if (entryPriceRow && !approxEqual(priceValue(weeklyEntryRow), priceValue(entryPriceRow))) {
        failures.push(`${context} weekly entry snapshot ${optionId} price ${priceValue(weeklyEntryRow)} does not match entry_prices.csv ${priceValue(entryPriceRow)}`);
      }
    }

    const elapsed = dayDiff(round.entry_date, row.target_date);
    if (elapsed === null) {
      failures.push(`${context} interim target_date ${row.target_date} cannot be compared to entry date ${round.entry_date}`);
    } else if (row.days_elapsed !== elapsed) {
      failures.push(`${context} interim days_elapsed ${row.days_elapsed} does not match date difference ${elapsed}`);
    }
    if (row.target_date < round.entry_date || row.target_date > round.exit_date) {
      failures.push(`${context} interim target_date ${row.target_date} is outside ${round.entry_date} to ${round.exit_date}`);
    }
    if (row.price_date > row.target_date) {
      failures.push(`${context} interim price_date ${row.price_date} is after target_date ${row.target_date}`);
    }
    if (row.target_date === round.entry_date) {
      if (!approxEqual(row.model_return_pct, 0) || !approxEqual(row.sp500_return_pct, 0) || !approxEqual(row.alpha_pp, 0)) {
        failures.push(`${context} interim entry-date row is not zero-return`);
      }
    }
  }
}

for (const style of apiReadModel.model_styles ?? []) {
  const model = modelById.get(style.model_id);
  if (!model) {
    failures.push(`${style.model_id} style row references missing model`);
    continue;
  }
  const rows = apiReadModel.allocations.filter((allocation) => allocation.model_id === style.model_id);
  const portfolioKeys = new Set(rows.map((allocation) => portfolioKey(allocation)));
  const roundIds = new Set(rows.map((allocation) => allocation.round_id));
  if (style.portfolio_count !== portfolioKeys.size) {
    failures.push(`${style.model_id} style portfolio_count ${style.portfolio_count} does not match allocation portfolio count ${portfolioKeys.size}`);
  }
  if (style.sample_round_count !== roundIds.size) {
    failures.push(`${style.model_id} style sample_round_count ${style.sample_round_count} does not match allocation round count ${roundIds.size}`);
  }

  let weightedRisk = 0;
  let totalPct = 0;
  let highRiskPct = 0;
  let defensivePct = 0;
  let techPct = 0;
  let cashPct = 0;
  let equityPct = 0;
  const categoryPct = new Map();
  for (const row of rows) {
    const asset = assetById.get(row.option_id);
    const score = riskScore(asset);
    weightedRisk += row.allocation_pct * score;
    totalPct += row.allocation_pct;
    if (score >= 4) highRiskPct += row.allocation_pct;
    if (isDefensive(row.option_id, asset)) defensivePct += row.allocation_pct;
    if (isTechnology(row.option_id, asset)) techPct += row.allocation_pct;
    if (asset?.is_cash) cashPct += row.allocation_pct;
    if (String(asset?.asset_class ?? "").toLowerCase() === "equity") equityPct += row.allocation_pct;
    const category = asset?.category ?? row.category ?? "unknown";
    categoryPct.set(category, (categoryPct.get(category) ?? 0) + row.allocation_pct);
  }
  const divisor = portfolioKeys.size || 1;
  const expectedRiskScore = totalPct > 0 ? weightedRisk / totalPct : null;
  const expectedTopCategory = Array.from(categoryPct.entries()).sort((a, b) => b[1] - a[1])[0]?.[0] ?? null;
  if (expectedRiskScore === null) {
    if (style.risk_appetite_score !== null) failures.push(`${style.model_id} style risk_appetite_score should be null`);
  } else if (!approxEqual(style.risk_appetite_score, expectedRiskScore)) {
    failures.push(`${style.model_id} style risk_appetite_score ${style.risk_appetite_score} does not match expected ${expectedRiskScore}`);
  }
  if (style.risk_appetite_label !== riskLabel(expectedRiskScore)) {
    failures.push(`${style.model_id} style risk_appetite_label ${style.risk_appetite_label} does not match score label ${riskLabel(expectedRiskScore)}`);
  }
  const expectedStylePercentages = {
    cash_allocation_pct: cashPct / divisor,
    equity_allocation_pct: equityPct / divisor,
    thematic_allocation_pct: techPct / divisor,
    high_risk_pct: highRiskPct / divisor,
    defensive_pct: defensivePct / divisor,
    tech_pct: techPct / divisor
  };
  for (const [field, expected] of Object.entries(expectedStylePercentages)) {
    if (!approxEqual(style[field], expected, BASIS_POINT_EPSILON)) {
      failures.push(`${style.model_id} style ${field} ${style[field]} does not match expected ${expected}`);
    }
    percentInRange(style[field], field, `${style.model_id} style`);
  }
  if (style.top_category !== expectedTopCategory) {
    failures.push(`${style.model_id} style top_category ${style.top_category} does not match expected ${expectedTopCategory}`);
  }
}

const cumulativeTracks = ["weekly", "monthly"];
for (const track of cumulativeTracks) {
  const rows = apiReadModel.results.filter((row) => row.track === track);
  if (rows.length === 0) continue;
  const expected = independentCumulativeLeaderboard(track);
  const actual = buildCumulativeLeaderboardData(apiReadModel, track);
  const context = `${track} cumulative leaderboard`;

  for (const [field, expectedValue] of Object.entries(expected.comparison)) {
    const actualValue = actual.comparison[field];
    if (Array.isArray(expectedValue)) {
      if (JSON.stringify(actualValue) !== JSON.stringify(expectedValue)) {
        failures.push(`${context} comparison ${field} ${JSON.stringify(actualValue)} does not match expected ${JSON.stringify(expectedValue)}`);
      }
    } else if (actualValue !== expectedValue) {
      failures.push(`${context} comparison ${field} ${actualValue} does not match expected ${expectedValue}`);
    }
  }

  if (actual.data.length !== expected.data.length) {
    failures.push(`${context} row count ${actual.data.length} does not match expected ${expected.data.length}`);
  }

  for (let index = 0; index < expected.data.length; index += 1) {
    const expectedRow = expected.data[index];
    const actualRow = actual.data[index];
    if (!actualRow) continue;
    const rowContext = `${context}/${expectedRow.model_id}`;
    if (actualRow.model_id !== expectedRow.model_id) {
      failures.push(`${context} rank ${index + 1} model ${actualRow.model_id} does not match expected ${expectedRow.model_id}`);
      continue;
    }
    for (const field of [
      "rank",
      "round_count",
      "tests_required",
      "tests_included",
      "is_rank_eligible",
      "sample_status",
      "wins"
    ]) {
      if (actualRow[field] !== expectedRow[field]) {
        failures.push(`${rowContext} ${field} ${actualRow[field]} does not match expected ${expectedRow[field]}`);
      }
    }
    for (const field of [
      "portfolio_return_pct",
      "benchmark_return_pct",
      "alpha_pp",
      "max_possible_return_pct",
      "capitalbench_score",
      "win_rate_pct",
      "positive_alpha_rate_pct"
    ]) {
      if (!sameNullableNumber(actualRow[field], expectedRow[field])) {
        failures.push(`${rowContext} ${field} ${actualRow[field]} does not match expected ${expectedRow[field]}`);
      }
    }
  }

  const latestRoundId = expected.comparison.completed_round_ids.at(-1);
  const latestRosterSize = new Set(rows.filter((row) => row.round_id === latestRoundId).map((row) => row.model_id)).size;
  if (latestRosterSize === 0) {
    failures.push(`${context} has no latest roster`);
  }
}

if (failures.length > 0) {
  console.error("Public data validation failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(
  JSON.stringify({
    ok: true,
    rounds: apiReadModel.rounds.length,
    results: apiReadModel.results.length,
    returns: apiReadModel.returns.length
  })
);
