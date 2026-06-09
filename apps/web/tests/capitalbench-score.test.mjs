import assert from "node:assert/strict";
import test from "node:test";
import { capitalBenchScore } from "../src/lib/capitalBenchScore.js";

test("CapitalBench Score captures positive opportunity on a bounded 0-100 scale", () => {
  assert.equal(capitalBenchScore(4.62, 4.62), 100);
  assert.ok(Math.abs(capitalBenchScore(3.93, 4.62) - 85.06493506493507) < 1e-12);
  assert.equal(capitalBenchScore(-2, 4), 0);
  assert.equal(capitalBenchScore(6, 4), 100);
});

test("CapitalBench Score handles a cash-best window", () => {
  assert.equal(capitalBenchScore(0, 0), 100);
  assert.equal(capitalBenchScore(-1, 0), 0);
  assert.equal(capitalBenchScore(Number.NaN, 4), null);
});
