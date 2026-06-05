import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { parse as parseYaml } from "yaml";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildCumulativeLeaderboardData, createMemoryApiAuthRepository, handleDataApiRequest } from "../src/lib/dataApi.js";

const failures = [];
const distRoot = join(process.cwd(), "dist");
const repoRoot = join(process.cwd(), "..", "..");

function readHtml(path) {
  return readFileSync(join(distRoot, path), "utf8");
}

function readRepoText(...segments) {
  const path = join(repoRoot, ...segments);
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

function parseCsvRows(text) {
  const lines = text.trim().split(/\r?\n/).filter(Boolean);
  const [headerLine, ...rowLines] = lines;
  if (!headerLine) return [];
  const headers = parseCsvLine(headerLine);
  return rowLines.map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]));
  });
}

function numberFromCell(value) {
  if (value === undefined || value === "") return null;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function parseYamlText(text) {
  try {
    return parseYaml(text);
  } catch {
    return null;
  }
}

function includes(html, expected, context) {
  if (!html.includes(expected)) failures.push(`${context} missing rendered text: ${expected}`);
}

function collapseWhitespace(value) {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function includesCollapsed(html, expected, context) {
  if (!collapseWhitespace(html).includes(collapseWhitespace(expected))) {
    failures.push(`${context} missing rendered text: ${expected}`);
  }
}

function includesAny(html, expectedValues, context) {
  if (!expectedValues.some((expected) => html.includes(expected))) {
    failures.push(`${context} missing rendered text; expected one of: ${expectedValues.join(" | ")}`);
  }
}

function excludes(html, unexpected, context) {
  if (html.includes(unexpected)) failures.push(`${context} contains stale rendered text: ${unexpected}`);
}

function latestDate(values) {
  return values.filter(Boolean).sort().at(-1);
}

function jsonLdGraphItems(html, context) {
  const match = html.match(/<script[^>]+type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/);
  if (!match) {
    failures.push(`${context} missing JSON-LD script`);
    return [];
  }
  try {
    const parsed = JSON.parse(match[1]);
    return Array.isArray(parsed["@graph"]) ? parsed["@graph"] : [];
  } catch (error) {
    failures.push(`${context} has invalid JSON-LD: ${error.message}`);
    return [];
  }
}

function datasetJsonLd(html, context) {
  const dataset = jsonLdGraphItems(html, context).find((item) => item?.["@type"] === "Dataset");
  if (!dataset) failures.push(`${context} missing Dataset JSON-LD`);
  return dataset ?? {};
}

function htmlSection(html, startNeedle, context) {
  const start = html.indexOf(startNeedle);
  if (start === -1) {
    failures.push(`${context} missing section start: ${startNeedle}`);
    return "";
  }
  const end = html.indexOf("</section>", start);
  if (end === -1) {
    failures.push(`${context} missing section end after: ${startNeedle}`);
    return html.slice(start);
  }
  return html.slice(start, end + "</section>".length);
}

function expectEqual(actual, expected, context) {
  if (actual !== expected) failures.push(`${context} expected ${JSON.stringify(expected)} but found ${JSON.stringify(actual)}`);
}

function expectClose(actual, expected, context, epsilon = 0.00000001) {
  const actualNumber = Number(actual);
  const expectedNumber = Number(expected);
  if (!Number.isFinite(actualNumber) || !Number.isFinite(expectedNumber) || Math.abs(actualNumber - expectedNumber) > epsilon) {
    failures.push(`${context} expected ${expectedNumber} but found ${actualNumber}`);
  }
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

function htmlTextVariants(value) {
  const escaped = htmlText(value);
  return [
    String(value),
    escaped,
    escaped.replaceAll("'", "&#39;"),
    escaped.replaceAll("'", "&#x27;")
  ];
}

function decodeHtmlAttribute(value) {
  return String(value)
    .replaceAll("&quot;", '"')
    .replaceAll("&#34;", '"')
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">")
    .replaceAll("&#39;", "'")
    .replaceAll("&#x27;", "'")
    .replaceAll("&amp;", "&");
}

function decodeAstroProps(value) {
  function decodeArray(items) {
    return items.map(decodeTuple);
  }
  function decodeObject(item) {
    if (typeof item !== "object" || item === null) return item;
    return Object.fromEntries(Object.entries(item).map(([key, tuple]) => [key, decodeTuple(tuple)]));
  }
  const decoders = {
    0: decodeObject,
    1: decodeArray,
    2: (item) => new RegExp(item),
    3: (item) => new Date(item),
    4: (item) => new Map(decodeArray(item)),
    5: (item) => new Set(decodeArray(item)),
    6: (item) => BigInt(item),
    7: (item) => new URL(item),
    8: (item) => new Uint8Array(item),
    9: (item) => new Uint16Array(item),
    10: (item) => new Uint32Array(item),
    11: (item) => Infinity * item
  };
  function decodeTuple(tuple) {
    const [type, payload] = tuple;
    return Object.hasOwn(decoders, type) ? decoders[type](payload) : undefined;
  }
  return decodeObject(JSON.parse(decodeHtmlAttribute(value)));
}

function allAstroIslandProps(html, componentName, { required = true } = {}) {
  const pattern = new RegExp(
    `<astro-island(?=[^>]*component-url="[^"]*${componentName}[^"]*")[^>]*\\sprops="([^"]*)"`,
    "gs"
  );
  const matches = [...html.matchAll(pattern)];
  if (matches.length === 0) {
    if (required) failures.push(`${componentName} island props were not found`);
    return [];
  }
  const props = [];
  for (const match of matches) {
    try {
      props.push(decodeAstroProps(match[1]));
    } catch (error) {
      failures.push(`${componentName} island props could not be decoded: ${error.message}`);
    }
  }
  return props;
}

function astroIslandProps(html, componentName) {
  return allAstroIslandProps(html, componentName)[0] ?? {};
}

async function dataApiBody(path) {
  const result = await handleDataApiRequest({
    request: new Request(`https://www.capitalbench.org${path}`),
    env: { API_AUTH_REQUIRED: "false" },
    authRepo: createMemoryApiAuthRepository(),
    now: new Date(apiReadModel.generated_at)
  });
  if (!result || result.status !== 200) {
    failures.push(`API docs example path ${path} returned ${result?.status ?? "no result"}`);
    return {};
  }
  return result.body ?? {};
}

function includesJsonField(html, key, value, context) {
  includes(html, htmlText(`"${key}": ${JSON.stringify(value)}`), context);
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

function providerLabelForModel(modelId) {
  return apiReadModel.models.find((model) => model.model_id === modelId)?.provider_label ?? modelId;
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

function publicRoundStatus(status) {
  return status === "active" ? "pending" : status;
}

function average(values) {
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : 0;
}

function averageOrNull(values) {
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : null;
}

function normalizedScore(value, ceiling) {
  if (typeof value !== "number" || typeof ceiling !== "number" || !Number.isFinite(value) || !Number.isFinite(ceiling)) return null;
  if (Math.abs(ceiling) < 0.0000001) return Math.abs(value - ceiling) < 0.0000001 ? 100 : 0;
  return (value / ceiling) * 100;
}

function expectedScorecardData(track) {
  const cumulative = buildCumulativeLeaderboardData(apiReadModel, track);
  const roundIds = cumulative.comparison.comparison_round_ids;
  const byRound = new Map();
  for (const roundId of roundIds) {
    const rows = apiReadModel.results.filter((row) => row.track === track && row.round_id === roundId);
    if (rows.length > 0) byRound.set(roundId, rows);
  }

  const benchmarkReturns = [];
  const benchmarkScores = [];
  const maxPossibleReturns = [];
  for (const roundId of roundIds) {
    const row = byRound.get(roundId)?.[0];
    if (!row) continue;
    if (typeof row.benchmark_return_pct === "number") benchmarkReturns.push(row.benchmark_return_pct);
    if (typeof row.max_possible_return_pct === "number") maxPossibleReturns.push(row.max_possible_return_pct);
    const benchmarkScore = normalizedScore(row.benchmark_return_pct, row.max_possible_return_pct);
    if (typeof benchmarkScore === "number") benchmarkScores.push(benchmarkScore);
  }

  const eligibleModels = cumulative.data.filter((row) => row.is_rank_eligible);
  const provisionalModels = cumulative.data.filter((row) => !row.is_rank_eligible);
  const topReturnModel = [...eligibleModels].sort(
    (left, right) =>
      Number(right.portfolio_return_pct ?? -Infinity) - Number(left.portfolio_return_pct ?? -Infinity) ||
      String(left.label).localeCompare(String(right.label))
  )[0];

  return {
    cumulative,
    averageRows: [
      ...eligibleModels.map((row) => ({
        key: row.model_id,
        label: row.label,
        value: row.portfolio_return_pct,
        testsIncluded: row.tests_included,
        testsRequired: row.tests_required,
        isRankEligible: row.is_rank_eligible
      })),
      ...(benchmarkReturns.length
        ? [
            {
              key: "sp500",
              label: "S&P 500",
              value: average(benchmarkReturns),
              testsIncluded: benchmarkReturns.length,
              testsRequired: roundIds.length,
              isRankEligible: benchmarkReturns.length === roundIds.length
            }
          ]
        : []),
      ...(maxPossibleReturns.length
        ? [
            {
              key: "max-possible",
              label: "Max possible",
              value: average(maxPossibleReturns),
              testsIncluded: maxPossibleReturns.length,
              testsRequired: roundIds.length,
              isRankEligible: true
            }
          ]
        : [])
    ],
    normalizedRows: [
      ...cumulative.data.map((row) => ({
        key: row.model_id,
        label: row.label,
        value: row.capitalbench_score,
        averageReturn: row.portfolio_return_pct,
        testsIncluded: row.tests_included,
        testsRequired: row.tests_required,
        isRankEligible: row.is_rank_eligible
      })),
      ...(benchmarkScores.length
        ? [
            {
              key: "sp500",
              label: "S&P 500",
              value: average(benchmarkScores),
              averageReturn: average(benchmarkReturns),
              testsIncluded: benchmarkScores.length,
              testsRequired: roundIds.length,
              isRankEligible: benchmarkScores.length === roundIds.length
            }
          ]
        : [])
    ],
    provisionalModels,
    topReturnModel
  };
}

function cumulativeLeaderScoreAuditText(track, leader) {
  if (!leader) return "";
  const cumulative = buildCumulativeLeaderboardData(apiReadModel, track);
  const values = cumulative.comparison.comparison_round_ids
    .map((roundId) =>
      apiReadModel.results.find((row) => row.track === track && row.round_id === roundId && row.model_id === leader.model_id)?.capitalbench_score
    )
    .filter((value) => typeof value === "number" && Number.isFinite(value))
    .map(scoreLabel);
  if (values.length === 0) return "";
  if (values.length === 1) return `${leader.label} ${scoreLabel(leader.capitalbench_score)} from one resolved test.`;
  return `${leader.label} ${scoreLabel(leader.capitalbench_score)} = average of ${values.join(", ")}. Scores are out of 100, not portfolio returns.`;
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

function validateLivePerformanceIsland(html) {
  const props = astroIslandProps(html, "LivePerformanceChart");
  const pageRows = Array.isArray(props.rows) ? props.rows : [];
  const expectedRows = (apiReadModel.interim_performance ?? []).filter((row) => row.status === "active");
  expectEqual(pageRows.length, expectedRows.length, "homepage live performance island row count");

  const pageByKey = new Map(
    pageRows.map((row) => [`${row.round_id}:${row.run_id}:${row.model_id}:${row.target_date}:${row.price_date}`, row])
  );
  for (const expected of expectedRows) {
    const key = `${expected.round_id}:${expected.run_id}:${expected.model_id}:${expected.target_date}:${expected.price_date}`;
    const actual = pageByKey.get(key);
    if (!actual) {
      failures.push(`homepage live performance island missing row ${key}`);
      continue;
    }
    expectEqual(actual.round_id, expected.round_id, `homepage live performance ${key} round_id`);
    expectEqual(actual.run_id, expected.run_id, `homepage live performance ${key} run_id`);
    expectEqual(actual.model_id, expected.model_id, `homepage live performance ${key} model_id`);
    expectEqual(actual.provider, expected.provider, `homepage live performance ${key} provider`);
    expectEqual(actual.target_date, expected.target_date, `homepage live performance ${key} target_date`);
    expectEqual(actual.price_date, expected.price_date, `homepage live performance ${key} price_date`);
    expectEqual(actual.days_elapsed, expected.days_elapsed, `homepage live performance ${key} days_elapsed`);
    expectEqual(actual.selected_option_id, expected.selected_option_id, `homepage live performance ${key} selected option`);
    expectEqual(actual.holding_count, expected.holding_count, `homepage live performance ${key} holding count`);
    expectEqual(actual.price_status, expected.price_status, `homepage live performance ${key} price status`);
    expectEqual(actual.published, expected.published, `homepage live performance ${key} published`);
    expectEqual(actual.track, expected.track, `homepage live performance ${key} track`);
    expectEqual(actual.status, "pending", `homepage live performance ${key} local status`);
    expectEqual(actual.entry_date, expected.entry_date, `homepage live performance ${key} entry date`);
    expectEqual(actual.exit_date, expected.exit_date, `homepage live performance ${key} exit date`);
    expectClose(actual.model_return, expected.model_return_pct / 100, `homepage live performance ${key} model return`);
    expectClose(actual.sp500_return, expected.sp500_return_pct / 100, `homepage live performance ${key} S&P 500 return`);
    expectClose(actual.alpha_vs_sp500, expected.alpha_pp / 100, `homepage live performance ${key} alpha`);
  }

  for (const actual of pageRows) {
    const key = `${actual.round_id}:${actual.run_id}:${actual.model_id}:${actual.target_date}:${actual.price_date}`;
    if (!expectedRows.some((row) => `${row.round_id}:${row.run_id}:${row.model_id}:${row.target_date}:${row.price_date}` === key)) {
      failures.push(`homepage live performance island has unexpected row ${key}`);
    }
  }
}

function validateActiveExposureIsland(html) {
  function effectiveActualAllocations(submission) {
    const rawAllocations = Array.isArray(submission.portfolio) ? submission.portfolio : [];
    if (rawAllocations.length > 0) return rawAllocations;
    if (!submission.selected_option_id) return [];
    return [
      {
        option_id: submission.selected_option_id,
        allocation_pct: 100,
        allocation_bps: 10000
      }
    ];
  }
  function allocationStats(allocations) {
    return {
      max_allocation_bps: allocations.length ? Math.max(...allocations.map((allocation) => allocation.allocation_bps ?? 0)) : 0,
      cash_allocation_bps: allocations
        .filter((allocation) => String(allocation.option_id).toUpperCase() === "CASH")
        .reduce((total, allocation) => total + Number(allocation.allocation_bps ?? 0), 0),
      benchmark_allocation_bps: allocations
        .filter((allocation) => String(allocation.option_id).toUpperCase() === "SP500")
        .reduce((total, allocation) => total + Number(allocation.allocation_bps ?? 0), 0)
    };
  }
  const props = astroIslandProps(html, "ActiveExposureMap");
  const pageRounds = Array.isArray(props.rounds) ? props.rounds : [];
  const expectedRounds = apiReadModel.rounds.filter(
    (round) => round.status === "active" && ["weekly", "monthly"].includes(round.track) && round.official_run_id
  );
  expectEqual(pageRounds.length, expectedRounds.length, "homepage active exposure island round count");

  const pageByRoundId = new Map(pageRounds.map((item) => [item.round?.round_id, item]));
  for (const expectedRound of expectedRounds) {
    const actualRound = pageByRoundId.get(expectedRound.round_id);
    if (!actualRound) {
      failures.push(`homepage active exposure island missing round ${expectedRound.round_id}`);
      continue;
    }
    expectEqual(actualRound.track, expectedRound.track, `homepage active exposure ${expectedRound.round_id} track`);
    expectEqual(actualRound.round.round_id, expectedRound.round_id, `homepage active exposure ${expectedRound.round_id} round_id`);
    expectEqual(actualRound.round.title, expectedRound.title, `homepage active exposure ${expectedRound.round_id} title`);
    expectEqual(actualRound.round.entry_date, expectedRound.entry_date, `homepage active exposure ${expectedRound.round_id} entry date`);
    expectEqual(actualRound.round.exit_date, expectedRound.exit_date, `homepage active exposure ${expectedRound.round_id} exit date`);
    expectEqual(actualRound.round.status, "pending", `homepage active exposure ${expectedRound.round_id} local status`);
    expectEqual(actualRound.round.official_run_id, expectedRound.official_run_id, `homepage active exposure ${expectedRound.round_id} official run`);

    const expectedPortfolios = apiReadModel.portfolios
      .filter((portfolio) => portfolio.round_id === expectedRound.round_id && portfolio.run_id === expectedRound.official_run_id)
      .sort((left, right) => left.model_id.localeCompare(right.model_id));
    const actualSubmissions = [...(actualRound.submissions ?? [])].sort((left, right) => left.model_id.localeCompare(right.model_id));
    expectEqual(actualSubmissions.length, expectedPortfolios.length, `homepage active exposure ${expectedRound.round_id} submission count`);

    const actualSubmissionByModel = new Map(actualSubmissions.map((submission) => [submission.model_id, submission]));
    for (const expectedPortfolio of expectedPortfolios) {
      const actualSubmission = actualSubmissionByModel.get(expectedPortfolio.model_id);
      const context = `homepage active exposure ${expectedRound.round_id} ${expectedPortfolio.model_id}`;
      if (!actualSubmission) {
        failures.push(`${context} missing submission`);
        continue;
      }
      expectEqual(actualSubmission.round_id, expectedPortfolio.round_id, `${context} round_id`);
      expectEqual(actualSubmission.run_id, expectedPortfolio.run_id, `${context} run_id`);
      expectEqual(actualSubmission.provider, expectedPortfolio.provider, `${context} provider`);
      expectEqual(actualSubmission.selected_option_id, expectedPortfolio.selected_option_id, `${context} selected option`);
      expectEqual(actualSubmission.holding_count, expectedPortfolio.holding_count, `${context} holding count`);
      const expectedStats = allocationStats(expectedPortfolio.allocations);
      expectEqual(actualSubmission.max_allocation_bps, expectedStats.max_allocation_bps, `${context} max allocation`);
      expectEqual(actualSubmission.cash_allocation_bps, expectedStats.cash_allocation_bps, `${context} cash allocation`);
      expectEqual(actualSubmission.benchmark_allocation_bps, expectedStats.benchmark_allocation_bps, `${context} benchmark allocation`);

      const actualAllocations = new Map(effectiveActualAllocations(actualSubmission).map((allocation) => [allocation.option_id, allocation]));
      expectEqual(actualAllocations.size, expectedPortfolio.allocations.length, `${context} allocation count`);
      for (const expectedAllocation of expectedPortfolio.allocations) {
        const actualAllocation = actualAllocations.get(expectedAllocation.option_id);
        const allocationContext = `${context} allocation ${expectedAllocation.option_id}`;
        if (!actualAllocation) {
          failures.push(`${allocationContext} missing`);
          continue;
        }
        expectClose(actualAllocation.allocation_pct, expectedAllocation.allocation_pct, `${allocationContext} pct`);
        expectEqual(actualAllocation.allocation_bps, expectedAllocation.allocation_bps, `${allocationContext} bps`);
      }
    }

    const expectedOptions = roundUniverseOptions(expectedRound.round_id);
    const actualOptions = [...(actualRound.options ?? [])].sort((left, right) => left.sort_order - right.sort_order);
    expectEqual(actualOptions.length, expectedOptions.length, `homepage active exposure ${expectedRound.round_id} option count`);
    const actualOptionById = new Map(actualOptions.map((option) => [option.option_id, option]));
    for (const expectedOption of expectedOptions) {
      const actualOption = actualOptionById.get(expectedOption.option_id);
      const optionContext = `homepage active exposure ${expectedRound.round_id} option ${expectedOption.option_id}`;
      if (!actualOption) {
        failures.push(`${optionContext} missing`);
        continue;
      }
      expectEqual(actualOption.name, expectedOption.name, `${optionContext} name`);
      expectEqual(actualOption.symbol, expectedOption.symbol, `${optionContext} symbol`);
      expectEqual(actualOption.asset_class, expectedOption.asset_class, `${optionContext} asset class`);
      expectEqual(actualOption.option_group, expectedOption.option_group, `${optionContext} option group`);
      expectEqual(actualOption.risk_bucket, expectedOption.risk_bucket, `${optionContext} risk bucket`);
      expectEqual(actualOption.is_cash, expectedOption.is_cash, `${optionContext} cash flag`);
      expectEqual(actualOption.is_benchmark, expectedOption.is_benchmark, `${optionContext} benchmark flag`);
      expectEqual(actualOption.sort_order, expectedOption.sort_order, `${optionContext} sort order`);
    }
  }

  for (const actualRound of pageRounds) {
    if (!expectedRounds.some((round) => round.round_id === actualRound.round?.round_id)) {
      failures.push(`homepage active exposure island has unexpected round ${actualRound.round?.round_id}`);
    }
  }
}

function effectiveSerializedAllocations(submission) {
  const rawAllocations = Array.isArray(submission?.portfolio) ? submission.portfolio : [];
  if (rawAllocations.length > 0) return rawAllocations;
  if (!submission?.selected_option_id) return [];
  return [
    {
      option_id: submission.selected_option_id,
      allocation_pct: 100,
      allocation_bps: 10000
    }
  ];
}

function assertLeaderboardRows(actualRows, expectedRows, context) {
  expectEqual(actualRows.length, expectedRows.length, `${context} row count`);
  const actualByModel = new Map(actualRows.map((row) => [row.model_id, row]));
  for (const expected of expectedRows) {
    const actual = actualByModel.get(expected.model_id);
    const rowContext = `${context} ${expected.model_id}`;
    if (!actual) {
      failures.push(`${rowContext} missing`);
      continue;
    }
    expectEqual(actual.round_id, expected.round_id, `${rowContext} round_id`);
    expectEqual(actual.run_id, expected.run_id, `${rowContext} run_id`);
    expectEqual(actual.provider, expected.provider, `${rowContext} provider`);
    expectEqual(actual.selected_option_id, expected.selected_option_id, `${rowContext} selected option`);
    expectEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `${rowContext} holding count`);
    expectClose(actual.portfolio_return ?? actual.selected_asset_return, expected.portfolio_return_pct / 100, `${rowContext} portfolio return`);
    expectClose(actual.selected_asset_return, expected.selected_asset_return_pct / 100, `${rowContext} selected asset return`);
    expectClose(actual.sp500_return, expected.benchmark_return_pct / 100, `${rowContext} S&P 500 return`);
    expectClose(actual.alpha_vs_sp500, expected.alpha_pp / 100, `${rowContext} alpha`);
    expectClose(actual.regret_vs_best_option, expected.regret_vs_best_option_pct / 100, `${rowContext} regret`);
  }
}

function validateLeaderboardTableIsland(html, round, context) {
  const expectedRows = apiReadModel.results
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  const islands = allAstroIslandProps(html, "LeaderboardTable", { required: expectedRows.length > 0 });
  const island = islands.find((props) => (props.fallbackRows ?? []).some((row) => row.round_id === round.round_id));
  if (expectedRows.length === 0) {
    if (island && (island.fallbackRows ?? []).length > 0) failures.push(`${context} has leaderboard rows for an unscored round`);
    return;
  }
  if (!island) {
    failures.push(`${context} LeaderboardTable island for ${round.round_id} was not found`);
    return;
  }
  assertLeaderboardRows(island.fallbackRows ?? [], expectedRows, `${context} LeaderboardTable fallbackRows`);
}

function validateOfficialPicksIsland(html, round, context) {
  const expectedPortfolios = apiReadModel.portfolios
    .filter((portfolio) => portfolio.round_id === round.round_id && portfolio.run_id === round.official_run_id)
    .sort((left, right) => left.model_id.localeCompare(right.model_id));
  const islands = allAstroIslandProps(html, "OfficialPicksTable", { required: expectedPortfolios.length > 0 });
  const island = islands.find((props) => props.roundId === round.round_id && props.runId === round.official_run_id);
  if (!island) {
    if (expectedPortfolios.length > 0) failures.push(`${context} OfficialPicksTable island for ${round.round_id} was not found`);
    return;
  }
  const actualRows = [...(island.fallbackRows ?? [])].sort((left, right) => left.model_id.localeCompare(right.model_id));
  expectEqual(actualRows.length, expectedPortfolios.length, `${context} OfficialPicksTable row count`);
  const actualByModel = new Map(actualRows.map((row) => [row.model_id, row]));
  for (const expected of expectedPortfolios) {
    const actual = actualByModel.get(expected.model_id);
    const rowContext = `${context} OfficialPicksTable ${expected.model_id}`;
    if (!actual) {
      failures.push(`${rowContext} missing`);
      continue;
    }
    expectEqual(actual.round_id, expected.round_id, `${rowContext} round_id`);
    expectEqual(actual.run_id, expected.run_id, `${rowContext} run_id`);
    expectEqual(actual.provider, expected.provider, `${rowContext} provider`);
    expectEqual(actual.selected_option_id, expected.selected_option_id, `${rowContext} selected option`);
    expectEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `${rowContext} holding count`);

    const actualAllocations = new Map(effectiveSerializedAllocations(actual).map((allocation) => [allocation.option_id, allocation]));
    expectEqual(actualAllocations.size, expected.allocations.length, `${rowContext} allocation count`);
    for (const expectedAllocation of expected.allocations) {
      const actualAllocation = actualAllocations.get(expectedAllocation.option_id);
      const allocationContext = `${rowContext} allocation ${expectedAllocation.option_id}`;
      if (!actualAllocation) {
        failures.push(`${allocationContext} missing`);
        continue;
      }
      expectClose(actualAllocation.allocation_pct ?? Number(actualAllocation.allocation_bps ?? 0) / 100, expectedAllocation.allocation_pct, `${allocationContext} pct`);
      expectClose(actualAllocation.allocation_bps ?? Number(actualAllocation.allocation_pct ?? 0) * 100, expectedAllocation.allocation_bps, `${allocationContext} bps`);
    }
  }

  const expectedOptions = roundUniverseOptions(round.round_id);
  const actualOptions = island.options ?? [];
  if (actualOptions.length > 0) {
    expectEqual(actualOptions.length, expectedOptions.length, `${context} OfficialPicksTable option count`);
  }
}

function validateRoundPerformanceIsland(html, round, context) {
  const expectedRows = (apiReadModel.interim_performance ?? [])
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .sort((left, right) => left.target_date.localeCompare(right.target_date) || left.model_id.localeCompare(right.model_id));
  const islands = allAstroIslandProps(html, "RoundPerformanceChart", { required: round.status !== "resolved" && expectedRows.length > 0 });
  const island = islands.find((props) => props.roundId === round.round_id && props.runId === round.official_run_id);
  if (round.status === "resolved") {
    if (island) failures.push(`${context} has a live performance island after resolution`);
    return;
  }
  if (!island) {
    if (expectedRows.length > 0) failures.push(`${context} RoundPerformanceChart island for ${round.round_id} was not found`);
    return;
  }
  const actualRows = island.fallbackRows ?? [];
  expectEqual(actualRows.length, expectedRows.length, `${context} RoundPerformanceChart row count`);
  const actualByKey = new Map(actualRows.map((row) => [`${row.model_id}:${row.target_date}`, row]));
  for (const expected of expectedRows) {
    const key = `${expected.model_id}:${expected.target_date}`;
    const actual = actualByKey.get(key);
    const rowContext = `${context} RoundPerformanceChart ${key}`;
    if (!actual) {
      failures.push(`${rowContext} missing`);
      continue;
    }
    expectEqual(actual.provider, expected.provider, `${rowContext} provider`);
    expectEqual(actual.price_date, expected.price_date, `${rowContext} price date`);
    expectEqual(Number(actual.days_elapsed), Number(expected.days_elapsed), `${rowContext} days elapsed`);
    expectEqual(actual.selected_option_id, expected.selected_option_id, `${rowContext} selected option`);
    expectEqual(Number(actual.holding_count ?? 1), Number(expected.holding_count ?? 1), `${rowContext} holding count`);
    expectClose(actual.model_return, expected.model_return_pct / 100, `${rowContext} model return`);
    expectClose(actual.sp500_return, expected.sp500_return_pct / 100, `${rowContext} S&P 500 return`);
    expectClose(actual.alpha_vs_sp500, expected.alpha_pp / 100, `${rowContext} alpha`);
  }
}

function assertRowsByJson(actualRows, expectedRows, context) {
  expectEqual(actualRows.length, expectedRows.length, `${context} row count`);
  for (let index = 0; index < expectedRows.length; index += 1) {
    const actual = actualRows[index];
    const expected = expectedRows[index];
    if (!actual) continue;
    for (const [field, expectedValue] of Object.entries(expected)) {
      const actualValue = actual[field];
      const rowContext = `${context} row ${index + 1} ${field}`;
      if (typeof expectedValue === "number") {
        expectClose(actualValue, expectedValue, rowContext);
      } else {
        expectEqual(actualValue ?? "", expectedValue ?? "", rowContext);
      }
    }
  }
}

function stripUndefined(value) {
  if (Array.isArray(value)) return value.map(stripUndefined);
  if (value && typeof value === "object") {
    return Object.fromEntries(
      Object.entries(value)
        .filter(([, item]) => item !== undefined)
        .map(([key, item]) => [key, stripUndefined(item)])
    );
  }
  return value;
}

function assertJsonEqual(actual, expected, context) {
  const actualJson = JSON.stringify(stripUndefined(actual));
  const expectedJson = JSON.stringify(stripUndefined(expected));
  if (actualJson !== expectedJson) {
    failures.push(`${context} serialized data mismatch`);
  }
}

function tableIslandByLabel(html, label, context) {
  const islands = allAstroIslandProps(html, "TableIsland", { required: false });
  const island = islands.find((props) => props.tableLabel === label);
  if (!island) failures.push(`${context} TableIsland '${label}' was not found`);
  return island;
}

function expectedResultReturnTableRows(round) {
  return apiReadModel.returns
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .sort((left, right) => left.rank - right.rank)
    .slice(0, 12)
    .map((row) => ({
      rank: row.rank,
      option_id: row.option_id,
      label: row.label,
      symbol: row.ticker,
      return: percentPointLabel(row.return_pct),
      entry_price: row.entry_price,
      exit_price: row.exit_price
    }));
}

function expectedAttributionTableRows(round) {
  const returnByOption = new Map(
    apiReadModel.returns
      .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
      .map((row) => [row.option_id, row.return_pct])
  );
  return apiReadModel.allocations
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .sort((left, right) => left.model_id.localeCompare(right.model_id) || left.allocation_rank - right.allocation_rank)
    .map((row) => {
      const optionReturn = returnByOption.get(row.option_id) ?? 0;
      return {
        model: modelLabel(row.model_id),
        option_id: row.option_id,
        allocation: allocationPctLabel(row.allocation_pct),
        option_return: percentPointLabel(optionReturn),
        contribution: percentPointLabel((row.allocation_pct / 100) * optionReturn)
      };
    });
}

function expectedPriceTableRows(round) {
  const returns = apiReadModel.returns
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  if (returns.length > 0) {
    const entryById = new Map(roundPriceRows(round.round_id, "entry").map((row) => [row.option_id, row]));
    const exitById = new Map(roundPriceRows(round.round_id, "exit").map((row) => [row.option_id, row]));
    return returns.map((row) => ({
      option_id: row.option_id,
      symbol: row.ticker,
      entry_date: entryById.get(row.option_id)?.date ?? "",
      entry_price: row.entry_price,
      exit_date: exitById.get(row.option_id)?.date ?? "",
      exit_price: row.exit_price,
      return: percentPointLabel(row.return_pct),
      source: row.exit_price_source || row.entry_price_source
    }));
  }
  return roundPriceRows(round.round_id, "entry").map((row) => ({
    option_id: row.option_id,
    symbol: row.symbol,
    entry_date: row.date,
    entry_price: row.price,
    source: row.source
  }));
}

function expectedHashRows(round) {
  const proof = apiReadModel.proof.find((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
  return Object.entries(proof?.hashes?.files ?? {}).map(([path, sha256]) => ({ path, sha256 }));
}

function validateRoundTableIslands(html, round, context) {
  const priceLabel = round.status === "resolved" ? "Scoring prices" : "Starting prices";
  const priceTable = tableIslandByLabel(html, priceLabel, context);
  if (priceTable) assertRowsByJson(priceTable.rows ?? [], expectedPriceTableRows(round), `${context} ${priceLabel}`);

  if (round.status === "resolved") {
    const expectedReturns = expectedResultReturnTableRows(round);
    const returnsTable = tableIslandByLabel(html, "Realized asset returns", context);
    if (returnsTable) assertRowsByJson(returnsTable.rows ?? [], expectedReturns, `${context} realized asset returns`);

    const expectedAttribution = expectedAttributionTableRows(round);
    if (expectedAttribution.length > 0) {
      const attributionTable = tableIslandByLabel(html, "Portfolio attribution", context);
      if (attributionTable) assertRowsByJson(attributionTable.rows ?? [], expectedAttribution, `${context} portfolio attribution`);
    }
  }

  const hashIsland = allAstroIslandProps(html, "HashTable", { required: false })[0];
  if (!hashIsland) {
    failures.push(`${context} HashTable island was not found`);
  } else {
    assertRowsByJson(hashIsland.rows ?? [], expectedHashRows(round), `${context} hash table`);
  }
}

function validateRoundsIndexIsland(html) {
  const island = allAstroIslandProps(html, "RoundsTable", { required: true })[0];
  if (!island) return;
  const expectedRows = apiReadModel.rounds.map((round) => ({
    round_id: round.round_id,
    title: round.title,
    description: round.description,
    decision_date: round.decision_date,
    decision_deadline_utc: round.decision_deadline_utc,
    horizon: round.horizon,
    horizon_days: round.horizon_days,
    entry_date: round.entry_date,
    exit_date: round.exit_date,
    status: publicRoundStatus(round.status),
    methodology_version: round.methodology_version,
    universe_version: round.universe_version,
    submission_format: round.submission_format,
    official_run_id: round.official_run_id
  })).sort((left, right) => right.decision_deadline_utc.localeCompare(left.decision_deadline_utc));
  assertRowsByJson(island.fallbackRows ?? [], expectedRows, "rounds index RoundsTable fallbackRows");
}

function validateUniverseTableIsland(html) {
  const island = allAstroIslandProps(html, "UniverseTable", { required: true })[0];
  if (!island) return;
  const latest = loadUniverseVersions()[0];
  const expectedRows = (latest?.rows ?? []).map((row) => ({
    option_id: row.option_id,
    name: row.label,
    symbol: row.ticker,
    asset_class: row.asset_class,
    option_group: row.category,
    risk_bucket: row.risk_bucket,
    is_cash: row.is_cash,
    is_benchmark: row.is_benchmark,
    sort_order: row.sort_order
  }));
  assertRowsByJson(island.fallbackRows ?? [], expectedRows, "universe page UniverseTable fallbackRows");
  expectEqual(island.disableRemote, true, "universe page UniverseTable remote override disabled");
}

function roundSortKey(round) {
  return `${round.exit_date ?? ""}:${round.decision_deadline_utc ?? ""}:${round.round_id ?? ""}`;
}

function dateLabel(value) {
  const date = new Date(`${String(value).slice(0, 10)}T00:00:00Z`);
  if (!Number.isFinite(date.getTime())) return String(value).slice(0, 10);
  return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

function dateOnly(value) {
  return value ? String(value).slice(0, 10) : "";
}

function latestRound(track, status) {
  return apiReadModel.rounds
    .filter((round) => round.track === track && round.status === status)
    .sort((left, right) => roundSortKey(right).localeCompare(roundSortKey(left)))[0];
}

function latestRoundByTrack(track) {
  return apiReadModel.rounds.find((round) => round.track === track);
}

function roundsForTrack(track) {
  return apiReadModel.rounds.filter((round) => round.track === track);
}

function trackLabel(track) {
  return track === "weekly" ? "Weekly" : "Monthly";
}

function roundTrackLabel(round) {
  return round.track === "weekly" ? "Weekly" : round.track === "monthly" ? "Monthly" : "Other";
}

function trackWindowLabel(round) {
  if (!round) return "No window yet";
  return `${round.entry_date} to ${round.exit_date}`;
}

function scoreEtaLine(round) {
  if (!round) return "No active test.";
  if (round.status === "resolved") return "Scores are published.";
  return `Scores after the ${round.exit_date} close.`;
}

function homepageScoreLine(round) {
  if (!round) return "No score window declared yet.";
  if (round.status === "resolved") return "Scores are published.";
  return `Results publish after the ${dateOnly(round.exit_date)} ending close.`;
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

function numberLabel(value, digits = 1) {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric.toFixed(digits) : "n/a";
}

function riskScoreValue(value) {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? `${numeric.toFixed(2)} / 5` : "n/a";
}

function riskScoreShort(value) {
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric.toFixed(2) : "n/a";
}

function effectiveSpreadLabel(value) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric) || numeric <= 0) return "0 assets";
  return `${numeric.toFixed(1)} assets`;
}

function roundOptionCount(roundId) {
  const text = readRepoText("rounds", roundId, "options.yaml");
  if (!text) return null;
  try {
    const parsed = parseYaml(text);
    return (parsed?.options ?? []).filter((option) => option?.include_in_universe !== false).length;
  } catch {
    return null;
  }
}

function roundUniverseOptions(roundId) {
  const text = readRepoText("rounds", roundId, "options.yaml");
  if (!text) return [];
  const parsed = parseYamlText(text);
  return (parsed?.options ?? [])
    .filter((option) => option?.include_in_universe !== false)
    .map((option, index) => {
      const optionId = String(option.id ?? option.option_id ?? "");
      return {
        option_id: optionId,
        name: String(option.name ?? option.label ?? optionId),
        symbol: String(option.symbol ?? option.asset_symbol ?? ""),
        asset_class: String(option.asset_class ?? "unknown"),
        option_group: String(option.option_group ?? option.category ?? "unknown"),
        risk_bucket: String(option.risk_bucket ?? "medium"),
        is_cash: Boolean(option.is_cash),
        is_benchmark: Boolean(option.is_benchmark) || optionId.toUpperCase() === "SP500",
        sort_order: index + 1
      };
    })
    .filter((option) => option.option_id);
}

function universeLabelFromFilename(filename) {
  const match = /^capitalbench_universe_(v\d+_\d+)\.yaml$/.exec(filename);
  return match ? match[1].replace("_", ".") : filename;
}

function universeVersionParts(label) {
  return label
    .replace(/^v/i, "")
    .split(".")
    .map((part) => Number(part))
    .filter((part) => Number.isFinite(part));
}

function compareUniverseVersionsDesc(left, right) {
  const leftParts = universeVersionParts(left);
  const rightParts = universeVersionParts(right);
  const length = Math.max(leftParts.length, rightParts.length);
  for (let index = 0; index < length; index += 1) {
    const diff = (rightParts[index] ?? 0) - (leftParts[index] ?? 0);
    if (diff !== 0) return diff;
  }
  return right.localeCompare(left);
}

const universeMetadata = {
  "v2.1": {
    status: "Current default for new tests",
    detail: "v2.0 plus Broad AI Technology, Autonomous Technology and Robotics, Cybersecurity, Solar Energy, and Metals and Mining."
  },
  "v2.0": {
    status: "Frozen for v2.0 tests",
    detail: "v1.5 plus country, sector, bond, commodity, currency, and crypto-proxy exposures."
  },
  "v1.5": {
    status: "Frozen for Round 1",
    detail: "Cash, broad US equity, factors, sectors, bonds, international equity, commodities, and AI themes."
  }
};

function loadUniverseVersions() {
  const universePath = join(repoRoot, "configs", "universes");
  return readdirSync(universePath)
    .filter((filename) => /^capitalbench_universe_v\d+_\d+\.yaml$/.test(filename))
    .map((file) => {
      const label = universeLabelFromFilename(file);
      const parsed = parseYamlText(readRepoText("configs", "universes", file));
      const rows = (parsed?.options ?? []).map((option, index) => ({
        option_id: option.id,
        label: option.name,
        ticker: option.symbol ?? "",
        asset_class: option.asset_class,
        category: option.option_group,
        risk_bucket: option.risk_bucket,
        is_cash: Boolean(option.is_cash),
        is_benchmark: Boolean(option.is_benchmark) || String(option.id ?? "").toUpperCase() === "SP500",
        sort_order: index + 1
      }));
      return {
        label,
        file,
        status: universeMetadata[label]?.status ?? "Versioned asset list",
        detail: universeMetadata[label]?.detail ?? "Versioned CapitalBench asset list.",
        rows
      };
    })
    .sort((left, right) => compareUniverseVersionsDesc(left.label, right.label));
}

function roundEntryPriceRows(roundId) {
  const text = readRepoText("rounds", roundId, "prices", "entry_prices.csv");
  if (!text) return [];
  return parseCsvRows(text)
    .map((row) => ({
      option_id: row.option_id,
      symbol: row.symbol ?? "",
      date: row.date ?? "",
      price: numberFromCell(row.price) ?? numberFromCell(row.adj_close) ?? numberFromCell(row.adjClose) ?? numberFromCell(row.close),
      source: row.source || row.price_source || (row.adj_close || row.adjClose ? "adj_close" : "close")
    }))
    .filter((row) => row.option_id && typeof row.price === "number");
}

function roundPriceRows(roundId, side) {
  const text = readRepoText("rounds", roundId, "prices", `${side}_prices.csv`);
  if (!text) return [];
  return parseCsvRows(text)
    .map((row) => ({
      option_id: row.option_id,
      symbol: row.symbol ?? "",
      date: row.date ?? "",
      price: numberFromCell(row.price) ?? numberFromCell(row.adj_close) ?? numberFromCell(row.adjClose) ?? numberFromCell(row.close),
      source: row.source || row.price_source || (row.adj_close || row.adjClose ? "adj_close" : "close")
    }))
    .filter((row) => row.option_id && typeof row.price === "number");
}

function roundProofFileCount(round) {
  const proof = apiReadModel.proof.find((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
  return proof?.hashes?.files ? Object.keys(proof.hashes.files).length : null;
}

function roundPortfolios(round) {
  return apiReadModel.portfolios.filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
}

function roundAllocations(round) {
  return apiReadModel.allocations.filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id);
}

function buildRoundConcentration(round) {
  const portfolios = roundPortfolios(round);
  const allocations = roundAllocations(round);
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
        total_bps: 0,
        holders: []
      };
    existing.total_bps += allocation.allocation_bps;
    existing.holders.push({
      model_id: allocation.model_id,
      provider: allocation.provider,
      allocation_pct: allocation.allocation_pct,
      allocation_bps: allocation.allocation_bps
    });
    byAsset.set(allocation.option_id, existing);
  }
  const assets = Array.from(byAsset.values())
    .map((row) => ({
      ...row,
      holders: row.holders.sort((left, right) => right.allocation_bps - left.allocation_bps),
      average_pct: modelCount > 0 ? row.total_bps / modelCount / 100 : 0
    }))
    .sort((left, right) => right.average_pct - left.average_pct || left.option_id.localeCompare(right.option_id));
  const concentrationScore = assets.reduce((total, asset) => total + (asset.average_pct / 100) ** 2, 0);
  return {
    model_count: modelCount,
    assets,
    top_asset_share_pct: assets[0]?.average_pct ?? 0,
    top_three_share_pct: assets.slice(0, 3).reduce((total, asset) => total + asset.average_pct, 0),
    effective_asset_count: concentrationScore > 0 ? 1 / concentrationScore : 0
  };
}

function latestRoundPerformanceSnapshot(round) {
  const rows = (apiReadModel.interim_performance ?? [])
    .filter(
      (row) =>
        row.round_id === round.round_id &&
        row.run_id === round.official_run_id &&
        row.published !== false &&
        typeof row.model_return_pct === "number" &&
        typeof row.sp500_return_pct === "number" &&
        typeof row.alpha_pp === "number"
    )
    .sort((left, right) => left.target_date.localeCompare(right.target_date) || modelLabel(left.model_id).localeCompare(modelLabel(right.model_id)));
  const dates = Array.from(new Set(rows.map((row) => row.target_date))).sort();
  const latestDate = dates.at(-1);
  const latestRows = latestDate
    ? rows
        .filter((row) => row.target_date === latestDate)
        .sort((left, right) => right.alpha_pp - left.alpha_pp || modelLabel(left.model_id).localeCompare(modelLabel(right.model_id)))
    : [];
  return {
    rows,
    dates,
    latest_date: latestDate,
    latest_rows: latestRows,
    is_renderable: dates.length >= 2 && rows.some((row) => row.days_elapsed > 0) && rows.length > 0
  };
}

function primaryPickCounts(portfolios) {
  const counts = new Map();
  for (const portfolio of portfolios) {
    if (!portfolio.selected_option_id) continue;
    counts.set(portfolio.selected_option_id, (counts.get(portfolio.selected_option_id) ?? 0) + 1);
  }
  let best;
  for (const entry of counts.entries()) {
    if (!best || entry[1] > best[1]) best = entry;
  }
  return best;
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

const GROUP_LABELS = {
  ai_and_technology: "AI and Technology",
  bonds_and_rates: "Bonds and Rates",
  cash: "Cash",
  cash_and_short_duration: "Cash and Short Duration",
  clean_energy: "Clean Energy",
  commodities: "Commodities",
  country_equity: "Country Equity",
  credit: "Credit",
  crypto: "Crypto",
  currencies: "Currencies",
  international_equity: "International Equity",
  us_broad_market: "US Broad Market",
  us_factor_equity: "US Factor Equity",
  us_growth_and_technology: "US Growth and Technology",
  us_industry: "US Industry",
  us_sector: "US Sector",
  us_size_factor: "US Size Factor",
  us_style_factor: "US Style Factor"
};

function groupLabel(value) {
  const normalized = String(value ?? "").toLowerCase();
  if (GROUP_LABELS[normalized]) return GROUP_LABELS[normalized];
  return String(value ?? "Other")
    .replaceAll("_", " ")
    .split(" ")
    .filter(Boolean)
    .map((part) => part[0]?.toUpperCase() + part.slice(1))
    .join(" ") || "Other";
}

function allocationThemeClass(optionId) {
  const normalized = String(optionId ?? "").toUpperCase();
  if (["ENERGY", "OIL", "BROAD_COMMODITIES"].includes(normalized)) return "allocation-energy";
  if (["SEMICONDUCTORS", "TECHNOLOGY", "SOFTWARE", "NASDAQ100", "LARGE_GROWTH"].includes(normalized)) {
    return "allocation-tech";
  }
  if (["GOLD", "MINERS"].includes(normalized)) return "allocation-gold";
  if (["SHORT_TREASURY", "INTERMEDIATE_TREASURY", "LONG_TREASURY", "TIPS", "CASH", "US_DOLLAR"].includes(normalized)) {
    return "allocation-defensive";
  }
  if (["CONSUMER_STAPLES", "UTILITIES", "HEALTHCARE"].includes(normalized)) return "allocation-stable";
  return "allocation-other";
}

function roundScoreEtaUtc(roundId, exitDate) {
  const job = parseYamlText(readRepoText("rounds", roundId, "automation", "resolution_job.yaml"));
  const automationEta = job?.due_at_utc ?? job?.next_attempt_at_utc;
  if (automationEta && Number.isFinite(Date.parse(automationEta))) return automationEta;
  const derivedEta = exitDate ? `${exitDate}T23:30:00Z` : undefined;
  return derivedEta && Number.isFinite(Date.parse(derivedEta)) ? derivedEta : undefined;
}

function expectedModelLiveScope(modelId, scope) {
  const allocations = apiReadModel.allocations.filter(
    (row) => row.model_id === modelId && row.status === "active" && (scope === "all" || row.track === scope)
  );
  const portfolioKeys = new Set(allocations.map(uniquePortfolioKey));
  const weeklyPortfolioKeys = new Set(allocations.filter((row) => row.track === "weekly").map(uniquePortfolioKey));
  const monthlyPortfolioKeys = new Set(allocations.filter((row) => row.track === "monthly").map(uniquePortfolioKey));
  const activeRounds = new Map();
  const holdings = new Map();

  for (const allocation of allocations) {
    const scoreEtaUtc = roundScoreEtaUtc(allocation.round_id, allocation.exit_date);
    activeRounds.set(allocation.round_id, {
      roundId: allocation.round_id,
      track: allocation.track,
      exitDate: allocation.exit_date,
      scoreEtaUtc
    });

    const existing =
      holdings.get(allocation.option_id) ??
      {
        optionId: allocation.option_id,
        label: assetDisplay(allocation),
        shortLabel: optionShortDisplay(allocation),
        symbol: allocation.ticker ?? "",
        group: groupLabel(allocation.category),
        themeClass: allocationThemeClass(allocation.option_id),
        totalBps: 0,
        portfolioKeys: new Set(),
        rounds: []
      };
    existing.totalBps += allocation.allocation_bps;
    existing.portfolioKeys.add(uniquePortfolioKey(allocation));
    existing.rounds.push({
      roundId: allocation.round_id,
      track: allocation.track,
      exitDate: allocation.exit_date,
      scoreEtaUtc,
      allocationPct: allocation.allocation_pct
    });
    holdings.set(allocation.option_id, existing);
  }

  const denominatorBps = portfolioKeys.size * 10_000;
  const holdingRows = Array.from(holdings.values())
    .map((holding) => ({
      optionId: holding.optionId,
      label: holding.label,
      shortLabel: holding.shortLabel,
      symbol: holding.symbol,
      group: holding.group,
      themeClass: holding.themeClass,
      exposurePct: denominatorBps > 0 ? (holding.totalBps / denominatorBps) * 100 : 0,
      portfolioCount: holding.portfolioKeys.size,
      rounds: holding.rounds.sort((left, right) => right.roundId.localeCompare(left.roundId))
    }))
    .sort((left, right) => right.exposurePct - left.exposurePct || left.label.localeCompare(right.label));
  const activeRoundRows = Array.from(activeRounds.values()).sort((left, right) => left.exitDate.localeCompare(right.exitDate));
  const nextScoreDate = activeRoundRows
    .map((round) => round.scoreEtaUtc ?? (round.exitDate ? `${round.exitDate}T23:30:00Z` : undefined))
    .filter(Boolean)
    .sort()[0];

  return {
    key: scope,
    label: scope === "all" ? "All Live" : trackLabel(scope),
    portfolioCount: portfolioKeys.size,
    roundCount: activeRoundRows.length,
    weeklyPortfolioCount: weeklyPortfolioKeys.size,
    monthlyPortfolioCount: monthlyPortfolioKeys.size,
    holdings: holdingRows,
    topHolding: holdingRows[0],
    topThreePct: holdingRows.slice(0, 3).reduce((total, holding) => total + holding.exposurePct, 0),
    nextScoreDate,
    activeRounds: activeRoundRows
  };
}

function expectedModelLiveScopes(modelId) {
  return {
    all: expectedModelLiveScope(modelId, "all"),
    weekly: expectedModelLiveScope(modelId, "weekly"),
    monthly: expectedModelLiveScope(modelId, "monthly")
  };
}

function validateModelLiveHoldingsIsland(html, modelId, context) {
  const props = astroIslandProps(html, "ModelLiveHoldings");
  if (!props.scopes) return;
  assertJsonEqual(props.scopes, expectedModelLiveScopes(modelId), `${context} ModelLiveHoldings scopes`);
}

function modelFingerprint(modelId) {
  const allocations = apiReadModel.allocations.filter((row) => row.model_id === modelId);
  const byPortfolio = new Map();
  for (const allocation of allocations) {
    const key = uniquePortfolioKey(allocation);
    const rows = byPortfolio.get(key) ?? [];
    rows.push(allocation);
    byPortfolio.set(key, rows);
  }
  const portfolioRows = Array.from(byPortfolio.values()).map((rows) =>
    [...rows].sort((left, right) => left.allocation_rank - right.allocation_rank || right.allocation_bps - left.allocation_bps)
  );
  const portfolioCount = portfolioRows.length;
  const denominator = portfolioCount * 10_000;
  const assets = new Map();
  const categories = new Map();

  for (const rows of portfolioRows) {
    for (const allocation of rows) {
      const existing =
        assets.get(allocation.option_id) ??
        {
          option_id: allocation.option_id,
          label: allocation.label,
          ticker: allocation.ticker,
          category: allocation.category,
          total_bps: 0,
          portfolio_keys: new Set(),
          top_pick_count: 0
        };
      existing.total_bps += allocation.allocation_bps;
      existing.portfolio_keys.add(uniquePortfolioKey(allocation));
      if (allocation.allocation_rank === 1) existing.top_pick_count += 1;
      assets.set(allocation.option_id, existing);
      const group = groupLabel(allocation.category);
      categories.set(group, (categories.get(group) ?? 0) + allocation.allocation_bps);
    }
  }

  const assetRows = Array.from(assets.values())
    .map((asset) => ({
      ...asset,
      frequency_pct: portfolioCount > 0 ? (asset.portfolio_keys.size / portfolioCount) * 100 : 0,
      average_allocation_pct: denominator > 0 ? (asset.total_bps / denominator) * 100 : 0
    }))
    .sort(
      (left, right) =>
        right.frequency_pct - left.frequency_pct ||
        right.average_allocation_pct - left.average_allocation_pct ||
        assetDisplay(left).localeCompare(assetDisplay(right))
    );

  return {
    portfolio_count: portfolioCount,
    average_holding_count: averageOrNull(portfolioRows.map((rows) => rows.length)),
    average_top_holding_pct: averageOrNull(portfolioRows.map((rows) => (rows[0]?.allocation_bps ?? 0) / 100)),
    most_common_top_holding: [...assetRows].sort(
      (left, right) => right.top_pick_count - left.top_pick_count || right.average_allocation_pct - left.average_allocation_pct
    )[0],
    assets: assetRows,
    categories: Array.from(categories.entries())
      .map(([group, bps]) => ({
        group,
        average_allocation_pct: denominator > 0 ? (bps / denominator) * 100 : 0
      }))
      .sort((left, right) => right.average_allocation_pct - left.average_allocation_pct)
  };
}

function modelHistoryRows(modelId) {
  const resultByRound = new Map(apiReadModel.results.filter((row) => row.model_id === modelId).map((row) => [row.round_id, row]));
  return apiReadModel.portfolios
    .filter((row) => row.model_id === modelId)
    .map((portfolio) => ({
      ...portfolio,
      allocations: [...(portfolio.allocations ?? [])].sort(
        (left, right) => left.allocation_rank - right.allocation_rank || right.allocation_bps - left.allocation_bps
      ),
      result: resultByRound.get(portfolio.round_id)
    }))
    .sort((left, right) => right.entry_date.localeCompare(left.entry_date) || right.round_id.localeCompare(left.round_id));
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

function homepageRiskProfiles() {
  return [...apiReadModel.model_styles]
    .filter((row) => typeof row.risk_appetite_score === "number")
    .sort(
      (left, right) =>
        left.risk_appetite_score - right.risk_appetite_score || modelLabel(left.model_id).localeCompare(modelLabel(right.model_id))
    );
}

function latestResultForTrack(track) {
  const round = latestRound(track, "resolved");
  const leaderboard = round
    ? apiReadModel.results
        .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
        .sort((left, right) => left.rank - right.rank)
    : [];
  return {
    round,
    leaderboard,
    winner: leaderboard[0]
  };
}

function resultTrackState(track) {
  const cumulative = buildCumulativeLeaderboardData(apiReadModel, track);
  const latestResult = latestResultForTrack(track);
  const pendingRound = latestRound(track, "active");
  const trackRounds = roundsForTrack(track);
  const completedCount =
    cumulative?.comparison?.completed_round_count ?? trackRounds.filter((round) => round.status === "resolved").length;
  return {
    track,
    label: trackLabel(track),
    latestResultRound: latestResult.round,
    pendingRound,
    cumulative,
    leaderboard: latestResult.leaderboard,
    winner: latestResult.winner,
    completedCount,
    totalCount: trackRounds.length,
    leader: cumulative?.data?.find((row) => row.is_rank_eligible) ?? latestResult.winner
  };
}

const indexHtml = readHtml("index.html");
const leaderboardsHtml = readHtml("leaderboards/index.html");
const latestMonthlyHtml = readHtml("leaderboards/latest-monthly/index.html");
const modelsIndexHtml = readHtml("models/index.html");
const roundsIndexHtml = readHtml("rounds/index.html");
const universeHtml = readHtml("universe/index.html");
const apiHtml = readHtml("api/index.html");
const methodologyHtml = readHtml("methodology/index.html");
const scoringHtml = readHtml("scoring/index.html");
const changelogHtml = readHtml("changelog/index.html");
const changelogSource = readRepoText("apps", "web", "src", "data", "changelog.ts");
const latestChangelogMatch = changelogSource.match(/id:\s*"([^"]+)"[\s\S]*?date:\s*"(\d{4}-\d{2}-\d{2})"[\s\S]*?title:\s*"([^"]+)"/);
const changelogEntryCount = [...changelogSource.matchAll(/^\s*id:\s*"/gm)].length;
if (latestChangelogMatch) {
  includes(changelogHtml, latestChangelogMatch[1], "changelog latest entry id");
  includes(changelogHtml, latestChangelogMatch[2], "changelog latest entry date");
  includes(changelogHtml, latestChangelogMatch[3], "changelog latest entry title");
  includes(changelogHtml, `"numberOfItems":${changelogEntryCount}`, "changelog structured data item count");
} else {
  failures.push("changelog source latest entry could not be parsed");
}

for (const track of ["weekly", "monthly"]) {
  const cumulative = buildCumulativeLeaderboardData(apiReadModel, track);
  if (cumulative.comparison.comparison_round_count === 0 || cumulative.data.length === 0) continue;
  const scorecard = expectedScorecardData(track);

  const eligibleRows = cumulative.data.filter((row) => row.is_rank_eligible);
  const leader = eligibleRows[0];
  if (!leader) failures.push(`${track} cumulative leaderboard has no rank-eligible leader`);

  const score = leader ? scoreLabel(leader.capitalbench_score) : "";
  const countLabel = resolvedLabel(cumulative.comparison.comparison_round_count);
  const pagePath = `leaderboards/cumulative-${track}/index.html`;
  const cumulativeHtml = readHtml(pagePath);
  const cumulativeScorecardHtml = htmlSection(
    cumulativeHtml,
    `<section class="track-scorecard-panel track-scorecard-${track}"`,
    `${track} cumulative scorecard`
  );
  const context = `${track} cumulative page`;

  includes(cumulativeHtml, `${cumulative.comparison.comparison_round_count} resolved`, context);
  includes(cumulativeScorecardHtml, score, context);
  includes(cumulativeScorecardHtml, "averages every resolved", context);
  includes(cumulativeScorecardHtml, `${cumulative.comparison.comparison_round_count} resolved tests averaged`, context);
  includes(cumulativeScorecardHtml, "full-history models ranked", context);
  includes(cumulativeScorecardHtml, `Newest resolved test: ${cumulative.comparison.comparison_round_ids.at(-1)}`, context);
  includes(cumulativeScorecardHtml, "Leader audit", `${context} score calculation audit`);
  includes(cumulativeScorecardHtml, cumulativeLeaderScoreAuditText(track, leader), `${context} score calculation audit`);
  includes(cumulativeScorecardHtml, "Rounds averaged:", context);
  for (const roundId of cumulative.comparison.comparison_round_ids) {
    includes(cumulativeScorecardHtml, roundId, context);
  }
  for (const row of cumulative.data) {
    includes(cumulativeScorecardHtml, row.label, `${context} ${row.model_id}`);
    if (typeof row.capitalbench_score === "number") {
      includes(cumulativeScorecardHtml, scoreLabel(row.capitalbench_score), `${context} ${row.model_id} CapitalBench Score`);
    }
    includes(cumulativeScorecardHtml, `${row.tests_included}/${row.tests_required}`, `${context} ${row.model_id} scored tests`);
  }
  includes(cumulativeScorecardHtml, "Average Return Details", `${context} average return chart`);
  for (const row of scorecard.averageRows) {
    if (typeof row.value === "number") {
      includesAny(cumulativeScorecardHtml, htmlTextVariants(row.label), `${context} average return ${row.key} label`);
      includes(cumulativeScorecardHtml, percentPointLabel(row.value), `${context} average return ${row.key} value`);
    }
  }
  const benchmarkScore = scorecard.normalizedRows.find((row) => row.key === "sp500");
  if (benchmarkScore && typeof benchmarkScore.value === "number") {
    includes(cumulativeScorecardHtml, scoreLabel(benchmarkScore.value), `${context} S&P 500 CapitalBench Score`);
  }
  if (scorecard.topReturnModel && typeof scorecard.topReturnModel.portfolio_return_pct === "number") {
    includes(cumulativeScorecardHtml, "Return leader", `${context} return leader label`);
    includes(cumulativeScorecardHtml, scorecard.topReturnModel.label, `${context} return leader model`);
    includes(cumulativeScorecardHtml, percentPointLabel(scorecard.topReturnModel.portfolio_return_pct), `${context} return leader value`);
  }

  const provisionalRows = cumulative.data.filter((row) => !row.is_rank_eligible);
  if (provisionalRows.length > 0) {
    includes(cumulativeScorecardHtml, "Not ranked yet", `${context} provisional section`);
  }
  for (const row of provisionalRows) {
    includes(cumulativeScorecardHtml, `${row.tests_included}/${row.tests_required}`, `${context} provisional marker`);
    includes(cumulativeScorecardHtml, "short history", `${context} provisional marker`);
    if (typeof row.portfolio_return_pct === "number") {
      includes(cumulativeScorecardHtml, percentPointLabel(row.portfolio_return_pct), `${context} provisional average return ${row.model_id}`);
    }
  }

  if (track === "weekly") {
    const homepageWeeklyScorecardHtml = htmlSection(
      indexHtml,
      '<section class="track-scorecard-panel track-scorecard-weekly"',
      "homepage weekly cumulative scorecard"
    );
    includes(indexHtml, "Full-history leader", "homepage weekly lane");
    includes(indexHtml, `${score} score · ${countLabel}`, "homepage weekly lane");
    includes(indexHtml, leader.label, "homepage weekly lane");
    includes(indexHtml, "Each bar is an average across all resolved tests in that track", "homepage scorecard average explanation");
    includes(homepageWeeklyScorecardHtml, "Full-History Model Scores", "homepage weekly cumulative chart title");
    includes(homepageWeeklyScorecardHtml, `${cumulative.comparison.comparison_round_count} resolved tests averaged`, "homepage weekly cumulative averaged count");
    includes(homepageWeeklyScorecardHtml, "full-history models ranked", "homepage weekly cumulative ranked model count");
    includes(homepageWeeklyScorecardHtml, `Newest resolved test: ${cumulative.comparison.comparison_round_ids.at(-1)}`, "homepage weekly cumulative newest included");
    includes(homepageWeeklyScorecardHtml, "Leader audit", "homepage weekly score calculation audit");
    includes(homepageWeeklyScorecardHtml, cumulativeLeaderScoreAuditText(track, leader), "homepage weekly score calculation audit");
    includes(homepageWeeklyScorecardHtml, "Rounds averaged:", "homepage weekly cumulative included rounds");
    for (const row of cumulative.data) {
      includes(homepageWeeklyScorecardHtml, row.label, `homepage weekly cumulative ${row.model_id}`);
      if (typeof row.capitalbench_score === "number") {
        includes(homepageWeeklyScorecardHtml, scoreLabel(row.capitalbench_score), `homepage weekly cumulative ${row.model_id} CapitalBench Score`);
      }
      includes(homepageWeeklyScorecardHtml, `${row.tests_included}/${row.tests_required}`, `homepage weekly cumulative ${row.model_id} scored tests`);
    }
    if (provisionalRows.length > 0) {
      includes(homepageWeeklyScorecardHtml, "Not ranked yet", "homepage weekly scorecard provisional section");
      includes(homepageWeeklyScorecardHtml, "not included in the main ranking", "homepage weekly scorecard provisional scope");
    }
    includes(homepageWeeklyScorecardHtml, "Average Return Details", "homepage weekly scorecard average return chart");
    for (const row of scorecard.averageRows) {
      if (typeof row.value === "number") {
        includesAny(homepageWeeklyScorecardHtml, htmlTextVariants(row.label), `homepage weekly average return ${row.key} label`);
        includes(homepageWeeklyScorecardHtml, percentPointLabel(row.value), `homepage weekly average return ${row.key} value`);
      }
    }
    if (benchmarkScore && typeof benchmarkScore.value === "number") {
      includes(homepageWeeklyScorecardHtml, scoreLabel(benchmarkScore.value), "homepage weekly S&P 500 CapitalBench Score");
    }
    if (scorecard.topReturnModel && typeof scorecard.topReturnModel.portfolio_return_pct === "number") {
      includes(homepageWeeklyScorecardHtml, "Return leader", "homepage weekly return leader label");
      includes(homepageWeeklyScorecardHtml, scorecard.topReturnModel.label, "homepage weekly return leader model");
      includes(homepageWeeklyScorecardHtml, percentPointLabel(scorecard.topReturnModel.portfolio_return_pct), "homepage weekly return leader value");
    }
    const allowedScoreAuditText = cumulativeLeaderScoreAuditText(track, leader);
    const homepageScorecardWithoutLeaderAudit = allowedScoreAuditText
      ? homepageWeeklyScorecardHtml.replace(allowedScoreAuditText, "")
      : homepageWeeklyScorecardHtml;
    const cumulativeScoreLabels = new Set(
      scorecard.normalizedRows.filter((row) => typeof row.value === "number").map((row) => scoreLabel(row.value))
    );
    for (const row of latestResultForTrack(track).leaderboard) {
      if (typeof row.capitalbench_score !== "number") continue;
      const latestOnlyScore = scoreLabel(row.capitalbench_score);
      if (!cumulativeScoreLabels.has(latestOnlyScore)) {
        excludes(homepageScorecardWithoutLeaderAudit, latestOnlyScore, `homepage weekly scorecard latest-only ${row.model_id} score`);
      }
    }
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
const homepageTrackRounds = ["weekly", "monthly"]
  .map((track) => latestRoundByTrack(track))
  .filter(Boolean);
includes(leaderboardsHtml, `<strong>${resolvedRoundCount}</strong>`, "leaderboards index completed count");
includes(leaderboardsHtml, `<strong>${activeRoundCount}</strong>`, "leaderboards index live count");
includes(leaderboardsHtml, `<strong>${apiReadModel.models.length}</strong>`, "leaderboards index model count");
includes(leaderboardsHtml, `<strong>${currentUniverseOptionCount} options</strong>`, "leaderboards index universe count");
if (latestResolvedRound) includes(leaderboardsHtml, latestResolvedRound.round_id, "leaderboards index latest scored round");
if (latestActiveWeekly) includes(leaderboardsHtml, latestActiveWeekly.round_id, "leaderboards index latest active weekly round");
if (latestActiveMonthly) includes(leaderboardsHtml, latestActiveMonthly.round_id, "leaderboards index latest active monthly round");

includes(indexHtml, `${apiReadModel.rounds.length} tests`, "homepage all-tests link count");
includes(indexHtml, `same ${currentUniverseOptionCount} assets`, "homepage process asset count");
includes(indexHtml, `${currentUniverseOptionCount} current assets`, "homepage safeguard current asset count");
includes(indexHtml, `${activeRoundCount} tests waiting for results`, "homepage safeguard open test count");
includes(indexHtml, `${apiReadModel.rounds.length}-test record`, "homepage timeline total test count");
includes(indexHtml, `<strong>${apiReadModel.models.length}</strong>`, "homepage current setup model count");
includes(indexHtml, `<strong>${currentUniverseOptionCount}</strong>`, "homepage current setup asset count");
includes(indexHtml, `<strong>${activeRoundCount}</strong>`, "homepage current setup open test count");
includes(indexHtml, `${activeRoundCount} open total`, "homepage current setup open total");
includes(indexHtml, "<strong>Weekly</strong>", "homepage current setup weekly label");
includes(indexHtml, "7 days", "homepage current setup weekly duration");
includes(indexHtml, "<strong>Monthly</strong>", "homepage current setup monthly label");
includes(indexHtml, "1 month", "homepage current setup monthly duration");
for (const round of homepageTrackRounds) {
  includes(indexHtml, round.round_id, `homepage current setup latest ${round.track} round`);
  includes(indexHtml, dateOnly(round.decision_deadline_utc), `homepage timeline ${round.round_id} decision date`);
  includes(indexHtml, trackWindowLabel(round), `homepage timeline ${round.round_id} window`);
  includes(indexHtml, homepageScoreLine(round), `homepage timeline ${round.round_id} score line`);
}

const resultStates = ["weekly", "monthly"].map(resultTrackState);
const latestPublishedResult = resultStates
  .filter((state) => state.latestResultRound && state.winner)
  .sort((left, right) => (right.latestResultRound?.exit_date ?? "").localeCompare(left.latestResultRound?.exit_date ?? ""))[0];
const liveRoundLabel = resultStates
  .map((state) => state.pendingRound?.round_id)
  .filter(Boolean)
  .join(" / ") || "None";

includes(leaderboardsHtml, "Benchmark status", "leaderboards index status panel");
includes(leaderboardsHtml, liveRoundLabel, "leaderboards index latest live label");
for (const state of resultStates) {
  const context = `leaderboards index ${state.track} track card`;
  includes(leaderboardsHtml, `${state.label} track`, context);
  includes(leaderboardsHtml, `${state.label} result`, `${context} latest route`);
  includes(leaderboardsHtml, `${state.label} aggregate`, `${context} aggregate route`);
  includes(leaderboardsHtml, state.latestResultRound?.round_id ?? "Pending", `${context} latest result label`);
  includes(leaderboardsHtml, state.pendingRound?.round_id ?? "None", `${context} pending round label`);
  includes(leaderboardsHtml, state.track === "weekly" ? "One market week" : "One market month", `${context} horizon`);

  if (state.cumulative.data.length > 0 && state.leader) {
    includes(leaderboardsHtml, `${modelLabel(state.leader.model_id)} Leads`, `${context} leader title`);
    includes(leaderboardsHtml, scoreLabel(state.leader.capitalbench_score), `${context} CapitalBench Score`);
    includes(leaderboardsHtml, providerLabelForModel(state.leader.model_id), `${context} provider`);
    includes(leaderboardsHtml, `${state.completedCount} tests`, `${context} route completed count`);
  } else {
    includes(leaderboardsHtml, `${state.label} Track`, `${context} pending title`);
    includes(leaderboardsHtml, "Waiting for the first completed score", `${context} pending copy`);
    includes(leaderboardsHtml, "Waiting for first score", `${context} pending status`);
    includes(leaderboardsHtml, "Not ready", `${context} aggregate route state`);
  }

  if (state.latestResultRound) {
    includes(leaderboardsHtml, `${state.latestResultRound.round_id}, ${trackWindowLabel(state.latestResultRound)}`, `${context} latest route description`);
  }
  if (state.pendingRound) {
    if (!state.latestResultRound) {
      includes(leaderboardsHtml, `${state.pendingRound.round_id} is live. ${scoreEtaLine(state.pendingRound)}`, `${context} pending route description`);
    }
    includes(leaderboardsHtml, scoreEtaLine(state.pendingRound), `${context} live score eta`);
    includes(leaderboardsHtml, trackWindowLabel(state.pendingRound), `${context} live window`);
    includes(leaderboardsHtml, state.pendingRound.official_run_id, `${context} live run id`);
  }
  if (state.cumulative.comparison.comparison_round_count > 0) {
    includes(
      leaderboardsHtml,
      `${state.cumulative.comparison.comparison_round_count} resolved ${state.label.toLowerCase()} test`,
      `${context} aggregate route description`
    );
  }
}

if (latestPublishedResult?.latestResultRound && latestPublishedResult.winner) {
  const context = "leaderboards index latest published result";
  const latestRound = latestPublishedResult.latestResultRound;
  const returnRows = apiReadModel.returns.filter(
    (row) => row.round_id === latestRound.round_id && row.run_id === latestRound.official_run_id
  );
  includes(leaderboardsHtml, "Most Recent Published Result", context);
  includes(leaderboardsHtml, `${latestPublishedResult.label} Portfolio Returns`, context);
  includes(leaderboardsHtml, latestRound.round_id, `${context} round id`);
  includes(leaderboardsHtml, trackWindowLabel(latestRound), `${context} window`);
  includes(leaderboardsHtml, modelLabel(latestPublishedResult.winner.model_id), `${context} winner`);
  includes(leaderboardsHtml, percentPointLabel(latestPublishedResult.winner.portfolio_return_pct), `${context} winner return`);
  includes(leaderboardsHtml, `<span><strong>Models</strong>${latestPublishedResult.leaderboard.length}</span>`, `${context} model count`);
  includes(leaderboardsHtml, `<span><strong>Eligible assets</strong>${returnRows.length}</span>`, `${context} eligible asset count`);
}

const monthlyState = resultTrackState("monthly");
if (monthlyState.pendingRound && !monthlyState.latestResultRound) {
  const context = "latest monthly page pending state";
  includes(latestMonthlyHtml, "No monthly result has been published yet", context);
  includes(latestMonthlyHtml, monthlyState.pendingRound.round_id, `${context} round id`);
  includes(latestMonthlyHtml, monthlyState.pendingRound.official_run_id, `${context} run id`);
  includes(latestMonthlyHtml, monthlyState.pendingRound.entry_date, `${context} entry date`);
  includes(latestMonthlyHtml, monthlyState.pendingRound.exit_date, `${context} exit date`);
  includes(latestMonthlyHtml, "No Monthly Score Yet", context);
  includes(latestMonthlyHtml, "Current monthly portfolios", context);
  const portfolios = roundPortfolios(monthlyState.pendingRound);
  for (const portfolio of portfolios) {
    const portfolioContext = `${context} portfolio ${portfolio.model_id}`;
    includes(latestMonthlyHtml, modelLabel(portfolio.model_id), portfolioContext);
    includes(latestMonthlyHtml, portfolio.selected_option_id, portfolioContext);
    for (const allocation of portfolio.allocations ?? []) {
      includes(latestMonthlyHtml, allocation.option_id, `${portfolioContext} allocation ${allocation.option_id}`);
      includes(latestMonthlyHtml, allocationPctLabel(allocation.allocation_pct), `${portfolioContext} allocation ${allocation.option_id} pct`);
    }
  }
}
const latestResolvedMonthlyRound = latestRound("monthly", "resolved");
const latestMonthlyDisplayRound = latestResolvedMonthlyRound ?? latestActiveMonthly;
if (latestResolvedMonthlyRound) {
  validateLeaderboardTableIsland(latestMonthlyHtml, latestResolvedMonthlyRound, "latest monthly page");
}
if (latestMonthlyDisplayRound) {
  validateOfficialPicksIsland(latestMonthlyHtml, latestMonthlyDisplayRound, "latest monthly page");
}

const roundDecisionDates = apiReadModel.rounds.map((round) => round.decision_date).filter(Boolean).sort();
const roundsIndexDataset = datasetJsonLd(roundsIndexHtml, "rounds index JSON-LD");
expectEqual(roundsIndexDataset.datePublished, roundDecisionDates[0], "rounds index JSON-LD datePublished");
expectEqual(roundsIndexDataset.dateModified, roundDecisionDates.at(-1), "rounds index JSON-LD dateModified");

for (const round of apiReadModel.rounds) {
  const context = `rounds index ${round.round_id}`;
  includes(roundsIndexHtml, round.round_id, context);
  includes(roundsIndexHtml, `/rounds/${round.round_id}/`, `${context} proof link`);
  includes(roundsIndexHtml, roundTrackLabel(round), `${context} track`);
  includes(roundsIndexHtml, round.status === "resolved" ? "scored" : round.status, `${context} status`);
  includes(roundsIndexHtml, dateOnly(round.decision_deadline_utc), `${context} decision deadline`);
  includes(roundsIndexHtml, round.horizon, `${context} horizon`);
  includes(roundsIndexHtml, dateOnly(round.exit_date), `${context} exit date`);
  includes(roundsIndexHtml, round.methodology_version, `${context} methodology`);
  includes(roundsIndexHtml, round.official_run_id, `${context} official run`);
}

const universeVersions = loadUniverseVersions();
const latestUniverse = universeVersions[0];
validateRoundsIndexIsland(roundsIndexHtml);
validateUniverseTableIsland(universeHtml);
if (latestUniverse) {
  includes(universeHtml, latestUniverse.label, "universe page latest label");
  includes(universeHtml, `${latestUniverse.rows.length} total choices for new public tests`, "universe page latest count");
  includes(universeHtml, `${latestUniverse.label} Option Table`, "universe page latest table title");
}
if (apiReadModel.current_universe_round_id) {
  includes(universeHtml, apiReadModel.current_universe_round_id, "universe page current round");
}
const universeRoundDates = apiReadModel.rounds
  .filter((round) => round.universe_version)
  .map((round) => round.decision_date)
  .filter(Boolean)
  .sort();
const currentUniverseRound = apiReadModel.rounds.find((round) => round.round_id === apiReadModel.current_universe_round_id);
const universeDataset = datasetJsonLd(universeHtml, "universe page JSON-LD");
expectEqual(universeDataset.datePublished, universeRoundDates[0], "universe page JSON-LD datePublished");
expectEqual(
  universeDataset.dateModified,
  currentUniverseRound?.decision_date ?? universeRoundDates.at(-1),
  "universe page JSON-LD dateModified"
);
for (const version of universeVersions) {
  const context = `universe page version ${version.label}`;
  includes(universeHtml, version.status, `${context} status`);
  includes(universeHtml, version.label, `${context} label`);
  includes(universeHtml, `${version.rows.length} options: ${version.detail}`, `${context} count and detail`);
  includes(universeHtml, version.file, `${context} file`);
}
for (const asset of latestUniverse?.rows ?? []) {
  const context = `universe page latest asset ${asset.option_id}`;
  includes(universeHtml, asset.option_id, `${context} option id`);
  includesAny(universeHtml, [asset.label, htmlText(asset.label)], `${context} name`);
  if (asset.ticker) includes(universeHtml, asset.ticker, `${context} ticker`);
  includes(universeHtml, asset.asset_class, `${context} asset class`);
  includes(universeHtml, asset.category, `${context} group`);
  includes(universeHtml, asset.risk_bucket, `${context} risk bucket`);
}

if (latestUniverse) {
  includes(methodologyHtml, `Universe ${latestUniverse.label}`, "methodology latest universe label");
  includes(methodologyHtml, `list has ${latestUniverse.rows.length} choices`, "methodology latest universe count");
}
for (const version of universeVersions.slice(1)) {
  includes(methodologyHtml, `${version.label} with ${version.rows.length} choices`, `methodology universe version ${version.label}`);
}

for (const [context, html] of [
  ["methodology", methodologyHtml],
  ["scoring", scoringHtml]
]) {
  includes(html, "100 * portfolio_return / max_possible_return", `${context} CapitalBench Score formula`);
  includes(html, "max_possible_return - portfolio_return", `${context} regret formula`);
  includes(html, "portfolio_return - sp500_return", `${context} S&P formula`);
  includes(html, "not average return divided by average max", `${context} cumulative score ratio explanation`);
  includesAny(html, ["all resolved tests", "every resolved test", "resolved test in that track"], `${context} cumulative scope`);
  includes(html, "short history", `${context} late-added model scope`);
}
includes(scoringHtml, "The score is not a return percentage", "scoring score scale explanation");
includes(scoringHtml, "3.93 divided by 4.62", "scoring score scale example");

includes(apiHtml, "cumulative rows average per-test score ratios", "API docs cumulative CapitalBench Score definition");
includes(apiHtml, "cumulative rows report the average of per-test max values", "API docs cumulative max possible definition");

const latestActiveWeeklyRound = latestRound("weekly", "active");
if (latestActiveWeeklyRound) includes(apiHtml, `/v1/rounds/${latestActiveWeeklyRound.round_id}/concentration`, "API docs concentration example");

const activePositioningApi = await dataApiBody("/api/v1/positioning/active?track=all&group_by=asset");
const activePositioningTop = activePositioningApi.data?.[0];
includes(apiHtml, htmlText("GET /v1/positioning/active?track=all&group_by=asset"), "API docs active positioning path");
includesJsonField(apiHtml, "portfolio_count", activePositioningApi.portfolio_count, "API docs active positioning portfolio count");
if (activePositioningTop) {
  includesJsonField(apiHtml, "key", activePositioningTop.key, "API docs active positioning top key");
  includesJsonField(apiHtml, "allocation_pct", activePositioningTop.allocation_pct, "API docs active positioning top allocation");
}

const assetHoldersApi = await dataApiBody("/api/v1/assets/SEMICONDUCTORS/model-holders?scope=active&track=weekly");
const assetHoldersTop = assetHoldersApi.data?.[0];
includes(apiHtml, htmlText("GET /v1/assets/SEMICONDUCTORS/model-holders?scope=active&track=weekly"), "API docs asset holders path");
includesJsonField(apiHtml, "portfolio_count", assetHoldersApi.portfolio_count, "API docs asset holders portfolio count");
if (assetHoldersTop) {
  includesJsonField(apiHtml, "key", assetHoldersTop.key, "API docs asset holders top model");
  includesJsonField(apiHtml, "allocation_pct", assetHoldersTop.allocation_pct, "API docs asset holders top allocation");
}

const livePerformanceApi = await dataApiBody("/api/v1/live/performance?track=all");
const livePerformanceTop = livePerformanceApi.data?.[0];
includes(apiHtml, htmlText("GET /v1/live/performance?track=all"), "API docs live performance path");
includesJsonField(apiHtml, "latest_price_date", livePerformanceApi.latest_price_date, "API docs live performance latest price date");
includesJsonField(apiHtml, "round_count", livePerformanceApi.round_count, "API docs live performance round count");
if (livePerformanceTop) {
  includesJsonField(apiHtml, "model_id", livePerformanceTop.model_id, "API docs live performance top model");
  includesJsonField(apiHtml, "portfolio_return_pct", livePerformanceTop.portfolio_return_pct, "API docs live performance top portfolio return");
  includesJsonField(apiHtml, "sp500_return_pct", livePerformanceTop.sp500_return_pct, "API docs live performance top S&P return");
  includesJsonField(apiHtml, "alpha_pp", livePerformanceTop.alpha_pp, "API docs live performance top alpha");
}

const latestWeeklyApi = await dataApiBody("/api/v1/leaderboards/latest?track=weekly");
const latestWeeklyApiTop = latestWeeklyApi.data?.[0];
includes(apiHtml, htmlText("GET /v1/leaderboards/latest?track=weekly"), "API docs latest weekly leaderboard path");
includesJsonField(apiHtml, "round_id", latestWeeklyApi.round_id, "API docs latest weekly round id");
if (latestWeeklyApiTop) {
  includesJsonField(apiHtml, "model_id", latestWeeklyApiTop.model_id, "API docs latest weekly top model");
  includesJsonField(apiHtml, "portfolio_return_pct", latestWeeklyApiTop.portfolio_return_pct, "API docs latest weekly top portfolio return");
  includesJsonField(apiHtml, "max_possible_return_pct", latestWeeklyApiTop.max_possible_return_pct, "API docs latest weekly max possible");
  includesJsonField(apiHtml, "capitalbench_score", latestWeeklyApiTop.capitalbench_score, "API docs latest weekly top score");
}

if (latestActiveWeeklyRound) {
  const concentrationPath = `/api/v1/rounds/${latestActiveWeeklyRound.round_id}/concentration`;
  const concentrationApi = await dataApiBody(concentrationPath);
  const concentrationTop = concentrationApi.assets?.[0];
  includes(apiHtml, concentrationPath.replace(/^\/api/, ""), "API docs round concentration path");
  includesJsonField(apiHtml, "round_id", concentrationApi.round_id, "API docs round concentration round id");
  includesJsonField(apiHtml, "model_count", concentrationApi.model_count, "API docs round concentration model count");
  if (concentrationTop) {
    includesJsonField(apiHtml, "option_id", concentrationTop.option_id, "API docs round concentration top option");
    includesJsonField(apiHtml, "allocation_pct", concentrationTop.allocation_pct, "API docs round concentration top allocation");
  }
}

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
      includesAny(indexHtml, [optionDisplay(topAsset), htmlText(optionDisplay(topAsset))], `${context} shared top pick`);
      includes(indexHtml, `Average across ${portfolios.length} model portfolios.`, `${context} model count`);
    } else {
      failures.push(`${context} has portfolios but no concentration top asset`);
    }
    includes(indexHtml, `Top 3 <strong>${allocationPctLabel(state.top_three_share_pct)}</strong>`, `${context} top-three concentration`);
    includes(indexHtml, `Spread <strong>${state.effective_asset_count.toFixed(1)} assets</strong>`, `${context} effective asset count`);

    for (const asset of assets.slice(0, 4)) {
      includesAny(indexHtml, [optionDisplay(asset), htmlText(optionDisplay(asset))], `${context} exposure ${asset.option_id}`);
      includes(indexHtml, allocationPctLabel(asset.average_pct), `${context} exposure ${asset.option_id} average allocation`);
    }
  } else {
    includes(indexHtml, `No model picks yet.`, context);
  }
}

const activeExposure = buildActiveExposureSummary();
validateLivePerformanceIsland(indexHtml);
validateActiveExposureIsland(indexHtml);
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

const riskProfiles = homepageRiskProfiles();
if (riskProfiles.length > 0) {
  const context = "homepage risk appetite";
  const riskScores = riskProfiles.map((row) => row.risk_appetite_score);
  const riskMinScore = Math.min(...riskScores);
  const riskMaxScore = Math.max(...riskScores);
  const rawRiskRange = riskMaxScore - riskMinScore;
  const riskFocusPadding = Math.max(0.06, Math.min(0.18, rawRiskRange * 0.18));
  let riskFocusMin = Math.max(1, riskMinScore - riskFocusPadding);
  let riskFocusMax = Math.min(5, riskMaxScore + riskFocusPadding);
  if (riskFocusMax - riskFocusMin < 0.36) {
    const center = (riskMinScore + riskMaxScore) / 2;
    riskFocusMin = Math.max(1, center - 0.18);
    riskFocusMax = Math.min(5, center + 0.18);
    if (riskFocusMax - riskFocusMin < 0.36) {
      if (riskFocusMin <= 1) riskFocusMax = Math.min(5, riskFocusMin + 0.36);
      if (riskFocusMax >= 5) riskFocusMin = Math.max(1, riskFocusMax - 0.36);
    }
  }
  const riskLabelSet = Array.from(new Set(riskProfiles.map((row) => row.risk_appetite_label)));
  const riskClusterLabel = riskLabelSet.length === 1 ? `All ${riskLabelSet[0]}` : riskLabelSet.join(" / ");
  const riskPortfolioCount = riskProfiles.reduce((total, row) => total + row.portfolio_count, 0);
  const lowestRisk = riskProfiles[0];
  const highestRisk = riskProfiles[riskProfiles.length - 1];

  includes(indexHtml, "Risk Appetite By Model", context);
  includes(indexHtml, `${riskPortfolioCount} saved portfolios`, `${context} saved portfolio count`);
  includes(indexHtml, riskClusterLabel, `${context} cluster label`);
  includes(indexHtml, `<b>${riskScoreShort(riskMinScore)}-${riskScoreShort(riskMaxScore)}</b>`, `${context} score range`);
  includes(indexHtml, modelLabel(highestRisk.model_id), `${context} highest risk model`);
  includes(indexHtml, modelLabel(lowestRisk.model_id), `${context} lowest risk model`);
  includes(indexHtml, `<strong>${riskScoreShort(riskFocusMin)}-${riskScoreShort(riskFocusMax)}</strong>`, `${context} focused range`);

  for (const row of riskProfiles) {
    const modelContext = `${context} ${row.model_id}`;
    includes(indexHtml, `/models/${row.model_id}/#model-fingerprint`, `${modelContext} fingerprint link`);
    includes(indexHtml, modelLabel(row.model_id), `${modelContext} model label`);
    includes(indexHtml, providerLabelForModel(row.model_id), `${modelContext} provider label`);
    includes(indexHtml, riskScoreValue(row.risk_appetite_score), `${modelContext} score`);
    includes(indexHtml, riskScoreShort(row.risk_appetite_score), `${modelContext} short score`);
    includes(indexHtml, row.risk_appetite_label, `${modelContext} risk label`);
    includes(indexHtml, pctValue(row.high_risk_pct), `${modelContext} high-risk exposure`);
    includes(indexHtml, pctValue(row.tech_pct), `${modelContext} technology exposure`);
    includes(indexHtml, pctValue(row.defensive_pct), `${modelContext} defensive exposure`);
  }
}

const latestResolvedWeeklyRound = latestRound("weekly", "resolved");
if (latestResolvedWeeklyRound) {
  const latestWeeklyHtml = readHtml("leaderboards/latest-weekly/index.html");
  validateLeaderboardTableIsland(latestWeeklyHtml, latestResolvedWeeklyRound, "latest weekly page");
  const latestWeeklyDisplayRound = latestResolvedWeeklyRound ?? latestActiveWeeklyRound;
  if (latestWeeklyDisplayRound) validateOfficialPicksIsland(latestWeeklyHtml, latestWeeklyDisplayRound, "latest weekly page");
  const latestWeeklyRows = apiReadModel.results
    .filter((row) => row.round_id === latestResolvedWeeklyRound.round_id && row.run_id === latestResolvedWeeklyRound.official_run_id)
    .sort((left, right) => left.rank - right.rank);
  const latestWeeklyWinner = latestWeeklyRows[0];
  const latestWeeklyMaxReturnRow = apiReadModel.returns
    .filter((row) => row.round_id === latestResolvedWeeklyRound.round_id && row.run_id === latestResolvedWeeklyRound.official_run_id)
    .sort((left, right) => Number(right.return_pct ?? -Infinity) - Number(left.return_pct ?? -Infinity))[0];
  includes(latestWeeklyHtml, latestResolvedWeeklyRound.entry_date, "latest weekly page entry date");
  includes(latestWeeklyHtml, latestResolvedWeeklyRound.exit_date, "latest weekly page exit date");
  includes(latestWeeklyHtml, latestResolvedWeeklyRound.round_id, "latest weekly page resolved round id");
  if (latestWeeklyWinner) {
    includes(latestWeeklyHtml, modelLabel(latestWeeklyWinner.model_id), "latest weekly page winner");
    includes(latestWeeklyHtml, percentPointLabel(latestWeeklyWinner.portfolio_return_pct), "latest weekly page winner return");
    includes(latestWeeklyHtml, percentPointLabel(latestWeeklyWinner.benchmark_return_pct), "latest weekly page benchmark return");
    includes(latestWeeklyHtml, "CapitalBench Score", "latest weekly page score audit label");
    includes(latestWeeklyHtml, "0-100 score, not return %", "latest weekly page score scale label");
    includes(latestWeeklyHtml, "Scores are out of 100, not portfolio returns.", "latest weekly page score scale explanation");
    includes(latestWeeklyHtml, scoreLabel(latestWeeklyWinner.capitalbench_score), "latest weekly page winner score audit");
    includes(
      latestWeeklyHtml,
      `${percentPointLabel(latestWeeklyWinner.portfolio_return_pct)} / ${percentPointLabel(latestWeeklyWinner.max_possible_return_pct)} max`,
      "latest weekly page score audit formula values"
    );
  }
  for (const row of latestWeeklyRows) {
    includes(latestWeeklyHtml, modelLabel(row.model_id), `latest weekly page result ${row.model_id}`);
    includes(latestWeeklyHtml, row.selected_option_id, `latest weekly page primary pick ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.portfolio_return_pct), `latest weekly page portfolio return ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.benchmark_return_pct), `latest weekly page benchmark return ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.alpha_pp), `latest weekly page alpha ${row.model_id}`);
    includes(latestWeeklyHtml, percentPointLabel(row.regret_vs_best_option_pct), `latest weekly page regret ${row.model_id}`);
    includes(latestWeeklyHtml, "CapitalBench Score audit", `latest weekly page score audit ${row.model_id}`);
    includes(
      latestWeeklyHtml,
      `${scoreLabel(row.capitalbench_score)} / 100 = ${percentPointLabel(row.portfolio_return_pct)} / ${percentPointLabel(row.max_possible_return_pct)} max asset: ${assetDisplay(latestWeeklyMaxReturnRow)}`,
      `latest weekly page score formula ${row.model_id}`
    );
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
  const roundDataset = datasetJsonLd(html, `${context} JSON-LD`);
  const roundPublishedDate = round.decision_date || round.entry_date;
  const roundPerformanceDates = (apiReadModel.interim_performance ?? [])
    .filter((row) => row.round_id === round.round_id && row.run_id === round.official_run_id)
    .map((row) => row.price_date || row.target_date);
  const roundModifiedDate = latestDate([
    roundPublishedDate,
    round.status === "resolved" ? round.exit_date : undefined,
    ...roundPerformanceDates
  ]);
  expectEqual(roundDataset.datePublished, roundPublishedDate, `${context} JSON-LD datePublished`);
  expectEqual(roundDataset.dateModified, roundModifiedDate, `${context} JSON-LD dateModified`);
  expectEqual(roundDataset.temporalCoverage, `${round.entry_date}/${round.exit_date}`, `${context} JSON-LD temporalCoverage`);
  validateOfficialPicksIsland(html, round, context);
  validateLeaderboardTableIsland(html, round, context);
  validateRoundPerformanceIsland(html, round, context);
  validateRoundTableIslands(html, round, context);

  const portfolios = apiReadModel.portfolios.filter(
    (portfolio) => portfolio.round_id === round.round_id && portfolio.run_id === round.official_run_id
  );
  if (portfolios.length !== round.model_count) {
    failures.push(`${context} model_count ${round.model_count} does not match generated portfolio count ${portfolios.length}`);
  }
  const optionCount = roundOptionCount(round.round_id);
  const entryPriceRows = roundEntryPriceRows(round.round_id);
  const proofFileCount = roundProofFileCount(round);
  const decisionNoun = round.submission_format === "portfolio" ? "allocations" : "picks";
  if (proofFileCount !== null) {
    includes(html, `${proofFileCount} public proof hashes`, `${context} proof hash count`);
    includes(html, `${proofFileCount} artifacts published`, `${context} audit artifact count`);
  }
  includes(html, `${portfolios.length} valid model ${decisionNoun}`, `${context} valid model portfolio count`);
  if (entryPriceRows.length > 0) includes(html, `${entryPriceRows.length} starting-price rows published`, `${context} entry price count`);
  if (optionCount !== null) {
    includes(html, `${optionCount} saved choices`, `${context} saved choice count`);
    includes(html, `${optionCount} model-facing choices`, `${context} model-facing choice count`);
  }

  const primaryPick = primaryPickCounts(portfolios);
  if (primaryPick) {
    const [optionId, count] = primaryPick;
    includes(html, optionId, `${context} most common primary pick`);
    includes(html, `${count} of ${portfolios.length} models selected`, `${context} most common pick count`);
    const consensusPrice = entryPriceRows.find((row) => row.option_id === optionId);
    if (consensusPrice?.price !== undefined) includes(html, `$${consensusPrice.price.toFixed(2)}`, `${context} consensus start price`);
  }

  const concentration = buildRoundConcentration(round);
  if (concentration.assets.length > 0) {
    includes(html, "Where Models Concentrated In This Test", `${context} consensus section`);
    includes(html, allocationPctLabel(concentration.top_asset_share_pct), `${context} consensus top exposure pct`);
    includes(html, allocationPctLabel(concentration.top_three_share_pct), `${context} consensus top-three pct`);
    includes(html, effectiveSpreadLabel(concentration.effective_asset_count), `${context} consensus effective spread`);
    includes(html, `Average allocation across ${concentration.model_count} model portfolios`, `${context} consensus model count`);
    for (const asset of concentration.assets.slice(0, 8)) {
      const assetContext = `${context} consensus asset ${asset.option_id}`;
      includesAny(html, [optionDisplay(asset), htmlText(optionDisplay(asset))], `${assetContext} label`);
      includes(html, allocationPctLabel(asset.average_pct), `${assetContext} average allocation`);
      includes(html, `${asset.holders.length} model${asset.holders.length === 1 ? "" : "s"}`, `${assetContext} holder count`);
      for (const holder of asset.holders.slice(0, 4)) {
        includes(html, modelLabel(holder.model_id), `${assetContext} holder ${holder.model_id}`);
        includes(html, allocationPctLabel(holder.allocation_pct), `${assetContext} holder ${holder.model_id} allocation`);
      }
    }
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
    const maxReturnRow = [...returns].sort((left, right) => Number(right.return_pct ?? -Infinity) - Number(left.return_pct ?? -Infinity))[0];
    const maxReturn = maxReturnRow?.return_pct ?? -Infinity;
    if (benchmark) includes(html, percentPointLabel(benchmark.return_pct), `${context} S&P 500 result`);
    if (Number.isFinite(maxReturn)) includes(html, percentPointLabel(maxReturn), `${context} max possible result`);
    includes(html, `${returns.length} entry and exit price rows support the final score`, `${context} scoring price row count`);
    includes(html, "What Moved During The Test", `${context} realized asset returns section`);
    for (const row of [...returns].sort((left, right) => left.rank - right.rank).slice(0, 12)) {
      const returnContext = `${context} realized return ${row.option_id}`;
      includes(html, row.option_id, returnContext);
      includes(html, row.label, `${returnContext} label`);
      if (row.ticker) includes(html, row.ticker, `${returnContext} ticker`);
      includes(html, percentPointLabel(row.return_pct), `${returnContext} return`);
      includes(html, String(row.entry_price), `${returnContext} entry price`);
      includes(html, String(row.exit_price), `${returnContext} exit price`);
    }
    for (const row of resultRows) {
      includes(html, modelLabel(row.model_id), `${context} result ${row.model_id}`);
      includes(html, percentPointLabel(row.portfolio_return_pct), `${context} result ${row.model_id}`);
      includes(html, percentPointLabel(row.benchmark_return_pct), `${context} result ${row.model_id} benchmark`);
      includes(html, percentPointLabel(row.alpha_pp), `${context} result ${row.model_id} alpha`);
      includes(html, percentPointLabel(row.regret_vs_best_option_pct), `${context} result ${row.model_id} regret`);
      includes(html, "CapitalBench Score audit", `${context} CapitalBench Score audit`);
      includes(html, "Scores are out of 100, not portfolio returns.", `${context} CapitalBench Score scale explanation`);
      includesCollapsed(
        html,
        `${scoreLabel(row.capitalbench_score)} / 100 = ${percentPointLabel(row.portfolio_return_pct)} / ${percentPointLabel(row.max_possible_return_pct)} max asset: ${assetDisplay(maxReturnRow)}`,
        `${context} result ${row.model_id} CapitalBench Score formula`
      );
    }
    for (const allocation of roundAllocations(round)) {
      const returnRow = returns.find((row) => row.option_id === allocation.option_id);
      if (!returnRow) continue;
      const contribution = (allocation.allocation_pct / 100) * returnRow.return_pct;
      const attributionContext = `${context} attribution ${allocation.model_id}/${allocation.option_id}`;
      includes(html, modelLabel(allocation.model_id), attributionContext);
      includes(html, allocation.option_id, attributionContext);
      includes(html, allocationPctLabel(allocation.allocation_pct), `${attributionContext} allocation`);
      includes(html, percentPointLabel(returnRow.return_pct), `${attributionContext} option return`);
      includes(html, percentPointLabel(contribution), `${attributionContext} contribution`);
    }
  } else if (resultRows.length > 0) {
    failures.push(`${context} is not resolved but has generated result rows`);
  } else {
    const performance = latestRoundPerformanceSnapshot(round);
    includes(html, "Live Portfolio And S&amp;P 500 Returns", `${context} live performance section`);
    if (performance.is_renderable) {
      includes(html, `${dateLabel(performance.latest_date)} snapshot`, `${context} live latest snapshot`);
      for (const row of performance.latest_rows) {
        const performanceContext = `${context} live performance ${row.model_id}`;
        includes(html, modelLabel(row.model_id), performanceContext);
        includes(html, providerLabelForModel(row.model_id), `${performanceContext} provider`);
        includes(html, signedPercentPointLabel(row.model_return_pct), `${performanceContext} portfolio return`);
        includes(html, signedPercentPointLabel(row.sp500_return_pct), `${performanceContext} S&P 500 return`);
        includes(html, signedPercentPointLabel(row.alpha_pp), `${performanceContext} alpha`);
        includes(html, row.selected_option_id, `${performanceContext} primary pick`);
      }
    } else {
      includes(html, "Live chart pending", `${context} live performance pending state`);
    }
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
  validateModelLiveHoldingsIsland(html, model.model_id, context);
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

  const fingerprint = modelFingerprint(model.model_id);
  includes(html, "Most frequently held assets", `${context} fingerprint asset section`);
  includes(html, "Average allocation by category", `${context} fingerprint category section`);
  includes(html, `<strong>${fingerprint.portfolio_count}</strong>`, `${context} fingerprint saved portfolio count`);
  if (fingerprint.average_holding_count !== null) {
    includes(html, `<strong>${numberLabel(fingerprint.average_holding_count)}</strong>`, `${context} fingerprint average holding count`);
  }
  if (fingerprint.average_top_holding_pct !== null) {
    includes(html, `<strong>${pctValue(fingerprint.average_top_holding_pct)}</strong>`, `${context} fingerprint average top holding`);
  }
  if (fingerprint.most_common_top_holding) {
    includesAny(
      html,
      [assetDisplay(fingerprint.most_common_top_holding), htmlText(assetDisplay(fingerprint.most_common_top_holding))],
      `${context} fingerprint most common top holding`
    );
  }
  for (const asset of fingerprint.assets.slice(0, 7)) {
    const assetContext = `${context} fingerprint asset ${asset.option_id}`;
    includesAny(html, [assetDisplay(asset), htmlText(assetDisplay(asset))], `${assetContext} label`);
    includes(html, groupLabel(asset.category), `${assetContext} group`);
    includes(html, `${pctValue(asset.frequency_pct)} held`, `${assetContext} frequency`);
    includes(html, `${pctValue(asset.average_allocation_pct)} avg`, `${assetContext} average allocation`);
  }
  for (const category of fingerprint.categories.slice(0, 7)) {
    const categoryContext = `${context} fingerprint category ${category.group}`;
    includes(html, category.group, `${categoryContext} label`);
    includes(html, pctValue(category.average_allocation_pct), `${categoryContext} average allocation`);
  }

  for (const portfolio of modelHistoryRows(model.model_id)) {
    const historyContext = `${context} history ${portfolio.round_id}`;
    includes(html, portfolio.round_id, historyContext);
    includes(html, portfolio.run_id, `${historyContext} run id`);
    includes(html, portfolio.track, `${historyContext} track`);
    includes(html, `${portfolio.entry_date} to ${portfolio.exit_date}`, `${historyContext} window`);
    for (const allocation of portfolio.allocations.slice(0, 4)) {
      includes(html, `${allocation.option_id} ${pctValue(allocation.allocation_pct)}`, `${historyContext} summary holding ${allocation.option_id}`);
    }
    for (const allocation of portfolio.allocations) {
      includesAny(
        html,
        [
          `${assetDisplay(allocation)} ${pctValue(allocation.allocation_pct)}`,
          htmlText(`${assetDisplay(allocation)} ${pctValue(allocation.allocation_pct)}`)
        ],
        `${historyContext} full holding ${allocation.option_id}`
      );
    }
    if (portfolio.result) {
      includes(html, signedPpLabel(portfolio.result.alpha_pp), `${historyContext} result alpha`);
    } else {
      includes(html, portfolio.status === "active" ? "Pending" : "Not scored", `${historyContext} pending result`);
    }
    if (portfolio.rationale_summary) {
      includesAny(html, htmlTextVariants(portfolio.rationale_summary), `${historyContext} rationale`);
    }
    if (portfolio.parsed_file_path) {
      includes(html, portfolio.parsed_file_path, `${historyContext} parsed proof path`);
    }
    includes(
      html,
      `rounds/${portfolio.round_id}/runs/${portfolio.run_id}/submissions/raw/${portfolio.model_id}.json`,
      `${historyContext} raw proof path`
    );
  }
}

if (failures.length > 0) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log(JSON.stringify({ ok: true, rendered_data_checks: true }));
