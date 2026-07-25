import assert from "node:assert/strict";
import test from "node:test";
import apiReadModel from "../src/generated/apiReadModel.js";
import { buildBenchmarkSetsData } from "../src/lib/benchmarkSets.js";
import {
  buildBenchmarkSetComparison,
  defaultBenchmarkSetComparison
} from "../src/lib/benchmarkSetComparison.js";

const benchmarkSets = buildBenchmarkSetsData(apiReadModel).sets;

test("default benchmark-set comparisons use the current and newest scored forming sets", () => {
  const weekly = defaultBenchmarkSetComparison(benchmarkSets, "weekly");
  const monthly = defaultBenchmarkSetComparison(benchmarkSets, "monthly");

  assert.equal(weekly.baseline.is_current, true);
  assert.ok(weekly.comparison.comparison.comparison_round_count > 0);
  assert.equal(monthly.baseline.is_current, true);
  assert.ok(monthly.comparison.comparison.comparison_round_count > 0);
});

test("benchmark-set comparison separates roster and round-window changes", () => {
  const baseline = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-05-28");
  const comparison = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-06-09");
  const result = buildBenchmarkSetComparison(apiReadModel, baseline, comparison);

  assert.equal(result.track, "weekly");
  assert.equal(result.models.common_count, 5);
  assert.deepEqual(result.models.added, ["anthropic-claude-fable-5"]);
  assert.deepEqual(result.models.removed, []);
  assert.deepEqual(result.rounds.shared, comparison.comparison.comparison_round_ids);
  assert.equal(result.rounds.baseline_only.length, baseline.comparison.comparison_round_count - result.rounds.shared.length);
  assert.equal(result.rounds.comparison_only.length, 0);
  const baselineTopThree = new Set(baseline.data.filter((row) => row.rank <= 3).map((row) => row.model_id));
  const expectedTopThreeOverlap = comparison.data
    .filter((row) => row.rank <= 3)
    .filter((row) => baselineTopThree.has(row.model_id)).length;
  assert.equal(result.ranking.top_three_overlap, expectedTopThreeOverlap);
  const expectedSimilarityLabel =
    result.ranking.similarity >= 0.8
      ? "Hardly changed"
      : result.ranking.similarity >= 0.5
        ? "Changed a little"
        : result.ranking.similarity >= 0.2
          ? "Changed"
          : "Changed a lot";
  assert.equal(result.ranking.similarity_label, expectedSimilarityLabel);
  assert.match(result.summary, /only in Jun 9 Weekly/);
  if (baseline.is_current || comparison.is_current) {
    assert.match(result.trust_guidance, /main published ranking/);
  } else {
    assert.match(result.trust_guidance, /enough completed rounds/);
  }
  assert.doesNotMatch(result.summary, /baseline|roster|comparison set/i);

  const gpt = result.models.rows.find((row) => row.model_id === "openai-gpt-5-5");
  assert.ok(gpt.baseline.score < 0);
  assert.ok(gpt.comparison.score > gpt.baseline.score);
  assert.equal(gpt.windows.same_rounds.round_count, result.rounds.shared.length);
  assert.equal(gpt.windows.baseline_only.round_count, result.rounds.baseline_only.length);
});

test("forming sets expose early performance without presenting it as established", () => {
  const baseline = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-05-28");
  const waiting = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-07-10");
  const result = buildBenchmarkSetComparison(apiReadModel, baseline, waiting);
  const swapped = buildBenchmarkSetComparison(apiReadModel, waiting, baseline);

  assert.equal(result.comparison.status, "forming");
  assert.equal(result.comparison.shared_round_count, waiting.comparison.comparison_round_count);
  assert.equal(result.comparison.is_qualified, false);
  assert.match(result.trust_guidance, /more reliable ranking/);
  assert.match(
    result.trust_guidance,
    new RegExp(`needs ${waiting.qualification_threshold - waiting.comparison.comparison_round_count} more`)
  );
  assert.match(swapped.trust_guidance, new RegExp(`Use ${baseline.short_label}`));
  assert.doesNotMatch(swapped.trust_guidance, /established ranking/);
});

test("swapping scored historical sets preserves set-specific conclusions", () => {
  const may28 = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-05-28");
  const june9 = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-06-09");
  const swapped = buildBenchmarkSetComparison(apiReadModel, june9, may28);

  assert.match(swapped.summary, new RegExp(may28.short_label));
  assert.match(swapped.summary, new RegExp(june9.short_label));
  assert.match(swapped.trust_guidance, /Both groups have enough completed rounds/);
  assert.equal(swapped.rounds.comparison_only.length, may28.comparison.comparison_round_count - swapped.rounds.shared.length);
});

test("benchmark-set comparison rejects cross-track or identical selections", () => {
  const weekly = benchmarkSets.find((set) => set.set_id === "weekly-set-2026-05-28");
  const monthly = benchmarkSets.find((set) => set.set_id === "monthly-set-2026-05-28");

  assert.throws(() => buildBenchmarkSetComparison(apiReadModel, weekly, weekly), /must be different/);
  assert.throws(() => buildBenchmarkSetComparison(apiReadModel, weekly, monthly), /same track/);
});
