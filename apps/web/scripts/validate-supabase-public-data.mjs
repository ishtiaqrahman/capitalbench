import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
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
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
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

function uniquePortfolioKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}`;
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

async function select(table, params = {}) {
  const url = new URL(`/rest/v1/${table}`, supabaseUrl);
  for (const [key, value] of Object.entries(params)) url.searchParams.set(key, value);
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
  return response.json();
}

function compareRounds(rows) {
  const byId = new Map(rows.map((row) => [row.round_id, row]));
  const expectedIds = new Set(apiReadModel.rounds.map((row) => row.round_id));
  const actualIds = new Set(rows.map((row) => row.round_id));

  for (const round of apiReadModel.rounds) {
    const actual = byId.get(round.round_id);
    if (!actual) {
      fail(`Supabase rounds missing ${round.round_id}`);
      continue;
    }
    assertEqual(actual.status, publicRoundStatus(round.status), `Supabase rounds ${round.round_id} status`);
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
  assertEqual(rows.length, expectedRows.length, `Supabase latest_${track} row count`);

  for (const expected of expectedRows) {
    const actual = byModel.get(expected.model_id);
    if (!actual) {
      fail(`Supabase latest_${track} missing ${expected.model_id}`);
      continue;
    }
    assertEqual(actual.round_id, expected.round_id, `Supabase latest_${track} ${expected.model_id} round_id`);
    assertEqual(actual.run_id, expected.run_id, `Supabase latest_${track} ${expected.model_id} run_id`);
    assertEqual(actual.selected_option_id, expected.selected_option_id, `Supabase latest_${track} ${expected.model_id} selected option`);
    assertEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `Supabase latest_${track} ${expected.model_id} holding count`);
    assertNear(Number(actual.portfolio_return ?? actual.selected_asset_return) * 100, expected.portfolio_return_pct, `Supabase latest_${track} ${expected.model_id} portfolio return`);
    assertNear(Number(actual.sp500_return) * 100, expected.benchmark_return_pct, `Supabase latest_${track} ${expected.model_id} S&P 500 return`);
    assertNear(Number(actual.alpha_vs_sp500) * 100, expected.alpha_pp, `Supabase latest_${track} ${expected.model_id} alpha`);
    assertNear(Number(actual.regret_vs_best_option) * 100, expected.regret_vs_best_option_pct, `Supabase latest_${track} ${expected.model_id} regret`);
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
      allocation_bps: Number(allocation.allocation_bps ?? Number(allocation.allocation_pct ?? 0) * 100)
    }))
    .filter((allocation) => allocation.option_id && allocation.allocation_bps > 0)
    .sort((left, right) => left.option_id.localeCompare(right.option_id));
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
    assertEqual(actual.selected_option_id, expected.selected_option_id, `Supabase submissions ${key} selected option`);
    assertEqual(actual.submission_format, expected.submission_format, `Supabase submissions ${key} submission format`);
    assertEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `Supabase submissions ${key} holding count`);

    const actualPortfolio = normalizedPortfolio(actual);
    const expectedPortfolio = normalizedPortfolio(expected);
    assertEqual(actualPortfolio.length, expectedPortfolio.length, `Supabase submissions ${key} allocation count`);
    for (let index = 0; index < expectedPortfolio.length; index += 1) {
      assertEqual(actualPortfolio[index]?.option_id, expectedPortfolio[index]?.option_id, `Supabase submissions ${key} allocation ${index + 1} option`);
      assertEqual(actualPortfolio[index]?.allocation_bps, expectedPortfolio[index]?.allocation_bps, `Supabase submissions ${key} allocation ${index + 1} bps`);
    }
  }

  for (const actualKey of actualKeys) {
    if (!expectedKeys.has(actualKey)) fail(`Supabase submissions has extra published row ${actualKey}`);
  }
}

const rounds = await select("rounds", {
  select: "round_id,status,entry_date,exit_date,decision_deadline_utc,methodology_version,submission_format,universe_version",
  published: "eq.true",
  order: "decision_deadline_utc.desc"
});
compareRounds(rounds);

for (const track of ["weekly", "monthly"]) {
  const rows = await select("latest_leaderboard", {
    select: "slot,round_id,run_id,model_id,selected_option_id,holding_count,portfolio_return,selected_asset_return,sp500_return,alpha_vs_sp500,regret_vs_best_option",
    published: "eq.true",
    slot: `eq.latest_${track}`,
    order: "alpha_vs_sp500.desc"
  });
  compareLatestLeaderboard(track, rows);
}

const submissions = await select("submissions", {
  select: "round_id,run_id,model_id,provider,selected_option_id,submission_format,holding_count,portfolio",
  published: "eq.true",
  order: "round_id.desc"
});
compareSubmissions(submissions);

if (failures.length > 0) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log(JSON.stringify({ ok: true, supabase_public_data_checks: true, rounds: rounds.length, submissions: submissions.length }));
