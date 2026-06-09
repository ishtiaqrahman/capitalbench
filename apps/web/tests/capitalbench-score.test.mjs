import assert from "node:assert/strict";
import test from "node:test";
import { capitalBenchScore, cumulativeCapitalBenchScore } from "../src/lib/capitalBenchScore.js";

test("CapitalBench Score compares a result directly with the oracle return", () => {
  assert.equal(capitalBenchScore(4.62, 4.62), 100);
  assert.ok(Math.abs(capitalBenchScore(3.93, 4.62) - 85.06493506493507) < 1e-12);
  assert.equal(capitalBenchScore(-2, 4), -50);
  assert.equal(capitalBenchScore(-1, 4), -25);
  assert.equal(capitalBenchScore(6, 4), 100);
});

test("CapitalBench Score handles a cash-best window", () => {
  assert.equal(capitalBenchScore(0, 0), 100);
  assert.equal(capitalBenchScore(-1, 0), null);
  assert.equal(capitalBenchScore(Number.NaN, 4), null);
});

test("cumulative score compares total model return with total oracle return", () => {
  assert.equal(cumulativeCapitalBenchScore([4, 3], [8, 6]), 50);
  assert.equal(cumulativeCapitalBenchScore([4, -1], [8, 2]), 30);
  assert.equal(cumulativeCapitalBenchScore([-1, -2], [2, 4]), -50);
  assert.equal(cumulativeCapitalBenchScore([], []), null);
});
