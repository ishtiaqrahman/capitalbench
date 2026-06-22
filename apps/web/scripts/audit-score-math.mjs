import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import { capitalBenchScore, cumulativeCapitalBenchScore } from "../src/lib/capitalBenchScore.js";
import { numberValue, pctLabel, portfolioReturnValue, scoreLabel } from "./audit-score-math-helpers.mjs";

const repoRoot = resolve(process.cwd(), "../..");
const roundsRoot = join(repoRoot, "rounds");
const EPSILON = 1e-8;
const BASIS_POINT_EPSILON = 1e-5;
const args = new Set(process.argv.slice(2));
const verbose = args.has("--verbose");

const failures = [];

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
  const lines = String(text ?? "").trim().split(/\r?\n/).filter(Boolean);
  if (lines.length === 0) return [];
  const [headerLine, ...rowLines] = lines;
  const headers = parseCsvLine(headerLine);
  return rowLines.map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]));
  });
}

function readCsv(path) {
  if (!existsSync(path)) return [];
  return parseCsv(readFileSync(path, "utf8"));
}

function readYaml(path) {
  if (!existsSync(path)) return {};
  return parseYaml(readFileSync(path, "utf8")) ?? {};
}

function closeEnough(actual, expected, epsilon = EPSILON) {
  return Number.isFinite(actual) && Number.isFinite(expected) && Math.abs(actual - expected) <= epsilon;
}

function fail(context, message) {
  failures.push(`${context}: ${message}`);
}

function trackFromRound(roundId, manifest) {
  const id = String(roundId ?? "").toUpperCase();
  const horizon = String(manifest.horizon ?? "").toLowerCase();
  if (id.endsWith("-1W") || horizon.includes("week")) return "weekly";
  if (id.endsWith("-1M") || horizon.includes("month")) return "monthly";
  return Number(manifest.horizon_days ?? 0) <= 10 ? "weekly" : "monthly";
}

function officialRuns(roundPath) {
  const runsPath = join(roundPath, "runs");
  if (!existsSync(runsPath)) return [];
  return readdirSync(runsPath, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => ({
      runId: entry.name,
      manifest: readYaml(join(runsPath, entry.name, "run_manifest.yaml"))
    }))
    .filter(
      (run) =>
        run.manifest.run_type === "official" &&
        run.manifest.official_score_eligible === true &&
        Number(run.manifest.invalid_submissions ?? 0) === 0
    )
    .sort((left, right) => {
      if (left.manifest.operator_selected_official && !right.manifest.operator_selected_official) return -1;
      if (!left.manifest.operator_selected_official && right.manifest.operator_selected_official) return 1;
      return left.runId.localeCompare(right.runId);
    });
}

function optionDisplay(row) {
  const symbol = row.asset_symbol || row.symbol || "";
  const label = row.label || row.option_id;
  return symbol ? `${label} (${symbol})` : label;
}

function resolvedRoundInputs() {
  if (!existsSync(roundsRoot)) throw new Error(`Missing rounds directory: ${roundsRoot}`);
  return readdirSync(roundsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name.startsWith("CB-"))
    .flatMap((entry) => {
      const roundPath = join(roundsRoot, entry.name);
      const manifest = readYaml(join(roundPath, "manifest.yaml"));
      const roundId = String(manifest.round_id ?? entry.name);
      const selectedRun = officialRuns(roundPath)[0];
      if (!selectedRun) return [];
      const resultsPath = join(roundPath, "runs", selectedRun.runId, "results");
      if (!existsSync(join(resultsPath, "leaderboard.csv"))) return [];
      return [
        {
          roundId,
          runId: selectedRun.runId,
          track: trackFromRound(roundId, manifest),
          entryDate: String(manifest.entry_date ?? ""),
          exitDate: String(manifest.exit_date ?? ""),
          resultsPath
        }
      ];
    })
    .sort((left, right) => `${left.exitDate}:${left.roundId}`.localeCompare(`${right.exitDate}:${right.roundId}`));
}

function auditRound(round) {
  const leaderboard = readCsv(join(round.resultsPath, "leaderboard.csv"));
  const returns = readCsv(join(round.resultsPath, "returns.csv"));
  const allocations = readCsv(join(round.resultsPath, "allocations.csv"));
  const context = `${round.roundId}/${round.runId}`;

  if (leaderboard.length === 0) fail(context, "missing leaderboard rows");
  if (returns.length === 0) fail(context, "missing return rows");
  if (allocations.length === 0) fail(context, "missing allocation rows");

  const returnRows = returns
    .map((row) => ({ ...row, returnValue: numberValue(row.return) }))
    .filter((row) => row.option_id && row.returnValue !== null);
  const maxReturnRow = [...returnRows].sort((left, right) => right.returnValue - left.returnValue)[0];
  const benchmarkRow =
    returnRows.find((row) => String(row.is_benchmark).toLowerCase() === "true") ??
    returnRows.find((row) => row.option_id === "SP500");
  if (!maxReturnRow) fail(context, "could not identify max-return asset");
  if (!benchmarkRow) fail(context, "could not identify S&P 500 benchmark row");

  const returnByOption = new Map(returnRows.map((row) => [row.option_id, row.returnValue]));
  const allocationsByModel = new Map();
  for (const allocation of allocations) {
    if (!allocation.model_id) continue;
    const rows = allocationsByModel.get(allocation.model_id) ?? [];
    rows.push(allocation);
    allocationsByModel.set(allocation.model_id, rows);
  }

  const rowAudits = [];
  for (const row of leaderboard) {
    const rowContext = `${context}/${row.model_id}`;
    const modelAllocations = allocationsByModel.get(row.model_id) ?? [];
    const allocationTotalBps = modelAllocations.reduce((total, allocation) => total + Number(allocation.allocation_bps ?? 0), 0);
    if (!closeEnough(allocationTotalBps, 10000, BASIS_POINT_EPSILON)) {
      fail(rowContext, `allocation_bps total ${allocationTotalBps} does not equal 10000`);
    }

    let weightedReturn = 0;
    for (const allocation of modelAllocations) {
      const optionReturn = returnByOption.get(allocation.option_id);
      const allocationBps = numberValue(allocation.allocation_bps);
      const allocationReturn = numberValue(allocation.option_return);
      const contribution = numberValue(allocation.return_contribution);
      if (optionReturn === undefined || allocationBps === null) {
        fail(rowContext, `missing return/allocation for ${allocation.option_id}`);
        continue;
      }
      weightedReturn += (allocationBps / 10000) * optionReturn;
      if (allocationReturn !== null && !closeEnough(allocationReturn, optionReturn)) {
        fail(rowContext, `${allocation.option_id} option_return ${allocationReturn} does not match returns.csv ${optionReturn}`);
      }
      const expectedContribution = (allocationBps / 10000) * optionReturn;
      if (contribution !== null && !closeEnough(contribution, expectedContribution)) {
        fail(rowContext, `${allocation.option_id} contribution ${contribution} does not match ${expectedContribution}`);
      }
    }

    const portfolioReturn = portfolioReturnValue(row);
    const selectedReturn = numberValue(row.selected_asset_return);
    const benchmarkReturn = numberValue(row.sp500_return);
    const alpha = numberValue(row.alpha_vs_sp500);
    const regret = numberValue(row.regret_vs_best_option);
    const selectedOptionReturn = returnByOption.get(row.selected_option_id);
    const maxReturn = maxReturnRow?.returnValue;
    const expectedAlpha = portfolioReturn !== null && benchmarkRow ? portfolioReturn - benchmarkRow.returnValue : null;
    const expectedRegret = portfolioReturn !== null && maxReturn !== undefined ? maxReturn - portfolioReturn : null;
    const score = portfolioReturn !== null && maxReturn !== undefined
      ? capitalBenchScore(portfolioReturn, maxReturn)
      : null;

    if (portfolioReturn === null) {
      fail(rowContext, "missing portfolio_return");
    } else if (!closeEnough(portfolioReturn, weightedReturn, 1e-7)) {
      fail(rowContext, `portfolio_return ${portfolioReturn} does not match weighted return ${weightedReturn}`);
    }
    if (selectedReturn !== null && selectedOptionReturn !== undefined && !closeEnough(selectedReturn, selectedOptionReturn)) {
      fail(rowContext, `selected_asset_return ${selectedReturn} does not match selected option return ${selectedOptionReturn}`);
    }
    if (benchmarkReturn !== null && benchmarkRow && !closeEnough(benchmarkReturn, benchmarkRow.returnValue)) {
      fail(rowContext, `sp500_return ${benchmarkReturn} does not match benchmark return ${benchmarkRow.returnValue}`);
    }
    if (alpha !== null && expectedAlpha !== null && !closeEnough(alpha, expectedAlpha)) {
      fail(rowContext, `alpha_vs_sp500 ${alpha} does not match portfolio minus S&P ${expectedAlpha}`);
    }
    if (regret !== null && expectedRegret !== null && !closeEnough(regret, expectedRegret)) {
      fail(rowContext, `regret_vs_best_option ${regret} does not match max minus portfolio ${expectedRegret}`);
    }
    if (score !== null && score > 100 + EPSILON) {
      fail(rowContext, `CapitalBench Score ${score} exceeds the oracle ceiling of 100`);
    }

    rowAudits.push({
      model_id: row.model_id,
      provider: row.provider,
      portfolioReturn,
      weightedReturn,
      benchmarkReturn: benchmarkRow?.returnValue,
      maxReturn,
      score,
      allocations: modelAllocations.map((allocation) => ({
        option_id: allocation.option_id,
        allocation_pct: numberValue(allocation.allocation_pct),
        option_return: returnByOption.get(allocation.option_id)
      }))
    });
  }

  rowAudits.sort((left, right) => (right.score ?? -Infinity) - (left.score ?? -Infinity));
  return {
    ...round,
    maxReturnRow,
    benchmarkRow,
    rows: rowAudits
  };
}

const roundAudits = resolvedRoundInputs().map(auditRound);
const cumulativeByTrack = new Map();
for (const round of roundAudits) {
  const track = cumulativeByTrack.get(round.track) ?? new Map();
  for (const row of round.rows) {
    const existing = track.get(row.model_id) ?? [];
    existing.push(row);
    track.set(row.model_id, existing);
  }
  cumulativeByTrack.set(round.track, track);
}

for (const round of roundAudits) {
  console.log(`${round.roundId} ${round.track} ${round.entryDate} to ${round.exitDate}`);
  console.log(`  max possible: ${optionDisplay(round.maxReturnRow)} ${pctLabel(round.maxReturnRow.returnValue)}`);
  console.log(`  S&P 500: ${optionDisplay(round.benchmarkRow)} ${pctLabel(round.benchmarkRow.returnValue)}`);
  for (const row of round.rows) {
    console.log(
      `  ${row.model_id}: score ${scoreLabel(row.score)}; portfolio ${pctLabel(row.portfolioReturn)}; best asset ${pctLabel(row.maxReturn)}; S&P ${pctLabel(row.benchmarkReturn)}`
    );
    if (verbose) {
      for (const allocation of row.allocations) {
        console.log(
          `    ${allocation.option_id} ${allocation.allocation_pct.toFixed(1)}% at ${pctLabel(allocation.option_return)}`
        );
      }
    }
  }
}

for (const [track, modelRows] of cumulativeByTrack.entries()) {
  const requiredCount = roundAudits.filter((round) => round.track === track).length;
  console.log(`${track} cumulative score audit (${requiredCount} resolved tests):`);
  const rows = Array.from(modelRows.entries())
    .map(([modelId, modelResults]) => ({
      modelId,
      modelResults,
      eligible: modelResults.length === requiredCount,
      score: cumulativeCapitalBenchScore(
        modelResults.map((row) => row.portfolioReturn),
        modelResults.map((row) => row.maxReturn)
      )
    }))
    .sort((left, right) => Number(right.eligible) - Number(left.eligible) || right.score - left.score);
  for (const row of rows) {
    const totalReturn = row.modelResults.reduce((total, result) => total + result.portfolioReturn, 0);
    const totalMaxReturn = row.modelResults.reduce((total, result) => total + result.maxReturn, 0);
    console.log(
      `  ${row.modelId}: ${scoreLabel(row.score)} = ${pctLabel(totalReturn)} total / ${pctLabel(totalMaxReturn)} oracle ${row.eligible ? "eligible" : `short history ${row.modelResults.length}/${requiredCount}`}`
    );
  }
}

if (failures.length > 0) {
  console.error("Score math audit failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(JSON.stringify({ ok: true, resolved_rounds: roundAudits.length, score_math_audit: true }));
