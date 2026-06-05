import { existsSync, readdirSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parse as parseYaml } from "yaml";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "../../..");
const roundsRoot = join(repoRoot, "rounds");
const args = process.argv.slice(2);
const options = {
  all: false,
  roundId: null,
  runId: null,
  strict: false,
  returnTolerancePp: 0.05,
  scoreTolerance: 0.2,
  priceToleranceUsd: 0.05
};

for (let index = 0; index < args.length; index += 1) {
  const arg = args[index];
  if (arg === "--all") options.all = true;
  else if (arg === "--round") options.roundId = args[++index];
  else if (arg === "--run-id") options.runId = args[++index];
  else if (arg === "--strict") options.strict = true;
  else if (arg === "--return-tolerance-pp") options.returnTolerancePp = Number(args[++index]);
  else if (arg === "--score-tolerance") options.scoreTolerance = Number(args[++index]);
  else if (arg === "--price-tolerance-usd") options.priceToleranceUsd = Number(args[++index]);
}

function readText(path) {
  if (!existsSync(path)) return "";
  return readFileSync(path, "utf8").trim();
}

function readYaml(path) {
  const text = readText(path);
  return text ? parseYaml(text) ?? {} : {};
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
  const lines = String(text ?? "").trim().split(/\r?\n/).filter(Boolean);
  if (!lines.length) return [];
  const headers = parseCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]));
  });
}

function readCsv(path) {
  return parseCsv(readText(path));
}

function numberValue(value) {
  if (value === undefined || value === null || value === "") return null;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function dateToUnix(date, dayOffset = 0) {
  const base = new Date(`${date}T00:00:00Z`);
  base.setUTCDate(base.getUTCDate() + dayOffset);
  return Math.floor(base.getTime() / 1000);
}

function utcDateFromUnix(timestamp) {
  return new Date(timestamp * 1000).toISOString().slice(0, 10);
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

function resolvedRounds() {
  return readdirSync(roundsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name.startsWith("CB-"))
    .map((entry) => {
      const roundPath = join(roundsRoot, entry.name);
      const manifest = readYaml(join(roundPath, "manifest.yaml"));
      const selectedRun = officialRuns(roundPath)[0];
      if (!selectedRun) return null;
      const leaderboardPath = join(roundPath, "runs", selectedRun.runId, "results", "leaderboard.csv");
      if (!existsSync(leaderboardPath)) return null;
      return {
        roundId: String(manifest.round_id ?? entry.name),
        entryDate: String(manifest.entry_date ?? ""),
        exitDate: String(manifest.exit_date ?? ""),
        runId: selectedRun.runId,
        roundPath
      };
    })
    .filter(Boolean)
    .sort((left, right) => `${left.exitDate}:${left.roundId}`.localeCompare(`${right.exitDate}:${right.roundId}`));
}

async function fetchYahooSeries(symbol, entryDate, exitDate) {
  const url =
    `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(symbol)}` +
    `?period1=${dateToUnix(entryDate, -5)}&period2=${dateToUnix(exitDate, 3)}&interval=1d&events=history&includeAdjustedClose=true`;
  const response = await fetch(url, { headers: { "User-Agent": "Mozilla/5.0" } });
  if (!response.ok) throw new Error(`Yahoo ${symbol} returned HTTP ${response.status}`);
  const payload = await response.json();
  const result = payload?.chart?.result?.[0];
  if (!result) throw new Error(`Yahoo ${symbol} returned no chart result`);

  const timestamps = result.timestamp ?? [];
  const quote = result.indicators?.quote?.[0] ?? {};
  const adjclose = result.indicators?.adjclose?.[0]?.adjclose ?? [];
  const rows = new Map();
  for (let index = 0; index < timestamps.length; index += 1) {
    const date = utcDateFromUnix(timestamps[index]);
    const adjusted = adjclose[index];
    const close = quote.close?.[index];
    rows.set(date, {
      price: typeof adjusted === "number" ? adjusted : close,
      source: typeof adjusted === "number" ? "yahoo_chart_adjclose" : "yahoo_chart_close"
    });
  }

  const marketTimeDate = result.meta?.regularMarketTime ? utcDateFromUnix(result.meta.regularMarketTime) : "";
  if (marketTimeDate === exitDate && typeof result.meta?.regularMarketPrice === "number") {
    const existing = rows.get(exitDate);
    if (!existing || typeof existing.price !== "number") {
      rows.set(exitDate, {
        price: result.meta.regularMarketPrice,
        source: "yahoo_regular_market_price"
      });
    }
  }
  return rows;
}

function materialDifference(value, tolerance) {
  return Number.isFinite(value) && Math.abs(value) > tolerance;
}

function pct(value) {
  return `${Number(value).toFixed(4)}%`;
}

function selectedRounds() {
  if (options.roundId) {
    const roundPath = join(roundsRoot, options.roundId);
    if (!existsSync(roundPath)) throw new Error(`Round not found: ${options.roundId}`);
    const manifest = readYaml(join(roundPath, "manifest.yaml"));
    const runId = options.runId ?? officialRuns(roundPath)[0]?.runId;
    return [{
      roundId: String(manifest.round_id ?? options.roundId),
      entryDate: String(manifest.entry_date ?? ""),
      exitDate: String(manifest.exit_date ?? ""),
      runId,
      roundPath
    }];
  }
  if (options.all) return resolvedRounds();
  const latest = resolvedRounds().at(-1);
  if (!latest) throw new Error("No resolved rounds found");
  return [latest];
}

async function auditRound(round) {
if (!round.runId) throw new Error(`No official run found for ${round.roundId}`);

const resultsPath = join(round.roundPath, "runs", round.runId, "results");
const returns = readCsv(join(resultsPath, "returns.csv"));
const leaderboard = readCsv(join(resultsPath, "leaderboard.csv"));
const allocations = readCsv(join(resultsPath, "allocations.csv"));
const externalReturnByOption = new Map();
const externalRows = [];
const missingRows = [];

for (const row of returns) {
  if (row.option_id === "CASH" || String(row.is_cash).toLowerCase() === "true") {
    externalReturnByOption.set(row.option_id, 0);
    continue;
  }
  try {
    const series = await fetchYahooSeries(row.asset_symbol, round.entryDate, round.exitDate);
    const entry = series.get(round.entryDate);
    const exit = series.get(round.exitDate);
    if (typeof entry?.price !== "number" || typeof exit?.price !== "number") {
      missingRows.push(`${row.option_id}/${row.asset_symbol}`);
      continue;
    }
    const externalReturn = (exit.price / entry.price - 1) * 100;
    const localReturn = numberValue(row.return) * 100;
    const entryDiff = entry.price - numberValue(row.entry_price);
    const exitDiff = exit.price - numberValue(row.exit_price);
    const returnDiff = externalReturn - localReturn;
    externalReturnByOption.set(row.option_id, externalReturn);
    externalRows.push({
      option_id: row.option_id,
      symbol: row.asset_symbol,
      local_return_pct: localReturn,
      external_return_pct: externalReturn,
      return_diff_pp: returnDiff,
      entry_diff_usd: entryDiff,
      exit_diff_usd: exitDiff,
      entry_source: entry.source,
      exit_source: exit.source,
      material:
        materialDifference(returnDiff, options.returnTolerancePp) ||
        materialDifference(entryDiff, options.priceToleranceUsd) ||
        materialDifference(exitDiff, options.priceToleranceUsd)
    });
  } catch (error) {
    missingRows.push(`${row.option_id}/${row.asset_symbol}: ${error.message}`);
  }
}

const localMax = [...returns].sort((left, right) => numberValue(right.return) - numberValue(left.return))[0];
const externalMax = [...externalRows].sort((left, right) => right.external_return_pct - left.external_return_pct)[0];
const allocationsByModel = new Map();
for (const allocation of allocations) {
  const rows = allocationsByModel.get(allocation.model_id) ?? [];
  rows.push(allocation);
  allocationsByModel.set(allocation.model_id, rows);
}

const modelRows = [];
for (const row of leaderboard) {
  const modelAllocations = allocationsByModel.get(row.model_id) ?? [];
  if (!modelAllocations.length) continue;
  const missingHeld = modelAllocations
    .filter((allocation) => !externalReturnByOption.has(allocation.option_id))
    .map((allocation) => allocation.option_id);
  if (missingHeld.length > 0) {
    modelRows.push({
      model_id: row.model_id,
      local_return_pct: numberValue(row.portfolio_return || row.selected_asset_return) * 100,
      external_return_pct: null,
      local_score: numberValue(row.portfolio_return || row.selected_asset_return) * 100 / (numberValue(localMax.return) * 100) * 100,
      external_score: null,
      missing_held_options: missingHeld
    });
    continue;
  }
  const externalReturn = modelAllocations.reduce((total, allocation) => {
    return total + (numberValue(allocation.allocation_bps) / 10_000) * externalReturnByOption.get(allocation.option_id);
  }, 0);
  const externalScore = externalMax ? (externalReturn / externalMax.external_return_pct) * 100 : null;
  modelRows.push({
    model_id: row.model_id,
    local_return_pct: numberValue(row.portfolio_return || row.selected_asset_return) * 100,
    external_return_pct: externalReturn,
    return_diff_pp: externalReturn - numberValue(row.portfolio_return || row.selected_asset_return) * 100,
    local_score: numberValue(row.portfolio_return || row.selected_asset_return) * 100 / (numberValue(localMax.return) * 100) * 100,
    external_score: externalScore,
    score_diff: externalScore === null ? null : externalScore - (numberValue(row.portfolio_return || row.selected_asset_return) * 100 / (numberValue(localMax.return) * 100) * 100)
  });
}

const materialRows = externalRows.filter((row) => row.material).sort((left, right) => Math.abs(right.return_diff_pp) - Math.abs(left.return_diff_pp));
const materialHeld = new Set(allocations.map((allocation) => allocation.option_id));
const materialHeldRows = materialRows.filter(
  (row) => materialHeld.has(row.option_id) && materialDifference(row.return_diff_pp, options.returnTolerancePp)
);

console.log(`${round.roundId} ${round.entryDate} to ${round.exitDate} (${round.runId})`);
console.log(`Yahoo-covered assets: ${externalRows.length}/${returns.filter((row) => row.option_id !== "CASH").length} non-cash rows`);
console.log(`Missing external rows: ${missingRows.length}${missingRows.length ? ` (${missingRows.slice(0, 12).join(", ")})` : ""}`);
console.log(`Local max: ${localMax.label} (${localMax.asset_symbol}) ${pct(numberValue(localMax.return) * 100)}`);
if (externalMax) console.log(`External covered max: ${externalMax.option_id} (${externalMax.symbol}) ${pct(externalMax.external_return_pct)}`);
console.log("");
console.log("Model impact:");
for (const row of modelRows) {
  if (row.external_return_pct === null) {
    console.log(`  ${row.model_id}: local ${pct(row.local_return_pct)}, external unavailable; missing ${row.missing_held_options.join(", ")}`);
  } else {
    console.log(
      `  ${row.model_id}: return ${pct(row.local_return_pct)} local vs ${pct(row.external_return_pct)} external; ` +
        `score ${row.local_score.toFixed(1)} local vs ${row.external_score.toFixed(1)} external`
    );
  }
}
console.log("");
console.log("Largest external return differences:");
for (const row of materialRows.slice(0, 15)) {
  console.log(
    `  ${row.option_id}/${row.symbol}: local ${pct(row.local_return_pct)} vs external ${pct(row.external_return_pct)} ` +
      `diff ${row.return_diff_pp.toFixed(4)} pp (${row.entry_source} -> ${row.exit_source})`
  );
}

const failed =
  options.strict &&
  (materialHeldRows.length > 0 ||
    modelRows.some(
      (row) =>
        row.external_return_pct !== null &&
        (materialDifference(row.return_diff_pp, options.returnTolerancePp) ||
          materialDifference(row.score_diff, options.scoreTolerance))
    ));
return { failed };
}

let failed = false;
const rounds = selectedRounds();
for (let index = 0; index < rounds.length; index += 1) {
  if (index > 0) console.log("");
  const result = await auditRound(rounds[index]);
  failed ||= result.failed;
}
if (failed) process.exit(1);
