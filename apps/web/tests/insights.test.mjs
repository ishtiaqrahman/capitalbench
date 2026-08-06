import assert from "node:assert/strict";
import test from "node:test";
import {
  calculationValue,
  combinedRecentWinnerInsight,
  currentLiveRoundIds,
  featuredInsightRows,
  insightHref,
  insightsForModel,
  insightsForRound,
  insightsForSurface,
  isCurrentLiveInsight,
  publishedInsightRows,
  roundReferenceTokens,
  staleLiveInsights
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

test("home surface replaces the repeated risk card with the combined recent-winner insight", () => {
  const liveRoundIds = ["CB-2026-08-04-1W", "CB-2026-08-04-1M"];
  const base = {
    status: "published",
    data_as_of: "2026-08-04",
    confidence: "high",
    publication_tier: "category",
    importance_score: 90
  };
  const recentWinner = (model_id, label, score, lifecycle_status = "active") => ({
    model_id,
    label,
    lifecycle_status,
    recent_winner: {
      current_methodology: {
        observation_count: 20,
        combined: {
          combined_available: true,
          average_tilt_score: score
        }
      }
    }
  });
  const readModel = {
    generated_at: "2026-08-04T23:00:00Z",
    risk_appetite: {
      current_decision_pulse: {
        weekly: { round_id: liveRoundIds[0] },
        monthly: { round_id: liveRoundIds[1] }
      }
    },
    model_behavior: {
      generated_at: "2026-08-04T22:00:00Z",
      data_as_of: "2026-08-04",
      profiles: [
        recentWinner("model-high", "Model High", 78.66),
        recentWinner("model-low", "Model Low", 55.77),
        recentWinner("model-retired", "Retired Model", 99.9, "retired")
      ]
    },
    insights: {
      insights: [
        {
          ...base,
          id: "positioning",
          category: "current_positioning",
          context: { scope: "live_rounds", round_ids: liveRoundIds }
        },
        {
          ...base,
          id: "risk",
          category: "risk_regime",
          context: { scope: "live_rounds", round_ids: liveRoundIds }
        },
        {
          ...base,
          id: "market-ready",
          category: "market_environment",
          confidence: "medium",
          context: { scope: "resolved_history", maturity: "ready", insight_kind: "synthesis" }
        }
      ]
    }
  };

  const insight = combinedRecentWinnerInsight(readModel);
  assert.equal(insight.title, "Model High follows recent winners most");
  assert.equal(insight.summary, "Model Low has the lowest combined tilt at 55.8. Monthly and weekly behavior receive equal weight.");
  assert.equal(insight.context.model_count, 2);
  assert.equal(insight.context.best.model_id, "model-high");
  assert.equal(insight.context.worst.model_id, "model-low");
  assert.equal(calculationValue(insight.calculations[0]), "78.7/100");
  assert.equal(insightHref(insight), "/models/patterns/#recent-winner-title");
  assert.deepEqual(insightsForSurface(readModel, "home", 3).map((row) => row.id), [
    "positioning",
    "market-ready",
    "combined-recent-winner-tilt"
  ]);
  assert.ok(!insightsForSurface(readModel, "home", 3).some((row) => row.id === "risk"));
});

test("combined recent-winner homepage insight requires two valid active models", () => {
  const readModel = {
    model_behavior: {
      profiles: [
        {
          model_id: "model-a",
          label: "Model A",
          lifecycle_status: "active",
          recent_winner: {
            current_methodology: {
              combined: { combined_available: false, average_tilt_score: null }
            }
          }
        }
      ]
    }
  };

  assert.equal(combinedRecentWinnerInsight(readModel), null);
});

test("live insight helpers identify the canonical current weekly and monthly rounds", () => {
  const readModel = {
    risk_appetite: {
      current_decision_pulse: {
        weekly: { round_id: "CB-2026-07-27-1W" },
        monthly: { round_id: "CB-2026-07-27-1M" }
      }
    },
    insights: {
      insights: [
        {
          id: "current-risk",
          status: "published",
          context: {
            scope: "live_rounds",
            round_ids: ["CB-2026-07-27-1W", "CB-2026-07-27-1M"]
          }
        },
        {
          id: "stale-risk",
          status: "published",
          context: {
            scope: "live_rounds",
            round_ids: ["CB-2026-07-24-1W", "CB-2026-07-24-1M"]
          }
        }
      ]
    }
  };

  assert.deepEqual(currentLiveRoundIds(readModel), ["CB-2026-07-27-1M", "CB-2026-07-27-1W"]);
  assert.equal(isCurrentLiveInsight(readModel, readModel.insights.insights[0]), true);
  assert.equal(isCurrentLiveInsight(readModel, readModel.insights.insights[1]), false);
  assert.deepEqual(staleLiveInsights(readModel).map((insight) => insight.id), ["stale-risk"]);
});

test("home and ticker surfaces exclude stale live insights", () => {
  const base = {
    status: "published",
    data_as_of: "2026-07-27",
    confidence: "high",
    publication_tier: "category",
    importance_score: 90
  };
  const readModel = {
    risk_appetite: {
      current_decision_pulse: {
        weekly: { round_id: "CB-2026-07-27-1W" },
        monthly: { round_id: "CB-2026-07-27-1M" }
      }
    },
    insights: {
      insights: [
        {
          ...base,
          id: "stale-positioning",
          category: "current_positioning",
          context: {
            scope: "live_rounds",
            round_ids: ["CB-2026-07-24-1W", "CB-2026-07-24-1M"]
          }
        },
        {
          ...base,
          id: "current-risk",
          category: "risk_regime",
          context: {
            scope: "live_rounds",
            round_ids: ["CB-2026-07-27-1W", "CB-2026-07-27-1M"]
          }
        },
        {
          ...base,
          id: "resolved-oracle",
          category: "oracle_comparison",
          context: { scope: "round", round_id: "CB-2026-07-24-1W" }
        }
      ]
    }
  };

  assert.deepEqual(insightsForSurface(readModel, "home", 3).map((insight) => insight.id), [
    "current-risk",
    "resolved-oracle"
  ]);
  assert.ok(!insightsForSurface(readModel, "ticker", 3).some((insight) => insight.id === "stale-positioning"));
});
