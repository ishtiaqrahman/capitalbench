import assert from "node:assert/strict";
import test from "node:test";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildBenchmarkSetsData } from "../src/lib/benchmarkSets.js";
import {
  buildBenchmarkSetRiskReturn,
  focusedRiskDomain
} from "../src/lib/benchmarkSetRiskReturn.js";

test("focused risk domain remains honest while preserving useful separation", () => {
  assert.deepEqual(focusedRiskDomain([58.8, 68.8, 67.5]), { minimum: 40, maximum: 80 });
  assert.deepEqual(focusedRiskDomain([72.8, 86.7, 67.5]), { minimum: 50, maximum: 100 });
  assert.deepEqual(focusedRiskDomain([0, 100]), { minimum: 0, maximum: 100 });
  assert.deepEqual(focusedRiskDomain([]), { minimum: 0, maximum: 100 });
});

test("risk-return data uses exactly the shared comparison-set rounds", () => {
  const sets = buildBenchmarkSetsData(apiReadModel).sets;
  const set = sets.find((candidate) => candidate.comparison.comparison_round_count > 0);
  const chart = buildBenchmarkSetRiskReturn(apiReadModel, set);

  assert.ok(chart);
  assert.equal(chart.roundCount, set.comparison.comparison_round_count);
  assert.equal(chart.models.length, set.data.filter((row) => row.is_rank_eligible).length);
  assert.ok(chart.models.every((row) => row.roundCount === chart.roundCount));
  assert.deepEqual(
    chart.models.map((row) => row.returnPct),
    [...chart.models.map((row) => row.returnPct)].sort((left, right) => right - left)
  );
});

test("S&P reference uses the canonical allocation-risk score and same-round return", () => {
  const set = buildBenchmarkSetsData(apiReadModel).sets.find(
    (candidate) => candidate.comparison.comparison_round_count > 0
  );
  const chart = buildBenchmarkSetRiskReturn(apiReadModel, set);

  assert.equal(chart.benchmark.riskScore, 67.5);
  assert.equal(chart.benchmark.returnPct, set.benchmark.return_pct);
  for (const row of chart.models) {
    assert.equal(row.alphaVsBenchmarkPct, row.returnPct - chart.benchmark.returnPct);
    assert.equal(
      row.beatsBenchmarkWithNoMoreRisk,
      row.returnPct > chart.benchmark.returnPct && row.riskScore <= chart.benchmark.riskScore
    );
  }
});

test("missing portfolio risk never produces a mismatched risk-return sample", () => {
  const set = buildBenchmarkSetsData(apiReadModel).sets.find(
    (candidate) => candidate.comparison.comparison_round_count > 0
  );
  const removedModelId = set.data.find((row) => row.is_rank_eligible).model_id;
  const removedRoundId = set.comparison.comparison_round_ids[0];
  const readModel = {
    ...apiReadModel,
    portfolios: apiReadModel.portfolios.filter(
      (portfolio) => !(portfolio.round_id === removedRoundId && portfolio.model_id === removedModelId)
    )
  };
  const chart = buildBenchmarkSetRiskReturn(readModel, set);

  assert.ok(chart);
  assert.ok(!chart.models.some((row) => row.modelId === removedModelId));
  assert.ok(chart.models.every((row) => row.roundCount === chart.roundCount));
});

test("sets without shared resolved rounds do not render a risk-return chart", () => {
  const set = buildBenchmarkSetsData(apiReadModel).sets.find(
    (candidate) => candidate.comparison.comparison_round_count === 0
  );
  if (!set) return;
  assert.equal(buildBenchmarkSetRiskReturn(apiReadModel, set), null);
});
