import assert from "node:assert/strict";
import test from "node:test";

import { orderedComparableBarWidth } from "../src/lib/orderedBarScale.js";

test("higher negative results always receive longer bars", () => {
  const worst = orderedComparableBarWidth(-0.06, -0.06, -0.02);
  const middle = orderedComparableBarWidth(-0.04, -0.06, -0.02);
  const best = orderedComparableBarWidth(-0.02, -0.06, -0.02);

  assert.ok(worst < middle);
  assert.ok(middle < best);
});

test("ordered bars preserve ranking across zero", () => {
  const negative = orderedComparableBarWidth(-0.02, -0.02, 0.03);
  const zero = orderedComparableBarWidth(0, -0.02, 0.03);
  const positive = orderedComparableBarWidth(0.03, -0.02, 0.03);

  assert.ok(negative < zero);
  assert.ok(zero < positive);
});
