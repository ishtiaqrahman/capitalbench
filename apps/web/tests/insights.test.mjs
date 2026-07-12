import assert from "node:assert/strict";
import test from "node:test";
import {
  featuredInsightRows,
  insightsForModel,
  insightsForRound,
  insightsForSurface,
  publishedInsightRows,
  roundReferenceTokens
} from "../src/lib/insights.js";

test("roundReferenceTokens links CapitalBench round IDs", () => {
  const tokens = roundReferenceTokens("Compare CB-2026-06-15-1W with CB-2026-06-22-1M.");

  assert.deepEqual(tokens, [
    { type: "text", text: "Compare " },
    { type: "round", text: "CB-2026-06-15-1W", href: "/rounds/CB-2026-06-15-1W" },
    { type: "text", text: " with " },
    { type: "round", text: "CB-2026-06-22-1M", href: "/rounds/CB-2026-06-22-1M" },
    { type: "text", text: "." }
  ]);
});

test("publishedInsightRows sorts newer benchmark subjects before older high-importance insights", () => {
  const rows = publishedInsightRows([
    {
      id: "older",
      status: "published",
      importance_score: 100,
      context: { data_as_of: "2026-06-17", round_id: "CB-2026-05-17-1M" }
    },
    {
      id: "newer",
      status: "published",
      importance_score: 20,
      context: { data_as_of: "2026-06-22", round_id: "CB-2026-06-15-1W" }
    },
    {
      id: "draft-newer",
      status: "draft",
      importance_score: 200,
      context: { data_as_of: "2026-06-23" }
    }
  ]);

  assert.deepEqual(rows.map((row) => row.id), ["newer", "older"]);
});

test("publishedInsightRows uses importance before round context inside the same confidence tier", () => {
  const rows = publishedInsightRows([
    {
      id: "older-round-high-importance",
      status: "published",
      importance_score: 100,
      data_as_of: "2026-06-22",
      context: { round_id: "CB-2026-06-15-1W" }
    },
    {
      id: "newer-round-low-importance",
      status: "published",
      importance_score: 20,
      data_as_of: "2026-06-22",
      context: { round_id: "CB-2026-06-22-1W" }
    }
  ]);

  assert.deepEqual(rows.map((row) => row.id), ["older-round-high-importance", "newer-round-low-importance"]);
});

test("publishedInsightRows prioritizes publication tier and confidence on the same data date", () => {
  const rows = publishedInsightRows([
    {
      id: "detail-low",
      status: "published",
      data_as_of: "2026-07-09",
      publication_tier: "detail",
      confidence: "low",
      importance_score: 100
    },
    {
      id: "global-high",
      status: "published",
      data_as_of: "2026-07-09",
      publication_tier: "global",
      confidence: "high",
      importance_score: 50
    }
  ]);

  assert.deepEqual(rows.map((row) => row.id), ["global-high", "detail-low"]);
});

test("featuredInsightRows balances categories and excludes detail-only findings", () => {
  const base = {
    status: "published",
    data_as_of: "2026-07-09",
    confidence: "high",
    publication_tier: "category"
  };
  const rows = featuredInsightRows(
    [
      { ...base, id: "a-1", category: "a", importance_score: 90 },
      { ...base, id: "a-2", category: "a", importance_score: 80 },
      { ...base, id: "b-1", category: "b", importance_score: 70 },
      { ...base, id: "hidden", category: "c", publication_tier: "detail", importance_score: 100 }
    ],
    3,
    2
  );

  assert.deepEqual(rows.map((row) => row.id), ["a-1", "b-1", "a-2"]);
});

test("resolved-history insights do not leak onto individual round pages", () => {
  const roundId = "CB-2026-06-22-1W";
  const readModel = {
    insights: {
      insights: [
        {
          id: "market-history",
          status: "published",
          title: `History including ${roundId}`,
          context: { scope: "resolved_history", round_ids: [roundId] }
        },
        {
          id: "direct-round",
          status: "published",
          context: { scope: "round", round_id: roundId }
        }
      ]
    }
  };

  assert.deepEqual(insightsForRound(readModel, roundId).map((row) => row.id), ["direct-round"]);
});

test("model pages use structured market-environment model IDs", () => {
  const readModel = {
    insights: {
      insights: [
        {
          id: "market-model",
          status: "published",
          category: "market_environment",
          context: { scope: "resolved_history", model_ids: ["model-a"] }
        },
        {
          id: "unrelated-name-match",
          status: "published",
          category: "market_environment",
          title: "model-a appears only in display text",
          context: { scope: "resolved_history", model_ids: ["model-b"] }
        }
      ]
    }
  };

  assert.equal(insightsForModel(readModel, { modelId: "model-a", limit: 3 })[0].id, "market-model");
  assert.ok(!insightsForModel(readModel, { modelId: "model-a", limit: 3 }).some((row) => row.id === "unrelated-name-match"));
});

test("model pages can omit generic fallback insights", () => {
  const readModel = {
    insights: {
      insights: [
        {
          id: "direct-model",
          status: "published",
          category: "market_environment",
          context: { scope: "resolved_history", model_ids: ["model-a"] }
        },
        {
          id: "generic-fallback",
          status: "published",
          category: "model_behavior",
          context: { scope: "resolved_history" }
        }
      ]
    }
  };

  assert.deepEqual(
    insightsForModel(readModel, { modelId: "model-a", includeFallback: false }).map((row) => row.id),
    ["direct-model"]
  );
  assert.deepEqual(insightsForModel(readModel, { modelId: "model-b", includeFallback: false }), []);
});

test("home and results surfaces include a ready non-low market-environment synthesis", () => {
  const base = {
    status: "published",
    data_as_of: "2026-07-09",
    confidence: "high",
    importance_score: 80,
    context: { scope: "resolved_history" }
  };
  const readModel = {
    insights: {
      insights: [
        { ...base, id: "positioning", category: "current_positioning", context: { scope: "live_rounds" } },
        { ...base, id: "result", category: "consensus_performance" },
        {
          ...base,
          id: "market-ready",
          category: "market_environment",
          confidence: "medium",
          publication_tier: "category",
          importance_score: 88,
          context: { scope: "resolved_history", maturity: "ready", insight_kind: "synthesis" }
        },
        {
          ...base,
          id: "market-forming",
          category: "market_environment",
          confidence: "low",
          context: { scope: "resolved_history", maturity: "forming", insight_kind: "direction_leader" }
        }
      ]
    }
  };

  assert.ok(insightsForSurface(readModel, "home", 3).some((row) => row.id === "market-ready"));
  assert.ok(insightsForSurface(readModel, "results", 3).some((row) => row.id === "market-ready"));
  assert.ok(!insightsForSurface(readModel, "home", 3).some((row) => row.id === "market-forming"));
  assert.equal(insightsForSurface(readModel, "ticker", 1)[0].id, "market-ready");
});
