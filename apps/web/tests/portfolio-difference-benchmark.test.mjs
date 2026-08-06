import test from "node:test";
import assert from "node:assert/strict";
import { buildPortfolioDifferenceBenchmark } from "../src/lib/portfolioDifferenceBenchmark.js";

function profile(modelId, score, options = {}) {
  const observationCount = options.observationCount ?? 10;
  const monthlyScore = options.monthlyScore ?? score;
  const weeklyScore = options.weeklyScore ?? score;
  const monthlyCount = options.monthlyCount ?? Math.ceil(observationCount / 2);
  const weeklyCount = options.weeklyCount ?? Math.floor(observationCount / 2);
  return {
    model_id: modelId,
    label: options.label ?? modelId,
    provider: options.provider ?? "test",
    provider_label: options.providerLabel ?? "Test",
    lifecycle_status: options.lifecycleStatus ?? "active",
    portfolio_difference: {
      current_methodology: {
        observation_count: observationCount,
        combined: {
          combined_available: options.combinedAvailable ?? true,
          average_difference_score: score,
          observation_count: observationCount,
          decision_date_count: observationCount
        },
        tracks: {
          monthly: {
            average_difference_score: monthlyScore,
            observation_count: monthlyCount,
            decision_date_count: monthlyCount
          },
          weekly: {
            average_difference_score: weeklyScore,
            observation_count: weeklyCount,
            decision_date_count: weeklyCount
          }
        },
        evidence: {
          label: options.evidenceLabel ?? "Established sample"
        }
      }
    }
  };
}

test("homepage Portfolio Difference benchmark defaults to active Overall scores", () => {
  const benchmark = buildPortfolioDifferenceBenchmark({
    data_as_of: "2026-08-06",
    profiles: [
      profile("model-middle", 42),
      profile("model-high", 80),
      profile("model-low", 12),
      profile("model-retired", 99, { lifecycleStatus: "retired" }),
      profile("model-no-combined", null, { combinedAvailable: false })
    ]
  });

  assert.equal(benchmark.dataAsOf, "2026-08-06");
  assert.deepEqual(benchmark.views.map((view) => view.key), ["overall", "monthly", "weekly"]);
  assert.deepEqual(benchmark.views[0].rows.map((row) => row.modelId), ["model-high", "model-middle", "model-low"]);
  assert.equal(benchmark.views[0].rows[0].distinction, "Most different");
  assert.equal(benchmark.views[0].rows[1].distinction, null);
  assert.equal(benchmark.views[0].rows[2].distinction, "Most like the group");
  assert.equal(benchmark.views[0].rows[1].observationCount, 10);
});

test("homepage Portfolio Difference views sort and count each horizon independently", () => {
  const benchmark = buildPortfolioDifferenceBenchmark({
    profiles: [
      profile("model-a", 55, { monthlyScore: 20, weeklyScore: 80, monthlyCount: 8, weeklyCount: 6 }),
      profile("model-b", 45, { monthlyScore: 70, weeklyScore: 30, monthlyCount: 5, weeklyCount: 9 })
    ]
  });

  assert.deepEqual(benchmark.views[1].rows.map((row) => row.modelId), ["model-b", "model-a"]);
  assert.deepEqual(benchmark.views[2].rows.map((row) => row.modelId), ["model-a", "model-b"]);
  assert.equal(benchmark.views[1].rows[0].observationCount, 5);
  assert.equal(benchmark.views[2].rows[0].observationCount, 6);
});

test("homepage Portfolio Difference benchmark clamps marker positions in every view", () => {
  const benchmark = buildPortfolioDifferenceBenchmark({
    profiles: [
      profile("model-high", 120, { monthlyScore: 130, weeklyScore: 110 }),
      profile("model-low", -5, { monthlyScore: -10, weeklyScore: -20 })
    ]
  });

  for (const view of benchmark.views) {
    assert.equal(view.rows[0].position, 100);
    assert.equal(view.rows[1].position, 0);
  }
});
