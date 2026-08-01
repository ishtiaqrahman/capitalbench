import assert from "node:assert/strict";
import test from "node:test";

import { benchmarkBarCoordinate, buildBenchmarkBarDomain, signedBarBorderRadius } from "../src/lib/benchmarkBars.js";

test("benchmark bar domains retain a zero baseline for positive and negative data", () => {
  const positive = buildBenchmarkBarDomain([0.01, 0.025]);
  const negative = buildBenchmarkBarDomain([-0.01, -0.025]);

  assert.equal(positive.minimum, 0);
  assert.ok(positive.maximum >= 0.025);
  assert.ok(negative.minimum <= -0.025);
  assert.equal(negative.maximum, 0);
});

test("symmetric benchmark domains make paired comparisons share a true scale", () => {
  const domain = buildBenchmarkBarDomain([-0.031, 0.018], { symmetric: true });

  assert.equal(domain.minimum, -domain.maximum);
  assert.ok(domain.ticks.includes(0));
  assert.equal(benchmarkBarCoordinate(0, domain), 50);
});

test("benchmark bar coordinates preserve magnitude instead of rank-normalizing it", () => {
  const domain = { minimum: -0.04, maximum: 0.04, ticks: [-0.04, 0, 0.04] };

  assert.equal(benchmarkBarCoordinate(-0.02, domain), 25);
  assert.equal(benchmarkBarCoordinate(0, domain), 50);
  assert.equal(benchmarkBarCoordinate(0.02, domain), 75);
});

test("signed bar radii keep the zero-axis edge square", () => {
  assert.equal(signedBarBorderRadius(0.02, "vertical", "7px"), "7px 7px 0 0");
  assert.equal(signedBarBorderRadius(-0.02, "vertical", "7px"), "0 0 7px 7px");
  assert.equal(signedBarBorderRadius(0.02, "horizontal", "7px"), "0 7px 7px 0");
  assert.equal(signedBarBorderRadius(-0.02, "horizontal", "7px"), "7px 0 0 7px");
});
