import assert from "node:assert/strict";
import test from "node:test";
import apiReadModel from "../src/generated/apiReadModel.js";
import {
  buildBenchmarkSetsData,
  comparisonOriginForRosterTransition
} from "../src/lib/benchmarkSets.js";

function result(roundId, modelId, portfolioReturnPct) {
  return {
    round_id: roundId,
    run_id: `run-${roundId}`,
    track: "weekly",
    model_id: modelId,
    portfolio_return_pct: portfolioReturnPct,
    benchmark_return_pct: 1,
    max_possible_return_pct: 10,
    alpha_pp: portfolioReturnPct - 1
  };
}

test("pure retirements retain the previous comparison origin", () => {
  const previousDefinition = {
    started_round_id: "r1",
    comparison_origin_round_id: "r1",
    model_ids: ["model-a", "model-b", "model-retired"]
  };

  assert.equal(
    comparisonOriginForRosterTransition({
      currentModelIds: ["model-a", "model-b"],
      previousDefinition,
      retiredModelIds: ["model-retired"]
    }),
    "r1"
  );
  assert.equal(
    comparisonOriginForRosterTransition({
      currentModelIds: ["model-a", "model-b", "model-new"],
      previousDefinition,
      retiredModelIds: ["model-retired"]
    }),
    null,
    "a replacement must start fresh"
  );
  assert.equal(
    comparisonOriginForRosterTransition({
      currentModelIds: ["model-a", "model-b"],
      previousDefinition,
      retiredModelIds: []
    }),
    null,
    "an unexplained smaller roster must not inherit history"
  );
});

test("a retirement successor ranks surviving models across inherited and new rounds", () => {
  const rounds = Array.from({ length: 6 }, (_, index) => ({
    round_id: `r${index + 1}`,
    track: "weekly",
    status: "resolved",
    exit_date: `2026-01-${String(index + 2).padStart(2, "0")}`,
    decision_deadline_utc: `2026-01-${String(index + 1).padStart(2, "0")}T20:00:00Z`,
    official_run_id: `run-r${index + 1}`
  }));
  const results = [];
  for (let index = 1; index <= 5; index += 1) {
    results.push(result(`r${index}`, "model-a", 2), result(`r${index}`, "model-b", 3), result(`r${index}`, "model-retired", 1));
  }
  results.push(result("r6", "model-a", 4), result("r6", "model-b", 5));

  const readModel = {
    benchmark_set_policy: {
      version: "benchmark_sets_v2",
      qualification_thresholds: { weekly: 6, monthly: 3 }
    },
    benchmark_set_definitions: [
      {
        set_id: "parent",
        track: "weekly",
        label: "Parent",
        started_round_id: "r1",
        comparison_origin_round_id: "r1",
        model_ids: ["model-a", "model-b", "model-retired"]
      },
      {
        set_id: "successor",
        track: "weekly",
        label: "Successor",
        started_round_id: "r6",
        comparison_origin_round_id: "r1",
        roster_policy: "frozen",
        model_ids: ["model-a", "model-b"]
      }
    ],
    models: [
      { model_id: "model-a", label: "Model A" },
      { model_id: "model-b", label: "Model B" },
      { model_id: "model-retired", label: "Retired Model", lifecycle_status: "retired" }
    ],
    rounds,
    results
  };

  const sets = buildBenchmarkSetsData(readModel).sets;
  const parent = sets.find((set) => set.set_id === "parent");
  const successor = sets.find((set) => set.set_id === "successor");

  assert.deepEqual(parent.comparison.comparison_round_ids, ["r1", "r2", "r3", "r4", "r5"]);
  assert.equal(parent.models.length, 3);
  assert.deepEqual(successor.comparison.comparison_round_ids, ["r1", "r2", "r3", "r4", "r5", "r6"]);
  assert.equal(successor.inherited_round_count, 5);
  assert.equal(successor.post_start_round_count, 1);
  assert.equal(successor.is_qualified, true);
  assert.equal(successor.is_current, true);
  assert.ok(successor.data.every((row) => row.tests_included === 6));

  const beforeSuccessorResolution = buildBenchmarkSetsData({
    ...readModel,
    benchmark_set_policy: {
      ...readModel.benchmark_set_policy,
      qualification_thresholds: { weekly: 5, monthly: 3 }
    },
    rounds: rounds.map((round) => (round.round_id === "r6" ? { ...round, status: "open" } : round))
  }).sets.find((set) => set.set_id === "successor");
  assert.equal(beforeSuccessorResolution.inherited_round_count, 5);
  assert.equal(beforeSuccessorResolution.post_start_round_count, 0);
  assert.equal(beforeSuccessorResolution.is_qualified, false);
  assert.equal(beforeSuccessorResolution.is_current, false);
});

test("production retirement successors inherit while additions start fresh", () => {
  const definitions = new Map(apiReadModel.benchmark_set_definitions.map((definition) => [definition.set_id, definition]));

  assert.equal(definitions.get("weekly-set-2026-07-21")?.comparison_origin_round_id, "CB-2026-07-10-1W");
  assert.equal(definitions.get("monthly-set-2026-07-21")?.comparison_origin_round_id, "CB-2026-07-10-1M");
  assert.equal(definitions.get("weekly-set-2026-08-19")?.comparison_origin_round_id, "CB-2026-08-13-1W");
  assert.equal(definitions.get("monthly-set-2026-08-19")?.comparison_origin_round_id, "CB-2026-08-13-1M");

  assert.equal(definitions.get("weekly-set-2026-07-24")?.comparison_origin_round_id, "CB-2026-07-24-1W");
  assert.equal(definitions.get("weekly-set-2026-08-13")?.comparison_origin_round_id, "CB-2026-08-13-1W");
});
