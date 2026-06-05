import assert from "node:assert/strict";
import test from "node:test";
import {
  buildCumulativeLeaderboardData,
  createMemoryApiAuthRepository,
  dataResultToResponse,
  handleDataApiRequest,
  hashApiKey
} from "../src/lib/dataApi.js";
import apiReadModel from "../src/generated/apiReadModel.js";

function getRequest(path, token) {
  return new Request(`https://www.capitalbench.org${path}`, {
    method: "GET",
    headers: token ? { authorization: `Bearer ${token}` } : {}
  });
}

async function apiGet(path, { token, env = {}, repo, now } = {}) {
  return await handleDataApiRequest({
    request: getRequest(path, token),
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
  const round = apiReadModel.rounds.find(
    (item) => item.track === track && (!status || item.status === status) && item.official_run_id
  );
  assert.ok(round, `expected a generated ${track} round with an official run`);
  return round.round_id;
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

  assert.equal(result.status, 200);
  assert.equal(result.body.scope, "active");
  assert.equal(result.body.track, "all");
  assert.ok(result.body.portfolio_count > 0);
  assert.ok(result.body.data.length > 0);
  assert.ok(result.body.data[0].allocation_pct > 0);
});

test("live performance returns interim mark-to-market data for open tests", async () => {
  const generatedLiveRows = apiReadModel.interim_performance.filter(
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

test("latest weekly leaderboard returns resolved scored rows", async () => {
  const latestWeeklyRoundId = latestRoundId("weekly", { status: "resolved" });
  const latestWeeklyRound = apiReadModel.rounds.find((item) => item.round_id === latestWeeklyRoundId);
  assert.ok(latestWeeklyRound, "expected latest weekly round metadata");
  const result = await apiGet("/api/v1/leaderboards/latest?track=weekly");

  assert.equal(result.status, 200);
  assert.equal(result.body.track, "weekly");
  assert.equal(result.body.round_id, latestWeeklyRoundId);
  assert.equal(result.body.data.length, latestWeeklyRound.model_count);
  assert.equal(result.body.data[0].rank, 1);
  assert.equal(typeof result.body.data[0].alpha_pp, "number");
  assert.equal(typeof result.body.data[0].max_possible_return_pct, "number");
  assert.equal(typeof result.body.data[0].capitalbench_score, "number");
});

test("cumulative weekly leaderboard ranks eligible same-roster rows by CapitalBench Score", async () => {
  const result = await apiGet("/api/v1/leaderboards/cumulative?track=weekly");

  assert.equal(result.status, 200);
  assert.equal(result.body.track, "weekly");
  assert.equal(result.body.comparison.mode, "latest_model_cohort");
  assert.ok(result.body.comparison.comparison_round_count > 0);
  assert.ok(result.body.data.length > 0);
  assert.equal(result.body.data[0].rank, 1);
  assert.equal(result.body.data[0].is_rank_eligible, true);
  assert.equal(typeof result.body.data[0].capitalbench_score, "number");
  assert.equal(typeof result.body.data[0].max_possible_return_pct, "number");
  for (let index = 1; index < result.body.data.length; index += 1) {
    const prior = result.body.data[index - 1];
    const current = result.body.data[index];
    if (prior.is_rank_eligible === current.is_rank_eligible) {
      assert.ok(prior.capitalbench_score >= current.capitalbench_score);
    }
  }
});

test("cumulative leaderboard starts a new comparable cohort when model roster changes", () => {
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
  assert.deepEqual(result.comparison.comparison_round_ids, ["r3"]);
  assert.deepEqual(result.comparison.excluded_round_ids, ["r1", "r2"]);
  assert.equal(result.data[0].model_id, "old-b");
  assert.equal(result.data[0].capitalbench_score, 80);
  assert.equal(result.data[1].model_id, "new-c");
  assert.ok(result.data.every((row) => row.tests_required === 1 && row.tests_included === 1 && row.is_rank_eligible));
});

test("round portfolios and current universe endpoints return real data", async () => {
  const latestWeeklyRoundId = latestRoundId("weekly");
  const portfolios = await apiGet(`/api/v1/rounds/${latestWeeklyRoundId}/portfolios`);
  const universe = await apiGet("/api/v1/universe/current");

  assert.equal(portfolios.status, 200);
  assert.equal(portfolios.body.round_id, latestWeeklyRoundId);
  assert.ok(portfolios.body.data.length >= 5);
  assert.ok(portfolios.body.data[0].allocations.length > 0);
  assert.equal(universe.status, 200);
  assert.equal(universe.body.round_id, apiReadModel.current_universe_round_id);
  assert.ok(universe.body.data.length >= 60);
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
