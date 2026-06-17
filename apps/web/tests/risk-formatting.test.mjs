import assert from "node:assert/strict";
import test from "node:test";
import { signedPulseChangeLabel } from "../src/lib/riskFormatting.js";

test("signedPulseChangeLabel keeps small non-zero pulse moves visible", () => {
  assert.equal(signedPulseChangeLabel(-0.04999999999999716), "-0.05");
  assert.equal(signedPulseChangeLabel(0.04999999999999716), "+0.05");
  assert.equal(signedPulseChangeLabel(-0.004), "0.0");
  assert.equal(signedPulseChangeLabel(0), "0.0");
  assert.equal(signedPulseChangeLabel(-0.55), "-0.6");
  assert.equal(signedPulseChangeLabel(1.24), "+1.2");
  assert.equal(signedPulseChangeLabel(null), "n/a");
});
