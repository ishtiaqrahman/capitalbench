import assert from "node:assert/strict";
import test from "node:test";
import {
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

function latestRoundId(track) {
  const round = apiReadModel.rounds.find((item) => item.track === track && item.official_run_id);
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

test("latest weekly leaderboard returns resolved scored rows", async () => {
  const result = await apiGet("/api/v1/leaderboards/latest?track=weekly");

  assert.equal(result.status, 200);
  assert.equal(result.body.track, "weekly");
  assert.equal(result.body.round_id, "CB-2026-05-24-1W");
  assert.equal(result.body.data.length, 4);
  assert.equal(result.body.data[0].rank, 1);
  assert.equal(typeof result.body.data[0].alpha_pp, "number");
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
