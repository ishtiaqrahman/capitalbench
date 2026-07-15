import assert from "node:assert/strict";
import test from "node:test";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildModelRiskBenchmark } from "../src/lib/modelRiskBenchmark.js";

const fixture = {
  data_as_of: "2026-07-14",
  methodology_href: "/risk-appetite/#method",
  profiles: [
    {
      model_id: "model-a",
      label: "Model A",
      provider: "openai",
      provider_label: "Provider A",
      sample: { portfolio_count: 10, monthly_portfolio_count: 6, weekly_portfolio_count: 4 },
      metrics: {
        average_risk_pulse: 60,
        monthly_risk_pulse: 55,
        weekly_risk_pulse: 80,
        average_top_allocation_pct: 32,
        defensive_pct: 8
      }
    },
    {
      model_id: "model-b",
      label: "Model B",
      provider: "google",
      provider_label: "Provider B",
      sample: { portfolio_count: 20, monthly_portfolio_count: 12, weekly_portfolio_count: 8 },
      metrics: {
        average_risk_pulse: 70,
        monthly_risk_pulse: 90,
        weekly_risk_pulse: 40,
        average_top_allocation_pct: 24,
        defensive_pct: 18
      }
    },
    {
      model_id: "missing-score",
      label: "Missing Score",
      sample: { portfolio_count: 2 },
      metrics: {}
    }
  ]
};

test("model risk benchmark ranks models separately for each horizon", () => {
  const benchmark = buildModelRiskBenchmark(fixture);
  const [overall, monthly, weekly] = benchmark.views;

  assert.deepEqual(overall.rows.map((row) => row.modelId), ["model-b", "model-a"]);
  assert.deepEqual(monthly.rows.map((row) => row.modelId), ["model-b", "model-a"]);
  assert.deepEqual(weekly.rows.map((row) => row.modelId), ["model-a", "model-b"]);
  assert.equal(benchmark.dataAsOf, "2026-07-14");
  assert.equal(benchmark.methodologyHref, "/risk-appetite/#method");
});

test("model risk benchmark preserves score meaning and view-specific sample counts", () => {
  const benchmark = buildModelRiskBenchmark(fixture);
  const overallModelA = benchmark.views[0].rows.find((row) => row.modelId === "model-a");
  const weeklyModelA = benchmark.views[2].rows.find((row) => row.modelId === "model-a");

  assert.equal(overallModelA.score, 60);
  assert.equal(overallModelA.riskLabel, "Risk-seeking");
  assert.equal(overallModelA.portfolioCount, 10);
  assert.equal(overallModelA.earlySample, false);
  assert.equal(overallModelA.averageTopAllocation, 32);
  assert.equal(overallModelA.defensiveAllocation, 8);

  assert.equal(weeklyModelA.score, 80);
  assert.equal(weeklyModelA.riskLabel, "Aggressive");
  assert.equal(weeklyModelA.portfolioCount, 4);
  assert.equal(weeklyModelA.earlySample, true);
});

test("generated model risk benchmark is sourced directly from published profile metrics", () => {
  const benchmark = buildModelRiskBenchmark(apiReadModel.model_behavior);
  const profiles = new Map(apiReadModel.model_behavior.profiles.map((profile) => [profile.model_id, profile]));

  assert.ok(benchmark.views.every((view) => view.rows.length > 0));
  for (const view of benchmark.views) {
    for (const row of view.rows) {
      const profile = profiles.get(row.modelId);
      const scoreField = view.scoreField;
      const countField = view.countField;
      assert.equal(row.score, profile.metrics[scoreField]);
      assert.equal(row.portfolioCount, profile.sample[countField]);
      assert.ok(row.score >= 0 && row.score <= 100);
    }
  }
});
