import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import {
  buildCumulativeLeaderboardData,
  createMemoryApiAuthRepository,
  dataResultToResponse,
  handleDataApiRequest,
  hashApiKey,
  officialRowsForReadModel,
  officialRowsForRound
} from "../src/lib/dataApi.js";
import { capitalBenchScore, cumulativeCapitalBenchScore } from "../src/lib/capitalBenchScore.js";
import { insightContextRecencyValue, insightRecencyValue } from "../src/lib/insights.js";
import apiReadModel from "../src/generated/apiReadModel.js";

function getRequest(path, token, headers = {}) {
  return new Request(`https://www.capitalbench.org${path}`, {
    method: "GET",
    headers: token ? { ...headers, authorization: `Bearer ${token}` } : headers
  });
}

async function apiGet(path, { token, env = {}, repo, now, headers } = {}) {
  return await handleDataApiRequest({
    request: getRequest(path, token, headers),
    env: { API_AUTH_REQUIRED: "false", ...env },
    authRepo: repo ?? createMemoryApiAuthRepository(),
    now: now ?? new Date("2026-06-01T21:00:00Z")
  });
}

async function authRepoForToken(token, overrides = {}) {
  return createMemoryApiAuthRepository([
    {
      id: "test-key",
      key_hash: await hashApiKey(token),
      name: "Test Key",
      email: "api@example.com",
      ...overrides
    }
  ]);
}

function latestRoundId(track, { status } = {}) {
  const round = latestRound(track, { status });
  assert.ok(round, `expected a generated ${track} round with an official run`);
  return round.round_id;
}

function latestRound(track, { status } = {}) {
  return apiReadModel.rounds
    .filter((item) => item.track === track && (!status || item.status === status) && item.official_run_id)
    .sort(
      (left, right) =>
        `${right.exit_date ?? ""}:${right.decision_deadline_utc ?? ""}:${right.round_id}`.localeCompare(
          `${left.exit_date ?? ""}:${left.decision_deadline_utc ?? ""}:${left.round_id}`
        )
    )[0];
}

function modelLabel(modelId) {
  return apiReadModel.models.find((model) => model.model_id === modelId)?.label ?? modelId;
}

function canonicalLeaderboardRows(roundId) {
  return officialRowsForRound(apiReadModel, apiReadModel.results, roundId)
    .sort((left, right) => left.rank - right.rank)
    .map((row) => ({ ...row, label: modelLabel(row.model_id) }));
}

function canonicalRoundReturns(roundId) {
  return officialRowsForRound(apiReadModel, apiReadModel.returns, roundId)
    .sort((left, right) => Number(left.rank ?? 9999) - Number(right.rank ?? 9999));
}

function canonicalRoundAllocations(roundId) {
  return officialRowsForRound(apiReadModel, apiReadModel.allocations, roundId).sort(
    (left, right) =>
      String(left.model_id).localeCompare(String(right.model_id)) ||
      Number(left.allocation_rank ?? 9999) - Number(right.allocation_rank ?? 9999)
  );
}

function assertApproxEqual(actual, expected, tolerance = 1e-9) {
  assert.ok(Math.abs(actual - expected) <= tolerance, `expected ${actual} to be within ${tolerance} of ${expected}`);
}

test("API rejects missing bearer key when auth is required", async () => {
  const result = await apiGet("/api/v1/models", {
    env: { API_AUTH_REQUIRED: "true" },
    repo: createMemoryApiAuthRepository()
  });

  assert.equal(result.status, 401);
  assert.equal(result.body.error, "unauthorized");
});

test("API handles CORS preflight without a response body", async () => {
  const result = await handleDataApiRequest({
    request: new Request("https://www.capitalbench.org/api/v1/models", { method: "OPTIONS" }),
    env: { API_AUTH_REQUIRED: "true" },
    authRepo: createMemoryApiAuthRepository()
  });
  const response = dataResultToResponse(result);

  assert.equal(response.status, 204);
  assert.equal(await response.text(), "");
});

test("API accepts an active bearer key", async () => {
  const token = "cb_live_test_key";
  const repo = await authRepoForToken(token);

  const result = await apiGet("/api/v1/models", {
    token,
    env: { API_AUTH_REQUIRED: "true" },
    repo
  });

  assert.equal(result.status, 200);
  assert.ok(result.body.data.length >= 5);
  assert.ok(result.body.data.some((model) => model.model_id === "openai-gpt-5-5"));
});

test("API rejects bearer keys without read:v1 scope", async () => {
  const token = "cb_live_scope_test";
  const repo = await authRepoForToken(token, { scopes: "read:live" });

  const result = await apiGet("/api/v1/models", {
    token,
    env: { API_AUTH_REQUIRED: "true" },
    repo
  });

  assert.equal(result.status, 403);
  assert.equal(result.body.error, "forbidden");
  assert.equal(result.body.required_scope, "read:v1");
});

test("API returns cache validators for successful read responses", async () => {
  const first = await apiGet("/api/v1/models");
  const etag = first.headers.etag;
  const second = await apiGet("/api/v1/models", { headers: { "if-none-match": etag } });

  assert.equal(first.status, 200);
  assert.ok(etag);
  assert.match(first.headers["cache-control"], /private/);
  assert.equal(first.headers.vary, "authorization");
  assert.equal(second.status, 304);
  assert.equal(second.body, null);
});

test("API applies per-minute key rate limit", async () => {
  const token = "cb_live_rate_limit_test";
  const repo = await authRepoForToken(token, { rate_limit_per_minute: 1, rate_limit_per_day: 100 });

  const first = await apiGet("/api/v1/models", {
    token,
    env: { API_AUTH_REQUIRED: "true" },
    repo
  });
  const second = await apiGet("/api/v1/models", {
    token,
    env: { API_AUTH_REQUIRED: "true" },
    repo
  });

  assert.equal(first.status, 200);
  assert.equal(second.status, 429);
  assert.equal(second.body.error, "rate_limit_exceeded");
});

test("active positioning returns live model allocation data", async () => {
  const result = await apiGet("/api/v1/positioning/active?track=all&group_by=asset");
  const activePortfolioCount = new Set(
    officialRowsForReadModel(apiReadModel, apiReadModel.portfolios)
      .filter((row) => row.status === "active")
      .map((row) => `${row.round_id}:${row.run_id}:${row.model_id}`)
  ).size;
  const activeRoundIds = new Set(apiReadModel.rounds.filter((row) => row.status === "active").map((row) => row.round_id));
  const resolvedRoundIds = new Set(apiReadModel.rounds.filter((row) => row.status === "resolved").map((row) => row.round_id));

  assert.equal(result.status, 200);
  assert.equal(result.body.scope, "active");
  assert.equal(result.body.track, "all");
  assert.equal(result.body.portfolio_count, activePortfolioCount);
  assert.ok(result.body.portfolio_count > 0);
  assert.ok(result.body.data.length > 0);
  assert.ok(result.body.data[0].allocation_pct > 0);
  assertApproxEqual(
    result.body.data.reduce((total, row) => total + row.allocation_pct, 0),
    100
  );
  for (const row of result.body.data) {
    assert.ok(row.round_count <= activeRoundIds.size);
    for (const track of row.tracks) assert.ok(["monthly", "weekly"].includes(track));
    for (const roundId of row.rounds ?? []) {
      assert.ok(!resolvedRoundIds.has(roundId), `active positioning included resolved round ${roundId}`);
    }
  }
});

test("live performance returns interim mark-to-market data for open tests", async () => {
  const generatedLiveRows = officialRowsForReadModel(apiReadModel, apiReadModel.interim_performance).filter(
    (row) => row.status === "active" && row.days_elapsed > 0
  );
  assert.ok(generatedLiveRows.length > 0);

  const result = await apiGet("/api/v1/live/performance?track=all");

  assert.equal(result.status, 200);
  assert.equal(result.body.status, "live_not_final");
  assert.equal(result.body.track, "all");
  assert.ok(result.body.round_count > 0);
  assert.ok(result.body.model_count > 0);
  assert.equal(typeof result.body.benchmark.return_pct, "number");
  assert.ok(result.body.data.length > 0);
  assert.equal(typeof result.body.data[0].portfolio_return_pct, "number");
  assert.equal(typeof result.body.data[0].sp500_return_pct, "number");
  assert.equal(typeof result.body.data[0].alpha_pp, "number");

  const roundResult = await apiGet(`/api/v1/rounds/${generatedLiveRows[0].round_id}/live-performance`);
  assert.equal(roundResult.status, 200);
  assert.equal(roundResult.body.round_id, generatedLiveRows[0].round_id);
  assert.ok(roundResult.body.history.length > 0);

  const modelResult = await apiGet(`/api/v1/models/${result.body.data[0].model_id}/live-performance?track=all`);
  assert.equal(modelResult.status, 200);
  assert.equal(modelResult.body.model_id, result.body.data[0].model_id);
  assert.ok(modelResult.body.data.length <= 1);
});

test("risk appetite returns the current live decision pulse", async () => {
  const result = await apiGet("/api/v1/risk-appetite");
  const pulse = result.body.current_decision_pulse;
  const outstanding = result.body.outstanding_live_book;

  assert.equal(result.status, 200);
  assert.deepEqual(result.body, apiReadModel.risk_appetite);
  assert.equal(typeof pulse.score, "number");
  assertApproxEqual(pulse.score, (pulse.weekly.score + pulse.monthly.score) / 2);
  assertApproxEqual(pulse.change_from_previous, pulse.score - pulse.previous_score);
  assert.equal(pulse.weekly.track, "weekly");
  assert.equal(pulse.monthly.track, "monthly");
  assert.ok(pulse.weekly.model_count > 0);
  assert.ok(pulse.monthly.model_count > 0);
  assertApproxEqual(
    pulse.top_assets.reduce((total, row) => total + row.allocation_pct, 0),
    100
  );
  assertApproxEqual(
    pulse.regime_exposure.reduce((total, row) => total + row.allocation_pct, 0),
    100
  );
  assert.ok(result.body.history.decision_pulse.length > 1);
  assert.equal(
    result.body.history.decision_pulse.at(-1).combined_score,
    pulse.score
  );
  const latestOutstandingHistory = result.body.history.outstanding_live_book.at(-1);
  assert.equal(
    latestOutstandingHistory.date,
    result.body.history.decision_pulse.at(-1).date
  );
  assert.ok(latestOutstandingHistory.portfolio_count > 0);
  assert.equal(
    outstanding.portfolio_count,
    new Set(
      apiReadModel.portfolios
        .filter((portfolio) => portfolio.status === "active")
        .map((portfolio) => `${portfolio.round_id}:${portfolio.run_id}:${portfolio.model_id}`)
    ).size
  );
});

test("latest weekly leaderboard returns resolved scored rows", async () => {
  const latestWeeklyRoundId = latestRoundId("weekly", { status: "resolved" });
  const latestWeeklyRound = apiReadModel.rounds.find((item) => item.round_id === latestWeeklyRoundId);
  assert.ok(latestWeeklyRound, "expected latest weekly round metadata");
  const result = await apiGet("/api/v1/leaderboards/latest?track=weekly");
  const expectedRows = canonicalLeaderboardRows(latestWeeklyRoundId);

  assert.equal(result.status, 200);
  assert.equal(result.body.track, "weekly");
  assert.equal(result.body.round_id, latestWeeklyRoundId);
  assert.equal(result.body.data.length, latestWeeklyRound.model_count);
  assert.deepEqual(result.body.data, expectedRows);
  assert.equal(result.body.data[0].rank, 1);
  assert.equal(typeof result.body.data[0].alpha_pp, "number");
  assert.equal(typeof result.body.data[0].max_possible_return_pct, "number");
  assert.equal(typeof result.body.data[0].capitalbench_score, "number");
});

test("cumulative weekly leaderboard ranks eligible all-resolved rows by CapitalBench Score", async () => {
  const result = await apiGet("/api/v1/leaderboards/cumulative?track=weekly");
  const expected = buildCumulativeLeaderboardData(apiReadModel, "weekly");
  const resolvedWeeklyRoundIds = apiReadModel.rounds
    .filter((round) => round.track === "weekly" && round.status === "resolved")
    .map((round) => round.round_id);

  assert.equal(result.status, 200);
  assert.deepEqual(result.body, expected);
  assert.equal(result.body.track, "weekly");
  assert.equal(result.body.comparison.mode, "all_resolved_rounds");
  assert.ok(result.body.comparison.comparison_round_count > 0);
  assert.ok(result.body.comparison.comparison_round_count > 1, "weekly scorecard should cover multiple resolved tests");
  assert.equal(result.body.comparison.comparison_round_count, result.body.comparison.completed_round_count);
  assert.equal(result.body.comparison.comparison_round_count, resolvedWeeklyRoundIds.length);
  assert.ok(result.body.data.length > 0);
  assert.equal(result.body.data[0].rank, 1);
  assert.equal(result.body.data[0].is_rank_eligible, true);
  assert.equal(typeof result.body.data[0].capitalbench_score, "number");
  assert.equal(typeof result.body.data[0].max_possible_return_pct, "number");

  const latestWeeklyRoundId = result.body.comparison.comparison_round_ids.at(-1);
  let foundNonLatestOnlyAverage = false;
  for (const row of result.body.data.filter((item) => item.is_rank_eligible)) {
    const rawRows = officialRowsForReadModel(apiReadModel, apiReadModel.results).filter((item) => item.track === "weekly" && item.model_id === row.model_id);
    const expectedScore = cumulativeCapitalBenchScore(
      rawRows.map((item) => item.portfolio_return_pct),
      rawRows.map((item) => item.max_possible_return_pct)
    );
    assertApproxEqual(row.capitalbench_score, expectedScore);
    const latestOnlyScore = rawRows.find((item) => item.round_id === latestWeeklyRoundId)?.capitalbench_score;
    if (typeof latestOnlyScore === "number" && Math.abs(latestOnlyScore - expectedScore) > 1e-9) {
      foundNonLatestOnlyAverage = true;
    }
  }
  assert.equal(foundNonLatestOnlyAverage, true, "weekly cumulative score should be distinguishable from latest-only scores");

  for (let index = 1; index < result.body.data.length; index += 1) {
    const prior = result.body.data[index - 1];
    const current = result.body.data[index];
    if (prior.is_rank_eligible === current.is_rank_eligible) {
      assert.ok(prior.capitalbench_score >= current.capitalbench_score);
    }
  }
});

test("cumulative leaderboard includes all resolved tests and marks late model history", () => {
  const fixture = {
    models: [
      { model_id: "old-a", label: "Old A" },
      { model_id: "old-b", label: "Old B" },
      { model_id: "new-c", label: "New C" }
    ],
    rounds: [
      { round_id: "r1", track: "weekly", status: "resolved", exit_date: "2026-05-10", decision_deadline_utc: "2026-05-03T20:00:00Z" },
      { round_id: "r2", track: "weekly", status: "resolved", exit_date: "2026-05-17", decision_deadline_utc: "2026-05-10T20:00:00Z" },
      { round_id: "r3", track: "weekly", status: "resolved", exit_date: "2026-05-24", decision_deadline_utc: "2026-05-17T20:00:00Z" }
    ],
    results: [
      { round_id: "r1", track: "weekly", model_id: "old-a", capitalbench_score: 20, portfolio_return_pct: 2, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 1, rank: 1 },
      { round_id: "r1", track: "weekly", model_id: "old-b", capitalbench_score: 10, portfolio_return_pct: 1, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 0, rank: 2 },
      { round_id: "r2", track: "weekly", model_id: "old-a", capitalbench_score: 30, portfolio_return_pct: 3, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 2, rank: 1 },
      { round_id: "r2", track: "weekly", model_id: "old-b", capitalbench_score: 20, portfolio_return_pct: 2, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 1, rank: 2 },
      { round_id: "r3", track: "weekly", model_id: "old-a", capitalbench_score: 50, portfolio_return_pct: 5, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 4, rank: 3 },
      { round_id: "r3", track: "weekly", model_id: "old-b", capitalbench_score: 80, portfolio_return_pct: 8, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 7, rank: 1 },
      { round_id: "r3", track: "weekly", model_id: "new-c", capitalbench_score: 70, portfolio_return_pct: 7, benchmark_return_pct: 1, max_possible_return_pct: 10, alpha_pp: 6, rank: 2 }
    ]
  };

  const result = buildCumulativeLeaderboardData(fixture, "weekly");

  assert.deepEqual(result.comparison.completed_round_ids, ["r1", "r2", "r3"]);
  assert.deepEqual(result.comparison.comparison_round_ids, ["r1", "r2", "r3"]);
  assert.deepEqual(result.comparison.excluded_round_ids, []);
  assert.equal(result.data[0].model_id, "old-b");
  assert.equal(result.data[0].capitalbench_score, ((1 + 2 + 8) / (10 + 10 + 10)) * 100);
  assert.equal(result.data[0].tests_required, 3);
  assert.equal(result.data[0].tests_included, 3);
  assert.equal(result.data[0].is_rank_eligible, true);
  assert.equal(result.data[0].wins, 1);
  assertApproxEqual(result.data[0].win_rate_pct, 100 / 3);
  assertApproxEqual(result.data[0].positive_alpha_rate_pct, 200 / 3);
  assert.equal(result.data[1].model_id, "old-a");
  assert.equal(result.data[1].capitalbench_score, ((2 + 3 + 5) / (10 + 10 + 10)) * 100);
  assert.equal(result.data[1].wins, 2);
  assertApproxEqual(result.data[1].win_rate_pct, 200 / 3);
  assert.equal(result.data[1].positive_alpha_rate_pct, 100);
  assert.equal(result.data[2].model_id, "new-c");
  assert.equal(result.data[2].capitalbench_score, (7 / 10) * 100);
  assert.equal(result.data[2].tests_required, 3);
  assert.equal(result.data[2].tests_included, 1);
  assert.equal(result.data[2].is_rank_eligible, false);
  assert.equal(result.data[2].sample_status, "provisional");
});

test("official row helpers preserve official rows and exclude retry runs", () => {
  const fixture = {
    rounds: [{ round_id: "r1", official_run_id: "official-run" }],
    results: [
      { round_id: "r1", run_id: "official-run", model_id: "m1" },
      { round_id: "r1", run_id: "retry-run", model_id: "m1" },
      { round_id: "r1", model_id: "legacy-no-run-id" }
    ]
  };

  assert.deepEqual(officialRowsForRound(fixture, fixture.results, "r1"), [
    { round_id: "r1", run_id: "official-run", model_id: "m1" },
    { round_id: "r1", model_id: "legacy-no-run-id" }
  ]);
  assert.deepEqual(officialRowsForReadModel(fixture, fixture.results), [
    { round_id: "r1", run_id: "official-run", model_id: "m1" },
    { round_id: "r1", model_id: "legacy-no-run-id" }
  ]);
});

test("round portfolios and current universe endpoints return real data", async () => {
  const latestWeeklyRoundId = latestRoundId("weekly");
  const portfolios = await apiGet(`/api/v1/rounds/${latestWeeklyRoundId}/portfolios`);
  const universe = await apiGet("/api/v1/universe/current");
  const round = apiReadModel.rounds.find((item) => item.round_id === latestWeeklyRoundId);
  const currentUniverseRound = apiReadModel.rounds.find((round) => round.round_id === apiReadModel.current_universe_round_id);
  const expectedPortfolios = officialRowsForRound(apiReadModel, apiReadModel.portfolios, latestWeeklyRoundId);
  const expectedUniverse = apiReadModel.assets.filter((asset) => asset.in_current_universe);

  assert.equal(portfolios.status, 200);
  assert.equal(portfolios.body.round_id, latestWeeklyRoundId);
  assert.equal(portfolios.body.run_id, round.official_run_id);
  assert.deepEqual(portfolios.body.data, expectedPortfolios);
  assert.ok(portfolios.body.data.length >= 5);
  assert.ok(portfolios.body.data[0].allocations.length > 0);
  assert.equal(universe.status, 200);
  assert.equal(universe.body.round_id, apiReadModel.current_universe_round_id);
  assert.equal(universe.body.universe_version, currentUniverseRound?.universe_version ?? null);
  assert.deepEqual(universe.body.data, expectedUniverse);
  assert.ok(universe.body.data.length >= 60);
});

test("round results endpoint mirrors canonical scored rows and universe returns", async () => {
  const latestWeeklyRoundId = latestRoundId("weekly", { status: "resolved" });
  const round = apiReadModel.rounds.find((item) => item.round_id === latestWeeklyRoundId);
  assert.ok(round, "expected latest resolved weekly round metadata");
  const result = await apiGet(`/api/v1/rounds/${latestWeeklyRoundId}/results`);
  const expectedRows = canonicalLeaderboardRows(latestWeeklyRoundId);
  const expectedReturns = canonicalRoundReturns(latestWeeklyRoundId);
  const expectedBenchmarkReturn = expectedReturns.find((row) => row.is_benchmark)?.return_pct ?? null;

  assert.equal(result.status, 200);
  assert.equal(result.body.round_id, latestWeeklyRoundId);
  assert.equal(result.body.run_id, round.official_run_id);
  assert.equal(result.body.benchmark_option_id, round.benchmark_option_id);
  assert.equal(result.body.benchmark_return_pct, expectedBenchmarkReturn);
  assert.deepEqual(result.body.data, expectedRows);
  assert.deepEqual(result.body.asset_returns, expectedReturns);
  assert.ok(result.body.asset_returns.length > result.body.data.length);

  for (const row of result.body.data) {
    assertApproxEqual(row.alpha_pp, row.portfolio_return_pct - row.benchmark_return_pct);
    assertApproxEqual(row.regret_vs_best_option_pct, row.max_possible_return_pct - row.portfolio_return_pct);
    assertApproxEqual(row.capitalbench_score, capitalBenchScore(row.portfolio_return_pct, row.max_possible_return_pct));
    assert.ok(row.capitalbench_score <= 100);
  }
});

test("metadata and raw dataset endpoints expose generated read model data", async () => {
  const modelId = apiReadModel.models[0].model_id;
  const activeRoundId = latestRoundId("weekly", { status: "active" });
  const resolvedRoundId = latestRoundId("weekly", { status: "resolved" });

  const metadata = await apiGet("/api/v1/metadata");
  assert.equal(metadata.status, 200);
  assert.equal(metadata.body.generated_at, apiReadModel.generated_at);
  assert.equal(metadata.body.source, apiReadModel.source);
  assert.equal(metadata.body.data_counts.interim_performance, apiReadModel.interim_performance.length);
  assert.equal(metadata.body.data_counts.returns, apiReadModel.returns.length);
  assert.ok(metadata.body.datasets.includes("benchmark_evidence"));

  const assets = await apiGet("/api/v1/assets?current=all&limit=250");
  assert.equal(assets.status, 200);
  assert.equal(assets.body.row_count, apiReadModel.assets.length);
  assert.deepEqual(assets.body.data, apiReadModel.assets);

  const evidence = await apiGet("/api/v1/benchmark-evidence");
  assert.equal(evidence.status, 200);
  assert.deepEqual(evidence.body, apiReadModel.benchmark_evidence);

  const returns = await apiGet(`/api/v1/returns?track=weekly&round_id=${resolvedRoundId}&limit=250`);
  assert.equal(returns.status, 200);
  assert.equal(returns.body.row_count, canonicalRoundReturns(resolvedRoundId).length);
  assert.deepEqual(returns.body.data, canonicalRoundReturns(resolvedRoundId));

  const allocations = await apiGet(`/api/v1/allocations?track=weekly&scope=cumulative&round_id=${activeRoundId}&limit=250`);
  assert.equal(allocations.status, 200);
  assert.equal(allocations.body.row_count, canonicalRoundAllocations(activeRoundId).length);
  assert.deepEqual(
    allocations.body.data.sort(
      (left, right) =>
        String(left.model_id).localeCompare(String(right.model_id)) ||
        Number(left.allocation_rank ?? 9999) - Number(right.allocation_rank ?? 9999)
    ),
    canonicalRoundAllocations(activeRoundId)
  );

  const history = await apiGet("/api/v1/live/performance/history?track=all&limit=5");
  assert.equal(history.status, 200);
  assert.equal(history.body.row_count, officialRowsForReadModel(apiReadModel, apiReadModel.interim_performance).length);
  assert.equal(history.body.data.length, 5);
  assert.ok(history.body.data.every((row) => row.round_id && row.model_id && row.target_date));

  const modelPortfolios = await apiGet(`/api/v1/models/${modelId}/portfolios?track=all&scope=cumulative`);
  const expectedModelPortfolios = officialRowsForReadModel(apiReadModel, apiReadModel.portfolios).filter(
    (row) => row.model_id === modelId
  );
  assert.equal(modelPortfolios.status, 200);
  assert.equal(modelPortfolios.body.model_id, modelId);
  assert.equal(modelPortfolios.body.data.length, expectedModelPortfolios.length);
  assert.ok(modelPortfolios.body.data.some((row) => row.rationale_summary && row.allocations?.length > 0));

  const proof = await apiGet(`/api/v1/rounds/${activeRoundId}/proof`);
  const proofList = await apiGet("/api/v1/proof?track=all&status=all&limit=250");
  assert.equal(proof.status, 200);
  assert.equal(proof.body.round_id, activeRoundId);
  assert.ok(proof.body.proof.hashes);
  assert.equal(proofList.status, 200);
  assert.equal(proofList.body.row_count, officialRowsForReadModel(apiReadModel, apiReadModel.proof).length);
  assert.ok(proofList.body.data.some((row) => row.round_id === activeRoundId));
});

test("round concentration endpoint returns consensus and concentration data", async () => {
  const latestWeeklyRoundId = latestRoundId("weekly");
  const result = await apiGet(`/api/v1/rounds/${latestWeeklyRoundId}/concentration`);

  assert.equal(result.status, 200);
  assert.equal(result.body.round_id, latestWeeklyRoundId);
  assert.equal(result.body.track, "weekly");
  assert.ok(result.body.model_count >= 5);
  assert.equal(result.body.portfolio_count, result.body.model_count);
  assert.ok(result.body.summary.top_asset_share_pct > 0);
  assert.ok(result.body.summary.top_three_share_pct >= result.body.summary.top_asset_share_pct);
  assert.ok(result.body.summary.effective_asset_count > 0);
  assert.ok(result.body.assets.length > 0);
  assert.ok(result.body.assets[0].allocation_pct > 0);
  assert.ok(result.body.assets[0].models.length > 0);
  assert.ok(result.body.categories.length > 0);
});

test("model holdings and asset holder endpoints filter correctly", async () => {
  const holdings = await apiGet("/api/v1/models/openai-gpt-5-5/holdings?scope=active&track=weekly");
  const holders = await apiGet("/api/v1/assets/SEMICONDUCTORS/model-holders?scope=active&track=all");

  assert.equal(holdings.status, 200);
  assert.equal(holdings.body.model_id, "openai-gpt-5-5");
  assert.ok(holdings.body.data.every((row) => row.model_id === "openai-gpt-5-5"));
  assert.equal(holders.status, 200);
  assert.equal(holders.body.group_by, "model");
  assert.ok(holders.body.data.length > 0);
});

test("model behavior endpoint exposes canonical behavior profiles", async () => {
  const list = await apiGet("/api/v1/models/behavior");
  const patterns = await apiGet("/api/v1/models/patterns");
  const modelId = "openai-gpt-5-5";
  const detail = await apiGet(`/api/v1/models/${modelId}/behavior`);

  assert.equal(list.status, 200);
  assert.equal(list.body.version, "model_behavior_v1");
  assert.equal(list.body.profiles.length, apiReadModel.models.length);
  assert.ok(list.body.summary.highest_risk_model_id);
  assert.ok(list.body.pairwise_similarity.length > 0);
  assert.equal(list.body.pattern_report.version, "model_behavior_pattern_report_v1");
  assert.equal(list.body.pattern_report.rows.length, apiReadModel.models.length);

  assert.equal(patterns.status, 200);
  assert.equal(patterns.body.version, "model_behavior_pattern_report_v1");
  assert.deepEqual(patterns.body.rows.map((row) => row.model_id).sort(), apiReadModel.models.map((model) => model.model_id).sort());
  assert.ok(patterns.body.llm_provenance.prompt_version);

  assert.equal(detail.status, 200);
  assert.equal(detail.body.model_id, modelId);
  assert.ok(detail.body.archetype.label);
  assert.ok(detail.body.sample.portfolio_count > 0);
  assert.ok(detail.body.metrics.average_risk_pulse >= 0);
  assert.ok(detail.body.metrics.average_risk_pulse <= 100);
  assert.ok(detail.body.methodology_href.includes("model-behavior-methodology"));
});

test("insights endpoint returns ranked public insights with detail lookups", async () => {
  const list = await apiGet("/api/v1/insights?limit=3");

  assert.equal(list.status, 200);
  assert.equal(list.body.engine_version, apiReadModel.insights.engine_version);
  assert.ok(list.body.insight_count >= list.body.data.length);
  assert.equal(list.body.data.length, Math.min(3, list.body.insight_count));
  assert.ok(list.body.categories.length > 0);
  assert.ok(list.body.data.every((insight) => insight.status === "published"));
  assert.deepEqual(
    list.body.categories,
    Array.from(new Set(apiReadModel.insights.insights.filter((row) => row.status === "published").map((row) => row.category))).sort()
  );
  for (let index = 1; index < list.body.data.length; index += 1) {
    const previous = list.body.data[index - 1];
    const current = list.body.data[index];
    const previousRecency = insightRecencyValue(previous);
    const currentRecency = insightRecencyValue(current);
    assert.ok(previousRecency >= currentRecency);
    const previousContextRecency = insightContextRecencyValue(previous);
    const currentContextRecency = insightContextRecencyValue(current);
    if (previousRecency === currentRecency) {
      assert.ok(previousContextRecency >= currentContextRecency);
    }
    if (previousRecency === currentRecency && previousContextRecency === currentContextRecency) {
      assert.ok(previous.importance_score >= current.importance_score);
    }
  }

  const first = list.body.data[0];
  assert.ok(first.id);
  assert.ok(first.title);
  assert.ok(first.summary);
  assert.ok(first.context);
  assert.ok(first.context.primary_label);
  assert.ok(first.evidence.length > 0);

  const detail = await apiGet(`/api/v1/insights/${first.id}`);
  assert.equal(detail.status, 200);
  assert.deepEqual(detail.body, first);

  const category = first.category;
  const filtered = await apiGet(`/api/v1/insights?category=${category}&limit=20`);
  assert.equal(filtered.status, 200);
  assert.ok(filtered.body.data.length > 0);
  assert.ok(filtered.body.data.every((insight) => insight.category === category));

  const missing = await apiGet("/api/v1/insights/not-a-real-insight");
  assert.equal(missing.status, 404);
});

test("OpenAPI documented endpoints are served by the data API", async () => {
  const spec = JSON.parse(readFileSync(new URL("../public/api/openapi.json", import.meta.url), "utf8"));
  const modelId = apiReadModel.models[0].model_id;
  const optionId = apiReadModel.assets.find((row) => row.option_id === "SEMICONDUCTORS")?.option_id ?? apiReadModel.assets[0].option_id;
  const activeRoundId = latestRoundId("weekly", { status: "active" });
  const resolvedRoundId = latestRoundId("weekly", { status: "resolved" });
  const benchmarkSetId = apiReadModel.benchmark_set_definitions.find((set) => set.track === "weekly")?.set_id ?? "weekly-set-2026-05-28";
  const insightId = apiReadModel.insights.insights[0]?.id ?? "no-insight";
  const sampleByOpenApiPath = new Map([
    ["/v1/metadata", "/api/v1/metadata"],
    ["/v1/positioning/active", "/api/v1/positioning/active?track=all&group_by=asset"],
    ["/v1/positioning/cumulative", `/api/v1/positioning/cumulative?track=weekly&model_id=${modelId}&group_by=asset`],
    ["/v1/positioning/consensus", "/api/v1/positioning/consensus?track=all&scope=active"],
    ["/v1/positioning/by-model/{model_id}", `/api/v1/positioning/by-model/${modelId}?track=all&scope=active`],
    ["/v1/positioning/by-asset/{option_id}", `/api/v1/positioning/by-asset/${optionId}?track=all&scope=active`],
    ["/v1/positioning/by-category", "/api/v1/positioning/by-category?track=all&scope=active"],
    ["/v1/positioning/changes", "/api/v1/positioning/changes?track=weekly&window=latest"],
    ["/v1/risk-appetite", "/api/v1/risk-appetite"],
    ["/v1/live/performance", "/api/v1/live/performance?track=all"],
    ["/v1/live/performance/history", "/api/v1/live/performance/history?track=all&limit=5"],
    ["/v1/returns", `/api/v1/returns?track=weekly&round_id=${resolvedRoundId}&limit=5`],
    ["/v1/allocations", "/api/v1/allocations?track=all&scope=active&limit=5"],
    ["/v1/proof", "/api/v1/proof?track=all&status=all&limit=5"],
    ["/v1/rounds", "/api/v1/rounds?track=all&status=all&limit=5"],
    ["/v1/rounds/{round_id}", `/api/v1/rounds/${activeRoundId}`],
    ["/v1/rounds/{round_id}/proof", `/api/v1/rounds/${activeRoundId}/proof`],
    ["/v1/rounds/{round_id}/portfolios", `/api/v1/rounds/${activeRoundId}/portfolios`],
    ["/v1/rounds/{round_id}/concentration", `/api/v1/rounds/${activeRoundId}/concentration`],
    ["/v1/rounds/{round_id}/live-performance", `/api/v1/rounds/${activeRoundId}/live-performance`],
    ["/v1/rounds/{round_id}/results", `/api/v1/rounds/${resolvedRoundId}/results`],
    ["/v1/leaderboards/latest", "/api/v1/leaderboards/latest?track=weekly"],
    ["/v1/leaderboards/cumulative", "/api/v1/leaderboards/cumulative?track=weekly"],
    ["/v1/leaderboards/benchmark-sets", "/api/v1/leaderboards/benchmark-sets?track=weekly"],
    ["/v1/leaderboards/benchmark-sets/{set_id}", `/api/v1/leaderboards/benchmark-sets/${benchmarkSetId}`],
    ["/v1/benchmark-evidence", "/api/v1/benchmark-evidence"],
    ["/v1/insights", "/api/v1/insights?limit=5"],
    ["/v1/insights/{insight_id}", `/api/v1/insights/${insightId}`],
    ["/v1/models", "/api/v1/models"],
    ["/v1/models/{model_id}", `/api/v1/models/${modelId}`],
    ["/v1/models/{model_id}/holdings", `/api/v1/models/${modelId}/holdings?track=all&scope=active`],
    ["/v1/models/{model_id}/portfolios", `/api/v1/models/${modelId}/portfolios?track=all&scope=cumulative`],
    ["/v1/models/{model_id}/live-performance", `/api/v1/models/${modelId}/live-performance?track=all`],
    ["/v1/models/{model_id}/style", `/api/v1/models/${modelId}/style`],
    ["/v1/models/behavior", "/api/v1/models/behavior"],
    ["/v1/models/patterns", "/api/v1/models/patterns"],
    ["/v1/models/{model_id}/behavior", `/api/v1/models/${modelId}/behavior`],
    ["/v1/universe/current", "/api/v1/universe/current"],
    ["/v1/assets", "/api/v1/assets?current=all&limit=5"],
    ["/v1/assets/{option_id}", `/api/v1/assets/${optionId}`],
    ["/v1/assets/{option_id}/model-holders", `/api/v1/assets/${optionId}/model-holders?scope=active&track=all`]
  ]);

  assert.deepEqual(spec.servers.map((server) => server.url), ["https://www.capitalbench.org/api"]);
  assert.deepEqual(Object.keys(spec.paths).sort(), Array.from(sampleByOpenApiPath.keys()).sort());

  const root = await apiGet("/api/v1");
  assert.equal(root.status, 200);
  assert.deepEqual(root.body.endpoints.sort(), Object.keys(spec.paths).sort());

  for (const [openApiPath, samplePath] of sampleByOpenApiPath) {
    const result = await apiGet(samplePath);
    assert.equal(result.status, 200, `${openApiPath} sample ${samplePath} returned ${result.status}`);
    assert.ok(result.body && typeof result.body === "object", `${openApiPath} did not return a JSON object`);
  }
});

test("every top-level generated read model dataset has an API exposure path", async () => {
  const modelId = apiReadModel.models[0].model_id;
  const activeRoundId = latestRoundId("weekly", { status: "active" });
  const resolvedRoundId = latestRoundId("weekly", { status: "resolved" });
  const coverage = {
    generated_at: "/api/v1/metadata",
    api_version: "/api/v1/metadata",
    source: "/api/v1/metadata",
    current_universe_round_id: "/api/v1/metadata",
    benchmark_set_policy: "/api/v1/leaderboards/benchmark-sets",
    benchmark_set_definitions: "/api/v1/metadata",
    rounds: "/api/v1/rounds?track=all&status=all&limit=5",
    models: "/api/v1/models",
    assets: "/api/v1/assets?current=all&limit=5",
    portfolios: `/api/v1/models/${modelId}/portfolios?track=all&scope=cumulative`,
    allocations: "/api/v1/allocations?track=all&scope=active&limit=5",
    results: `/api/v1/rounds/${resolvedRoundId}/results`,
    returns: `/api/v1/returns?track=weekly&round_id=${resolvedRoundId}&limit=5`,
    interim_performance: `/api/v1/live/performance/history?track=weekly&round_id=${activeRoundId}&limit=5`,
    model_styles: `/api/v1/models/${modelId}/style`,
    model_behavior: "/api/v1/models/behavior",
    risk_appetite: "/api/v1/risk-appetite",
    insights: "/api/v1/insights?limit=5",
    proof: `/api/v1/rounds/${activeRoundId}/proof`,
    benchmark_evidence: "/api/v1/benchmark-evidence"
  };

  assert.deepEqual(Object.keys(coverage).sort(), Object.keys(apiReadModel).sort());
  for (const [dataset, path] of Object.entries(coverage)) {
    const result = await apiGet(path);
    assert.equal(result.status, 200, `${dataset} coverage path ${path} returned ${result.status}`);
  }
});

test("API rejects documented path parameters and unsupported score mixing correctly", async () => {
  const validModelId = apiReadModel.models[0].model_id;
  const validOptionId = apiReadModel.assets.find((row) => row.option_id === "SEMICONDUCTORS")?.option_id ?? apiReadModel.assets[0].option_id;

  const filtered = await apiGet(`/api/v1/positioning/cumulative?track=weekly&model_id=${validModelId}`);
  assert.equal(filtered.status, 200);
  assert.ok(filtered.body.data.every((row) => row.models.every((model) => model.model_id === validModelId)));

  const missingModel = await apiGet("/api/v1/positioning/by-model/not-a-model?scope=active");
  const missingModelQuery = await apiGet("/api/v1/positioning/cumulative?model_id=not-a-model");
  const missingAsset = await apiGet("/api/v1/positioning/by-asset/not-an-asset?scope=active");
  const missingAssetHolders = await apiGet("/api/v1/assets/not-an-asset/model-holders?scope=active");
  const latestAll = await apiGet("/api/v1/leaderboards/latest?track=all");
  const cumulativeAll = await apiGet("/api/v1/leaderboards/cumulative?track=all");
  const unsupportedWindow = await apiGet("/api/v1/positioning/changes?track=weekly&window=4_rounds");
  const validAssetHolders = await apiGet(`/api/v1/assets/${validOptionId}/model-holders?scope=active`);

  assert.equal(missingModel.status, 404);
  assert.equal(missingModelQuery.status, 404);
  assert.equal(missingAsset.status, 404);
  assert.equal(missingAssetHolders.status, 404);
  assert.equal(latestAll.status, 400);
  assert.equal(cumulativeAll.status, 400);
  assert.equal(unsupportedWindow.status, 400);
  assert.equal(validAssetHolders.status, 200);
});
