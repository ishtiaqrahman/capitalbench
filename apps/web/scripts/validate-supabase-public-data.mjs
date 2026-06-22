import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import apiReadModel from "../src/generated/apiReadModel.js";

const failures = [];
const appRoot = process.cwd();
const repoRoot = resolve(appRoot, "../..");

function loadEnvFile(path) {
  if (!existsSync(path)) return;
  const text = readFileSync(path, "utf8");
  for (const line of text.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const match = /^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/.exec(trimmed);
    if (!match) continue;
    const [, key, rawValue] = match;
    if (process.env[key]) continue;
    process.env[key] = rawValue.replace(/^['"]|['"]$/g, "");
  }
}

loadEnvFile(join(repoRoot, ".env.local"));
loadEnvFile(join(repoRoot, ".env"));
loadEnvFile(join(appRoot, ".env.local"));
loadEnvFile(join(appRoot, ".env"));

const supabaseUrl = process.env.PUBLIC_SUPABASE_URL ?? process.env.SUPABASE_URL;
const supabaseKey = process.env.PUBLIC_SUPABASE_ANON_KEY ?? process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.log(JSON.stringify({ ok: true, skipped: true, reason: "missing_supabase_env" }));
  process.exit(0);
}

function fail(message) {
  failures.push(message);
}

function publicRoundStatus(status) {
  return status === "active" ? "pending" : status;
}

function normalizeDate(value) {
  return String(value ?? "").slice(0, 10);
}

function normalizeTimestamp(value) {
  const text = String(value ?? "");
  if (!text) return "";
  const date = new Date(text);
  return Number.isNaN(date.getTime()) ? text : date.toISOString().replace(".000Z", "Z");
}

function finiteNumber(value) {
  if (value === null || value === undefined || value === "") return null;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function isBenchmarkOption(optionId, value) {
  return Boolean(value) || String(optionId ?? "").toUpperCase() === "SP500";
}

function readYaml(path, fallback = null) {
  if (!existsSync(path)) return fallback;
  try {
    return parseYaml(readFileSync(path, "utf8"));
  } catch {
    return fallback;
  }
}

function parseCsvRecords(text) {
  const records = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let index = 0; index < text.length; index += 1) {
    const char = text[index];
    if (quoted) {
      if (char === '"' && text[index + 1] === '"') {
        field += '"';
        index += 1;
      } else if (char === '"') {
        quoted = false;
      } else {
        field += char;
      }
    } else if (char === '"') {
      quoted = true;
    } else if (char === ",") {
      row.push(field);
      field = "";
    } else if (char === "\n") {
      row.push(field);
      records.push(row);
      row = [];
      field = "";
    } else if (char !== "\r") {
      field += char;
    }
  }
  if (field || row.length > 0) {
    row.push(field);
    records.push(row);
  }
  return records;
}

function readCsv(path) {
  if (!existsSync(path)) return [];
  const records = parseCsvRecords(readFileSync(path, "utf8"));
  if (records.length === 0) return [];
  const [header, ...rows] = records;
  return rows
    .filter((row) => row.length > 1 || row[0])
    .map((row) => Object.fromEntries(header.map((column, index) => [column, row[index] ?? ""])));
}

const leaderboardCache = new Map();

function leaderboardRows(roundId, runId) {
  const key = `${roundId}:${runId}`;
  if (!leaderboardCache.has(key)) {
    const path = join(repoRoot, "rounds", roundId, "runs", runId, "results", "leaderboard.csv");
    leaderboardCache.set(key, readCsv(path));
  }
  return leaderboardCache.get(key);
}

function assertEqual(actual, expected, context) {
  if (actual !== expected) fail(`${context}: expected ${expected}, got ${actual}`);
}

function assertNear(actual, expected, context, tolerance = 0.000001) {
  const actualNumber = finiteNumber(actual);
  const expectedNumber = finiteNumber(expected);
  if (actualNumber === null || expectedNumber === null || Math.abs(actualNumber - expectedNumber) > tolerance) {
    fail(`${context}: expected ${expected}, got ${actual}`);
  }
}

function assertNullableNear(actual, expected, context, tolerance = 0.000001) {
  if (actual === null || actual === undefined || actual === "") {
    if (expected !== null && expected !== undefined && expected !== "") fail(`${context}: expected ${expected}, got ${actual}`);
    return;
  }
  if (expected === null || expected === undefined || expected === "") {
    fail(`${context}: expected ${expected}, got ${actual}`);
    return;
  }
  assertNear(actual, expected, context, tolerance);
}

function uniquePortfolioKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}`;
}

function runKey(row) {
  return `${row.round_id}:${row.run_id}`;
}

function resultKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}`;
}

function returnKey(row) {
  return `${row.round_id}:${row.run_id}:${row.option_id}`;
}

function allocationKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}:${row.allocation_rank}:${row.option_id}`;
}

function interimPerformanceKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}:${normalizeDate(row.target_date)}`;
}

function optionKey(row) {
  return `${row.round_id}:${row.option_id}`;
}

function latestRound(track, status) {
  return apiReadModel.rounds
    .filter((round) => round.track === track && round.status === status)
    .sort((left, right) =>
      `${right.exit_date}:${right.decision_deadline_utc}:${right.round_id}`.localeCompare(
        `${left.exit_date}:${left.decision_deadline_utc}:${left.round_id}`
      )
    )[0];
}

function average(values) {
  if (values.length === 0) return null;
  return values.reduce((total, value) => total + value, 0) / values.length;
}

function median(values) {
  if (values.length === 0) return null;
  const sorted = [...values].sort((left, right) => left - right);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 1 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
}

function compoundReturn(values) {
  return values.reduce((total, value) => total * (1 + value), 1) - 1;
}

function cumulativeLogAlpha(modelReturns, benchmarkReturns) {
  return modelReturns.reduce((total, modelReturn, index) => {
    const benchmarkReturn = benchmarkReturns[index];
    if (modelReturn <= -1 || benchmarkReturn <= -1) return total;
    return total + Math.log(1 + modelReturn) - Math.log(1 + benchmarkReturn);
  }, 0);
}

const PAGE_SIZE = 1000;

async function selectPage(table, params = {}, offset = 0) {
  const url = new URL(`/rest/v1/${table}`, supabaseUrl);
  for (const [key, value] of Object.entries(params)) url.searchParams.set(key, value);
  url.searchParams.set("limit", String(PAGE_SIZE));
  url.searchParams.set("offset", String(offset));
  const response = await fetch(url, {
    headers: {
      apikey: supabaseKey,
      authorization: `Bearer ${supabaseKey}`,
      accept: "application/json"
    }
  });
  if (!response.ok) {
    throw new Error(`Supabase select failed for ${table}: HTTP ${response.status}`);
  }
  const rows = await response.json();
  if (!Array.isArray(rows)) {
    throw new Error(`Supabase select failed for ${table}: expected array response`);
  }
  return rows;
}

async function select(table, params = {}) {
  const rows = [];
  for (let offset = 0; ; offset += PAGE_SIZE) {
    const page = await selectPage(table, params, offset);
    rows.push(...page);
    if (page.length < PAGE_SIZE) break;
  }
  return rows;
}

function compareRounds(rows) {
  const byId = new Map(rows.map((row) => [row.round_id, row]));
  const expectedIds = new Set(apiReadModel.rounds.map((row) => row.round_id));
  const actualIds = new Set(rows.map((row) => row.round_id));
  assertEqual(rows.length, apiReadModel.rounds.length, "Supabase rounds row count");

  for (const round of apiReadModel.rounds) {
    const actual = byId.get(round.round_id);
    if (!actual) {
      fail(`Supabase rounds missing ${round.round_id}`);
      continue;
    }
    assertEqual(actual.status, publicRoundStatus(round.status), `Supabase rounds ${round.round_id} status`);
    assertEqual(actual.horizon ?? "", round.horizon ?? "", `Supabase rounds ${round.round_id} horizon`);
    assertEqual(Number(actual.horizon_days ?? 0), Number(round.horizon_days ?? 0), `Supabase rounds ${round.round_id} horizon_days`);
    assertEqual(normalizeDate(actual.entry_date), round.entry_date, `Supabase rounds ${round.round_id} entry_date`);
    assertEqual(normalizeDate(actual.exit_date), round.exit_date, `Supabase rounds ${round.round_id} exit_date`);
    assertEqual(normalizeTimestamp(actual.decision_deadline_utc), normalizeTimestamp(round.decision_deadline_utc), `Supabase rounds ${round.round_id} deadline`);
    assertEqual(actual.methodology_version ?? "", round.methodology_version ?? "", `Supabase rounds ${round.round_id} methodology`);
    assertEqual(actual.submission_format ?? "", round.submission_format ?? "", `Supabase rounds ${round.round_id} submission format`);
    assertEqual(actual.universe_version ?? "", round.universe_version ?? "", `Supabase rounds ${round.round_id} universe version`);
  }

  for (const actualId of actualIds) {
    if (!expectedIds.has(actualId)) fail(`Supabase rounds has extra published round ${actualId}`);
  }
}

function expectedRuns() {
  return apiReadModel.rounds.map((round) => {
    const manifestPath = join(repoRoot, "rounds", round.round_id, "runs", round.official_run_id, "run_manifest.yaml");
    const manifest = readYaml(manifestPath, {});
    return {
      round_id: round.round_id,
      run_id: round.official_run_id,
      run_type: String(manifest.run_type ?? ""),
      mode: String(manifest.mode ?? ""),
      mock: Boolean(manifest.mock),
      official_score_eligible: Boolean(manifest.official_score_eligible),
      operator_selected_official: Boolean(manifest.operator_selected_official),
      methodology_version: String(manifest.methodology_version ?? ""),
      replicates: Number(manifest.replicates ?? 1),
      model_count: finiteNumber(manifest.model_count),
      valid_submissions: finiteNumber(manifest.valid_submissions),
      invalid_submissions: finiteNumber(manifest.invalid_submissions),
      created_at_utc: manifest.created_at_utc ?? "",
      completed_at_utc: manifest.completed_at_utc ?? ""
    };
  });
}

function compareRuns(rows) {
  const expectedRows = expectedRuns();
  const byKey = new Map(rows.map((row) => [runKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(runKey));
  const actualKeys = new Set(rows.map(runKey));
  assertEqual(rows.length, expectedRows.length, "Supabase runs row count");

  for (const expected of expectedRows) {
    const key = runKey(expected);
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase runs missing ${key}`);
      continue;
    }
    assertEqual(actual.run_type ?? "", expected.run_type, `Supabase runs ${key} run_type`);
    assertEqual(actual.mode ?? "", expected.mode, `Supabase runs ${key} mode`);
    assertEqual(Boolean(actual.mock), expected.mock, `Supabase runs ${key} mock`);
    assertEqual(Boolean(actual.official_score_eligible), expected.official_score_eligible, `Supabase runs ${key} official_score_eligible`);
    assertEqual(Boolean(actual.operator_selected_official), expected.operator_selected_official, `Supabase runs ${key} operator_selected_official`);
    assertEqual(actual.methodology_version ?? "", expected.methodology_version, `Supabase runs ${key} methodology_version`);
    assertEqual(Number(actual.replicates ?? 1), expected.replicates, `Supabase runs ${key} replicates`);
    assertEqual(finiteNumber(actual.model_count), expected.model_count, `Supabase runs ${key} model_count`);
    assertEqual(finiteNumber(actual.valid_submissions), expected.valid_submissions, `Supabase runs ${key} valid_submissions`);
    assertEqual(finiteNumber(actual.invalid_submissions), expected.invalid_submissions, `Supabase runs ${key} invalid_submissions`);
    assertEqual(normalizeTimestamp(actual.created_at_utc), normalizeTimestamp(expected.created_at_utc), `Supabase runs ${key} created_at_utc`);
    assertEqual(normalizeTimestamp(actual.completed_at_utc), normalizeTimestamp(expected.completed_at_utc), `Supabase runs ${key} completed_at_utc`);
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase runs has extra published row ${actualKey}`);
  }
}

function compareModels(rows) {
  const expectedRows = apiReadModel.models;
  const byId = new Map(rows.map((row) => [row.model_id, row]));
  const expectedIds = new Set(expectedRows.map((row) => row.model_id));
  const actualIds = new Set(rows.map((row) => row.model_id));
  assertEqual(rows.length, expectedRows.length, "Supabase models row count");

  for (const expected of expectedRows) {
    const actual = byId.get(expected.model_id);
    if (!actual) {
      fail(`Supabase models missing ${expected.model_id}`);
      continue;
    }
    assertEqual(actual.provider, expected.provider, `Supabase models ${expected.model_id} provider`);
    assertEqual(actual.display_name ?? "", expected.label, `Supabase models ${expected.model_id} display_name`);
  }

  for (const actualId of actualIds) {
    if (!expectedIds.has(actualId)) fail(`Supabase models has extra published model ${actualId}`);
  }
}

function expectedCumulativeOfficialRows() {
  const bySlotModel = new Map();
  for (const row of apiReadModel.results) {
    const slot = `cumulative_${row.track}`;
    const key = `${slot}:${row.model_id}`;
    const existing =
      bySlotModel.get(key) ??
      {
        slot,
        model_id: row.model_id,
        provider: row.provider,
        returns: [],
        benchmarkReturns: [],
        alphas: [],
        regrets: [],
        costs: [],
        roundIds: []
      };
    existing.returns.push((row.portfolio_return_pct ?? row.selected_asset_return_pct) / 100);
    existing.benchmarkReturns.push(row.benchmark_return_pct / 100);
    existing.alphas.push(row.alpha_pp / 100);
    existing.regrets.push(row.regret_vs_best_option_pct / 100);
    const leaderboardRow = leaderboardRows(row.round_id, row.run_id).find((candidate) => candidate.model_id === row.model_id);
    const cost = finiteNumber(leaderboardRow?.cost_usd);
    if (cost !== null) existing.costs.push(cost);
    existing.roundIds.push(row.round_id);
    bySlotModel.set(key, existing);
  }

  return Array.from(bySlotModel.values()).map((row) => ({
    slot: row.slot,
    model_id: row.model_id,
    provider: row.provider,
    resolved_rounds: row.returns.length,
    average_official_return: average(row.returns),
    average_sp500_return: average(row.benchmarkReturns),
    average_alpha_vs_sp500: average(row.alphas),
    median_alpha_vs_sp500: median(row.alphas),
    cumulative_model_return: compoundReturn(row.returns),
    cumulative_sp500_return: compoundReturn(row.benchmarkReturns),
    cumulative_log_alpha: cumulativeLogAlpha(row.returns, row.benchmarkReturns),
    hit_rate_vs_sp500: row.alphas.filter((value) => value > 0).length / row.alphas.length,
    hit_rate_vs_cash: row.returns.filter((value) => value > 0).length / row.returns.length,
    average_regret_vs_best_option: average(row.regrets),
    best_round_alpha: Math.max(...row.alphas),
    worst_round_alpha: Math.min(...row.alphas),
    total_cost_usd: row.costs.length > 0 ? row.costs.reduce((total, value) => total + value, 0) : null,
    average_cost_usd: average(row.costs),
    rounds_included: [...row.roundIds].sort().join(",")
  }));
}

function compareCumulativeOfficial(rows) {
  const expectedRows = expectedCumulativeOfficialRows();
  const byKey = new Map(rows.map((row) => [`${row.slot}:${row.model_id}`, row]));
  const expectedKeys = new Set(expectedRows.map((row) => `${row.slot}:${row.model_id}`));
  const actualKeys = new Set(rows.map((row) => `${row.slot}:${row.model_id}`));
  assertEqual(rows.length, expectedRows.length, "Supabase cumulative_official_leaderboard row count");

  for (const expected of expectedRows) {
    const key = `${expected.slot}:${expected.model_id}`;
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase cumulative_official_leaderboard missing ${key}`);
      continue;
    }
    assertEqual(actual.provider, expected.provider, `Supabase cumulative official ${key} provider`);
    assertEqual(Number(actual.resolved_rounds), expected.resolved_rounds, `Supabase cumulative official ${key} resolved_rounds`);
    assertNear(actual.average_official_return, expected.average_official_return, `Supabase cumulative official ${key} average_official_return`);
    assertNear(actual.average_sp500_return, expected.average_sp500_return, `Supabase cumulative official ${key} average_sp500_return`);
    assertNear(actual.average_alpha_vs_sp500, expected.average_alpha_vs_sp500, `Supabase cumulative official ${key} average_alpha_vs_sp500`);
    assertNear(actual.median_alpha_vs_sp500, expected.median_alpha_vs_sp500, `Supabase cumulative official ${key} median_alpha_vs_sp500`);
    assertNear(actual.cumulative_model_return, expected.cumulative_model_return, `Supabase cumulative official ${key} cumulative_model_return`);
    assertNear(actual.cumulative_sp500_return, expected.cumulative_sp500_return, `Supabase cumulative official ${key} cumulative_sp500_return`);
    assertNear(actual.cumulative_log_alpha, expected.cumulative_log_alpha, `Supabase cumulative official ${key} cumulative_log_alpha`);
    assertNear(actual.hit_rate_vs_sp500, expected.hit_rate_vs_sp500, `Supabase cumulative official ${key} hit_rate_vs_sp500`);
    assertNear(actual.hit_rate_vs_cash, expected.hit_rate_vs_cash, `Supabase cumulative official ${key} hit_rate_vs_cash`);
    assertNear(actual.average_regret_vs_best_option, expected.average_regret_vs_best_option, `Supabase cumulative official ${key} average_regret_vs_best_option`);
    assertNear(actual.best_round_alpha, expected.best_round_alpha, `Supabase cumulative official ${key} best_round_alpha`);
    assertNear(actual.worst_round_alpha, expected.worst_round_alpha, `Supabase cumulative official ${key} worst_round_alpha`);
    assertNullableNear(actual.total_cost_usd, expected.total_cost_usd, `Supabase cumulative official ${key} total_cost_usd`);
    assertNullableNear(actual.average_cost_usd, expected.average_cost_usd, `Supabase cumulative official ${key} average_cost_usd`);
    assertEqual(actual.rounds_included, expected.rounds_included, `Supabase cumulative official ${key} rounds_included`);
    assertEqual(Boolean(actual.published), true, `Supabase cumulative official ${key} published`);
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase cumulative_official_leaderboard has extra published row ${actualKey}`);
  }
}

function compareCumulativeStability(rows) {
  if (rows.length > 0) {
    fail(`Supabase cumulative_stability_leaderboard has ${rows.length} published rows but no stability rows are in the generated public read model`);
  }
}

function compareLatestLeaderboard(track, rows) {
  const latest = latestRound(track, "resolved");
  if (!latest) {
    if (rows.length > 0) fail(`Supabase latest_${track} has ${rows.length} rows but no resolved ${track} round exists`);
    return;
  }
  const expectedRows = apiReadModel.results
    .filter((row) => row.round_id === latest.round_id && row.run_id === latest.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  const byModel = new Map(rows.map((row) => [row.model_id, row]));
  const expectedModelIds = new Set(expectedRows.map((row) => row.model_id));
  const actualModelIds = new Set(rows.map((row) => row.model_id));
  assertEqual(rows.length, expectedRows.length, `Supabase latest_${track} row count`);

  for (const expected of expectedRows) {
    const actual = byModel.get(expected.model_id);
    if (!actual) {
      fail(`Supabase latest_${track} missing ${expected.model_id}`);
      continue;
    }
    assertEqual(actual.slot, `latest_${track}`, `Supabase latest_${track} ${expected.model_id} slot`);
    assertEqual(actual.round_id, expected.round_id, `Supabase latest_${track} ${expected.model_id} round_id`);
    assertEqual(actual.run_id, expected.run_id, `Supabase latest_${track} ${expected.model_id} run_id`);
    assertEqual(actual.provider, expected.provider, `Supabase latest_${track} ${expected.model_id} provider`);
    assertEqual(actual.selected_option_id, expected.selected_option_id, `Supabase latest_${track} ${expected.model_id} selected option`);
    assertEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `Supabase latest_${track} ${expected.model_id} holding count`);
    assertNear(Number(actual.portfolio_return ?? actual.selected_asset_return) * 100, expected.portfolio_return_pct, `Supabase latest_${track} ${expected.model_id} portfolio return`);
    assertNear(Number(actual.sp500_return) * 100, expected.benchmark_return_pct, `Supabase latest_${track} ${expected.model_id} S&P 500 return`);
    assertNear(Number(actual.alpha_vs_sp500) * 100, expected.alpha_pp, `Supabase latest_${track} ${expected.model_id} alpha`);
    assertNear(Number(actual.regret_vs_best_option) * 100, expected.regret_vs_best_option_pct, `Supabase latest_${track} ${expected.model_id} regret`);
  }

  for (const actualModelId of actualModelIds) {
    if (!expectedModelIds.has(actualModelId)) fail(`Supabase latest_${track} has extra published model ${actualModelId}`);
  }
}

function normalizedPortfolio(row) {
  const source = Array.isArray(row.portfolio) ? row.portfolio : Array.isArray(row.allocations) ? row.allocations : [];
  if (source.length === 0 && row.selected_option_id) {
    return [{ option_id: row.selected_option_id, allocation_bps: 10_000 }];
  }
  return source
    .map((allocation) => ({
      option_id: allocation.option_id,
      allocation_bps: Number(allocation.allocation_bps ?? Number(allocation.allocation_pct ?? 0) * 100),
      rationale: String(allocation.rationale ?? allocation.rationale_summary ?? "")
    }))
    .filter((allocation) => allocation.option_id && allocation.allocation_bps > 0)
    .sort((left, right) => left.option_id.localeCompare(right.option_id));
}

function normalizedStringArray(value) {
  if (!Array.isArray(value)) return [];
  return value.map((item) => String(item)).sort();
}

function roundOptions(roundId) {
  const optionsPath = join(repoRoot, "rounds", roundId, "options.yaml");
  const yaml = readYaml(optionsPath, {});
  const options = Array.isArray(yaml?.options) ? yaml.options : [];
  return options
    .filter((option) => option.include_in_universe !== false)
    .map((option, index) => {
      const optionId = String(option.id ?? option.option_id ?? "");
      return {
        round_id: roundId,
        option_id: optionId,
        name: String(option.name ?? option.label ?? option.id ?? option.option_id ?? ""),
        symbol: String(option.symbol ?? option.asset_symbol ?? ""),
        asset_class: String(option.asset_class ?? "unknown"),
        option_group: String(option.option_group ?? option.category ?? "unknown"),
        risk_bucket: String(option.risk_bucket ?? "medium"),
        is_cash: Boolean(option.is_cash),
        is_benchmark: isBenchmarkOption(optionId, option.is_benchmark),
        include_in_universe: option.include_in_universe !== false,
        sort_order: index + 1
      };
    })
    .filter((option) => option.option_id);
}

function compareOptions(rows) {
  const expectedRows = apiReadModel.rounds.flatMap((round) => roundOptions(round.round_id));
  const byKey = new Map(rows.map((row) => [optionKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(optionKey));
  const actualKeys = new Set(rows.map(optionKey));
  assertEqual(rows.length, expectedRows.length, "Supabase options row count");

  for (const expected of expectedRows) {
    const key = optionKey(expected);
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase options missing ${key}`);
      continue;
    }
    assertEqual(actual.name ?? "", expected.name, `Supabase options ${key} name`);
    assertEqual(actual.symbol ?? "", expected.symbol, `Supabase options ${key} symbol`);
    assertEqual(actual.asset_class ?? "", expected.asset_class, `Supabase options ${key} asset_class`);
    assertEqual(actual.option_group ?? "", expected.option_group, `Supabase options ${key} option_group`);
    assertEqual(actual.risk_bucket ?? "", expected.risk_bucket, `Supabase options ${key} risk_bucket`);
    assertEqual(Boolean(actual.is_cash), expected.is_cash, `Supabase options ${key} is_cash`);
    assertEqual(Boolean(actual.is_benchmark), expected.is_benchmark, `Supabase options ${key} is_benchmark`);
    assertEqual(Boolean(actual.include_in_universe), expected.include_in_universe, `Supabase options ${key} include_in_universe`);
    assertEqual(Number(actual.sort_order), expected.sort_order, `Supabase options ${key} sort_order`);
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase options has extra published row ${actualKey}`);
  }
}

function compareSubmissions(rows) {
  const expectedRows = apiReadModel.portfolios;
  const byKey = new Map(rows.map((row) => [uniquePortfolioKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(uniquePortfolioKey));
  const actualKeys = new Set(rows.map(uniquePortfolioKey));
  assertEqual(rows.length, expectedRows.length, "Supabase submissions row count");

  for (const expected of expectedRows) {
    const key = uniquePortfolioKey(expected);
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase submissions missing ${key}`);
      continue;
    }
    assertEqual(actual.provider, expected.provider, `Supabase submissions ${key} provider`);
    assertEqual(actual.mode ?? "", expected.mode ?? "", `Supabase submissions ${key} mode`);
    assertEqual(actual.run_type ?? "", "official", `Supabase submissions ${key} run_type`);
    assertEqual(actual.selected_option_id, expected.selected_option_id, `Supabase submissions ${key} selected option`);
    assertEqual(actual.submission_format, expected.submission_format, `Supabase submissions ${key} submission format`);
    assertEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `Supabase submissions ${key} holding count`);
    assertNear(actual.confidence, expected.confidence, `Supabase submissions ${key} confidence`);
    assertEqual(actual.rationale_summary ?? "", expected.rationale_summary ?? "", `Supabase submissions ${key} rationale summary`);
    assertEqual(actual.portfolio_rationale ?? "", expected.portfolio_rationale ?? "", `Supabase submissions ${key} portfolio rationale`);
    assertEqual(
      JSON.stringify(normalizedStringArray(actual.key_risks)),
      JSON.stringify(normalizedStringArray(expected.key_risks)),
      `Supabase submissions ${key} key risks`
    );

    const actualPortfolio = normalizedPortfolio(actual);
    const expectedPortfolio = normalizedPortfolio(expected);
    assertEqual(actualPortfolio.length, expectedPortfolio.length, `Supabase submissions ${key} allocation count`);
    for (let index = 0; index < expectedPortfolio.length; index += 1) {
      assertEqual(actualPortfolio[index]?.option_id, expectedPortfolio[index]?.option_id, `Supabase submissions ${key} allocation ${index + 1} option`);
      assertEqual(actualPortfolio[index]?.allocation_bps, expectedPortfolio[index]?.allocation_bps, `Supabase submissions ${key} allocation ${index + 1} bps`);
      assertEqual(actualPortfolio[index]?.rationale ?? "", expectedPortfolio[index]?.rationale ?? "", `Supabase submissions ${key} allocation ${index + 1} rationale`);
    }
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase submissions has extra published row ${actualKey}`);
  }
}

function portfolioByKey() {
  return new Map(apiReadModel.portfolios.map((row) => [uniquePortfolioKey(row), row]));
}

function expectedPortfolioMetrics(portfolio) {
  const assets = new Map(apiReadModel.assets.map((asset) => [asset.option_id, asset]));
  const allocations = Array.isArray(portfolio?.allocations) ? portfolio.allocations : [];
  let maxAllocationBps = 0;
  let cashAllocationBps = 0;
  let benchmarkAllocationBps = 0;
  let concentrationHhi = 0;
  for (const allocation of allocations) {
    const allocationBps = Number(allocation.allocation_bps ?? 0);
    const asset = assets.get(allocation.option_id);
    maxAllocationBps = Math.max(maxAllocationBps, allocationBps);
    if (asset?.is_cash) cashAllocationBps += allocationBps;
    if (asset?.is_benchmark || allocation.option_id === "SP500") benchmarkAllocationBps += allocationBps;
    const weight = allocationBps / 10_000;
    concentrationHhi += weight * weight;
  }
  return {
    max_allocation_bps: maxAllocationBps || 10_000,
    cash_allocation_bps: cashAllocationBps,
    benchmark_allocation_bps: benchmarkAllocationBps,
    concentration_hhi: concentrationHhi || null
  };
}

function compareSubmissionAllocations(rows) {
  const expectedRows = apiReadModel.allocations;
  const byKey = new Map(rows.map((row) => [allocationKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(allocationKey));
  const actualKeys = new Set(rows.map(allocationKey));
  assertEqual(rows.length, expectedRows.length, "Supabase submission_allocations row count");

  for (const expected of expectedRows) {
    const key = allocationKey(expected);
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase submission_allocations missing ${key}`);
      continue;
    }
    assertEqual(Number(actual.allocation_bps), Number(expected.allocation_bps), `Supabase submission_allocations ${key} allocation_bps`);
    assertEqual(actual.rationale_summary ?? "", expected.rationale ?? "", `Supabase submission_allocations ${key} rationale`);
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase submission_allocations has extra published row ${actualKey}`);
  }
}

function compareOfficialResults(rows) {
  const expectedRows = apiReadModel.results;
  const portfolios = portfolioByKey();
  const byKey = new Map(rows.map((row) => [resultKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(resultKey));
  const actualKeys = new Set(rows.map(resultKey));
  assertEqual(rows.length, expectedRows.length, "Supabase official_results row count");

  for (const expected of expectedRows) {
    const key = resultKey(expected);
    const actual = byKey.get(key);
    const portfolio = portfolios.get(key);
    if (!actual) {
      fail(`Supabase official_results missing ${key}`);
      continue;
    }
    assertEqual(actual.provider, expected.provider, `Supabase official_results ${key} provider`);
    if (portfolio) assertEqual(actual.mode ?? "", portfolio.mode ?? "", `Supabase official_results ${key} mode`);
    assertEqual(actual.submission_format ?? "", expected.submission_format ?? "", `Supabase official_results ${key} submission_format`);
    assertEqual(actual.selected_option_id ?? "", expected.selected_option_id ?? "", `Supabase official_results ${key} selected_option_id`);
    assertEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `Supabase official_results ${key} holding_count`);
    assertNullableNear(actual.confidence, expected.confidence, `Supabase official_results ${key} confidence`);
    assertNullableNear(actual.selected_asset_return, expected.selected_asset_return_pct / 100, `Supabase official_results ${key} selected_asset_return`);
    assertNullableNear(actual.portfolio_return, expected.portfolio_return_pct / 100, `Supabase official_results ${key} portfolio_return`);
    assertNullableNear(actual.sp500_return, expected.benchmark_return_pct / 100, `Supabase official_results ${key} sp500_return`);
    assertNullableNear(actual.alpha_vs_sp500, expected.alpha_pp / 100, `Supabase official_results ${key} alpha_vs_sp500`);
    assertNullableNear(actual.regret_vs_best_option, expected.regret_vs_best_option_pct / 100, `Supabase official_results ${key} regret_vs_best_option`);
    assertEqual(finiteNumber(actual.rank_among_options), finiteNumber(expected.rank_among_options), `Supabase official_results ${key} rank_among_options`);
    const metrics = expectedPortfolioMetrics(portfolio);
    assertEqual(Number(actual.max_allocation_bps ?? 10_000), metrics.max_allocation_bps, `Supabase official_results ${key} max_allocation_bps`);
    assertEqual(Number(actual.cash_allocation_bps ?? 0), metrics.cash_allocation_bps, `Supabase official_results ${key} cash_allocation_bps`);
    assertEqual(Number(actual.benchmark_allocation_bps ?? 0), metrics.benchmark_allocation_bps, `Supabase official_results ${key} benchmark_allocation_bps`);
    assertNullableNear(actual.concentration_hhi, metrics.concentration_hhi, `Supabase official_results ${key} concentration_hhi`);
    if (portfolio) {
      assertEqual(actual.rationale_summary ?? "", portfolio.rationale_summary ?? "", `Supabase official_results ${key} rationale_summary`);
      assertEqual(
        JSON.stringify(normalizedStringArray(actual.key_risks)),
        JSON.stringify(normalizedStringArray(portfolio.key_risks)),
        `Supabase official_results ${key} key_risks`
      );
    }
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase official_results has extra published row ${actualKey}`);
  }
}

function compareOptionReturns(rows) {
  const expectedRows = apiReadModel.returns;
  const byKey = new Map(rows.map((row) => [returnKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(returnKey));
  const actualKeys = new Set(rows.map(returnKey));
  assertEqual(rows.length, expectedRows.length, "Supabase option_returns row count");

  for (const expected of expectedRows) {
    const key = returnKey(expected);
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase option_returns missing ${key}`);
      continue;
    }
    assertEqual(actual.label ?? "", expected.label ?? "", `Supabase option_returns ${key} label`);
    assertEqual(actual.asset_symbol ?? "", expected.ticker ?? "", `Supabase option_returns ${key} asset_symbol`);
    assertNullableNear(actual.entry_price, expected.entry_price, `Supabase option_returns ${key} entry_price`);
    assertNullableNear(actual.exit_price, expected.exit_price, `Supabase option_returns ${key} exit_price`);
    assertEqual(actual.entry_price_source ?? "", expected.entry_price_source ?? "", `Supabase option_returns ${key} entry_price_source`);
    assertEqual(actual.exit_price_source ?? "", expected.exit_price_source ?? "", `Supabase option_returns ${key} exit_price_source`);
    assertNullableNear(actual.realized_return, expected.return_pct / 100, `Supabase option_returns ${key} realized_return`);
    assertEqual(Number(actual.rank), Number(expected.rank), `Supabase option_returns ${key} rank`);
    assertEqual(Boolean(actual.is_benchmark), Boolean(expected.is_benchmark), `Supabase option_returns ${key} is_benchmark`);
    assertEqual(Boolean(actual.is_cash), Boolean(expected.is_cash), `Supabase option_returns ${key} is_cash`);
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase option_returns has extra published row ${actualKey}`);
  }
}

function compareRoundWeeklyPerformance(rows) {
  const expectedRows = (apiReadModel.interim_performance ?? []).filter((row) => row.published === true);
  const byKey = new Map(rows.map((row) => [interimPerformanceKey(row), row]));
  const expectedKeys = new Set(expectedRows.map(interimPerformanceKey));
  const actualKeys = new Set(rows.map(interimPerformanceKey));
  assertEqual(rows.length, expectedRows.length, "Supabase round_weekly_performance row count");

  for (const expected of expectedRows) {
    const key = interimPerformanceKey(expected);
    const actual = byKey.get(key);
    if (!actual) {
      fail(`Supabase round_weekly_performance missing ${key}`);
      continue;
    }
    assertEqual(actual.provider, expected.provider, `Supabase round_weekly_performance ${key} provider`);
    assertEqual(normalizeDate(actual.price_date), expected.price_date, `Supabase round_weekly_performance ${key} price_date`);
    assertEqual(Number(actual.days_elapsed), Number(expected.days_elapsed), `Supabase round_weekly_performance ${key} days_elapsed`);
    assertEqual(actual.run_type ?? "", expected.run_type ?? "", `Supabase round_weekly_performance ${key} run_type`);
    assertEqual(actual.submission_format ?? "", expected.submission_format ?? "", `Supabase round_weekly_performance ${key} submission_format`);
    assertEqual(actual.selected_option_id ?? "", expected.selected_option_id ?? "", `Supabase round_weekly_performance ${key} selected_option_id`);
    assertEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `Supabase round_weekly_performance ${key} holding_count`);
    assertNear(Number(actual.model_return) * 100, expected.model_return_pct, `Supabase round_weekly_performance ${key} model_return`);
    assertNear(Number(actual.sp500_return) * 100, expected.sp500_return_pct, `Supabase round_weekly_performance ${key} sp500_return`);
    assertNear(Number(actual.alpha_vs_sp500) * 100, expected.alpha_pp, `Supabase round_weekly_performance ${key} alpha_vs_sp500`);
    assertEqual(actual.price_status ?? "", expected.price_status ?? "", `Supabase round_weekly_performance ${key} price_status`);
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase round_weekly_performance has extra published row ${actualKey}`);
  }
}

const rounds = await select("rounds", {
  select: "round_id,status,horizon,horizon_days,entry_date,exit_date,decision_deadline_utc,methodology_version,submission_format,universe_version",
  published: "eq.true",
  order: "decision_deadline_utc.desc"
});
compareRounds(rounds);

const runs = await select("runs", {
  select:
    "round_id,run_id,run_type,mode,mock,official_score_eligible,operator_selected_official,methodology_version,replicates,model_count,valid_submissions,invalid_submissions,created_at_utc,completed_at_utc",
  published: "eq.true",
  order: "round_id.desc,run_id.asc"
});
compareRuns(runs);

const models = await select("models", {
  select: "model_id,provider,display_name",
  published: "eq.true",
  order: "model_id.asc"
});
compareModels(models);

const options = await select("options", {
  select: "round_id,option_id,name,symbol,asset_class,option_group,risk_bucket,is_cash,is_benchmark,include_in_universe,sort_order",
  published: "eq.true",
  order: "round_id.desc,sort_order.asc"
});
compareOptions(options);

const officialResults = await select("official_results", {
  select:
    "round_id,run_id,model_id,provider,mode,submission_format,selected_option_id,confidence,selected_asset_return,portfolio_return,sp500_return,alpha_vs_sp500,regret_vs_best_option,rank_among_options,holding_count,max_allocation_bps,cash_allocation_bps,benchmark_allocation_bps,concentration_hhi,rationale_summary,key_risks",
  published: "eq.true",
  order: "round_id.desc,model_id.asc"
});
compareOfficialResults(officialResults);

const optionReturns = await select("option_returns", {
  select:
    "round_id,run_id,option_id,label,asset_symbol,entry_price,exit_price,entry_price_source,exit_price_source,realized_return,rank,is_benchmark,is_cash",
  published: "eq.true",
  order: "round_id.desc,rank.asc"
});
compareOptionReturns(optionReturns);

for (const track of ["weekly", "monthly"]) {
  const rows = await select("latest_leaderboard", {
    select: "slot,round_id,run_id,model_id,provider,selected_option_id,holding_count,portfolio_return,selected_asset_return,sp500_return,alpha_vs_sp500,regret_vs_best_option",
    published: "eq.true",
    slot: `eq.latest_${track}`,
    order: "alpha_vs_sp500.desc"
  });
  compareLatestLeaderboard(track, rows);
}

const cumulativeOfficial = await select("cumulative_official_leaderboard", {
  select:
    "slot,model_id,provider,resolved_rounds,average_official_return,average_sp500_return,average_alpha_vs_sp500,median_alpha_vs_sp500,cumulative_model_return,cumulative_sp500_return,cumulative_log_alpha,hit_rate_vs_sp500,hit_rate_vs_cash,average_regret_vs_best_option,best_round_alpha,worst_round_alpha,total_cost_usd,average_cost_usd,rounds_included,published",
  published: "eq.true",
  order: "slot.asc,model_id.asc"
});
compareCumulativeOfficial(cumulativeOfficial);

const cumulativeStability = await select("cumulative_stability_leaderboard", {
  select: "slot,model_id,published",
  published: "eq.true",
  order: "slot.asc,model_id.asc"
});
compareCumulativeStability(cumulativeStability);

const submissions = await select("submissions", {
  select: "round_id,run_id,model_id,provider,mode,run_type,selected_option_id,submission_format,holding_count,confidence,rationale_summary,portfolio_rationale,key_risks,portfolio",
  published: "eq.true",
  order: "round_id.desc"
});
compareSubmissions(submissions);

const submissionAllocations = await select("submission_allocations", {
  select: "round_id,run_id,model_id,replicate_index,option_id,allocation_bps,allocation_rank,rationale_summary",
  published: "eq.true",
  order: "round_id.desc,model_id.asc,allocation_rank.asc"
});
compareSubmissionAllocations(submissionAllocations);

const weeklyPerformance = await select("round_weekly_performance", {
  select:
    "round_id,run_id,model_id,provider,target_date,price_date,days_elapsed,run_type,submission_format,selected_option_id,holding_count,model_return,sp500_return,alpha_vs_sp500,price_status",
  published: "eq.true",
  order: "round_id.desc,target_date.asc,model_id.asc"
});
compareRoundWeeklyPerformance(weeklyPerformance);

if (failures.length > 0) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log(
  JSON.stringify({
    ok: true,
    supabase_public_data_checks: true,
    rounds: rounds.length,
    runs: runs.length,
    models: models.length,
    options: options.length,
    official_results: officialResults.length,
    option_returns: optionReturns.length,
    submissions: submissions.length,
    submission_allocations: submissionAllocations.length,
    weekly_performance: weeklyPerformance.length,
    cumulative_official: cumulativeOfficial.length,
    cumulative_stability: cumulativeStability.length
  })
);
