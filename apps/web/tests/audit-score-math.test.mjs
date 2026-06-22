import assert from "node:assert/strict";
import test from "node:test";
import { portfolioReturnValue, scoreLabel } from "../scripts/audit-score-math-helpers.mjs";

test("portfolioReturnValue falls back to selected asset return for legacy single-pick rows", () => {
  assert.equal(
    portfolioReturnValue({
      portfolio_return: "",
      selected_asset_return: "0.067255"
    }),
    0.067255
  );
});

test("portfolioReturnValue prefers explicit portfolio return when present", () => {
  assert.equal(
    portfolioReturnValue({
      portfolio_return: "0.0125",
      selected_asset_return: "0.067255"
    }),
    0.0125
  );
});

test("scoreLabel formats missing scores without throwing", () => {
  assert.equal(scoreLabel(null), "n/a");
});
